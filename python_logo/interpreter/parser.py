class Parser:
    """Parses a string of commands by splitting it into individual elements
    and providing methods to access each element sequentially.

    Attributes:
        code (list[str]): List of command elements.
        index (int): Current position in the token list.

    Methods:
        nextElem(): Retrieves the next element in the command sequence.
        notEmpty(): Checks if there are more elements left to process.
    """

    def __init__(self, code: str) -> None:
        """Initializes the Parser with a string of commands, splitting
        it into elements and setting the starting index.

        Args:
            code (str): The command string to be parsed.
        """
        self.code = code.split()
        self.index = -1

    def next_elem(self) -> str:
        """Retrieves the next element in the command sequence.

        Returns:
            str: The next element (command or argument) in the code list.
        """
        self.index += 1
        return self.code[self.index]

    def not_empty(self) -> bool:
        """Checks if there are more elements to process.

        Returns:
            bool: True if there are more elements, False otherwise.
        """
        return self.index + 1 != len(self.code)
