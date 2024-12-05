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


# Tests for AliexpressException
def test_aliexpress_exception_creation():
    """Tests the creation of AliexpressException."""
    reason = "Product not found"
    exception = AliexpressException(reason)
    assert exception.reason == reason
    assert str(exception) == reason


def test_aliexpress_exception_string_representation():
    """Tests the string representation of AliexpressException."""
    reason = "Invalid request parameters"
    exception = AliexpressException(reason)
    assert str(exception) == reason


# Tests for InvalidArgumentException
def test_invalid_argument_exception():
    """Tests the creation of InvalidArgumentException."""
    reason = "Missing required parameter"
    exception = InvalidArgumentException(reason)
    assert exception.reason == reason
    assert str(exception) == reason


# Tests for ProductIdNotFoundException
def test_product_id_not_found_exception():
    """Tests the creation of ProductIdNotFoundException."""
    reason = "Product ID 123 not found"
    exception = ProductIdNotFoundException(reason)
    assert exception.reason == reason
    assert str(exception) == reason


# Tests for ApiRequestException
def test_api_request_exception():
    """Tests the creation of ApiRequestException."""
    reason = "Network error while connecting to AliExpress API"
    exception = ApiRequestException(reason)
    assert exception.reason == reason
    assert str(exception) == reason


# Tests for ApiRequestResponseException
def test_api_request_response_exception():
    """Tests the creation of ApiRequestResponseException."""
    reason = "Invalid response from AliExpress API"
    exception = ApiRequestResponseException(reason)
    assert exception.reason == reason
    assert str(exception) == reason


# Tests for ProductsNotFoudException
def test_products_not_found_exception():
    """Tests the creation of ProductsNotFoudException."""
    reason = "No products found matching the criteria"
    exception = ProductsNotFoudException(reason)
    assert exception.reason == reason
    assert str(exception) == reason


# Tests for CategoriesNotFoudException
def test_categories_not_found_exception():
    """Tests the creation of CategoriesNotFoudException."""
    reason = "No categories found matching the criteria"
    exception = CategoriesNotFoudException(reason)
    assert exception.reason == reason
    assert str(exception) == reason


# Tests for InvalidTrackingIdException
def test_invalid_tracking_id_exception():
    """Tests the creation of InvalidTrackingIdException."""
    reason = "Invalid or missing tracking ID"
    exception = InvalidTrackingIdException(reason)
    assert exception.reason == reason
    assert str(exception) == reason



#Tests for exception raising
def test_invalid_argument_exception_raising():
    with pytest.raises(InvalidArgumentException) as excinfo:
        raise InvalidArgumentException("Missing parameter")
    assert str(excinfo.value) == "Missing parameter"
```