import requests
import pytest
from src.configuration import BASE_URL


@pytest.mark.acceptance
def test_item_min_max_price():
    response = requests.get(f"{BASE_URL}/products/i511400f/prices-history?period=12m")

    content = response.json()
    min_price = content['prices']['min']['amount']
    max_price = content['prices']['max']['amount']

    assert max_price > min_price, f'Max price {max_price} is not higher than min price {min_price}'

    assert min_price != max_price, 'Min and max prices are equal'
