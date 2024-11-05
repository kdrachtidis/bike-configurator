from unittest.mock import Mock
from fastapi.testclient import TestClient

from main import app
from routers.components import add_bike_component
from schemas import BikeComponentInput, User, BikeComponent

client = TestClient(app)


def test_add_bikecomponent():
    response = client.post("/api/bikecomponents/",
                           json={
                               "group": "test_group",
                               "name": "test_name",
                               "price": 100,
                               "source": "test_source"
                           }  # , headers={'Authorization': 'Bearer reindert'}
                           )
    assert response.status_code == 200
    bikecomponent = response.json()
    assert bikecomponent['group'] == 'test_group'
    assert bikecomponent['source'] == 'test_source'


# def test_add_car_with_mock_session():
#     mock_session = Mock()
#     input = BikeComponentInput(price=2, name="xl")
#     user = User(username="user2")
#     result = add_bike_component(
#         component_input=input, session=mock_session, user=user)

#     mock_session.add.assert_called_once()
#     mock_session.commit.assert_called_once()
#     mock_session.refresh.assert_called_once()
#     assert isinstance(result, BikeComponent)
#     assert result.price == 2
#     assert result.name == "xl"
