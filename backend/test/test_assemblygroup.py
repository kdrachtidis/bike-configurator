from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_all_assemblygroups():
    response = client.get("/api/assemblygroups/")
    assert response.status_code == 200


def test_read_assemblygroup():
    response = client.get("/api/assemblygroups/1")
    assert response.status_code == 200
