```python
import pytest
import json
import os
from unittest.mock import patch

# Mock the chrome API functions
def mock_chrome_tabs_sendMessage(tab_id, message):
    pass

def mock_chrome_storage_local_get(key, callback):
    collected_data = {"data": "test_data"}
    callback({"collectedData": collected_data})

def mock_fetch(url, payload):
    return mock_response(200)

def mock_response(status_code):
    response = {"ok": status_code == 200}
    return type('Response', (), {'ok': response['ok'], 'json': lambda: {} })

@patch('__main__.chrome.tabs.sendMessage', side_effect=mock_chrome_tabs_sendMessage)
@patch('__main__.chrome.storage.local.get', side_effect=mock_chrome_storage_local_get)
@patch('__main__.fetch', side_effect=mock_fetch)
def test_sendDataToServer_valid_input(mock_fetch, mock_storage, mock_send_message):
    """Test sendDataToServer with valid input."""
    url = 'https://example.com'
    __main__.sendDataToServer(url)
    mock_fetch.assert_called_with('http://127.0.0.1/hypotez.online/api/', None)

@patch('__main__.chrome.tabs.sendMessage', side_effect=mock_chrome_tabs_sendMessage)
@patch('__main__.chrome.storage.local.get')
@patch('__main__.fetch')
def test_sendDataToServer_no_collected_data(mock_fetch, mock_storage, mock_send_message):
    """Test sendDataToServer with no collected data."""
    mock_storage.return_value = {}
    url = 'https://example.com'
    __main__.sendDataToServer(url)
    mock_fetch.assert_not_called()
    mock_storage.assert_called_with('collectedData')


@patch('__main__.chrome.tabs.sendMessage', side_effect=mock_chrome_tabs_sendMessage)
@patch('__main__.chrome.storage.local.get')
@patch('__main__.fetch', side_effect=mock_fetch)
def test_sendDataToServer_fetch_error(mock_fetch, mock_storage, mock_send_message):
    """Test sendDataToServer with fetch error."""
    mock_fetch.side_effect = Exception("Fetch error")
    mock_storage.return_value = {"collectedData": {"data": "test_data"}}
    url = 'https://example.com'
    with pytest.raises(Exception) as excinfo:
        __main__.sendDataToServer(url)
    assert "Failed to send data to server" in str(excinfo.value)


@patch('__main__.chrome.tabs.sendMessage', side_effect=mock_chrome_tabs_sendMessage)
@patch('__main__.chrome.storage.local.get', side_effect=mock_chrome_storage_local_get)
@patch('__main__.fetch', side_effect=mock_response(404))
def test_sendDataToServer_fetch_error_status_404(mock_fetch, mock_storage, mock_send_message):
  """
  Test sendDataToServer with a fetch error (status code 404).
  """
  url = 'https://example.com'
  with pytest.raises(Exception) as excinfo:
      __main__.sendDataToServer(url)
  assert "Failed to send data to server" in str(excinfo.value)


```

**Explanation and Improvements:**

1. **Mocking:** The code now heavily uses `unittest.mock.patch` to mock the `chrome` API functions (`chrome.tabs.sendMessage`, `chrome.storage.local.get`, `fetch`). This is crucial for testing functions that interact with external resources (like the browser API) without needing a real browser.

2. **Comprehensive Test Cases:** The tests cover valid inputs, cases where `collectedData` is missing, and a fetch error scenario.

3. **Exception Handling:**  `pytest.raises` is used correctly to assert that the expected exception is raised in the `sendDataToServer_fetch_error` test. Also added a test for a non-200 status code (404).

4. **Clearer Test Names:** Test names are more descriptive (e.g., `test_sendDataToServer_valid_input`, `test_sendDataToServer_no_collected_data`).

5. **Data Setup:** Mocking `chrome.storage.local.get` ensures that the data is correctly passed to `sendDataToServer` to make the tests more robust and less reliant on external factors.

6. **Side Effects:** The `side_effect` parameter is used to return mock objects or raise exceptions during the `fetch` call, making the test cases independent of real network requests.

7. **Error Handling:** The test now properly handles the `fetch` error and checks for the specific error message within the exception.


**How to Run the Tests:**

1.  Save the test code as a Python file (e.g., `test_background.py`).
2.  Make sure you have `pytest` installed (`pip install pytest`).
3.  Run the tests from your terminal: `pytest test_background.py`


**Important Considerations:**

- **Real API Calls:** The provided tests now mock all interaction with the Chrome API and simulate a response. In a real-world scenario, if you need to test against a real server, you would need to properly mock or integrate a server.
- **`__main__`:**  The `__main__` is crucial when patching functions from the actual file.


This revised solution is more robust and provides a better testing Startegy for the `background.js` code. Remember to adapt the mock functions to the specifics of your Chrome API calls if they are different.  The examples provided are a good starting point but consider any specific error handling the server might require.