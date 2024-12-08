```python
import pytest
import json
import requests
from unittest.mock import patch

# Mock the fetch function for testing
@patch('requests.post')
def test_sendDataToServer_valid_input(mock_post):
    """Tests sendDataToServer with valid input and successful server response."""
    test_url = "https://example.com"
    test_data = {"key": "value"}
    
    # Mock the chrome.storage.local.get response
    mock_get_result = {"collectedData": test_data}
    mock_storage = {'get': lambda key, callback: callback(mock_get_result)}
    
    # Mock the fetch call
    mock_post.return_value.ok = True
    mock_post.return_value.json.return_value = {}  # Placeholder for actual response
    
    with patch('chrome.storage.local', mock_storage):
        from webdriver.chrome.extentions.test_extention.background import sendDataToServer
        sendDataToServer(test_url)

    # Assertions for the mock
    mock_post.assert_called_once_with(
        'http://127.0.0.1/hypotez.online/api/',
        data=json.dumps(test_data),
        headers={'Content-Type': 'application/json'}
    )


@patch('requests.post')
def test_sendDataToServer_no_collected_data(mock_post):
    """Tests sendDataToServer when no collected data is found."""
    test_url = "https://example.com"

    mock_get_result = {"collectedData": None}
    mock_storage = {'get': lambda key, callback: callback(mock_get_result)}
    
    with patch('chrome.storage.local', mock_storage):
        from webdriver.chrome.extentions.test_extention.background import sendDataToServer
        sendDataToServer(test_url)
        
    mock_post.assert_not_called()


@patch('requests.post')
def test_sendDataToServer_server_error(mock_post):
    """Tests sendDataToServer when the server returns an error."""
    test_url = "https://example.com"
    test_data = {"key": "value"}
    
    mock_get_result = {"collectedData": test_data}
    mock_storage = {'get': lambda key, callback: callback(mock_get_result)}
    mock_post.return_value.ok = False  # Simulate an error response

    with patch('chrome.storage.local', mock_storage):
        from webdriver.chrome.extentions.test_extention.background import sendDataToServer

        with pytest.raises(Exception) as excinfo:
            sendDataToServer(test_url)
            
        assert 'Failed to send data to server' in str(excinfo.value)

    # Assertions for the mock to ensure it was called
    mock_post.assert_called_once_with(
        'http://127.0.0.1/hypotez.online/api/',
        data=json.dumps(test_data),
        headers={'Content-Type': 'application/json'}
    )

```

**Explanation and Improvements:**

1. **Mocking `requests.post`:**  Crucially, the code now uses `@patch('requests.post')` to mock the `requests.post` function.  This is essential for unit testing because `fetch` interacts with an external resource (the server).  This isolates the background.js function from the external API call, making the tests reliable.

2. **Mocking `chrome.storage.local`:** The tests now mock `chrome.storage.local.get` to control the data provided to `sendDataToServer`. This is essential to isolate the test from the actual storage mechanism.

3. **Clearer Assertions:**  The assertions now explicitly check if `requests.post` was called with the correct URL, data, and headers, ensuring all parameters are validated.

4. **Error Handling Test:** The `test_sendDataToServer_server_error` now effectively tests the error handling.  It uses `pytest.raises` to verify that the expected exception (`Exception`) is raised when the server returns an error. This is vital to ensure the code gracefully handles failure cases.

5. **`no_collected_data` test:** Added a test to handle the case where there's no `collectedData` in storage.

6. **Import `json`:** Added `import json` for handling JSON data properly.

7. **Import `requests`:** Added `import requests` to use the `requests` library.

8. **Explicit `from` statements:** Added `from` statements to clearly indicate the module from which the function is imported.

9. **Placeholder for Actual Response:** The mock now includes a placeholder for a real response (`mock_post.return_value.json.return_value = {}`) to be more realistic.

These improvements make the tests more comprehensive, robust, and accurately reflect the behavior of the `sendDataToServer` function in different scenarios. Remember to install the necessary libraries: `pytest`, `requests`, and `unittest.mock`.


**To Run the Tests:**

1.  Save the test code as a `.py` file (e.g., `test_background.py`).
2.  Ensure you have the `webdriver/chrome/extentions/test_extention/background.js` file in your project.
3.  Run the tests from your terminal using: `pytest test_background.py`