```python
import pytest
from urllib.parse import urlparse, parse_qs
import validators
from hypotez.src.utils.string.url import extract_url_params, is_url

def test_extract_url_params_valid_url_with_params():
    """Tests extract_url_params with a valid URL containing parameters."""
    url = "https://www.example.com/path?param1=value1&param2=value2&param3="
    expected_params = {"param1": "value1", "param2": "value2", "param3": ""}
    actual_params = extract_url_params(url)
    assert actual_params == expected_params

def test_extract_url_params_valid_url_with_multiple_values():
    """Tests extract_url_params with a valid URL containing parameters with multiple values."""
    url = "https://www.example.com/path?param1=value1&param1=value2&param2=value3"
    expected_params = {"param1": ["value1", "value2"], "param2": "value3"}
    actual_params = extract_url_params(url)
    assert actual_params == expected_params



def test_extract_url_params_valid_url_no_params():
    """Tests extract_url_params with a valid URL with no parameters."""
    url = "https://www.example.com/path"
    assert extract_url_params(url) is None


def test_extract_url_params_invalid_url():
    """Tests extract_url_params with an invalid URL."""
    url = "invalid_url"
    assert extract_url_params(url) is None


def test_is_url_valid_url():
    """Tests is_url with a valid URL."""
    url = "https://www.example.com"
    assert is_url(url) is True

def test_is_url_invalid_url():
    """Tests is_url with an invalid URL."""
    url = "invalid_url"
    assert is_url(url) is False


def test_is_url_empty_string():
    """Tests is_url with an empty string."""
    url = ""
    assert is_url(url) is False


def test_is_url_with_http():
    """Tests is_url with a URL starting with http."""
    url = "http://www.example.com"
    assert is_url(url) is True


def test_is_url_with_https():
    """Tests is_url with a URL starting with https."""
    url = "https://www.example.com"
    assert is_url(url) is True

def test_extract_url_params_malformed_url():
  """Tests extract_url_params with a malformed URL."""
  url = "invalid-url?param=value"
  assert extract_url_params(url) is None

def test_extract_url_params_url_with_only_one_param_value():
    """Tests with a url having only one value per key"""
    url = "https://www.example.com/?param1=value1"
    expected_params = {'param1': 'value1'}
    assert extract_url_params(url) == expected_params

def test_is_url_with_trailing_slash():
    """Tests is_url with a URL ending in a trailing slash."""
    url = "https://www.example.com/"
    assert is_url(url) is True


def test_is_url_with_different_protocols():
    """Tests is_url with different protocols (ftp, etc.)"""
    url = "ftp://ftp.example.com/file.txt"
    assert is_url(url) is True

```