"""
"""
from typing import Dict
from pydantic import Field
from oracc.epsd2.models.utils import BaseModel, OraccFileBase
from oracc.epsd2.utils import load_json


class Config(BaseModel):
    """
    Lorem ipsum
    """

    pathname: str = Field(..., description="", example="epsd2")
    name: str = Field(..., description="", example="electronic PSD 2nd Edition")
    abbrev: str = Field(..., description="", example="ePSD2")
    project_type: str = Field(
        ..., alias="project-type", description="", example="superglo"
    )
    blurb: str = Field(..., description="", example="")
    public: str = Field(..., description="", example="")
    options: Dict[str, str] = Field(..., description="", example={})


class Metadata(OraccFileBase):
    """
    This provides several objects:
    "config" - the configuration info for the project;
    "witnesses" - only present if projects use composite texts, this provides information on which manuscripts are witnesses of the composites in the project;
    "formats" - a collection of lists indicating the presence of transliterations, transliterations and lemmatized data in the project.
    """

    config: Config = Field(..., description="", example={})
    formats: Dict[str, str] = Field(..., description="", example={})

    @classmethod
    def load(cls) -> "Metadata":
        """Loads the JSON data and instantiates the class."""
        data = load_json("metadata.json")
        return cls(**data)


__all__ = ["Metadata"]
