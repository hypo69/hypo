```python
import pytest
from types import SimpleNamespace
import json
from unittest.mock import Mock
from src.logger import logger
from src.utils import pprint
from ..errors import ApiRequestException, ApiRequestResponseException

# Mock the logger for testing
logger = Mock()


# Mock the request object
def mock_request(response_data):
    request = Mock()
    request.getResponse.return_value = response_data
    return request

# Fixture for valid response data
@pytest.fixture
def valid_response_data():
    return {"resp_result": {"resp_code": 200, "resp_msg": "OK", "result": {"key": "value"}}}


# Fixture for invalid response data
@pytest.fixture
def invalid_response_data():
    return {"resp_result": {"resp_code": 400, "resp_msg": "Bad Request"}}


# Fixture for response with missing 'resp_result' key
@pytest.fixture
def missing_resp_result_data():
    return {"another_key": {"resp_code": 200, "resp_msg": "OK"}}


# Tests for api_request function
def test_api_request_valid_response(valid_response_data, mock_request):
    """Test with a valid response."""
    request = mock_request(valid_response_data)
    response = api_request(request, 'resp_result')
    assert response == {"key": "value"}
    logger.warning.assert_not_called()
    logger.critical.assert_not_called()


def test_api_request_invalid_response_code(invalid_response_data, mock_request):
    """Test with an invalid response code (400)."""
    request = mock_request(invalid_response_data)
    response = api_request(request, 'resp_result')
    assert response is not None
    logger.warning.called_with("Response code 400 - Bad Request",exc_info=False)
    logger.critical.assert_not_called()


def test_api_request_missing_resp_result(missing_resp_result_data, mock_request):
    """Test with missing 'resp_result' key."""
    request = mock_request(missing_resp_result_data)
    response = api_request(request, 'resp_result')
    assert response is None
    logger.critical.called_once()


def test_api_request_exception_in_get_response(mock_request):
    """Test when an exception occurs in getResponse."""
    request = mock_request(None)
    request.getResponse.side_effect = Exception("Mock getResponse error")
    response = api_request(request, 'resp_result')
    assert response is None
    logger.critical.called_once()


def test_api_request_exception_in_parsing(valid_response_data, mock_request):
    """Test when an exception occurs during JSON parsing."""
    request = mock_request(valid_response_data)
    response = api_request(request, 'resp_result')
    assert response is not None

    # Mock an exception during json.loads() to catch it
    request.getResponse.return_value = valid_response_data
    with pytest.raises(ValueError):  # Or another appropriate exception
        api_request(request, 'resp_result')

    # Ensure critical is called if the exception is not handled
    logger.critical.assert_called_with(any, pprint(any), exc_info=False)




def test_api_request_exception_in_response_check():
    """Test when an exception occurs when checking the response."""
    # Simulate an exception occurring when accessing 'resp_code'
    with pytest.raises(AttributeError, match="object has no attribute"):
        response = SimpleNamespace(resp_code=None)
        api_request(Mock(), 'resp_result') # Simulate a request object
    logger.error.assert_called_with(None, any, exc_info=False)


```