```python
import pytest
import re
from hypotez.src.suppliers.aliexpress.utils.extract_product_id import extract_prod_ids, extract_id

def test_extract_prod_ids_valid_url():
    """Tests extract_prod_ids with a valid URL."""
    url = "https://www.aliexpress.com/item/123456.html"
    expected_id = "123456"
    actual_id = extract_prod_ids(url)
    assert actual_id == expected_id

def test_extract_prod_ids_valid_urls_list():
    """Tests extract_prod_ids with a list of valid URLs."""
    urls = ["https://www.aliexpress.com/item/123456.html", "https://www.aliexpress.com/item/7891011.html"]
    expected_ids = ["123456", "7891011"]
    actual_ids = extract_prod_ids(urls)
    assert actual_ids == expected_ids

def test_extract_prod_ids_mixed_urls_list():
    """Tests extract_prod_ids with a list containing both valid and invalid URLs."""
    urls = ["https://www.aliexpress.com/item/123456.html", "https://www.example.com/item/abcdef.html", "7891011"]
    expected_ids = ["123456", "7891011"]
    actual_ids = extract_prod_ids(urls)
    assert actual_ids == expected_ids


def test_extract_prod_ids_valid_id_string():
    """Tests extract_prod_ids with a valid product ID string."""
    product_id = "123456"
    expected_id = "123456"
    actual_id = extract_prod_ids(product_id)
    assert actual_id == expected_id

def test_extract_prod_ids_invalid_url():
    """Tests extract_prod_ids with an invalid URL."""
    url = "https://www.example.com/item/abcdef.html"
    actual_id = extract_prod_ids(url)
    assert actual_id is None

def test_extract_prod_ids_empty_list():
    """Tests extract_prod_ids with an empty list of URLs."""
    urls = []
    actual_ids = extract_prod_ids(urls)
    assert actual_ids is None

def test_extract_id_valid_url():
    """Tests extract_id with a valid URL."""
    url = "https://www.aliexpress.com/item/123456.html"
    expected_id = "123456"
    actual_id = extract_id(url)
    assert actual_id == expected_id

def test_extract_id_valid_id():
    """Tests extract_id with a valid product ID."""
    product_id = "7891011"
    expected_id = "7891011"
    actual_id = extract_id(product_id)
    assert actual_id == expected_id
    
def test_extract_id_invalid_url():
    """Tests extract_id with an invalid URL."""
    url = "https://www.example.com/item/abcdef.html"
    actual_id = extract_id(url)
    assert actual_id is None

def test_extract_id_no_match():
    """Tests extract_id with a URL with no match."""
    url = "https://www.example.com/something.html"
    actual_id = extract_id(url)
    assert actual_id is None
```