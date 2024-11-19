from typing import Generator

import lark.exceptions

class LogoInterpreter:
    """Class to interpret parsed Logo programming language commands.

    Attributes:
        commands (Generator | None): A generator that yields commands parsed from the Logo tree structure.
    """
    def __init__(self):
        self.commands = None

    def run(self, tree: lark.Tree) -> dict:
        """Executes the parsed tree and returns a list of commands as dictionaries."""
        self.commands = self._commands_generator(tree)
        return self._as_list()

    def _commands_generator(self, tree: lark.Tree) -> Generator[dict, None, None]:
        """Generates commands for the turtle from the tree returned by parser."""
        for command in tree.children:
            c = command.children[0]
            match c.data:
                case "repeat":
                    repeat_count = int(str(command.children[1].children[0]))
                    for _ in range(repeat_count):
                        yield from self._commands_generator(lark.Tree("repeat", command.children[2:]))
                case "if":
                    condition = str(command.children[1].data)
                    if condition == "true":
                        yield from self._commands_generator(lark.Tree("if", command.children[2:]))
                case "forward" | "backward" | "left" | "right":
                    yield {
                        "name": str(c.data),
                        "value": int(str(command.children[1].children[0]))
                    }
                case _:
                    yield {"name": str(c.data)}

    def _as_list(self) -> dict:
        """Converts generator of commands for the turtle to a list of dicts."""
        command_list = []
        try:
            while True:
                command_list.append(next(self.commands))
        except StopIteration:
            return {"commands": command_list}
