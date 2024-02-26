from .text_base import TextBase


class TextLiteraryEarly(TextBase):
    """
    An early literary text.
    """

    id_composite: str = ""
    keywords: str = ""
    place: str = ""

    @property
    def file_id(self) -> str:
        return self.id_composite if self.id_composite else self.id_text


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

    @property
    def file_id(self) -> str:
        return self.id_composite if self.id_composite else self.id_text
