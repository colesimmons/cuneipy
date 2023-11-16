from typing import Any, Dict, List, Literal, Optional, Union, TypeAlias, ForwardRef

from typing_extensions import Annotated

from pydantic import BaseModel, Discriminator, Field, Tag


####################
# Discontinuity
####################
class Discontinuity(BaseModel):
    # type = "cell-end" | "cell-start" | "column" | "field-end" | "field-start" | "line-start" | "nonw" | "nonx" | "object" | "surface"

    # Required
    node: Literal["d"]
    type_: str = Field(..., alias="type")

    # Optional
    label: str = Field("")
    n: str = Field("")
    subtype: str = Field("")
    strict: str = Field("")
    state: str = Field("")
    extent: str = Field("")
    scope: str = Field("")
    frag: str = Field("")
    lang: str = Field("")
    delim: str = Field("")
    queried: str = Field("")
    flags: str = Field("")
    o: str = Field("")


####################
# Lemma
####################
class Para(BaseModel):
    class_: str = Field(..., alias="class")  # syntax | boundary | pointer
    type_: str = Field(
        ..., alias="type"
    )  # and | sentence | no sentence | label | pointer_ref
    text: str = Field(...)
    val: str = Field(...)  # empty str
    bracketing_level: str = Field(...)  # "0"


class Lemma(BaseModel):
    # Required
    node: Literal["l"]
    id_: str = Field(..., alias="id")
    ref: str
    inst: str

    # [{'name': 'field', 'group': 'env', 'ngram': '-1', 'ref': 'P010055.4.1'}, {'name': 'discourse', 'group': 'env', 'value': 'body', 'ngram': '-1', 'ref': 'P010055.4.1'}]
    f: Dict[str, Any]  # TODO

    # [{'name': 'field', 'group': 'env', 'ngram': '-1', 'ref': 'P010055.4.1'}, {'name': 'discourse', 'group': 'env', 'value': 'body', 'ngram': '-1', 'ref': 'P010055.4.1'}]
    props: List[Dict[str, str]]  # TODO

    # Optional
    frag: str = Field("")
    sig: str = Field("")
    exoprj: str = Field("")
    exolng: str = Field("")
    exosig: str = Field("")
    ftype: str = Field("")
    cof_tails: str = Field("", alias="cof-tails")
    cof_head: str = Field("", alias="cof-head")
    tail_sig: str = Field("", alias="tail-sig")

    para: List[Para] = Field("")
    bad: str = Field("")


####################
# Other
####################
class LLNode(BaseModel):  # only 50 of these
    # Required
    node: Literal["ll"]
    id_: str = Field(alias="id")

    # [{'node': 'l', 'frag': 'šagan', 'ref': 'P020281.27.2', 'inst': '%sux:šagan=amagan[child-bearing mother]',
    # 'sig': "@epsd2/admin/ed3b%sux:šagan=amagan[mother//child-bearing mother]N'N$amagan/šagan#~",
    # 'f': {'lang': 'sux', 'form': 'šagan', 'delim': '', 'gdl': [{'v': 'šagan', 'id': 'P020281.27.2.0'}]
    choices: List[Dict[str, Any]]


class LinkbaseNode(BaseModel):  # only 50 of these
    linkbase: Any


####################
# Chunk
####################
Chunk = ForwardRef("Chunk")


def get_node_type(node: Any):
    if "node" in node:
        return node["node"]
    if "linkbase" in node:
        return "linkbase"
    return None


CDLNode = Annotated[
    Union[
        Annotated[Chunk, Tag("c")],
        Annotated[Discontinuity, Tag("d")],
        Annotated[Lemma, Tag("l")],
        Annotated[LLNode, Tag("ll")],
        Annotated[LinkbaseNode, Tag("linkbase")],
    ],
    Field(get_node_type),
]


class Chunk(BaseModel):
    # type = "discourse" | "phrase" | "sentence" | "text"

    # Required
    node: Literal["c"]
    type_: str = Field(..., alias="type")
    id_: str = Field(..., alias="id")

    # Optional
    cdl: List[CDLNode] = []
    implicit: bool = False
    label: str = Field("")
    ref: str = Field("")
    subtype: str = Field("")
    tag: str = Field("")
