```python
import pytest
from unittest.mock import MagicMock
from src.suppliers.amazon.login import login
from src.logger.logger import logger

# Mock the logger to avoid actual logging during tests
logger.debug = MagicMock()
logger.error = MagicMock()
logger.info = MagicMock()

@pytest.fixture
def mock_supplier():
    """Provides a mock supplier object with necessary attributes."""
    supplier_mock = MagicMock()
    supplier_mock.locators_store = {
        'login': {
            'open_login_inputs': 'open_login_selector',
            'email_input': 'email_input_selector',
            'continue_button': 'continue_button_selector',
            'password_input': 'password_input_selector',
            'keep_signed_in_checkbox': 'checkbox_selector',
            'success_login_button': 'success_button_selector',
        }
    }
    supplier_mock.driver = MagicMock()
    supplier_mock.driver.current_url = "https://www.amazon.com/"
    return supplier_mock

def test_login_successful(mock_supplier):
    """Test successful login with all interactions working correctly."""
    driver_mock = mock_supplier.driver
    driver_mock.click.return_value = True
    driver_mock.execute_locator.return_value = True
    driver_mock.current_url = "https://www.amazon.com/"

    assert login(mock_supplier) is True
    
    driver_mock.window_focus.assert_called()
    driver_mock.get_url.assert_called_with('https://amazon.com/')
    driver_mock.click.assert_called_with('open_login_selector')
    driver_mock.execute_locator.assert_called_with('email_input_selector')
    driver_mock.execute_locator.assert_called_with('continue_button_selector')
    driver_mock.execute_locator.assert_called_with('password_input_selector')
    driver_mock.execute_locator.assert_called_with('checkbox_selector')
    driver_mock.execute_locator.assert_called_with('success_button_selector')
    driver_mock.maximize_window.assert_called()
    logger.info.assert_called()
    logger.error.assert_not_called()


def test_login_open_login_inputs_fails_first_time(mock_supplier):
    """Test case where clicking 'open_login_inputs' fails once but succeeds on retry."""
    driver_mock = mock_supplier.driver
    driver_mock.click.side_effect = [False, True] # Fail first, then succeed
    driver_mock.execute_locator.return_value = True
    driver_mock.current_url = "https://www.amazon.com/"

    assert login(mock_supplier) is True
    
    driver_mock.window_focus.assert_called()
    driver_mock.get_url.assert_called_with('https://amazon.com/')
    assert driver_mock.click.call_count == 2
    driver_mock.click.assert_called_with('open_login_selector')
    driver_mock.refresh.assert_called()
    driver_mock.execute_locator.assert_called_with('email_input_selector')
    driver_mock.execute_locator.assert_called_with('continue_button_selector')
    driver_mock.execute_locator.assert_called_with('password_input_selector')
    driver_mock.execute_locator.assert_called_with('checkbox_selector')
    driver_mock.execute_locator.assert_called_with('success_button_selector')
    driver_mock.maximize_window.assert_called()
    logger.info.assert_called()
    logger.debug.assert_called()
    logger.error.assert_not_called()


def test_login_open_login_inputs_fails_both_times(mock_supplier):
    """Test case where clicking 'open_login_inputs' fails both times."""
    driver_mock = mock_supplier.driver
    driver_mock.click.return_value = False  # Fail both times
    driver_mock.execute_locator.return_value = True
    driver_mock.current_url = "https://www.amazon.com/"

    assert login(mock_supplier) is None  # Expecting None, because of return without value
    
    driver_mock.window_focus.assert_called()
    driver_mock.get_url.assert_called_with('https://amazon.com/')
    assert driver_mock.click.call_count == 2
    driver_mock.click.assert_called_with('open_login_selector')
    driver_mock.refresh.assert_called()
    logger.debug.assert_called()
    logger.info.assert_not_called()
    logger.error.assert_not_called()


def test_login_email_input_fails(mock_supplier):
    """Test case where filling email input fails."""
    driver_mock = mock_supplier.driver
    driver_mock.click.return_value = True
    driver_mock.execute_locator.side_effect = [False, True, True, True, True]  # Email fails
    driver_mock.current_url = "https://www.amazon.com/"

    assert login(mock_supplier) is None  # Expecting None, because of return without value
    
    driver_mock.window_focus.assert_called()
    driver_mock.get_url.assert_called_with('https://amazon.com/')
    driver_mock.click.assert_called_with('open_login_selector')
    driver_mock.execute_locator.assert_called_with('email_input_selector')
    logger.info.assert_not_called()
    logger.error.assert_not_called()

def test_login_continue_button_fails(mock_supplier):
    """Test case where clicking 'continue_button' fails."""
    driver_mock = mock_supplier.driver
    driver_mock.click.return_value = True
    driver_mock.execute_locator.side_effect = [True, False, True, True, True] # continue fails
    driver_mock.current_url = "https://www.amazon.com/"

    assert login(mock_supplier) is None  # Expecting None, because of return without value

    driver_mock.window_focus.assert_called()
    driver_mock.get_url.assert_called_with('https://amazon.com/')
    driver_mock.click.assert_called_with('open_login_selector')
    driver_mock.execute_locator.assert_called_with('email_input_selector')
    driver_mock.execute_locator.assert_called_with('continue_button_selector')
    logger.info.assert_not_called()
    logger.error.assert_not_called()


def test_login_password_input_fails(mock_supplier):
    """Test case where filling password input fails."""
    driver_mock = mock_supplier.driver
    driver_mock.click.return_value = True
    driver_mock.execute_locator.side_effect = [True, True, False, True, True]  # password fails
    driver_mock.current_url = "https://www.amazon.com/"

    assert login(mock_supplier) is None  # Expecting None, because of return without value

    driver_mock.window_focus.assert_called()
    driver_mock.get_url.assert_called_with('https://amazon.com/')
    driver_mock.click.assert_called_with('open_login_selector')
    driver_mock.execute_locator.assert_called_with('email_input_selector')
    driver_mock.execute_locator.assert_called_with('continue_button_selector')
    driver_mock.execute_locator.assert_called_with('password_input_selector')
    logger.info.assert_not_called()
    logger.error.assert_not_called()

def test_login_keep_signed_in_checkbox_fails(mock_supplier):
    """Test case where filling the keep signed in checkbox fails."""
    driver_mock = mock_supplier.driver
    driver_mock.click.return_value = True
    driver_mock.execute_locator.side_effect = [True, True, True, False, True] # checkbox fails
    driver_mock.current_url = "https://www.amazon.com/"

    assert login(mock_supplier) is None  # Expecting None, because of return without value
    
    driver_mock.window_focus.assert_called()
    driver_mock.get_url.assert_called_with('https://amazon.com/')
    driver_mock.click.assert_called_with('open_login_selector')
    driver_mock.execute_locator.assert_called_with('email_input_selector')
    driver_mock.execute_locator.assert_called_with('continue_button_selector')
    driver_mock.execute_locator.assert_called_with('password_input_selector')
    driver_mock.execute_locator.assert_called_with('checkbox_selector')
    logger.info.assert_not_called()
    logger.error.assert_not_called()

def test_login_success_login_button_fails(mock_supplier):
    """Test case where clicking the 'success_login_button' fails."""
    driver_mock = mock_supplier.driver
    driver_mock.click.return_value = True
    driver_mock.execute_locator.side_effect = [True, True, True, True, False] # success button fails
    driver_mock.current_url = "https://www.amazon.com/"

    assert login(mock_supplier) is None  # Expecting None, because of return without value
    
    driver_mock.window_focus.assert_called()
    driver_mock.get_url.assert_called_with('https://amazon.com/')
    driver_mock.click.assert_called_with('open_login_selector')
    driver_mock.execute_locator.assert_called_with('email_input_selector')
    driver_mock.execute_locator.assert_called_with('continue_button_selector')
    driver_mock.execute_locator.assert_called_with('password_input_selector')
    driver_mock.execute_locator.assert_called_with('checkbox_selector')
    driver_mock.execute_locator.assert_called_with('success_button_selector')
    logger.info.assert_not_called()
    logger.error.assert_not_called()


def test_login_failed_login_redirect(mock_supplier):
    """Test case where login fails due to redirection to the sign-in page."""
    driver_mock = mock_supplier.driver
    driver_mock.click.return_value = True
    driver_mock.execute_locator.return_value = True
    driver_mock.current_url = "https://www.amazon.com/ap/signin"  # Simulate a failed login redirect

    assert login(mock_supplier) is None # Expecting None, because of return without value
    
    driver_mock.window_focus.assert_called()
    driver_mock.get_url.assert_called_with('https://amazon.com/')
    driver_mock.click.assert_called_with('open_login_selector')
    driver_mock.execute_locator.assert_called_with('email_input_selector')
    driver_mock.execute_locator.assert_called_with('continue_button_selector')
    driver_mock.execute_locator.assert_called_with('password_input_selector')
    driver_mock.execute_locator.assert_called_with('checkbox_selector')
    driver_mock.execute_locator.assert_called_with('success_button_selector')
    logger.error.assert_called()
    logger.info.assert_not_called()
```