from unittest.mock import Mock
from fastapi.testclient import TestClient

from src.main import app
from src.models.bikecomponent import BikeComponentInput, BikeComponent
from src.models.assemblygroupmodule import AssemblyGroupModule
from src.crud.bikecomponent import create_bikecomponent

client = TestClient(app)

class TestBikeComponentRead:
    def test_read_all_bikecomponents(self):
        response = client.get("/api/bikecomponents/")
        assert response.status_code == 200
        bikecomponents = response.json()
        assert all(["source" in c for c in bikecomponents])
        assert all(["group" in c for c in bikecomponents])


    def test_read_bikecomponent(self):
        response = client.get("/api/bikecomponents/1")
        assert response.status_code == 200
        bikecomponent = response.json()
        assert "name" in bikecomponent
        assert "id" in bikecomponent

class TestBikeComponentCreate:
    def test_create_bikecomponent_with_mock_session(self):
        # Arrange
        mock_session = Mock()
        mock_assemblygroupmodule = AssemblyGroupModule(id=1, name="TestAssemblyGroupModule", assemblygroups=[])
        mock_session.get.return_value = mock_assemblygroupmodule

        input_data = BikeComponentInput(name="TestBikeComponent", source="TestSource", price=100, group="TestGroup")
        # Act
        result = create_bikecomponent(id=1, input=input_data, session=mock_session)

        # Assert
        mock_session.get.assert_called_once_with(AssemblyGroupModule, 1)
        mock_session.commit.assert_called_once()
        mock_session.refresh.assert_called_once()
        assert isinstance(result, BikeComponent)
        assert result.name == "TestBikeComponent"
        assert result.source == "TestSource"
        assert result.price == 100
        assert result.group == "TestGroup"
