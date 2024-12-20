PARSER_ERROR_SUFFIX = """Please use one of the commands provided below:

    (forward | fd) <number>
    (backward | bk) <number>
    (left | lt) <number>
    (right | rt) <number>
    showturtle | st
    hideturtle | ht
    penup | pu
    pendown | pd
    repeat <number> [ <command> ... ]
    if <condition> [ <command> ... ]
    """


class FrontendNotBuiltError(Exception):
    """Raised when the frontend is not built."""

    default_message = (
        "dist folder not found. "
        "See https://github.com/YarynaRachkevych1/python-logo/blob/main/frontend/README.md"
        " for instructions on how to build the frontend."
    )

    def __init__(self, message: str = default_message) -> None:
        """Initializes the error.

        Args:
            message (str): The error message.
        """
        self.message = message
        super().__init__(self.message)


class InterpreterInvalidCommandError(Exception):
    """Raised when an invalid command is given to the interpreter."""

    default_message = "Invalid command. Make sure you provided a supported command."

    def __init__(self, message: str = default_message) -> None:
        """Initializes the error.

        Args:
            message (str): The error message.
        """
        self.message = message
        super().__init__(self.message)


class InterpreterInvalidTreeError(Exception):
    """Raised when an invalid tree is given to the interpreter."""

    default_message = (
        "Invalid command tree. "
        "Make sure you provided a tree parsed with parse() function."
    )

    def __init__(self, message: str = default_message) -> None:
        """Initializes the error.

        Args:
            message (str): The error message.
        """
        self.message = message
        super().__init__(self.message)


class InterpreterUnboundVariableError(Exception):
    """Raised when an unbound variable is given to the interpreter."""

    default_message = (
        "Unbound Variable: '%s'. " "Make sure your program binds all of its variables."
    )

    def __init__(self, variable: str, message: str = default_message) -> None:
        """Initializes the error.

        Args:
            variable (str): The variable with unbound value.
            message (str): The error message.
        """
        self.message = message % variable
        super().__init__(self.message)


class ParserInvalidCommandError(Exception):
    """Raised when an invalid command is given to the parser."""

    default_message = f"Invalid command. {PARSER_ERROR_SUFFIX}"

    def __init__(self, message: str = default_message) -> None:
        """Initializes the error.

        Args:
            message (str): The error message.
        """
        self.message = message
        super().__init__(self.message)


class ParserUnexpectedTokenError(Exception):
    """Raised when an unexpected token is found in the input."""

    default_message = f"Unexpected token. {PARSER_ERROR_SUFFIX}"

    def __init__(self, message: str = default_message) -> None:
        """Initializes the error.

        Args:
            message (str): The error message.
        """
        self.message = message
        super().__init__(self.message)
