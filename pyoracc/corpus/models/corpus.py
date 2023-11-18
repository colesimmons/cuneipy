from typing import Dict, List
from enum import Enum
from pydantic import BaseModel, Field, ConfigDict
import json
from pathlib import Path
from typing import Set

from pyoracc.corpus.models.text import (
    BaseText,
    EarlyLitText,
    Ed3aText,
    Ed3bText,
    Ed12Text,
    Lagash2Text,
    LiteraryText,
    OakkText,
    PraxisText,
    PraxisUdughulText,
    PraxisVariaText,
    RoyalText,
    Ur3Text
)
from pyoracc.corpus.enums import CorpusType


class Corpus(BaseModel):
    texts: List[BaseText] = []

    @classmethod
    def load(cls, corpus: CorpusType, dir: str) -> "Corpus":
        catalogue_path = Path(dir) / "catalogue.json"
        with open(catalogue_path) as f:
            catalogue = json.load(f)
        texts = []
        for text_data in catalogue["members"].values():
            dir_path = str(Path(dir) / "corpusjson/")

            if corpus is CorpusType.ED12:
                text = Ed12Text(dir_path=dir_path, **text_data)
            elif corpus is CorpusType.ED3A:
                text = Ed3aText(dir_path=dir_path, **text_data)
            elif corpus is CorpusType.ED3B:
                text = Ed3bText(dir_path=dir_path, **text_data)
            elif corpus is CorpusType.EBLA:
                continue
            elif corpus is CorpusType.OAKK:
                text = OakkText(dir_path=dir_path, **text_data)
            elif corpus is CorpusType.UR3:
                text = Ur3Text(dir_path=dir_path, **text_data)
            elif corpus is CorpusType.LAGASH2:
                text = Lagash2Text(dir_path=dir_path, **text_data)
            elif corpus is CorpusType.OLDBAB:
                continue
            elif corpus is CorpusType.EARLYLIT:
                text = EarlyLitText(dir_path=dir_path, **text_data)
            elif corpus is CorpusType.LITERARY:
                text = LiteraryText(dir_path=dir_path, **text_data)
            elif corpus is CorpusType.ROYAL:
                text = RoyalText(dir_path=dir_path, **text_data)
            elif corpus is CorpusType.PRAXIS:
                text = PraxisText(dir_path=dir_path, **text_data)
            elif corpus is CorpusType.PRAXIS_UDUGHUL:
                text = PraxisUdughulText(dir_path=dir_path, **text_data)
            elif corpus is CorpusType.PRAXIS_VARIA:
                text = PraxisVariaText(dir_path=dir_path, **text_data)

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

    def summarize_corpus_properties(self):
        num_texts = len(self.texts)

        # Dict where key is property name and
        # value is number of texts that have a non-empty value for that property 
        property_counts = {}
        for text in self.texts:
            for field in text.model_fields:
                if field not in property_counts:
                    property_counts[field] = 0

                value = getattr(text, field)
                if len(value):
                    property_counts[field] += 1
        
        # Now format it a percentage of the overall number of texts
        for property_name, count in property_counts.items():
            property_counts[property_name] = (count / num_texts) * 100

        return property_counts
        

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
