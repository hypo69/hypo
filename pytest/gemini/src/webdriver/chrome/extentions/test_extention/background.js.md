```python
import pytest
from unittest.mock import patch, MagicMock
import json

# Mock chrome API
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
        self.local = MockLocal()
    
class MockLocal:
     def __init__(self):
        self.get = MagicMock()


class MockEvent:
    def __init__(self):
      self.listeners = []

    def addListener(self, callback):
        self.listeners.append(callback)

    def trigger(self, *args):
        for callback in self.listeners:
            callback(*args)


# Fixture to setup mock chrome object
@pytest.fixture
def mock_chrome():
    with patch('chrome', MockChrome()):
        yield chrome # now we can use chrome as the mock
        
# Import the code to be tested
from hypotez.src.webdriver.chrome.extentions.test_extention import background

def test_browser_action_on_clicked(mock_chrome):
    """Test that browser action click sends message to tab"""
    tab_id = 123
    tab_url = "http://example.com"
    mock_tab = MagicMock(id=tab_id, url=tab_url)
    mock_chrome.browserAction.onClicked.trigger(mock_tab)

    mock_chrome.tabs.sendMessage.assert_called_once_with(tab_id, {'action': 'collectData', 'url': tab_url})


def test_runtime_on_message_collect_data(mock_chrome):
    """Test that runtime message with collectData action calls sendDataToServer"""
    mock_send_data_to_server = MagicMock()
    with patch('hypotez.src.webdriver.chrome.extentions.test_extention.background.sendDataToServer', mock_send_data_to_server):
        message = {'action': 'collectData', 'url': 'http://test.com'}
        sender = {}
        sendResponse = MagicMock()
        mock_chrome.runtime.onMessage.trigger(message, sender, sendResponse)
    
    mock_send_data_to_server.assert_called_once_with('http://test.com')

def test_runtime_on_message_other_action(mock_chrome):
    """Test that runtime message with other action does not call sendDataToServer"""
    mock_send_data_to_server = MagicMock()
    with patch('hypotez.src.webdriver.chrome.extentions.test_extention.background.sendDataToServer', mock_send_data_to_server):
        message = {'action': 'otherAction', 'url': 'http://test.com'}
        sender = {}
        sendResponse = MagicMock()
        mock_chrome.runtime.onMessage.trigger(message, sender, sendResponse)
    
    mock_send_data_to_server.assert_not_called()

@pytest.mark.asyncio
async def test_send_data_to_server_success(mock_chrome):
    """Test sendDataToServer sends data to server and handles success"""
    mock_chrome.storage.local.get.return_value = {"collectedData": {"key": "value"}}

    mock_fetch = MagicMock()
    mock_response = MagicMock(ok=True)
    mock_fetch.return_value = mock_response
    
    with patch('hypotez.src.webdriver.chrome.extentions.test_extention.background.fetch', mock_fetch):
        with patch('hypotez.src.webdriver.chrome.extentions.test_extention.background.console.log') as mock_console_log:
            background.sendDataToServer('http://test.com')
            mock_chrome.storage.local.get.assert_called_once_with('collectedData', )
            mock_fetch.assert_called_once()
            mock_console_log.assert_called_once_with('Data sent to server successfully')
            
            args, kwargs = mock_fetch.call_args
            assert args[0] == 'http://127.0.0.1/hypotez.online/api/'
            assert kwargs['method'] == 'POST'
            assert kwargs['headers'] == {'Content-Type': 'application/json'}
            assert json.loads(kwargs['body']) == {"key": "value"}


@pytest.mark.asyncio
async def test_send_data_to_server_fetch_error(mock_chrome):
    """Test sendDataToServer handles fetch error"""
    mock_chrome.storage.local.get.return_value = {"collectedData": {"key": "value"}}
    mock_fetch = MagicMock()
    mock_response = MagicMock(ok=False)
    mock_fetch.return_value = mock_response
    
    with patch('hypotez.src.webdriver.chrome.extentions.test_extention.background.fetch', mock_fetch):
          with patch('hypotez.src.webdriver.chrome.extentions.test_extention.background.console.error') as mock_console_error:
            background.sendDataToServer('http://test.com')
            mock_fetch.assert_called_once()
            mock_console_error.assert_called() # Check if console.error is called, it does not matter what message it prints
           
@pytest.mark.asyncio
async def test_send_data_to_server_no_collected_data(mock_chrome):
    """Test sendDataToServer handles no collected data"""
    mock_chrome.storage.local.get.return_value = {"collectedData": None}
    
    with patch('hypotez.src.webdriver.chrome.extentions.test_extention.background.console.error') as mock_console_error:
          background.sendDataToServer('http://test.com')
          mock_chrome.storage.local.get.assert_called_once()
          mock_console_error.assert_called_once_with('No collected data found')
```