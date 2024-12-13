```python
import pytest
from hypotez.src.suppliers.aliexpress.api.tools import get_product_id

# Fixture definitions, if needed
@pytest.fixture
def valid_product_url():
    """Provides a valid AliExpress product URL."""
    return "https://www.aliexpress.com/item/1005001234567890.html"

@pytest.fixture
def invalid_product_url():
    """Provides an invalid AliExpress product URL."""
    return "https://www.example.com/item/12345.html"

@pytest.fixture
def product_url_with_query():
  """Provides a valid AliExpress product URL with query parameters."""
  return "https://www.aliexpress.com/item/1005001234567890.html?spm=a2g0o.detail.1000023.1.2b2a2d0eT9iZ6P&gps-id=pcDetailBottomMoreThisSeller&scm=1007.13339.169870.0&scm_id=1007.13339.169870.0&scm-url=1007.13339.169870.0&pvid=e2f76c5b-2a5a-4b3c-a7b3-625d1a3e45a0&_t=gps-id:pcDetailBottomMoreThisSeller,scm-url:1007.13339.169870.0,pvid:e2f76c5b-2a5a-4b3c-a7b3-625d1a3e45a0,tpp_buckets:21387%230%23233228%234"


# Tests for get_product_id
def test_get_product_id_valid_url(valid_product_url):
    """Checks that get_product_id correctly extracts the product ID from a valid URL."""
    product_id = get_product_id(valid_product_url)
    assert product_id == "1005001234567890"

def test_get_product_id_invalid_url(invalid_product_url):
    """Checks that get_product_id returns None for an invalid URL."""
    product_id = get_product_id(invalid_product_url)
    assert product_id is None

def test_get_product_id_url_with_query(product_url_with_query):
  """Checks that get_product_id correctly extracts the product ID from a valid URL with query parameters."""
  product_id = get_product_id(product_url_with_query)
  assert product_id == "1005001234567890"

def test_get_product_id_empty_url():
    """Checks that get_product_id returns None for an empty URL."""
    product_id = get_product_id("")
    assert product_id is None

def test_get_product_id_none_url():
    """Checks that get_product_id returns None for None input."""
    product_id = get_product_id(None)
    assert product_id is None

def test_get_product_id_url_without_item_part():
  """Checks that get_product_id returns None if the URL does not contain item part"""
  url = "https://www.aliexpress.com/category/12345/stuff.html"
  product_id = get_product_id(url)
  assert product_id is None

def test_get_product_id_url_with_different_ending():
  """Checks that get_product_id correctly extracts the product ID from a valid URL with a different ending."""
  url = "https://www.aliexpress.com/item/1005001234567890"
  product_id = get_product_id(url)
  assert product_id == "1005001234567890"
```