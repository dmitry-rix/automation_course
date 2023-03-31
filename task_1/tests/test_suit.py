import pytest
import requests


@pytest.mark.smoke
def test_item_price_response():
    response = requests.get("https://catalog.api.onliner.by/products/i511400f/prices-history?period=12m")

    assert response.status_code == 200, 'Invalid response status code.'


@pytest.mark.acceptance
def test_item_price_currency():
    response = requests.get("https://catalog.api.onliner.by/products/i511400f/prices-history?period=12m")

    content = response.json()
    price_currency = content["prices"]["current"]["currency"]

    assert price_currency == "BYN", 'Invalid currency in response.'


@pytest.mark.acceptance
def test_item_actual_price():
    response = requests.get("https://catalog.api.onliner.by/products/i511400f/prices-history?period=12m")

    content = response.json()
    actual_price = content["prices"]["current"]["amount"]
    min_price = content['prices']["min"]["amount"]

    assert actual_price == min_price, 'Actual price does match minimum price.'
