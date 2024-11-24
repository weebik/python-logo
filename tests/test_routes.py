from pathlib import Path

import pytest

from python_logo import create_app

STATUS_CODE_OK = 200
FRONTEND_NOT_BUILT_MESSAGE = "dist folder not found. Run `npm run build` first."


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_serve(client):
    if not (Path(__name__).parent.parent / "dist").exists():
        raise FileNotFoundError(FRONTEND_NOT_BUILT_MESSAGE)
    response = client.get("/")
    assert response.status_code == STATUS_CODE_OK
    assert b"Logo Playground" in response.data
