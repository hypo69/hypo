```python
import pytest
import re
from hypotez.src.suppliers.aliexpress.utils.extract_product_id import extract_prod_ids, extract_id

# Test data
VALID_URLS = [
    "https://www.aliexpress.com/item/123456.html",
    "https://www.aliexpress.com/item/7891011.html",
    "https://www.aliexpress.com/item/987654321.html",
]
INVALID_URLS = [
    "https://www.example.com/item/abcdef.html",
    "https://www.aliexpress.com/item/",  # Missing ID
    "invalid_url",
]
PRODUCT_IDS = [
    "123456",
    "7891011",
    "987654321",
]
MIXED_INPUT = [
    "https://www.aliexpress.com/item/123456.html",
    "https://www.example.com/item/abcdef.html",
    "7891011",
]


def test_extract_prod_ids_valid_url():
    """Tests with a valid URL."""
    result = extract_prod_ids(VALID_URLS[0])
    assert result == "123456"


def test_extract_prod_ids_valid_urls_list():
    """Tests with a list of valid URLs."""
    result = extract_prod_ids(VALID_URLS)
    assert result == ["123456", "7891011", "987654321"]


def test_extract_prod_ids_invalid_urls_list():
    """Tests with a list of invalid URLs."""
    result = extract_prod_ids(INVALID_URLS)
    assert result is None


def test_extract_prod_ids_mixed_input():
    """Tests with a mixed list of URLs and IDs."""
    result = extract_prod_ids(MIXED_INPUT)
    assert result == ["123456", "7891011"]


def test_extract_prod_ids_single_id():
    """Tests with a valid product ID."""
    result = extract_prod_ids(PRODUCT_IDS[0])
    assert result == "123456"


def test_extract_prod_ids_invalid_id():
    """Tests with an invalid product ID (not a number)."""
    result = extract_prod_ids("abcdef")
    assert result is None



def test_extract_prod_ids_empty_list():
    """Tests with an empty list."""
    result = extract_prod_ids([])
    assert result is None


def test_extract_id_valid_url():
    """Tests the extract_id function with a valid URL."""
    result = extract_id(VALID_URLS[0])
    assert result == "123456"


def test_extract_id_invalid_url():
    """Tests the extract_id function with an invalid URL."""
    result = extract_id(INVALID_URLS[0])
    assert result is None

def test_extract_id_valid_product_id():
    """Tests with a valid product ID."""
    result = extract_id(PRODUCT_IDS[1])
    assert result == "7891011"

def test_extract_id_empty_string():
    """Tests with an empty string."""
    result = extract_id("")
    assert result is None

def test_extract_id_no_match():
    """Tests with a URL with no match."""
    result = extract_id("https://www.example.com/item/")
    assert result is None


def test_extract_id_already_id():
    """Tests with a URL that's already a valid product ID."""
    result = extract_id(PRODUCT_IDS[0])
    assert result == "123456"

```