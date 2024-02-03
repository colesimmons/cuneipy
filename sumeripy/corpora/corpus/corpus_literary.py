from .corpus_base import CorpusBase
from ..text import TextLiteraryEarly, TextLiteraryOldBab


class CorpusLiteraryEarly(CorpusBase[TextLiteraryEarly]):
    """ """

    def load(self, texts):
        self.texts = [TextLiteraryEarly(**text) for text in texts]


class CorpusLiteraryOldBab(CorpusBase[TextLiteraryOldBab]):
    """ """

    def load(self, texts):
        self.texts = [TextLiteraryOldBab(**text) for text in texts]
