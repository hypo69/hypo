```python
import pytest
import json
import time

# Mock functions for testing
def mock_chrome_tabs_sendMessage(tab_id, message):
    pass

def mock_chrome_storage_local_get(key, callback):
    data = {'collectedData': {'key': 'value'}}
    callback(data)

def mock_fetch(url, options):
    return None

# Mock sendDataToServer function
def mock_sendDataToServer(url):
    global call_count_mock
    call_count_mock += 1
    return

def test_collectData_valid_input():
    """Tests the 'collectData' action with a valid URL."""
    global call_count_mock
    call_count_mock = 0
    mock_chrome_tabs_sendMessage = lambda tab_id, message: None
    # Mocking the fetch function for testing
    mock_fetch = lambda url, options: None
    mock_sendDataToServer = mock_sendDataToServer

    message = {'action': 'collectData', 'url': 'https://www.example.com'}
    # Mock the chrome.storage.local.get call for testing
    mock_chrome_storage_local_get = lambda key, callback: callback({'collectedData': {'key': 'value'}})
    chrome.tabs.sendMessage = mock_chrome_tabs_sendMessage

    # Replace the actual functions with the mocks
    chrome.runtime.onMessage.addListener(
        lambda message, sender, sendResponse: mock_sendDataToServer(message['url'])
    )
    chrome.storage.local.get = mock_chrome_storage_local_get
    chrome.tabs.sendMessage = mock_chrome_tabs_sendMessage
    chrome.fetch = mock_fetch


    # Call the function to be tested
    chrome.action.onClicked.addListener(
        lambda tab: chrome.tabs.sendMessage(tab.id, message)
    )
    assert call_count_mock == 1


def test_collectData_invalid_url():
    """Tests handling of invalid URLs."""
    global call_count_mock
    call_count_mock = 0
    #Mock functions for testing
    chrome.tabs.sendMessage = lambda tab_id, message: None
    message = {'action': 'collectData', 'url': None} # Invalid URL
    chrome.runtime.onMessage.addListener(
        lambda message, sender, sendResponse: mock_sendDataToServer(message['url'])
    )

    # Call the function to be tested
    with pytest.raises(TypeError):
        chrome.action.onClicked.addListener(
            lambda tab: chrome.tabs.sendMessage(tab.id, message)
        )



def test_collectData_no_data():
    """Tests handling when no collected data is found."""
    global call_count_mock
    call_count_mock = 0

    message = {'action': 'collectData', 'url': 'https://www.example.com'}
    # Mock the chrome.storage.local.get call to return empty data
    mock_chrome_storage_local_get = lambda key, callback: callback({'collectedData': None})
    chrome.storage.local.get = mock_chrome_storage_local_get
    chrome.runtime.onMessage.addListener(
        lambda message, sender, sendResponse: mock_sendDataToServer(message['url'])
    )

    chrome.action.onClicked.addListener(
        lambda tab: chrome.tabs.sendMessage(tab.id, message)
    )
    assert call_count_mock == 1 # Ensure sendDataToServer was called

# Replace 'chrome' with your actual chrome module
#   Import necessary modules

import chrome # or whatever module you're using


```

**Explanation and Improvements:**

1. **Mock Functions:** The code now uses mock functions (`mock_chrome_tabs_sendMessage`, `mock_chrome_storage_local_get`, `mock_fetch`, `mock_sendDataToServer`) to isolate the tests from the actual browser API.  This is crucial for unit testing.  Importantly, we mock `fetch` to avoid network interactions.

2. **Clearer Test Cases:** The test cases are more descriptive about the scenarios being tested (valid input, invalid URL).

3. **Error Handling:**  The `test_collectData_invalid_url` test now demonStartes how to use `pytest.raises` to check for exceptions when the input is invalid.

4. **Global Variables:** Using global variables like `call_count_mock` in tests is generally discouraged. However, for the sake of brevity and since the context is about testing a browser extension, and using the Chrome API, I use them, acknowledging this is not ideal.  In a real application, you would typically use a proper testing setup with classes and methods.


5. **`chrome` Module:** The tests now include a placeholder `import chrome`. You need to replace this with the actual import statement for your Chrome extension API if it's different.

6. **Missing `chrome` module:**  Critically, you need to `import chrome` somewhere. If you don't have a test-friendly mock for the `chrome` module, you cannot run these tests.  Consider how to mock the Chrome API for the test environment.


**To Run These Tests:**

1. **Install pytest:**
   ```bash
   pip install pytest
   ```

2. **Replace `import chrome`:** With the correct import for your browser extension's API.  **Crucially**, you need mocks for these functions.

3. **Run the tests:**
   ```bash
   pytest your_test_file.py
   ```

Remember to adapt the test cases based on the specific behavior and structure of your `background.js` file and the Chrome extension API you're using.  The use of mock functions is essential for effective unit testing in browser extensions.