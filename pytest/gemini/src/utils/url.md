```python
import pytest
from urllib.parse import urlparse, parse_qs
import validators
from hypotez.src.utils.string.url import extract_url_params, is_url

# Fixtures (if needed)


# Tests for extract_url_params
def test_extract_url_params_valid_url_with_params():
    """Checks function with a valid URL containing parameters."""
    url = "https://example.com/path?param1=value1&param2=value2&param3="
    expected_params = {"param1": "value1", "param2": "value2", "param3": ""}
    actual_params = extract_url_params(url)
    assert actual_params == expected_params

def test_extract_url_params_valid_url_with_multiple_values():
    url = "https://example.com/path?param1=value1&param1=value2"
    expected_params = {"param1": ["value1", "value2"]}
    actual_params = extract_url_params(url)
    assert actual_params == expected_params
    
def test_extract_url_params_valid_url_with_single_value_params():
    url = "https://example.com/path?param1=value1"
    expected_params = {"param1": "value1"}
    actual_params = extract_url_params(url)
    assert actual_params == expected_params
    

def test_extract_url_params_valid_url_no_params():
    """Checks function with a valid URL without parameters."""
    url = "https://example.com/path"
    assert extract_url_params(url) is None

def test_extract_url_params_invalid_url():
    """Checks function with an invalid URL."""
    url = "invalid_url"
    assert extract_url_params(url) is None

def test_extract_url_params_empty_string():
    """Checks function with an empty string."""
    url = ""
    assert extract_url_params(url) is None

# Tests for is_url
def test_is_url_valid_url():
    """Checks function with a valid URL."""
    url = "https://www.example.com"
    assert is_url(url) is True

def test_is_url_invalid_url():
    """Checks function with an invalid URL."""
    url = "invalid_url"
    assert is_url(url) is False

def test_is_url_empty_string():
    """Checks function with an empty string."""
    url = ""
    assert is_url(url) is False

def test_is_url_invalid_protocol():
    url = "ftp://example.com"
    assert is_url(url) is False

def test_is_url_with_fragment():
    url = "https://example.com/page#fragment"
    assert is_url(url) is True

def test_is_url_with_path():
    url = "https://example.com/path/to/resource.txt"
    assert is_url(url) is True


def test_is_url_invalid_characters():
    """Testing with special characters"""
    url = "https://example.com/path?param1=value1&param2=v@lue2"
    assert is_url(url) is True

def test_extract_url_params_with_non_ascii_characters():
    url = "https://example.com/path?param1=тест&param2=another_test"
    params = extract_url_params(url)
    assert params == {"param1": "тест", "param2": "another_test"}
```