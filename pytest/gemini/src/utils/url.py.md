```python
import pytest
from hypotez.src.utils.url import extract_url_params, is_url

# Test cases for extract_url_params function
def test_extract_url_params_valid_url_with_params():
    """Checks if parameters are correctly extracted from a valid URL with parameters."""
    url = "http://example.com?param1=value1&param2=value2"
    expected_params = {"param1": "value1", "param2": "value2"}
    assert extract_url_params(url) == expected_params

def test_extract_url_params_valid_url_with_single_param():
    """Checks if single parameter is correctly extracted from a valid URL."""
    url = "http://example.com?param1=value1"
    expected_params = {"param1": "value1"}
    assert extract_url_params(url) == expected_params

def test_extract_url_params_valid_url_with_multiple_values_for_same_param():
    """Checks if a parameter with multiple values is correctly extracted as a list."""
    url = "http://example.com?param1=value1&param1=value2"
    expected_params = {"param1": ["value1", "value2"]}
    assert extract_url_params(url) == expected_params

def test_extract_url_params_valid_url_with_empty_params():
    """Checks if empty parameters are handled correctly."""
    url = "http://example.com?"
    assert extract_url_params(url) is None

def test_extract_url_params_valid_url_without_params():
    """Checks if None is returned for a valid URL without parameters."""
    url = "http://example.com"
    assert extract_url_params(url) is None

def test_extract_url_params_url_with_no_scheme():
    """Checks if parameters are extracted when the URL has no scheme."""
    url = "example.com?param1=value1"
    expected_params = {"param1": "value1"}
    assert extract_url_params(url) == expected_params

def test_extract_url_params_url_with_special_characters():
    """Checks if special characters in URL parameters are handled correctly."""
    url = "http://example.com?param1=value%201&param2=value+2"
    expected_params = {"param1": "value 1", "param2": "value+2"}
    assert extract_url_params(url) == expected_params

def test_extract_url_params_empty_url():
    """Checks if empty URL returns None"""
    url = ""
    assert extract_url_params(url) is None
    
def test_extract_url_params_url_with_only_question_mark():
    """Checks if only question mark returns None"""
    url = "?"
    assert extract_url_params(url) is None


# Test cases for is_url function
def test_is_url_valid_url():
    """Checks if a valid URL is correctly identified."""
    assert is_url("http://example.com") is True
    assert is_url("https://example.com") is True
    assert is_url("ftp://example.com") is True
    assert is_url("http://subdomain.example.com") is True
    assert is_url("https://example.com/path/to/resource") is True
    assert is_url("http://example.com?param1=value1") is True

def test_is_url_invalid_url():
    """Checks if an invalid URL is correctly identified."""
    assert is_url("not a url") is False
    assert is_url("www.example.com") is False  # Missing scheme
    assert is_url("example.com") is False     # Missing scheme and www
    assert is_url("http://") is False         # Empty domain
    assert is_url("https://.com") is False
    assert is_url("http://example") is False
    assert is_url("http://example.") is False

def test_is_url_empty_string():
    """Checks if an empty string is correctly identified as not a URL."""
    assert is_url("") is False

def test_is_url_url_with_special_characters():
    """Checks if URL with special characters in path is valid."""
    assert is_url("http://example.com/path/with/space%20in/it") is True
    assert is_url("https://example.com/path/with/!@#$%^&*/in/it") is True

def test_is_url_url_with_port_number():
     """Checks if url with port is valid."""
     assert is_url("http://localhost:8080") is True
     assert is_url("https://example.com:8443") is True

def test_is_url_url_with_username_and_password():
    """Checks if url with username and password is valid"""
    assert is_url("http://username:password@example.com") is True
    
def test_is_url_url_with_unicode_characters():
     """Checks if urls with unicode is valid"""
     assert is_url("http://пример.com") is True
     assert is_url("https://üñîçøðê.com") is True
```