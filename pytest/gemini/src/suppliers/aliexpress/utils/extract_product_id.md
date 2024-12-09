```python
import pytest
import re
from hypotez.src.suppliers.aliexpress.utils.extract_product_id import extract_prod_ids, extract_id

# Test data
valid_urls = [
    "https://www.aliexpress.com/item/123456.html",
    "https://www.aliexpress.com/item/7891011.html",
    "https://www.aliexpress.com/item/987654321.html",
    "https://www.aliexpress.com/item/12345.html",  # Valid with lower number
]
invalid_urls = [
    "https://www.example.com/item/abcdef.html",
    "https://www.example.com/item/not-a-number.html",
    "invalid_url",
    "http://www.example.com",
    "https://www.aliexpress.com/item/",  # Missing number
]
valid_ids = ["123456", "7891011", "987654321", "12345"]
invalid_ids = ["abc", "123.45", " "]

mixed_urls = [
    "https://www.aliexpress.com/item/123456.html",
    "https://www.example.com/item/abcdef.html",
    "7891011",
]


def test_extract_id_valid_url():
    """Tests extracting ID from a valid URL."""
    assert extract_id(valid_urls[0]) == "123456"


def test_extract_id_valid_id():
    """Tests handling valid product IDs."""
    assert extract_id(valid_ids[0]) == "123456"


def test_extract_id_invalid_url():
    """Tests handling invalid URLs."""
    assert extract_id(invalid_urls[0]) is None
    assert extract_id(invalid_urls[1]) is None


def test_extract_id_empty_string():
    assert extract_id("") is None

def test_extract_id_invalid_id():
    """Tests handling invalid product IDs."""
    assert extract_id(invalid_ids[0]) is None

def test_extract_id_missing_number():
    """Tests handling URLs missing a number."""
    assert extract_id("https://www.aliexpress.com/item/") is None

def test_extract_id_valid_mixed_urls():
    """Tests handling mixed URLs and IDs."""
    assert extract_prod_ids(mixed_urls) == ["123456", "7891011"]



def test_extract_prod_ids_valid_list_urls():
    """Tests extracting IDs from a list of valid URLs."""
    extracted_ids = extract_prod_ids(valid_urls)
    assert extracted_ids == ["123456", "7891011", "987654321", "12345"]


def test_extract_prod_ids_empty_list_urls():
    """Tests extracting IDs from an empty list."""
    assert extract_prod_ids([]) is None


def test_extract_prod_ids_invalid_list_urls():
    """Tests extracting IDs from a list containing invalid URLs."""
    extracted_ids = extract_prod_ids(valid_urls + invalid_urls)
    assert extracted_ids == ["123456", "7891011", "987654321", "12345"]


def test_extract_prod_ids_mixed_urls_and_ids():
    """Tests handling mixed list of URLs and IDs."""
    mixed_input = valid_urls + valid_ids + invalid_urls
    extracted_ids = extract_prod_ids(mixed_input)
    assert extracted_ids == ["123456", "7891011", "987654321", "12345", "123456", "7891011", "987654321", "12345"]


def test_extract_prod_ids_valid_string_url():
    """Tests extracting IDs from a valid string URL."""
    assert extract_prod_ids(valid_urls[0]) == "123456"


def test_extract_prod_ids_invalid_string_url():
    """Tests extracting IDs from an invalid string URL."""
    assert extract_prod_ids(invalid_urls[0]) is None

def test_extract_prod_ids_valid_single_id():
  assert extract_prod_ids(valid_ids[0]) == "123456"

```