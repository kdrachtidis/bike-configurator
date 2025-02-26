from unittest.mock import Mock
from fastapi.testclient import TestClient

from app.main import app
from app.views.user import User
from app.models.biketype import BikeTypeInput, BikeType
from app.views.biketype import create_a_bike_type

client = TestClient(app)


def test_read_all_biketypes():
    response = client.get("/app/biketypes/")
    assert response.status_code == 200
    biketypes = response.json()
    assert all(["name" in c for c in biketypes])
    assert all(["id" in c for c in biketypes])


def test_read_biketype():
    response = client.get("/app/biketypes/1")
    assert response.status_code == 200
    biketype = response.json()
    assert "name" in biketype
    assert "id" in biketype


# def test_create_biketype():
#     response = client.post("/app/biketypes/", json={
#         "name": "TestBikeType"
#     })
#     assert response.status_code == 200


# def test_create_biketype_with_mock_session():
#     mock_session = Mock()
#     input = BikeTypeInput(name="TestBikeType")
#     user = User(username="TestUser")
#     result = create_a_bike_type(input=input, session=mock_session, user=user)

#     mock_session.add.assert_called_once()
#     mock_session.commit.assert_called_once()
#     mock_session.refresh.assert_called_once()
#     assert isinstance(result, BikeType)
#     assert result.name == "TestBikeType"
