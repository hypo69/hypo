```python
import pytest
from unittest.mock import MagicMock
from types import SimpleNamespace
import json
from src.suppliers.aliexpress.api.helpers.requests import api_request
from src.suppliers.aliexpress.api.errors import ApiRequestException, ApiRequestResponseException
from src.logger.logger import logger

# Fixture for a successful response
@pytest.fixture
def mock_successful_request():
    mock_request = MagicMock()
    mock_request.getResponse.return_value = {
        "response_name": {
            "resp_result": {
                "resp_code": 200,
                "resp_msg": "Success",
                "result": {"key": "value"}
            }
        }
    }
    return mock_request

# Fixture for a failed response
@pytest.fixture
def mock_failed_request():
    mock_request = MagicMock()
    mock_request.getResponse.return_value = {
        "response_name": {
            "resp_result": {
                "resp_code": 500,
                "resp_msg": "Internal Server Error",
            }
        }
    }
    return mock_request

# Fixture for a request that raises an exception during getResponse
@pytest.fixture
def mock_exception_request():
    mock_request = MagicMock()
    mock_request.getResponse.side_effect = Exception("Request failed")
    return mock_request

# Fixture for a response missing resp_result
@pytest.fixture
def mock_missing_resp_result_request():
    mock_request = MagicMock()
    mock_request.getResponse.return_value = {
        "response_name": {}
    }
    return mock_request

# Fixture for a response with no resp_code
@pytest.fixture
def mock_missing_resp_code_request():
    mock_request = MagicMock()
    mock_request.getResponse.return_value = {
        "response_name": {
            "resp_result": {
                "resp_msg": "Missing code"
            }
        }
    }
    return mock_request



def test_api_request_successful(mock_successful_request):
    """
    Test successful API request with a valid response.
    """
    result = api_request(mock_successful_request, "response_name")
    assert result == {"key": "value"}

def test_api_request_failed_response(mock_failed_request):
    """
    Test API request with a failed response (non-200 status code).
    """
    result = api_request(mock_failed_request, "response_name")
    assert result is None


def test_api_request_exception_during_request(mock_exception_request):
    """
    Test API request when an exception occurs during the initial request.
    """
    result = api_request(mock_exception_request, "response_name")
    assert result is None

def test_api_request_missing_resp_result(mock_missing_resp_result_request):
    """
    Test API request when the response is missing the 'resp_result'.
    """
    result = api_request(mock_missing_resp_result_request, "response_name")
    assert result is None

def test_api_request_missing_resp_code(mock_missing_resp_code_request):
    """
    Test API request when the response is missing the 'resp_code'.
    """
    result = api_request(mock_missing_resp_code_request, "response_name")
    assert result is None


def test_api_request_with_attemps():
    """
    Test API request with a specified number of attempts.
    This test will just check that it doesn't crash.
    """
    mock_request = MagicMock()
    mock_request.getResponse.return_value = {
        "response_name": {
            "resp_result": {
                "resp_code": 200,
                "resp_msg": "Success",
                "result": {"key": "value"}
            }
        }
    }
    result = api_request(mock_request, "response_name", attemps=3)
    assert result == {"key": "value"}

def test_api_request_with_invalid_json_response():
    """
    Test API request when response contains invalid json.
    """
    mock_request = MagicMock()
    mock_request.getResponse.return_value = {
        "response_name": {
            "resp_result": "invalid json"
        }
    }
    result = api_request(mock_request, "response_name")
    assert result is None
```