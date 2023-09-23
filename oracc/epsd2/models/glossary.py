"""
"""
from typing import Dict, List
from pydantic import Field
from oracc.epsd2.models.utils import BaseModel, OraccFileBase
from oracc.epsd2.utils import load_json


class Form(BaseModel):
    """
    Represents a form of a word or term.
    """

    c: int = Field("", alias="c", description="", example=49745)
    n: str = Field(..., alias="n", description="", example="kas-kal")
    rws: str = Field("", alias="rws", description="", example="ES")

    # Occurrence data
    count: int = Field(..., alias="icount", description="Instance count", example=0)
    percent_of_instances: int = Field(
        ..., alias="ipct", description="Instance percentage", example=0
    )

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


class NormForm(BaseModel):
    """
    Represents a normalized form of a word or term.
    """

    # Occurrence data
    count: int = Field(..., alias="icount", description="Instance count", example=0)
    percent_of_instances: int = Field(
        ..., alias="ipct", description="Instance percentage", example=0
    )

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


class Norm(BaseModel):
    """
    Represents a normalized word or term.
    """

    forms: List[NormForm] = Field(
        [], alias="forms", description="List of normalized forms", example=[]
    )
    n: str = Field(
        ...,
        alias="n",
        description="Name or label of the normalized word",
        example="kaskal",
    )

    # Occurrence data
    count: int = Field(..., alias="icount", description="Instance count", example=366)
    percent_of_instances: int = Field(
        ..., alias="ipct", description="Instance percentage", example=27
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


class GlossaryBase(BaseModel):
    """
    Represents a base glossary entry.
    """

    n: str = Field(
        ...,
        alias="n",
        description="Name or label of the glossary entry",
        example="kaskal",
    )

    # Occurrence data
    count: int = Field(..., alias="icount", description="Instance count", example=1326)
    percent_of_instances: int = Field(
        ..., alias="ipct", description="Instance percentage", example=0
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


class Cont(BaseModel):
    """
    Lorem ipsum
    """

    n: str = Field(
        ..., alias="n", description="Name or label of the entry", example="-la=l.a"
    )

    # Occurrence data
    count: int = Field(..., alias="icount", description="Instance count", example=57)
    percent_of_instances: int = Field(
        ..., alias="ipct", description="Instance percentage", example=4
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


class Morph(BaseModel):
    """
    Lorem ipsum
    """

    n: str = Field(..., alias="n", description="", example=",ani.ta")

    # Occurrence data
    count: int = Field(..., alias="icount", description="Instance count", example=1)
    percent_of_instances: int = Field(
        ..., alias="ipct", description="Instance percentage", example=0
    )

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


class Prefix(BaseModel):
    """
    Lorem ipsum
    """

    n: str = Field(..., alias="n", description="", example="mu.na")

    # Occurrence data
    count: int = Field(..., alias="icount", description="Instance count", example=2)
    percent_of_instances: int = Field(
        ..., alias="ipct", description="Instance percentage", example=100
    )

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


class FormSans(BaseModel):
    """
    Lorem ipsum
    """

    n: str = Field(
        ..., alias="n", description="Name or label of the entry", example="kas-kal"
    )

    # Occurrence data
    count: int = Field(..., alias="icount", description="Instance count", example=0)
    percent_of_instances: int = Field(
        ..., alias="ipct", description="Instance percentage", example=0
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
        description="Canonical ID for the entry",
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


class CofData(BaseModel):
    """
    Lorem ipsum
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


class Signature(BaseModel):
    """
    Lorem ipsum
    """

    sig: str = Field(
        "",
        alias="sig",
        description="Signature string",
        example="@epsd2%sux:zu-zu=Zuzu[1//1]PN'PN$Zuzu/zu-zu#~",
    )
    cof_data: CofData = Field(None, alias="cof-data", description="CofData object")

    # Occurrence data
    count: int = Field(..., alias="icount", description="Instance count", example=4)
    percent_of_instances: int = Field(
        ..., alias="ipct", description="Instance percentage", example=57
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


class Sense(BaseModel):
    """
    Lorem ipsum
    """

    bases: List[GlossaryBase] = Field(
        ..., alias="bases", description="List of GlossaryBase objects"
    )
    conts: List[Cont] = Field([], alias="conts", description="List of Cont objects")
    forms: List[Form] = Field(..., alias="forms", description="List of Form objects")
    form_sans: List[FormSans] = Field(
        ..., alias="form-sanss", description="List of FormSans objects"
    )
    mng: str = Field("", alias="mng", description="Meaning", example="way, road")
    morphs: List[Morph] = Field(
        ..., alias="morphs", description="List of Morph objects"
    )
    n: str = Field(
        ..., alias="n", description="Name or label", example="kaskal[way//way, road]N'N"
    )
    norms: List[Norm] = Field(..., alias="norms", description="List of Norm objects")
    num: str = Field(..., alias="num", description="Number", example="1.")
    ok: bool = Field(False, alias="ok", description="OK status", example=True)
    oracc_id: str = Field(
        "", alias="oracc_id", description="Oracc ID", example="o0007905"
    )
    pos: str = Field(..., alias="pos", description="Part of speech", example="N")
    prefixs: List[Prefix] = Field(
        [], alias="prefixs", description="List of Prefix objects"
    )
    sigs: List[Signature] = Field(
        ..., alias="sigs", description="List of Signature objects"
    )

    # Occurrence data
    count: int = Field(..., alias="icount", description="Instance count", example=1314)
    percent_of_instances: int = Field(
        ..., alias="ipct", description="Instance percentage", example=99
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


class Period(BaseModel):
    """
    Lorem ipsum
    """

    p: str = Field("", alias="p", description="Period description", example="Archaic")

    # Occurrence data
    count: int = Field(..., alias="icount", description="Instance count", example=1)
    percent_of_instances: int = Field(
        ..., alias="ipct", description="Instance percentage", example=0
    )

    # Reference data
    xis: str = Field(
        "",
        alias="xis",
        description="Extended identifier string",
        example="sux.r00f203.p.s000",
    )


class Compound(BaseModel):
    """
    Lorem ipsum
    """

    cf: str = Field(..., alias="cf", description="Citation form", example="zurzar")
    epos: str = Field(
        ..., alias="epos", description="Extended part of speech", example="N"
    )
    gw: str = Field(..., alias="gw", description="Guide word", example="sound")
    mng: str = Field(
        ..., alias="mng", description="Meaning", example="a sound (onomatopoeic)"
    )
    partsig: str = Field(
        ..., alias="partsig", description="Part signature", example="zurzar[sound]N"
    )
    pos: str = Field(..., alias="pos", description="Part of speech", example="N")
    primary: str = Field(
        "", alias="primary", description="Primary identifier", example="1"
    )
    ref: str = Field(..., alias="ref", description="Reference", example="o0043041")
    type: str = Field("", alias="type", description="Type of entry", example="cpd")


class SeeCompound(BaseModel):
    """
    Lorem ipsum
    """

    xcpd: str = Field(
        ..., alias="xcpd", description="", example="zurzar za[make noise]V/t"
    )
    eref: str = Field(..., alias="eref", description="", example="o0043043")


class Bibliography(BaseModel):
    """
    Lorem ipsum
    """

    ref: str = Field(
        ..., alias="ref", description="Reference", example="H. Waetzoldt, UNT 11-12."
    )
    year: str = Field(..., alias="year", description="Year", example="1972")


class Equivalency(BaseModel):
    """
    Lorem ipsum
    """

    equiv: str = Field(..., alias="equiv", description="Equivalent to", example="rimmu")
    lang: str = Field(..., alias="lang", description="Language", example="akk")


class GlossaryItem(BaseModel):
    """
    Lorem ipsum
    """

    alias: str = Field(
        "", alias="alias", description="Alias", example="Zubi[the Zubi//the Zubi]WN'WN"
    )
    bases: List[GlossaryBase] = Field(
        "", alias="bases", description="List of GlossaryBase objects"
    )
    bib: List[Bibliography] = Field([], alias="bib", description="Bibliography")
    cf: str = Field(..., alias="cf", description="Citation form", example="kaskal")
    compound: List[Compound] = Field(
        [], alias="compound", description="List of Compound objects"
    )
    conts: List[Cont] = Field(..., alias="conts", description="List of Cont objects")
    equivalencies: List[Equivalency] = Field(
        [], alias="equivs", description="List of equivalent items in other languages"
    )
    forms: List[Form] = Field(..., alias="forms", description="List of Form objects")
    form_sans: List[FormSans] = Field(..., alias="form-sanss", description="")
    gw: str = Field("", alias="gw", description="Guide word", example="way")
    headword: str = Field(
        ..., alias="headword", description="Headword", example="kaskal[way]N"
    )
    morph2s: List[Morph] = Field(
        ..., alias="morph2s", description="List of Morph objects"
    )
    morphs: List[Morph] = Field(
        ..., alias="morphs", description="List of Morph objects"
    )
    norms: List[Norm] = Field(..., alias="norms", description="List of Norm objects")
    periods: List[Period] = Field(
        ..., alias="periods", description="List of Period objects"
    )
    pos: str = Field(..., alias="pos", description="Part of speech", example="N")
    prefixs: List[Prefix] = Field(
        ..., alias="prefixs", description="List of Prefix objects"
    )
    rws: str = Field("", alias="rws", description="RWS", example="ES")
    see_compounds: List[SeeCompound] = Field([], alias="see-compounds", description="")
    senses: List[Sense] = Field(
        ..., alias="senses", description="List of Sense objects"
    )
    stems: List[str] = Field(..., alias="stems", description="List of stems")

    # Occurrence data
    count: int = Field(..., alias="icount", description="Instance count", example=1333)
    percent_of_instances: int = Field(
        ..., alias="ipct", description="Instance percentage", example=100
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
    entries: List[GlossaryItem] = Field("", alias="entries", description="", example=[])
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
