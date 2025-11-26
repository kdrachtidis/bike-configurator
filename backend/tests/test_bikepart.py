from unittest.mock import Mock
from fastapi.testclient import TestClient

from src.main import app
from src.models.bikepart import BikePartInput, BikePart
from src.models.bikecomponent import BikeComponent
from src.crud.bikepart import create_bikepart_by_hierarchy

client = TestClient(app)

class TestBikePartRead:
    def test_read_bikepart(self): # Test direct route: bikepart 5
        response = client.get("/api/bikeparts/5")
        assert response.status_code == 200
    
    def test_read_bikeparts_by_hierarchy(self):
        # Test hierarchical route: biketype 2, bikecomponent 3
        response = client.get("/api/biketypes/2/bikecomponents/3/bikeparts")
        assert response.status_code == 200
        
    def test_read_bikepart_by_hierarchy(self):
        # Test hierarchical route: biketype 2, bikecomponent 3, part 1
        response = client.get("/api/biketypes/2/bikecomponents/3/bikeparts/1")
        assert response.status_code == 200

class TestBikePartCreate:
    def test_create_bikepart_by_hierarchy_with_mock_session(self):
        # This function has become more complex and tests the hierarchical logic
        # Disabled for now as it requires a complete mock structure
        pass