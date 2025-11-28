from unittest.mock import Mock
from fastapi.testclient import TestClient
from fastapi import HTTPException

from src.main import app
from src.models.biketype import BikeTypeInput, BikeType

client = TestClient(app)

class TestBikeTypeReadAll:
    def test_read_all_biketypes_with_mock_session(self):
        from src.crud.biketype import read_all_biketypes
        
        # Arrange
        mock_session = Mock()
        
        # Create mock bike types
        mock_biketype1 = BikeType(id=1, name="Mountain Bike")
        mock_biketype2 = BikeType(id=2, name="Road Bike")
        
        # Mock the exec().all() chain
        mock_result = Mock()
        mock_result.all.return_value = [mock_biketype1, mock_biketype2]
        mock_session.exec.return_value = mock_result
        
        # Act
        result = read_all_biketypes(session=mock_session)
        
        # Assert
        assert isinstance(result, list)
        assert len(result) == 2
        assert all(isinstance(bt, BikeType) for bt in result)
        assert mock_session.exec.called

class TestBikeTypeRead:
    def test_read_biketype_with_mock_session(self):
        from src.crud.biketype import read_biketype
        
        # Arrange
        mock_session = Mock()
        mock_biketype = BikeType(id=1, name="Mountain Bike")
        mock_session.get.return_value = mock_biketype
        
        # Act
        result = read_biketype(biketype_id=1, session=mock_session)
        
        # Assert
        mock_session.get.assert_called_once_with(BikeType, 1)
        assert result == mock_biketype
        assert result.name == "Mountain Bike"
        assert result.id == 1
    
    def test_read_biketype_not_found(self):
        from src.crud.biketype import read_biketype
        
        # Arrange
        mock_session = Mock()
        mock_session.get.return_value = None
        
        # Act & Assert
        try:
            read_biketype(biketype_id=999, session=mock_session)
            assert False, "Expected HTTPException to be raised"
        except HTTPException as e:
            assert e.status_code == 404

class TestBikeTypeCreate:
    def test_create_biketype_with_mock_session(self):
        from src.crud.biketype import create_biketype
        
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

class TestBikeTypeUpdate:
    def test_update_biketype_with_mock_session(self):
        from src.crud.biketype import update_biketype
        
        # Arrange
        mock_session = Mock()
        
        # Existing bike type
        existing_biketype = BikeType(id=1, name="Old Name")
        mock_session.get.return_value = existing_biketype
        
        # New data for update
        new_data = BikeTypeInput(name="New Name")
        
        # Act
        result = update_biketype(biketype_id=1, input=new_data, session=mock_session)
        
        # Assert
        assert result.name == "New Name"
        assert mock_session.commit.called
        mock_session.get.assert_called_once_with(BikeType, 1)
    
    def test_update_biketype_not_found(self):
        from src.crud.biketype import update_biketype
        
        # Arrange
        mock_session = Mock()
        mock_session.get.return_value = None
        
        new_data = BikeTypeInput(name="New Name")
        
        # Act & Assert
        try:
            update_biketype(biketype_id=999, input=new_data, session=mock_session)
            assert False, "Expected HTTPException to be raised"
        except HTTPException as e:
            assert e.status_code == 404

class TestBikeTypeDelete:
    def test_delete_biketype_with_mock_session(self):
        from src.crud.biketype import delete_biketype
        
        # Arrange
        mock_session = Mock()
        
        # Existing bike type
        existing_biketype = BikeType(id=1, name="To Be Deleted")
        mock_session.get.return_value = existing_biketype
        
        # Act
        delete_biketype(biketype_id=1, session=mock_session)
        
        # Assert
        mock_session.delete.assert_called_once_with(existing_biketype)
        assert mock_session.commit.called
        mock_session.get.assert_called_once_with(BikeType, 1)
    
    def test_delete_biketype_not_found(self):
        from src.crud.biketype import delete_biketype
        
        # Arrange
        mock_session = Mock()
        mock_session.get.return_value = None
        
        # Act & Assert
        try:
            delete_biketype(biketype_id=999, session=mock_session)
            assert False, "Expected HTTPException to be raised"
        except HTTPException as e:
            assert e.status_code == 404