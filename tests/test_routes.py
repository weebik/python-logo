import pytest

from python_logo import create_app

STATUS_CODE_OK = 200


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_serve(client):
    response = client.get("/")
    assert response.status_code == STATUS_CODE_OK
    assert b"Logo Playground" in response.data
