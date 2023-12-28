from dataclasses import dataclass
from typing import Optional


@dataclass
class ParseNode:
    name: str
    children: Optional[list["ParseNode"]] = None


def _t(tokens: list[str], cur_index: int) -> tuple[ParseNode, int]:
    child_1, new_cur_index = _token(tokens, cur_index)
    child_2, new_cur_index = _prod(tokens, new_cur_index)

    return ParseNode("T", [child_1, child_2]), new_cur_index


def _token(tokens: list[str], cur_index: int) -> tuple[ParseNode, int]:
    try:
        child_1, new_cur_index = _terminal("(", tokens, cur_index)
        child_2, new_cur_index = _start(tokens, new_cur_index)
        child_3, new_cur_index = _terminal(")", tokens, new_cur_index)

        return ParseNode("TOKEN", [child_1, child_2, child_3]), new_cur_index

    except (TypeError, IndexError):
        child, new_cur_index = _terminal("id", tokens, cur_index)

        return ParseNode("TOKEN", [child]), new_cur_index


def _prod(tokens: list[str], cur_index: int) -> tuple[ParseNode, int]:
    try:
        child_1, new_cur_index = _terminal("*", tokens, cur_index)
        child_2, new_cur_index = _token(tokens, new_cur_index)
        child_3, new_cur_index = _prod(tokens, new_cur_index)

        return ParseNode("PROD", [child_1, child_2, child_3]), new_cur_index

    except (TypeError, IndexError):
        return ParseNode("PROD", [ParseNode("eps")]), cur_index


def _sum(tokens: list[str], cur_index: int) -> tuple[ParseNode, int]:
    try:
        child_1, new_cur_index = _terminal("+", tokens, cur_index)
        child_2, new_cur_index = _t(tokens, new_cur_index)
        child_3, new_cur_index = _sum(tokens, new_cur_index)

        return ParseNode("SUM", [child_1, child_2, child_3]), new_cur_index

    except (TypeError, IndexError):
        return ParseNode("SUM", [ParseNode("eps")]), cur_index


def _start(tokens: list[str], cur_index: int) -> tuple[ParseNode, int]:
    child_1, new_cur_index = _t(tokens, cur_index)
    child_2, new_cur_index = _sum(tokens, new_cur_index)

    return ParseNode("START", [child_1, child_2]), new_cur_index


def _terminal(
    terminal: str, tokens: list[str], cur_index: int
) -> tuple[ParseNode, int]:
    if terminal == tokens[cur_index]:
        return ParseNode(terminal), cur_index + 1

    elif terminal == "id" and tokens[cur_index].isdigit():
        return ParseNode(f"id({tokens[cur_index]})"), cur_index + 1

    raise TypeError(f"Incorrect input: must be terminal, passed {tokens[cur_index]}")


def parse(tokens: list[str]) -> ParseNode:
    tree, result_index = _start(tokens, 0)

    if result_index != len(tokens):
        raise TypeError

    return tree


def pretty_print(tree: ParseNode) -> None:
    def cur_print(node: ParseNode, number_of_points: int) -> None:
        print("." * number_of_points + node.name)

        if node.children:
            for child in node.children:
                cur_print(child, number_of_points + len(node.name))

    cur_print(tree, 0)
