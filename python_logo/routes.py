from flask import Blueprint, render_template, request

from .interpreter.command import Command
from .interpreter.parser import Parser

main = Blueprint("main", __name__)


@main.route("/")
def index() -> tuple[str, int]:
    """Renders the index page.

    Returns:
        tuple[str, int]: The rendered index page with status code.
    """
    return render_template("index.html"), 200


@main.route("/", methods=["POST"])
def index_post() -> tuple[str, int]:
    """Handles form submission and prints the user's code.

    Returns:
        tuple[str, int]: An empty response with status code.
    """
    user_code = request.form.get("code")
    print(type(user_code))
    create_parser(user_code)
    return "", 204


def create_parser(code: str | None) -> None:
    """Parses the provided code string and prints a list of commands.

    Args:
        code (str): The command string to parse.
    """
    if code is not None:
        parser = Parser(code)
        commands = []

        while parser.not_empty():
            code_element = parser.next_elem()
            if code_element in ["pu", "pd", "ht", "st"]:
                commands.append(Command(code_element))
            else:
                commands.append(Command(code_element, parser.next_elem()))

        print("List of commands:")
        for c in commands:
            print(c.name, c.arg)
