from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_biketypes():
    response = client.get("/app/api/biketypes/")
    assert response.status_code == 200
