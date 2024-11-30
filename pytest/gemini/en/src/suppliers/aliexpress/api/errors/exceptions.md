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
    exception = AliexpressException("Invalid request")
    assert exception.reason == "Invalid request"
    assert str(exception) == "Invalid request"


def test_aliexpress_exception_custom_message():
    """Tests the __str__ method of AliexpressException."""
    exception = AliexpressException("Product not found")
    assert str(exception) == "Product not found"


def test_invalid_argument_exception():
    """Tests the InvalidArgumentException."""
    exception = InvalidArgumentException("Missing parameter")
    assert exception.reason == "Missing parameter"
    assert str(exception) == "Missing parameter"

def test_product_id_not_found_exception():
    """Tests the ProductIdNotFoundException."""
    exception = ProductIdNotFoundException("ID 123 not found")
    assert exception.reason == "ID 123 not found"
    assert str(exception) == "ID 123 not found"

def test_api_request_exception():
    """Tests the ApiRequestException."""
    exception = ApiRequestException("Network error")
    assert exception.reason == "Network error"
    assert str(exception) == "Network error"


def test_api_request_response_exception():
    """Tests the ApiRequestResponseException."""
    exception = ApiRequestResponseException("Invalid JSON response")
    assert exception.reason == "Invalid JSON response"
    assert str(exception) == "Invalid JSON response"

def test_products_not_found_exception():
    """Tests the ProductsNotFoudException."""
    exception = ProductsNotFoudException("No products found")
    assert exception.reason == "No products found"
    assert str(exception) == "No products found"


def test_categories_not_found_exception():
    """Tests the CategoriesNotFoudException."""
    exception = CategoriesNotFoudException("No categories found")
    assert exception.reason == "No categories found"
    assert str(exception) == "No categories found"


def test_invalid_tracking_id_exception():
    """Tests the InvalidTrackingIdException."""
    exception = InvalidTrackingIdException("Invalid tracking ID format")
    assert exception.reason == "Invalid tracking ID format"
    assert str(exception) == "Invalid tracking ID format"


@pytest.mark.parametrize("reason", [
  "Invalid request",
  "Missing parameter",
  "Incorrect format",
  "Network error",
  "Invalid JSON response",
  "No products found",
  "No categories found",
  "Invalid tracking ID format"
])
def test_custom_exception_inheritance(reason):
    """Tests inheritance from AliexpressException across various exceptions."""
    # Create instances of specific exceptions, passing a reason.
    if reason == "Invalid request":
       exception = AliexpressException(reason)
    elif reason == "Missing parameter":
       exception = InvalidArgumentException(reason)
    elif reason == "Incorrect format":
       exception = InvalidArgumentException(reason)
    elif reason == "Network error":
       exception = ApiRequestException(reason)
    elif reason == "Invalid JSON response":
       exception = ApiRequestResponseException(reason)
    elif reason == "No products found":
       exception = ProductsNotFoudException(reason)
    elif reason == "No categories found":
       exception = CategoriesNotFoudException(reason)
    elif reason == "Invalid tracking ID format":
        exception = InvalidTrackingIdException(reason)
    else:
      exception = AliexpressException(reason)

    assert isinstance(exception, AliexpressException), f"Exception {reason} is not a subtype of AliexpressException"
    assert str(exception) == reason, f"String representation of {reason} exception is incorrect."

```