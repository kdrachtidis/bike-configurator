from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_get_bikecomponents():
    response = client.get("/api/bikecomponents/")
    assert response.status_code == 200
    bikecomponents = response.json()
    assert all(["source" in c for c in bikecomponents])
    assert all(["group" in c for c in bikecomponents])