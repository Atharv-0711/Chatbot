import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_page(client):
    """Test the main page loads correctly."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Chat with Rini" in response.data

def test_chat_endpoint(client):
    """Test the /chat endpoint with a sample message."""
    response = client.post('/chat', json={'message': 'Hello Rini, how was your day?'})
    assert response.status_code == 200
    json_data = response.get_json()
    assert 'response' in json_data
    # Check that the response is a non-empty string
    assert isinstance(json_data['response'], str)
    assert len(json_data['response']) > 0

# Additional tests can be added here for edge cases and error handling

def test_chat_endpoint_empty_message(client):
    """Test the /chat endpoint with an empty message."""
    response = client.post('/chat', json={'message': ''})
    assert response.status_code == 200
    json_data = response.get_json()
    assert 'response' in json_data
    assert isinstance(json_data['response'], str)
    assert len(json_data['response']) > 0

def test_chat_endpoint_missing_message(client):
    """Test the /chat endpoint with missing message key."""
    response = client.post('/chat', json={})
    assert response.status_code == 200
    json_data = response.get_json()
    assert 'response' in json_data
    assert isinstance(json_data['response'], str)
    assert len(json_data['response']) > 0

def test_chat_endpoint_invalid_method(client):
    """Test the /chat endpoint with GET method which is not allowed."""
    response = client.get('/chat')
    assert response.status_code == 405  # Method Not Allowed
