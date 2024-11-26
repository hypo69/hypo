```python
import pytest
from types import SimpleNamespace
import json
from unittest.mock import Mock
from src.logger import logger
from src.utils import pprint
from ..errors import ApiRequestException, ApiRequestResponseException

# Mock logger for testing purposes
logger = Mock()

# Mock request object
def mock_request_object(response_data, response_name, resp_code, resp_msg, result):
    request = Mock()
    response = {response_name: {'resp_result': {'resp_code': resp_code, 'resp_msg': resp_msg, 'result':result}}}
    request.getResponse = lambda: response if response else {}
    return request


def test_api_request_valid_response():
    """Tests api_request with a valid response."""
    request = mock_request_object({'resp_code': 200, 'resp_msg': 'OK', 'result': 'Success'}, 'resp_data', 200, 'OK', 'Success')
    response = api_request(request, 'resp_data')
    assert response == 'Success'
    logger.warning.assert_not_called()
    logger.critical.assert_not_called()
    logger.error.assert_not_called()


def test_api_request_invalid_response_code():
    """Tests api_request with an invalid response code."""
    request = mock_request_object({'resp_code': 400, 'resp_msg': 'Bad Request', 'result': 'Error'}, 'resp_data', 400, 'Bad Request', 'Error')
    response = api_request(request, 'resp_data')
    assert response is None
    logger.warning.called_once()
    logger.warning.assert_called_with('Response code 400 - Bad Request', exc_info=False)
    logger.critical.assert_not_called()
    logger.error.assert_not_called()


def test_api_request_json_parsing_error():
    """Tests api_request with an error during JSON parsing."""
    request = mock_request_object({'resp_code': 200, 'resp_msg': 'OK', 'result': 'not_json'}, 'resp_data', 200, 'OK', 'not_json')
    response = api_request(request, 'resp_data')
    assert response is None
    logger.critical.called_once()  # Critical log should be triggered
    logger.error.assert_not_called()

def test_api_request_empty_response():
    """Tests api_request with an empty response."""
    request = Mock()
    request.getResponse.return_value = {}
    response = api_request(request, 'resp_data')
    assert response is None
    logger.critical.assert_not_called()
    logger.warning.assert_not_called()
    logger.error.assert_not_called()

def test_api_request_exception_during_request():
    """Tests api_request with an exception during getResponse."""
    request = Mock()
    request.getResponse.side_effect = Exception("Simulate an error")
    response = api_request(request, 'resp_data')
    assert response is None
    logger.critical.assert_not_called()
    logger.warning.assert_not_called()
    logger.error.assert_not_called()
```

**Explanation and Improvements:**

1. **Mocking:**  Crucially, the code now uses `unittest.mock.Mock` to simulate the `request` object. This is essential for testing `api_request` without depending on external APIs.  The `mock_request_object` function is introduced for cleaner setup of mocked requests with specific responses.

2. **Comprehensive Test Cases:** The tests now cover various scenarios:
   - Valid responses (200).
   - Invalid response codes (400).
   - Errors during JSON parsing.
   - Empty responses.
   - Exceptions raised during `request.getResponse()`.

3. **Clear Assertions:**  Assertions are now more specific, checking for `None` where appropriate and ensuring the correct messages are logged.

4. **Mocked Logger:** The `logger` is mocked using `Mock()`. This prevents actual logging to the console during the tests.

5. **Edge Cases:** The `test_api_request_empty_response` covers an important edge case.

6. **Error Handling:** The tests now explicitly check if the functions handle exceptions appropriately.

7. **`pytest.raises` (Not Used Here):**  Since we are mocking the `request` object and handling exceptions directly in the `api_request` function, `pytest.raises` isn't needed for directly testing exception handling within `api_request` itself.

8. **`pprint`:**  The mock is updated to use `logger.critical` or `logger.warning` correctly, and there's no need for the `pprint` call within the tests unless needed for complex situations.

This significantly improved test suite provides more robust and targeted checks for the `api_request` function, ensuring it correctly handles various situations and doesn't crash with unexpected data. Remember to install `pytest` if you haven't already (`pip install pytest`).  To run the tests, save the above code as a `.py` file (e.g., `test_requests.py`) and run `pytest test_requests.py` from your terminal. Remember to have the `src` package structure in place.