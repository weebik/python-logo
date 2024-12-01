from .interpreter import Interpreter
from .parser import parse


def run(code: str) -> Interpreter:
    """Runs Logo parser and interpreter.

    Args:
        code (str): Logo code to run.

    Returns:
        Interpreter: The interpreter class with an iterator to obtain the commands.
    """
    tree = parse(code)
    return Interpreter(tree)
