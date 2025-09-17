from unittest.mock import Mock
from fastapi.testclient import TestClient

from src.main import app
from src.models.biketype import BikeTypeInput, BikeType
from src.crud.biketype import create_biketype

client = TestClient(app)

class TestBikeTypeRead:
    def test_read_all_biketypes(self):
        response = client.get("/api/biketypes/")
        assert response.status_code == 200
        biketypes = response.json()
        assert all(["name" in c for c in biketypes])
        assert all(["id" in c for c in biketypes])


    def test_read_biketype(self):
        response = client.get("/api/biketypes/1")
        assert response.status_code == 200
        biketype = response.json()
        assert "name" in biketype
        assert "id" in biketype


def test_create_biketype_with_mock_session():
    # Arrange
    mock_session = Mock()
    input_data = BikeTypeInput(name="TestBikeType")
    # Act
    result = create_biketype(input=input_data, session=mock_session)

    # Assert
    mock_session.add.assert_called_once()
    mock_session.commit.assert_called_once()
    mock_session.refresh.assert_called_once()
    assert isinstance(result, BikeType)
    assert result.name == "TestBikeType"