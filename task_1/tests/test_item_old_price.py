import requests
import pytest
from src.configuration import BASE_URL


@pytest.mark.acceptance
def test_item_old_price():
    response = requests.get(f"{BASE_URL}/products/i511400f/prices-history?period=12m")

    content = response.json()
    current_price = content['prices']['current']['amount']
    old_price = content['prices']['max']['amount']

    assert current_price == old_price, f"Actual price {current_price} does not match minimum price {old_price}"
