"""
"""
from typing import Dict, List
from pydantic import Field
from oracc.epsd2.models.utils import BaseModel, OraccFileBase
from oracc.epsd2.utils import load_json


####################
# index-cat.json
####################
class _IndexKey(BaseModel):
    """
    Lorem ipsum
    """

    key: str = Field("", description="", example="p137994")
    count: int = Field("", description="", example=1)
    instances: List[str] = Field(
        [], description="", example=["epsd2/admin/ur3:P137994"]
    )


class IndexCat(OraccFileBase):
    """
    The index-xxx.json files are exports of a subset of the index data created and used by the Oracc search engine,
    giving the keys the indexer has generated from the input words and the locations in which they occur in the corpus.
    These keys may have been normalized using a variety of processes: accents are rendered as numeric indices; case may be foled;
    for English translation indexes a stemmer is used so that,
    e.g., "received" and "receives" will be gathered together under "receive" in the index.

    The text IDs are always qualified with a project name because any project can use texts from other projects.
    For "txt", "lem" and "tra" index types, the instances are given as word IDs,
    so they can be used to locate the instance in the text edition.
    A simple way of displaying instances is to use the URL http://oracc.org/PROJECT/INSTANCE_ID/html,
    e.g., http://oracc.org/rimanum/P405219.4.1/html.

    If you omit the "/html" the text is loaded into the Oracc pager instead of retrieving the simple HTML version.
    """

    name: str = Field(..., description="", example="cat")
    keys: List[_IndexKey] = Field(..., description="", example=[])
    map: Dict[str, str] = Field(..., description="", example={})

    @classmethod
    def load(cls) -> "IndexCat":
        """Loads the JSON data and instantiates the class."""
        data = load_json("index-cat.json")
        return cls(**data)


####################
# index-lem.json
####################
class IndexLem(OraccFileBase):
    """
    Lorem ipsum
    """

    name: str = Field(..., description="", example="lem")
    keys: List[_IndexKey] = Field(..., description="", example=[])
    map: Dict[str, str] = Field(..., description="", example={})

    @classmethod
    def load(cls) -> "IndexLem":
        """Loads the JSON data and instantiates the class."""
        data = load_json("index-lem.json")
        return cls(**data)


####################
# index-sux.json
####################
class IndexSux(OraccFileBase):
    """
    Lorem ipsum
    """

    name: str = Field(..., description="", example="sux")
    keys: List[_IndexKey] = Field(..., description="", example=[])
    map: Dict[str, str] = Field(..., description="", example={})

    @classmethod
    def load(cls) -> "IndexSux":
        """Loads the JSON data and instantiates the class."""
        data = load_json("index-sux.json")
        return cls(**data)


__all__ = ["IndexCat", "IndexSux", "IndexLem"]
