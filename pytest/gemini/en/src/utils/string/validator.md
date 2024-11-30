```python
import pytest
import re
from hypotez.src.utils.string.validator import ProductFieldsValidator

# Fixture for testing purposes
@pytest.fixture
def example_data():
    return {
        "valid_price": "123.45",
        "invalid_price": "abc",
        "price_with_commas": "123,45",
        "empty_price": "",
        "valid_weight": "56.78",
        "invalid_weight": "def",
        "weight_with_commas": "123,45",
        "empty_weight": "",
        "valid_sku": "12345",
        "invalid_sku": "12",
        "valid_url": "https://www.example.com",
        "invalid_url": "invalid.url",
        "url_without_http": "www.example.com",
        "empty_url": "",
        "int_string": "123",
        "non_int_string": "abc"
    }

# Tests for ProductFieldsValidator.validate_price
def test_validate_price_valid(example_data):
    """Tests validate_price with a valid price."""
    assert ProductFieldsValidator.validate_price(example_data["valid_price"]) is True

def test_validate_price_invalid(example_data):
    """Tests validate_price with an invalid price."""
    assert ProductFieldsValidator.validate_price(example_data["invalid_price"]) is None

def test_validate_price_with_commas(example_data):
    """Tests validate_price with a price containing commas."""
    assert ProductFieldsValidator.validate_price(example_data["price_with_commas"]) is True

def test_validate_price_empty(example_data):
    """Tests validate_price with an empty string."""
    assert ProductFieldsValidator.validate_price(example_data["empty_price"]) is None

# Tests for ProductFieldsValidator.validate_weight
# (Similar structure to validate_price tests)
def test_validate_weight_valid(example_data):
    assert ProductFieldsValidator.validate_weight(example_data["valid_weight"]) is True

def test_validate_weight_invalid(example_data):
    assert ProductFieldsValidator.validate_weight(example_data["invalid_weight"]) is None

def test_validate_weight_with_commas(example_data):
    assert ProductFieldsValidator.validate_weight(example_data["weight_with_commas"]) is True

def test_validate_weight_empty(example_data):
    assert ProductFieldsValidator.validate_weight(example_data["empty_weight"]) is None


# Tests for ProductFieldsValidator.validate_sku
def test_validate_sku_valid(example_data):
    assert ProductFieldsValidator.validate_sku(example_data["valid_sku"]) is True

def test_validate_sku_invalid_short(example_data):
    assert ProductFieldsValidator.validate_sku(example_data["invalid_sku"]) is None

# Tests for ProductFieldsValidator.validate_url
def test_validate_url_valid(example_data):
    assert ProductFieldsValidator.validate_url(example_data["valid_url"]) is True

def test_validate_url_invalid(example_data):
    assert ProductFieldsValidator.validate_url(example_data["invalid_url"]) is None

def test_validate_url_without_http(example_data):
    assert ProductFieldsValidator.validate_url(example_data["url_without_http"]) is True


def test_validate_url_empty(example_data):
    assert ProductFieldsValidator.validate_url(example_data["empty_url"]) is None


def test_isint_valid(example_data):
    assert ProductFieldsValidator.isint(example_data["int_string"]) is True

def test_isint_invalid(example_data):
    assert ProductFieldsValidator.isint(example_data["non_int_string"]) is None
```