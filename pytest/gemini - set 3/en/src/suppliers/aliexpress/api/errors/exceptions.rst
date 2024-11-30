```python
import pytest

from hypotez.src.suppliers.aliexpress.api.errors.exceptions import (
    AliexpressException,
    InvalidArgumentException,
    ProductIdNotFoundException,
    ApiRequestException,
    ApiRequestResponseException,
    ProductsNotFoudException,
    CategoriesNotFoudException,
    InvalidTrackingIdException,
)


def test_aliexpress_exception_creation():
    """Tests the creation of AliexpressException."""
    reason = "Something went wrong"
    exception = AliexpressException(reason)
    assert exception.reason == reason
    assert str(exception) == reason


def test_aliexpress_exception_string_representation():
    """Tests the string representation of AliexpressException."""
    reason = "Invalid input"
    exception = AliexpressException(reason)
    assert str(exception) == reason


def test_invalid_argument_exception():
    """Tests the creation and string representation of InvalidArgumentException."""
    reason = "The input data is invalid"
    exception = InvalidArgumentException(reason)
    assert exception.reason == reason
    assert str(exception) == reason


def test_product_id_not_found_exception():
    """Tests the creation and string representation of ProductIdNotFoundException."""
    reason = "Product ID not found"
    exception = ProductIdNotFoundException(reason)
    assert exception.reason == reason
    assert str(exception) == reason


def test_api_request_exception():
    """Tests the creation and string representation of ApiRequestException."""
    reason = "API request failed"
    exception = ApiRequestException(reason)
    assert exception.reason == reason
    assert str(exception) == reason


def test_api_request_response_exception():
    """Tests the creation and string representation of ApiRequestResponseException."""
    reason = "API request response invalid"
    exception = ApiRequestResponseException(reason)
    assert exception.reason == reason
    assert str(exception) == reason


def test_products_not_found_exception():
    """Tests the creation and string representation of ProductsNotFoudException."""
    reason = "No products found"
    exception = ProductsNotFoudException(reason)
    assert exception.reason == reason
    assert str(exception) == reason

def test_categories_not_found_exception():
    """Tests the creation and string representation of CategoriesNotFoudException."""
    reason = "No categories found"
    exception = CategoriesNotFoudException(reason)
    assert exception.reason == reason
    assert str(exception) == reason

def test_invalid_tracking_id_exception():
    """Tests the creation and string representation of InvalidTrackingIdException."""
    reason = "Invalid tracking ID"
    exception = InvalidTrackingIdException(reason)
    assert exception.reason == reason
    assert str(exception) == reason


# Important:  Test exception raising (very crucial!)
def test_invalid_argument_exception_raising():
    """Tests the raising of InvalidArgumentException."""
    with pytest.raises(InvalidArgumentException) as excinfo:
        raise InvalidArgumentException("Invalid input")
    assert str(excinfo.value) == "Invalid input"

#Add more tests for other exceptions, if required.
#Example for testing a function that may raise exceptions:

# def my_function(input_data):
#     # ... your function ...
#     if input_data == "invalid":
#         raise InvalidArgumentException("Invalid input")
#     return "OK"

# def test_my_function_with_invalid_input():
#     with pytest.raises(InvalidArgumentException) as excinfo:
#         my_function("invalid")
#     assert str(excinfo.value) == "Invalid input"


```