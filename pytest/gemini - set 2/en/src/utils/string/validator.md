```python
import pytest
import re
from hypotez.src.utils.string.validator import ProductFieldsValidator

# Fixture definitions (if needed)


# Tests for validate_price
def test_validate_price_valid_input():
    """Checks validate_price with a valid price."""
    assert ProductFieldsValidator.validate_price("10.99") is True
    assert ProductFieldsValidator.validate_price("123456789.12") is True
    assert ProductFieldsValidator.validate_price("0.00") is True

def test_validate_price_invalid_input():
    """Checks validate_price with invalid price formats."""
    assert ProductFieldsValidator.validate_price("abc") is None
    assert ProductFieldsValidator.validate_price("10,99") is True  # Handles comma as decimal
    assert ProductFieldsValidator.validate_price("10.99.12") is None
    assert ProductFieldsValidator.validate_price("") is None
    assert ProductFieldsValidator.validate_price("10,99,12") is None  # Multiple commas

def test_validate_price_empty_string():
    """Checks validate_price with an empty string."""
    assert ProductFieldsValidator.validate_price("") is None


# Tests for validate_weight
def test_validate_weight_valid_input():
    """Checks validate_weight with valid weight."""
    assert ProductFieldsValidator.validate_weight("10.5") is True
    assert ProductFieldsValidator.validate_weight("5000") is True

def test_validate_weight_invalid_input():
    """Checks validate_weight with invalid weight formats."""
    assert ProductFieldsValidator.validate_weight("abc") is None
    assert ProductFieldsValidator.validate_weight("10,5") is True
    assert ProductFieldsValidator.validate_weight("10.5.5") is None
    assert ProductFieldsValidator.validate_weight("") is None
    assert ProductFieldsValidator.validate_weight("10,5,5") is None

def test_validate_weight_empty_string():
    """Checks validate_weight with an empty string."""
    assert ProductFieldsValidator.validate_weight("") is None


# Tests for validate_sku
def test_validate_sku_valid_input():
    """Checks validate_sku with valid SKU."""
    assert ProductFieldsValidator.validate_sku("12345") is True
    assert ProductFieldsValidator.validate_sku("ABCDE") is True
    assert ProductFieldsValidator.validate_sku("1234") is True


def test_validate_sku_invalid_input_short():
    """Checks validate_sku with too short SKU."""
    assert ProductFieldsValidator.validate_sku("12") is None


def test_validate_sku_invalid_input_empty():
    """Checks validate_sku with empty string."""
    assert ProductFieldsValidator.validate_sku("") is None



# Tests for validate_url
def test_validate_url_valid_input():
    """Checks validate_url with valid URLs."""
    assert ProductFieldsValidator.validate_url("https://www.example.com") is True
    assert ProductFieldsValidator.validate_url("http://example.com") is True
    assert ProductFieldsValidator.validate_url("https://example.com/path") is True
    assert ProductFieldsValidator.validate_url("http://example.com/?param=1") is True

def test_validate_url_invalid_input():
    """Checks validate_url with invalid or missing URLs."""
    assert ProductFieldsValidator.validate_url("invalid-url") is None
    assert ProductFieldsValidator.validate_url("") is None
    assert ProductFieldsValidator.validate_url("http:/example.com") is None  # Missing double slash


def test_validate_url_missing_protocol():
  """Checks validate_url with URL missing protocol"""
  assert ProductFieldsValidator.validate_url("example.com") is True


#Tests for isint
def test_isint_valid_input():
    """Checks isint with valid integers"""
    assert ProductFieldsValidator.isint("10") is True
    assert ProductFieldsValidator.isint("12345") is True
    assert ProductFieldsValidator.isint("0") is True


def test_isint_invalid_input():
    """Checks isint with non-integer input."""
    assert ProductFieldsValidator.isint("abc") is None
    assert ProductFieldsValidator.isint("10.5") is None
    assert ProductFieldsValidator.isint("") is None
```