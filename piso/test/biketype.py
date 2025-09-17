from unittest.mock import Mock
from fastapi.testclient import TestClient

from app.main import app
from app.views.user import User, get_current_user
from app.models.biketype import BikeTypeInput, BikeType
from app.views.biketype import create_a_bike_type

client = TestClient(app)


# def test_read_all_biketypes():
#     response = client.get("/api/biketypes/")
#     assert response.status_code == 200
#     biketypes = response.json()
#     assert all(["name" in c for c in biketypes])
#     assert all(["id" in c for c in biketypes])


# def test_read_biketype():
#     response = client.get("/api/biketypes/1")
#     assert response.status_code == 200
#     biketype = response.json()
#     assert "name" in biketype
#     assert "id" in biketype


# def test_create_biketype():
#     login_response = client.post("/api/login", data={
#         "username": "TestUser",
#         "password": "Welcome1!"
#     })
#     assert login_response.status_code == 200
#     token = login_response.json()["access_token"]

#     response = client.post(
#         "/api/biketypes/",
#         json={"name": "TestBikeType"},
#         headers={"Authorization": f"Bearer {token}"}
#     )
#     assert response.status_code == 200

from fastapi import Depends

def override_get_current_user():
    return User(username="TestUser", password="Welcome1!")

app.dependency_overrides[get_current_user] = override_get_current_user

def test_create_biketype_with_user():
    response = client.post("/api/biketypes/", json={"name": "TestBikeType"})
    print(response.status_code, response.text)
    assert response.status_code == 201


# def test_create_biketype_with_mock_session():
#     mock_session = Mock()
#     input = BikeTypeInput(name="TestBikeType")
#     user = User(username="TestUser", password="Welcome1!")
#     result = create_a_bike_type(input=input, session=mock_session, user=user)

#     mock_session.add.assert_called_once()
#     mock_session.commit.assert_called_once()
#     mock_session.refresh.assert_called_once()
#     assert isinstance(result, BikeType)
#     assert result.name == "TestBikeType"
