from unittest.mock import Mock
from fastapi.testclient import TestClient

from src.main import app
from src.models.bikecomponent import BikeComponentInput, BikeComponent
from src.models.biketype import BikeType
from src.crud.bikecomponent import create_bikecomponent

client = TestClient(app)

class TestBikeComponentRead:
    def test_read_bikecomponent(self):
        response = client.get("/api/bikecomponents/1")
        assert response.status_code == 200
        
    def test_read_bikecomponents_by_biketype(self):
        # Test hierarchische Route: biketype 2
        response = client.get("/api/biketypes/2/bikecomponents")
        assert response.status_code == 200
        
    def test_read_bikecomponent_by_hierarchy(self):
        # Test hierarchische Route: biketype 2, bikecomponent 1
        response = client.get("/api/biketypes/2/bikecomponents/1")
        assert response.status_code == 200

class TestBikeComponentCreate:
    def test_create_bikecomponent_with_mock_session(self):
        # Arrange
        mock_session = Mock()
        mock_biketype = BikeType(id=1, name="Test Bike Type", bikecomponents=[])
        mock_session.get.return_value = mock_biketype

        input_data = BikeComponentInput(name="Test Bike Component")
        # Act
        result = create_bikecomponent(id=1, input=input_data, session=mock_session)

        # Assert
        mock_session.get.assert_called_once_with(BikeType, 1)
        mock_session.commit.assert_called_once()
        mock_session.refresh.assert_called_once()
        assert isinstance(result, BikeComponent)
        assert result.name == "Test Bike Component"
        assert result in mock_biketype.bikecomponents