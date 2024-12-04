```python
import pytest
from urllib.parse import urlparse, parse_qs
import validators
from hypotez.src.utils.string.url import extract_url_params, is_url

# Fixtures (if needed)


@pytest.fixture
def valid_url():
    return "https://example.com?param1=value1&param2=value2&param3="


@pytest.fixture
def valid_url_single_value():
    return "https://example.com?param1=value1"


@pytest.fixture
def invalid_url():
    return "invalid-url"


@pytest.fixture
def url_with_no_params():
    return "https://example.com"

# Tests for extract_url_params
def test_extract_url_params_valid(valid_url):
    """Tests extract_url_params with a valid URL containing multiple parameters."""
    expected_params = {"param1": "value1", "param2": "value2", "param3": ""}
    actual_params = extract_url_params(valid_url)
    assert actual_params == expected_params


def test_extract_url_params_single_value(valid_url_single_value):
    """Tests extract_url_params with a valid URL containing a single value parameter."""
    expected_params = {"param1": "value1"}
    actual_params = extract_url_params(valid_url_single_value)
    assert actual_params == expected_params


def test_extract_url_params_no_params(url_with_no_params):
    """Tests extract_url_params with a valid URL containing no parameters."""
    actual_params = extract_url_params(url_with_no_params)
    assert actual_params is None


def test_extract_url_params_invalid_url(invalid_url):
    """Tests extract_url_params with an invalid URL."""
    actual_params = extract_url_params(invalid_url)
    assert actual_params is None



# Tests for is_url
def test_is_url_valid(valid_url):
    """Tests is_url with a valid URL."""
    assert is_url(valid_url) is True


def test_is_url_invalid(invalid_url):
    """Tests is_url with an invalid URL."""
    assert is_url(invalid_url) is False


def test_is_url_empty_string():
    """Tests is_url with an empty string."""
    assert is_url("") is False


def test_is_url_no_protocol():
    """Tests is_url with a URL missing a protocol."""
    assert is_url("example.com") is False


def test_is_url_with_special_characters():
    """Tests is_url with a URL containing special characters."""
    assert is_url("https://example.com/path?query=special;characters") is True

# Example test for potential exception handling (if any):
# def test_extract_url_params_malformed_url():
#     """Tests extract_url_params with malformed URL (edge case)."""
#     malformed_url = "https://example.com?param1=value1&param2"
#     with pytest.raises(ValueError):  # Replace with appropriate exception type
#         extract_url_params(malformed_url)
```