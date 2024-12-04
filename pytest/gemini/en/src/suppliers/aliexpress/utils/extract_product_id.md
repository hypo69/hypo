```python
import pytest
import re
from hypotez.src.suppliers.aliexpress.utils.extract_product_id import extract_prod_ids, extract_id

def test_extract_prod_ids_valid_url():
    """Checks correct extraction from a valid URL."""
    url = "https://www.aliexpress.com/item/123456.html"
    expected_id = "123456"
    assert extract_prod_ids(url) == expected_id

def test_extract_prod_ids_valid_urls_list():
    """Checks correct extraction from a list of valid URLs."""
    urls = ["https://www.aliexpress.com/item/123456.html", "https://www.aliexpress.com/item/7891011.html"]
    expected_ids = ["123456", "7891011"]
    assert extract_prod_ids(urls) == expected_ids

def test_extract_prod_ids_valid_prod_id():
    """Checks correct handling of a valid product ID."""
    prod_id = "7891011"
    expected_id = "7891011"
    assert extract_prod_ids(prod_id) == expected_id

def test_extract_prod_ids_invalid_url():
    """Checks handling of an invalid URL."""
    url = "https://www.example.com/item/abcdef.html"
    assert extract_prod_ids(url) is None


def test_extract_prod_ids_mixed_urls():
    """Checks handling of a mix of valid and invalid URLs."""
    urls = ["https://www.aliexpress.com/item/123456.html", "https://www.example.com/item/abcdef.html", "7891011"]
    expected_ids = ["123456", "7891011"]
    assert extract_prod_ids(urls) == expected_ids


def test_extract_prod_ids_empty_list():
    """Tests with an empty list."""
    urls = []
    assert extract_prod_ids(urls) is None


def test_extract_id_valid_url():
    """Checks valid URL extraction."""
    url = "https://www.aliexpress.com/item/123456.html"
    expected_id = "123456"
    assert extract_id(url) == expected_id


def test_extract_id_valid_prod_id():
  """Checks valid product ID input."""
  prod_id = "123456"
  assert extract_id(prod_id) == prod_id

def test_extract_id_invalid_url():
    """Checks invalid URL handling."""
    url = "https://www.example.com/item/abcdef.html"
    assert extract_id(url) is None


def test_extract_id_no_match():
    """Checks handling of URLs with no match."""
    url = "https://www.example.com/somethingelse.html"
    assert extract_id(url) is None

def test_extract_id_with_item_prefix():
    """Tests URL with optional 'item/' prefix"""
    url = "https://www.aliexpress.com/item/123456.html"
    expected = "123456"
    assert extract_id(url) == expected

    url2 = "https://www.aliexpress.com/123456.html"
    expected2 = "123456"
    assert extract_id(url2) == expected2

def test_extract_id_non_string_input():
    """Tests non-string input."""
    with pytest.raises(TypeError):
        extract_id(123)
```