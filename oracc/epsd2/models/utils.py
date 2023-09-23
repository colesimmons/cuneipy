from datetime import datetime
from pydantic import BaseModel as PydanticBaseModel, Field, ConfigDict


class BaseModel(PydanticBaseModel):
    """Forbid extra keys"""

    model_config = ConfigDict(extra="forbid")


class OraccFileBase(BaseModel):
    """Base schema for ePSD files"""

    type: str = Field(..., alias="type", description="", example="corpus")
    project: str = Field(..., alias="project", description="", example="epsd2")
    source: str = Field(
        ..., alias="source", description="", example="http://oracc.org/epsd2"
    )
    license: str = Field(
        ...,
        alias="license",
        description="",
        example="This data is released under the CC0 license",
    )
    license_url: str = Field(
        ...,
        alias="license_url",
        description="",
        example="https://creativecommons.org/publicdomain/zero/1.0/",
        alias="license-url",
    )
    more_info: str = Field(
        ...,
        alias="more_info",
        description="",
        example="http://oracc.org/doc/opendata/",
        alias="more-info",
    )
    timestamp: datetime = Field(
        ...,
        alias="timestamp",
        description="",
        example="2021-12-21T03:21:44",
        alias="UTC-timestamp",
    )
