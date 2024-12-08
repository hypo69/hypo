```python
import pytest
import re
from hypotez.src.suppliers.aliexpress.utils.extract_product_id import extract_prod_ids, extract_id

def test_extract_prod_ids_valid_url():
    """Tests extract_prod_ids with a valid URL."""
    url = "https://www.aliexpress.com/item/123456.html"
    result = extract_prod_ids(url)
    assert result == "123456"

def test_extract_prod_ids_valid_urls_list():
    """Tests extract_prod_ids with a list of valid URLs."""
    urls = ["https://www.aliexpress.com/item/123456.html", "https://www.aliexpress.com/item/7891011.html"]
    result = extract_prod_ids(urls)
    assert result == ["123456", "7891011"]

def test_extract_prod_ids_valid_mixed_input():
    """Tests extract_prod_ids with a valid URL and a valid product ID."""
    urls = ["https://www.aliexpress.com/item/123456.html", "7891011"]
    result = extract_prod_ids(urls)
    assert result == ["123456", "7891011"]


def test_extract_prod_ids_invalid_url():
    """Tests extract_prod_ids with an invalid URL."""
    url = "https://www.example.com/item/abcdef.html"
    result = extract_prod_ids(url)
    assert result is None

def test_extract_prod_ids_invalid_urls_list():
    """Tests extract_prod_ids with a list containing an invalid URL."""
    urls = ["https://www.example.com/item/abcdef.html", "https://www.aliexpress.com/item/7891011.html"]
    result = extract_prod_ids(urls)
    assert result == ["7891011"]


def test_extract_prod_ids_empty_list():
    """Tests extract_prod_ids with an empty list."""
    urls = []
    result = extract_prod_ids(urls)
    assert result is None


def test_extract_prod_ids_product_id_only():
    """Tests extract_prod_ids with a product ID string as input."""
    product_id = "7891011"
    result = extract_prod_ids(product_id)
    assert result == "7891011"


def test_extract_id_valid_url():
    """Tests extract_id with a valid URL."""
    url = "https://www.aliexpress.com/item/123456.html"
    result = extract_id(url)
    assert result == "123456"


def test_extract_id_valid_product_id():
    """Tests extract_id with a valid product ID."""
    product_id = "123456"
    result = extract_id(product_id)
    assert result == "123456"


def test_extract_id_invalid_url():
    """Tests extract_id with an invalid URL."""
    url = "https://www.example.com/item/abcdef.html"
    result = extract_id(url)
    assert result is None


def test_extract_id_no_match():
    """Tests extract_id with a URL with no match."""
    url = "https://www.example.com/item/"
    result = extract_id(url)
    assert result is None


def test_extract_id_missing_html():
    """Tests extract_id with a URL missing '.html'."""
    url = "https://www.aliexpress.com/item/123456"
    result = extract_id(url)
    assert result is None

def test_extract_id_with_item_prefix():
   url = "https://www.aliexpress.com/item/123456.html"
   result = extract_id(url)
   assert result == "123456"
def test_extract_id_with_item_prefix_no_slash():
   url = "https://www.aliexpress.com/item123456.html"
   result = extract_id(url)
   assert result is None
```