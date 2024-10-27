from flask import Blueprint, Response, render_template, request

main = Blueprint("main", __name__)


@main.route("/")
def index() -> str:
    """Renders the index page.

    Returns:
        str: The rendered index page.
    """
    return render_template("index.html")


@main.route("/", methods=["POST"])
def index_post() -> Response:
    """Handles form submission and prints the user's code.

    Returns:
        Response: A response object with status 204.
    """
    user_code = request.form["code"]
    print(user_code)
    return Response(status=204)
