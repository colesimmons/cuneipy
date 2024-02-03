"""
This module defines the Corpus class, which represents a corpus of texts.

The Corpus class provides methods for loading a corpus from a given path,
retrieving unique values for specific fields, and summarizing the properties of the corpus.

Example usage:
    corpus = Corpus.load(CorpusType.ADMIN_ED3A, "/path/to/corpus")
    unique_values = corpus.get_unique_values({"field1", "field2"})
    summary = corpus.summarize_corpus_properties()


    # catalogue.json # TODO
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

"""

from typing import Dict, Generic, List, Set, TypeVar

from pydantic import BaseModel

from .types import Text

T = TypeVar("T", bound=Text)


class CorpusBase(BaseModel, Generic[T]):
    """
    Represents a corpus of texts.

    Attributes:
        texts (List[CorpusText]): A list of CorpusText objects representing the texts in the corpus.
    """

    texts: List[T] = []

    # def __init__(self, texts: List[TextType]):
    # self.texts = TextType()

    #   @classmethod
    #   def load(cls: Type["BaseCorpus[T]"], path: str) -> "BaseCorpus[T]":
    #       """Load a corpus from a given path.
    #
    #        Args:
    #            corpus (CorpusType): The type of corpus to load.
    #            path (str): The path to the corpus.
    #
    #        Returns:
    #            Corpus: The loaded corpus.
    #        """
    #        catalogue_path = Path(path) / "catalogue.json"
    #        with open(catalogue_path, "r", encoding="utf-8") as f:
    #            catalogue = json.load(f)
    #        dir_path = str(Path(path) / "corpusjson/")
    #        cls([
    #            {"dir_path": dir_path, **text_data}
    #            for text_data in catalogue["members"].values()
    #        ])

    def get_unique_values(self, whitelist) -> Dict[str, Set[str]]:
        """
        Useful for getting a list of all the unique values for a given field or fields.

        Args:
            whitelist (Set[str]): A set of field names to include in the unique values.

        Returns:
            Dict[str, Set[str]]: A dictionary where the keys are field names and the values are sets of unique values for each field.
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
        """Summarizes the properties of the corpus.

        Returns:
            dict: A dictionary where the key is the property name and the value is the percentage of texts that have a non-empty value for that property.
        """
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
