```python
import pytest
import re
from hypotez.src.suppliers.aliexpress.utils.extract_product_id import extract_prod_ids, extract_id

def test_extract_prod_ids_valid_url():
    """Tests with a valid URL."""
    url = "https://www.aliexpress.com/item/123456.html"
    expected_output = "123456"
    assert extract_prod_ids(url) == expected_output

def test_extract_prod_ids_valid_urls_list():
    """Tests with a list of valid URLs."""
    urls = ["https://www.aliexpress.com/item/123456.html", "https://www.aliexpress.com/item/7891011.html"]
    expected_output = ["123456", "7891011"]
    assert extract_prod_ids(urls) == expected_output

def test_extract_prod_ids_valid_id():
    """Tests with a valid product ID."""
    prod_id = "123456"
    expected_output = "123456"
    assert extract_prod_ids(prod_id) == expected_output

def test_extract_prod_ids_invalid_url():
    """Tests with an invalid URL."""
    url = "https://www.example.com/item/abcdef.html"
    assert extract_prod_ids(url) is None

def test_extract_prod_ids_empty_list():
    """Tests with an empty list of URLs."""
    urls = []
    assert extract_prod_ids(urls) is None


def test_extract_prod_ids_mixed_valid_invalid_urls():
    """Tests with a list containing valid and invalid URLs."""
    urls = ["https://www.aliexpress.com/item/123456.html", "https://www.example.com/item/abcdef.html", "https://www.aliexpress.com/item/7891011.html"]
    expected_output = ["123456", "7891011"]
    assert extract_prod_ids(urls) == expected_output

def test_extract_id_valid_url():
    """Tests with a valid URL using the extract_id function."""
    url = "https://www.aliexpress.com/item/123456.html"
    expected_output = "123456"
    assert extract_id(url) == expected_output

def test_extract_id_valid_id():
    """Tests with a valid product ID using the extract_id function."""
    prod_id = "123456"
    expected_output = "123456"
    assert extract_id(prod_id) == expected_output

def test_extract_id_invalid_url():
    """Tests with an invalid URL using the extract_id function."""
    url = "https://www.example.com/item/abcdef.html"
    assert extract_id(url) is None

def test_extract_id_no_match():
    """Tests with a URL with no match using the extract_id function."""
    url = "https://www.example.com/product/123456"
    assert extract_id(url) is None


def test_extract_prod_ids_with_item_prefix():
    """Test with URLs containing 'item/' prefix"""
    urls = ["https://www.aliexpress.com/item/123456.html", "https://www.aliexpress.com/item/987654.html"]
    assert extract_prod_ids(urls) == ['123456', '987654']

def test_extract_prod_ids_with_no_item_prefix():
    """Test with URLs not containing 'item/' prefix"""
    urls = ["https://www.aliexpress.com/item-123456.html", "https://www.aliexpress.com/987654.html"]
    assert extract_prod_ids(urls) == ['123456', '987654']

def test_extract_prod_ids_with_empty_string():
    urls = ""
    assert extract_prod_ids(urls) is None

def test_extract_prod_ids_with_none():
    urls = None
    assert extract_prod_ids(urls) is None

# Add more tests as needed
```