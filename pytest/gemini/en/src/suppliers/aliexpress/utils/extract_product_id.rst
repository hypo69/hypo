```python
import pytest
import re
from hypotez.src.suppliers.aliexpress.utils.extract_product_id import extract_prod_ids, extract_id

def test_extract_prod_ids_valid_url():
    """Tests with a valid URL."""
    url = "https://www.aliexpress.com/item/123456.html"
    result = extract_prod_ids(url)
    assert result == "123456"

def test_extract_prod_ids_valid_urls_list():
    """Tests with a list of valid URLs."""
    urls = ["https://www.aliexpress.com/item/123456.html", "https://www.aliexpress.com/item/7891011.html"]
    result = extract_prod_ids(urls)
    assert result == ["123456", "7891011"]

def test_extract_prod_ids_mixed_urls():
    """Tests with a mixed list of valid and invalid URLs."""
    urls = ["https://www.aliexpress.com/item/123456.html", "https://www.example.com/item/abcdef.html", "7891011"]
    result = extract_prod_ids(urls)
    assert result == ["123456", "7891011"]

def test_extract_prod_ids_invalid_url():
    """Tests with an invalid URL."""
    url = "https://www.example.com/item/abcdef.html"
    result = extract_prod_ids(url)
    assert result is None


def test_extract_prod_ids_empty_list():
    """Tests with an empty list of URLs."""
    urls = []
    result = extract_prod_ids(urls)
    assert result is None


def test_extract_prod_ids_all_invalid_urls():
    """Tests with a list of URLs that don't match the pattern."""
    urls = ["https://www.example.com/item/abcdef.html", "https://www.example.com/item2/abcdef.html"]
    result = extract_prod_ids(urls)
    assert result is None

def test_extract_prod_ids_valid_product_id():
    """Tests with a valid product ID as input."""
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
  product_id = "7891011"
  result = extract_id(product_id)
  assert result == "7891011"
  
def test_extract_id_invalid_url():
  """Tests extract_id with an invalid URL."""
  url = "https://www.example.com/item/abcdef.html"
  result = extract_id(url)
  assert result is None
  
def test_extract_id_no_match():
    """Tests extract_id with a URL with no match."""
    url = "https://www.example.com/someotherpage.html"
    result = extract_id(url)
    assert result is None

def test_extract_id_empty_string():
  """Tests extract_id with an empty string."""
  url = ""
  result = extract_id(url)
  assert result is None

```