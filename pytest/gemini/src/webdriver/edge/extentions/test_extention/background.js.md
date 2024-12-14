```python
import pytest
from unittest.mock import MagicMock, patch
import json

# Mock the chrome API
class MockChrome:
    def __init__(self):
        self.browserAction = MockBrowserAction()
        self.tabs = MockTabs()
        self.runtime = MockRuntime()
        self.storage = MockStorage()

class MockBrowserAction:
    def __init__(self):
        self.onClicked = MockEvent()

class MockTabs:
    def __init__(self):
        self.sendMessage = MagicMock()

class MockRuntime:
    def __init__(self):
       self.onMessage = MockEvent()
       
class MockStorage:
    def __init__(self):
        self.local = MockLocalStorage()
    
class MockLocalStorage:
    def __init__(self):
        self.get = MagicMock()
        
class MockEvent:
     def __init__(self):
        self.listeners = []
     def addListener(self, callback):
        self.listeners.append(callback)

# Mock the fetch API
class MockResponse:
    def __init__(self, ok, status=200):
        self.ok = ok
        self.status = status
        
    def json(self):
        return {"message": "Success"}  # Mock response data


@pytest.fixture
def mock_chrome():
    """Mocks the chrome API for testing."""
    with patch('background.chrome', new_callable=MockChrome) as mock_chrome:
        yield mock_chrome

@pytest.fixture
def mock_fetch():
     with patch('background.fetch') as mock_fetch:
         yield mock_fetch
         
@pytest.fixture
def background():
    import hypotez.src.webdriver.edge.extentions.test_extention.background as background
    return background


def test_browser_action_on_click_sends_message(mock_chrome, background):
    """Tests if clicking the browser action sends a message to the current tab."""
    tab_id = 1
    tab_url = 'https://example.com'
    mock_tab = MagicMock(id=tab_id, url=tab_url)
    
    # Simulate a browser action click
    for listener in mock_chrome.browserAction.onClicked.listeners:
        listener(mock_tab)

    # Verify that sendMessage was called with the correct arguments
    mock_chrome.tabs.sendMessage.assert_called_once_with(tab_id, {'action': 'collectData', 'url': tab_url})


def test_runtime_on_message_collect_data(mock_chrome, mock_fetch, background):
    """Tests if the runtime message listener correctly handles 'collectData' action."""
    test_url = 'https://example.com/test'
    mock_chrome.storage.local.get.side_effect = lambda key, callback: callback({'collectedData': {'test': 'data'}})

    # Simulate a message being received
    for listener in mock_chrome.runtime.onMessage.listeners:
        listener({'action': 'collectData', 'url': test_url}, None, None)
    
    # Ensure fetch is called with correct URL and data
    mock_fetch.assert_called_once()
    url, options = mock_fetch.call_args
    assert url == 'http://127.0.0.1/hypotez.online/api/'
    assert options['method'] == 'POST'
    assert options['headers'] == {'Content-Type': 'application/json'}
    assert options['body'] == json.dumps({'test': 'data'})
    

def test_send_data_to_server_success(mock_chrome, mock_fetch, background):
    """Tests the successful sending of data to the server."""
    test_url = 'https://example.com/test'
    mock_chrome.storage.local.get.side_effect = lambda key, callback: callback({'collectedData': {'test': 'data'}})
    mock_fetch.return_value =  Promise(MockResponse(ok=True))
    
    background.sendDataToServer(test_url)
    # Ensure fetch is called
    mock_fetch.assert_called_once()

def test_send_data_to_server_no_data(mock_chrome, mock_fetch, background, capsys):
    """Tests handling of no collected data in sendDataToServer."""
    test_url = 'https://example.com/test'
    mock_chrome.storage.local.get.side_effect = lambda key, callback: callback({})

    background.sendDataToServer(test_url)
    captured = capsys.readouterr()
    assert "No collected data found" in captured.err
    mock_fetch.assert_not_called()
    
def test_send_data_to_server_fetch_error(mock_chrome, mock_fetch, background, capsys):
    """Tests the error handling of a failed fetch request."""
    test_url = 'https://example.com/test'
    mock_chrome.storage.local.get.side_effect = lambda key, callback: callback({'collectedData': {'test': 'data'}})
    mock_fetch.return_value = Promise(MockResponse(ok=False,status=500))
    
    background.sendDataToServer(test_url)
    captured = capsys.readouterr()
    assert "Error sending data to server:" in captured.err
    assert "Failed to send data to server" in captured.err

class Promise:
    def __init__(self, value):
        self.value = value
        self.catch_callback = None

    def then(self, callback):
      if self.value.ok:
        callback(self.value)
      return self

    def catch(self, callback):
        if not self.value.ok:
            callback(Exception("Failed to send data to server"))
        return self
```