from typing import Union

from .corpus_admin import (
    CorpusAdminEd1and2,
    CorpusAdminEd3a,
    CorpusAdminEd3b,
    CorpusAdminLagash2,
    CorpusAdminOldAkk,
    CorpusAdminUr3,
)
from .corpus_literary import CorpusLiteraryEarly, CorpusLiteraryOldBab
from .corpus_other import (
    CorpusIncantations,
    CorpusLiturgies,
    CorpusRoyal,
    CorpusUdughul,
    CorpusVaria,
)

Corpus = Union[
    CorpusAdminEd1and2,
    CorpusAdminEd3a,
    CorpusAdminEd3b,
    CorpusAdminLagash2,
    CorpusAdminOldAkk,
    CorpusAdminUr3,
    CorpusLiteraryEarly,
    CorpusLiteraryOldBab,
    CorpusIncantations,
    CorpusLiturgies,
    CorpusRoyal,
    CorpusUdughul,
    CorpusVaria,
]
