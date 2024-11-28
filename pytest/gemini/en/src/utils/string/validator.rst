```python
import pytest
import re
from hypotez.src.utils.string.validator import ProductFieldsValidator

# Define fixtures if needed


# Tests for validate_price
def test_validate_price_valid_input():
    """Checks validate_price with a valid price."""
    assert ProductFieldsValidator.validate_price("123.45") is True
    assert ProductFieldsValidator.validate_price("1000") is True
    assert ProductFieldsValidator.validate_price("100,5") is True  # Handles comma
    assert ProductFieldsValidator.validate_price("1234567890.123456") is True


def test_validate_price_invalid_input():
    """Checks validate_price with invalid input (non-numeric)."""
    assert ProductFieldsValidator.validate_price("abc") is None  # Invalid price
    assert ProductFieldsValidator.validate_price("123.45a") is None  # Invalid price
    assert ProductFieldsValidator.validate_price("") is None  # Empty string
    assert ProductFieldsValidator.validate_price(" ") is None  # Whitespace


def test_validate_price_empty_string():
    """Checks validate_price with an empty string input."""
    assert ProductFieldsValidator.validate_price("") is None


# Tests for validate_weight
def test_validate_weight_valid_input():
    """Checks validate_weight with a valid weight."""
    assert ProductFieldsValidator.validate_weight("123.45") is True
    assert ProductFieldsValidator.validate_weight("1000") is True
    assert ProductFieldsValidator.validate_weight("100,5") is True  # Handles comma
    assert ProductFieldsValidator.validate_weight("1234567890.123456") is True


def test_validate_weight_invalid_input():
    """Checks validate_weight with invalid input (non-numeric)."""
    assert ProductFieldsValidator.validate_weight("abc") is None  # Invalid weight
    assert ProductFieldsValidator.validate_weight("123.45a") is None  # Invalid weight
    assert ProductFieldsValidator.validate_weight("") is None  # Empty string
    assert ProductFieldsValidator.validate_weight(" ") is None  # Whitespace


def test_validate_weight_empty_string():
    """Checks validate_weight with an empty string input."""
    assert ProductFieldsValidator.validate_weight("") is None


# Tests for validate_sku
def test_validate_sku_valid_input():
    """Checks validate_sku with valid input (minimum length)."""
    assert ProductFieldsValidator.validate_sku("12345") is True
    assert ProductFieldsValidator.validate_sku("SKU123") is True


def test_validate_sku_invalid_input_short():
    """Checks validate_sku with invalid input (too short)."""
    assert ProductFieldsValidator.validate_sku("12") is None  # Too short
    assert ProductFieldsValidator.validate_sku("") is None  # Empty string
    assert ProductFieldsValidator.validate_sku(" ") is None  # Whitespace



# Tests for validate_url
def test_validate_url_valid_input():
    """Checks validate_url with a valid URL."""
    assert ProductFieldsValidator.validate_url("https://www.example.com") is True
    assert ProductFieldsValidator.validate_url("http://example.com") is True
    assert ProductFieldsValidator.validate_url("https://example.org/path?query=param") is True

def test_validate_url_invalid_input():
    """Checks validate_url with invalid URL (missing scheme or netloc)."""
    assert ProductFieldsValidator.validate_url("example.com") is None
    assert ProductFieldsValidator.validate_url("http://") is None
    assert ProductFieldsValidator.validate_url("") is None
    assert ProductFieldsValidator.validate_url("invalid-url") is None


def test_validate_url_missing_protocol():
    """Checks validate_url with a URL missing the protocol."""
    assert ProductFieldsValidator.validate_url("www.example.com") is True


# Tests for isint
def test_isint_valid_input():
    """Checks isint with a valid integer string."""
    assert ProductFieldsValidator.isint("123") is True
    assert ProductFieldsValidator.isint("0") is True
    assert ProductFieldsValidator.isint("-10") is True


def test_isint_invalid_input():
    """Checks isint with an invalid integer string."""
    assert ProductFieldsValidator.isint("abc") is None
    assert ProductFieldsValidator.isint("12.3") is None
    assert ProductFieldsValidator.isint("") is None
    assert ProductFieldsValidator.isint(" ") is None
```