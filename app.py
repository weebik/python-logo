import subprocess
from pathlib import Path

from python_logo import create_app, socketio
from python_logo.exceptions import NpmExecutableError

_FRONTEND_DIR = Path(__file__).resolve().parent / "frontend"
_frontend_files_list = [
    p
    for p in _FRONTEND_DIR.glob("**/*")
    if "node_modules" not in str(p) and p.is_file()
]
app = create_app()


if __name__ == "__main__":
    try:
        process_install = subprocess.run(
            ["npm", "install", "--prefix", _FRONTEND_DIR.as_posix()], check=True
        )
        process_build = subprocess.run(
            ["npm", "run", "build", "--prefix", _FRONTEND_DIR.as_posix()], check=True
        )
    except subprocess.CalledProcessError as err:
        raise NpmExecutableError from err
    socketio.run(app, debug=True, extra_files=_frontend_files_list)
