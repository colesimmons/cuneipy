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
from .corpus_type import CorpusType
from .types import Corpus


__all__ = [
    # Possible corpora
    "CorpusType",
    # Union type
    "Corpus",
    # Corpora – Admin
    "CorpusAdminEd1and2",
    "CorpusAdminEd3a",
    "CorpusAdminEd3b",
    "CorpusAdminLagash2",
    "CorpusAdminOldAkk",
    "CorpusAdminUr3",
    # Corpora – Literary
    "CorpusLiteraryEarly",
    "CorpusLiteraryOldBab",
    # Corpora – Other
    "CorpusIncantations",
    "CorpusLiturgies",
    "CorpusRoyal",
    "CorpusUdughul",
    "CorpusVaria",
]
