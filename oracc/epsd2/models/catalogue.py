"""
"""
from typing import Dict, List
from pydantic import Field
from oracc.epsd2.models.utils import BaseModel, OraccFileBase
from oracc.epsd2.utils import load_json


class _CatalogueItem(BaseModel):
    """ """

    accession_no: str = Field(
        "",
        alias="accession_no",
        description="Accession number assigned by the repository",
        example="1896-06-12, 0089",
    )
    accounting_period: str = Field(
        "",
        alias="accounting_period",
        description="Accounting period during which the item was acquired or catalogued",
        example="Enentarzi.01.00.00 to Enentarzi.04.00.00 ?",
    )
    acquisition_history: str = Field(
        "",
        alias="acquisition_history",
        description="History of how the item was acquired",
        example="check",
    )
    additional_p_numbers: str = Field(
        "",
        alias="additional_p_numbers",
        description="Additional identification numbers",
        example="P373870 (K 13619)",
    )
    alternative_years: str = Field(
        "",
        alias="alternative_years",
        description="Alternative years or time periods associated with the item",
        example="SH25 SH32 IS03",
    )
    ark: str = Field(
        "",
        alias="ark",
        description="Archival Resource Key for the item",
        example="21198/zz001s91nk",
    )
    ark_number: str = Field(
        "",
        alias="ark_number",
        description="Another form of Archival Resource Key",
        example="21198/zz001q0qmv",
    )
    atf_source: str = Field(
        "",
        alias="atf_source",
        description="Source of ATF data",
        example="Foxvog, Daniel A.",
    )
    atf_up: str = Field(
        "",
        alias="atf_up",
        description="Date of the last ATF update",
        example="20181201 firth",
    )
    author: str = Field(
        "",
        alias="author",
        description="Author of the item or document",
        example="Langdon, Stephen H.",
    )
    author_remarks: str = Field(
        "",
        alias="author_remarks",
        description="Additional remarks about the author or item",
        example="Chicago Stone. Isin",
    )
    bibliography__book_title: str = Field(
        "",
        alias="bibliography__book_title",
        description="Title of the book where the item is cited or discussed",
        example="Babylonian and Assyrian Text Commentaries: Origins of Interpretation",
    )
    bibliography__id_biblio: str = Field(
        "",
        alias="bibliography__id_biblio",
        description="Identifier for the bibliographic entry",
        example="R000285",
    )
    bibliography__journal_title: str = Field(
        "",
        alias="bibliography__journal_title",
        description="Title of the journal where the item is cited or discussed",
        example="Archiv für Orientforschung",
    )
    bibliography__shortref: str = Field(
        "",
        alias="bibliography__shortref",
        description="Short reference for the bibliographic entry",
        example="Frahm 2011",
    )
    bibliography__volume_number: str = Field(
        "",
        alias="bibliography__volume_number",
        description="Volume number of the journal or book",
        example="1",
    )
    catchline: str = Field(
        "",
        alias="catchline",
        description="Catchline or summary of the item's content",
        example="not preserved",
    )
    cdli_collation: str = Field(
        "",
        alias="cdli_collation",
        description="Collation information from the CDLI (Cuneiform Digital Library Initiative)",
        example="dahl",
    )
    cdli_comments: str = Field(
        "",
        alias="cdli_comments",
        description="Comments or notes from the CDLI",
        example="20130126 englund: collated BM 5.89; discussed by J. Friberg, AfO 44/45 (1997/98) 052",
    )
    cdli_problems: str = Field(
        "",
        alias="cdli_problems",
        description="Known issues or problems noted by the CDLI",
        example="2ndary publ: MSL 14, p.87",
    )
    checked: str = Field(
        "",
        alias="checked",
        description="Date when the item was last checked or verified",
        example="09/07/2010",
    )
    citation: str = Field(
        "",
        alias="citation",
        description="Citation information for the item",
        example="Powell 1973, 100; Edzard, Dietz, ZA 66, 163; Pomponio 1987, XIII",
    )
    collection: str = Field(
        "",
        alias="collection",
        description="Collection to which the item belongs",
        example="Ashmolean Museum, Oxford, UK",
    )
    collection_copyright: str = Field(
        "",
        alias="collection_copyright",
        description="Copyright information for the collection",
        example="<http://cdli.ucla.edu/collections/ashmolean/ashmolean_copyright.html>",
    )
    colophon_disclosing_author: str = Field(
        "",
        alias="colophon_disclosing_author",
        description="Colophon information disclosing the author",
        example="not preserved",
    )
    colophon_describing_source: str = Field(
        "",
        alias="colophon_describing_source",
        description="Colophon information describing the source or origin",
        example="not preserved",
    )
    composite_id: str = Field(
        "",
        alias="composite_id",
        description="Identifier for composite items",
        example="Q006205",
    )
    condition_description: str = Field(
        "",
        alias="condition_description",
        description="Description of the item's physical condition",
        example="reddish hard stone, with an inscription on two faces and on three edges.",
    )
    copy_: str = Field(
        "", alias="copy", description="Indicates if the item is a copy", example="mine"
    )
    created_by: str = Field(
        "",
        alias="created_by",
        description="Person who created the catalogue entry",
        example="Jamie Novotny",
    )
    created_on: str = Field(
        "",
        alias="created_on",
        description="Date when the catalogue entry was created",
        example="3/26/2021 3:54:11 PM",
    )
    credits: str = Field(
        "",
        alias="credits",
        description="Credits for the edition or translation",
        example="Edition by Marco Bonechi",
    )
    date_entered: str = Field(
        "",
        alias="date_entered",
        description="Date when the item was entered into the catalogue",
        example="12/4/2001",
    )
    date_of_origin: str = Field(
        "",
        alias="date_of_origin",
        description="Date or period of the item's origin",
        example="Lugalanda.00.00.00 ?",
    )
    date_remarks: str = Field(
        "",
        alias="date_remarks",
        description="Additional remarks about the date or period of the item",
        example="Quradum archive",
    )
    date_updated: str = Field(
        "",
        alias="date_updated",
        description="Date when the item was last updated",
        example="2018-10-20",
    )
    dates_referenced: str = Field(
        "",
        alias="dates_referenced",
        description="Dates or periods referenced within the item",
        example="Lugalanda.00.00.00 ?",
    )
    db_source: str = Field(
        "",
        alias="db_source",
        description="Source database for the item",
        example="20011204 protocuneiform_catalogue",
    )
    designation: str = Field(
        "",
        alias="designation",
        description="Designation or label for the item",
        example="OECT 07, 013",
    )
    dumb: str = Field(
        "",
        alias="dumb",
        description="Unspecified attribute, possibly for internal use",
        example="SI.A-a archive",
    )
    dumb2: str = Field(
        "",
        alias="dumb2",
        description="Another unspecified attribute, possibly for internal use",
        example="In the OLP 4 publication this tablet listed as kept at the Katholieke Universiteit Leuven;",
    )
    editor: str = Field(
        "",
        alias="editor",
        description="Editor of the item",
        example="Marie-Françoise Besnier",
    )
    electronic_publication: str = Field(
        "",
        alias="electronic_publication",
        description="URL for the electronic publication of the item",
        example="http://courses.smsu.edu/mac566f/DykeCollege/dykecollege.htm",
    )
    elevation: str = Field(
        "",
        alias="elevation",
        description="Elevation information, possibly related to the findspot",
        example="check",
    )
    excavation_no: str = Field(
        "",
        alias="excavation_no",
        description="Excavation number for the item",
        example="U 12965",
    )
    external_id: str = Field(
        "",
        alias="external_id",
        description="External identifier for the item",
        example="bdtns:015742",
    )
    findspot: str = Field(
        "",
        alias="findspot",
        description="Location where the item was found",
        example="palace room 108",
    )
    findspot_remarks: str = Field(
        "",
        alias="findspot_remarks",
        description="Additional remarks about the findspot",
        example="Area I dump",
    )
    findspot_square: str = Field(
        "",
        alias="findspot_square",
        description="Square or section of the findspot",
        example="SE",
    )
    funder: str = Field(
        "",
        alias="funder",
        description="Entity that funded the excavation or research",
        example="UK Arts and Humanities Research Council",
    )
    genre: str = Field(
        "",
        alias="genre",
        description="Genre of the item, e.g., Administrative, Literary",
        example="Administrative",
    )
    google_earth_collection: str = Field(
        "",
        alias="google_earth_collection",
        description="Coordinates for Google Earth, possibly related to the findspot",
        example="51 31.162' N, 00 7.627' W",
    )
    has_score: str = Field(
        "",
        alias="has_score",
        description="Indicates if the item has a score, possibly a quality or importance score",
        example="1",
    )
    has_sources: str = Field(
        "",
        alias="has_sources",
        description="Indicates if the item has sources or references",
        example="1",
    )
    height: str = Field(
        "",
        alias="height",
        description="Height of the item, possibly in a standard unit",
        example="?",
    )
    id_: str = Field(
        "", alias="id", description="Unique identifier for the item", example="5086"
    )
    id_composite: str = Field(
        "",
        alias="id_composite",
        description="Identifier for the composite item, if applicable",
        example="Q009323",
    )
    id_text: str = Field(
        "",
        alias="id_text",
        description="Text identifier for the item",
        example="P005311",
    )
    id_text_int: str = Field(
        "",
        alias="id_text_int",
        description="Integer form of the text identifier",
        example="5311",
    )
    images: List[str] = Field(
        [],
        alias="images",
        description="List of image URLs or identifiers related to the item",
        example=[],
    )
    join_information: str = Field(
        "",
        alias="join_information",
        description="Information about how this item joins with others, if applicable",
        example="P010103 lead, single entry",
    )
    keywords: str = Field(
        "",
        alias="keywords",
        description="Keywords associated with the item",
        example="zame, hymns, ED IIIb",
    )
    langs: str = Field(
        "",
        alias="langs",
        description="Language codes associated with the item",
        example="0x02000000",
    )
    language: str = Field(
        "",
        alias="language",
        description="Primary language of the item",
        example="Sumerian",
    )
    language_remarks: str = Field(
        "",
        alias="language_remarks",
        description="Additional remarks about the language",
        example="Akkadian",
    )
    last_modified: str = Field(
        "",
        alias="last_modified",
        description="Date and time when the item was last modified",
        example="23/02/2013 14:31:24",
    )
    last_modified_by: str = Field(
        "",
        alias="last_modified_by",
        description="Person who last modified the item",
        example="Jamie Novotny",
    )
    last_modified_on: str = Field(
        "",
        alias="last_modified_on",
        description="Date when the item was last modified",
        example="4/2/2021 7:06:58 AM",
    )
    lemmed: str = Field(
        "",
        alias="lemmed",
        description="Date when the item was lemmatized",
        example="08/12/2009",
    )
    lineart_up: str = Field(
        "",
        alias="lineart_up",
        description="Information about line art updates, possibly resolution",
        example="150ppi 20160630",
    )
    material: str = Field(
        "",
        alias="material",
        description="Material from which the item is made",
        example="clay",
    )
    museum_no: str = Field(
        "",
        alias="museum_no",
        description="Museum number for the item",
        example="Ashm 1928-0017",
    )

    new_q: str = Field(
        "", alias="new_q", description="New query identifier", example="Q001016"
    )
    non_sign_list_series: str = Field(
        "",
        alias="Non_Sign_List_Series",
        description="Non-sign list series",
        example="metro, list",
    )
    notes: str = Field(
        "",
        alias="notes",
        description="Notes on the field",
        example="updated from Tinney file 1/24/2006",
    )
    object_type: str = Field(
        "", alias="object_type", description="Type of object", example="tablet"
    )
    object_preservation: str = Field(
        "",
        alias="object_preservation",
        description="Object preservation status",
        example="25%",
    )
    object_remarks: str = Field(
        "",
        alias="object_remarks",
        description="Remarks on the object",
        example="kudurru",
    )
    other_names: str = Field(
        "",
        alias="other_names",
        description="Other names or references",
        example="Steible: Enanatum I 32",
    )
    owner: str = Field(
        "",
        alias="owner",
        description="Owner of the object",
        example="Ashmolean Museum, Oxford, UK",
    )
    p_number_problems: str = Field(
        "",
        alias="P_number_problems",
        description="Problems with P number",
        example="no P number",
    )
    parallels: str = Field(
        "",
        alias="parallels",
        description="Parallel references",
        example="dcclt:P274929 dcclt:P349861",
    )
    period: str = Field(
        "",
        alias="period",
        description="Historical period",
        example="Early Dynastic IIIa",
    )
    period_remarks: str = Field(
        "",
        alias="period_remarks",
        description="Remarks on the period",
        example="reign of MUG-si or e2-IGI.NIM-pa-e3",
    )
    photo: str = Field(
        "", alias="photo", description="Photo identifier", example="cdli"
    )
    photo_up: str = Field(
        "",
        alias="photo_up",
        description="Photo upload details",
        example="600ppi 20160630",
    )
    photographed: str = Field(
        "", alias="photographed", description="Date photographed", example="15/01/2008"
    )
    photographer: str = Field(
        "", alias="photographer", description="Name of photographer", example="Philippe"
    )
    place: str = Field(
        "", alias="place", description="Place of origin", example="Abu Salabikh"
    )
    pleiades_id: str = Field(
        "", alias="pleiades_id", description="Pleiades ID", example="912985"
    )
    pleiades_coord: str = Field(
        "",
        alias="pleiades_coord",
        description="Pleiades coordinates",
        example="[46.104748,30.961580]",
    )
    pr_joins__pages: str = Field(
        "",
        alias="pr_joins__pages",
        description="Pages where joins are discussed",
        example="88-9, 100, 102-3, 108, 206-8, 293-4, 297, 336",
    )
    principal: str = Field(
        "",
        alias="principal",
        description="Principal researcher",
        example="Eleanor Robson",
    )
    primary_edition: str = Field(
        "",
        alias="primary_edition",
        description="Primary edition reference",
        example="RIME 3/1, E3/1.1.2.100add",
    )
    primary_publication: str = Field(
        "",
        alias="primary_publication",
        description="Primary publication reference",
        example="OECT 07, 013",
    )
    proof_read: str = Field(
        "", alias="proof-read", description="Proofread date", example="12/12/2009"
    )
    proof_reader: str = Field(
        "",
        alias="proof-reader",
        description="Name of proofreader",
        example="Eleanor Robson",
    )
    project: str = Field(
        "", alias="project", description="Project name", example="epsd2/admin/ed3a"
    )
    provenience: str = Field(
        "",
        alias="provenience",
        description="Provenience of the object",
        example="Kish (mod. Tell Uhaimir)",
    )
    provenience_remarks: str = Field(
        "",
        alias="provenience_remarks",
        description="Remarks on provenience",
        example="Uruk ?",
    )
    public: str = Field("", alias="public", description="Is it public?", example="no")
    publication_date: str = Field(
        "", alias="publication_date", description="Date of publication", example="1928"
    )
    publication_history: str = Field(
        "",
        alias="publication_history",
        description="Publication history",
        example="Watelin, Louis C. & Langdon, Stephen H., EK 4, pl. 44, no. 7, W 1928-17; Westenholz, Aage, CUSAS 26 (2014) 019",
    )
    published_collation: str = Field(
        "",
        alias="published_collation",
        description="Published collation reference",
        example="Or Ant. 22, 84",
    )
    record_id: str = Field(
        "", alias="record_id", description="Record ID", example="2611"
    )
    reference: str = Field(
        "", alias="reference", description="Reference ID", example="P227713"
    )
    repository: str = Field(
        "",
        alias="repository",
        description="Repository details",
        example="DSpace@Cambridge, University of Cambridge",
    )
    royal_colophon: str = Field(
        "",
        alias="royal_colophon",
        description="Royal colophon details",
        example="not preserved",
    )
    ruler: str = Field("", alias="ruler", description="Ruler name", example="Gungunum")
    seal_id: str = Field("", alias="seal_id", description="Seal ID", example="Sx")
    seal_information: str = Field(
        "",
        alias="seal_information",
        description="Information on the seal",
        example="sealed; inscription: il2",
    )
    series: str = Field("", alias="series", description="Series name", example="Šulgi")
    series_section: str = Field(
        "",
        alias="series_section",
        description="Section of the series",
        example="2135add",
    )
    series_tablet_no: str = Field(
        "",
        alias="series_tablet_no",
        description="Tablet number in the series",
        example="Syllabary B",
    )
    series_2: str = Field(
        "",
        alias="series_2",
        description="Secondary series name",
        example="OB Nippur Diri",
    )
    sources: str = Field(
        "", alias="sources", description="Source references", example="P498296"
    )
    special_features: str = Field(
        "",
        alias="special_features",
        description="Special features of the text",
        example="extract text",
    )
    status: str = Field(
        "", alias="status", description="Status of the object", example="active"
    )
    stratigraphic_level: str = Field(
        "", alias="stratigraphic_level", description="Stratigraphic level", example="3"
    )
    subgenre: str = Field(
        "", alias="subgenre", description="Subgenre of the text", example="God List"
    )
    subgenre_remarks: str = Field(
        "",
        alias="subgenre_remarks",
        description="Remarks on the subgenre",
        example="field purchase.",
    )
    supergenre: str = Field(
        "", alias="supergenre", description="Supergenre of the text", example="ELA"
    )
    surface_preservation: str = Field(
        "",
        alias="surface_preservation",
        description="Surface preservation status",
        example="Excellent",
    )
    tablet_number_2: str = Field(
        "", alias="tablet_number_2", description="Secondary tablet number", example="03"
    )
    text_remarks: str = Field(
        "",
        alias="text_remarks",
        description="Remarks on the text",
        example="irrigation fee",
    )
    textual_colophon: str = Field(
        "",
        alias="textual_colophon",
        description="Textual colophon details",
        example="not preserved",
    )
    thickness: str = Field(
        "", alias="thickness", description="Thickness of the object", example="?"
    )
    trans: str = Field(
        "", alias="trans", description="Translation status", example="en"
    )
    translit_ed: str = Field(
        "",
        alias="translit_ed",
        description="Transliteration edition date",
        example="30/11/2009",
    )
    translation_source: str = Field(
        "",
        alias="translation_source",
        description="Source of translation",
        example="no translation",
    )
    uploaded: str = Field(
        "", alias="uploaded", description="Upload date", example="09/07/2010"
    )
    uri: str = Field(
        "",
        alias="uri",
        description="URI for the object",
        example="http://cdli.ucla.edu/P005311",
    )
    user: str = Field(
        "", alias="user", description="User who uploaded the data", example="Admin"
    )
    width: str = Field(
        "", alias="width", description="Width of the object", example="?"
    )
    xproject: str = Field(
        "", alias="xproject", description="Cross-project identifier", example="CDLI"
    )


class Catalogue(OraccFileBase):
    """
    Although projects may have their own catalogue fields, all projects provide at least one of id_text or id_composite (some use a mix); designation; period; and provenience.
    """

    members: Dict[str, _CatalogueItem] = Field(
        ..., alias="members", description="", example={}
    )
    summaries: Dict[str, str] = Field(
        ..., alias="summaries", description="", example={}
    )

    @classmethod
    def load(cls) -> "Catalogue":
        """Loads the JSON data and instantiates the class."""
        data = load_json("catalogue.json")
        return cls(**data)


__all__ = ["Catalogue"]
