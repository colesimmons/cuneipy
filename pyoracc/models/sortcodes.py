"""
"""
from typing import Dict
from pydantic import Field
from pyoracc.epsd2.models.utils import BaseModel
from pyoracc.utils import load_json


class Sortvals(BaseModel):
    """
    Lorem ipsum
    """

    genres: Dict[str, int] = Field(..., alias="genres", description="", example={})
    periods: Dict[str, int] = Field(..., alias="periods", description="", example={})
    places: Dict[str, int] = Field(..., alias="places", description="", example={})
    rulers: Dict[str, int] = Field(..., alias="rulers", description="", example={})
    sessions: Dict[str, int] = Field(..., alias="sessions", description="", example={})
    subgenre_remarks: Dict[str, int] = Field(
        {}, alias="subgenre_remarks", description="", example={}
    )
    subgenres: Dict[str, int] = Field(
        ..., alias="subgenres", description="", example={}
    )
    supergenres: Dict[str, int] = Field(
        ..., alias="supergenres", description="", example={}
    )


class Sortcodes(BaseModel):
    """
    Lorem ipsum
    """

    sortvals: Sortvals = Field(..., alias="sortvals", description="", example={})

    @classmethod
    def load(cls) -> "Sortcodes":
        """Loads the JSON data and instantiates the class."""
        data = load_json("sortcodes.json")
        return cls(**data)


__all__ = ["Sortcodes"]
