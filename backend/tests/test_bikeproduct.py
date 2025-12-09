from unittest.mock import Mock
from fastapi.testclient import TestClient
from fastapi import HTTPException

from src.main import app
from src.models.bikeproduct import BikeProductInput, BikeProduct
from src.models.bikepart import BikePart

client = TestClient(app)

class TestBikeProductReadAll:
    def test_read_all_bikeproducts_with_mock_session(self):
        from src.crud.bikeproduct import read_all_bikeproducts
        
        # Arrange
        mock_session = Mock()
        
        # Create mock bike products
        mock_product1 = BikeProduct(id=1, name="Product 1", source="Source 1", price=100)
        mock_product2 = BikeProduct(id=2, name="Product 2", source="Source 2", price=200)
        
        # Mock the exec().all() chain
        mock_result = Mock()
        mock_result.all.return_value = [mock_product1, mock_product2]
        mock_session.exec.return_value = mock_result
        
        # Act
        result = read_all_bikeproducts(session=mock_session)
        
        # Assert
        assert isinstance(result, list)
        assert len(result) == 2
        assert all(isinstance(p, BikeProduct) for p in result)
        assert mock_session.exec.called

class TestBikeProductCreate:
    def test_create_bikeproduct_with_mock_session(self):
        from src.crud.bikeproduct import create_bikeproduct
        
        # Arrange
        mock_session = Mock()
        mock_bikepart = BikePart(id=1, name="Test Bike Part", bikeproducts=[])
        mock_session.get.return_value = mock_bikepart

        input_data = BikeProductInput(name="Test Bike Product", source="Test Source", price=100)
        
        # Act
        result = create_bikeproduct(bikepart_id=1, input=input_data, session=mock_session)

        # Assert
        mock_session.get.assert_called_once_with(BikePart, 1)
        mock_session.commit.assert_called_once()
        mock_session.refresh.assert_called_once()
        assert isinstance(result, BikeProduct)
        assert result.name == "Test Bike Product"
        assert result.source == "Test Source"
        assert result.price == 100
        assert result in mock_bikepart.bikeproducts
    
    def test_create_bikeproduct_bikepart_not_found(self):
        from src.crud.bikeproduct import create_bikeproduct
        
        # Arrange
        mock_session = Mock()
        mock_session.get.return_value = None
        
        input_data = BikeProductInput(name="Test Product", source="Test Source", price=100)
        
        # Act & Assert
        try:
            create_bikeproduct(bikepart_id=999, input=input_data, session=mock_session)
            assert False, "Expected HTTPException to be raised"
        except HTTPException as e:
            assert e.status_code == 404

class TestBikeProductRead:
    def test_read_bikeproduct_with_mock_session(self):
        from src.crud.bikeproduct import read_bikeproduct
        
        # Arrange
        mock_session = Mock()
        mock_bikeproduct = BikeProduct(id=1, name="Test Product", source="Test Source", price=100)
        mock_bikepart = BikePart(id=1, name="Test Bike Part", bikeproducts=[mock_bikeproduct])
        
        # Mock get to return bikepart first, then bikeproduct
        mock_session.get.side_effect = [mock_bikepart, mock_bikeproduct]
        
        # Act
        result = read_bikeproduct(part_id=1, product_id=1, session=mock_session)
        
        # Assert
        assert mock_session.get.call_count == 2
        assert result == mock_bikeproduct
        assert result.name == "Test Product"
        assert result.id == 1
    
    def test_read_bikeproduct_part_not_found(self):
        from src.crud.bikeproduct import read_bikeproduct
        
        # Arrange
        mock_session = Mock()
        mock_session.get.return_value = None
        
        # Act & Assert
        try:
            read_bikeproduct(part_id=999, product_id=1, session=mock_session)
            assert False, "Expected HTTPException to be raised"
        except HTTPException as e:
            assert e.status_code == 404
    
    def test_read_bikeproduct_product_not_found(self):
        from src.crud.bikeproduct import read_bikeproduct
        
        # Arrange
        mock_session = Mock()
        mock_bikepart = BikePart(id=1, name="Test Bike Part", bikeproducts=[])
        mock_session.get.side_effect = [mock_bikepart, None]
        
        # Act & Assert
        try:
            read_bikeproduct(part_id=1, product_id=999, session=mock_session)
            assert False, "Expected HTTPException to be raised"
        except HTTPException as e:
            assert e.status_code == 404
    
    def test_read_bikeproduct_not_in_part(self):
        from src.crud.bikeproduct import read_bikeproduct
        
        # Arrange
        mock_session = Mock()
        mock_bikeproduct = BikeProduct(id=1, name="Test Product", source="Test Source", price=100)
        mock_bikepart = BikePart(id=1, name="Test Bike Part", bikeproducts=[])  # Empty list
        
        mock_session.get.side_effect = [mock_bikepart, mock_bikeproduct]
        
        # Act & Assert
        try:
            read_bikeproduct(part_id=1, product_id=1, session=mock_session)
            assert False, "Expected HTTPException to be raised"
        except HTTPException as e:
            assert e.status_code == 404

class TestBikeProductUpdate:
    def test_update_bikeproduct_with_mock_session(self):
        from src.crud.bikeproduct import update_bikeproduct
        
        # Arrange
        mock_session = Mock()
        
        # Existing bike product
        existing_product = BikeProduct(id=1, name="Old Name", source="Old Source", price=100)
        mock_bikepart = BikePart(id=1, name="Test Bike Part", bikeproducts=[existing_product])
        
        # Mock get to return bikepart first, then bikeproduct
        mock_session.get.side_effect = [mock_bikepart, existing_product]
        
        # New data for update
        new_data = BikeProductInput(name="New Name", source="New Source", price=200)
        
        # Act
        result = update_bikeproduct(part_id=1, product_id=1, new_data=new_data, session=mock_session)
        
        # Assert
        assert result.name == "New Name"
        assert result.source == "New Source"
        assert result.price == 200
        assert mock_session.commit.called
        assert mock_session.refresh.called
        assert mock_session.get.call_count == 2
    
    def test_update_bikeproduct_part_not_found(self):
        from src.crud.bikeproduct import update_bikeproduct
        
        # Arrange
        mock_session = Mock()
        mock_session.get.return_value = None
        
        new_data = BikeProductInput(name="New Name", source="New Source", price=200)
        
        # Act & Assert
        try:
            update_bikeproduct(part_id=999, product_id=1, new_data=new_data, session=mock_session)
            assert False, "Expected HTTPException to be raised"
        except HTTPException as e:
            assert e.status_code == 404
    
    def test_update_bikeproduct_product_not_found(self):
        from src.crud.bikeproduct import update_bikeproduct
        
        # Arrange
        mock_session = Mock()
        mock_bikepart = BikePart(id=1, name="Test Bike Part", bikeproducts=[])
        mock_session.get.side_effect = [mock_bikepart, None]
        
        new_data = BikeProductInput(name="New Name", source="New Source", price=200)
        
        # Act & Assert
        try:
            update_bikeproduct(part_id=1, product_id=999, new_data=new_data, session=mock_session)
            assert False, "Expected HTTPException to be raised"
        except HTTPException as e:
            assert e.status_code == 404

class TestBikeProductDelete:
    def test_delete_bikeproduct_with_mock_session(self):
        from src.crud.bikeproduct import delete_bikeproduct
        
        # Arrange
        mock_session = Mock()
        
        # Existing bike product
        existing_product = BikeProduct(id=1, name="To Be Deleted", source="Test Source", price=100)
        mock_bikepart = BikePart(id=1, name="Test Bike Part", bikeproducts=[existing_product])
        
        # Mock get to return bikepart first, then bikeproduct
        mock_session.get.side_effect = [mock_bikepart, existing_product]
        
        # Act
        delete_bikeproduct(part_id=1, product_id=1, session=mock_session)
        
        # Assert
        mock_session.delete.assert_called_once_with(existing_product)
        assert mock_session.commit.called
        assert mock_session.get.call_count == 2
    
    def test_delete_bikeproduct_part_not_found(self):
        from src.crud.bikeproduct import delete_bikeproduct
        
        # Arrange
        mock_session = Mock()
        mock_session.get.return_value = None
        
        # Act & Assert
        try:
            delete_bikeproduct(part_id=999, product_id=1, session=mock_session)
            assert False, "Expected HTTPException to be raised"
        except HTTPException as e:
            assert e.status_code == 404
    
    def test_delete_bikeproduct_product_not_found(self):
        from src.crud.bikeproduct import delete_bikeproduct
        
        # Arrange
        mock_session = Mock()
        mock_bikepart = BikePart(id=1, name="Test Bike Part", bikeproducts=[])
        mock_session.get.side_effect = [mock_bikepart, None]
        
        # Act & Assert
        try:
            delete_bikeproduct(part_id=1, product_id=999, session=mock_session)
            assert False, "Expected HTTPException to be raised"
        except HTTPException as e:
            assert e.status_code == 404
