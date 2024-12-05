```python
import pytest
import unittest.mock as mock

def test_onInstalled_listener_logging(mocker):
    """
    Tests the onInstalled listener logs the correct message.
    """
    # Mock the console.log function
    mock_console_log = mocker.patch('console.log')

    # Call the function (which will trigger the listener)
    chrome_runtime_onInstalled = mock.Mock()
    chrome_runtime_onInstalled.addListener(lambda: None)
    chrome_runtime_onInstalled.onInstalled.assert_not_called()  # Should not be called in this test

    # Expect the mock to be called with the correct message
    mock_console_log.assert_called_once_with('OpenAI Model Interface Extension Installed')


# No further tests are possible as the code does not return any values
# or contain any functions that could be tested.
```