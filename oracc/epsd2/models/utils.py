from datetime import datetime
from pydantic import BaseModel as PydanticBaseModel, Field, ConfigDict


class BaseModel(PydanticBaseModel):
    """Forbid extra keys"""

    model_config = ConfigDict(extra="forbid")


class OraccFileBase(BaseModel):
    """Base schema for ePSD files"""

    type: str = Field(..., description="", example="corpus")
    project: str = Field(..., description="", example="epsd2")
    source: str = Field(..., description="", example="http://oracc.org/epsd2")
    license: str = Field(
        ..., description="", example="This data is released under the CC0 license"
    )
    license_url: str = Field(
        ...,
        description="",
        example="https://creativecommons.org/publicdomain/zero/1.0/",
        alias="license-url",
    )
    more_info: str = Field(
        ..., description="", example="http://oracc.org/doc/opendata/", alias="more-info"
    )
    timestamp: datetime = Field(
        ..., description="", example="2021-12-21T03:21:44", alias="UTC-timestamp"
    )
