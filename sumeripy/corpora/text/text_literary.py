from .text_base import TextBase


class TextLiteraryEarly(TextBase):
    """
    An early literary text.
    """

    id_composite: str = ""
    keywords: str = ""
    place: str = ""


class TextLiteraryOldBab(TextBase):
    """
    A literary text from the Old Babylonian period.
    """

    chap: str = ""
    distribution: str = ""
    id_composite: str = ""
    keywords: str = ""
    place: str = ""
    provdist: str = ""
    sec1: str = ""
    sec2: str = ""
    sources: str = ""
