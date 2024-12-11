```python
import pytest
from urllib.parse import urlparse, parse_qs
import validators
from hypotez.src.utils.string.url import extract_url_params, is_url

# Fixtures (if needed)


# Tests for extract_url_params
def test_extract_url_params_valid_url_with_params():
    """Checks correct extraction of parameters from a valid URL."""
    url = "https://example.com/path?param1=value1&param2=value2&param3="
    expected_params = {"param1": "value1", "param2": "value2", "param3": ""}
    actual_params = extract_url_params(url)
    assert actual_params == expected_params

def test_extract_url_params_valid_url_with_multiple_values():
    """Checks handling of multiple values for the same parameter."""
    url = "https://example.com/path?param1=value1&param1=value2&param3=value3"
    expected_params = {"param1": ["value1", "value2"], "param3": "value3"}
    actual_params = extract_url_params(url)
    assert actual_params == expected_params


def test_extract_url_params_valid_url_no_params():
    """Checks handling of a valid URL with no parameters."""
    url = "https://example.com/path"
    assert extract_url_params(url) is None


def test_extract_url_params_invalid_url():
    """Checks handling of an invalid URL."""
    url = "invalid_url"
    assert extract_url_params(url) is None

def test_extract_url_params_empty_url():
    """Checks handling of an empty URL string."""
    url = ""
    assert extract_url_params(url) is None

# Tests for is_url
def test_is_url_valid_url():
    """Checks if a valid URL is correctly identified."""
    url = "https://www.example.com"
    assert is_url(url) is True

def test_is_url_invalid_url():
    """Checks if an invalid URL is correctly identified."""
    url = "invalid-url"
    assert is_url(url) is False


def test_is_url_empty_string():
    """Checks if an empty string is considered as invalid URL."""
    url = ""
    assert is_url(url) is False

def test_is_url_with_special_characters():
    """Tests a URL with special characters."""
    url = "https://www.example.com/path?param1=value1&param2=value%20with%20space"
    assert is_url(url) is True

def test_is_url_non_string_input():
    """Tests with a non-string input."""
    with pytest.raises(TypeError):
        is_url(123)




```