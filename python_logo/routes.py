from flask import Blueprint, render_template, request

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
    print(user_code)
    return "", 204
