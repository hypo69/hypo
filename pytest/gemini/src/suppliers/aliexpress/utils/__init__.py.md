```python
import pytest

from hypotez.src.suppliers.aliexpress.utils import extract_prod_ids, ensure_https, locales


# Fixtures can be added if needed for specific test setups
@pytest.fixture
def valid_url():
    return "https://www.aliexpress.com/item/1234567890.html"


@pytest.fixture
def invalid_url():
    return "http://www.example.com/somepage.html"


@pytest.fixture
def valid_url_no_protocol():
    return "www.aliexpress.com/item/1234567890.html"

# Tests for extract_prod_ids
def test_extract_prod_ids_valid_url(valid_url):
    """Test extracting product IDs from a valid AliExpress URL."""
    product_ids = extract_prod_ids(valid_url)
    assert product_ids == ["1234567890"]


def test_extract_prod_ids_invalid_url(invalid_url):
    """Test extracting product IDs from an invalid URL."""
    product_ids = extract_prod_ids(invalid_url)
    assert product_ids == []

def test_extract_prod_ids_multiple_ids():
    """Test extracting multiple product IDs from a string."""
    url_string = "https://www.aliexpress.com/item/1234567890.html https://www.aliexpress.com/item/0987654321.html"
    product_ids = extract_prod_ids(url_string)
    assert product_ids == ['1234567890', '0987654321']


def test_extract_prod_ids_empty_string():
    """Test extracting IDs from an empty string."""
    product_ids = extract_prod_ids("")
    assert product_ids == []

def test_extract_prod_ids_url_without_id():
    """Test extracting product IDs from an AliExpress URL without product IDs."""
    url = "https://www.aliexpress.com/category/123/test.html"
    product_ids = extract_prod_ids(url)
    assert product_ids == []


# Tests for ensure_https
def test_ensure_https_valid_https_url(valid_url):
    """Test that a valid HTTPS URL remains unchanged."""
    https_url = ensure_https(valid_url)
    assert https_url == valid_url


def test_ensure_https_http_url():
    """Test that a HTTP URL is converted to HTTPS."""
    http_url = "http://www.aliexpress.com/item/1234567890.html"
    https_url = ensure_https(http_url)
    assert https_url == "https://www.aliexpress.com/item/1234567890.html"

def test_ensure_https_no_protocol_url(valid_url_no_protocol):
    """Test that a URL with no protocol is converted to HTTPS."""
    https_url = ensure_https(valid_url_no_protocol)
    assert https_url == "https://www.aliexpress.com/item/1234567890.html"


def test_ensure_https_empty_string():
    """Test ensure_https with an empty string."""
    https_url = ensure_https("")
    assert https_url == ""


def test_ensure_https_non_url_string():
     """Test ensure_https with a non-URL string."""
     non_url_string = "not a url"
     https_url = ensure_https(non_url_string)
     assert https_url == "not a url"


# Tests for locales
def test_locales_is_dict():
    """Test if locales is a dictionary."""
    assert isinstance(locales, dict)


def test_locales_contains_keys():
     """Test if locales contains some of the expected keys."""
     assert "en" in locales
     assert "ru" in locales
     assert "es" in locales

def test_locales_values_are_strings():
    """Test if locales values are all strings."""
    for key, value in locales.items():
        assert isinstance(value, str)
```