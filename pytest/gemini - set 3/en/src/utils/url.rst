```python
import pytest
from urllib.parse import urlparse, parse_qs
import validators
from hypotez.src.utils.string.url import extract_url_params, is_url

def test_extract_url_params_valid_url_with_params():
    """Checks extraction of parameters from a valid URL with multiple parameters."""
    url = "https://example.com?param1=value1&param2=value2&param3="
    expected_params = {"param1": "value1", "param2": "value2", "param3": ""}
    actual_params = extract_url_params(url)
    assert actual_params == expected_params

def test_extract_url_params_valid_url_with_single_param():
    """Checks extraction of parameters from a valid URL with a single value parameter."""
    url = "https://example.com?param1=value1"
    expected_params = {"param1": "value1"}
    actual_params = extract_url_params(url)
    assert actual_params == expected_params
    

def test_extract_url_params_valid_url_no_params():
    """Checks if extract_url_params returns None for a URL without parameters."""
    url = "https://example.com"
    actual_params = extract_url_params(url)
    assert actual_params is None


def test_extract_url_params_invalid_url():
    """Checks handling of an invalid URL string."""
    url = "invalid_url"
    actual_params = extract_url_params(url)
    assert actual_params is None

def test_extract_url_params_malformed_url():
    """Checks if extract_url_params handles malformed URL strings gracefully."""
    url = "https://example.com?param1=value1&param2"
    actual_params = extract_url_params(url)
    assert actual_params is None
    
def test_is_url_valid_url():
    """Checks if is_url returns True for a valid URL."""
    url = "https://www.example.com"
    assert is_url(url) is True

def test_is_url_invalid_url():
    """Checks if is_url returns False for an invalid URL."""
    url = "invalid-url"
    assert is_url(url) is False

def test_is_url_empty_string():
    """Checks if is_url handles empty strings correctly."""
    url = ""
    assert is_url(url) is False

def test_is_url_non_string_input():
    """Checks if is_url raises TypeError for non-string input."""
    with pytest.raises(TypeError):
        is_url(123)

def test_is_url_malformed_url():
    """Checks if is_url handles malformed URLs correctly."""
    url = "http:://invalid.url"
    assert is_url(url) is False

def test_is_url_no_protocol():
    """Checks if is_url handles URLs without a protocol correctly."""
    url = "example.com"
    assert is_url(url) is False

#This test assumes that input is a string, so no need to raise exception for non-string.
def test_is_url_with_special_chars():
    """Checks if is_url handles URLs with special characters correctly."""
    url = "https://example.com/path?param=value#fragment"
    assert is_url(url) is True
```