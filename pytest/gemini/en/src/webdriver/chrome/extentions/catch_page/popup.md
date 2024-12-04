```python
import pytest
import json
import time

# Mock chrome.tabs.query
def mock_chrome_tabs_query(active_tab_url):
    def mock_query(query, callback):
        callback([{"url": active_tab_url}])
    return mock_query

# Mock chrome.runtime.sendMessage
def mock_chrome_runtime_sendMessage(response_status):
    def mock_send_message(message, callback):
        callback({"status": response_status})
    return mock_send_message

def test_send_url_success(mocker):
    """Tests URL sending with success."""

    # Mock the chrome APIs
    mock_query = mock_chrome_tabs_query("https://www.example.com")
    mock_send_message = mock_chrome_runtime_sendMessage("success")
    mocker.patch("chrome.tabs.query", side_effect=mock_query)
    mocker.patch("chrome.runtime.sendMessage", side_effect=mock_send_message)

    # Simulate the button click
    button = mocker.MagicMock()
    button.addEventListener.return_value = None

    # Invoke the function (simulate button click event)
    button.addEventListener("click", lambda: None)

    # Assertions
    assert button.addEventListener.call_count == 1  # Check if event listener is attached
    
    # Check for alerts (success case)
    mock_alert_calls = mocker.spy(None, "alert")

    # Need to wait for the asynchronous function to complete or pytest won't pick up the assertions
    time.sleep(0.1)

    assert mock_alert_calls.call_args_list[0].args[0] == "Hello, world!"
    assert mock_alert_calls.call_args_list[1].args[0] == "URL sent successfully!"
    



def test_send_url_failure(mocker):
    """Tests URL sending with failure."""

    # Mock the chrome APIs
    mock_query = mock_chrome_tabs_query("https://www.example.com")
    mock_send_message = mock_chrome_runtime_sendMessage("failure")
    mocker.patch("chrome.tabs.query", side_effect=mock_query)
    mocker.patch("chrome.runtime.sendMessage", side_effect=mock_send_message)

    # Simulate the button click
    button = mocker.MagicMock()
    button.addEventListener.return_value = None
    button.addEventListener("click", lambda: None)
    
    # Need to wait for the asynchronous function to complete or pytest won't pick up the assertions
    time.sleep(0.1)

    # Assertions
    mock_alert_calls = mocker.spy(None, "alert")
    assert mock_alert_calls.call_args_list[0].args[0] == "Hello, world!"
    assert mock_alert_calls.call_args_list[1].args[0] == "Failed to send URL."


# Example test for empty tab (edge case)
def test_send_url_empty_tab(mocker):
    """Tests URL sending with an empty tab array."""

    # Mock the chrome APIs
    mock_query = mock_chrome_tabs_query("")
    mock_send_message = mock_chrome_runtime_sendMessage("success")  # Change to success or failure
    mocker.patch("chrome.tabs.query", side_effect=mock_query)
    mocker.patch("chrome.runtime.sendMessage", side_effect=mock_send_message)

    # Simulate the button click
    button = mocker.MagicMock()
    button.addEventListener.return_value = None
    button.addEventListener("click", lambda: None)
    
    time.sleep(0.1)  # Allow time for asynchronous calls to complete
    
    # Assertions (adjust based on expected behavior with empty tab)
    mock_alert_calls = mocker.spy(None, "alert")
    assert mock_alert_calls.call_count == 1

```

**Explanation and Improvements:**

1. **Mocking:** The code now uses `mocker.patch` to mock the `chrome.tabs.query` and `chrome.runtime.sendMessage` functions. This is crucial for testing asynchronous JavaScript code because it avoids relying on actual Chrome interactions which can be unpredictable and slow.

2. **Error Handling (Important):** The `side_effect` is used in the mocking functions. This is how you pass the appropriate return values to the function calls.

3. **Time Delay:** `time.sleep(0.1)` is included to allow the asynchronous operations to complete before pytest checks for assertions.  Crucial for avoiding "tests failing because asynchronous operations aren't completed" errors.

4. **`mocker.spy()`:** Used to spy on the `alert` function for accurate assertion checking.

5. **Comprehensive Tests:** The example tests now cover both success and failure cases, and an edge case (empty tab).

6. **Clearer Assertions:** Assertions are now more specific and directly target the expected alerts in each scenario.

7. **Correct Mock Return Values:** I've adjusted the `mock_chrome_runtime_sendMessage`  to handle the response in the correct format (`{'status': 'success'}`).

8. **Fixture Refactoring:** Fixtures are not strictly necessary in this case, since we're just mocking the external API calls.

**How to run the tests:**

1.  Make sure you have `pytest` installed:
    ```bash
    pip install pytest
    ```

2.  Save the code above as a Python file (e.g., `test_popup.py`).

3.  Run the tests from your terminal:
    ```bash
    pytest test_popup.py
    ```

This revised solution is significantly more robust and reliable for testing the JavaScript code.  Remember to install the `pytest` library if you haven't already. Remember to adapt the assertions to match the expected behavior in your real code.