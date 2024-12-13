```python
import pytest
from hypotez.src.suppliers.aliexpress.utils.extract_product_id import extract_prod_ids


def test_extract_prod_ids_single_valid_url():
    """Checks correct extraction of a product ID from a single valid AliExpress URL."""
    url = "https://www.aliexpress.com/item/123456.html"
    assert extract_prod_ids(url) == "123456"


def test_extract_prod_ids_single_valid_id():
    """Checks correct return of a valid product ID when passed as a string."""
    product_id = "7891011"
    assert extract_prod_ids(product_id) == "7891011"


def test_extract_prod_ids_list_valid_urls():
    """Checks correct extraction of product IDs from a list of valid AliExpress URLs."""
    urls = ["https://www.aliexpress.com/item/123456.html", "https://www.aliexpress.com/item/7891011.html"]
    assert extract_prod_ids(urls) == ["123456", "7891011"]


def test_extract_prod_ids_list_mixed_urls_and_ids():
    """Checks correct extraction from a list containing both valid URLs and product IDs."""
    urls = ["https://www.aliexpress.com/item/123456.html", "7891011"]
    assert extract_prod_ids(urls) == ["123456", "7891011"]


def test_extract_prod_ids_list_mixed_valid_and_invalid_urls():
    """Checks correct extraction from a list containing valid and invalid URLs."""
    urls = ["https://www.aliexpress.com/item/123456.html", "https://www.example.com/item/abcdef.html"]
    assert extract_prod_ids(urls) == ["123456"]

def test_extract_prod_ids_list_only_invalid_urls():
    """Checks correct handling of a list containing only invalid URLs."""
    urls = ["https://www.example.com/item/abcdef.html", "https://www.example.com/item/ghijkl.html"]
    assert extract_prod_ids(urls) is None


def test_extract_prod_ids_single_invalid_url():
    """Checks correct handling of a single invalid URL."""
    url = "https://www.example.com/item/abcdef.html"
    assert extract_prod_ids(url) is None


def test_extract_prod_ids_empty_list():
    """Checks correct handling of an empty list."""
    urls = []
    assert extract_prod_ids(urls) is None


def test_extract_prod_ids_invalid_input_type():
    """Checks correct handling of an invalid input type."""
    with pytest.raises(AttributeError):
        extract_prod_ids(123456)


def test_extract_prod_ids_url_with_no_item_keyword():
    """Checks correct handling of a valid url without item keyword."""
    url = "https://www.aliexpress.com/123456.html"
    assert extract_prod_ids(url) == "123456"
    
def test_extract_prod_ids_url_with_slash_before_id():
    """Checks correct handling of a url with slash before product id"""
    url = "https://www.aliexpress.com/item/123456.html"
    assert extract_prod_ids(url) == '123456'
    
def test_extract_prod_ids_url_with_slash_before_and_after_id():
    """Checks correct handling of a url with slash before and after id"""
    url = "https://www.aliexpress.com/item/123456/.html"
    assert extract_prod_ids(url) == '123456'
```