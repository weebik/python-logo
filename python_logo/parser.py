import lark.exceptions
from lark import Lark, Transformer, v_args

from .exceptions import ParserInvalidCommandError, ParserUnexpectedTokenError

_LOGO_GRAMMAR = """
start: command+
?command: hideturtle | showturtle | penup | pendown
    | forward | backward | left | right
    | repeat | if_command | make | func_def | func_call

number: NUMBER
var_name: /[a-zA-Z_-]+/
func_name: /[a-zA-Z_-]+/
variable: ":" var_name

?expr: term
    | expr "+" term -> add
    | expr "-" term -> sub
?term: power
    | term "*" power -> mul
    | term "/" power -> div
?power: factor
    | power "^" factor -> pow
?factor: atom
    | "-" factor -> neg
    | "(" expr ")"
?atom: number
    | variable

hideturtle: "hideturtle" | "ht"
showturtle: "showturtle" | "st"
penup: "penup" | "pu"
pendown: "pendown" | "pd"

forward: ("forward" | "fd") expr
backward: ("backward" | "bk") expr
left: ("left" | "lt") expr
right: ("right" | "rt") expr

repeat: "repeat" expr "[" command+ "]"

if_command: "if" (true | false) "[" command+ "]" ((else_command) "[" command+ "]")?
else_command: "else"
true: "true" | "True"
false: "false" | "False"

make: "make" var_name expr
func_def: "to" func_name arguments command+ "end"
func_call: func_name (expr)*

arguments: (variable)*

%import common.NUMBER
%import common.WS
%ignore WS
"""


class _LogoJsonTransformer(Transformer):
    """Transforms Logo language code into JSON format."""

    def start(self, items: list) -> dict:
        return {"tokens": items}

    @v_args(inline=True)
    def number(self, value: str) -> float:
        return float(value)

    @v_args(inline=True)
    def var_name(self, value: str) -> str:
        return str(value)

    @v_args(inline=True)
    def func_name(self, value: str) -> str:
        return str(value)

    @v_args(inline=True)
    def variable(self, value: str) -> str:
        return str(value)

    def add(self, items: list) -> dict:
        return {"op": "+", "left": items[0], "right": items[1]}

    def sub(self, items: list) -> dict:
        return {"op": "-", "left": items[0], "right": items[1]}

    def mul(self, items: list) -> dict:
        return {"op": "*", "left": items[0], "right": items[1]}

    def div(self, items: list) -> dict:
        return {"op": "/", "left": items[0], "right": items[1]}

    def pow(self, items: list) -> dict:
        return {"op": "^", "left": items[0], "right": items[1]}

    def neg(self, items: list) -> dict:
        return {"op": "neg", "value": items[0]}

    def hideturtle(self, items: list) -> dict:  # noqa: ARG002
        return {"name": "hideturtle"}

    def showturtle(self, items: list) -> dict:  # noqa: ARG002
        return {"name": "showturtle"}

    def penup(self, items: list) -> dict:  # noqa: ARG002
        return {"name": "penup"}

    def pendown(self, items: list) -> dict:  # noqa: ARG002
        return {"name": "pendown"}

    def forward(self, items: list) -> dict:
        return {"name": "forward", "value": items[0]}

    def backward(self, items: list) -> dict:
        return {"name": "backward", "value": items[0]}

    def left(self, items: list) -> dict:
        return {"name": "left", "value": items[0]}

    def right(self, items: list) -> dict:
        return {"name": "right", "value": items[0]}

    def repeat(self, items: list) -> dict:
        return {"name": "repeat", "value": items[0], "commands": items[1:]}

    def if_command(self, items: list) -> dict:
        condition = items[0]
        if "else" in items:
            separator_index = items.index("else")
            commands = items[1:separator_index]
            else_commands = items[separator_index + 1 :]
        else:
            commands = items[1:]
            else_commands = []
        return {
            "name": "if",
            "condition": condition,
            "commands": commands,
            "else_commands": else_commands,
        }

    def else_command(self, items: list) -> str:  # noqa: ARG002
        return "else"

    def true(self, items: list) -> str:  # noqa: ARG002
        return "true"

    def false(self, items: list) -> str:  # noqa: ARG002
        return "false"

    def arguments(self, items: list) -> str:
        return items

    def make(self, items: list) -> dict:
        return {"name": "make", "var_name": items[0], "value": items[1]}

    def func_def(self, items: list) -> dict:
        return {"name": "func_def", "func_name": items[0], \
                "arguments": items[1], "commands": items[2:]}

    def func_call(self, items: list) -> dict:
        return {"name": "func_call", "func_name": items[0], "arguments": items[1:]}

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
