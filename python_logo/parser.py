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


def parse_logo(code: str) -> lark.Tree:
    """Parses the given Logo code and returns its JSON representation.

    Args:
        code (str): The Logo code to be parsed.

    Returns:
        lark.Tree: The tokenized representation of the code.
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
