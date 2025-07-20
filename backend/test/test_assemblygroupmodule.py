from unittest.mock import Mock
from fastapi.testclient import TestClient

from app.main import app
from app.views.user import User
from app.models.assemblygroupmodule import AssemblyGroupModuleInput, AssemblyGroupModule
from app.views.assemblygroupmodule import create_an_assembly_group_module

client = TestClient(app)


def test_read_all_assemblygroupmodules():
    response = client.get("/api/assemblygroupmodules/")
    assert response.status_code == 200


def test_read_assemblygroupmodule():
    response = client.get("/api/assemblygroupmodules/1")
    assert response.status_code == 200

# def test_create_assemblygroupmodule_with_mock_session():
#     mock_session = Mock()
#     input = AssemblyGroupModuleInput(name="TestAssemblyGroupModule")
#     user = User(username="TestUser")
#     result = create_an_assembly_group_module(id=1, input=input, session=mock_session, user=user)

#     mock_session.add.assert_called_once()
#     mock_session.commit.assert_called_once()
#     mock_session.refresh.assert_called_once()
#     assert isinstance(result, AssemblyGroupModule)
#     assert result.name == "TestAssemblyGroupModule"