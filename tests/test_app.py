import pytest
from app import app

@pytest.fixture
def client():
    # Set up the test client
    with app.test_client() as client:
        yield client

def test_weather(client):
    # Send a GET request to the '/weather' endpoint
    response = client.get('/weather')
    
    # Assert the response status code is 200
    assert response.status_code == 200
    
    # Get the JSON response data
    data = response.get_json()
    
    # Assert that the expected keys are in the response
    assert "temperature" in data
    assert "humidity" in data
    assert "status" in data
