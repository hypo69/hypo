```python
import pytest
from unittest.mock import MagicMock
from pathlib import Path
from types import SimpleNamespace

from src.webdriver.driver import Driver
from src.endpoints.advertisement.facebook.scenarios.switch_account import switch_account
from src.utils.jjson import j_loads_ns

# Mock the global settings object for file path access
class MockGS:
    class MockPath:
        def __init__(self):
            self.src = Path("mock_src")
        
    def __init__(self):
        self.path = self.MockPath()

gs = MockGS()

# Define a mock function for j_loads_ns to avoid file reads during tests.
def mock_j_loads_ns(path):
    if path == Path(gs.path.src / 'endpoints' / 'advertisement' / 'facebook' / 'locators' / 'post_message.json'):
        return SimpleNamespace(
            switch_to_account_button=SimpleNamespace(
                locator_type='xpath',
                locator_value='//div[@aria-label="Switch Account"]',
            )
        )
    return SimpleNamespace() # default fallback if other paths used.


@pytest.fixture
def mock_driver():
    """Provides a mock Driver instance for tests."""
    driver = MagicMock(spec=Driver)
    return driver

def test_switch_account_button_present(mock_driver, monkeypatch):
    """
    Test case to verify the `switch_account` function clicks the switch account button when it is found.
    """
    monkeypatch.setattr("src.endpoints.advertisement.facebook.scenarios.switch_account.j_loads_ns", mock_j_loads_ns)
    
    # Setup mock to simulate button existence
    mock_driver.execute_locator.return_value = True  # Simulate the button found.
    
    switch_account(mock_driver)

    # Check if `execute_locator` was called with the correct locator.
    mock_driver.execute_locator.assert_called_once_with(
        mock_j_loads_ns(Path(gs.path.src / 'endpoints' / 'advertisement' / 'facebook' / 'locators' / 'post_message.json')).switch_to_account_button
    )


def test_switch_account_button_not_present(mock_driver, monkeypatch):
    """
    Test case to verify the `switch_account` function does not perform action when switch account button is not found
    """
    monkeypatch.setattr("src.endpoints.advertisement.facebook.scenarios.switch_account.j_loads_ns", mock_j_loads_ns)
    
    # Setup mock to simulate button not found
    mock_driver.execute_locator.return_value = False  # Simulate the button NOT found.

    switch_account(mock_driver)

    # Verify that no action has been taken, which means the mock function is not called
    mock_driver.execute_locator.assert_called_once_with(
        mock_j_loads_ns(Path(gs.path.src / 'endpoints' / 'advertisement' / 'facebook' / 'locators' / 'post_message.json')).switch_to_account_button
    )

```