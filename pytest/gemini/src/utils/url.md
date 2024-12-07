```python
import pytest
from urllib.parse import urlparse, parse_qs
import validators
from hypotez.src.utils.string.url import extract_url_params, is_url


def test_extract_url_params_valid_url_with_params():
    """Checks extract_url_params with a valid URL containing parameters."""
    url = "https://example.com?param1=value1&param2=value2&param3="
    expected_params = {"param1": "value1", "param2": "value2", "param3": ""}
    result = extract_url_params(url)
    assert result == expected_params


def test_extract_url_params_valid_url_with_single_value_param():
    """Checks extract_url_params with a valid URL containing a single-valued parameter."""
    url = "https://example.com?param1=value1"
    expected_params = {"param1": "value1"}
    result = extract_url_params(url)
    assert result == expected_params


def test_extract_url_params_valid_url_no_params():
    """Checks extract_url_params with a valid URL without parameters."""
    url = "https://example.com"
    result = extract_url_params(url)
    assert result is None


def test_extract_url_params_invalid_url():
    """Checks extract_url_params with an invalid URL."""
    url = "invalid_url"
    result = extract_url_params(url)
    assert result is None


def test_is_url_valid_url():
    """Checks is_url with a valid URL."""
    url = "https://www.example.com"
    assert is_url(url) is True


def test_is_url_invalid_url():
    """Checks is_url with an invalid URL."""
    url = "invalid-url"
    assert is_url(url) is False


def test_is_url_empty_string():
    """Checks is_url with an empty string."""
    url = ""
    assert is_url(url) is False


def test_is_url_with_special_characters():
    """Checks is_url with a URL containing special characters."""
    url = "https://example.com/path?query=special+characters"
    assert is_url(url) is True


# Test for edge case handling with query parameters containing multiple values.
def test_extract_url_params_multiple_values():
  url = "https://example.com?param1=value1&param1=value2&param2="
  expected_params = {"param1": ["value1", "value2"], "param2": []}
  result = extract_url_params(url)
  #Check if the parsing correctly returns a list for repeated parameters.
  assert result == {"param1": ["value1", "value2"], "param2": []}


# Test with a URL that contains non-standard characters in the query.
def test_extract_url_params_non_standard_characters():
    url = "https://example.com?param1=value1&param2=value%20with%20spaces"
    result = extract_url_params(url)
    assert result["param1"] == "value1"
    assert result["param2"] == "value with spaces"

```