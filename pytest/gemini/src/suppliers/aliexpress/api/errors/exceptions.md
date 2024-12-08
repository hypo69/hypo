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


def test_aliexpress_exception_init():
    """Tests the initialization of the AliexpressException class."""
    reason = "This is a test reason."
    exception = AliexpressException(reason)
    assert exception.reason == reason
    assert str(exception) == reason


def test_aliexpress_exception_str():
    """Tests the __str__ method of the AliexpressException class."""
    reason = "Error reason"
    exception = AliexpressException(reason)
    assert str(exception) == reason


def test_invalid_argument_exception():
    """Tests the InvalidArgumentException class."""
    reason = "Invalid arguments provided"
    exception = InvalidArgumentException(reason)
    assert exception.reason == reason
    assert str(exception) == reason


def test_product_id_not_found_exception():
    """Tests the ProductIdNotFoundException class."""
    reason = "Product ID not found"
    exception = ProductIdNotFoundException(reason)
    assert exception.reason == reason
    assert str(exception) == reason


def test_api_request_exception():
    """Tests the ApiRequestException class."""
    reason = "API request failed"
    exception = ApiRequestException(reason)
    assert exception.reason == reason
    assert str(exception) == reason


def test_api_request_response_exception():
    """Tests the ApiRequestResponseException class."""
    reason = "Invalid API response"
    exception = ApiRequestResponseException(reason)
    assert exception.reason == reason
    assert str(exception) == reason


def test_products_not_found_exception():
    """Tests the ProductsNotFoudException class."""
    reason = "No products found"
    exception = ProductsNotFoudException(reason)
    assert exception.reason == reason
    assert str(exception) == reason


def test_categories_not_found_exception():
    """Tests the CategoriesNotFoudException class."""
    reason = "No categories found"
    exception = CategoriesNotFoudException(reason)
    assert exception.reason == reason
    assert str(exception) == reason


def test_invalid_tracking_id_exception():
    """Tests the InvalidTrackingIdException class."""
    reason = "Invalid tracking ID"
    exception = InvalidTrackingIdException(reason)
    assert exception.reason == reason
    assert str(exception) == reason


@pytest.mark.parametrize(
    "exception_type, reason",
    [
        (InvalidArgumentException, "Invalid arguments provided"),
        (ProductIdNotFoundException, "Product ID not found"),
        (ApiRequestException, "API request failed"),
        (ApiRequestResponseException, "Invalid API response"),
        (ProductsNotFoudException, "No products found"),
        (CategoriesNotFoudException, "No categories found"),
        (InvalidTrackingIdException, "Invalid tracking ID"),
    ],
)
def test_exception_inheritance(exception_type, reason):
    """Tests inheritance and exception raising."""
    exception = exception_type(reason)
    assert isinstance(exception, AliexpressException)

```