import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_hello(client):
    """Test the root route"""
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b"Hello, Flask!"

def test_get_items_empty(client):
    """Test GET /items when there are no items"""
    response = client.get('/items')
    assert response.status_code == 200
    assert response.json == {'items': []}

def test_add_item(client):
    """Test POST /items to add a new item"""
    item_data = {'name': 'item1'}
    response = client.post('/items', json=item_data)
    assert response.status_code == 201
    assert response.json == {'message': 'Item added successfully'}

def test_get_item_not_found(client):
    """Test GET /items/<item_id> for a non-existing item"""
    response = client.get('/items/999')
    assert response.status_code == 404
    assert response.json == {'error': 'Item not found'}
