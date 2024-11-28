from pathlib import Path

from python_logo import create_app, socketio
from python_logo.exceptions import FrontendNotBuiltError

_DIST_FRONTEND_DIR = Path(__file__).parent / "dist"
app = create_app()


if __name__ == "__main__":
    if not _DIST_FRONTEND_DIR.exists():
        raise FrontendNotBuiltError
    socketio.run(app, debug=True)
