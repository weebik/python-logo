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


class NpmExecutableError(Exception):
    """Raised when the npm executable is not found."""

    default_message = (
        "npm executable error. "
        "Please make sure npm (>=18) is installed and in your PATH."
    )

    def __init__(self, message: str = default_message) -> None:
        """Initializes the error.

        Args:
            message (str): The error message.
        """
        self.message = message
        super().__init__(self.message)


class FrontendNotBuiltError(Exception):
    """Raised when the frontend is not built."""

    default_message = "dist folder not found. Run `npm run build` first."

    def __init__(self, message: str = default_message) -> None:
        """Initializes the error.

        Args:
            message (str): The error message.
        """
        self.message = message
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
