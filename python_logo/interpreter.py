from collections.abc import Generator, Iterator

from .exceptions import InterpreterInvalidCommandError, InterpreterInvalidTreeError


class Interpreter:
    """Class to interpret parsed Logo programming language commands.
    Interpreted commands include only commands that affects the turtle directly.

    Args:
        tree (dict): Parsed Logo tree with parse() function.
    """

    def __init__(self, tree: dict) -> None:
        """Initializes the Interpreter instance."""
        try:
            self._commands = tree["commands"]
        except KeyError as err:
            raise InterpreterInvalidTreeError from err
        except TypeError as err:
            raise InterpreterInvalidTreeError from err

    def _interpret(self, commands: list) -> Generator[dict, None, None]:
        """Generates interpreted commands.

        Args:
            commands (list): List of parsed commands.

        Returns:
            Generator[dict, None, None]: Generator of interpreted commands.
        """
        try:
            for command in commands:
                name = command["name"]
                match name:
                    case "repeat":
                        value = command["value"]
                        for _ in range(value):
                            yield from self._interpret(command["commands"])
                    case "if":
                        condition = command["condition"]
                        if condition == "true":
                            yield from self._interpret(command["commands"])
                    case (
                        "forward"
                        | "backward"
                        | "left"
                        | "right"
                        | "hideturtle"
                        | "showturtle"
                        | "penup"
                        | "pendown"
                    ):
                        yield command
                    case _:
                        raise InterpreterInvalidCommandError
        except KeyError as err:
            raise InterpreterInvalidTreeError from err

    def interpret_all(self) -> dict:
        """Interprets all parsed commands.

        Returns:
            dict: All interpreted commands.
        """
        return {"commands": list(self)}

    def __iter__(self) -> Iterator[dict]:
        """Iterates over commands and interprets them.

        Returns:
            Iterator[dict]: Iterator of interpreted commands.
        """
        return self._interpret(self._commands)
