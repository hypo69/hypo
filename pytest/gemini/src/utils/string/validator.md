```python
import pytest
import re
from urllib.parse import urlparse

from hypotez.src.utils.string.validator import ProductFieldsValidator

# This is a placeholder as the code defines Ptrn and StringFormatter but doesn't define them
# Replace with actual implementations if available.
class Ptrn:
    clear_price = re.compile(r"[^0-9,.]")
    clear_number = re.compile(r"[^0-9]")


class StringFormatter:
    @staticmethod
    def remove_special_characters(text):
        return re.sub(r"[^a-zA-Z0-9]", "", text)
    
    @staticmethod
    def remove_line_breaks(text):
      return text.replace('\n', '').replace('\r', '')



def test_validate_price_valid_input():
    """Checks validate_price with a valid price."""
    assert ProductFieldsValidator.validate_price("123.45") is True
    assert ProductFieldsValidator.validate_price("1000") is True
    assert ProductFieldsValidator.validate_price("1,234.56") is True  # Validates with comma


def test_validate_price_invalid_input():
    """Checks validate_price with an invalid price."""
    assert ProductFieldsValidator.validate_price("abc") is None
    assert ProductFieldsValidator.validate_price("123.45.67") is None
    assert ProductFieldsValidator.validate_price("") is None #Empty string


def test_validate_price_empty_string():
  assert ProductFieldsValidator.validate_price("") is None

def test_validate_weight_valid_input():
    """Checks validate_weight with a valid weight."""
    assert ProductFieldsValidator.validate_weight("123.45") is True
    assert ProductFieldsValidator.validate_weight("1000") is True
    assert ProductFieldsValidator.validate_weight("1,234.56") is True


def test_validate_weight_invalid_input():
    """Checks validate_weight with an invalid weight."""
    assert ProductFieldsValidator.validate_weight("xyz") is None
    assert ProductFieldsValidator.validate_weight("123.45.67") is None
    assert ProductFieldsValidator.validate_weight("") is None


def test_validate_weight_empty_string():
  assert ProductFieldsValidator.validate_weight("") is None

def test_validate_sku_valid_input():
    """Checks validate_sku with valid SKU."""
    assert ProductFieldsValidator.validate_sku("SKU123") is True
    assert ProductFieldsValidator.validate_sku("abc123") is True
    assert ProductFieldsValidator.validate_sku("12345") is True
    assert ProductFieldsValidator.validate_sku("longSKU") is True


def test_validate_sku_invalid_input():
    """Checks validate_sku with invalid SKU (too short)."""
    assert ProductFieldsValidator.validate_sku("ab") is None  # Less than 3 chars


def test_validate_sku_empty_string():
  assert ProductFieldsValidator.validate_sku("") is None



def test_validate_url_valid_input():
    """Checks validate_url with a valid URL."""
    assert ProductFieldsValidator.validate_url("https://www.example.com") is True
    assert ProductFieldsValidator.validate_url("http://example.com") is True
    assert ProductFieldsValidator.validate_url("https://example.com/path?query=value") is True


def test_validate_url_invalid_input():
    """Checks validate_url with an invalid URL."""
    assert ProductFieldsValidator.validate_url("invalid_url") is None
    assert ProductFieldsValidator.validate_url("http:/example.com") is None #Invalid schema


def test_validate_url_missing_parts():
    """Checks validate_url with URLs missing parts"""
    assert ProductFieldsValidator.validate_url("example.com") is None
    assert ProductFieldsValidator.validate_url("http://") is None


def test_validate_url_empty_string():
  assert ProductFieldsValidator.validate_url("") is None


def test_isint_valid_input():
  assert ProductFieldsValidator.isint("123") is True
  assert ProductFieldsValidator.isint("0") is True

def test_isint_invalid_input():
  assert ProductFieldsValidator.isint("abc") is None
  assert ProductFieldsValidator.isint("12.3") is None
  assert ProductFieldsValidator.isint("") is None
```