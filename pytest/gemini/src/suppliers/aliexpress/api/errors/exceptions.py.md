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
    """Checks if AliexpressException is created correctly and has the correct reason."""
    reason = "Test reason"
    exception = AliexpressException(reason)
    assert exception.reason == reason
    assert str(exception) == reason


def test_aliexpress_exception_str():
    """Checks if the __str__ method returns the correct reason."""
    reason = "Another test reason"
    exception = AliexpressException(reason)
    assert str(exception) == reason


# Tests for InvalidArgumentException
def test_invalid_argument_exception_creation():
    """Checks if InvalidArgumentException is created correctly."""
    reason = "Invalid argument"
    exception = InvalidArgumentException(reason)
    assert isinstance(exception, AliexpressException)
    assert exception.reason == reason
    assert str(exception) == reason


# Tests for ProductIdNotFoundException
def test_product_id_not_found_exception_creation():
    """Checks if ProductIdNotFoundException is created correctly."""
    reason = "Product ID not found"
    exception = ProductIdNotFoundException(reason)
    assert isinstance(exception, AliexpressException)
    assert exception.reason == reason
    assert str(exception) == reason

# Tests for ApiRequestException
def test_api_request_exception_creation():
    """Checks if ApiRequestException is created correctly."""
    reason = "API request failed"
    exception = ApiRequestException(reason)
    assert isinstance(exception, AliexpressException)
    assert exception.reason == reason
    assert str(exception) == reason


# Tests for ApiRequestResponseException
def test_api_request_response_exception_creation():
    """Checks if ApiRequestResponseException is created correctly."""
    reason = "API request response invalid"
    exception = ApiRequestResponseException(reason)
    assert isinstance(exception, AliexpressException)
    assert exception.reason == reason
    assert str(exception) == reason


# Tests for ProductsNotFoudException
def test_products_not_found_exception_creation():
    """Checks if ProductsNotFoudException is created correctly."""
    reason = "No products found"
    exception = ProductsNotFoudException(reason)
    assert isinstance(exception, AliexpressException)
    assert exception.reason == reason
    assert str(exception) == reason


# Tests for CategoriesNotFoudException
def test_categories_not_found_exception_creation():
    """Checks if CategoriesNotFoudException is created correctly."""
    reason = "No categories found"
    exception = CategoriesNotFoudException(reason)
    assert isinstance(exception, AliexpressException)
    assert exception.reason == reason
    assert str(exception) == reason


# Tests for InvalidTrackingIdException
def test_invalid_tracking_id_exception_creation():
    """Checks if InvalidTrackingIdException is created correctly."""
    reason = "Invalid tracking ID"
    exception = InvalidTrackingIdException(reason)
    assert isinstance(exception, AliexpressException)
    assert exception.reason == reason
    assert str(exception) == reason
```