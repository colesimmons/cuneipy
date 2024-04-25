"""
Defines the base class for all text models.

These are attributes shared by texts in all corpora.
"""

import json
import re
from typing import List, Optional

from pydantic import BaseModel, ConfigDict

from .cdl import CDLNode, Chunk, Discontinuity, DiscontinuityType, Lemma, parse_cdl_node
from .enums import (
    Genre,
    Language,
    ObjectType,
    Period,
    Status,
    Supergenre,
    XProject,
)


class TextBase(BaseModel):
    model_config = ConfigDict(extra="forbid")  # TODO add this to other models
    dir_path: str

    cdl: List[CDLNode] = []

    # Metadata
    id_text: str = ""
    designation: str = ""  # almost always defined
    language: Language = Language.UNSPECIFIED
    object_type: ObjectType = ObjectType.UNSPECIFIED
    period: Period = Period.UNSPECIFIED

    # Genre
    genre: Genre = Genre.UNSPECIFIED
    # subgenre: Subgenre = Subgenre.UNSPECIFIED # TODO
    subgenre: str = ""
    supergenre: Supergenre = Supergenre.UNSPECIFIED

    # Provenience
    excavation_no: str = ""
    museum_no: str = ""
    primary_publication: str = ""
    provenience: str
    publication_history: str = ""

    # Other
    accession_no: str = ""
    bdtns_id: str = ""
    date_of_origin: str = ""
    designation: str
    images: List[str] = []
    langs: str = ""
    project: str
    public: str = ""  # '', 'no'
    status: Status = Status.UNSPECIFIED
    trans: List[str] = []
    uri: str = ""
    xproject: XProject = XProject.UNSPECIFIED

    @property
    def file_id(self) -> str:
        return self.id_text

    # TODO: are there members in catalogue that aren't in corpusjson/?
    # TODO: are there files in corpusjson/ that aren't in catalogue?
    # TODO: use timestamp
    def load_contents(self) -> None:
        """
        Load the contents of the text from a JSON file.

        If the `id_text` attribute is not set, the `cdl` attribute will be set to an empty list.

        Returns:
            None
        """

        if not self.file_id:
            raise ValueError("no file id: ", self.model_dump())

        text_path = f"{self.dir_path}/{self.file_id}.json"
        with open(text_path, "r", encoding="utf-8") as f:
            text_data = json.load(f)
        self.cdl = [parse_cdl_node(node) for node in text_data["cdl"]]

    def transliteration(self) -> str:
        """
        Return the transliteration of the text.

        Returns:
            str: The transliteration of the text.
        """
        tokens = _crawl_cdl_for_text(self.cdl)
        text = " ".join(tokens)
        surfaces = text.split("==SURFACE==")
        surfaces = [surface.strip() for surface in surfaces if surface.strip()]

        text = ("==SURFACE==\n" + "\n==SURFACE==\n".join(surfaces)) if surfaces else ""
        text = re.sub(r"\ *\n\ *", "\n", text)
        text = re.sub(r"\n+", "\n", text)
        text = re.sub(r"\ +", " ", text)
        return text.strip()


def _discontinuity_to_text(node: Discontinuity) -> Optional[str]:
    if node.type_ == DiscontinuityType.OBJECT:
        return None
    if node.type_ == DiscontinuityType.LINE_START:
        return "\n"
    if node.type_ == DiscontinuityType.COLUMN:
        return "\n==COLUMN==\n"
    if node.type_ == DiscontinuityType.SURFACE:
        return "==SURFACE=="

    if node.state == "missing":
        return "\n==MISSING==\n"
    if node.state == "blank":
        if node.scope == "line":
            return "\n==MISSING==\n"
        if node.scope == "space":
            return "\n==BLANK_SPACE==\n"
        return None
    if node.state == "ruling":
        return "\n==RULING==\n"

    return None


def _extract_text_from_node(node: CDLNode) -> Optional[str]:
    if type(node) == Discontinuity:
        return _discontinuity_to_text(node)
    if type(node) == Lemma:
        text = node.frag
        gdl = node.f.get("gdl", [])
        # This is not the most precise, but it'll do...
        # Otherwise, we end up with unbalanced brackets
        # and there's not an easy way around that without potentially
        # introducing many more bugs.
        if any("breakStart" in node for node in gdl):
            if "[" not in text:
                text = f"[{text}"
        if any("breakEnd" in node for node in gdl):
            if "]" not in text:
                text = f"{text}]"
        return text

    return None


def _crawl_cdl_for_text(cdl: List[CDLNode]) -> List[str]:
    current_tokens: List[str] = []

    for node in cdl:
        if type(node) == Chunk:
            tokens = _crawl_cdl_for_text(node.cdl)
            current_tokens += tokens
        else:
            text = _extract_text_from_node(node)
            if text:
                current_tokens.append(text)

    return current_tokens
