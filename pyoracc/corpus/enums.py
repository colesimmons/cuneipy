from enum import Enum


class CorpusType(Enum):
    """
    Enum class representing the available corpora in the ORACC project.
    """

    ED12 = "ed12"
    ED3A = "ed3a"
    ED3B = "ed3b"
    EBLA = "ebla"
    OAKK = "oakk"
    UR3 = "ur3"
    LAGASH2 = "lagash2"
    OLDBAB = "oldbab"
    EARLYLIT = "earlylit"
    LITERARY = "literary"
    ROYAL = "royal"
    PRAXIS = "praxis"
    PRAXIS_UDUGHUL = "praxis_udughul"
    PRAXIS_VARIA = "praxis_varia"

    def get_download_url(self):
        """
        Returns the download URL for the given corpus.

        Raises:
          ValueError: If the corpus is invalid.
        """
        if self is CorpusType.ED12:
            return "http://oracc.museum.upenn.edu/json/epsd2-admin-ed12.zip"
        elif self is CorpusType.ED3A:
            return "http://oracc.museum.upenn.edu/json/epsd2-admin-ed3a.zip"
        elif self is CorpusType.ED3B:
            return "http://oracc.museum.upenn.edu/json/epsd2-admin-ed3b.zip"
        elif self is CorpusType.EBLA:
            return "http://oracc.museum.upenn.edu/json/epsd2-admin-ebla.zip"
        elif self is CorpusType.OAKK:
            return "http://oracc.museum.upenn.edu/json/epsd2-admin-oakk.zip"
        elif self is CorpusType.UR3:
            return "http://oracc.museum.upenn.edu/json/epsd2-admin-ur3.zip"
        elif self is CorpusType.LAGASH2:
            return "http://oracc.museum.upenn.edu/json/epsd2-admin-lagash2.zip"
        elif self is CorpusType.OLDBAB:
            return "http://oracc.museum.upenn.edu/json/epsd2-admin/oldbab.zip"
        elif self is CorpusType.EARLYLIT:
            return "http://oracc.museum.upenn.edu/json/epsd2-earlylit.zip"
        elif self is CorpusType.LITERARY:
            return "http://oracc.museum.upenn.edu/json/epsd2-literary.zip"
        elif self is CorpusType.ROYAL:
            return "http://oracc.museum.upenn.edu/json/epsd2-royal.zip"
        elif self is CorpusType.PRAXIS:
            return "http://oracc.museum.upenn.edu/json/epsd2-praxis.zip"
        elif self is CorpusType.PRAXIS_UDUGHUL:
            return "http://oracc.museum.upenn.edu/json/epsd2-praxis-udughul.zip"
        elif self is CorpusType.PRAXIS_VARIA:
            return "http://oracc.museum.upenn.edu/json/epsd2-praxis-varia.zip"
        else:
            raise ValueError("Invalid corpus")


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
