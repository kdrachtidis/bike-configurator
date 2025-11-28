from unittest.mock import Mock
from fastapi.testclient import TestClient
from fastapi import HTTPException

from src.main import app
from src.models.bikecomponent import BikeComponentInput, BikeComponent
from src.models.biketype import BikeType
from src.crud.bikecomponent import create_bikecomponent

client = TestClient(app)

class TestBikeComponentRead:
    def test_read_bikecomponent_with_mock_session(self):
        from src.crud.bikecomponent import read_bikecomponent
        
        # Arrange
        mock_session = Mock()
        mock_bikecomponent = BikeComponent(id=1, name="Test Bike Component")
        mock_session.get.return_value = mock_bikecomponent
        
        # Act
        result = read_bikecomponent(bikecomponent_id=1, session=mock_session)
        
        # Assert
        mock_session.get.assert_called_once_with(BikeComponent, 1)
        assert result == mock_bikecomponent
        assert result.name == "Test Bike Component"
        assert result.id == 1
        
    def test_read_bikecomponent_not_found(self):
        from src.crud.bikecomponent import read_bikecomponent
        
        # Arrange
        mock_session = Mock()
        mock_session.get.return_value = None  # BikeComponent not found
        
        # Act & Assert
        try:
            read_bikecomponent(bikecomponent_id=999, session=mock_session)
            assert False, "Expected HTTPException to be raised"
        except HTTPException as e:
            assert e.status_code == 404

class TestBikeComponentsReadAll:
    def test_read_all_bikecomponents_by_biketype_with_mock_session(self):
        # Arrange
        mock_session = Mock()
        
        # Create mock bike components
        mock_bikecomponent1 = BikeComponent(id=1, name="Component 1")
        mock_bikecomponent2 = BikeComponent(id=2, name="Component 2")
        
        # Create mock bike type with the components in its list
        mock_biketype = BikeType(id=2, name="Test Bike Type", bikecomponents=[mock_bikecomponent1, mock_bikecomponent2])
        
        # Configure mock session to return the mock bike type
        mock_session.get.return_value = mock_biketype
        
        # Act
        from src.crud.bikecomponent import read_all_bikecomponents_by_biketype
        result = read_all_bikecomponents_by_biketype(biketype_id=2, session=mock_session)
        
        # Assert
        mock_session.get.assert_called_once_with(BikeType, 2)
        assert isinstance(result, list)
        assert len(result) == 2
        assert all(isinstance(comp, BikeComponent) for comp in result)

class TestBikeComponentCreate:
    def test_create_bikecomponent_with_mock_session(self):
        # Arrange
        mock_session = Mock()
        mock_biketype = BikeType(id=1, name="Test Bike Type", bikecomponents=[])
        mock_session.get.return_value = mock_biketype

        input_data = BikeComponentInput(name="Test Bike Component")
        # Act
        result = create_bikecomponent(biketype_id=1, input=input_data, session=mock_session)

        # Assert
        mock_session.get.assert_called_once_with(BikeType, 1)
        mock_session.commit.assert_called_once()
        mock_session.refresh.assert_called_once()
        assert isinstance(result, BikeComponent)
        assert result.name == "Test Bike Component"
        assert result in mock_biketype.bikecomponents

class TestBikeComponentReadByHierarchy:
    def test_read_bikecomponent_by_hierarchy_with_mock_session(self):
        from src.crud.bikecomponent import read_bikecomponent_by_biketype
        
        # Arrange
        mock_session = Mock()
        
        # Create mock bike component
        mock_bikecomponent = BikeComponent(id=1, name="Test Bike Component")
        
        # Create mock bike type with the component in its list
        mock_biketype = BikeType(id=2, name="Test Bike Type", bikecomponents=[mock_bikecomponent])
        
        # Configure mock session to return appropriate objects
        def mock_get(model, id):
            if model == BikeType and id == 2:
                return mock_biketype
            elif model == BikeComponent and id == 1:
                return mock_bikecomponent
            return None
        
        mock_session.get.side_effect = mock_get
        
        # Act
        result = read_bikecomponent_by_biketype(biketype_id=2, bikecomponent_id=1, session=mock_session)
        
        # Assert
        assert result == mock_bikecomponent
        assert result.name == "Test Bike Component"
        assert result.id == 1
        assert mock_session.get.call_count == 2  # Called twice: once for biketype, once for bikecomponent
        
    def test_read_bikecomponent_by_hierarchy_biketype_not_found(self):
        from src.crud.bikecomponent import read_bikecomponent_by_biketype
        
        # Arrange
        mock_session = Mock()
        mock_session.get.return_value = None  # BikeType not found
        
        # Act & Assert
        try:
            read_bikecomponent_by_biketype(biketype_id=999, bikecomponent_id=1, session=mock_session)
            assert False, "Expected HTTPException to be raised"
        except HTTPException as e:
            assert e.status_code == 404
            
    def test_read_bikecomponent_by_hierarchy_component_not_in_biketype(self):
        from src.crud.bikecomponent import read_bikecomponent_by_biketype
        
        # Arrange
        mock_session = Mock()
        
        # Create separate components
        mock_bikecomponent = BikeComponent(id=1, name="Test Component")
        other_component = BikeComponent(id=2, name="Other Component")
        
        # BikeType only has 'other_component', not the one we're looking for
        mock_biketype = BikeType(id=2, name="Test Bike Type", bikecomponents=[other_component])
        
        def mock_get(model, id):
            if model == BikeType and id == 2:
                return mock_biketype
            elif model == BikeComponent and id == 1:
                return mock_bikecomponent
            return None
        
        mock_session.get.side_effect = mock_get
        
        # Act & Assert
        try:
            read_bikecomponent_by_biketype(biketype_id=2, bikecomponent_id=1, session=mock_session)
            assert False, "Expected HTTPException to be raised"
        except HTTPException as e:
            assert e.status_code == 404
            assert "not found in bike type" in str(e.detail)

class TestBikeComponentUpdateByHierarchy:
    def test_update_bikecomponent_by_hierarchy_with_mock_session(self):
        from src.crud.bikecomponent import update_bikecomponent_by_biketype
        from src.models.bikecomponent import BikeComponentInput
        
        # Arrange
        mock_session = Mock()
        
        # Existing bike component
        existing_component = BikeComponent(id=1, name="Old Name")
        
        # BikeType containing the existing component
        mock_biketype = BikeType(id=2, name="Test Bike Type", bikecomponents=[existing_component])
        
        def mock_get(model, id):
            if model == BikeType and id == 2:
                return mock_biketype
            elif model == BikeComponent and id == 1:
                return existing_component
            return None
        
        mock_session.get.side_effect = mock_get
        
        # New data for update
        new_data = BikeComponentInput(name="New Name")
        
        # Act
        result = update_bikecomponent_by_biketype(biketype_id=2, bikecomponent_id=1, input=new_data, session=mock_session)
        
        # Assert
        assert result.name == "New Name"
        assert mock_session.commit.called
        assert mock_session.refresh.called

class TestBikeComponentDeleteByHierarchy:
    def test_delete_bikecomponent_by_hierarchy_with_mock_session(self):
        from src.crud.bikecomponent import delete_bikecomponent_by_biketype
        
        # Arrange
        mock_session = Mock()
        
        # Existing bike component
        existing_component = BikeComponent(id=1, name="To Be Deleted")
        
        # BikeType containing the existing component
        mock_biketype = BikeType(id=2, name="Test Bike Type", bikecomponents=[existing_component])
        
        def mock_get(model, id):
            if model == BikeType and id == 2:
                return mock_biketype
            elif model == BikeComponent and id == 1:
                return existing_component
            return None
        
        mock_session.get.side_effect = mock_get
        
        # Act
        delete_bikecomponent_by_biketype(biketype_id=2, bikecomponent_id=1, session=mock_session)
        
        # Assert
        mock_session.delete.assert_called_once_with(existing_component)
        assert mock_session.commit.called