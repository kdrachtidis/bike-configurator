from unittest.mock import Mock
from fastapi.testclient import TestClient

from src.main import app
from src.models.bikeproduct import BikeProductInput, BikeProduct
from src.models.bikepart import BikePart
from src.crud.bikeproduct import create_bikeproduct

client = TestClient(app) # FastAPI test client

class TestBikeProductRead:
    def test_read_all_bikeproducts(self): # Test direct route: all bikeproducts
        response = client.get("/api/bikeproducts/")
        assert response.status_code == 200 # OK
        bikeproducts = response.json() # List of bikeproducts
        assert all(["source" in c for c in bikeproducts]) # Check that all bikeproducts have 'source' field
        assert all(["group" in c for c in bikeproducts]) # Check that all bikeproducts have 'group' field


    def test_read_bikeproduct(self): # Test direct route: bikeproduct 1
        response = client.get("/api/bikeproducts/1")
        assert response.status_code == 200 # OK
        bikeproduct = response.json() # Single bikeproduct
        assert "name" in bikeproduct # Check that bikeproduct has 'name' field
        assert "id" in bikeproduct # Check that bikeproduct has 'id' field

class TestBikeProductCreate:
    def test_create_bikeproduct_with_mock_session(self): # Test creating a bikeproduct with a mock session
        mock_session = Mock() # Create a mock session
        mock_bikepart = BikePart(id=1, name="Test Bike Part", bikecomponents=[]) # Mock BikePart
        mock_session.get.return_value = mock_bikepart # Mock the get method to return the mock BikePart

        input_data = BikeProductInput(name="Test Bike Product", source="Test Source", price=100, group="Test Group") # Input data for creating a bikeproduct
        
        result = create_bikeproduct(id=1, input=input_data, session=mock_session) # Call the create_bikeproduct function

        # Assert
        mock_session.get.assert_called_once_with(BikePart, 1) # Check that get was called correctly
        mock_session.commit.assert_called_once() # Check that commit was called
        mock_session.refresh.assert_called_once() # Check that refresh was called
        assert isinstance(result, BikeProduct) # Check that result is a BikeProduct
        assert result.name == "Test Bike Product" # Check that the name is correct
        assert result.source == "Test Source" # Check that the source is correct
        assert result.price == 100 # Check that the price is correct
        assert result.group == "Test Group" # Check that the group is correct
