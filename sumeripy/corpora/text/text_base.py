"""
Defines the base class for all text models.

These are attributes shared by texts in all corpora.
"""

import json
from typing import List

from pydantic import BaseModel, ConfigDict
from .cdl import CDLNode, parse_cdl_node
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
        if not self.id_text:  # TODO
            self.cdl = []
            return

        text_path = f"{self.dir_path}/{self.id_text}.json"
        with open(text_path, "r", encoding="utf-8") as f:
            text_data = json.load(f)
        self.cdl = [parse_cdl_node(node) for node in text_data["cdl"]]
        return text_data
