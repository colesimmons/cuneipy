"""
"""
from enum import Enum
from datetime import datetime
from pydantic import BaseModel as PydanticBaseModel, Field, ConfigDict


class BaseModel(PydanticBaseModel):
    """Forbid extra keys"""

    model_config = ConfigDict(extra="forbid")


class OraccFileBase(BaseModel):
    """Base schema for ePSD files"""

    type: str = Field(..., alias="type", description="", example="corpus")
    project: str = Field(..., alias="project", description="", example="epsd2")
    source: str = Field(
        ..., alias="source", description="", example="http://oracc.org/epsd2"
    )
    license: str = Field(
        ...,
        alias="license",
        description="",
        example="This data is released under the CC0 license",
    )
    license_url: str = Field(
        ...,
        alias="license-url",
        description="",
        example="https://creativecommons.org/publicdomain/zero/1.0/",
    )
    more_info: str = Field(
        ...,
        alias="more-info",
        description="",
        example="http://oracc.org/doc/opendata/",
    )
    timestamp: datetime = Field(
        ...,
        alias="UTC-timestamp",
        description="",
        example="2021-12-21T03:21:44",
    )


class OccurrenceStatsMixin(PydanticBaseModel):
    """
    Occurrence statistics
    """

    # Occurrence data
    count: int = Field(..., alias="icount", description="Instance count", example=1333)
    percent_of_instances: int = Field(
        ..., alias="ipct", description="Instance percentage", example=100
    )


class PartOfSpeechEnum(str, Enum):
    """
    Part of Speech values.

    The count represents the number of items in the glossary with that part of speech.

    Note: the count does not reflect the number of times those items occur in the corpus,
    nor the number of times they are used as an effective part of speech.

    Standard POS tags:

    POS tags for proper nouns:
    """

    ############################
    # BASIC WORD CLASSES
    # http://oracc.museum.upenn.edu/doc/help/languages/akkadian/index.html
    ############################
    ADJECTIVE = "AJ"
    """Adjective

    Glossary count: 267

    Examples:
    - asaŋ[~flour]AJ
    - huldiŋ[rotten]AJ
    - hulutag[useless]AJ
    - pešŋal[mighty?]AJ
    - sala[bug-ridden]AJ
    """

    ADVERB = "AV"
    """Adverb

    Includes:
    - temporal adverbs (e.g.: inanna[now], anumma[now//herewith], šattišam[yearly])
    - interrogative adverbs (e.g.: ali[where?], ammīni[why?], kī[how?], mati[when?])
    - demonstrative adverbs (e.g.: kīam[thus])

    Glossary count: 7

    Examples:
    - abaraša[truly]AV
    - ahiaš[quickly]AV
    - hur[ever]AV
    - tukundi[quickly]AV
    """

    NOUN = "N"
    """Noun

    Glossary count: 7830

    Examples:
    - harhar[bird]N
    - kib[wheat]N
    - kirihaš[disease]N
    - nunus[woman]N
    - zazaga[flour]N
    """

    NUMBER = "NU"
    """Number

    Glossary count: 60

    Examples:
    - aš[one]NU
    - nimuš[three]NU
    - ninnu[fifty]NU
    - udili[ten]NU
    - šargal[216000]NU
    """

    VERB_INTRANSITIVE = "V/i"
    """Intransitive verb

    Glossary count: 434

    Examples:
    - buluh[vomit]V/i
    - dirig[fall]V/i
    - heše[oppressed]V/i
    - rib[surpassing]V/i
    - ul[swell]V/i
    """

    VERB_TRANSITIVE = "V/t"
    """Transitive verb

    Glossary count: 1058

    Examples:
    - gilim[cross]V/t
    - kigaŋ[love]V/t
    - ma[burn]V/t
    - paŋ[breathe]V/t
    - šeš[weep]V/t
    """

    ############################
    # PRONOUNS
    # http://oracc.museum.upenn.edu/doc/help/languages/akkadian/index.html
    ############################
    DEMONSTRATIVE_PRONOUN = "DP"
    """Demonstrative pronoun

    Glossary count: 5

    Examples:
    - ne[this]DP
    - nen[this]DP
    - re[that]DP
    - ullia[those]DP
    """

    INDEPENDENT_PRONOUN = "IP"
    """Independent/anaphoric pronoun

    Glossary count: 10

    Examples:
    - ane[he]IP
    - anene[they]IP
    - menden[we]IP
    - menzen[you]IP
    - ur[he]IP
    """

    INTERROGATIVE_PRONOUN = "QP"
    """Interrogative pronoun

    Glossary count: 20

    Examples:
    - ana[what?]QP
    - anaš[why?]QP
    - inešgin[how]QP
    - mea[where?]QP
    - meta[whence?]QP
    """

    REFLEXIVE_PRONOUN = "RP"
    """Reflexive pronoun

    Glossary count: 2

    Examples:
    - ni[self]RP
    """

    ############################
    # PROPER NOUNS
    # http://oracc.museum.upenn.edu/doc/help/languages/propernouns/index.html
    ############################

    CELESTIAL_NAME = "CN"
    """Celestial name (proper noun)

    Glossary count: 48

    Numeric guide words clarify when a name is used to refer to
    the same or different entities.

    Examples:
    - Allub[1]CN
    - Balaŋ[Drum]CN
    - Ellaŋ[1]CN
    - Gagpan[1]CN
    - Muš[Snake]CN
    """

    DIVINE_NAME = "DN"
    """Divine name (proper noun)

    Glossary count: 2879

    Numeric guide words clarify when a name is used to refer to
    the same or different entities.

    Examples:
    - Ki'ursaŋene[0]DN
    - ME-hursaŋ[1]DN
    - Marutukka[1]DN
    - Ŋešbara[1]DN
    - Šitatarru[1]DN
    """

    ETHNOS_NAME = "EN"
    """Ethnos name (proper noun)

    Glossary count: 8

    Numeric guide words clarify when a name is used to refer to
    the same or different entities.

    Examples:
    - Kaššu[Kassite]EN
    - Martu[1]EN
    - Tidnum[1]EN
    - akkadu[Akkadian]EN
    - Šimaški[1]EN
    """

    FIELD_NAME = "FN"
    """Field name (proper noun)

    Glossary count: 5

    Numeric guide words clarify when a name is used to refer to
    the same or different entities.

    Examples:
    - Ambartur[0]FN
    - Anašezi[1]FN
    - Gibanda[0]FN
    - Tulamušenu[1]FN
    """

    GEOGRAPHICAL_NAME = "GN"
    """Geographical name (proper noun)
    
    Lands and other geographical entities without their own tag.

    Glossary count: 2

    Numeric guide words clarify when a name is used to refer to
    the same or different entities.

    Examples:
    - Garta[0]GN
    - Ibrat[0]GN
    - Kureren[1]GN
    - Mutiabala[0]GN
    - Zabšali[1]GN
    """

    LINEAGE_NAME = "LN"
    """Lineage name (proper noun)

    Glossary count: 2

    Numeric guide words clarify when a name is used to refer to
    the same or different entities.

    Examples:
    - Ekur-zakir[1]LN
    - Nur-Šamaš[1]LN
    """

    MONTH_NAME = "MN"
    """Month name (proper noun)

    Glossary count: 121

    Numeric guide words clarify when a name is used to refer to
    the same or different entities.

    Examples:
    - Akiti[1]MN
    - Ezemšulgirak[1]MN
    - Inanaṣarbat[1]MN
    - Šueša[1]MN
    - Šumsala[1]MN
    """

    PERSONAL_NAME = "PN"
    """Personal name (proper noun)

    Glossary count: 1342

    Numeric guide words clarify when a name is used to refer to
    the same or different entities.

    Examples:
    - Lugalanatum[1]PN
    - Mešbarag[1]PN
    - Šuerra[4]PN
    - Šulgirili[3]PN
    - Šulgiririŋu[1]PN
    """

    QUARTER_NAME = "QN"
    """City area (proper noun)

    Glossary count: 3

    Numeric guide words clarify when a name is used to refer to
    the same or different entities.

    Examples:
    - Baltil[1]QN
    - Eridug[3]QN
    - Šuanna[1]QN
    """

    ROYAL_NAME = "RN"
    """Royal name (proper noun)

    Glossary count: 331

    Numeric guide words clarify when a name is used to refer to
    the same or different entities.

    Examples:
    - Enbieštar[1]RN
    - Enlilpabilgagi[0]RN
    - Enmenduranak[1]RN
    - Lugalŋu[1]RN
    - Singamil[1]RN
    """

    SETTLEMENT_NAME = "SN"
    """Settlement name (proper noun)

    Glossary count: 379

    Numeric guide words clarify when a name is used to refer to
    the same or different entities.

    Examples:
    - Aššu[1]SN
    - Kazallu[1]SN
    - Mari[1]SN
    - Maškan-Šapir[1]SN
    - Zugulme[1]SN
    """

    TEMPLE_NAME = "TN"
    """Temple name (proper noun)

    Glossary count: 486

    Numeric guide words clarify when a name is used to refer to
    the same or different entities.

    Examples:
    - Aneŋara[1]TN
    - Ekitušakkile[1]TN
    - Enammah[1]TN
    - Kitušakkile[0]TN
    - Ŋešbanda[1]TN
    """

    WATERCOURSE_NAME = "WN"
    """Watercourse name (proper noun)

    Glossary count: 183

    Numeric guide words clarify when a name is used to refer to
    the same or different entities.

    Examples:
    - Agibil[0]WN
    - Idnunananna[1]WN
    - Idnunkug[1]WN
    - Narsina[1]WN
    - Ursaŋani[1]WN
    """

    ############################
    # OTHER
    # http://oracc.museum.upenn.edu/doc/help/languages/akkadian/index.html
    ############################

    CONJUNCTION = "CNJ"
    """Conjunction

    Glossary count: 8

    Examples:
    - enna[until]CNJ
    - he[whether]CNJ
    - tukum[if]CNJ
    - tukumbi[if]CNJ
    - uda[if]CNJ
    """

    INTERJECTION = "J"
    """Interjection

    Glossary count: 21

    Examples:
    - ale'aya[cry]J
    - a'u[exclamation]J
    - ili[exclamation]J
    - inanna[entreaty]J
    - me'am[dear]J
    """

    MA = "MA"
    """?

    Glossary count: 24

    Examples:
    - adal[exclamation]MA
    - angam[consequently]MA
    - ineš[now]MA
    - inešta[henceforth]MA
    - udmeda[ever]MA
    """

    O = "O"
    """?

    Glossary count: 10

    Examples:
    - e'en[so]O
    - ganame[surely]O
    - ginam[like]O
    - nanna[without]O
    - nenam[so]O
    """

    PREPOSITION = "PRP"
    """Preposition

    Glossary count: 1

    Examples:
    - ki[with]PRP
    """

    UNKNOWN = "U"
    """Unknown 

    Glossary count: 4

    Examples:
    - budug[unmng]U
    - rib[unmng]U
    """


class PeriodEnum(str, Enum):
    """
    Periods of the Sumerian language.
    """

    EARLY_DYNASTIC_I_II = "Early Dynastic I-II"
    """2900-2700 BCE"""

    EARLY_DYNASTIC_IIIA = "Early Dynastic IIIa"
    """2600-2500 BCE"""

    EARLY_DYNASTIC_IIIB = "Early Dynastic IIIb"
    """2500-2340 BCE"""

    EBLA = "Ebla"
    """2350-2250 BCE"""

    OLD_AKKADIAN = "Old Akkadian"
    """2300-2200 BCE"""

    LAGASH_II = "Lagash II"
    """2200-2100 BCE"""

    UR_III = "Ur III"
    """2100-2000 BCE"""

    OLD_BABYLONIAN = "Old Babylonian"
    """2000-1600 BCE"""

    MIDDLE_BABYLONIAN = "Middle Babylonian"
    """1400-1100 BCE"""

    MIDDLE_ASSYRIAN = "Middle Assyrian"
    """1400-1000 BCE"""

    NEO_ASSYRIAN = "Neo-Assyrian"
    """911-612 BCE"""

    NEO_BABYLONIAN = "Neo-Babylonian"
    """626-539 BCE"""

    PERSIAN = "Persian"
    """547-331 BCE"""

    HELLENISTIC = "Hellenistic"
    """323-63 BCE"""

    UNCERTAIN = "Uncertain"
    """Uncertain period"""

    UNKNOWN = "unknown"
    """Unknown period"""
