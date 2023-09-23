"""
"""
from typing import List
from pydantic import Field
from oracc.epsd2.models.utils import BaseModel, OraccFileBase
from oracc.epsd2.utils import load_json


class Chunk(BaseModel):
    """
    Lorem ipsum
    """

    type: str = Field(..., alias="type", description="", example="h1")
    url: str = Field(..., alias="url", description="", example="epsd2/index.html#d2e38")
    text: str = Field(
        ..., alias="text", description="", example="ePSD2 2.5 (2021-12-21)"
    )


class Portal(OraccFileBase):
    """
    Lorem ipsum
    """

    chunks: List[Chunk] = Field(..., description="", example=[])

    @classmethod
    def load(cls) -> "Portal":
        """Loads the JSON data and instantiates the class."""
        data = load_json("epsd2-portal.json")
        return cls(**data)


__all__ = ["Portal"]
