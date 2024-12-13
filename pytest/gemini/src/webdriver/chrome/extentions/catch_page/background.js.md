```python
import pytest
from unittest.mock import patch, MagicMock
import json

# Mock chrome API
class MockChrome:
    def __init__(self):
        self.action = MockAction()
        self.runtime = MockRuntime()
        self.tabs = MockTabs()
        self.storage = MockStorage()

class MockAction:
    def __init__(self):
         self.onClicked = MockEvent()

class MockRuntime:
    def __init__(self):
        self.onMessage = MockEvent()
    def sendMessage(self, tabId, message):
        pass #mocked method for sending message to content script

class MockEvent:
    def __init__(self):
        self.listeners = []
    def addListener(self, callback):
        self.listeners.append(callback)

class MockTabs:
     def sendMessage(self, tabId, message):
        pass  #mocked method for sending message to content script

class MockStorage:
    def __init__(self):
       self.local = MockLocal()

    class MockLocal:
      def get(self, key, callback):
        callback({'collectedData': {'test':'data'}})

# Setup the mock chrome API
mock_chrome = MockChrome()

# Mock the global chrome object
@pytest.fixture(autouse=True)
def mock_chrome_api(monkeypatch):
    monkeypatch.setattr("chrome", mock_chrome)

# Import the background script after mocking chrome
from hypotez.src.webdriver.chrome.extentions.catch_page import background

@pytest.fixture
def mock_fetch():
    """Mocks the fetch function to simulate HTTP requests."""
    with patch('hypotez.src.webdriver.chrome.extentions.catch_page.background.fetch') as mock_fetch:
        yield mock_fetch

def test_chrome_action_onClicked_listener():
    """Tests that the onClicked listener sends a message to the tab."""
    
    # Mock the tab object
    mock_tab = MagicMock(id=123, url="http://test.com")

    # Trigger the onClicked event by calling the callback
    mock_chrome.action.onClicked.listeners[0](mock_tab)

    # Assert that chrome.tabs.sendMessage was called correctly
    mock_chrome.tabs.sendMessage.assert_called_once_with(123, {'action': 'collectData', 'url': 'http://test.com'})


def test_chrome_runtime_onMessage_listener_collectData(mock_fetch):
    """Tests the onMessage listener with 'collectData' action."""

    # Prepare mock objects for message and sender
    mock_message = {'action': 'collectData', 'url': 'http://test.com'}
    mock_sender = MagicMock()
    mock_sendResponse = MagicMock()
    
    # Mock the fetch to return an ok response
    mock_response = MagicMock(ok=True)
    mock_fetch.return_value = MagicMock(then=lambda cb: cb(mock_response))

    # Trigger the onMessage event
    mock_chrome.runtime.onMessage.listeners[0](mock_message, mock_sender, mock_sendResponse)

     # Assert fetch was called with correct parameters
    mock_fetch.assert_called_once()
    call_args, call_kwargs = mock_fetch.call_args
    assert call_args[0] == 'http://127.0.0.1/hypotez/catch_request.php'
    assert call_kwargs['method'] == 'POST'
    assert call_kwargs['headers'] == {'Content-Type': 'application/json'}
    assert call_kwargs['body'] == '{"test": "data"}'

def test_chrome_runtime_onMessage_listener_other_action():
    """Tests the onMessage listener with an action other than 'collectData'."""
    
    # Prepare mock objects for message and sender
    mock_message = {'action': 'otherAction', 'url': 'http://test.com'}
    mock_sender = MagicMock()
    mock_sendResponse = MagicMock()

    # Trigger the onMessage event
    mock_chrome.runtime.onMessage.listeners[0](mock_message, mock_sender, mock_sendResponse)

    # Assert that fetch was not called 
    assert not mock_fetch.called

def test_sendDataToServer_success(mock_fetch):
    """Tests sendDataToServer function with successful fetch response."""
    
    # Mock the fetch to return an ok response
    mock_response = MagicMock(ok=True)
    mock_fetch.return_value = MagicMock(then=lambda cb: cb(mock_response))

    # Call the sendDataToServer function directly
    background.sendDataToServer('http://test.com')
    
    # Assert fetch was called with correct parameters
    mock_fetch.assert_called_once()
    call_args, call_kwargs = mock_fetch.call_args
    assert call_args[0] == 'http://127.0.0.1/hypotez/catch_request.php'
    assert call_kwargs['method'] == 'POST'
    assert call_kwargs['headers'] == {'Content-Type': 'application/json'}
    assert call_kwargs['body'] == '{"test": "data"}'


def test_sendDataToServer_fetch_error(mock_fetch):
    """Tests sendDataToServer function with failed fetch response."""

    # Mock the fetch to return a non-ok response
    mock_response = MagicMock(ok=False)
    mock_fetch.return_value = MagicMock(then=lambda cb: cb(mock_response))

    # Call the sendDataToServer function directly
    background.sendDataToServer('http://test.com')
    
     # Assert fetch was called with correct parameters
    mock_fetch.assert_called_once()
    call_args, call_kwargs = mock_fetch.call_args
    assert call_args[0] == 'http://127.0.0.1/hypotez/catch_request.php'
    assert call_kwargs['method'] == 'POST'
    assert call_kwargs['headers'] == {'Content-Type': 'application/json'}
    assert call_kwargs['body'] == '{"test": "data"}'

def test_sendDataToServer_no_data(mock_fetch,monkeypatch):
    """Tests sendDataToServer function when no data is found in chrome storage."""
    
    # Reset the mock storage to not have data
    mock_chrome.storage.local.get = lambda key, callback: callback({})

    # Mock console error
    mock_console_error = MagicMock()
    monkeypatch.setattr("console.error",mock_console_error)


    # Call the sendDataToServer function directly
    background.sendDataToServer('http://test.com')

     # Assert fetch was not called
    assert not mock_fetch.called
    #Assert error was logged
    mock_console_error.assert_called_once_with('No collected data found')
```