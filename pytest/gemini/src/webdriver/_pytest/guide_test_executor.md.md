```python
import pytest
from unittest.mock import MagicMock, patch
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

from src.webdriver.executor import ExecuteLocator
from src.logger.exceptions import ExecuteLocatorException

@pytest.fixture
def driver_mock():
    """Provides a mock WebDriver object."""
    return MagicMock()

@pytest.fixture
def execute_locator(driver_mock):
    """Provides an instance of ExecuteLocator with the mock driver."""
    return ExecuteLocator(driver_mock)

# Tests for get_webelement_by_locator
def test_get_webelement_by_locator_single_element(execute_locator, driver_mock):
    """Checks if the method correctly returns a single WebElement."""
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
    """Checks if the method correctly returns a list of WebElements when multiple are found."""
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
    """Checks if the method returns False when no element is found."""
    driver_mock.find_elements.return_value = []

    locator = {
        "by": "XPATH",
        "selector": "//div[@id='not_exist']"
    }

    result = execute_locator.get_webelement_by_locator(locator)
    
    driver_mock.find_elements.assert_called_once_with(By.XPATH, "//div[@id='not_exist']")
    assert result is False

def test_get_webelement_by_locator_invalid_locator(execute_locator, driver_mock):
    """Checks if the method handles an invalid locator by raising an exception."""
    locator = {
        "by": "INVALID",
        "selector": "//div[@id='test']"
    }
    with pytest.raises(ExecuteLocatorException, match="Unsupported locator type: INVALID"):
        execute_locator.get_webelement_by_locator(locator)
    
    driver_mock.find_elements.assert_not_called()


# Tests for get_attribute_by_locator
def test_get_attribute_by_locator(execute_locator, driver_mock):
    """Checks if the method correctly retrieves an attribute of a WebElement."""
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
    
def test_get_attribute_by_locator_no_element(execute_locator, driver_mock):
    """Checks if the method returns False when no element is found."""
    driver_mock.find_elements.return_value = []

    locator = {
        "by": "XPATH",
        "selector": "//div[@id='not_exist']",
        "attribute": "data-test"
    }

    result = execute_locator.get_attribute_by_locator(locator)
    
    driver_mock.find_elements.assert_called_once_with(By.XPATH, "//div[@id='not_exist']")
    assert result is False

def test_get_attribute_by_locator_no_attribute(execute_locator, driver_mock):
    """Checks if the method raises exception when no attribute specified."""
    element = MagicMock(spec=WebElement)
    driver_mock.find_elements.return_value = [element]
    locator = {
        "by": "XPATH",
        "selector": "//div[@id='test']"
    }
    with pytest.raises(ExecuteLocatorException, match="Attribute name is missing"):
         execute_locator.get_attribute_by_locator(locator)

# Tests for send_message
def test_send_message(execute_locator, driver_mock):
    """Checks if the method correctly sends a message to a WebElement."""
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

def test_send_message_typing_speed(execute_locator, driver_mock):
    """Checks if the method correctly sends a message with typing speed."""
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
    
def test_send_message_no_element(execute_locator, driver_mock):
    """Checks if the method returns False when no element is found."""
    driver_mock.find_elements.return_value = []

    locator = {
        "by": "XPATH",
        "selector": "//input[@id='not_exist']"
    }
    message = "Hello"

    result = execute_locator.send_message(locator, message, typing_speed=0, continue_on_error=True)
    
    driver_mock.find_elements.assert_called_once_with(By.XPATH, "//input[@id='not_exist']")
    assert result is False
```