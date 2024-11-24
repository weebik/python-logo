from pathlib import Path

from flask import Blueprint, Response, send_from_directory

from .exceptions import FrontendNotBuiltError

_DIST_FRONTEND_DIR = Path(__file__).parent.parent / "dist"
main = Blueprint("main", __name__)


@main.route("/", defaults={"path": "index.html"})
@main.route("/<path:path>")
def serve(path: str) -> Response:
    """Serves the requested file from the dist folder.

    Args:
        path (str): The path to the served file.

    Returns:
        Response: The response containing the file.
    """
    if not _DIST_FRONTEND_DIR.exists():
        raise FrontendNotBuiltError
    return send_from_directory("../dist", path)
