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

def test_extract_url_params_valid_url_with_single_value_param():
    """Checks extraction of parameter with single value."""
    url = "https://example.com?param1=value1"
    expected_params = {"param1": "value1"}
    actual_params = extract_url_params(url)
    assert actual_params == expected_params

def test_extract_url_params_valid_url_no_params():
    """Checks handling of a valid URL without parameters."""
    url = "https://example.com"
    assert extract_url_params(url) is None


def test_extract_url_params_invalid_url():
    """Checks handling of an invalid URL."""
    url = "invalid_url"
    assert extract_url_params(url) is None

def test_is_url_valid_url():
    """Checks if a valid URL is correctly identified."""
    url = "https://www.example.com"
    assert is_url(url) is True

def test_is_url_invalid_url():
    """Checks if an invalid URL is correctly identified."""
    invalid_url = "invalid-url"
    assert is_url(invalid_url) is False
    
def test_is_url_empty_string():
    """Checks if an empty string is considered as an invalid URL."""
    empty_string = ""
    assert is_url(empty_string) is False
    
def test_is_url_with_special_characters():
    """Checks if a URL with special characters is considered a valid URL."""
    url_with_special_char = "https://example.com/path?param=value#fragment"
    assert is_url(url_with_special_char) is True
    
def test_is_url_with_non_standard_scheme():
    """Checks if a URL with a non-standard scheme (e.g., ftp) is considered a valid URL."""
    url_non_standard_scheme = "ftp://example.com"
    assert is_url(url_non_standard_scheme) is True


def test_is_url_with_malformed_url():
  """Tests is_url with a malformed URL that doesn't violate RFCs (e.g., missing parts)."""
  malformed_url = "http:://example.com"
  assert is_url(malformed_url) is False

def test_extract_url_params_with_empty_query_string():
  """Tests extract_url_params with an empty query string."""
  url = "https://example.com?"
  assert extract_url_params(url) is None


# Example usage of fixtures (if needed)
# @pytest.fixture
# def example_data():
#     return {"key1": "value1", "key2": "value2"}

# def test_function_using_fixture(example_data):
#     # Use example_data in your test
#     assert example_data["key1"] == "value1"
```