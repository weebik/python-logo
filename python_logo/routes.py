from flask import Blueprint, render_template, request

from .utils import parse_logo_http_response

main = Blueprint("main", __name__)


@main.route("/")
def index() -> tuple[str, int]:
    """Renders the index page.

    Returns:
        tuple[str, int]: The rendered index page with status code.
    """
    return render_template("index.html"), 200


@main.route("/", methods=["POST"])
def index_post() -> tuple[dict, int]:
    """Handles form submission and prints the user's code.

    Returns:
        tuple[dict, int]: A response with status code.
    """
    user_code = request.form.get("code")
    if user_code is None:
        return {"error": "No code provided."}, 400

    user_code = user_code.strip()
    response = parse_logo_http_response(user_code)
    print(response[0])
    return response
