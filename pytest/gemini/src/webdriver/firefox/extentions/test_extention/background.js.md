```python
import pytest
from unittest.mock import MagicMock

# Mock the browser API for testing
@pytest.fixture
def mock_browser():
    """Mocks the browser API for testing."""
    browser_mock = MagicMock()
    browser_mock.browserAction.onClicked = MagicMock()
    browser_mock.scripting.executeScript = MagicMock()
    return browser_mock


def test_browser_action_on_click(mock_browser):
    """
    Tests that the executeScript function is called when the browser action is clicked.
    It verifies that executeScript is called with the correct target and files.
    """
    # Simulate a click on the browser action
    tab_mock = MagicMock()
    tab_mock.id = 123  # Mock tab ID
    mock_browser.browserAction.onClicked.listeners[0](tab_mock)
    
    # Assert that executeScript was called once
    mock_browser.scripting.executeScript.assert_called_once()
    
    # Check arguments for executeScript
    args, _ = mock_browser.scripting.executeScript.call_args
    assert args == ({
        'target': { 'tabId': 123 },
        'files': ["contentScript.js"],
    },)
    
def test_browser_action_on_click_multiple_listeners(mock_browser):
    """
    Tests that the executeScript function is called when browser action has multiple listener, it verifies that the right listener execute
    """
    # Simulate a click on the browser action
    tab_mock = MagicMock()
    tab_mock.id = 123  # Mock tab ID
    
    def dummy_listener(tab):
        pass
    
    mock_browser.browserAction.onClicked.addListener(dummy_listener)
    
    mock_browser.browserAction.onClicked.listeners[1](tab_mock)
    
     # Assert that executeScript was called once
    mock_browser.scripting.executeScript.assert_called_once()
    
    # Check arguments for executeScript
    args, _ = mock_browser.scripting.executeScript.call_args
    assert args == ({
        'target': { 'tabId': 123 },
        'files': ["contentScript.js"],
    },)

def test_browser_action_on_click_no_tab_id(mock_browser):
   """
    Tests the behaviour when the tab has no id, this is an unexpected case
    It verifies that the the listener handles this edge case
   """
   # Simulate a click on the browser action
   tab_mock = MagicMock()
   tab_mock.id = None  # Mock tab ID
   mock_browser.browserAction.onClicked.listeners[0](tab_mock)
   
   # Assert that executeScript was called once
   mock_browser.scripting.executeScript.assert_called_once()
   
   # Check arguments for executeScript
   args, _ = mock_browser.scripting.executeScript.call_args
   assert args == ({
       'target': { 'tabId': None },
       'files': ["contentScript.js"],
   },)
```