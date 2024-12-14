```python
import pytest
from unittest.mock import MagicMock
from unittest.mock import AsyncMock

# Mock the browser API
@pytest.fixture
def mock_browser():
    """Mocks the browser API for testing."""
    browser_mock = MagicMock()
    browser_mock.browserAction = MagicMock()
    browser_mock.browserAction.onClicked = MagicMock()
    browser_mock.scripting = MagicMock()
    browser_mock.scripting.executeScript = AsyncMock()

    return browser_mock


# Mock the Tab object
@pytest.fixture
def mock_tab():
    """Mocks the Tab object for testing."""
    tab_mock = MagicMock()
    tab_mock.id = 123
    return tab_mock


def test_browser_action_on_clicked_listener_calls_execute_script(mock_browser, mock_tab):
    """
    Test that when browserAction.onClicked is triggered, it calls scripting.executeScript
    with correct target and files.
    """
    # Arrange: Setup mocks and get the listener function
    listener_callback = mock_browser.browserAction.onClicked.addListener.call_args[0][0]

    # Act: Simulate the browser action click with a mock tab object
    listener_callback(mock_tab)

    # Assert: Check that scripting.executeScript was called with correct arguments
    mock_browser.scripting.executeScript.assert_called_once_with(
        target={'tabId': mock_tab.id}, files=['contentScript.js']
    )


def test_browser_action_on_clicked_listener_no_tab(mock_browser):
    """
    Test that listener can run when no tab is given (this might occur during testing, though not in browser)
    """
    # Arrange: Setup mocks and get the listener function
    listener_callback = mock_browser.browserAction.onClicked.addListener.call_args[0][0]

    # Act: Simulate the browser action click with no tab object
    # The listener will need to handle cases where tab information may not be present
    try:
         listener_callback(None)
    except Exception as e:
         pytest.fail(f"Listener should not throw an exception: {e}")

    # Assert: Check that scripting.executeScript was not called, since no tab id is available
    mock_browser.scripting.executeScript.assert_not_called()

def test_browser_action_on_clicked_listener_empty_tab(mock_browser):
    """
    Test that listener can run when  tab object is empty(this might occur during testing, though not in browser)
    """
    # Arrange: Setup mocks and get the listener function
    listener_callback = mock_browser.browserAction.onClicked.addListener.call_args[0][0]

    # Act: Simulate the browser action click with a empty tab object
    # The listener will need to handle cases where tab information may not be present
    mock_tab = MagicMock()
    try:
         listener_callback(mock_tab)
    except Exception as e:
         pytest.fail(f"Listener should not throw an exception: {e}")

    # Assert: Check that scripting.executeScript was not called, since no tab id is available
    mock_browser.scripting.executeScript.assert_not_called()
```