```python
import pytest
from unittest.mock import MagicMock

# Mock the chrome.runtime and chrome.runtime.onInstalled
class MockChromeRuntime:
    def __init__(self):
        self.onInstalled = MockChromeOnInstalled()

class MockChromeOnInstalled:
    def __init__(self):
        self.listeners = []

    def addListener(self, listener):
        self.listeners.append(listener)

    def trigger(self):
       for listener in self.listeners:
         listener()



# Fixture for mocking chrome.runtime
@pytest.fixture
def mock_chrome_runtime():
    """Provides a mock chrome.runtime object."""
    mock_runtime = MockChromeRuntime()
    global chrome  # Use global to mimic the global chrome object
    chrome = mock_runtime
    return mock_runtime

def test_extension_installed_listener_triggered(mock_chrome_runtime, capsys):
    """Checks if the listener function is triggered upon installation and logs the message."""
    
    #  The code under test is implicitly part of the injected chrome context
    # chrome.runtime.onInstalled.addListener(() => {
    #     console.log('OpenAI Model Interface Extension Installed');
    # });

    mock_chrome_runtime.onInstalled.trigger()

    # Capture the console output
    captured = capsys.readouterr()
    assert "OpenAI Model Interface Extension Installed" in captured.out
    
def test_extension_installed_listener_not_triggered_before_event(mock_chrome_runtime, capsys):
     """Ensure that the console message is not logged before the installation event is triggered."""
     captured = capsys.readouterr()
     assert "OpenAI Model Interface Extension Installed" not in captured.out

```