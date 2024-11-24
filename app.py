import subprocess
from pathlib import Path

from python_logo import create_app
from python_logo.exceptions import NpmExecutableError

frontend_path = Path(__name__).parent / "frontend"
frontend_files_list = [
    p
    for p in frontend_path.glob("**/*")
    if "node_modules" not in str(p) and p.is_file()
]
app = create_app()


if __name__ == "__main__":
    try:
        process_install = subprocess.run(
            ["npm", "install", "--prefix", frontend_path.as_posix()], check=True
        )
        process_build = subprocess.run(
            ["npm", "run", "build", "--prefix", frontend_path.as_posix()], check=True
        )
    except subprocess.CalledProcessError as err:
        raise NpmExecutableError from err
    app.run(debug=True, extra_files=frontend_files_list)
