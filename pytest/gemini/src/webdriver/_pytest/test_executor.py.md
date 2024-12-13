```python
import pytest
from unittest.mock import MagicMock, patch, create_autospec
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from src.webdriver.executor import ExecuteLocator
from src.logger.exceptions import ExecuteLocatorException

@pytest.fixture
def driver_mock():
    """Provides a mock WebDriver object."""
    return MagicMock()

@pytest.fixture
def execute_locator(driver_mock):
    """Provides an instance of ExecuteLocator with a mock WebDriver."""
    return ExecuteLocator(driver_mock)

def test_get_webelement_by_locator_single_element(execute_locator, driver_mock):
    """
    Test getting a single WebElement by locator.
    Verifies that the correct element is returned and find_elements is called correctly.
    """
    element = MagicMock(spec=WebElement)
    driver_mock.find_elements.return_value = [element]

    locator = {
        "by": "XPATH",
        "selector": "//div[@id='test']"
    }
    
    result = execute_locator.get_webelement_by_locator(locator)
    
    driver_mock.find_elements.assert_called_once_with(By.XPATH, "//div[@id='test']")
    assert result == element

def test_get_webelement_by_locator_multiple_elements(execute_locator, driver_mock):
    """
    Test getting multiple WebElements by locator.
    Verifies that the correct list of elements is returned and find_elements is called correctly.
    """
    elements = [MagicMock(spec=WebElement) for _ in range(3)]
    driver_mock.find_elements.return_value = elements

    locator = {
        "by": "XPATH",
        "selector": "//div[@class='test']"
    }

    result = execute_locator.get_webelement_by_locator(locator)
    
    driver_mock.find_elements.assert_called_once_with(By.XPATH, "//div[@class='test']")
    assert result == elements

def test_get_webelement_by_locator_no_element(execute_locator, driver_mock):
    """
    Test getting no WebElement when the element is not found.
    Verifies that False is returned and find_elements is called correctly.
    """
    driver_mock.find_elements.return_value = []

    locator = {
        "by": "XPATH",
        "selector": "//div[@id='not_exist']"
    }

    result = execute_locator.get_webelement_by_locator(locator)
    
    driver_mock.find_elements.assert_called_once_with(By.XPATH, "//div[@id='not_exist']")
    assert result is False

def test_get_attribute_by_locator(execute_locator, driver_mock):
    """
    Test getting an attribute of a WebElement by locator.
    Verifies that the correct attribute value is returned, find_elements and get_attribute are called correctly.
    """
    element = MagicMock(spec=WebElement)
    element.get_attribute.return_value = "test_value"
    driver_mock.find_elements.return_value = [element]

    locator = {
        "by": "XPATH",
        "selector": "//div[@id='test']",
        "attribute": "data-test"
    }

    result = execute_locator.get_attribute_by_locator(locator)
    
    driver_mock.find_elements.assert_called_once_with(By.XPATH, "//div[@id='test']")
    element.get_attribute.assert_called_once_with("data-test")
    assert result == "test_value"

def test_get_attribute_by_locator_element_not_found(execute_locator, driver_mock):
    """
    Test getting an attribute when the element is not found, should return False.
    """
    driver_mock.find_elements.return_value = []
    locator = {
        "by": "XPATH",
        "selector": "//div[@id='not_exist']",
        "attribute": "data-test"
    }

    result = execute_locator.get_attribute_by_locator(locator)
    driver_mock.find_elements.assert_called_once_with(By.XPATH, "//div[@id='not_exist']")
    assert result is False


def test_send_message(execute_locator, driver_mock):
    """
    Test sending a message to a WebElement by locator.
    Verifies that the message is sent correctly and find_elements, send_keys are called correctly.
    """
    element = MagicMock(spec=WebElement)
    driver_mock.find_elements.return_value = [element]

    locator = {
        "by": "XPATH",
        "selector": "//input[@id='test']"
    }
    message = "Hello World"

    result = execute_locator.send_message(locator, message, typing_speed=0, continue_on_error=True)
    
    driver_mock.find_elements.assert_called_once_with(By.XPATH, "//input[@id='test']")
    element.send_keys.assert_called_once_with(message)
    assert result is True

def test_send_message_element_not_found(execute_locator, driver_mock):
    """
    Test sending a message when the element is not found, should return False.
    """
    driver_mock.find_elements.return_value = []

    locator = {
        "by": "XPATH",
        "selector": "//input[@id='not_exist']"
    }
    message = "Hello World"
    result = execute_locator.send_message(locator, message, typing_speed=0, continue_on_error=True)
    driver_mock.find_elements.assert_called_once_with(By.XPATH, "//input[@id='not_exist']")
    assert result is False


def test_send_message_typing_speed(execute_locator, driver_mock):
    """
    Test sending a message with a typing speed to a WebElement by locator.
    Verifies that the message is sent with a delay, find_elements and send_keys are called correctly and the time.sleep is called as expected.
    """
    element = MagicMock(spec=WebElement)
    driver_mock.find_elements.return_value = [element]

    locator = {
        "by": "XPATH",
        "selector": "//input[@id='test']"
    }
    message = "Hello"
    typing_speed = 0.1

    with patch('time.sleep', return_value=None) as mock_sleep:
        result = execute_locator.send_message(locator, message, typing_speed=typing_speed, continue_on_error=True)
    
    driver_mock.find_elements.assert_called_once_with(By.XPATH, "//input[@id='test']")
    assert element.send_keys.call_count == len(message)
    mock_sleep.assert_called_with(typing_speed)
    assert result is True

def test_send_message_with_exception(execute_locator, driver_mock):
    """
    Test send message when send_keys raises an exception with continue_on_error=True, should return False and not raise an exception.
    """
    element = MagicMock(spec=WebElement)
    driver_mock.find_elements.return_value = [element]
    element.send_keys.side_effect = Exception("Error sending message")

    locator = {
        "by": "XPATH",
        "selector": "//input[@id='test']"
    }
    message = "Hello"
    result = execute_locator.send_message(locator, message, typing_speed=0, continue_on_error=True)
    assert result is False
    
def test_send_message_with_exception_no_continue(execute_locator, driver_mock):
    """
    Test send message when send_keys raises an exception with continue_on_error=False, should raise an exception.
    """
    element = MagicMock(spec=WebElement)
    driver_mock.find_elements.return_value = [element]
    element.send_keys.side_effect = Exception("Error sending message")

    locator = {
        "by": "XPATH",
        "selector": "//input[@id='test']"
    }
    message = "Hello"
    with pytest.raises(Exception, match="Error sending message"):
       execute_locator.send_message(locator, message, typing_speed=0, continue_on_error=False)
```