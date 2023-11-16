import json
from typing import List, Dict, Any, Optional, Union

from pydantic import BaseModel, Field, ConfigDict

from pyoracc.corpus.enums import (
    GenreEnum,
    LanguageEnum,
    ObjectTypeEnum,
    PeriodEnum,
    StatusEnum,
    SupergenreEnum,
    XProjectEnum,
)
from pyoracc.corpus.models.text_data import (
    CDLNode,
    Chunk,
    Discontinuity,
    Lemma,
    LLNode,
    LinkbaseNode,
)


class Text(BaseModel):
    # TODO: Find out how often below fields are defined
    model_config = ConfigDict(extra="forbid")
    dir_path: str

    cdl: List[CDLNode] = []

    # Metadata
    id_text: str
    language: LanguageEnum = LanguageEnum.UNSPECIFIED
    object_type: ObjectTypeEnum = ObjectTypeEnum.UNSPECIFIED
    period: PeriodEnum = PeriodEnum.UNSPECIFIED

    # Genre
    genre: GenreEnum = GenreEnum.UNSPECIFIED
    # subgenre: SubgenreEnum = SubgenreEnum.UNSPECIFIED
    subgenre: str = ""
    supergenre: SupergenreEnum = SupergenreEnum.UNSPECIFIED

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
    status: StatusEnum = StatusEnum.UNSPECIFIED
    trans: List[str] = []
    uri: str = ""
    xproject: XProjectEnum = ""

    # Less standard
    acquisition_history: str = ""
    ark_number: str = ""
    atf_source: str = ""
    atf_up: str = ""
    author: str = ""
    author_remarks: str = ""
    cdli_comments: str = ""
    chap: str = ""
    citation: str = ""
    collection: str = ""
    date_entered: str = ""
    date_remarks: str = ""
    date_updated: str = ""
    dates_referenced: str = ""
    db_source: str = ""
    designation: str = ""
    distribution: str = ""
    electronic_publication: str = ""
    external_id: str = ""
    google_earth_collection: str = ""
    height: str = ""
    id_: str = Field("", alias="id")
    id_composite: str = ""
    id_text_int: str = ""
    id_text: str = ""
    keywords: str = ""
    lineart_up: str = ""
    material: str = ""
    object_remarks: str = ""
    photo_up: str = ""
    place: str = ""
    primary_edition: str = ""
    provdist: str = ""
    provenience_remarks: str = ""
    publication_date: str = ""
    published_collation: str = ""
    ruler: str = ""
    sec1: str = ""
    sec2: str = ""
    seal_id: str = ""
    seal_information: str = ""
    sources: str = ""
    subgenre_remarks: str = ""
    thickness: str = ""
    translation_source: str = ""
    width: str = ""

    # TODO: are there members in catalogue that aren't in corpusjson/?
    # TODO: are there files in corpusjson/ that aren't in catalogue?
    # TODO: use timestamp
    def load_contents(self) -> None:
        if not self.id_text:  # TODO
            self.cdl = []
            return

        text_path = f"{self.dir_path}/{self.id_text}.json"
        with open(text_path) as f:
            text_data = json.load(f)
        self.cdl = [parse_node(node) for node in text_data["cdl"]]
        # self.cdl = text_data["cdl"]
        return text_data


def parse_node(node):
    node_type = node.get("node", "")

    if "cdl" in node:
        node["cdl"] = [parse_node(n) for n in node["cdl"]]

    if node_type == "c":
        return Chunk(**node)
    elif node_type == "d":
        return Discontinuity(**node)
    elif node_type == "l":
        return Lemma(**node)
    elif node_type == "ll":
        return LLNode(**node)
    elif "linkbase" in node:
        return LinkbaseNode(**node)
    else:
        raise ValueError(f"Unknown node type: {node_type}")
