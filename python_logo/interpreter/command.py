class Command:
    """Represents a single command with an optional argument.

    Attributes:
        name (str): Command name.
        arg (Optional): Command argument, if any.
    """

    def __init__(self, name: str, arg: str | None = None) -> None:
        """Initializes a Command with a name and optional argument.

        Args:
            name (str): Command name.
            arg (Optional[str]): Command argument. Defaults to None.
        """
        self.name = name
        self.arg = arg
