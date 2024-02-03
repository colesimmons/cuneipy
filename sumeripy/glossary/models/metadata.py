"""
"""
from typing import Dict
from pydantic import Field
from pyoracc.epsd2.models.utils import BaseModel, OraccFileBase
from pyoracc.epsd2.utils import load_json


# Config class
class Config(BaseModel):
    """
    Lorem ipsum
    """

    abbrev: str = Field(
        ..., alias="abbrev", description="Abbreviation of the project", example="ePSD2"
    )
    blurb: str = Field(
        ..., alias="blurb", description="Short description or blurb", example=""
    )
    name: str = Field(
        ...,
        alias="name",
        description="Name of the project",
        example="electronic PSD 2nd Edition",
    )
    options: Dict[str, str] = Field(
        ..., alias="options", description="Additional options", example={}
    )
    pathname: str = Field(
        ..., alias="pathname", description="Path name", example="epsd2"
    )
    project_type: str = Field(
        ..., alias="project-type", description="Type of the project", example="superglo"
    )
    public: str = Field(
        ..., alias="public", description="Public availability status", example=""
    )


# Metadata class
class Metadata(OraccFileBase):
    """
    This provides several objects:
    "config" - the configuration info for the project;
    "witnesses" - only present if projects use composite texts, this provides information on which manuscripts are witnesses of the composites in the project;
    "formats" - a collection of lists indicating the presence of transliterations, transliterations and lemmatized data in the project.
    """

    config: Config = Field(
        ..., alias="config", description="Configuration information", example={}
    )
    formats: Dict[str, str] = Field(
        ..., alias="formats", description="Data formats available", example={}
    )

    @classmethod
    def load(cls) -> "Metadata":
        """Loads the JSON data and instantiates the class."""
        data = load_json("metadata.json")
        return cls(**data)


__all__ = ["Metadata"]
