from typing import Union

from .text_admin import (
    TextAdminEd1and2,
    TextAdminEd3a,
    TextAdminEd3b,
    TextAdminOldAkk,
    TextAdminLagash2,
    TextAdminUr3,
)
from .text_literary import TextLiteraryEarly, TextLiteraryOldBab
from .text_other import (
    TextIncantations,
    TextLiturgies,
    TextRoyal,
    TextUdughul,
    TextVaria,
)

Text = Union[
    TextAdminEd1and2,
    TextAdminEd3a,
    TextAdminEd3b,
    TextAdminOldAkk,
    TextAdminLagash2,
    TextAdminUr3,
    TextLiteraryEarly,
    TextLiteraryOldBab,
    TextRoyal,
    TextIncantations,
    TextUdughul,
    TextLiturgies,
    TextVaria,
]
