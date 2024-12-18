from collections.abc import Generator, Iterator

from .exceptions import (
    InterpreterFunctionExecutionError,
    InterpreterInvalidCommandError,
    InterpreterInvalidTreeError,
    InterpreterUnboundVariableError,
    InterpreterUndefinedFunctionError,
)


class Interpreter:
    """Class to interpret parsed Logo programming language commands.
    Interpreted commands include only commands that affects the turtle directly.
    It doesn't include variables, functions or commands that are used for control flow.

    Args:
        tree (dict): Parsed Logo tree with parse() function.
    """

    def __init__(self, tree: dict) -> None:
        """Initializes the Interpreter instance."""
        self._variables = {}
        self._fuctions = {}
        try:
            self._commands = tree["tokens"]
        except KeyError as err:
            raise InterpreterInvalidTreeError from err
        except TypeError as err:
            raise InterpreterInvalidTreeError from err

    def _interpret(self, commands: list) -> Generator[dict, None, None]: #noqa: PLR0912, C901
        """Generates and interprets commands.

        Args:
            commands (list): List of parsed commands.

        Returns:
            Generator[dict, None, None]: Generator of commands.
        """
        try:
            for command in commands:
                name = command["name"]
                match name:
                    case "func_def":
                        func_name = command["func_name"]
                        func_commands = command["commands"]
                        self._fuctions[func_name] = func_commands
                    case "func_call":
                        func_name = command["func_name"]
                        try:
                            func_commands = self._fuctions[func_name]
                            try:
                                yield from self._interpret(func_commands)
                            except Exception as execution_err:
                                raise InterpreterFunctionExecutionError (func_name, \
                                                str(execution_err)) from execution_err
                        except KeyError as err:
                            raise InterpreterUndefinedFunctionError(func_name) from err
                    case "make":
                        var_name = command["var_name"]
                        value = self._evaluate(command["value"])
                        self._variables[var_name] = value
                    case "repeat":
                        value = self._evaluate(command["value"])
                        print(command)
                        for _ in range(int(value)):
                            yield from self._interpret(command["commands"])
                    case "if":
                        condition = command["condition"]
                        if condition == "true":
                            yield from self._interpret(command["commands"])
                        else:
                            yield from self._interpret(command["else_commands"])
                    case "forward" | "backward" | "left" | "right":
                        command["value"] = self._evaluate(command["value"])
                        yield command
                    case "hideturtle" | "showturtle" | "penup" | "pendown":
                        yield command
                    case _:
                        raise InterpreterInvalidCommandError
        except KeyError as err:
            raise InterpreterInvalidTreeError from err

    def _evaluate(self, value: float | str | dict) -> float:  # noqa: C901, PLR0911
        """Evaluates the value of the possible variable.

        Args:
            value (int | str | dict): Value, variable or expression to evaluate.

        Returns:
            int: Value of the possible variable.
        """
        # Value is a number.
        if isinstance(value, float):
            return value

        # Value is a variable.
        if isinstance(value, str):
            try:
                return self._variables[value]
            except KeyError as err:
                raise InterpreterUnboundVariableError(value) from err

        # Value is an expression.
        if isinstance(value, dict):
            try:
                match value["op"]:
                    case "+":
                        return self._evaluate(value["left"]) + self._evaluate(
                            value["right"]
                        )
                    case "-":
                        return self._evaluate(value["left"]) - self._evaluate(
                            value["right"]
                        )
                    case "*":
                        return self._evaluate(value["left"]) * self._evaluate(
                            value["right"]
                        )
                    case "/":
                        return self._evaluate(value["left"]) / self._evaluate(
                            value["right"]
                        )
                    case "^":
                        return self._evaluate(value["left"]) ** self._evaluate(
                            value["right"]
                        )
                    case "neg":
                        return -self._evaluate(value["value"])
                    case _:
                        raise InterpreterInvalidCommandError
            except KeyError as err:
                raise InterpreterInvalidTreeError from err

        raise InterpreterInvalidTreeError

    def __iter__(self) -> Iterator[dict]:
        """Iterates over commands and interprets them.

        Returns:
            Iterator[dict]: Iterator of commands.
        """
        return self._interpret(self._commands)
