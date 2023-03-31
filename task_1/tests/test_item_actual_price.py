import requests
import pytest
from src.configuration import BASE_URL


@pytest.mark.acceptance
def test_item_actual_price():
    response = requests.get(f"{BASE_URL}/products/i511400f/prices-history?period=12m")

    content = response.json()
    actual_price = content["prices"]["current"]["amount"]
    min_price = content['prices']["min"]["amount"]

    assert actual_price == min_price, f"Actual price {actual_price} does match minimum price {min_price}"
