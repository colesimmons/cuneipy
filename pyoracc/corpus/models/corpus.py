from typing import Dict, List
from enum import Enum
from pydantic import BaseModel, Field, ConfigDict
import json
from pathlib import Path
from typing import Set


# Good
class GenreEnum(str, Enum):
    ADMINISTRATIVE = "Administrative"
    ASTRONOMICAL = "Astronomical"
    HYMN_PRAYER = "Hymn-Prayer"
    FAKE = "fake (modern)"
    LEGAL = "Legal"
    LETTER = "Letter"
    LEXICAL = "Lexical"
    LEXICAL_SCHOOL = "Lexical; School"
    LITERARY = "Literary"
    LITURGY = "Liturgy"
    MATHEMATICAL = "Mathematical"
    RITUAL = "Ritual"
    ROYAL_INSCRIPTION = "Royal Inscription"
    ROYAL_OR_MONUMENTAL = "Royal/Monumental"
    SCIENTIFIC = "Scientific"
    UNCERTAIN = "uncertain"
    UNSPECIFIED = ""


class LanguageEnum(str, Enum):
    AKKADIAN = "Akkadian"
    NON_SUMERIAN_EBLAITE = "non-Sumerian (Eblaite)"
    NON_SUMERIAN_UNDET = "non-Sumerian (undetermined)"
    SUMERIAN = "Sumerian"
    SUX_AKK_BILINGUAL = "S-A bilingual"
    UNSPECIFIED = ""


class ObjectTypeEnum(str, Enum):
    BARREL = "barrel"
    BRAND = "Brand"
    BRICK = "brick"
    BULLA = "bulla"
    BULLA_2 = "Bulla"
    BULLA_UNCERTAIN = "Bulla (?)"
    CLAY_SEALING = "Clay sealing"
    CONE = "cone"
    CYLINDER = "cylinder"
    CYLINDER_SEAL = "Cylinder Seal"
    CYLINDRICAL_TABLET = "Cylindrical tablet"
    DOOR_SEALING = "Door sealing"
    ENVELOPE_UNCERTAIN = "Envelope (?)"
    ENVELOPE_CLOSED = "Envelope - Closed"
    ENVELOPE_CLOSED_UNCERTAIN = "Envelope - Closed (?)"
    ENVELOPE_FRAGMENT = "Envelope - Fragment"
    ENVELOPE_FRAGMENT_UNCERTAIN = "Envelope - Fragment (?)"
    FAKE = "Fake"
    FAKE_UNCERTAIN = "Fake (?)"
    JAR_SEALING = "Jar sealing"
    LABEL = "Label"
    LABEL_UNCERTAIN = "Label (?)"
    OTHER = "Other"
    OTHER_SEE_REMARKS = "other (see object remarks)"
    PRISM = "prism"
    REPRODUCTION_OR_CAST = "Reproduction or cast"
    REPRODUCTION_OR_CAST_UNCERTAIN = "Reproduction or cast (?)"
    ROUND_TABLET = "Round tablet"
    SEAL = "seal (not impression)"
    SEALING = "sealing"
    TABLET = "tablet"
    TABLET_2 = "Tablet"
    TABLET_AND_ENVELOPE = "tablet & envelope"
    TABLET_AND_ENVELOPE_2 = "Tablet and envelope"
    TABLET_AND_ENVELOPE_3 = "Tablet and Envelope"
    TAG = "tag"
    UNCERTAIN = "Uncertain"
    UNSPECIFIED = ""


class PeriodEnum(str, Enum):
    EARLY_DYNASTIC_I_II = "Early Dynastic I-II"
    EARLY_DYNASTIC_III_A = "Early Dynastic IIIa"
    EARLY_DYNASTIC_III_B = "Early Dynastic IIIb"
    EBLA = "Ebla"
    FAKE = "fake"
    LAGASH_II = "Lagash II"
    MIDDLE_BABYLONIAN = "Middle Babylonian"
    NEO_ASSYRIAN = "Neo-Assyrian"
    NEO_BABYLONIAN = "Neo-Babylonian"
    OLD_AKKADIAN = "Old Akkadian"
    OLD_BABYLONIAN = "Old Babylonian"
    PRE_URUK_V = "Pre-Uruk V"
    UR_III = "Ur III"
    UNCERTAIN = "Uncertain"
    UNKNOWN = "Unknown"
    UNSPECIFIED = ""


class StatusEnum(str, Enum):
    A = "A"
    D = "D"
    I = "I"
    UNSPECIFIED = ""


class SupergenreEnum(str, Enum):
    ELA = "ELA"
    LEX = "LEX"
    LIT = "LIT"
    STL = "STL"
    UNKNOWN = "unknown"
    UNKNOWN_2 = "UNK"
    UNSPECIFIED = ""


class XProjectEnum(str, Enum):
    CDLI = "CDLI"


# TODO
class SubgenreEnum(str, Enum):
    ADMINISTRATIVE = "administrative"
    ADMINISTRATIVE_2 = "Administrative"
    ASJ = "ASJ 8, 107 27"
    BUILDING_FLOOR_PLAN = "building floor plan"
    BULLA = "bulla"
    CONTRACT = "contract"
    CONTRACT_UNCERTAIN = "contract ?"
    DITILLA = "ditilla"
    COMPOSITE = "composite"
    COMPOSITE_SEAL_ROYAL = "composite seal, royal"
    DEBATE_POEMS = "Debate poems"
    EXERCISE = "exercise"
    EXERCISE_2 = "Exercise"
    FIELD_PLAN = "field plan (drawing)"
    JUDGEMENT = "judgement"
    GABA_RI = "gaba-ri"
    HYMNS_TO_DEITIES = "Hymns addressed to deities//Inana"
    HOUSE_PURCHASE = "house purchase"
    LEGAL_DOCUMENT = "Legal document"
    LEGAL_DOCUMENT_ORDAL = 'Legal document: ""Ordal'
    LEGAL_DOCUMENT_GUARANTEE = "Legal document: guarantee"
    LEGAL_DOCUMENT_PURCHASE = "Legal document: purchase"
    LEGAL_DOCUMENT_UNCERTAIN = "Legal document?"
    LETTER_ORDER = "letter order"
    LIST_OF_OFFERINGS = "List of offerings"
    LIST_OF_OFFERINGS_UNCERTAIN = "List of offerings?"
    LOAN = "Loan"
    LOAN_2 = "loan"
    MAEKAWA = "Maekawa, ASJ 17, 184, no. 108"
    MESSENGER = "messenger"
    MESSENGER_TEXT = "messenger text"
    MESSENGER_TEXT_2 = "Messenger text"
    MESSENGER_TEXT_W_GABA_RI = "messenger text w/ gaba-ri"
    METRO_MATHEMATICAL = "metro-mathematical"
    MODEL_CONTRACTS = "model contracts"
    OTHER_LETTERS = "Other letters and letter-prayers"
    PHYSICAL_CYLINDER_SEAL = "physical cylinder seal"
    PHYSICAL_SEAL_ROYAL = "physical seal, royal"
    PISAN_DUB = "pisan-dub"
    PISAN_DUB_BA = "pisan-dub-ba"
    PISAN_DUB_BA_W_GABA_RI = "pisan-dub-ba w/ gaba-ri"
    PROVERB_COLLECTIONS = "Proverb collections"
    SALE_CONTRACT = "sale contract"
    SALE_CONTRACT_FIELD = "sale contract, field"
    SALE_CONTRACT_HOUSE = "sale contract, house"
    SALE_CONTRACT_UNCERTAIN = "sale contract ?"
    SIA_ARCHIVE = "SI.A-a archive"
    STRINGED_BULLA = "stringed bulla"
    SURUPPAK_LIST = "Šuruppak List of Personal Names and Professions"
    TABULAR_ACCOUNT = "tabular account"
    TRIANGLE_TAG = "triangle tag"
    UNSPECIFIED = ""


class Text(BaseModel):
    model_config = ConfigDict(extra="forbid")

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


class Corpus(BaseModel):
    texts: List[Text] = []

    @classmethod
    def load(cls, dir: str) -> "Corpus":
        catalogue_path = Path(dir) / "catalogue.json"
        with open(catalogue_path) as f:
            catalogue = json.load(f)
        texts = []
        for text_data in catalogue["members"].values():
            text = Text(**text_data)
            texts.append(text)
        return cls(texts=texts)

    def get_unique_values(self) -> Dict[str, Set[str]]:
        whitelist = {"subgenre"}
        unique_values = {}
        for text in self.texts:
            for field in text.model_fields:
                if field not in whitelist:
                    continue
                if field not in unique_values:
                    unique_values[field] = set()
                unique_values[field].add(getattr(text, field))
        return unique_values

    # catalogue.json
    # Very useful!

    # corpus.json
    # Not really useful. Just tells you what files are in corpusjson.

    # gloss-qpn.json
    # QPN: Oracc Linguistic Annotation for Proper Nouns
    # http://oracc.museum.upenn.edu/doc/help/languages/propernouns/index.html

    # gloss-sux.json
    # SUX: Oracc Linguistic Annotation for Sumerian
    # http://oracc.museum.upenn.edu/doc/help/languages/sumerian/index.html

    # "The index-xxx.json files are exports of a subset of the index data created and used by the Oracc search engine,
    # giving the keys the indexer has generated from the input words and the locations in which they occur in the corpus."
    # http://oracc.museum.upenn.edu/doc/opendata/json/index.html
    # index-cat.json
    # index-lem.json
    # index-qpn.json
    # index-sux.json
    # index-tra.json
    # index-txt.json

    # Tells you what formats are available
    # metadata.json
    # sortcodes.json
