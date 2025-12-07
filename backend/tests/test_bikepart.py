from unittest.mock import Mock
from fastapi.testclient import TestClient
from fastapi import HTTPException

from src.main import app
from src.models.bikepart import BikePartInput, BikePart
from src.models.bikecomponent import BikeComponent
from src.models.biketype import BikeType

client = TestClient(app)

class TestBikePartReadAll:
    def test_read_all_bikeparts_with_mock_session(self):
        from src.crud.bikepart import read_all_bikeparts
        
        # Arrange
        mock_session = Mock()
        mock_result = Mock()
        mock_bikepart1 = BikePart(id=1, name="Part 1")
        mock_bikepart2 = BikePart(id=2, name="Part 2")
        mock_result.all.return_value = [mock_bikepart1, mock_bikepart2]
        mock_session.exec.return_value = mock_result
        
        # Act
        result = read_all_bikeparts(session=mock_session)
        
        # Assert
        assert isinstance(result, list)
        assert len(result) == 2
        assert result[0].name == "Part 1"
        assert result[1].name == "Part 2"
        mock_session.exec.assert_called_once()
    
    def test_read_all_bikeparts_empty(self):
        from src.crud.bikepart import read_all_bikeparts
        
        # Arrange
        mock_session = Mock()
        mock_result = Mock()
        mock_result.all.return_value = []
        mock_session.exec.return_value = mock_result
        
        # Act
        result = read_all_bikeparts(session=mock_session)
        
        # Assert
        assert isinstance(result, list)
        assert len(result) == 0

class TestBikePartReadByHierarchy:
    def test_read_bikeparts_by_hierarchy_with_mock_session(self):
        from src.crud.bikepart import read_bikeparts
        
        # Arrange
        mock_session = Mock()
        
        # Create mock bike parts
        mock_bikepart1 = BikePart(id=1, name="Part 1")
        mock_bikepart2 = BikePart(id=2, name="Part 2")
        
        # Create mock bike component with the parts in its list
        mock_bikecomponent = BikeComponent(id=3, name="Test Component", bikeparts=[mock_bikepart1, mock_bikepart2])
        
        # Create mock bike type with the component in its list
        mock_biketype = BikeType(id=2, name="Test Bike Type", bikecomponents=[mock_bikecomponent])
        
        def mock_get(model, id):
            if model == BikeType and id == 2:
                return mock_biketype
            elif model == BikeComponent and id == 3:
                return mock_bikecomponent
            return None
        
        mock_session.get.side_effect = mock_get
        
        # Act
        result = read_bikeparts(biketype_id=2, bikecomponent_id=3, session=mock_session)
        
        # Assert
        assert isinstance(result, list)
        assert len(result) == 2
        assert all(isinstance(part, BikePart) for part in result)
        assert mock_session.get.call_count == 2

class TestBikePartCreate:
    def test_create_bikepart_with_mock_session(self):
        from src.crud.bikepart import create_bikepart
        
        # Arrange
        mock_session = Mock()
        
        # Create mock bike component
        mock_bikecomponent = BikeComponent(id=3, name="Test Component", bikeparts=[])
        
        # Create mock bike type with the component in its list
        mock_biketype = BikeType(id=2, name="Test Bike Type", bikecomponents=[mock_bikecomponent])
        
        def mock_get(model, id):
            if model == BikeType and id == 2:
                return mock_biketype
            elif model == BikeComponent and id == 3:
                return mock_bikecomponent
            return None
        
        mock_session.get.side_effect = mock_get
        
        # Input data
        input_data = BikePartInput(name="New Bike Part")
        
        # Act
        result = create_bikepart(biketype_id=2, bikecomponent_id=3, input=input_data, session=mock_session)
        
        # Assert
        assert isinstance(result, BikePart)
        assert result.name == "New Bike Part"
        assert result in mock_bikecomponent.bikeparts
        assert mock_session.commit.called
        assert mock_session.refresh.called
        assert mock_session.get.call_count == 2

class TestBikePartReadSingle:
    def test_read_bikepart_with_mock_session(self):
        from src.crud.bikepart import read_bikepart
        
        # Arrange
        mock_session = Mock()
        
        # Create mock bike part
        mock_bikepart = BikePart(id=1, name="Test Bike Part")
        
        # Create mock bike component with the part in its list
        mock_bikecomponent = BikeComponent(id=3, name="Test Component", bikeparts=[mock_bikepart])
        
        # Create mock bike type with the component in its list
        mock_biketype = BikeType(id=2, name="Test Bike Type", bikecomponents=[mock_bikecomponent])
        
        def mock_get(model, id):
            if model == BikeType and id == 2:
                return mock_biketype
            elif model == BikeComponent and id == 3:
                return mock_bikecomponent
            elif model == BikePart and id == 1:
                return mock_bikepart
            return None
        
        mock_session.get.side_effect = mock_get
        
        # Act
        result = read_bikepart(biketype_id=2, bikecomponent_id=3, bikepart_id=1, session=mock_session)
        
        # Assert
        assert result == mock_bikepart
        assert result.name == "Test Bike Part"
        assert result.id == 1
        assert mock_session.get.call_count == 3
    
    def test_read_bikepart_biketype_not_found(self):
        from src.crud.bikepart import read_bikepart
        
        # Arrange
        mock_session = Mock()
        mock_session.get.return_value = None
        
        # Act & Assert
        try:
            read_bikepart(biketype_id=999, bikecomponent_id=3, bikepart_id=1, session=mock_session)
            assert False, "Expected HTTPException to be raised"
        except HTTPException as e:
            assert e.status_code == 404
    
    def test_read_bikepart_part_not_in_component(self):
        from src.crud.bikepart import read_bikepart
        
        # Arrange
        mock_session = Mock()
        
        # Create separate parts
        mock_bikepart = BikePart(id=1, name="Test Part")
        other_part = BikePart(id=2, name="Other Part")
        
        # Component only has 'other_part', not the one we're looking for
        mock_bikecomponent = BikeComponent(id=3, name="Test Component", bikeparts=[other_part])
        mock_biketype = BikeType(id=2, name="Test Bike Type", bikecomponents=[mock_bikecomponent])
        
        def mock_get(model, id):
            if model == BikeType and id == 2:
                return mock_biketype
            elif model == BikeComponent and id == 3:
                return mock_bikecomponent
            elif model == BikePart and id == 1:
                return mock_bikepart
            return None
        
        mock_session.get.side_effect = mock_get
        
        # Act & Assert
        try:
            read_bikepart(biketype_id=2, bikecomponent_id=3, bikepart_id=1, session=mock_session)
            assert False, "Expected HTTPException to be raised"
        except HTTPException as e:
            assert e.status_code == 404
            assert "not found in bike component" in str(e.detail)

class TestBikePartUpdate:
    def test_update_bikepart_with_mock_session(self):
        from src.crud.bikepart import update_bikepart
        
        # Arrange
        mock_session = Mock()
        
        # Existing bike part
        existing_part = BikePart(id=1, name="Old Name")
        
        # BikeComponent containing the existing part
        mock_bikecomponent = BikeComponent(id=3, name="Test Component", bikeparts=[existing_part])
        
        # BikeType containing the component
        mock_biketype = BikeType(id=2, name="Test Bike Type", bikecomponents=[mock_bikecomponent])
        
        def mock_get(model, id):
            if model == BikeType and id == 2:
                return mock_biketype
            elif model == BikeComponent and id == 3:
                return mock_bikecomponent
            elif model == BikePart and id == 1:
                return existing_part
            return None
        
        mock_session.get.side_effect = mock_get
        
        # New data for update
        new_data = BikePartInput(name="New Name")
        
        # Act
        result = update_bikepart(biketype_id=2, bikecomponent_id=3, bikepart_id=1, input=new_data, session=mock_session)
        
        # Assert
        assert result.name == "New Name"
        assert mock_session.commit.called
        assert mock_session.get.call_count == 3

class TestBikePartDelete:
    def test_delete_bikepart_with_mock_session(self):
        from src.crud.bikepart import delete_bikepart
        
        # Arrange
        mock_session = Mock()
        
        # Existing bike part
        existing_part = BikePart(id=1, name="To Be Deleted")
        
        # BikeComponent containing the existing part
        mock_bikecomponent = BikeComponent(id=3, name="Test Component", bikeparts=[existing_part])
        
        # BikeType containing the component
        mock_biketype = BikeType(id=2, name="Test Bike Type", bikecomponents=[mock_bikecomponent])
        
        def mock_get(model, id):
            if model == BikeType and id == 2:
                return mock_biketype
            elif model == BikeComponent and id == 3:
                return mock_bikecomponent
            elif model == BikePart and id == 1:
                return existing_part
            return None
        
        mock_session.get.side_effect = mock_get
        
        # Act
        delete_bikepart(biketype_id=2, bikecomponent_id=3, bikepart_id=1, session=mock_session)
        
        # Assert
        mock_session.delete.assert_called_once_with(existing_part)
        assert mock_session.commit.called
        assert mock_session.get.call_count == 3