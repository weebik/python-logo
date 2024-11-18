from collections.abc import Generator

import lark.exceptions
from lark import Lark

from .exceptions import ParserInvalidCommandError, ParserUnexpectedTokenError

logo_grammar = """
start: command+
command: ((forward | backward | left | right) number) \
         | (showturtle | hideturtle | penup | pendown) \
         | ((repeat) number "[" command+ "]") \
         | ((if) (true | false) "[" command+ "]")
forward: "forward" | "fd"
backward: "backward" | "bk"
left: "left" | "lt"
right: "right" | "rt"
showturtle: "showturtle" | "st"
hideturtle: "hideturtle" | "ht"
penup: "penup" | "pu"
pendown: "pendown" | "pd"
repeat: "repeat"
if: "if"
true: "true" | "True"
false: "false" | "False"
number: SIGNED_INT

%import common.SIGNED_INT
%import common.WS
%ignore WS
"""


def interpreter(tree: lark.Tree) -> Generator[dict, None, None]:
    """Generates commands for the turtle from the tree returned by parser."""
    for command in tree.children:
        c = command.children[0]
        match c.data:
            case "repeat":
                repeat_count = int(str(command.children[1].children[0]))
                for _ in range(repeat_count):
                    yield from interpreter(lark.Tree("repeat", command.children[2:]))
            case "if":
                condition = str(command.children[1].data)
                if condition == "true":
                    yield from interpreter(lark.Tree("if", command.children[2:]))
            case "forward" | "backward" | "left" | "right":
                yield {
                    "name": str(c.data),
                    "value": int(str(command.children[1].children[0]))
                }
            case _:
                yield {"name": str(c.data)}


def interpreter_as_list(generator: Generator[dict, None, None]) -> dict:
    """Converts generator of commands for the turtle to a list of dicts."""
    command_list = []
    try:
        while True:
            command_list.append(next(generator))
    except StopIteration:
        return {"commands": command_list}


def parse_logo(code: str) -> lark.Tree:
    """Parses the given Logo code and returns its JSON representation.

    Args:
        code (str): The Logo code to be parsed.

    Returns:
        dict: The tokenized representation of the code.
    """
    code = code.strip()
    if code == "":
        return lark.Tree("start", [])

    parser = Lark(logo_grammar, parser="lalr")

    try:
        print(parser.parse(code).pretty())
        return parser.parse(code)
    except lark.exceptions.UnexpectedCharacters as err:
        raise ParserInvalidCommandError from err
    except lark.exceptions.UnexpectedToken as err:
        raise ParserUnexpectedTokenError from err
