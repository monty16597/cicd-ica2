import pytest
from app import app
from flask import jsonify, request

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_items_internal_state(client):
    """Test that the internal `items` list reflects changes"""
    # Adding items
    item_data_1 = {'name': 'item1'}
    item_data_2 = {'name': 'item2'}
    client.post('/items', json=item_data_1)
    client.post('/items', json=item_data_2)

    # Check if the internal state matches
    response = client.get('/items')
    assert response.status_code == 200
    assert response.json == {'items': [{'name': 'item1'}, {'name': 'item2'}]}

def test_get_item_internal_state(client):
    """Test that the correct item is returned based on its index"""
    item_data = {'name': 'item1'}
    client.post('/items', json=item_data)

    # Fetch the item using its index
    response = client.get('/items/0')
    assert response.status_code == 200
    assert response.json == {'item': {'name': 'item1'}}

def test_get_item_internal_state_not_found(client):
    """Test that requesting an out-of-range item returns 404"""
    response = client.get('/items/999')
    assert response.status_code == 404
    assert response.json == {'error': 'Item not found'}
