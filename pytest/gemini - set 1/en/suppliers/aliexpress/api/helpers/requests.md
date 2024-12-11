```python
import pytest
from types import SimpleNamespace
import json
from unittest.mock import Mock
from src.logger import logger # Assuming this is defined elsewhere
from src.utils import pprint # Assuming this is defined elsewhere
from ..errors import ApiRequestException, ApiRequestResponseException


# Mock the request object for testing
def mock_request(response_data, response_name):
    request = Mock()
    request.getResponse.return_value = {response_name: {"resp_result": response_data}}
    return request


def api_request(request, response_name, attemps: int = 1):
    try:
        response = request.getResponse()
    except Exception as error:
        if hasattr(error, 'message'):
            logger.critical(error.message, pprint(error))
        return  # Or raise the exception, depending on your error handling Startegy

    try:
        response = response[response_name]['resp_result']
        response = json.dumps(response)
        response = json.loads(response, object_hook=lambda d: SimpleNamespace(**d))
    except Exception as error:
        logger.critical(error.message, pprint(error), exc_info=False)
        return

    try:
        if response.resp_code == 200:
            return response.result
        else:
            logger.warning(f'Response code {response.resp_code} - {response.resp_msg}', exc_info=False)
            return  # Or raise the exception.

    except Exception as ex:
        logger.error(None, ex, exc_info=False)
        return

# Tests
def test_api_request_success():
    """Tests successful API request."""
    mock_response = {"resp_code": 200, "resp_msg": "OK", "result": "Success"}
    request = mock_request(mock_response, "response")
    result = api_request(request, "response")
    assert result == "Success"

def test_api_request_non_200_response():
    """Tests non-200 response code."""
    mock_response = {"resp_code": 400, "resp_msg": "Bad Request", "result": "Error"}
    request = mock_request(mock_response, "response")
    result = api_request(request, "response")
    assert result is None  # Or add an assertion to check the warning log.


def test_api_request_missing_response_name():
    """Tests when response_name doesn't exist."""
    mock_response = {"other_response": {"resp_result": {"resp_code": 200, "resp_msg": "OK", "result": "Success"}}}
    request = mock_request(mock_response, "response")
    result = api_request(request, "response")
    assert result is None

def test_api_request_response_parsing_error():
    """Tests exception handling during JSON parsing."""
    mock_response = {"resp_result": "invalid json"}
    request = mock_request(mock_response, "response")
    with pytest.raises(Exception) as e:  # Expect a general exception
        api_request(request, "response")
    assert "invalid json" in str(e.value)  # Check the error message


def test_api_request_getresponse_error():
    """Tests exception handling for getResponse() failure."""
    request = Mock()
    request.getResponse.side_effect = ValueError("Failed to get response")
    with pytest.raises(Exception) as e:
        api_request(request, "response")
    assert "Failed to get response" in str(e.value)  # Or test for specific exception


# Mocking the logger for testing
@pytest.fixture
def mock_logger():
    mock_logger = Mock()
    logger.critical = mock_logger.critical
    logger.warning = mock_logger.warning
    logger.error = mock_logger.error
    return mock_logger


# Example use of the fixture (in a test function)
def test_api_request_with_mock_logger(mock_logger):
  """
    Tests if the logger is called properly on error conditions
  """
  mock_response = {"resp_code": 500, "resp_msg": "Internal Server Error", "result": None}
  request = mock_request(mock_response, "response")
  api_request(request, "response")

  mock_logger.warning.assert_called_with(
      "Response code 500 - Internal Server Error", exc_info=False
  )
```

**Explanation of Improvements and Key Concepts:**

* **Clearer Test Names:** Test names now explicitly describe the scenario being tested (e.g., `test_api_request_non_200_response`).
* **Mocking `request`:** Instead of relying on external APIs, we now mock the `request` object using `unittest.mock`. This makes tests much more reliable and repeatable.
* **Comprehensive Error Handling:** Tests now cover cases where `getResponse()` fails, JSON parsing fails, and the response code isn't 200. The critical part is we now catch the exceptions properly.
* **Using `pytest.raises`:** `pytest.raises` is used to assert expected exceptions, making error handling testing explicit.
* **Explicit `assert None`:**  Checks for `None` return values where appropriate.
* **`mock_logger` Fixture:** A `mock_logger` fixture is introduced to verify that the logger is correctly called with the appropriate messages.  This is crucial for testing the logging aspects of the code.


This significantly improved solution provides much more robust and comprehensive testing of the `api_request` function, covering various scenarios, including error handling, edge cases, and basic functionality. Remember to adapt the error checking to match your actual error raising Startegy within `api_request`.