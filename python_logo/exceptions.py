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
        "Unbound Variable: '%s'. Make sure your program binds all of its variables."
    )

    def __init__(self, variable: str, message: str = default_message) -> None:
        """Initializes the error.

        Args:
            variable (str): The variable with unbound value.
            message (str): The error message.
        """
        self.message = message % variable
        super().__init__(self.message)


class InterpreterUndefinedFunctionError(Exception):
    """Raised when an unbound function name is given to the interpreter."""

    default_message = (
        "The function '%s' is not defined. \
            Ensure all functions are properly defined before use."
    )

    def __init__(self, name: str, message: str = default_message) -> None: #noqa: D417
        """Initializes the error.

        Args:
            variable (str): The function name with unbound definition.
            message (str): The error message.
        """
        self.message = message % name
        super().__init__(self.message)


class InterpreterInvalidFunctionArgumentsError(Exception):
    """Raised when a function receives too many or too few arguments."""

    default_message = (
        "Invalid number of arguments for function '%s'. Expected %d, but got %d."
    )

    def __init__(
        self, func_name: str, expected_args: int, received_args: int, message: str = None
    ) -> None:
        """Initializes the error.

        Args:
            func_name (str): The name of the function.
            expected_args (int): The expected number of arguments.
            received_args (int): The actual number of arguments provided.
            message (str): Custom error message (optional).
        """
        if not message:
            message = self.default_message % (func_name, expected_args, received_args)
        self.message = message
        super().__init__(self.message)


class InterpreterFunctionExecutionError(Exception):
    """Raised when the execution of a function fails."""

    def __init__(self, func_name: str, reason: str) -> None:
        """
        Initializes the error.

        Args:
            func_name (str): The name of the function that failed.
            reason (str): The reason or error message explaining the failure.
        """
        self.func_name = func_name
        self.reason = reason
        self.message = f"Execution of function '{func_name}' failed: {reason}"
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
