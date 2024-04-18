from .text_base import TextBase


class TextIncantations(TextBase):
    """
    An incantation text.
    """

    pass


class TextLiturgies(TextBase):
    """
    A liturgical text.
    """

    pass


class TextRoyal(TextBase):
    """
    A royal text.
    """

    @property
    def file_id(self) -> str:
        if not self.id_text:
            return self.id_composite
        return self.id_text

    distribution: str = ""
    id_composite: str = ""
    keywords: str = ""
    place: str = ""
    primary_edition: str = ""
    provdist: str = ""
    ruler: str = ""
    sources: str = ""


class TextUdughul(TextBase):
    """
    An text with instructions on warding off udug.
    """

    pass


class TextVaria(TextBase):
    """
    A text containing practical varia.
    """

    pass
