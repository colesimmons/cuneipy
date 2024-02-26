"""
Defines the base class for all text models.

These are attributes shared by texts in all corpora.
"""

import json
from typing import List, Optional
import re

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

        # Drop empty surfaces
        surfaces = text.split("$SURFACE$")
        surfaces = [s.strip() for s in surfaces if s.strip()]

        # Drop the first line start, replace others with newlines
        surface_texts = []
        for surface in surfaces:
            # If it starts with "$LINE$", drop it
            # if surface.startswith("$LINE$"):
                #surface = surface[6:]
            surface = surface.replace("$LINE$", "\n")
            surface_texts.append("==SURFACE== \n" + surface)

        new_text = "\n".join(surface_texts)

        # Replace any repeated sequence of " \n " with a single " \n "
        new_text = re.sub(r"( *\n+ *)+", " \n ", new_text)
        return new_text.strip()


def _discontinuity_to_text(node: Discontinuity) -> Optional[str]:
    if node.type_ == DiscontinuityType.LINE_START:
        return "$LINE$"
    elif node.type_ == DiscontinuityType.COLUMN:
        # return "$COL$"
        return None
    elif node.type_ == DiscontinuityType.SURFACE:
        return "$SURFACE$ "
    elif node.state == "missing" and node.scope == "line":
        return "\n $MISSING_LINES$ \n"
    return None

def _extract_text_from_node(node: CDLNode) -> Optional[str]:
    if type(node) == Discontinuity:
        return _discontinuity_to_text(node)
    if type(node) == Lemma:
        if node.frag:
            return node.frag
        # Going to have to pull it off the gdl
        if node.f and node.f['form']:
            return node.f['form']
        raise ValueError(f"Could not find text for lemma node: {node}")

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
