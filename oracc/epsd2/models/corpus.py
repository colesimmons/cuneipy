"""
"""
from typing import Dict
from pydantic import Field
from oracc.epsd2.models.shared import OraccFileBase


class Corpus(OraccFileBase):
    """
    The JSON file corpus.json is another manifest file: it lists the individual text editions that are located in the folder corpusjson/:
    """

    proxies: Dict[str, str] = Field(..., description="", example={"P223478": "blms"})


__all__ = ["Corpus"]
