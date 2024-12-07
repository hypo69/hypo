```python
import pytest
import requests
from unittest.mock import patch

from hypotez.src.check_release import check_latest_release


# Mock the requests library
@pytest.fixture
def mock_response(monkeypatch):
    def mock_get(url):
        return mock_response_obj
    monkeypatch.setattr(requests, 'get', mock_get)
    return mock_response_obj

@pytest.fixture
def mock_response_obj():
    return requests.Response()


# Tests for check_latest_release
def test_check_latest_release_success(mock_response):
    """Tests successful retrieval of the latest release."""
    mock_response.status_code = 200
    mock_response.json.return_value = {"tag_name": "v1.0.0"}
    result = check_latest_release("owner", "repo")
    assert result == "v1.0.0"


def test_check_latest_release_failed_status_code(mock_response):
    """Tests handling of non-200 status codes (error)."""
    mock_response.status_code = 404
    result = check_latest_release("owner", "repo")
    assert result is None


def test_check_latest_release_empty_response(mock_response):
    """Tests if the function returns None with an empty json response"""
    mock_response.status_code = 200
    mock_response.json.return_value = {}
    result = check_latest_release("owner", "repo")
    assert result is None

@patch('hypotez.src.check_release.logger')
def test_check_latest_release_exception(mock_logger, mock_response):
    """Tests exception handling (e.g., invalid JSON)."""
    mock_response.status_code = 200
    mock_response.json.side_effect = ValueError("Invalid JSON")

    with pytest.raises(ValueError):
        check_latest_release("owner", "repo")
    mock_logger.error.assert_called_once()  #Check if error logging is called
    

def test_check_latest_release_invalid_url():
    """Tests behavior with an invalid URL."""
    with pytest.raises(requests.exceptions.RequestException):
      check_latest_release("owner", "repo")

def test_check_latest_release_invalid_input_owner(mock_response):
    """Tests handling invalid owner input (string, not empty)."""
    mock_response.status_code = 200
    mock_response.json.return_value = {"tag_name": "v1.0.0"}
    result = check_latest_release(None, "repo")
    assert result is None


def test_check_latest_release_invalid_input_repo(mock_response):
    """Tests handling invalid repo input (string, not empty)."""
    mock_response.status_code = 200
    mock_response.json.return_value = {"tag_name": "v1.0.0"}
    result = check_latest_release("owner", None)
    assert result is None

# Edge cases: empty strings, None values for owner/repo, and ensure no exceptions
# are raised in these cases.

# Test for missing required arguments in function call
def test_check_latest_release_missing_arguments():
    with pytest.raises(TypeError):
        check_latest_release("owner")
```