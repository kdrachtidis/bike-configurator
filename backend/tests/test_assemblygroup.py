from unittest.mock import Mock
from fastapi.testclient import TestClient

from src.main import app
from src.models.assemblygroup import AssemblyGroupInput, AssemblyGroup
from src.models.biketype import BikeType
from src.crud.assemblygroup import create_assemblygroup 

client = TestClient(app)

class TestAssemblyGroupRead:
    def test_read_assemblygroup(self):
        response = client.get("/api/assemblygroups/1")
        assert response.status_code == 200
        
    def test_read_assemblygroups_by_biketype(self):
        # Test hierarchische Route: biketype 2
        response = client.get("/api/biketypes/2/assemblygroups")
        assert response.status_code == 200
        
    def test_read_assemblygroup_by_hierarchy(self):
        # Test hierarchische Route: biketype 2, assemblygroup 1
        response = client.get("/api/biketypes/2/assemblygroups/1")
        assert response.status_code == 200

class TestAssemblyGroupCreate:
    def test_create_assemblygroup_with_mock_session(self):
        # Arrange
        mock_session = Mock()
        mock_biketype = BikeType(id=1, name="TestBikeType", assemblygroups=[])
        mock_session.get.return_value = mock_biketype

        input_data = AssemblyGroupInput(name="TestAssemblyGroup")
        # Act
        result = create_assemblygroup(id=1, input=input_data, session=mock_session)

        # Assert
        mock_session.get.assert_called_once_with(BikeType, 1)
        mock_session.commit.assert_called_once()
        mock_session.refresh.assert_called_once()
        assert isinstance(result, AssemblyGroup)
        assert result.name == "TestAssemblyGroup"
        assert result in mock_biketype.assemblygroups