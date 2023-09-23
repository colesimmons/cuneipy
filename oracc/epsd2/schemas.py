"""
Catalogue
Corpus
EPSDPortal
SignList
Glossary
IndexCat
IndexLem
IndexSux
Metadata
Sortcodes
"""
from typing import Dict, List, ForwardRef
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict


class BaseModel_(BaseModel):
    model_config = ConfigDict(extra="forbid")


class _OraccFileBase(BaseModel_):
    """Base schema for ePSD files"""

    type: str = Field(..., description="", example="corpus")
    project: str = Field(..., description="", example="epsd2")
    source: str = Field(..., description="", example="http://oracc.org/epsd2")
    license: str = Field(
        ..., description="", example="This data is released under the CC0 license"
    )
    license_url: str = Field(
        ...,
        description="",
        example="https://creativecommons.org/publicdomain/zero/1.0/",
        alias="license-url",
    )
    more_info: str = Field(
        ..., description="", example="http://oracc.org/doc/opendata/", alias="more-info"
    )
    timestamp: datetime = Field(
        ..., description="", example="2021-12-21T03:21:44", alias="UTC-timestamp"
    )


####################
# catalogue.json
####################
class CatalogueItem(BaseModel_):
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


class Catalogue(_OraccFileBase):
    """
    Although projects may have their own catalogue fields, all projects provide at least one of id_text or id_composite (some use a mix); designation; period; and provenience.
    """

    members: Dict[str, CatalogueItem] = Field(..., description="", example={})
    summaries: Dict[str, str] = Field(..., description="", example={})


####################
# corpus.json
####################
class Corpus(_OraccFileBase):
    """
    The JSON file corpus.json is another manifest file: it lists the individual text editions that are located in the folder corpusjson/:
    """

    proxies: Dict[str, str] = Field(..., description="", example={"P223478": "blms"})


####################
# epsd2-portal.json
####################
class Chunk(BaseModel_):
    type: str = Field(..., description="", example="h1")
    url: str = Field(..., description="", example="epsd2/index.html#d2e38")
    text: str = Field(..., description="", example="ePSD2 2.5 (2021-12-21)")


class EPSDPortal(_OraccFileBase):
    chunks: List[Chunk] = Field(..., description="", example=[])


####################
# epsd2-sl.json
####################
class _Modifier(BaseModel_):
    b: str = Field("", description="base?", example="MU\u0160\u2083")
    # https://build-oracc.museum.upenn.edu//ns/gdl/1.0/index.html#Modifier
    m: str = Field("", description="modifier?", example="g")
    a: str = Field("", description="", example="a")


_Sequence = ForwardRef("_Sequence")


class _Sequence(BaseModel_):
    s: str = Field("", description="Sign", example="A")
    # beside, joining, containing, above, crossing, opposing, repeated
    o: str = Field("", description="Operator types", example="beside")
    form: str = Field("", description="", example="MU\u0160\u2083@g")
    mods: List[_Modifier] = Field([], description="", example=[])
    m: str = Field("", description="", example="l")
    n: str = Field("", description="", example="n")
    r: str = Field("", description="", example="9")
    seq: List[_Sequence] = Field(
        [], description="", example=[{"s": "GI\u0160", "o": "beside"}]
    )


_Sequence.update_forward_refs()


class _GDL(BaseModel_):
    """GDL = Grapheme Description Language"""

    c: str = Field("", description="Compound", example="|GI\u0160.LU\u2082|")
    seq: List[_Sequence] = Field(
        [], description="", example=[{"s": "GI\u0160", "o": "beside"}]
    )
    mods: List[Dict[str, str]] = Field(
        "", description="", example=[{"b": "ZA"}, {"m": "t"}]
    )
    n: str = Field("", description="", example="n")
    form: str = Field("", description="", example="9(U)")
    s: str = Field("", description="", example="ZU₅")


class _Sign(BaseModel_):
    # Are these two lists the same length?...
    gdl: List[_GDL] = Field(..., description="", example=[{"c": "|GI\u0160.LU\u2082|"}])
    values: List[str] = Field(
        [], description="", example=["a", "aya₂", "dur₅", "duru₅"]
    )


class SignList(_OraccFileBase):
    index: Dict[str, str] = Field(..., description="", example={"am₃": "|A.AN|"})
    signs: Dict[str, _Sign] = Field(..., description="", example={})


####################
# gloss-sux.json
####################
class _Form(BaseModel_):
    type: str = Field(..., description="", example="form")
    cbd_id: str = Field("", description="", example="o0031651.0")
    id: str = Field("", description="", example="o0031651.0")
    n: str = Field(..., description="", example="kas-kal")
    c: int = Field("", description="", example=49745)
    icount: int = Field(..., description="", example=0)
    ipct: int = Field(..., description="", example=0)
    xis: str = Field(..., description="", example="sux.r000005")
    ref: str = Field("", description="", example="o0048612.0")
    rws: str = Field("", description="", example="ES")


class _NormForm(BaseModel_):
    type: str = Field(..., description="", example="normform")
    cbd_id: str = Field(..., description="", example="o0031651.42")
    ref: str = Field(..., description="", example="o0031651.0")
    icount: int = Field(..., description="", example=0)
    ipct: int = Field(..., description="", example=0)
    xis: str = Field(..., description="", example="sux.r000005")


class _Norm(BaseModel_):
    cbd_id: str = Field("", description="", example="o0031651.41")
    id: str = Field("", description="", example="o0031651.41")
    icount: int = Field(..., description="", example=366)
    ipct: int = Field(..., description="", example=27)
    xis: str = Field(..., description="", example="sux.r00f228")
    n: str = Field(..., description="", example="kaskal")
    forms: List[_NormForm] = Field([], description="", example=[])


class _GlossaryBase(BaseModel_):
    type: str = Field(..., description="", example="base")
    cbd_id: str = Field("", description="", example="o0031651.111")
    id: str = Field("", description="", example="o0031651.111")
    n: str = Field(..., description="", example="kaskal")
    icount: int = Field(..., description="", example=1326)
    ipct: int = Field(..., description="", example=0)
    xis: str = Field(..., description="", example="sux.r00f22e")


class _Cont(BaseModel_):
    type: str = Field(..., description="", example="cont")
    cbd_id: str = Field("", description="", example="o0031651.114")
    id: str = Field("", description="", example="o0031651.114")
    n: str = Field(..., description="", example="-la=l.a")
    icount: int = Field(..., description="", example=57)
    ipct: int = Field(..., description="", example=4)
    xis: str = Field(..., description="", example="sux.r00f230")


class _Morph(BaseModel_):
    type: str = Field(..., description="", example="morph")
    cbd_id: str = Field("", description="", example="o0031651.116")
    id: str = Field("", description="", example="o0031651.116")
    n: str = Field(..., description="", example=",ani.ta")
    icount: int = Field(..., description="", example=1)
    ipct: int = Field(..., description="", example=0)
    xis: str = Field(..., description="", example="sux.r00f21c")


class _Prefix(BaseModel_):
    type: str = Field(..., description="", example="prefix")
    cbd_id: str = Field("", description="", example="o0023448.9")
    id: str = Field("", description="", example="o0023448.9")
    n: str = Field(..., description="", example="mu.na")
    icount: int = Field(..., description="", example=2)
    ipct: int = Field(..., description="", example=100)
    xis: str = Field(..., description="", example="sux.r000009")


class _FormSans(BaseModel_):
    type: str = Field(..., description="", example="form-sans")
    cbd_id: str = Field("", description="", example="o0031651.144")
    id: str = Field("", description="", example="o0031651.144")
    n: str = Field(..., description="", example="kas-kal")
    icount: int = Field(..., description="", example=0)
    ipct: int = Field(..., description="", example=0)
    xis: str = Field(..., description="", example="sux.r000005")


class _CofData(BaseModel_):
    head: str = Field(..., description="", example="zu[tooth//ivory]N'N")
    tail: Dict[str, str] = Field(
        ..., description="", example="{'sig': \"bir[shred//to shred]V/t'V/t\"}}"
    )  # TODO


class _Signature(BaseModel_):
    type: str = Field(..., description="", example="sig")
    id: str = Field("", description="", example="o0018496.8")
    sig: str = Field(
        "", description="", example="@epsd2%sux:zu-zu=Zuzu[1//1]PN'PN$Zuzu/zu-zu#~"
    )
    icount: int = Field(..., description="", example=4)
    ipct: int = Field(..., description="", example=57)
    xis: str = Field(..., description="", example="sux.r002bb1")
    cof_data: _CofData = Field(None, alias="cof-data", description="")


class _Sense(BaseModel_):
    id: str = Field(..., description="", example="sux.x0139035")
    type: str = Field(..., description="", example="sense")
    cbd_id: str = Field("", description="", example="sux.x0974361")
    n: str = Field(..., description="", example="kaskal[way//way, road]N'N")
    oracc_id: str = Field("", description="", example="o0007905", alias="oid")
    icount: int = Field(..., description="", example=1314)
    ipct: int = Field(..., description="", example=99)
    xis: str = Field(..., description="", example="sux.r00f237")
    ok: bool = Field(False, description="", example=True)
    num: str = Field(..., description="", example="1.")
    pos: str = Field(..., description="", example="N")
    mng: str = Field("", description="", example="way, road")
    forms: List[_Form] = Field(..., description="", example=[])
    norms: List[_Norm] = Field(..., description="", example=[])
    bases: List[_GlossaryBase] = Field(..., description="", example=[])
    conts: List[_Cont] = Field([], description="", example=[])
    morphs: List[_Morph] = Field(..., description="", example=[])
    form_sans: List[_FormSans] = Field(
        ..., description="", example=[], alias="form-sanss"
    )
    prefixs: List[_Prefix] = Field([], description="", example=[])
    sigs: List[_Signature] = Field(..., description="", example=[])


class _Period(BaseModel_):
    p: str = Field("", description="", example="Archaic")
    icount: int = Field(..., description="", example=1)
    ipct: int = Field(..., description="", example=0)
    xis: str = Field("", description="", example="sux.r00f203.p.s000")


class _Compound(BaseModel_):
    type: str = Field("", description="", example="cpd")
    primary: str = Field("", description="", example="1")
    partsig: str = Field(..., description="", example="zurzar[sound]N")
    ref: str = Field(..., description="", example="o0043041")
    cf: str = Field(..., description="", example="zurzar")
    gw: str = Field(..., description="", example="sound")
    mng: str = Field(..., description="", example="a sound (onomatopoeic)")
    pos: str = Field(..., description="", example="N")
    epos: str = Field(..., description="", example="N")


class _GlossaryItem(BaseModel_):
    alias: str = Field("", description="", example="Zubi[the Zubi//the Zubi]WN'WN")
    headword: str = Field(..., description="", example="kaskal[way]N")
    id: str = Field(..., description="", example="o0031651")
    oracc_id: str = Field("", description="", example="o0031651", alias="oid")
    icount: int = Field(..., description="", example=1333)
    ipct: int = Field(..., description="", example=100)
    xis: str = Field(..., description="", example="sux.o00f203")
    dc_title: str = Field(..., description="", example="epsd2/sux/kaskal[way]")
    cf: str = Field(..., description="citation form", example="kaskal")
    gw: str = Field("", description="guide word", example="way")
    pos: str = Field(..., description="part of speech", example="N")
    forms: List[_Form] = Field(..., description="", example=[])
    norms: List[_Norm] = Field(..., description="", example=[])
    bases: List[_GlossaryBase] = Field("", description="", example=[])
    conts: List[_Cont] = Field(..., description="", example=[])
    morphs: List[_Morph] = Field(..., description="", example=[])
    morph2s: List[_Morph] = Field(..., description="", example=[])
    stems: List[str] = Field(..., description="", example=[])
    prefixs: List[_Prefix] = Field(..., description="", example=[])
    form_sans: List[_FormSans] = Field(
        ..., description="", example=[], alias="form-sanss"
    )
    senses: List[_Sense] = Field(..., description="", example=[])
    periods: List[_Period] = Field(..., description="", example=[])
    compound: List[_Compound] = Field([], description="", example=[])
    rws: str = Field("", description="", example="ES")


class Glossary(_OraccFileBase):
    lang: str = Field("", description="", example="sux")
    entries: List[_GlossaryItem] = Field("", description="", example=[])
    instances: Dict[str, List[str]] = Field(
        "", description="sux-id -> list", example=[]
    )
    summaries: Dict[str, str] = Field(
        "",
        description="o/x-id -> summary",
        example={
            "o0023086": '<p class="summary" id="o0023086"><span class="summary"><span class="summary-headword">...'
        },
    )


####################
# index-cat.json
####################
class _IndexKey(BaseModel_):
    key: str = Field("", description="", example="p137994")
    count: int = Field("", description="", example=1)
    instances: List[str] = Field(
        [], description="", example=["epsd2/admin/ur3:P137994"]
    )


class IndexCat(_OraccFileBase):
    """
    The index-xxx.json files are exports of a subset of the index data created and used by the Oracc search engine,
    giving the keys the indexer has generated from the input words and the locations in which they occur in the corpus.
    These keys may have been normalized using a variety of processes: accents are rendered as numeric indices; case may be foled;
    for English translation indexes a stemmer is used so that,
    e.g., "received" and "receives" will be gathered together under "receive" in the index.

    The text IDs are always qualified with a project name because any project can use texts from other projects.
    For "txt", "lem" and "tra" index types, the instances are given as word IDs,
    so they can be used to locate the instance in the text edition.
    A simple way of displaying instances is to use the URL http://oracc.org/PROJECT/INSTANCE_ID/html,
    e.g., http://oracc.org/rimanum/P405219.4.1/html.

    If you omit the "/html" the text is loaded into the Oracc pager instead of retrieving the simple HTML version.
    """

    name: str = Field(..., description="", example="cat")
    keys: List[_IndexKey] = Field(..., description="", example=[])
    map: Dict[str, str] = Field(..., description="", example={})


####################
# index-lem.json
####################
class IndexLem(_OraccFileBase):
    name: str = Field(..., description="", example="lem")
    keys: List[_IndexKey] = Field(..., description="", example=[])
    map: Dict[str, str] = Field(..., description="", example={})


####################
# index-sux.json
####################
class IndexSux(_OraccFileBase):
    name: str = Field(..., description="", example="sux")
    keys: List[_IndexKey] = Field(..., description="", example=[])
    map: Dict[str, str] = Field(..., description="", example={})


####################
# metadata.json
####################
class Config(BaseModel_):
    pathname: str = Field(..., description="", example="epsd2")
    name: str = Field(..., description="", example="electronic PSD 2nd Edition")
    abbrev: str = Field(..., description="", example="ePSD2")
    project_type: str = Field(
        ..., alias="project-type", description="", example="superglo"
    )
    blurb: str = Field(..., description="", example="")
    public: str = Field(..., description="", example="")
    options: Dict[str, str] = Field(..., description="", example={})


class Metadata(_OraccFileBase):
    """
    This provides several objects:
    "config" - the configuration info for the project;
    "witnesses" - only present if projects use composite texts, this provides information on which manuscripts are witnesses of the composites in the project;
    "formats" - a collection of lists indicating the presence of transliterations, transliterations and lemmatized data in the project.
    """

    config: Config = Field(..., description="", example={})
    formats: Dict[str, str] = Field(..., description="", example={})


####################
# sortcodes.json
####################
class Sortvals(BaseModel_):
    periods: Dict[str, int] = Field(..., description="", example={})
    subgenre_remarks_t: Dict[str, int] = Field(..., description="", example={})
    rulers: Dict[str, int] = Field(..., description="", example={})
    sessions: Dict[str, int] = Field(..., description="", example={})
    places: Dict[str, int] = Field(..., description="", example={})
    subgenres: Dict[str, int] = Field(..., description="", example={})
    supergenres: Dict[str, int] = Field(..., description="", example={})
    genres: Dict[str, int] = Field(..., description="", example={})


class Sortcodes(BaseModel_):
    sortvals: Sortvals = Field(..., description="", example={})
