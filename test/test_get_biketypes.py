from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_get_biketypes():
    response = client.get("/api/biketypes/")
    assert response.status_code == 200
