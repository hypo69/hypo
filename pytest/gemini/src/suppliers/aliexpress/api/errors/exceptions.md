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
    InvalidTrackingIdException
)


# Test cases for AliexpressException
def test_aliexpress_exception_creation():
    """Tests the creation of AliexpressException."""
    reason = "Test reason"
    exception = AliexpressException(reason)
    assert exception.reason == reason
    assert str(exception) == reason


def test_aliexpress_exception_string_representation():
    """Tests string representation of AliexpressException."""
    reason = "Error message"
    exception = AliexpressException(reason)
    assert str(exception) == reason


# Test cases for InvalidArgumentException
def test_invalid_argument_exception():
    """Tests creation and string representation of InvalidArgumentException."""
    reason = "Invalid argument provided"
    exception = InvalidArgumentException(reason)
    assert exception.reason == reason
    assert str(exception) == reason

# Test cases for ProductIdNotFoundException
def test_product_id_not_found_exception():
    """Tests creation and string representation of ProductIdNotFoundException."""
    reason = "Product ID not found"
    exception = ProductIdNotFoundException(reason)
    assert exception.reason == reason
    assert str(exception) == reason

# Test cases for ApiRequestException
def test_api_request_exception():
    """Tests creation and string representation of ApiRequestException."""
    reason = "API request failed"
    exception = ApiRequestException(reason)
    assert exception.reason == reason
    assert str(exception) == reason


# Test cases for ApiRequestResponseException
def test_api_request_response_exception():
    """Tests creation and string representation of ApiRequestResponseException."""
    reason = "Invalid API response"
    exception = ApiRequestResponseException(reason)
    assert exception.reason == reason
    assert str(exception) == reason


# Test cases for ProductsNotFoudException
def test_products_not_found_exception():
    """Tests creation and string representation of ProductsNotFoudException."""
    reason = "No products found"
    exception = ProductsNotFoudException(reason)
    assert exception.reason == reason
    assert str(exception) == reason


# Test cases for CategoriesNotFoudException
def test_categories_not_found_exception():
    """Tests creation and string representation of CategoriesNotFoudException."""
    reason = "No categories found"
    exception = CategoriesNotFoudException(reason)
    assert exception.reason == reason
    assert str(exception) == reason


# Test cases for InvalidTrackingIdException
def test_invalid_tracking_id_exception():
    """Tests creation and string representation of InvalidTrackingIdException."""
    reason = "Invalid tracking ID"
    exception = InvalidTrackingIdException(reason)
    assert exception.reason == reason
    assert str(exception) == reason


# Test for invalid inputs, these could potentially fail with TypeError.
def test_invalid_reason_type():
    with pytest.raises(TypeError):
        AliexpressException(123)  # Passing an integer as reason.
```