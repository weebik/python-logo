from flask import Blueprint, render_template, request

main = Blueprint("main", __name__)


@main.route("/")
def index() -> tuple[str, int]:
    """Renders the index page.

    Returns:
        str: The rendered index page.
    """
    return render_template("index.html"), 200


@main.route("/", methods=["POST"])
def index_post() -> tuple[str, int]:
    """Handles form submission and prints the user's code.

    Returns:
        Response: A response object with status 204.
    """
    user_code = request.form.get("code")
    print(user_code)
    return "", 204
