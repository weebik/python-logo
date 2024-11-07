import lark.exceptions
from lark import Lark, Transformer

from .exceptions import ParserInvalidCommandError, ParserUnexpectedTokenError

logo_grammar = """
start: command+
command: ((forward | backward | left | right) number) \
         | (showturtle | hideturtle | penup | pendown)
forward: "forward" | "fd"
backward: "backward" | "bk"
left: "left" | "lt"
right: "right" | "rt"
showturtle: "showturtle" | "st"
hideturtle: "hideturtle" | "ht"
penup: "penup" | "pu"
pendown: "pendown" | "pd"
number: SIGNED_INT

%import common.SIGNED_INT
%import common.WS
%ignore WS
"""


class LogoJsonTransformer(Transformer):
    """Transforms Logo language code into JSON format."""

    def start(self, items: list[str]) -> dict[str, list[str]]:  # noqa: D102
        return {"commands": items}

    def command(self, items: list[str]) -> dict[str, str]:  # noqa: D102
        command = items[0]
        if command in ["forward", "backward", "left", "right"]:
            number = items[1]
            return {"command": command, "value": number}
        return {"command": command}

    def forward(self, items: list[str]) -> str:  # noqa: D102, ARG002
        return "forward"

    def backward(self, items: list[str]) -> str:  # noqa: D102, ARG002
        return "backward"

    def left(self, items: list[str]) -> str:  # noqa: D102, ARG002
        return "left"

    def right(self, items: list[str]) -> str:  # noqa: D102, ARG002
        return "right"

    def showturtle(self, items: list[str]) -> str:  # noqa: D102, ARG002
        return "showturtle"

    def hideturtle(self, items: list[str]) -> str:  # noqa: D102, ARG002
        return "hideturtle"

    def penup(self, items: list[str]) -> str:  # noqa: D102, ARG002
        return "penup"

    def pendown(self, items: list[str]) -> str:  # noqa: D102, ARG002
        return "pendown"

    def number(self, items: list[str]) -> int:  # noqa: D102
        return int(items[0])


def parse_logo(code: str) -> dict:
    """Parses the given Logo code and returns its JSON representation.

    Args:
        code (str): The Logo code to be parsed.

    Returns:
        dict: The tokenized representation of the code.
    """
    code = code.strip()
    if code == "":
        return {"commands": []}

    parser = Lark(logo_grammar, parser="lalr", transformer=LogoJsonTransformer())

    try:
        return parser.parse(code)
    except lark.exceptions.UnexpectedCharacters as err:
        raise ParserInvalidCommandError from err
    except lark.exceptions.UnexpectedToken as err:
        raise ParserUnexpectedTokenError from err
