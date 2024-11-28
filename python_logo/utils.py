from .interpreter import Interpreter
from .parser import parse


def run(code: str) -> Interpreter:
    """Runs Logo parser and interpreter.

    Args:
        code (str): Logo code to run.

    Returns:
        Interpreter: Interpreter object with the result of the code.
    """
    tree = parse(code)
    return Interpreter(tree)
