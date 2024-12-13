```python
import pytest
from unittest.mock import MagicMock, patch
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from src.webdriver.executor import ExecuteLocator
from src.logger.exceptions import WebDriverException, ExecuteLocatorException

@pytest.fixture
def mock_webdriver():
    """Provides a mock WebDriver instance."""
    mock_driver = MagicMock(spec=webdriver.Chrome)
    mock_element = MagicMock(spec=WebElement)
    mock_driver.find_element.return_value = mock_element
    mock_driver.find_elements.return_value = [mock_element]
    return mock_driver

@pytest.fixture
def executor(mock_webdriver):
    """Provides an instance of ExecuteLocator with a mock WebDriver."""
    return ExecuteLocator(mock_webdriver)

def test_execute_locator_no_action_success(executor, mock_webdriver):
    """Checks successful execution when no action is specified in locator."""
    locator = {"by": "id", "selector": "test_id"}
    result = executor.execute_locator(locator)
    assert isinstance(result, WebElement)
    mock_webdriver.find_element.assert_called_once_with(By.ID, "test_id")


def test_execute_locator_get_attribute_success(executor, mock_webdriver):
    """Checks successful execution when getting an attribute."""
    mock_element = mock_webdriver.find_element.return_value
    mock_element.get_attribute.return_value = "test_value"
    locator = {"by": "id", "selector": "test_id", "attribute": "value"}
    result = executor.execute_locator(locator)
    assert result == "test_value"
    mock_element.get_attribute.assert_called_once_with("value")

def test_execute_locator_send_keys_success(executor, mock_webdriver):
    """Checks successful execution of send_keys action."""
    mock_element = mock_webdriver.find_element.return_value
    locator = {"by": "id", "selector": "test_id", "action": "send_keys"}
    message = "test message"
    result = executor.execute_locator(locator, message=message)
    assert result is True
    mock_element.send_keys.assert_called_once_with(message)

def test_execute_locator_click_success(executor, mock_webdriver):
     """Checks successful execution of click action."""
     mock_element = mock_webdriver.find_element.return_value
     locator = {"by": "id", "selector": "test_id", "action": "click"}
     result = executor.execute_locator(locator)
     assert result is True
     mock_element.click.assert_called_once()


def test_execute_locator_invalid_action(executor):
    """Checks handling of an invalid action in the locator."""
    locator = {"by": "id", "selector": "test_id", "action": "invalid_action"}
    with pytest.raises(ExecuteLocatorException, match="invalid_action is not implemented"):
       executor.execute_locator(locator)

def test_execute_locator_no_such_element(executor, mock_webdriver):
    """Checks handling of NoSuchElementException."""
    mock_webdriver.find_element.side_effect = NoSuchElementException("Element not found")
    locator = {"by": "id", "selector": "test_id"}
    with pytest.raises(ExecuteLocatorException, match="Element not found"):
         executor.execute_locator(locator, continue_on_error=False)


def test_execute_locator_no_such_element_continue_on_error(executor, mock_webdriver):
    """Checks handling of NoSuchElementException and continue_on_error flag is True."""
    mock_webdriver.find_element.side_effect = NoSuchElementException("Element not found")
    locator = {"by": "id", "selector": "test_id"}
    result = executor.execute_locator(locator, continue_on_error=True)
    assert result is False


def test_execute_locator_timeout_exception(executor, mock_webdriver):
    """Checks handling of TimeoutException during wait."""
    mock_webdriver.find_element.side_effect = TimeoutException("Timeout")
    locator = {"by": "id", "selector": "test_id", "timeout": 1, "timeout_for_event": "presence_of_element_located"}
    with pytest.raises(ExecuteLocatorException, match="Timeout"):
        executor.execute_locator(locator, continue_on_error=False)

def test_execute_locator_timeout_exception_continue_on_error(executor, mock_webdriver):
    """Checks handling of TimeoutException during wait and continue_on_error flag is True."""
    mock_webdriver.find_element.side_effect = TimeoutException("Timeout")
    locator = {"by": "id", "selector": "test_id", "timeout": 1, "timeout_for_event": "presence_of_element_located"}
    result = executor.execute_locator(locator, continue_on_error=True)
    assert result is False

def test_get_webelement_by_locator_success(executor, mock_webdriver):
    """Checks successful retrieval of WebElement(s) by locator."""
    locator = {"by": "id", "selector": "test_id"}
    element = executor.get_webelement_by_locator(locator)
    assert isinstance(element, WebElement)
    mock_webdriver.find_element.assert_called_once_with(By.ID, "test_id")

    locator_multiple = {"by": "xpath", "selector": "//div"}
    elements = executor.get_webelement_by_locator(locator_multiple)
    assert isinstance(elements, list)
    assert len(elements) > 0
    mock_webdriver.find_elements.assert_called_once_with(By.XPATH, "//div")

def test_get_webelement_by_locator_not_found(executor, mock_webdriver):
    """Checks handling of element not found."""
    mock_webdriver.find_element.side_effect = NoSuchElementException("Element not found")
    locator = {"by": "id", "selector": "test_id"}
    result = executor.get_webelement_by_locator(locator)
    assert result is False

def test_get_attribute_by_locator_success(executor, mock_webdriver):
    """Checks successful retrieval of an element attribute."""
    mock_element = mock_webdriver.find_element.return_value
    mock_element.get_attribute.return_value = "test_attribute"
    locator = {"by": "id", "selector": "test_id", "attribute": "value"}
    attribute_value = executor.get_attribute_by_locator(locator)
    assert attribute_value == "test_attribute"
    mock_element.get_attribute.assert_called_once_with("value")

def test_get_attribute_by_locator_no_element(executor, mock_webdriver):
     """Checks handling of element not found during attribute retrieval."""
     mock_webdriver.find_element.side_effect = NoSuchElementException("Element not found")
     locator = {"by": "id", "selector": "test_id", "attribute": "value"}
     result = executor.get_attribute_by_locator(locator)
     assert result is False

def test_get_attribute_by_locator_no_attribute(executor, mock_webdriver):
    """Checks handling of no attribute."""
    mock_element = mock_webdriver.find_element.return_value
    mock_element.get_attribute.return_value = None
    locator = {"by": "id", "selector": "test_id", "attribute": "value"}
    result = executor.get_attribute_by_locator(locator)
    assert result is None
    mock_element.get_attribute.assert_called_once_with("value")

def test_send_message_success(executor, mock_webdriver):
    """Checks successful sending of message to an element."""
    mock_element = mock_webdriver.find_element.return_value
    locator = {"by": "id", "selector": "test_id"}
    message = "test message"
    result = executor.send_message(locator, message, 0,True)
    assert result is True
    mock_element.send_keys.assert_called_once_with(message)

def test_send_message_no_element(executor, mock_webdriver):
    """Checks handling of NoSuchElementException when sending a message."""
    mock_webdriver.find_element.side_effect = NoSuchElementException("Element not found")
    locator = {"by": "id", "selector": "test_id"}
    message = "test message"
    result = executor.send_message(locator, message, 0,True)
    assert result is False
    mock_webdriver.find_element.assert_called_once_with(By.ID, "test_id")

def test_evaluate_locator_str(executor):
    """Checks evaluation of a string attribute."""
    attribute = "test_string"
    result = executor.evaluate_locator(attribute)
    assert result == "test_string"

def test_evaluate_locator_list(executor):
    """Checks evaluation of a list attribute."""
    attribute = ["test_1", "test_2"]
    result = executor.evaluate_locator(attribute)
    assert result == "test_1 test_2"

def test_evaluate_locator_dict(executor):
    """Checks evaluation of a dictionary attribute."""
    attribute = {"key1": "value1", "key2": "value2"}
    result = executor.evaluate_locator(attribute)
    assert result == "value1 value2"


def test_evaluate_locator_empty_list(executor):
    """Checks evaluation of an empty list."""
    attribute = []
    result = executor.evaluate_locator(attribute)
    assert result == ""

def test_evaluate_locator_empty_dict(executor):
    """Checks evaluation of an empty dictionary."""
    attribute = {}
    result = executor.evaluate_locator(attribute)
    assert result == ""

def test__evaluate_valid_attribute(executor):
    """Checks _evaluate method with valid input."""
    attribute = "test_attribute"
    result = executor._evaluate(attribute)
    assert result == "test_attribute"

def test__evaluate_empty_attribute(executor):
    """Checks _evaluate method with empty input."""
    attribute = ""
    result = executor._evaluate(attribute)
    assert result is None

def test__evaluate_none_attribute(executor):
    """Checks _evaluate method with None input."""
    attribute = None
    result = executor._evaluate(attribute)
    assert result is None

def test_get_locator_keys():
    """Checks get_locator_keys method and return static list."""
    expected_keys = ['by', 'selector', 'selector 2', 'attribute', 'if_list', 'use_mouse', 'mandatory', 'timeout', 'timeout_for_event', 'event', 'action']
    assert ExecuteLocator.get_locator_keys() == expected_keys
```