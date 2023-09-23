"""
"""
from typing import Dict, List
from pydantic import Field
from oracc.epsd2.models.shared import BaseModel, OraccFileBase


class Form(BaseModel):
    """
    Lorem ipsum
    """

    type: str = Field(..., description="", example="form")
    cbd_id: str = Field("", description="", example="o0031651.0")
    id: str = Field("", description="", example="o0031651.0")
    n: str = Field(..., description="", example="kas-kal")
    c: int = Field("", description="", example=49745)
    icount: int = Field(..., description="", example=0)
    ipct: int = Field(..., description="", example=0)
    xis: str = Field(..., description="", example="sux.r000005")
    ref: str = Field("", description="", example="o0048612.0")
    rws: str = Field("", description="", example="ES")


class NormForm(BaseModel):
    """
    Lorem ipsum
    """

    type: str = Field(..., description="", example="normform")
    cbd_id: str = Field(..., description="", example="o0031651.42")
    ref: str = Field(..., description="", example="o0031651.0")
    icount: int = Field(..., description="", example=0)
    ipct: int = Field(..., description="", example=0)
    xis: str = Field(..., description="", example="sux.r000005")


class Norm(BaseModel):
    """
    Lorem ipsum
    """

    cbd_id: str = Field("", description="", example="o0031651.41")
    id: str = Field("", description="", example="o0031651.41")
    icount: int = Field(..., description="", example=366)
    ipct: int = Field(..., description="", example=27)
    xis: str = Field(..., description="", example="sux.r00f228")
    n: str = Field(..., description="", example="kaskal")
    forms: List[NormForm] = Field([], description="", example=[])


class GlossaryBase(BaseModel):
    """
    Lorem ipsum
    """

    type: str = Field(..., description="", example="base")
    cbd_id: str = Field("", description="", example="o0031651.111")
    id: str = Field("", description="", example="o0031651.111")
    n: str = Field(..., description="", example="kaskal")
    icount: int = Field(..., description="", example=1326)
    ipct: int = Field(..., description="", example=0)
    xis: str = Field(..., description="", example="sux.r00f22e")


class Cont(BaseModel):
    """
    Lorem ipsum
    """

    type: str = Field(..., description="", example="cont")
    cbd_id: str = Field("", description="", example="o0031651.114")
    id: str = Field("", description="", example="o0031651.114")
    n: str = Field(..., description="", example="-la=l.a")
    icount: int = Field(..., description="", example=57)
    ipct: int = Field(..., description="", example=4)
    xis: str = Field(..., description="", example="sux.r00f230")


class Morph(BaseModel):
    """
    Lorem ipsum
    """

    type: str = Field(..., description="", example="morph")
    cbd_id: str = Field("", description="", example="o0031651.116")
    id: str = Field("", description="", example="o0031651.116")
    n: str = Field(..., description="", example=",ani.ta")
    icount: int = Field(..., description="", example=1)
    ipct: int = Field(..., description="", example=0)
    xis: str = Field(..., description="", example="sux.r00f21c")


class Prefix(BaseModel):
    """
    Lorem ipsum
    """

    type: str = Field(..., description="", example="prefix")
    cbd_id: str = Field("", description="", example="o0023448.9")
    id: str = Field("", description="", example="o0023448.9")
    n: str = Field(..., description="", example="mu.na")
    icount: int = Field(..., description="", example=2)
    ipct: int = Field(..., description="", example=100)
    xis: str = Field(..., description="", example="sux.r000009")


class FormSans(BaseModel):
    """
    Lorem ipsum
    """

    type: str = Field(..., description="", example="form-sans")
    cbd_id: str = Field("", description="", example="o0031651.144")
    id: str = Field("", description="", example="o0031651.144")
    n: str = Field(..., description="", example="kas-kal")
    icount: int = Field(..., description="", example=0)
    ipct: int = Field(..., description="", example=0)
    xis: str = Field(..., description="", example="sux.r000005")


class CofData(BaseModel):
    """
    Lorem ipsum
    """

    head: str = Field(..., description="", example="zu[tooth//ivory]N'N")
    tail: Dict[str, str] = Field(
        ..., description="", example="{'sig': \"bir[shred//to shred]V/t'V/t\"}}"
    )  # TODO


class Signature(BaseModel):
    """
    Lorem ipsum
    """

    type: str = Field(..., description="", example="sig")
    id: str = Field("", description="", example="o0018496.8")
    sig: str = Field(
        "", description="", example="@epsd2%sux:zu-zu=Zuzu[1//1]PN'PN$Zuzu/zu-zu#~"
    )
    icount: int = Field(..., description="", example=4)
    ipct: int = Field(..., description="", example=57)
    xis: str = Field(..., description="", example="sux.r002bb1")
    cof_data: CofData = Field(None, alias="cof-data", description="")


class Sense(BaseModel):
    """
    Lorem ipsum
    """

    id: str = Field(..., description="", example="sux.x0139035")
    type: str = Field(..., description="", example="sense")
    cbd_id: str = Field("", description="", example="sux.x0974361")
    n: str = Field(..., description="", example="kaskal[way//way, road]N'N")
    oracc_id: str = Field("", description="", example="o0007905", alias="oid")
    icount: int = Field(..., description="", example=1314)
    ipct: int = Field(..., description="", example=99)
    xis: str = Field(..., description="", example="sux.r00f237")
    ok: bool = Field(False, description="", example=True)
    num: str = Field(..., description="", example="1.")
    pos: str = Field(..., description="", example="N")
    mng: str = Field("", description="", example="way, road")
    forms: List[Form] = Field(..., description="", example=[])
    norms: List[Norm] = Field(..., description="", example=[])
    bases: List[GlossaryBase] = Field(..., description="", example=[])
    conts: List[Cont] = Field([], description="", example=[])
    morphs: List[Morph] = Field(..., description="", example=[])
    form_sans: List[FormSans] = Field(
        ..., description="", example=[], alias="form-sanss"
    )
    prefixs: List[Prefix] = Field([], description="", example=[])
    sigs: List[Signature] = Field(..., description="", example=[])


class Period(BaseModel):
    """
    Lorem ipsum
    """

    p: str = Field("", description="", example="Archaic")
    icount: int = Field(..., description="", example=1)
    ipct: int = Field(..., description="", example=0)
    xis: str = Field("", description="", example="sux.r00f203.p.s000")


class Compound(BaseModel):
    """
    Lorem ipsum
    """

    type: str = Field("", description="", example="cpd")
    primary: str = Field("", description="", example="1")
    partsig: str = Field(..., description="", example="zurzar[sound]N")
    ref: str = Field(..., description="", example="o0043041")
    cf: str = Field(..., description="", example="zurzar")
    gw: str = Field(..., description="", example="sound")
    mng: str = Field(..., description="", example="a sound (onomatopoeic)")
    pos: str = Field(..., description="", example="N")
    epos: str = Field(..., description="", example="N")


class GlossaryItem(BaseModel):
    """
    Lorem ipsum
    """

    alias: str = Field("", description="", example="Zubi[the Zubi//the Zubi]WN'WN")
    headword: str = Field(..., description="", example="kaskal[way]N")
    id: str = Field(..., description="", example="o0031651")
    oracc_id: str = Field("", description="", example="o0031651", alias="oid")
    icount: int = Field(..., description="", example=1333)
    ipct: int = Field(..., description="", example=100)
    xis: str = Field(..., description="", example="sux.o00f203")
    dc_title: str = Field(..., description="", example="epsd2/sux/kaskal[way]")
    cf: str = Field(..., description="citation form", example="kaskal")
    gw: str = Field("", description="guide word", example="way")
    pos: str = Field(..., description="part of speech", example="N")
    forms: List[Form] = Field(..., description="", example=[])
    norms: List[Norm] = Field(..., description="", example=[])
    bases: List[GlossaryBase] = Field("", description="", example=[])
    conts: List[Cont] = Field(..., description="", example=[])
    morphs: List[Morph] = Field(..., description="", example=[])
    morph2s: List[Morph] = Field(..., description="", example=[])
    stems: List[str] = Field(..., description="", example=[])
    prefixs: List[Prefix] = Field(..., description="", example=[])
    form_sans: List[FormSans] = Field(
        ..., description="", example=[], alias="form-sanss"
    )
    senses: List[Sense] = Field(..., description="", example=[])
    periods: List[Period] = Field(..., description="", example=[])
    compound: List[Compound] = Field([], description="", example=[])
    rws: str = Field("", description="", example="ES")


class Glossary(OraccFileBase):
    """
    Lorem ipsum
    """

    lang: str = Field("", description="", example="sux")
    entries: List[GlossaryItem] = Field("", description="", example=[])
    instances: Dict[str, List[str]] = Field(
        "", description="sux-id -> list", example=[]
    )
    summaries: Dict[str, str] = Field(
        "",
        description="o/x-id -> summary",
        example={
            "o0023086": '<p class="summary" id="o0023086"><span class="summary"><span class="summary-headword">...'
        },
    )


__all__ = ["Glossary"]
