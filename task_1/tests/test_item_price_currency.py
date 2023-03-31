import pytest
import requests
from src.enums.global_enums import GlobalErrorMessages
from src.configuration import BASE_URL


@pytest.mark.acceptance
def test_item_price_currency():
    response = requests.get(f"{BASE_URL}/products/i511400f/prices-history?period=12m")

    content = response.json()
    price_currency = content["prices"]["current"]["currency"]

    assert price_currency == "BYN", GlobalErrorMessages.INVALID_CURRENCY.value
