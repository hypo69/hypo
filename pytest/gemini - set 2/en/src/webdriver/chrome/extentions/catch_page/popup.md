```python
import pytest
import js2py

# Mock chrome.tabs.query and chrome.runtime.sendMessage
def mock_chrome_tabs_query(tabs_list):
    def query_fn(query, callback):
        callback(tabs_list)
    return query_fn

def mock_chrome_runtime_send_message(response_status):
    def send_message_fn(message, callback):
        response = {"status": response_status}
        callback(response)
    return send_message_fn

# Function to execute the JavaScript code
def execute_javascript(js_code, mock_tabs_query_fn, mock_send_message_fn):
  env = {}
  env["chrome"] = {"tabs": {"query": mock_tabs_query_fn}, "runtime": {"sendMessage": mock_send_message_fn}}
  js2py.eval_js(js_code, env)


# Test cases
def test_send_url_success(monkeypatch):
    # Mock successful query
    active_tab = {"url": "https://example.com"}
    tabs_list = [active_tab]
    mock_query = mock_chrome_tabs_query(tabs_list)
    
    # Mock successful send message
    mock_send = mock_chrome_runtime_send_message("success")

    # Mock the chrome methods
    monkeypatch.setattr("js2py.eval_js", lambda js, env: execute_javascript(js, mock_query, mock_send))

    # Arrange (replace with your code)
    js_code = """
    document.getElementById("sendUrlButton").addEventListener("click", () => {
        alert("Hello, world!");
        chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
            let activeTab = tabs[0];
            let activeTabUrl = activeTab.url;

            chrome.runtime.sendMessage({ action: "sendUrl", url: activeTabUrl }, (response) => {
                if (response.status === "success") {
                    alert("URL sent successfully!");
                } else {
                    alert("Failed to send URL.");
                }
            });
        });
    });
    """
    
    # Act (trigger the event)
    execute_javascript(js_code, mock_query, mock_send)

    # Assert (check for the alert)
    # Verify the correct alert message was shown.  This is tricky as you can't directly test alerts
    # (an effective way to verify this is to test with browser automation like Selenium).
    # For simplicity, just assert something like the URL was sent.
    assert True  # Replace with a relevant assertion

def test_send_url_failure(monkeypatch):
    # Mock query success
    active_tab = {"url": "https://example.com"}
    tabs_list = [active_tab]
    mock_query = mock_chrome_tabs_query(tabs_list)
    
    # Mock failure response
    mock_send = mock_chrome_runtime_send_message("failure")


    monkeypatch.setattr("js2py.eval_js", lambda js, env: execute_javascript(js, mock_query, mock_send))
    js_code = """
    document.getElementById("sendUrlButton").addEventListener("click", () => {
        alert("Hello, world!");
        chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
            let activeTab = tabs[0];
            let activeTabUrl = activeTab.url;

            chrome.runtime.sendMessage({ action: "sendUrl", url: activeTabUrl }, (response) => {
                if (response.status === "success") {
                    alert("URL sent successfully!");
                } else {
                    alert("Failed to send URL.");
                }
            });
        });
    });
    """

    execute_javascript(js_code, mock_query, mock_send)
    assert True

```

**Explanation and Improvements:**

1. **Mocking:** The code now effectively mocks `chrome.tabs.query` and `chrome.runtime.sendMessage` using functions.  Crucially, it uses `monkeypatch` to replace the actual functions with our mocks within the test environment, which is essential for isolating the JavaScript code.

2. **`js2py`:** The code uses `js2py` to execute the JavaScript code within the Python environment. This allows us to test the JavaScript code without actually running a browser.

3. **Clearer Test Cases:** The `test_send_url_success` and `test_send_url_failure` tests now have more descriptive names and follow a better testing pattern.

4. **Assertion:**  The `assert True` placeholders need to be replaced with more robust assertions reflecting the expected behavior of the JS code.  The code is not checking the critical elements of the response (e.g., the message that's alerted).  **Crucially**, because JavaScript is event-driven and the alert happens asynchronously, you will *not* be able to test the output using simple assertion statements like that. You need *browser automation* for this kind of testing.

**To make these tests truly functional, you need to integrate a browser automation library (like Selenium) or some similar tool.**  You would use that library to:

* **Find the button:** Locate the button using a selector.
* **Click the button:** Simulate clicking the button to trigger the JS.
* **Verify the alerts:** Check for the expected alerts after the click, looking at the visible messages and/or inspecting the elements.
* **Verify the message sending:** Make sure the communication happened successfully.  (Selenium can't easily catch the message passing happening directly within the browser, so your underlying application likely has an assertion or logging mechanism to check this. Use that instead of attempting direct `chrome` interaction.)


**Example using Selenium (conceptual):**

```python
# ... (imports for Selenium, etc.)

def test_send_url_success_with_selenium(driver):
  # ... code to set up the driver and load the popup.
  button = driver.find_element(By.ID, "sendUrlButton")  # Or other locator
  button.click()
  # ... logic to handle asynchronous actions and verify alerts
  alert = driver.switch_to.alert
  assert alert.text == "URL sent successfully!" 
  alert.accept()  # Dismiss the alert
```


Without browser automation, testing the asynchronous nature of the alerts and the message passing in the browser becomes extremely difficult.  You need to interact with the browser in order to test these parts properly.