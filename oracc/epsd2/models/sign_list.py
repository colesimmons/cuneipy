"""
"""
from typing import Dict, List, ForwardRef
from pydantic import Field
from oracc.epsd2.models.utils import BaseModel, OraccFileBase
from oracc.epsd2.utils import load_json


class _Modifier(BaseModel):
    """
    Lorem ipsum
    """

    b: str = Field("", description="base?", example="MU\u0160\u2083")
    # https://build-oracc.museum.upenn.edu//ns/gdl/1.0/index.html#Modifier
    m: str = Field("", description="modifier?", example="g")
    a: str = Field("", description="", example="a")


_Sequence = ForwardRef("_Sequence")


class _Sequence(BaseModel):
    """
    Lorem ipsum
    """

    s: str = Field("", description="Sign", example="A")
    # beside, joining, containing, above, crossing, opposing, repeated
    o: str = Field("", description="Operator types", example="beside")
    form: str = Field("", description="", example="MU\u0160\u2083@g")
    mods: List[_Modifier] = Field([], description="", example=[])
    m: str = Field("", description="", example="l")
    n: str = Field("", description="", example="n")
    r: str = Field("", description="", example="9")
    seq: List[_Sequence] = Field(
        [], description="", example=[{"s": "GI\u0160", "o": "beside"}]
    )


_Sequence.update_forward_refs()


class _GDL(BaseModel):
    """GDL = Grapheme Description Language"""

    c: str = Field("", description="Compound", example="|GI\u0160.LU\u2082|")
    seq: List[_Sequence] = Field(
        [], description="", example=[{"s": "GI\u0160", "o": "beside"}]
    )
    mods: List[Dict[str, str]] = Field(
        "", description="", example=[{"b": "ZA"}, {"m": "t"}]
    )
    n: str = Field("", description="", example="n")
    form: str = Field("", description="", example="9(U)")
    s: str = Field("", description="", example="ZU₅")


class _Sign(BaseModel):
    """
    Lorem ipsum
    """

    # Are these two lists the same length?...
    gdl: List[_GDL] = Field(..., description="", example=[{"c": "|GI\u0160.LU\u2082|"}])
    values: List[str] = Field(
        [], description="", example=["a", "aya₂", "dur₅", "duru₅"]
    )


class SignList(OraccFileBase):
    """
    Lorem ipsum
    """

    index: Dict[str, str] = Field(..., description="", example={"am₃": "|A.AN|"})
    signs: Dict[str, _Sign] = Field(..., description="", example={})

    @classmethod
    def load(cls) -> "SignList":
        """Loads the JSON data and instantiates the class."""
        data = load_json("epsd2-sl.json")
        return cls(**data)


__all__ = ["SignList"]
