"""
"""
from typing import Dict, List
from pydantic import Field
from oracc.epsd2.models.utils import BaseModel, OraccFileBase
from oracc.epsd2.utils import load_json


class _Modifier(BaseModel):
    """
    Lorem ipsum
    """

    b: str = Field("", alias="b", description="base?", example="MU\u0160\u2083")
    # https://build-oracc.museum.upenn.edu//ns/gdl/1.0/index.html#Modifier
    m: str = Field("", alias="m", description="modifier?", example="g")
    a: str = Field("", alias="a", description="", example="a")


class _Sequence(BaseModel):
    """
    Lorem ipsum
    """

    s: str = Field("", alias="s", description="Sign", example="A")
    # beside, joining, containing, above, crossing, opposing, repeated
    o: str = Field("", alias="o", description="Operator types", example="beside")
    form: str = Field("", alias="form", description="", example="MU\u0160\u2083@g")
    mods: List[_Modifier] = Field([], alias="mods", description="", example=[])
    m: str = Field("", alias="m", description="m", example="l")
    n: str = Field("", alias="n", description="n", example="n")
    r: str = Field("", alias="r", description="r", example="9")
    seq: List["_Sequence"] = Field(
        [], alias="seq", description="", example=[{"s": "GI\u0160", "o": "beside"}]
    )


class _GDL(BaseModel):
    """GDL = Grapheme Description Language"""

    c: str = Field("", alias="c", description="Compound", example="|GI\u0160.LU\u2082|")

    # Will only be defined for number signs or compound signs
    seq: List[_Sequence] = Field([], alias="seq")

    mods: List[Dict[str, str]] = Field(
        "", alias="mods", description="", example=[{"b": "ZA"}, {"m": "t"}]
    )
    n: str = Field("", alias="n", description="", example="n")
    form: str = Field("", alias="form", description="", example="9(U)")
    s: str = Field("", alias="s", description="", example="ZU₅")


class _Sign(BaseModel):
    """
    Lorem ipsum
    """

    gdl: List[_GDL] = Field(
        ..., alias="gdl", description="", example=[{"c": "|GI\u0160.LU\u2082|"}]
    )
    values: List[str] = Field(
        [],
        alias="values",
        description="Possible readings of a sign",
        example=["a", "aya₂", "dur₅", "duru₅"],
    )


class SignList(OraccFileBase):
    """ """

    index: Dict[str, str] = Field(
        ...,
        alias="index",
        description="Mapping from values to sign names",
        example={"am₃": "|A.AN|"},
    )
    signs: Dict[str, _Sign] = Field(
        ...,
        alias="signs",
        description="Mapping from sign name to detailed sign data",
        example={},
    )

    @classmethod
    def load(cls) -> "SignList":
        """Loads the JSON data and instantiates the class."""
        data = load_json("epsd2-sl.json")
        return cls(**data)


__all__ = ["SignList"]
