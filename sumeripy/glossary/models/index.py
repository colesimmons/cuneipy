"""
"""
from typing import Dict, List
from pydantic import Field
from pyoracc.epsd2.models.utils import BaseModel, OraccFileBase
from pyoracc.epsd2.utils import load_json


# _IndexKey class
class _IndexKey(BaseModel):
    """
    Lorem ipsum
    """

    count: int = Field(..., alias="count", description="Count of instances", example=1)
    instances: List[str] = Field(
        [],
        alias="instances",
        description="List of instances",
        example=["epsd2/admin/ur3:P137994"],
    )
    key: str = Field("", alias="key", description="Key identifier", example="p137994")


# IndexCat class
class IndexCat(OraccFileBase):
    """
    The index-xxx.json files are exports of a subset of the index data created and used by the Oracc search engine,
    ...
    """

    keys: List[_IndexKey] = Field(
        ..., alias="keys", description="List of index keys", example=[]
    )
    map: Dict[str, str] = Field(
        ..., alias="map", description="Mapping dictionary", example={}
    )
    name: str = Field(
        ..., alias="name", description="Name of the index category", example="cat"
    )

    @classmethod
    def load(cls) -> "IndexCat":
        """Loads the JSON data and instantiates the class."""
        data = load_json("index-cat.json")
        return cls(**data)


# IndexLem class
class IndexLem(OraccFileBase):
    """
    Lorem ipsum
    """

    keys: List[_IndexKey] = Field(
        ..., alias="keys", description="List of index keys", example=[]
    )
    map: Dict[str, str] = Field(
        ..., alias="map", description="Mapping dictionary", example={}
    )
    name: str = Field(
        ..., alias="name", description="Name of the index category", example="lem"
    )

    @classmethod
    def load(cls) -> "IndexLem":
        """Loads the JSON data and instantiates the class."""
        data = load_json("index-lem.json")
        return cls(**data)


# IndexSux class
class IndexSux(OraccFileBase):
    """
    Lorem ipsum
    """

    keys: List[_IndexKey] = Field(
        ..., alias="keys", description="List of index keys", example=[]
    )
    map: Dict[str, str] = Field(
        ..., alias="map", description="Mapping dictionary", example={}
    )
    name: str = Field(
        ..., alias="name", description="Name of the index category", example="sux"
    )

    @classmethod
    def load(cls) -> "IndexSux":
        """Loads the JSON data and instantiates the class."""
        data = load_json("index-sux.json")
        return cls(**data)


__all__ = ["IndexCat", "IndexSux", "IndexLem"]
