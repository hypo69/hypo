```python
import pytest
import re
from hypotez.src.utils.string.validator import ProductFieldsValidator

# Define fixtures (if needed)


# Tests for validate_price
def test_validate_price_valid():
    """Checks valid price input."""
    assert ProductFieldsValidator.validate_price("10.50") is True
    assert ProductFieldsValidator.validate_price("1000") is True
    assert ProductFieldsValidator.validate_price("1234567890") is True
    assert ProductFieldsValidator.validate_price("10,50") is True  # Handles comma
    assert ProductFieldsValidator.validate_price("10.5000") is True # Handles multiple decimals

def test_validate_price_invalid():
    """Checks invalid price input."""
    assert ProductFieldsValidator.validate_price("abc") is None
    assert ProductFieldsValidator.validate_price("10,50,10") is None  # More than one comma
    assert ProductFieldsValidator.validate_price("") is None
    assert ProductFieldsValidator.validate_price("10.5.5") is None #multiple decimals

def test_validate_price_empty():
    """Checks handling of empty string."""
    assert ProductFieldsValidator.validate_price("") is None



# Tests for validate_weight
def test_validate_weight_valid():
    """Checks valid weight input."""
    assert ProductFieldsValidator.validate_weight("10.5") is True
    assert ProductFieldsValidator.validate_weight("1000") is True
    assert ProductFieldsValidator.validate_weight("1234567890") is True
    assert ProductFieldsValidator.validate_weight("10,50") is True # Handles comma
    assert ProductFieldsValidator.validate_weight("10.12345") is True #Handles multiple decimals
def test_validate_weight_invalid():
    """Checks invalid weight input."""
    assert ProductFieldsValidator.validate_weight("abc") is None
    assert ProductFieldsValidator.validate_weight("10,50,10") is None # Handles multiple commas
    assert ProductFieldsValidator.validate_weight("") is None
    assert ProductFieldsValidator.validate_weight("10.5.5") is None # handles multiple decimals


def test_validate_weight_empty():
    """Checks handling of empty string."""
    assert ProductFieldsValidator.validate_weight("") is None


# Tests for validate_sku
def test_validate_sku_valid():
    """Checks valid sku input."""
    assert ProductFieldsValidator.validate_sku("12345") is True
    assert ProductFieldsValidator.validate_sku("abcde") is True
    assert ProductFieldsValidator.validate_sku("SKU123") is True
    assert ProductFieldsValidator.validate_sku("  SKU-123  ") is True  # Handles whitespace
def test_validate_sku_invalid():
    """Checks invalid sku input."""
    assert ProductFieldsValidator.validate_sku("1") is None #Below min length
    assert ProductFieldsValidator.validate_sku("") is None
    assert ProductFieldsValidator.validate_sku(" ") is None #Only spaces
def test_validate_sku_short():
    """Checks handling of sku with length less than 3."""
    assert ProductFieldsValidator.validate_sku("ab") is None
    

# Tests for validate_url
def test_validate_url_valid():
    """Checks valid URL input."""
    assert ProductFieldsValidator.validate_url("https://www.example.com") is True
    assert ProductFieldsValidator.validate_url("http://example.com") is True
    assert ProductFieldsValidator.validate_url("https://subdomain.example.com/path?query=value") is True
def test_validate_url_invalid():
    """Checks invalid URL input."""
    assert ProductFieldsValidator.validate_url("invalid-url") is None
    assert ProductFieldsValidator.validate_url("") is None
    assert ProductFieldsValidator.validate_url("http:/example.com") is None #invalid URL
def test_validate_url_no_scheme():
    """Checks handling of URL without scheme."""
    assert ProductFieldsValidator.validate_url("example.com") is None #Missing scheme
def test_validate_url_no_netloc():
    """Checks handling of URL without netloc."""
    assert ProductFieldsValidator.validate_url("http://") is None #missing netloc


# Tests for isint (added)
def test_isint_valid():
    assert ProductFieldsValidator.isint("123") is True
    assert ProductFieldsValidator.isint("0") is True
    assert ProductFieldsValidator.isint("-10") is True

def test_isint_invalid():
    assert ProductFieldsValidator.isint("abc") is None
    assert ProductFieldsValidator.isint("1.2") is None
    assert ProductFieldsValidator.isint("") is None
```