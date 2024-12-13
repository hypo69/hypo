```python
import pytest
from unittest.mock import MagicMock
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from src.webdriver.js import JavaScript


@pytest.fixture
def mock_driver():
    """Provides a mock WebDriver instance."""
    driver = MagicMock(spec=WebDriver)
    return driver

@pytest.fixture
def mock_element():
    """Provides a mock WebElement instance."""
    element = MagicMock(spec=WebElement)
    return element


def test_javascript_init(mock_driver):
    """Checks if the JavaScript class initializes correctly with a WebDriver instance."""
    js_helper = JavaScript(mock_driver)
    assert js_helper.driver == mock_driver


def test_unhide_DOM_element_success(mock_driver, mock_element):
    """Checks if unhide_DOM_element executes script successfully and returns True."""
    js_helper = JavaScript(mock_driver)
    mock_driver.execute_script.return_value = None  # script execution should be successful
    assert js_helper.unhide_DOM_element(mock_element) is True
    mock_driver.execute_script.assert_called_once()  # Assert that the script was called


def test_unhide_DOM_element_failure(mock_driver, mock_element):
    """Checks if unhide_DOM_element returns False when script execution fails."""
    js_helper = JavaScript(mock_driver)
    mock_driver.execute_script.side_effect = Exception("Script execution failed")
    assert js_helper.unhide_DOM_element(mock_element) is False
    mock_driver.execute_script.assert_called_once()  # Assert that the script was called


def test_ready_state_complete(mock_driver):
    """Checks if ready_state returns 'complete' when the document loading is complete."""
    js_helper = JavaScript(mock_driver)
    mock_driver.execute_script.return_value = 'complete'
    assert js_helper.ready_state == 'complete'


def test_ready_state_loading(mock_driver):
    """Checks if ready_state returns 'loading' when the document is still loading."""
    js_helper = JavaScript(mock_driver)
    mock_driver.execute_script.return_value = 'loading'
    assert js_helper.ready_state == 'loading'


def test_ready_state_error(mock_driver):
    """Checks if ready_state returns '' when an error occurs."""
    js_helper = JavaScript(mock_driver)
    mock_driver.execute_script.side_effect = Exception("Script execution failed")
    assert js_helper.ready_state == ''


def test_window_focus_success(mock_driver):
    """Checks if window_focus executes the script successfully."""
    js_helper = JavaScript(mock_driver)
    js_helper.window_focus()
    mock_driver.execute_script.assert_called_once()


def test_window_focus_failure(mock_driver):
    """Checks if window_focus handles the script execution failure gracefully."""
    js_helper = JavaScript(mock_driver)
    mock_driver.execute_script.side_effect = Exception("Script execution failed")
    js_helper.window_focus()  # It should not raise an exception


def test_get_referrer_valid(mock_driver):
    """Checks if get_referrer returns the correct referrer URL."""
    js_helper = JavaScript(mock_driver)
    mock_driver.execute_script.return_value = 'https://example.com/referrer'
    assert js_helper.get_referrer() == 'https://example.com/referrer'


def test_get_referrer_empty(mock_driver):
    """Checks if get_referrer returns an empty string when no referrer is available."""
    js_helper = JavaScript(mock_driver)
    mock_driver.execute_script.return_value = None
    assert js_helper.get_referrer() == ''


def test_get_referrer_error(mock_driver):
    """Checks if get_referrer returns '' when an error occurs."""
    js_helper = JavaScript(mock_driver)
    mock_driver.execute_script.side_effect = Exception("Script execution failed")
    assert js_helper.get_referrer() == ''


def test_get_page_lang_valid(mock_driver):
    """Checks if get_page_lang returns the correct language code."""
    js_helper = JavaScript(mock_driver)
    mock_driver.execute_script.return_value = 'en-US'
    assert js_helper.get_page_lang() == 'en-US'


def test_get_page_lang_empty(mock_driver):
    """Checks if get_page_lang returns an empty string when no language code is available."""
    js_helper = JavaScript(mock_driver)
    mock_driver.execute_script.return_value = None
    assert js_helper.get_page_lang() == ''


def test_get_page_lang_error(mock_driver):
    """Checks if get_page_lang returns '' when an error occurs."""
    js_helper = JavaScript(mock_driver)
    mock_driver.execute_script.side_effect = Exception("Script execution failed")
    assert js_helper.get_page_lang() == ''
```