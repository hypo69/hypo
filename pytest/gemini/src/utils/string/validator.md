```python
import pytest
from hypotez.src.utils.string.validator import ProductFieldsValidator

# Define fixtures (if needed)


# Tests for validate_price
def test_validate_price_valid_input():
    """Checks validate_price with a valid price."""
    assert ProductFieldsValidator.validate_price("123.45") is True
    assert ProductFieldsValidator.validate_price("1000") is True
    assert ProductFieldsValidator.validate_price("12,34") is True  # Test comma handling


def test_validate_price_invalid_input():
    """Checks validate_price with invalid price formats."""
    assert ProductFieldsValidator.validate_price("abc") is None
    assert ProductFieldsValidator.validate_price("12.34.56") is None
    assert ProductFieldsValidator.validate_price("") is None
    assert ProductFieldsValidator.validate_price("12,34,56") is None  # Test multiple commas


def test_validate_price_empty_string():
    """Checks validate_price with an empty string."""
    assert ProductFieldsValidator.validate_price("") is None


# Tests for validate_weight
def test_validate_weight_valid_input():
    """Checks validate_weight with valid weight."""
    assert ProductFieldsValidator.validate_weight("50.2") is True
    assert ProductFieldsValidator.validate_weight("100") is True
    assert ProductFieldsValidator.validate_weight("10,50") is True  # Test comma handling


def test_validate_weight_invalid_input():
    """Checks validate_weight with invalid weight formats."""
    assert ProductFieldsValidator.validate_weight("xyz") is None
    assert ProductFieldsValidator.validate_weight("10.5.0") is None
    assert ProductFieldsValidator.validate_weight("") is None


def test_validate_weight_empty_string():
    """Checks validate_weight with an empty string."""
    assert ProductFieldsValidator.validate_weight("") is None


# Tests for validate_sku
def test_validate_sku_valid_input():
    """Checks validate_sku with a valid SKU."""
    assert ProductFieldsValidator.validate_sku("SKU123") is True
    assert ProductFieldsValidator.validate_sku("123") is True
    assert ProductFieldsValidator.validate_sku("ABC") is True



def test_validate_sku_invalid_input_short_sku():
    """Checks validate_sku with an invalid SKU (too short)."""
    assert ProductFieldsValidator.validate_sku("AB") is None


def test_validate_sku_invalid_input_empty_string():
    """Checks validate_sku with an empty string."""
    assert ProductFieldsValidator.validate_sku("") is None


# Tests for validate_url
def test_validate_url_valid_input():
    """Checks validate_url with a valid URL."""
    assert ProductFieldsValidator.validate_url("https://www.example.com") is True
    assert ProductFieldsValidator.validate_url("http://example.com") is True


def test_validate_url_invalid_input():
    """Checks validate_url with an invalid URL."""
    assert ProductFieldsValidator.validate_url("invalid-url") is None
    assert ProductFieldsValidator.validate_url("http://") is None
    assert ProductFieldsValidator.validate_url("") is None



def test_validate_url_missing_scheme():
    """Checks validate_url with a URL missing the scheme."""
    assert ProductFieldsValidator.validate_url("www.example.com") is None
    assert ProductFieldsValidator.validate_url("example.com") is None

# Tests for isint
def test_isint_valid_input():
    """Checks isint with a valid integer."""
    assert ProductFieldsValidator.isint("123") is True
    assert ProductFieldsValidator.isint("0") is True
    assert ProductFieldsValidator.isint("-10") is True
    
def test_isint_invalid_input():
    """Checks isint with an invalid input."""
    assert ProductFieldsValidator.isint("abc") is None
    assert ProductFieldsValidator.isint("12.34") is None
    assert ProductFieldsValidator.isint("") is None

```