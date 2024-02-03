"""
"""
from typing import Dict
from pydantic import Field
from pyoracc.epsd2.models.utils import OraccFileBase
from pyoracc.epsd2.utils import load_json


class Corpus(OraccFileBase):
    """
    The JSON file corpus.json is another manifest file: it lists the individual text editions that are located in the folder corpusjson/:
    """

    proxies: Dict[str, str] = Field(..., description="", example={"P223478": "blms"})

    @classmethod
    def load(cls) -> "Corpus":
        """Loads the JSON data and instantiates the class."""
        data = load_json("corpus.json")
        return cls(**data)


__all__ = ["Corpus"]
