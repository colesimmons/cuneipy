"""
CorpusType
"""

from enum import Enum

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


class CorpusType(str, Enum):
    """
    Enum representing the available corpora.

    http://oracc.museum.upenn.edu/epsd2/json/
    """

    # ------------------------
    # Administrative Texts
    # ------------------------

    # Early Dynastic I-II (Administrative)
    ADMIN_ED_1_2 = "admin_ed12"

    # Early Dynastic IIIa (Administrative)
    ADMIN_ED_3A = "admin_ed3a"

    # Early Dynastic IIIb (Administrative)
    ADMIN_ED_3B = "admin_ed3b"

    # Ebla (Administrative)
    # ADMIN_EBLA = "admin_ebla" # TODO

    # Old Akkadian (Administrative)
    ADMIN_OAKK = "admin_oakk"

    # Second Dynasty of Lagaš (Administrative)
    ADMIN_LAGASH2 = "admin_lagash2"

    # Third Dynasty of Ur (Administrative)
    ADMIN_UR3 = "admin_ur3"

    # Old Babylonian (Administrative)
    # ADMIN_OLDBAB = "admin_oldbab" # TODO

    # ------------------------
    # Other
    # ------------------------
    # Literary - pre-OB
    LITERARY_EARLY = "early_lit"  # TODO: lit_early

    # Literary - Old Babylonian
    LITERARY_OLDBAB = "oldbab_lit"

    # Royal
    ROYAL = "royal"

    # Incantations
    INCANTATIONS = "incantations"

    # Liturgies
    LITURGIES = "liturgies"

    # Udughul
    UDUGHUL = "udughul"

    # Practical Varia
    PRACTICAL_VARIA = "varia"

    @property
    def url(self) -> str:
        """
        Returns the download URL for the given corpus.

        Defined at: http://oracc.museum.upenn.edu/epsd2/json/

        Raises:
          ValueError: If the corpus is invalid.
        """

        base = "http://oracc.museum.upenn.edu/json/"
        type_to_filename = {
            CorpusType.ADMIN_ED_1_2: "epsd2-admin-ed12",
            CorpusType.ADMIN_ED_3A: "epsd2-admin-ed3a",
            CorpusType.ADMIN_ED_3B: "epsd2-admin-ed3b",
            # CorpusType.ADMIN_EBLA: "epsd2-admin-ebla",
            CorpusType.ADMIN_OAKK: "epsd2-admin-oakk",
            CorpusType.ADMIN_LAGASH2: "epsd2-admin-lagash2",
            CorpusType.ADMIN_UR3: "epsd2-admin-ur3",
            # CorpusType.ADMIN_OLDBAB: "epsd2-admin/oldbab",
            CorpusType.LITERARY_EARLY: "epsd2-earlylit",
            CorpusType.LITERARY_OLDBAB: "epsd2-literary",
            CorpusType.ROYAL: "epsd2-royal",
            CorpusType.INCANTATIONS: "epsd2-praxis",
            CorpusType.UDUGHUL: "epsd2-praxis-udughul",
            CorpusType.LITURGIES: "epsd2-praxis-liturgy",
            CorpusType.PRACTICAL_VARIA: "epsd2-praxis-varia",
        }
        if self in type_to_filename:
            return f"{base}{type_to_filename[self]}.zip"
        raise ValueError("Invalid corpus")

    @property
    def model(self):
        type_to_model = {
            CorpusType.ADMIN_ED_1_2: CorpusAdminEd1and2,
            CorpusType.ADMIN_ED_3A: CorpusAdminEd3a,
            CorpusType.ADMIN_ED_3B: CorpusAdminEd3b,
            # CorpusType.ADMIN_EBLA: TextAdminEbla,
            CorpusType.ADMIN_OAKK: CorpusAdminOldAkk,
            CorpusType.ADMIN_LAGASH2: CorpusAdminLagash2,
            CorpusType.ADMIN_UR3: CorpusAdminUr3,
            # CorpusType.ADMIN_OLDBAB: TextAdminOldBab,
            CorpusType.LITERARY_EARLY: CorpusLiteraryEarly,
            CorpusType.LITERARY_OLDBAB: CorpusLiteraryOldBab,
            CorpusType.ROYAL: CorpusRoyal,
            CorpusType.INCANTATIONS: CorpusIncantations,
            CorpusType.UDUGHUL: CorpusUdughul,
            CorpusType.LITURGIES: CorpusLiturgies,
            CorpusType.PRACTICAL_VARIA: CorpusVaria,
        }
        if self in type_to_model:
            return type_to_model[self]
        raise ValueError("Invalid corpus")
