from unittest.mock import Mock
from fastapi.testclient import TestClient

from backend.src.main import app
from src.views.user import User
from src.models.bikecomponent import BikeComponentInput, BikeComponent
from src.views.bikecomponent import create_a_bike_component

client = TestClient(app)


def test_read_all_bikecomponents():
    response = client.get("/api/bikecomponents/")
    assert response.status_code == 200
    bikecomponents = response.json()
    assert all(["source" in c for c in bikecomponents])
    assert all(["group" in c for c in bikecomponents])


def test_read_bikecomponent():
    response = client.get("/api/bikecomponents/1")
    assert response.status_code == 200
    bikecomponent = response.json()
    assert "name" in bikecomponent
    assert "id" in bikecomponent


# def test_add_bikecomponent_with_mock_session():
#     mock_session = Mock()
#     input = BikeComponentInput(name="TestBikeComponent", source="TestSource", price=100, group="TestGroup", id="1")
#     user = User(username="TestUser")
#     result = create_a_bike_component(id="1", input=input, session=mock_session, user=user)

#     mock_session.add.assert_called_once()
#     mock_session.commit.assert_called_once()
#     mock_session.refresh.assert_called_once()
#     assert isinstance(result, BikeComponent)
#     assert result.name == "TestBikeComponent"
#     # assert result.source == "TestSource"
#     # assert result.price == 100
#     # assert result.group == "TestGroup"
