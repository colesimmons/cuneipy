"""
"""
from typing import Any, Dict, List
from pydantic import Field, model_validator
from pyoracc.epsd2.models.utils import (
    BaseModel,
    OraccFileBase,
    PeriodEnum,
    PartOfSpeechEnum,
    OccurrenceStatsMixin,
)
from pyoracc.epsd2.utils import load_json


class _Base(BaseModel, OccurrenceStatsMixin):
    """
    Rather than use the term 'root' we use the term 'base' to indicate
    the portion of a word-form that writes the word itself
    rather than any attached morphological markers.

    Two special notations are used for Sumerian bases for situations where a single grapheme combines morphology and base.
    When the first part of the grapheme is morphological and the second part belongs to the base,
    we separate them with the degree symbol, °, as in b°e₂ for b+e.

    When the first part of the grapheme belongs to the base and the second is morphological,
    we separate them using the centred dot, ·, as in e₂-udu-k·a, a writing of e'uduk[sheephouse].
    """

    n: str = Field(
        ...,
        alias="n",
        description="Name or label of the glossary entry",
        example="kaskal",
    )

    # Reference data
    id: str = Field(
        "",
        alias="id",
        description="Unique identifier for the glossary entry",
        example="o0031651.111",
    )
    cbd_id: str = Field(
        "",
        alias="cbd_id",
        description="Canonical ID for the glossary entry",
        example="o0031651.111",
    )
    xis: str = Field(
        ...,
        alias="xis",
        description="Extended identifier string",
        example="sux.r00f22e",
    )
    type: str = Field(
        ..., alias="type", description="The type of glossary entry", example="base"
    )


class _Bibliography(BaseModel):
    """
    Lorem ipsum
    """

    ref: str = Field(
        ..., alias="ref", description="Reference", example="H. Waetzoldt, UNT 11-12."
    )
    year: str = Field(..., alias="year", description="Year", example="1972")


class _Compound(BaseModel):
    """
    Lorem ipsum
    """

    citation_form: str = Field(
        ...,
        alias="cf",
        description="The headword used in the dictionary. "
        "In general, ePSD2 headwords use the long forms of words, and explicitly include the final -k in genitive compounds.",
        example="kaskal",
    )
    effective_part_of_speech: PartOfSpeechEnum = Field(
        ..., alias="epos", description="Effective part of speech", example="N"
    )
    guide_word: str = Field(
        ...,
        alias="gw",
        description="A label for the word which is primarily intended as a way of disambiguating homophones. "
        "Guide Words are not necessarily a 'basic' meaning for the word, although in practice this is often the case.",
        example="sound",
    )
    meaning: str = Field(
        ..., alias="mng", description="Meaning", example="a sound (onomatopoeic)"
    )
    partsig: str = Field(
        ..., alias="partsig", description="Part signature", example="zurzar[sound]N"
    )
    part_of_speech: PartOfSpeechEnum = Field(
        ...,
        alias="pos",
        description="The reference part-of-speech for the word. "
        "In some cases, words are used both as nouns and as verbs, "
        "and it is not always obvious which to use as the reference part-of-speech. "
        "In this case we simply make a conventional choice. See EPOS.",
        example="N",
    )
    primary: str = Field(
        "", alias="primary", description="Primary identifier", example="1"
    )
    ref: str = Field(..., alias="ref", description="Reference", example="o0043041")
    type: str = Field("", alias="type", description="Type of entry", example="cpd")

    @model_validator(mode="before")
    @classmethod
    def check_pos(cls, data: Any) -> Any:
        """Hotfix instance where 'pos'/'epos' is 'n' instead of 'N'"""
        if isinstance(data, dict):
            if "pos" in data and data["pos"] == "n":
                data["pos"] = "N"
            if "epos" in data and data["epos"] == "n":
                data["epos"] = "N"
        return data


class _CompoundOrthographicForm(BaseModel):
    """
    COFs: Compound Orthographic Forms

    COFs are forms that are written as one word but in fact should be understood as more than one lemma.
    Their meanings are transparent and they do not justify a separate entry in the glossary.


    http://oracc.museum.upenn.edu/doc/help/glossaries/cofs/index.html
    """

    head: str = Field(
        ...,
        alias="head",
        description="Head of the entry",
        example="zu[tooth//ivory]N'N",
    )
    tail: Dict[str, str] = Field(
        ...,
        alias="tail",
        description="Tail of the entry",
        example="{'sig': \"bir[shred//to shred]V/t'V/t\"}}",
    )


class _Continuation(BaseModel, OccurrenceStatsMixin):
    """
    Continuation graphemes are annotated explicitly because they often give information about the ending of a word.
    They have the form +-ga=g.a meaning that the base is followed by GA, writing the end of the base, g, and some other item, a.

    There is some inconsistency in ePSD2 about when a CONT is used and when a centred dot is used in the base:
    this will be rectified in a forthcoming release.

    ---

    The Sumerian grapheme following the base, used only when that grapheme is the continuation of the end of the BASE, e.g., -ma in inim-ma.
    The deconstruction of the grapheme gives the consonant which continues the grapheme followed by the vowel which is normally a morpheme or morpheme constituent.
    http://oracc.museum.upenn.edu/doc/help/glossaries/index.html
    """

    n: str = Field(
        ..., alias="n", description="Name or label of the entry", example="-la=l.a"
    )

    # Reference data
    id: str = Field(
        "",
        alias="id",
        description="Unique identifier for the entry",
        example="o0031651.114",
    )
    cbd_id: str = Field(
        "",
        alias="cbd_id",
        description="Canonical ID for the entry",
        example="o0031651.114",
    )
    xis: str = Field(
        ...,
        alias="xis",
        description="Extended identifier string",
        example="sux.r00f230",
    )
    type: str = Field(
        ..., alias="type", description="The type of entry", example="cont"
    )


class _Equivalency(BaseModel):
    """
    Lorem ipsum
    """

    equiv: str = Field(..., alias="equiv", description="Equivalent to", example="rimmu")
    lang: str = Field(..., alias="lang", description="Language", example="akk")


class _Form(BaseModel, OccurrenceStatsMixin):
    """
    Represents a form of a word or term.
    """

    c: int = Field("", alias="c", description="", example=49745)
    n: str = Field(..., alias="n", description="", example="kas-kal")
    rws: str = Field("", alias="rws", description="", example="ES")

    # Reference data
    id: str = Field(
        "",
        alias="id",
        description="Unique identifier for the form",
        example="o0031651.0",
    )
    cbd_id: str = Field(
        "",
        alias="cbd_id",
        description="Unique identifier for the form",
        example="o0031651.0",
    )
    ref: str = Field("", alias="ref", description="Reference ID", example="o0048612.0")
    xis: str = Field(
        ...,
        alias="xis",
        description="Extended identifier string",
        example="sux.r000005",
    )
    type: str = Field(..., alias="type", description="", example="form")


class _FormSans(BaseModel, OccurrenceStatsMixin):
    """
    Lorem ipsum
    """

    n: str = Field(
        ..., alias="n", description="Name or label of the entry", example="kas-kal"
    )

    # Reference data
    id: str = Field(
        "",
        alias="id",
        description="Unique identifier for the entry",
        example="o0031651.144",
    )
    cbd_id: str = Field(
        "",
        alias="cbd_id",
        description="Corpus-Based Dictionary ID",
        example="o0031651.144",
    )
    xis: str = Field(
        ...,
        alias="xis",
        description="Extended identifier string",
        example="sux.r000005",
    )
    type: str = Field(
        ..., alias="type", description="The type of entry", example="form-sans"
    )


class _Morphology(BaseModel, OccurrenceStatsMixin):
    """
    The morphology string follows a simple set of conventions for which preliminary documentation is available on the morphology pages.
    http://oracc.museum.upenn.edu/epsd2/about/annotation/morphology/index.html
    """

    n: str = Field(..., alias="n", description="", example=",ani.ta")

    # Reference data
    id: str = Field(
        "",
        alias="id",
        description="Unique identifier for the entry",
        example="o0031651.116",
    )
    cbd_id: str = Field(
        "",
        alias="cbd_id",
        description="Canonical ID for the entry",
        example="o0031651.116",
    )
    xis: str = Field(
        ...,
        alias="xis",
        description="Extended identifier string",
        example="sux.r00f21c",
    )
    type: str = Field(
        ..., alias="type", description="The type of entry", example="morph"
    )


class _NormalizationForm(BaseModel, OccurrenceStatsMixin):
    """
    Represents a normalized form of a word or term.
    """

    # Reference data
    cbd_id: str = Field(
        ...,
        alias="cbd_id",
        description="Canonical ID for the normalized form",
        example="o0031651.42",
    )
    ref: str = Field(..., alias="ref", description="Reference ID", example="o0031651.0")
    type: str = Field(..., alias="type", description="", example="normform")
    xis: str = Field(
        ...,
        alias="xis",
        description="Extended identifier string",
        example="sux.r000005",
    )


class _Normalization(BaseModel, OccurrenceStatsMixin):
    """
    Represents a normalized word or term.
    """

    forms: List[_NormalizationForm] = Field(
        [], alias="forms", description="List of normalized forms", example=[]
    )
    n: str = Field(
        ...,
        alias="n",
        description="Name or label of the normalized word",
        example="kaskal",
    )

    # Reference data
    id: str = Field(
        "",
        alias="id",
        description="Unique identifier for the normalized word",
        example="o0031651.41",
    )
    cbd_id: str = Field(
        "",
        alias="cbd_id",
        description="Canonical ID for the normalized word",
        example="o0031651.41",
    )
    xis: str = Field(
        ...,
        alias="xis",
        description="Extended identifier string",
        example="sux.r00f228",
    )


class _Period(BaseModel, OccurrenceStatsMixin):
    """
    Lorem ipsum
    """

    name: PeriodEnum = Field(
        ..., alias="p", description="Period description", example="Archaic"
    )

    # Reference data
    xis: str = Field(
        "",
        alias="xis",
        description="Extended identifier string",
        example="sux.r00f203.p.s000",
    )


class _Prefix(BaseModel, OccurrenceStatsMixin):
    """
    Lorem ipsum
    """

    n: str = Field(..., alias="n", description="", example="mu.na")

    # Reference data
    id: str = Field(
        "",
        alias="id",
        description="Unique identifier for the entry",
        example="o0023448.9",
    )
    cbd_id: str = Field(
        "",
        alias="cbd_id",
        description="Canonical ID for the entry",
        example="o0023448.9",
    )
    xis: str = Field(
        ...,
        alias="xis",
        description="Extended identifier string",
        example="sux.r000009",
    )
    type: str = Field(
        ..., alias="type", description="The type of entry", example="prefix"
    )


class _SeeCompound(BaseModel):
    """
    Lorem ipsum
    """

    xcpd: str = Field(
        ..., alias="xcpd", description="", example="zurzar za[make noise]V/t"
    )
    eref: str = Field(..., alias="eref", description="", example="o0043043")


class _Signature(BaseModel, OccurrenceStatsMixin):
    """
    Lorem ipsum
    """

    sig: str = Field(
        "",
        alias="sig",
        description="Signature string",
        example="@epsd2%sux:zu-zu=Zuzu[1//1]PN'PN$Zuzu/zu-zu#~",
    )
    cof_data: _CompoundOrthographicForm = Field(
        None, alias="cof-data", description="CofData object"
    )

    # Reference data
    id: str = Field(
        "", alias="id", description="Unique identifier", example="o0018496.8"
    )
    xis: str = Field(
        ...,
        alias="xis",
        description="Extended identifier string",
        example="sux.r002bb1",
    )
    type: str = Field(..., alias="type", description="Type of entry", example="sig")


class _Sense(BaseModel, OccurrenceStatsMixin):
    """
    Senses are indicative of the range of meanings of words.

    An ongoing objective for future work on ePSD2 is to improve annotation of the corpora
    with regard to senses in order to provide a more nuanced understanding of the ways words are used in context.
    """

    bases: List[_Base] = Field(
        ..., alias="bases", description="List of GlossaryBase objects"
    )

    continuation: List[_Continuation] = Field(
        [], alias="conts", description="List of Cont objects"
    )
    forms: List[_Form] = Field(..., alias="forms", description="List of Form objects")
    form_sans: List[_FormSans] = Field(
        ..., alias="form-sanss", description="List of FormSans objects"
    )
    mng: str = Field("", alias="mng", description="Meaning", example="way, road")
    morphs: List[_Morphology] = Field(
        ..., alias="morphs", description="List of _Morphology objects"
    )
    n: str = Field(
        ..., alias="n", description="Name or label", example="kaskal[way//way, road]N'N"
    )
    norms: List[_Normalization] = Field(
        ..., alias="norms", description="List of Norm objects"
    )
    num: str = Field(..., alias="num", description="Number", example="1.")
    ok: bool = Field(False, alias="ok", description="OK status", example=True)
    oracc_id: str = Field(
        "", alias="oracc_id", description="Oracc ID", example="o0007905"
    )
    pos: str = Field(..., alias="pos", description="Part of speech", example="N")
    prefixs: List[_Prefix] = Field(
        [], alias="prefixs", description="List of Prefix objects"
    )
    sigs: List[_Signature] = Field(
        ..., alias="sigs", description="List of Signature objects"
    )

    # Reference data
    id: str = Field(
        ..., alias="id", description="Unique identifier", example="sux.x0139035"
    )
    cbd_id: str = Field(
        "", alias="cbd_id", description="Canonical ID", example="sux.x0974361"
    )
    oid: str = Field("", alias="oid", description="Oracc ID?", example="o0002866")
    xis: str = Field(
        ...,
        alias="xis",
        description="Extended identifier string",
        example="sux.r00f237",
    )
    type: str = Field(..., alias="type", description="Type of entry", example="sense")


# TODO: Field(title="")


class Entry(BaseModel, OccurrenceStatsMixin):
    """
    Lorem ipsum
    """

    alias: str = Field(
        "", alias="alias", description="Alias", example="Zubi[the Zubi//the Zubi]WN'WN"
    )
    citation_form: str = Field(
        ...,
        alias="cf",
        description="The headword used in the dictionary. "
        "In general, ePSD2 headwords use the long forms of words, and explicitly include the final -k in genitive compounds.",
        example="kaskal",
    )
    guide_word: str = Field(
        "",
        alias="gw",
        description="A label for the word which is primarily intended as a way of disambiguating homophones. "
        "Guide Words are not necessarily a 'basic' meaning for the word, although in practice this is often the case.",
        example="way",
    )
    headword: str = Field(
        ..., alias="headword", description="Headword", example="kaskal[way]N"
    )
    part_of_speech: str = Field(
        ...,
        alias="pos",
        description="The reference part-of-speech for the word. "
        "In some cases, words are used both as nouns and as verbs, "
        "and it is not always obvious which to use as the reference part-of-speech. "
        "In this case we simply make a conventional choice. See EPOS.",
        example="N",
    )
    register_or_writing_system: str = Field(
        "", alias="rws", description="'' or 'ES'", example="ES"
    )

    bases: List[_Base] = Field(..., alias="bases")
    bibliography: List[_Bibliography] = Field([], alias="bib")
    compounds: List[_Compound] = Field([], alias="compound")
    continuations: List[_Continuation] = Field(..., alias="conts")
    equivalencies: List[_Equivalency] = Field([], alias="equivs")
    forms: List[_Form] = Field(..., alias="forms")
    form_sans: List[_FormSans] = Field(..., alias="form-sanss")
    morphology: List[_Morphology] = Field(..., alias="morphs")

    # Always empty
    morphology_2: List[_Morphology] = Field(..., alias="morph2s")
    stems: List[str] = Field(..., alias="stems", description="List of stems")

    normalized: List[_Normalization] = Field(..., alias="norms")
    periods: List[_Period] = Field(..., alias="periods")
    prefixs: List[_Prefix] = Field(..., alias="prefixs")
    see_compounds: List[_SeeCompound] = Field([], alias="see-compounds", description="")
    senses: List[_Sense] = Field(
        ..., alias="senses", description="List of Sense objects"
    )

    # Reference data
    id: str = Field(
        ..., alias="id", description="Unique identifier", example="o0031651"
    )
    dc_title: str = Field(
        ..., alias="dc_title", description="DC Title", example="epsd2/sux/kaskal[way]"
    )
    oracc_id: str = Field(
        "", alias="oracc_id", description="Oracc ID", example="o0031651"
    )
    oid: str = Field("", alias="oid", description="Oracc ID?", example="o0031651")
    xis: str = Field(
        ...,
        alias="xis",
        description="Extended identifier string",
        example="sux.o00f203",
    )


class Glossary(OraccFileBase):
    """
    Lorem ipsum
    """

    lang: str = Field("", alias="lang", description="", example="sux")
    entries: List[Entry] = Field("", alias="entries", description="", example=[])
    instances: Dict[str, List[str]] = Field(
        "", alias="instances", description="sux-id -> list", example=[]
    )
    summaries: Dict[str, str] = Field(
        "",
        alias="summaries",
        description="o/x-id -> summary",
        example={
            "o0023086": '<p class="summary" id="o0023086"><span class="summary"><span class="summary-headword">...'
        },
    )

    @classmethod
    def load(cls) -> "Glossary":
        """Loads the JSON data and instantiates the class."""
        data = load_json("gloss-sux.json")
        return cls(**data)


__all__ = ["Glossary"]
