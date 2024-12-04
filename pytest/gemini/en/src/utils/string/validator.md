```python
import pytest
import re
from urllib.parse import urlparse

from hypotez.src.utils.string.validator import ProductFieldsValidator


# Fixture definitions (if needed)


@pytest.fixture
def valid_price():
    return "123.45"


@pytest.fixture
def invalid_price():
    return "abc"


@pytest.fixture
def empty_price():
    return ""


@pytest.fixture
def valid_weight():
    return "10.5kg"


@pytest.fixture
def invalid_weight():
    return "xyz"


@pytest.fixture
def empty_weight():
    return ""


@pytest.fixture
def valid_sku():
    return "12345"


@pytest.fixture
def invalid_sku():
    return "12"


@pytest.fixture
def empty_sku():
    return ""


@pytest.fixture
def valid_url():
    return "https://www.example.com"


@pytest.fixture
def invalid_url():
    return "invalid_url"


@pytest.fixture
def empty_url():
    return ""

@pytest.fixture
def valid_int_str():
    return "123"

@pytest.fixture
def invalid_int_str():
    return "abc"

# Tests for ProductFieldsValidator.validate_price
def test_validate_price_valid(valid_price):
    """Test validate_price with valid price."""
    assert ProductFieldsValidator.validate_price(valid_price) is True


def test_validate_price_invalid(invalid_price):
    """Test validate_price with invalid price (non-numeric)."""
    assert ProductFieldsValidator.validate_price(invalid_price) is None

def test_validate_price_empty(empty_price):
    """Test validate_price with empty price."""
    assert ProductFieldsValidator.validate_price(empty_price) is None




# Tests for ProductFieldsValidator.validate_weight
def test_validate_weight_valid(valid_weight):
    """Test validate_weight with valid weight."""
    assert ProductFieldsValidator.validate_weight(valid_weight) is True


def test_validate_weight_invalid(invalid_weight):
    """Test validate_weight with invalid weight (non-numeric)."""
    assert ProductFieldsValidator.validate_weight(invalid_weight) is None

def test_validate_weight_empty(empty_weight):
    """Test validate_weight with empty weight."""
    assert ProductFieldsValidator.validate_weight(empty_weight) is None



# Tests for ProductFieldsValidator.validate_sku
def test_validate_sku_valid(valid_sku):
    """Test validate_sku with valid sku."""
    assert ProductFieldsValidator.validate_sku(valid_sku) is True


def test_validate_sku_invalid_short(invalid_sku):
    """Test validate_sku with invalid sku (too short)."""
    assert ProductFieldsValidator.validate_sku(invalid_sku) is None

def test_validate_sku_empty(empty_sku):
    """Test validate_sku with empty sku."""
    assert ProductFieldsValidator.validate_sku(empty_sku) is None


# Tests for ProductFieldsValidator.validate_url
def test_validate_url_valid(valid_url):
    """Test validate_url with valid URL."""
    assert ProductFieldsValidator.validate_url(valid_url) is True


def test_validate_url_invalid(invalid_url):
    """Test validate_url with invalid URL."""
    assert ProductFieldsValidator.validate_url(invalid_url) is None


def test_validate_url_empty(empty_url):
    """Test validate_url with empty URL."""
    assert ProductFieldsValidator.validate_url(empty_url) is None


def test_isint_valid(valid_int_str):
    assert ProductFieldsValidator.isint(valid_int_str) is True


def test_isint_invalid(invalid_int_str):
    assert ProductFieldsValidator.isint(invalid_int_str) is None


```