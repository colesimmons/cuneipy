from pydantic import Field
from .text_base import TextBase


class TextAdminEd1and2(TextBase):
    """
    An administrative text from the Early Dynastic I and II periods.
    """

    pass


class TextAdminEd3a(TextBase):
    """
    An administrative text from the Early Dynastic IIIa period.
    """

    pass


class TextAdminEd3b(TextBase):
    """
    An administrative text from the Early Dynastic IIIb period.
    """

    pass


class TextAdminOldAkk(TextBase):
    """
    An administrative text from the Old Akkadian period.
    """

    pass


class TextAdminLagash2(TextBase):
    """
    An administrative text from the Second Dynasty of Lagaš.
    """

    pass


class TextAdminUr3(TextBase):
    """
    An administrative text from the Third Dynasty of Ur.

    Only a small number of these extra fields are defined.
    """

    acquisition_history: str = ""
    ark_number: str = ""
    atf_source: str = ""
    atf_up: str = ""
    author: str = ""
    author_remarks: str = ""
    cdli_comments: str = ""
    citation: str = ""
    collection: str = ""
    date_entered: str = ""
    date_remarks: str = ""
    date_updated: str = ""
    dates_referenced: str = ""
    db_source: str = ""
    electronic_publication: str = ""
    external_id: str = ""
    google_earth_collection: str = ""
    height: str = ""
    id_: str = Field("", alias="id")
    id_text_int: str = ""
    lineart_up: str = ""
    material: str = ""
    object_remarks: str = ""
    photo_up: str = ""
    provenience_remarks: str = ""
    publication_date: str = ""
    published_collation: str = ""
    seal_id: str = ""
    seal_information: str = ""
    subgenre_remarks: str = ""
    thickness: str = ""
    translation_source: str = ""
    width: str = ""
