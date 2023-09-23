"""
"""
from typing import List
from pydantic import Field
from oracc.epsd2.models.shared import BaseModel, OraccFileBase


class Chunk(BaseModel):
    """
    Lorem ipsum
    """

    type: str = Field(..., description="", example="h1")
    url: str = Field(..., description="", example="epsd2/index.html#d2e38")
    text: str = Field(..., description="", example="ePSD2 2.5 (2021-12-21)")


class Portal(OraccFileBase):
    """
    Lorem ipsum
    """

    chunks: List[Chunk] = Field(..., description="", example=[])


__all__ = ["Portal"]
