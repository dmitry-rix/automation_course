import requests
import pytest
from src.configuration import BASE_URL
from src.enums.global_enums import GlobalErrorMessages

@pytest.mark.smoke
def test_item_price_response():
    response = requests.get(f"{BASE_URL}/products/i511400f/prices-history?period=12m")

    assert response.status_code == 200, GlobalErrorMessages.INVALID_STATUS_CODE.value

    # comment for visibility