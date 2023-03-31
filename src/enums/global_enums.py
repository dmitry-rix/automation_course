from enum import Enum


class GlobalErrorMessages(Enum):
    INVALID_STATUS_CODE = 'Incorrect response status code'
    INVALID_CURRENCY = 'Invalid currency in response'