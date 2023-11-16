from typing import Dict, List
from enum import Enum
from pydantic import BaseModel, Field, ConfigDict
import json
from pathlib import Path
from typing import Set

from pyoracc.corpus.models.text import Text


class Corpus(BaseModel):
    texts: List[Text] = []

    @classmethod
    def load(cls, dir: str) -> "Corpus":
        catalogue_path = Path(dir) / "catalogue.json"
        with open(catalogue_path) as f:
            catalogue = json.load(f)
        texts = []
        for text_data in catalogue["members"].values():
            text = Text(dir_path=str(Path(dir) / "corpusjson/"), **text_data)
            texts.append(text)
        return cls(texts=texts)

    def get_unique_values(self, whitelist) -> Dict[str, Set[str]]:
        """
        Useful for getting a list of all the unique values for a given field or fields.

        e.g. corpus.get_unique_values({ "period", "language" })
        """
        unique_values = {}
        for text in self.texts:
            for field in text.model_fields:
                if field not in whitelist:
                    continue
                if field not in unique_values:
                    unique_values[field] = set()
                unique_values[field].add(getattr(text, field))
        return unique_values

    # catalogue.json
    # Very useful!

    # corpus.json
    # Not really useful. Just tells you what files are in corpusjson.

    # gloss-qpn.json
    # QPN: Oracc Linguistic Annotation for Proper Nouns
    # http://oracc.museum.upenn.edu/doc/help/languages/propernouns/index.html

    # gloss-sux.json
    # SUX: Oracc Linguistic Annotation for Sumerian
    # http://oracc.museum.upenn.edu/doc/help/languages/sumerian/index.html

    # "The index-xxx.json files are exports of a subset of the index data created and used by the Oracc search engine,
    # giving the keys the indexer has generated from the input words and the locations in which they occur in the corpus."
    # http://oracc.museum.upenn.edu/doc/opendata/json/index.html
    # index-cat.json
    # index-lem.json
    # index-qpn.json
    # index-sux.json
    # index-tra.json
    # index-txt.json

    # Tells you what formats are available
    # metadata.json
    # sortcodes.json
