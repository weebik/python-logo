from flask import Blueprint, render_template, request

from .parser import parse_logo

main = Blueprint("main", __name__)


@main.route("/")
def index() -> tuple[str, int]:
    """Renders the index page.

    Returns:
        tuple[str, int]: The rendered index page with status code.
    """
    return render_template("index.html"), 200


@main.route("/", methods=["POST"])
def index_post() -> tuple[str | dict[str, str], int]:
    """Handles form submission and prints the user's code.

    Returns:
        tuple[str | dict[str, str], int]: A response with status code.
    """
    user_code = request.form.get("code")
    if user_code is None:
        user_code = ""
    tree = parse_logo(user_code)
    print(tree)
    return tree, 200
