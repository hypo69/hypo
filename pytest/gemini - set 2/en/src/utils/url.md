```python
import pytest
from urllib.parse import urlparse, parse_qs
import validators
from hypotez.src.utils.string.url import extract_url_params, is_url

# Test data
valid_url = "https://www.example.com?param1=value1&param2=value2&param3="
valid_url_single_param = "https://www.example.com?param1=value1"
invalid_url = "invalid_url"
url_with_empty_query = "https://www.example.com"
url_with_multiple_values = "https://www.example.com?param1=value1&param1=value2"
url_with_space = "https://example.com?param1=value 1"


def test_extract_url_params_valid_url():
    """Checks correct extraction of parameters from a valid URL."""
    params = extract_url_params(valid_url)
    assert params == {'param1': 'value1', 'param2': 'value2', 'param3': ''}  # Correctly handles empty values

def test_extract_url_params_valid_url_single_param():
    """Checks correct extraction of parameters from a URL with a single parameter."""
    params = extract_url_params(valid_url_single_param)
    assert params == {'param1': 'value1'}


def test_extract_url_params_url_with_empty_query():
    """Checks extraction from a URL with no query parameters."""
    params = extract_url_params(url_with_empty_query)
    assert params is None


def test_extract_url_params_with_multiple_values():
    """Checks extraction when a parameter has multiple values."""
    params = extract_url_params(url_with_multiple_values)
    assert params == {'param1': 'value2'} # Correct handling


def test_extract_url_params_invalid_url():
    """Checks handling of an invalid URL."""
    params = extract_url_params(invalid_url)
    assert params is None


def test_extract_url_params_with_space():
    """Checks extraction when a parameter value has spaces."""
    params = extract_url_params(url_with_space)
    assert params == {"param1": "value 1"}


def test_is_url_valid():
    """Tests with a valid URL."""
    assert is_url(valid_url) is True


def test_is_url_invalid():
    """Tests with an invalid URL."""
    assert is_url(invalid_url) is False

def test_is_url_empty_string():
  """Tests with an empty string."""
  assert is_url("") is False

def test_is_url_valid_single_param():
    """Tests with a valid URL containing a single parameter."""
    assert is_url(valid_url_single_param) is True


def test_is_url_no_query():
    """Tests a URL without query parameters."""
    assert is_url(url_with_empty_query) is True


#Additional tests for edge cases (these are important)
def test_is_url_with_non_ascii():
  """Tests with a URL containing non-ASCII characters."""
  url_non_ascii = "https://example.com/page?param=你好世界"
  assert is_url(url_non_ascii) is True



```