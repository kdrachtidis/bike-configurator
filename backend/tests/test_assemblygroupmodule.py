from unittest.mock import Mock
from fastapi.testclient import TestClient

from src.main import app
from src.models.assemblygroupmodule import AssemblyGroupModuleInput, AssemblyGroupModule
from src.models.assemblygroup import AssemblyGroup
from src.crud.assemblygroupmodule import create_assemblygroupmodule

client = TestClient(app)

class TestAssemblyGroupModuleRead:
    def test_read_all_assemblygroupmodules(self):
        response = client.get("/api/assemblygroupmodules/")
        assert response.status_code == 200


    def test_read_assemblygroupmodule(self):
        response = client.get("/api/assemblygroupmodules/5")
        assert response.status_code == 200

class TestAssemblyGroupModuleCreate:
    def test_create_assemblygroupmodule_with_mock_session(self):
        # Arrange
        mock_session = Mock()
        mock_assemblygroup = AssemblyGroup(id=1, name="TestAssemblyGroup", biketypes=[])
        mock_session.get.return_value = mock_assemblygroup

        input_data = AssemblyGroupModuleInput(name="TestAssemblyGroupModule")
        # Act
        result = create_assemblygroupmodule(id=1, input=input_data, session=mock_session)

        # Assert
        mock_session.get.assert_called_once_with(AssemblyGroup, 1)
        mock_session.commit.assert_called_once()
        mock_session.refresh.assert_called_once()
        assert isinstance(result, AssemblyGroupModule)
        assert result.name == "TestAssemblyGroupModule"
        assert result in mock_assemblygroup.assemblygroupmodules