"""
Defines the base class for all text models.

These are attributes shared by texts in all corpora.
"""

import json
import re
from enum import Enum
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

special_token_format = r"#[\S]*?#"


# can't use <...> because that already represents something in the translits
class SpecialToken(Enum):
    MISSING = "#MISSING#"
    BLANK_SPACE = "#BLANK_SPACE#"
    COLUMN = "#COLUMN#"
    RULING = "#RULING#"
    SURFACE = "#SURFACE#"
    LINE_START = "\n"


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

        def _without_special_tokens(text: str) -> str:
            text = re.sub(special_token_format, "", text)
            text = text.replace("\n", "")
            text = text.replace(" ", "")
            return text

        tokens, langs = _crawl_cdl_for_text(self.cdl)
        self.langs = ", ".join(sorted(list(langs)))
        text = " ".join(tokens)

        # Only include surfaces if there are non-special tokens
        surfaces = text.split(SpecialToken.SURFACE.value)
        surfaces = [surface.strip() for surface in surfaces]
        surfaces = [surface for surface in surfaces if _without_special_tokens(surface)]

        text = ""
        if surfaces:
            join_with = f"\n{SpecialToken.SURFACE.value}\n"
            text = f"{SpecialToken.SURFACE.value}\n" + join_with.join(surfaces)

        text = re.sub(r"\ *\n\ *", "\n", text)  # remove spaces around newlines
        text = re.sub(r"\n+", "\n", text)  # remove multiple newlines
        text = re.sub(r"\ +", " ", text)  # remove multiple spaces
        return text.strip()


def _discontinuity_to_text(node: Discontinuity) -> Optional[str]:
    if node.type_ == DiscontinuityType.OBJECT:
        return None
    if node.type_ == DiscontinuityType.LINE_START:
        return "\n"
    if node.type_ == DiscontinuityType.COLUMN:
        return f"\n{SpecialToken.COLUMN.value}\n"
    if node.type_ == DiscontinuityType.SURFACE:
        return SpecialToken.SURFACE.value

    if node.state == "missing":
        return f"\n{SpecialToken.MISSING.value}\n"
    if node.state == "blank":
        if node.scope == "line":
            return f"\n{SpecialToken.MISSING.value}\n"
        if node.scope == "space":
            return f"\n{SpecialToken.BLANK_SPACE.value}\n"
        return None
    if node.state == "ruling":
        return f"\n{SpecialToken.RULING.value}\n"

    return None


def _extract_text_from_node(node: CDLNode) -> Optional[str]:
    if type(node) == Discontinuity:
        return _discontinuity_to_text(node)
    if type(node) == Lemma:
        text = node.frag if node.frag else node.f.get("form", "")

        # This is not the most precise, but it'll do...
        # The "text" above often excludes opening or closing brackets
        # in conjunction with parentheses or 'n', causing them to be unbalanced.
        # This is a compromise between precision and not introducing more bugs.
        ideal_bracket_seq = ""
        for item in node.f.get("gdl", []):
            for subitem in item.get("seq", []) + item.get("group", []):
                ideal_bracket_seq += "[" if subitem.get("breakStart") else ""
                ideal_bracket_seq += "]" if subitem.get("breakEnd") else ""
            ideal_bracket_seq += "[" if item.get("breakStart") else ""
            ideal_bracket_seq += "]" if item.get("breakEnd") else ""

        # No brackets
        if not ideal_bracket_seq:
            return text

        actual_bracket_seq = "".join([char for char in text if char in "[]"])

        # It's got em all
        if ideal_bracket_seq == actual_bracket_seq:
            return text

        # It's missing some
        # -------------------
        # 1. Simple open-and-shut
        if ideal_bracket_seq.startswith("[") and ideal_bracket_seq.endswith("]"):
            # This is designed to handle seqs like "abc]-def-[ghi]"
            if not actual_bracket_seq.startswith("["):
                text = "[" + text
            if not actual_bracket_seq.endswith("]"):
                text = text + "]"
            # But there are still possible seqs like "abc]-[1(diš)-[ghi]"
            # So if we still don't have it, just throw out all the nuance
            # and wrap the whole thing.
            actual_bracket_seq = "".join([char for char in text if char in "[]"])
            if ideal_bracket_seq == actual_bracket_seq:
                return text
            text = text.replace("[", "").replace("]", "")
            return "[" + text + "]"

        # 2. Starts w/ closing
        if ideal_bracket_seq.startswith("]") and not actual_bracket_seq.startswith("]"):
            first_open_bracket_idx = text.find("[")
            if first_open_bracket_idx == -1:
                text = text + "]"
            else:
                text = (
                    text[:first_open_bracket_idx] + "]" + text[first_open_bracket_idx:]
                )

        # 3. Ends w/ opening
        if ideal_bracket_seq.endswith("[") and not actual_bracket_seq.endswith("["):
            first_close_bracket_idx = text.find("]")
            if first_close_bracket_idx == -1:
                text = "[" + text
            else:
                text = (
                    text[:first_close_bracket_idx]
                    + "["
                    + text[first_close_bracket_idx:]
                )

        # See if we got it now...
        actual_bracket_seq = "".join([char for char in text if char in "[]"])
        if ideal_bracket_seq == actual_bracket_seq:
            return text

        # Still no?!
        text = text.replace("[", "").replace("]", "")
        if "[]" in ideal_bracket_seq:
            text = "[" + text + "]"
        if ideal_bracket_seq.startswith("["):
            text = "[" + text
        if ideal_bracket_seq.endswith("]"):
            text += "]"
        return text

    return None


def _extract_lang_from_node(node: CDLNode) -> set:
    if type(node) == Lemma:
        return node.f.get("lang", "")
    return ""


def _crawl_cdl_for_text(cdl: List[CDLNode]) -> List[str]:
    current_tokens: List[str] = []
    langs = set()

    for node in cdl:
        if type(node) == Chunk:
            tokens, langs_ = _crawl_cdl_for_text(node.cdl)
            current_tokens += tokens
            langs |= langs_
        else:
            text = _extract_text_from_node(node)
            lang = _extract_lang_from_node(node)
            if text:
                current_tokens.append(text)
            if lang:
                langs.add(lang)

    return current_tokens, langs
