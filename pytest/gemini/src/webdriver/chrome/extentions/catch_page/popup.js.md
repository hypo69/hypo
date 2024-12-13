```python
import pytest
from unittest import mock
from unittest.mock import MagicMock

# Since the provided code is JavaScript and runs in a browser context,
# we cannot directly test it with pytest in a traditional way.
# Instead, we'll create mock objects and simulate browser APIs 
# to test the logic within the JavaScript code.

@pytest.fixture
def mock_chrome():
    """Provides a mock chrome object with the necessary methods."""
    mock_chrome = MagicMock()
    mock_chrome.tabs = MagicMock()
    mock_chrome.runtime = MagicMock()
    return mock_chrome

def test_send_url_button_click_success(mock_chrome):
    """
    Tests the scenario where the URL is sent successfully.
    
    This test simulates a button click event, where the URL of the active tab
    is retrieved and sent via a message.
    It asserts that the message is sent with correct parameters and that
    the success alert is shown when a successful response is received.
    """
    mock_tab = MagicMock(url="https://example.com")
    mock_chrome.tabs.query.side_effect = lambda query, callback: callback([mock_tab])

    mock_runtime_message_response = {"status": "success"}
    mock_chrome.runtime.sendMessage.side_effect = lambda message, callback: callback(mock_runtime_message_response)

    # Simulate the button click
    popup_js_code = """
    document.getElementById("sendUrlButton").addEventListener("click", () => {
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

    # Create a mock document with getElementById, that acts like a browser.
    mock_document = MagicMock()
    mock_button = MagicMock()
    mock_document.getElementById.return_value = mock_button
    
    # Create mock window.alert
    mock_alert = MagicMock()
    
    with mock.patch.dict("sys.modules", {
          "chrome": mock_chrome,
          "document": mock_document,
          "window": MagicMock(alert=mock_alert),
      }):
        # Execute the JS code
        exec(popup_js_code)
        mock_button.click()

    # Assertions
    mock_chrome.tabs.query.assert_called_once_with({ "active": True, "currentWindow": True }, mock.ANY)
    mock_chrome.runtime.sendMessage.assert_called_once_with({ "action": "sendUrl", "url": "https://example.com" }, mock.ANY)
    mock_alert.assert_called_with("URL sent successfully!")

def test_send_url_button_click_failure(mock_chrome):
    """
    Tests the scenario where sending the URL fails.

    This test simulates a button click event, where the URL of the active tab
    is retrieved and sent via a message.
    It asserts that the message is sent with correct parameters and that
    the failure alert is shown when an unsuccessful response is received.
    """
    mock_tab = MagicMock(url="https://example.com")
    mock_chrome.tabs.query.side_effect = lambda query, callback: callback([mock_tab])

    mock_runtime_message_response = {"status": "failure"}
    mock_chrome.runtime.sendMessage.side_effect = lambda message, callback: callback(mock_runtime_message_response)

    # Simulate the button click
    popup_js_code = """
    document.getElementById("sendUrlButton").addEventListener("click", () => {
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

    # Create a mock document with getElementById, that acts like a browser.
    mock_document = MagicMock()
    mock_button = MagicMock()
    mock_document.getElementById.return_value = mock_button
    
    # Create mock window.alert
    mock_alert = MagicMock()
    
    with mock.patch.dict("sys.modules", {
          "chrome": mock_chrome,
          "document": mock_document,
          "window": MagicMock(alert=mock_alert),
      }):
        # Execute the JS code
        exec(popup_js_code)
        mock_button.click()

    # Assertions
    mock_chrome.tabs.query.assert_called_once_with({ "active": True, "currentWindow": True }, mock.ANY)
    mock_chrome.runtime.sendMessage.assert_called_once_with({ "action": "sendUrl", "url": "https://example.com" }, mock.ANY)
    mock_alert.assert_called_with("Failed to send URL.")

def test_send_url_button_click_no_active_tab(mock_chrome):
    """
    Tests the scenario where no active tab is found.

    This test simulates a button click event, when the tabs query returns an empty list.
    It asserts that message is not send, and no exception was throw.
    """
    mock_chrome.tabs.query.side_effect = lambda query, callback: callback([])


    # Simulate the button click
    popup_js_code = """
    document.getElementById("sendUrlButton").addEventListener("click", () => {
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

    # Create a mock document with getElementById, that acts like a browser.
    mock_document = MagicMock()
    mock_button = MagicMock()
    mock_document.getElementById.return_value = mock_button
    
    # Create mock window.alert
    mock_alert = MagicMock()
    
    with mock.patch.dict("sys.modules", {
          "chrome": mock_chrome,
          "document": mock_document,
          "window": MagicMock(alert=mock_alert),
      }):
        # Execute the JS code
        exec(popup_js_code)
        mock_button.click()

    # Assertions
    mock_chrome.tabs.query.assert_called_once_with({ "active": True, "currentWindow": True }, mock.ANY)
    mock_chrome.runtime.sendMessage.assert_not_called()
    mock_alert.assert_not_called()


def test_send_url_button_click_message_no_callback(mock_chrome):
    """
    Tests the scenario where the send message action has no callback.

    This test simulates a button click event, where the URL of the active tab
    is retrieved and sent via a message.
    It asserts that the message is sent with correct parameters and no exception is thrown.
    """
    mock_tab = MagicMock(url="https://example.com")
    mock_chrome.tabs.query.side_effect = lambda query, callback: callback([mock_tab])
    mock_chrome.runtime.sendMessage.side_effect = lambda message, callback: None

    # Simulate the button click
    popup_js_code = """
    document.getElementById("sendUrlButton").addEventListener("click", () => {
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

    # Create a mock document with getElementById, that acts like a browser.
    mock_document = MagicMock()
    mock_button = MagicMock()
    mock_document.getElementById.return_value = mock_button
    
    # Create mock window.alert
    mock_alert = MagicMock()
    
    with mock.patch.dict("sys.modules", {
          "chrome": mock_chrome,
          "document": mock_document,
          "window": MagicMock(alert=mock_alert),
      }):
        # Execute the JS code
        exec(popup_js_code)
        mock_button.click()

    # Assertions
    mock_chrome.tabs.query.assert_called_once_with({ "active": True, "currentWindow": True }, mock.ANY)
    mock_chrome.runtime.sendMessage.assert_called_once_with({ "action": "sendUrl", "url": "https://example.com" }, mock.ANY)
    mock_alert.assert_not_called()
```