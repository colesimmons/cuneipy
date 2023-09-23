"""
"""
from typing import Dict
from pydantic import Field
from oracc.epsd2.models.shared import BaseModel


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


__all__ = ["Sortcodes"]
