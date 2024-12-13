```python
import pytest
from unittest.mock import MagicMock
from src.suppliers.aliexpress.scenarios.login import login


# Fixture definitions
@pytest.fixture
def mock_supplier():
    """Provides a mock Supplier object for testing."""
    mock_supplier = MagicMock()
    mock_supplier.driver = MagicMock()
    mock_supplier.locators = {
        'login': {
            'cookies_accept': 'cookies_accept_locator',
            'open_login': 'open_login_locator',
            'email_locator': 'email_locator_val',
            'password_locator': 'password_locator_val',
            'loginbutton_locator': 'loginbutton_locator_val',
        }
    }
    return mock_supplier


def test_login_success(mock_supplier):
    """Checks if the login function returns True when all locators are found and executed successfully."""
    # Configure mock driver behavior
    mock_supplier.driver.get_url.return_value = None
    mock_supplier.driver.execute_locator.side_effect = [True, True, True, True, True]
    mock_supplier.driver.wait.return_value = None

    # Call the login function
    result = login(mock_supplier)

    # Assert that login returns True
    assert result is True

    # Assert that the driver methods were called
    mock_supplier.driver.get_url.assert_called_once_with('https://www.aliexpress.com')
    mock_supplier.driver.execute_locator.assert_any_call('cookies_accept_locator')
    mock_supplier.driver.execute_locator.assert_any_call('open_login_locator')
    mock_supplier.driver.execute_locator.assert_any_call('email_locator_val')
    mock_supplier.driver.execute_locator.assert_any_call('password_locator_val')
    mock_supplier.driver.execute_locator.assert_any_call('loginbutton_locator_val')
    assert mock_supplier.driver.wait.call_count == 3


def test_login_email_locator_fails(mock_supplier):
    """Checks if login returns True (for now) when the email locator is not found. (TODO: change after logic implemented)"""
    # Configure mock driver behavior to fail at email locator
    mock_supplier.driver.get_url.return_value = None
    mock_supplier.driver.execute_locator.side_effect = [True, True, False, True, True]
    mock_supplier.driver.wait.return_value = None


    # Call the login function
    result = login(mock_supplier)

    # Assert that login returns True (for now)
    assert result is True

    # Assert that the driver methods were called
    mock_supplier.driver.get_url.assert_called_once_with('https://www.aliexpress.com')
    mock_supplier.driver.execute_locator.assert_any_call('cookies_accept_locator')
    mock_supplier.driver.execute_locator.assert_any_call('open_login_locator')
    mock_supplier.driver.execute_locator.assert_any_call('email_locator_val')
    assert mock_supplier.driver.wait.call_count == 3


def test_login_password_locator_fails(mock_supplier):
    """Checks if login returns True (for now) when the password locator is not found. (TODO: change after logic implemented)"""
    # Configure mock driver behavior to fail at password locator
    mock_supplier.driver.get_url.return_value = None
    mock_supplier.driver.execute_locator.side_effect = [True, True, True, False, True]
    mock_supplier.driver.wait.return_value = None

    # Call the login function
    result = login(mock_supplier)

    # Assert that login returns True (for now)
    assert result is True

    # Assert that the driver methods were called
    mock_supplier.driver.get_url.assert_called_once_with('https://www.aliexpress.com')
    mock_supplier.driver.execute_locator.assert_any_call('cookies_accept_locator')
    mock_supplier.driver.execute_locator.assert_any_call('open_login_locator')
    mock_supplier.driver.execute_locator.assert_any_call('password_locator_val')
    assert mock_supplier.driver.wait.call_count == 3



def test_login_button_locator_fails(mock_supplier):
    """Checks if login returns True (for now) when the login button locator is not found. (TODO: change after logic implemented)"""
    # Configure mock driver behavior to fail at login button locator
    mock_supplier.driver.get_url.return_value = None
    mock_supplier.driver.execute_locator.side_effect = [True, True, True, True, False]
    mock_supplier.driver.wait.return_value = None


    # Call the login function
    result = login(mock_supplier)

    # Assert that login returns True (for now)
    assert result is True

    # Assert that the driver methods were called
    mock_supplier.driver.get_url.assert_called_once_with('https://www.aliexpress.com')
    mock_supplier.driver.execute_locator.assert_any_call('cookies_accept_locator')
    mock_supplier.driver.execute_locator.assert_any_call('open_login_locator')
    mock_supplier.driver.execute_locator.assert_any_call('loginbutton_locator_val')
    assert mock_supplier.driver.wait.call_count == 3



```