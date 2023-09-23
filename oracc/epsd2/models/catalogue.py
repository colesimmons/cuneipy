"""
"""
from typing import Dict, List
from pydantic import Field
from oracc.epsd2.models.shared import BaseModel, OraccFileBase


class _CatalogueItem(BaseModel):
    """
    Lorem ipsum
    """

    accession_no: str = Field("", description="", example="1896-06-12, 0089")
    accounting_period: str = Field(
        "", description="", example="Enentarzi.01.00.00 to Enentarzi.04.00.00 ?"
    )
    acquisition_history: str = Field("", description="", example="check")
    additional_p_numbers: str = Field(
        "", alias="Additional_P_numbers", description="", example="P373870 (K 13619)"
    )
    alternative_years: str = Field("", description="", example="SH25 SH32 IS03")
    ark: str = Field("", description="", example="21198/zz001s91nk")
    ark_number: str = Field("", description="", example="21198/zz001q0qmv")
    atf_source: str = Field("", description="", example="Foxvog, Daniel A.")
    atf_up: str = Field("", description="", example="20181201 firth")
    author: str = Field("", description="", example="Langdon, Stephen H.")
    author_remarks: str = Field("", description="", example="Chicago Stone. Isin")
    bibliography__book_title: str = Field(
        "",
        description="",
        example="Babylonian and Assyrian Text Commentaries: Origins of Interpretation",
    )
    bibliography__id_biblio: str = Field("", description="", example="R000285")
    bibliography__journal_title: str = Field(
        "", description="", example="Archiv für Orientforschung"
    )
    bibliography__shortref: str = Field("", description="", example="Frahm 2011")
    bibliography__volume_number: str = Field("", description="", example="1")
    catchline: str = Field("", description="", example="not preserved")
    cdli_collation: str = Field(
        "",
        description="",
        example="dahl",
    )
    cdli_comments: str = Field(
        "",
        description="",
        example="20130126 englund: collated BM 5.89; discussed by J. Friberg, AfO 44/45 (1997/98) 052",
    )
    cdli_problems: str = Field(
        "",
        description="",
        example="2ndary publ: MSL 14, p.87",
        alias="CDLI_problems",
    )
    checked: str = Field("", description="", example="09/07/2010")
    citation: str = Field(
        "",
        description="",
        example="Powell 1973, 100; Edzard, Dietz, ZA 66, 163; Pomponio 1987, XIII",
    )
    collection: str = Field("", description="", example="Ashmolean Museum, Oxford, UK")
    collection_copyright: str = Field(
        "",
        description="",
        example="<http://cdli.ucla.edu/collections/ashmolean/ashmolean_copyright.html>",
    )
    colophon_disclosing_author: str = Field("", description="", example="not preserved")
    colophon_describing_source: str = Field("", description="", example="not preserved")
    composite_id: str = Field("", description="", example="Q006205")
    condition_description: str = Field(
        "",
        description="",
        example="reddish hard stone, with an inscription on two faces and on three edges.",
    )
    copy_: str = Field("", alias="copy", description="", example="mine")
    created_by: str = Field("", description="", example="Jamie Novotny")
    created_on: str = Field("", description="", example="3/26/2021 3:54:11 PM")
    credits: str = Field("", description="", example="Edition by Marco Bonechi")
    date_entered: str = Field("", description="", example="12/4/2001")  # TODO
    date_of_origin: str = Field("", description="", example="Lugalanda.00.00.00 ?")
    date_remarks: str = Field("", description="", example="Quradum archive")
    date_updated: str = Field("", description="", example="2018-10-20")  # TODO
    dates_referenced: str = Field("", description="", example="Lugalanda.00.00.00 ?")
    db_source: str = Field(
        "", description="", example="20011204 protocuneiform_catalogue"
    )
    designation: str = Field(..., description="", example="OECT 07, 013")
    dumb: str = Field("", description="", example="SI.A-a archive")
    dumb2: str = Field(
        "",
        description="",
        example="In the OLP 4 publication this tablet listed as kept at the Katholieke Universiteit Leuven;",
    )
    editor: str = Field("", description="", example="Marie-Françoise Besnier")
    electronic_publication: str = Field(
        "",
        description="",
        example="http://courses.smsu.edu/mac566f/DykeCollege/dykecollege.htm",
    )
    elevation: str = Field(
        "",
        description="",
        example="check",
    )
    excavation_no: str = Field("", description="", example="U 12965")
    external_id: str = Field("", description="", example="bdtns:015742")
    findspot: str = Field("", description="", example="palace room 108")
    findspot_remarks: str = Field("", description="", example="Area I dump")
    findspot_square: str = Field("", description="", example="SE")
    funder: str = Field(
        "", description="", example="UK Arts and Humanities Research Council"
    )
    genre: str = Field("", description="", example="Administrative")
    google_earth_collection: str = Field(
        "", description="", example="51 31.162' N, 00 7.627' W"
    )
    has_score: str = Field("", alias="has-score", description="", example="1")
    has_sources: str = Field("", description="", example="1", alias="has-sources")
    height: str = Field("", description="", example="?")
    id_: str = Field("", description="", example="5086", alias="id")
    id_composite: str = Field("", description="", example="Q009323")
    id_text: str = Field("", description="", example="P005311")
    id_text_int: str = Field("", description="", example="5311")
    images: List[str] = Field([], description="", example=[])
    join_information: str = Field(
        "", description="", example="P010103 lead, single entry"
    )
    keywords: str = Field("", description="", example="zame, hymns, ED IIIb")
    langs: str = Field("", description="", example="0x02000000")
    language: str = Field("", description="", example="Sumerian")
    language_remarks: str = Field("", description="", example="Akkadian")
    last_modified: str = Field("", description="", example="23/02/2013 14:31:24")
    last_modified_by: str = Field("", description="", example="Jamie Novotny")
    last_modified_on: str = Field("", description="", example="4/2/2021 7:06:58 AM")
    lemmed: str = Field("", description="", example="08/12/2009")
    lineart_up: str = Field("", description="", example="150ppi 20160630")
    material: str = Field("", description="", example="clay")
    museum_no: str = Field("", description="", example="Ashm 1928-0017")
    new_q: str = Field("", description="", example="Q001016")
    non_sign_list_series: str = Field(
        "", description="", example="metro, list", alias="Non_Sign_List_Series"
    )
    notes: str = Field("", description="", example="updated from Tinney file 1/24/2006")
    object_type: str = Field("", description="", example="tablet")
    object_preservation: str = Field("", description="", example="25%")
    object_remarks: str = Field("", description="", example="kudurru")
    other_names: str = Field("", description="", example="Steible: Enanatum I 32")
    owner: str = Field("", description="", example="Ashmolean Museum, Oxford, UK")
    p_number_problems: str = Field(
        "", alias="P_number_problems", description="", example="no P number"
    )
    parallels: str = Field("", description="", example="dcclt:P274929 dcclt:P349861")
    period: str = Field("", description="", example="Early Dynastic IIIa")
    period_remarks: str = Field(
        "", description="", example="reign of MUG-si or e2-IGI.NIM-pa-e3"
    )
    photo: str = Field("", description="", example="cdli")
    photo_up: str = Field("", description="", example="600ppi 20160630")
    photographed: str = Field("", description="", example="15/01/2008")
    photographer: str = Field("", description="", example="Philippe")
    place: str = Field("", description="", example="Abu Salabikh")
    pleiades_id: str = Field("", description="", example="912985")
    pleiades_coord: str = Field("", description="", example="[46.104748,30.961580]")
    pr_joins__pages: str = Field(
        "", description="", example="88-9, 100, 102-3, 108, 206-8, 293-4, 297, 336"
    )
    principal: str = Field("", description="", example="Eleanor Robson")
    primary_edition: str = Field(
        "", description="", example="RIME 3/1, E3/1.1.2.100add"
    )
    primary_publication: str = Field("", description="", example="OECT 07, 013")
    proof_read: str = Field(
        "", alias="proof-read", description="", example="12/12/2009"
    )
    proof_reader: str = Field(
        "", alias="proof-reader", description="", example="Eleanor Robson"
    )
    project: str = Field(..., description="", example="epsd2/admin/ed3a")
    provenience: str = Field("", description="", example="Kish (mod. Tell Uhaimir)")
    provenience_remarks: str = Field("", description="", example="Uruk ?")
    public: str = Field("", description="", example="no")
    publication_date: str = Field("", description="", example="1928")
    publication_history: str = Field(
        "",
        description="",
        example="Watelin, Louis C. & Langdon, Stephen H., EK 4, pl. 44, no. 7, W 1928-17; Westenholz, Aage, CUSAS 26 (2014) 019",
    )
    published_collation: str = Field("", description="", example="Or Ant. 22, 84")
    record_id: str = Field("", description="", example="2611")
    reference: str = Field("", description="", example="P227713")
    repository: str = Field(
        "", description="", example="DSpace@Cambridge, University of Cambridge"
    )
    royal_colophon: str = Field("", description="", example="not preserved")
    ruler: str = Field("", description="", example="Gungunum")
    seal_id: str = Field("", description="", example="Sx")
    seal_information: str = Field(
        "", description="", example="sealed; inscription: il2"
    )
    series: str = Field("", description="", example="Šulgi")
    series_section: str = Field("", description="", example="2135add")
    series_tablet_no: str = Field("", description="", example="Syllabary B")
    series_2: str = Field("", description="", example="OB Nippur Diri")
    sources: str = Field("", description="", example="P498296")
    special_features: str = Field("", description="", example="extract text")
    status: str = Field("", description="", example="active")
    stratigraphic_level: str = Field("", description="", example="3")
    subgenre: str = Field("", description="", example="God List")
    subgenre_remarks: str = Field("", description="", example="field purchase.")
    supergenre: str = Field("", description="", example="ELA")
    surface_preservation: str = Field("", description="", example="Excellent")
    tablet_number_2: str = Field("", description="", example="03")
    text_remarks: str = Field("", description="", example="irrigation fee")
    textual_colophon: str = Field("", description="", example="not preserved")
    thickness: str = Field("", description="", example="?")
    trans: str = Field("", description="", example="en")
    translit_ed: str = Field("", description="", example="30/11/2009")
    translation_source: str = Field("", description="", example="no translation")
    uploaded: str = Field("", description="", example="09/07/2010")
    uri: str = Field("", description="", example="http://cdli.ucla.edu/P005311")
    user: str = Field("", description="", example="Admin")
    width: str = Field("", description="", example="?")
    xproject: str = Field("", description="", example="CDLI")


class Catalogue(OraccFileBase):
    """
    Although projects may have their own catalogue fields, all projects provide at least one of id_text or id_composite (some use a mix); designation; period; and provenience.
    """

    members: Dict[str, _CatalogueItem] = Field(..., description="", example={})
    summaries: Dict[str, str] = Field(..., description="", example={})


__all__ = ["Catalogue"]
