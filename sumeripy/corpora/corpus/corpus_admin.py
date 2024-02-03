from .corpus_base import CorpusBase
from ..text import (
    TextAdminEd1and2,
    TextAdminEd3a,
    TextAdminEd3b,
    TextAdminOldAkk,
    TextAdminLagash2,
    TextAdminUr3,
)


class CorpusAdminEd1and2(CorpusBase[TextAdminEd1and2]):
    """ """

    def load(self, texts):
        self.texts = [TextAdminEd1and2(**text) for text in texts]


class CorpusAdminEd3a(CorpusBase[TextAdminEd3a]):
    """ """

    def load(self, texts):
        self.texts = [TextAdminEd3a(**text) for text in texts]


class CorpusAdminEd3b(CorpusBase[TextAdminEd3b]):
    """ """

    def load(self, texts):
        self.texts = [TextAdminEd3b(**text) for text in texts]


class CorpusAdminOldAkk(CorpusBase[TextAdminOldAkk]):
    """ """

    def load(self, texts):
        self.texts = [TextAdminOldAkk(**text) for text in texts]


class CorpusAdminLagash2(CorpusBase[TextAdminLagash2]):
    """ """

    def load(self, texts):
        self.texts = [TextAdminLagash2(**text) for text in texts]


class CorpusAdminUr3(CorpusBase[TextAdminUr3]):
    """ """

    def load(self, texts):
        self.texts = [TextAdminUr3(**text) for text in texts]
