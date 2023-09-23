"""
"""
from typing import Dict
from pydantic import Field
from oracc.epsd2.models.utils import BaseModel
from oracc.epsd2.utils import load_json


class Sortvals(BaseModel):
    """
    Lorem ipsum
    """

    periods: Dict[str, int] = Field(..., description="", example={})
    subgenre_remarks_t: Dict[str, int] = Field(..., description="", example={})
    rulers: Dict[str, int] = Field(..., description="", example={})
    sessions: Dict[str, int] = Field(..., description="", example={})
    places: Dict[str, int] = Field(..., description="", example={})
    subgenres: Dict[str, int] = Field(..., description="", example={})
    supergenres: Dict[str, int] = Field(..., description="", example={})
    genres: Dict[str, int] = Field(..., description="", example={})


class Sortcodes(BaseModel):
    """
    Lorem ipsum
    """

    sortvals: Sortvals = Field(..., description="", example={})

    @classmethod
    def load(cls) -> "Sortcodes":
        """Loads the JSON data and instantiates the class."""
        data = load_json("epsd2-sortcodes.json")
        return cls(**data)


__all__ = ["Sortcodes"]
