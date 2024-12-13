```python
import pytest

from hypotez.src.suppliers.aliexpress.api.tools.get_product_id import get_product_id
from hypotez.src.suppliers.aliexpress.errors import ProductIdNotFoundException


def test_get_product_id_valid_id_string():
    """Checks if the function returns the product ID when a valid ID is provided as a string."""
    product_id = "1234567890"
    assert get_product_id(product_id) == [product_id]


def test_get_product_id_valid_id_string_with_leading_and_trailing_spaces():
    """Checks if the function returns the product ID when a valid ID is provided as a string with leading and trailing spaces."""
    product_id = "   1234567890   "
    assert get_product_id(product_id) == ["1234567890"]

def test_get_product_id_valid_id_in_url_string():
    """Checks if the function returns the product ID when a valid ID is part of URL."""
    url = "https://www.aliexpress.com/item/1234567890.html"
    assert get_product_id(url) == ["1234567890"]

def test_get_product_id_valid_ids_in_url_string():
    """Checks if the function returns the product ID when multiple valid IDs are in part of URL."""
    url = "https://www.aliexpress.com/item/1234567890.html?item/9876543210.html"
    assert get_product_id(url) == ["1234567890", "9876543210"]


def test_get_product_id_invalid_input_no_id():
    """Checks if the function raises ProductIdNotFoundException when no product ID is found."""
    with pytest.raises(ProductIdNotFoundException):
        get_product_id("this is a text without a product id")


def test_get_product_id_invalid_input_empty_string():
    """Checks if the function raises ProductIdNotFoundException when the input is an empty string."""
    with pytest.raises(ProductIdNotFoundException):
        get_product_id("")

def test_get_product_id_invalid_input_non_numeric_string():
     """Checks if the function raises ProductIdNotFoundException when the input is a non-numeric string."""
     with pytest.raises(ProductIdNotFoundException):
         get_product_id("abc")

def test_get_product_id_invalid_input_string_with_letters_and_numbers():
    """Checks if the function raises ProductIdNotFoundException when the input is a string containing both numbers and letters not in url format."""
    with pytest.raises(ProductIdNotFoundException):
        get_product_id("abc123def")

def test_get_product_id_special_chars_input():
    """Checks if the function raises ProductIdNotFoundException when special characters are given"""
    with pytest.raises(ProductIdNotFoundException):
        get_product_id("!@#$%^&*()")
```