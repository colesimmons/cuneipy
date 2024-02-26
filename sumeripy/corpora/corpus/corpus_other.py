from .corpus_base import CorpusBase
from ..text import (
    TextIncantations,
    TextLiturgies,
    TextRoyal,
    TextUdughul,
    TextVaria,
)


class CorpusIncantations(CorpusBase[TextIncantations]):
    """ """

    def load(self, texts):
        self.texts = [TextIncantations(**text) for text in texts]


class CorpusLiturgies(CorpusBase[TextLiturgies]):
    """ """

    def load(self, texts):
        self.texts = [TextLiturgies(**text) for text in texts]


class CorpusRoyal(CorpusBase[TextRoyal]):
    """ """

    def load(self, texts):
        self.texts = [TextRoyal(**text) for text in texts]


class CorpusUdughul(CorpusBase[TextUdughul]):
    """ """

    def load(self, texts):
        self.texts = [TextUdughul(**text) for text in texts]


class CorpusVaria(CorpusBase[TextVaria]):
    """ """

    def load(self, texts):
        self.texts = [TextVaria(**text) for text in texts]
