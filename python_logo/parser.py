import lark.exceptions
from lark import Lark, Transformer

from .exceptions import ParserInvalidCommandError, ParserUnexpectedTokenError

_LOGO_GRAMMAR = """
start: command+
command: ((forward | backward | left | right) number) \
         | (showturtle | hideturtle | penup | pendown) \
         | ((repeat) number "[" command+ "]") \
         | ((if_command) (true | false) "[" command+ "]"\
            ((else_command) "[" command+ "]")?)
forward: "forward" | "fd"
backward: "backward" | "bk"
left: "left" | "lt"
right: "right" | "rt"
showturtle: "showturtle" | "st"
hideturtle: "hideturtle" | "ht"
penup: "penup" | "pu"
pendown: "pendown" | "pd"
repeat: "repeat"
if_command: "if"
else_command: "else"
true: "true" | "True"
false: "false" | "False"
number: SIGNED_INT

%import common.SIGNED_INT
%import common.WS
%ignore WS
"""


class _LogoJsonTransformer(Transformer):
    """Transforms Logo language code into JSON format."""

    def start(self, items: list) -> dict:
        return {"tokens": items}

    def command(self, items: list) -> dict:
        name = items[0]
        if name == "repeat":
            value = items[1]
            commands = items[2:]
            return {"name": name, "value": value, "commands": commands}
        if name == "if":
            condition = items[1]
            if "else" in items:
                separator_index = items.index("else")
                commands = items[2:separator_index]
                else_commands = items[separator_index+1:]
            else:
                commands = items[2:]
                else_commands = []
            return {"name": name, "condition": condition, "commands": commands,
                    "else_commands": else_commands}
        if name in ["forward", "backward", "left", "right"]:
            value = items[1]
            return {"name": name, "value": value}
        return {"name": name}

    def forward(self, items: list) -> str:  # noqa: ARG002
        return "forward"

    def backward(self, items: list) -> str:  # noqa: ARG002
        return "backward"

    def left(self, items: list) -> str:  # noqa: ARG002
        return "left"

    def right(self, items: list) -> str:  # noqa: ARG002
        return "right"

    def showturtle(self, items: list) -> str:  # noqa: ARG002
        return "showturtle"

    def hideturtle(self, items: list) -> str:  # noqa: ARG002
        return "hideturtle"

    def penup(self, items: list) -> str:  # noqa: ARG002
        return "penup"

    def pendown(self, items: list) -> str:  # noqa: ARG002
        return "pendown"

    def repeat(self, items: list) -> str:  # noqa: ARG002
        return "repeat"

    def if_command(self, items: list) -> str:  # noqa: ARG002
        return "if"

    def else_command(self, items: list) -> str:  # noqa: ARG002
        return "else"

    def true(self, items: list) -> str:  # noqa: ARG002
        return "true"

    def false(self, items: list) -> str:  # noqa: ARG002
        return "false"

    def number(self, items: list) -> int:
        return int(items[0])


def parse(code: str) -> dict:
    """Parses the given Logo code and returns its JSON representation.

    Args:
        code (str): The Logo code to be parsed.

    Returns:
        dict: Code tree representation in JSON format.
    """
    code = code.strip()
    if code == "":
        return {"tokens": []}

    parser = Lark(_LOGO_GRAMMAR, parser="lalr", transformer=_LogoJsonTransformer())

    try:
        return parser.parse(code)
    except lark.exceptions.UnexpectedCharacters as err:
        raise ParserInvalidCommandError from err
    except lark.exceptions.UnexpectedToken as err:
        raise ParserUnexpectedTokenError from err
