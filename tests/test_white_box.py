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