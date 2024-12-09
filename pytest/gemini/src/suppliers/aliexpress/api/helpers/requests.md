```python
import pytest
from types import SimpleNamespace
import json
from unittest.mock import Mock, patch
from src.logger import logger
from src.utils.printer import pprint
from ..errors import ApiRequestException, ApiRequestResponseException


# Mock objects for testing
class MockRequest:
    def __init__(self, response_data=None):
        self.response_data = response_data

    def getResponse(self):
        if self.response_data:
            return self.response_data
        else:
            raise Exception("No response data")


@pytest.fixture
def mock_request_success():
    response_data = {"response_name": {"resp_result": {"resp_code": 200, "result": "success", "resp_msg": "OK"}}}
    return MockRequest(response_data)


@pytest.fixture
def mock_request_failure():
    response_data = {"response_name": {"resp_result": {"resp_code": 400, "result": "error", "resp_msg": "Bad Request"}}}
    return MockRequest(response_data)


@pytest.fixture
def mock_request_invalid_response_format():
    response_data = {"response_name": {"resp_result": "invalid json"}}
    return MockRequest(response_data)


@pytest.fixture
def mock_request_no_response():
    return MockRequest()


@patch('src.logger.logger')
def test_api_request_success(mock_logger, mock_request_success):
    """Tests api_request with a successful response."""
    response = api_request(mock_request_success, "response_name")
    assert response == "success"
    mock_logger.warning.assert_not_called()
    mock_logger.critical.assert_not_called()
    mock_logger.error.assert_not_called()



@patch('src.logger.logger')
def test_api_request_failure(mock_logger, mock_request_failure):
    """Tests api_request with a failed response (non-200 status)."""
    response = api_request(mock_request_failure, "response_name")
    assert response == None
    mock_logger.warning.called_once_with("Response code 400 - Bad Request", exc_info=False)
    mock_logger.critical.assert_not_called()
    mock_logger.error.assert_not_called()


@patch('src.logger.logger')
def test_api_request_invalid_response_format(mock_logger, mock_request_invalid_response_format):
    """Tests api_request with invalid JSON response format."""
    response = api_request(mock_request_invalid_response_format, "response_name")
    assert response == None
    mock_logger.critical.called_once()
    mock_logger.warning.assert_not_called()
    mock_logger.error.assert_not_called()


@patch('src.logger.logger')
def test_api_request_no_response(mock_logger, mock_request_no_response):
    """Tests api_request with no response (exception during getResponse)."""
    with pytest.raises(Exception):
        api_request(mock_request_no_response, "response_name")
    mock_logger.critical.assert_not_called()
    mock_logger.warning.assert_not_called()
    mock_logger.error.assert_not_called()

```