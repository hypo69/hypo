```python
import pytest
from unittest.mock import MagicMock, patch
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from src.webdriver.executor import ExecuteLocator
from src.logger.exceptions import WebDriverException, ExecuteLocatorException
from types import SimpleNamespace

# Fixtures
@pytest.fixture
def mock_webdriver():
    """Provides a mock WebDriver instance for testing."""
    mock_driver = MagicMock(spec=webdriver.Chrome)
    mock_element = MagicMock(spec=WebElement)
    mock_driver.find_element.return_value = mock_element
    mock_driver.find_elements.return_value = [mock_element]
    return mock_driver

@pytest.fixture
def execute_locator(mock_webdriver):
    """Provides an instance of ExecuteLocator with a mock WebDriver."""
    return ExecuteLocator(mock_webdriver)

@pytest.fixture
def sample_locator():
    """Provides a sample locator dictionary for testing."""
    return {
        "by": "xpath",
        "selector": "//div[@id='test']",
        "attribute": "text",
        "timeout": 10,
        "timeout_for_event": "presence_of_element_located",
        "event": None,
        "if_list": "first",
        "use_mouse": False,
        "mandatory": True
    }

@pytest.fixture
def sample_locator_list():
    """Provides a sample locator dictionary for testing list elements."""
    return {
        "by": "xpath",
        "selector": "//div[@class='test']",
        "attribute": "text",
        "timeout": 10,
        "timeout_for_event": "presence_of_element_located",
        "event": None,
        "if_list": "all",
        "use_mouse": False,
        "mandatory": True
    }


# Tests for __init__ method
def test_init_sets_driver_and_actions(mock_webdriver):
    """Checks if the driver and action chains are set correctly during initialization."""
    executor = ExecuteLocator(mock_webdriver)
    assert executor.driver == mock_webdriver
    assert isinstance(executor.actions, ActionChains)


# Tests for execute_locator method
def test_execute_locator_valid_locator(execute_locator, mock_webdriver, sample_locator):
    """Checks correct execution with a valid locator dictionary."""
    mock_element = MagicMock(spec=WebElement)
    mock_element.get_attribute.return_value = "test attribute"
    mock_webdriver.find_element.return_value = mock_element

    result = execute_locator.execute_locator(sample_locator)
    assert result == "test attribute"
    mock_webdriver.find_element.assert_called_once_with(By.XPATH, "//div[@id='test']")
    mock_element.get_attribute.assert_called_once_with("text")


def test_execute_locator_with_message(execute_locator, mock_webdriver, sample_locator):
    """Checks if a message is sent using the send_message method."""
    mock_element = MagicMock(spec=WebElement)
    mock_webdriver.find_element.return_value = mock_element
    with patch.object(execute_locator, 'send_message', return_value=True) as mock_send:
       execute_locator.execute_locator({**sample_locator, 'message':'test message'}, 'test message')
       mock_send.assert_called_once_with({**sample_locator, 'message':'test message'}, 'test message', 0, True)

def test_execute_locator_no_element_found(execute_locator, mock_webdriver, sample_locator):
    """Checks correct handling when no element is found."""
    mock_webdriver.find_element.side_effect = NoSuchElementException()
    with pytest.raises(ExecuteLocatorException):
        execute_locator.execute_locator(sample_locator)
    mock_webdriver.find_element.assert_called_once_with(By.XPATH, "//div[@id='test']")
   

def test_execute_locator_timeout(execute_locator, mock_webdriver, sample_locator):
      """Checks correct handling when a timeout exception occurs"""
      mock_webdriver.find_element.side_effect = TimeoutException()
      with pytest.raises(ExecuteLocatorException):
          execute_locator.execute_locator(sample_locator)
      mock_webdriver.find_element.assert_called_once_with(By.XPATH, "//div[@id='test']")



# Tests for get_webelement_by_locator method
def test_get_webelement_by_locator_finds_element(execute_locator, mock_webdriver, sample_locator):
    """Checks if get_webelement_by_locator correctly retrieves a web element."""
    mock_element = MagicMock(spec=WebElement)
    mock_webdriver.find_element.return_value = mock_element
    result = execute_locator.get_webelement_by_locator(sample_locator)
    assert result == mock_element
    mock_webdriver.find_element.assert_called_once_with(By.XPATH, "//div[@id='test']")


def test_get_webelement_by_locator_returns_false_when_no_element(execute_locator, mock_webdriver, sample_locator):
    """Checks that get_webelement_by_locator returns False when the element is not found."""
    mock_webdriver.find_element.side_effect = NoSuchElementException()
    result = execute_locator.get_webelement_by_locator(sample_locator)
    assert result is False
    mock_webdriver.find_element.assert_called_once_with(By.XPATH, "//div[@id='test']")


def test_get_webelement_by_locator_returns_list_of_elements(execute_locator, mock_webdriver, sample_locator_list):
    """Checks that get_webelement_by_locator returns list of elements."""
    mock_element = MagicMock(spec=WebElement)
    mock_webdriver.find_elements.return_value = [mock_element]
    result = execute_locator.get_webelement_by_locator(sample_locator_list)
    assert result == [mock_element]
    mock_webdriver.find_elements.assert_called_once_with(By.XPATH, "//div[@class='test']")



# Tests for get_attribute_by_locator method
def test_get_attribute_by_locator_returns_attribute(execute_locator, mock_webdriver, sample_locator):
    """Checks that get_attribute_by_locator returns the attribute of an element."""
    mock_element = MagicMock(spec=WebElement)
    mock_element.get_attribute.return_value = "test attribute"
    mock_webdriver.find_element.return_value = mock_element
    result = execute_locator.get_attribute_by_locator(sample_locator)
    assert result == "test attribute"
    mock_element.get_attribute.assert_called_once_with("text")


def test_get_attribute_by_locator_no_element(execute_locator, mock_webdriver, sample_locator):
      """Checks that get_attribute_by_locator returns False if no element is found."""
      mock_webdriver.find_element.side_effect = NoSuchElementException()
      result = execute_locator.get_attribute_by_locator(sample_locator)
      assert result is False
      mock_webdriver.find_element.assert_called_once_with(By.XPATH, "//div[@id='test']")


def test_get_attribute_by_locator_returns_list_of_attributes(execute_locator, mock_webdriver, sample_locator_list):
    """Checks that get_attribute_by_locator returns a list of attributes."""
    mock_element1 = MagicMock(spec=WebElement)
    mock_element2 = MagicMock(spec=WebElement)
    mock_element1.get_attribute.return_value = "test attribute 1"
    mock_element2.get_attribute.return_value = "test attribute 2"
    mock_webdriver.find_elements.return_value = [mock_element1,mock_element2]

    result = execute_locator.get_attribute_by_locator(sample_locator_list)
    assert result == ["test attribute 1","test attribute 2"]
    mock_webdriver.find_elements.assert_called_once_with(By.XPATH, "//div[@class='test']")


# Tests for _get_element_attribute method
def test_get_element_attribute_returns_attribute(execute_locator, mock_webdriver):
    """Checks if _get_element_attribute returns the correct attribute."""
    mock_element = MagicMock(spec=WebElement)
    mock_element.get_attribute.return_value = "test attribute"
    result = execute_locator._get_element_attribute(mock_element, "test_attr")
    assert result == "test attribute"
    mock_element.get_attribute.assert_called_once_with("test_attr")


def test_get_element_attribute_returns_none_on_exception(execute_locator, mock_webdriver):
    """Checks if _get_element_attribute returns None when get_attribute raises an exception."""
    mock_element = MagicMock(spec=WebElement)
    mock_element.get_attribute.side_effect = Exception()
    result = execute_locator._get_element_attribute(mock_element, "test_attr")
    assert result is None
    mock_element.get_attribute.assert_called_once_with("test_attr")


# Tests for send_message method
def test_send_message_sends_message(execute_locator, mock_webdriver, sample_locator):
    """Checks if send_message sends the message correctly."""
    mock_element = MagicMock(spec=WebElement)
    mock_webdriver.find_element.return_value = mock_element
    result = execute_locator.send_message(sample_locator, "test message", 0, True)
    assert result is True
    mock_element.send_keys.assert_called_once_with("test message")

def test_send_message_no_element(execute_locator, mock_webdriver, sample_locator):
      """Checks that send_message returns False if no element is found."""
      mock_webdriver.find_element.side_effect = NoSuchElementException()
      result = execute_locator.send_message(sample_locator, "test message", 0, True)
      assert result is False
      mock_webdriver.find_element.assert_called_once_with(By.XPATH, "//div[@id='test']")


def test_send_message_typing_speed(execute_locator, mock_webdriver, sample_locator):
    """Checks if send_message sends the message correctly using typing speed."""
    mock_element = MagicMock(spec=WebElement)
    mock_webdriver.find_element.return_value = mock_element
    with patch('time.sleep') as mock_sleep:
        result = execute_locator.send_message(sample_locator, "test", 0.1, True)
        assert result is True
        assert mock_element.send_keys.call_count == 4
        mock_sleep.assert_called()
        assert mock_sleep.call_count == 3

# Tests for evaluate_locator method
def test_evaluate_locator_returns_string(execute_locator):
    """Checks if evaluate_locator returns the string input."""
    result = execute_locator.evaluate_locator("test_string")
    assert result == "test_string"

def test_evaluate_locator_evaluates_placeholder(execute_locator):
    """Checks if evaluate_locator evaluates a placeholder string"""
    with patch.object(execute_locator, '_evaluate', return_value="eval_result") as mock_evaluate:
        result = execute_locator.evaluate_locator("%test_placeholder%")
        mock_evaluate.assert_called_once_with("test_placeholder")
        assert result == "eval_result"


def test_evaluate_locator_returns_list(execute_locator):
    """Checks if evaluate_locator returns the string input."""
    result = execute_locator.evaluate_locator(["test_string1","test_string2"])
    assert result == "['test_string1', 'test_string2']"

def test_evaluate_locator_returns_dict(execute_locator):
    """Checks if evaluate_locator returns the string input."""
    result = execute_locator.evaluate_locator({"test_string1":"value1","test_string2":"value2"})
    assert result == "{'test_string1': 'value1', 'test_string2': 'value2'}"


# Tests for _evaluate method
def test_evaluate_returns_string(execute_locator):
    """Checks if _evaluate returns the string input."""
    result = execute_locator._evaluate("test_string")
    assert result == "test_string"

def test_evaluate_returns_none_invalid_placeholder(execute_locator):
    """Checks if _evaluate returns None for invalid placeholders."""
    result = execute_locator._evaluate("invalid_placeholder")
    assert result is None


# Tests for get_locator_keys method
def test_get_locator_keys_returns_list():
    """Checks if get_locator_keys returns a list of keys."""
    keys = ExecuteLocator.get_locator_keys()
    assert isinstance(keys, list)


def test_click_element_success(execute_locator, mock_webdriver, sample_locator):
    """Test case for successful click element with navigation."""
    mock_element = MagicMock(spec=WebElement)
    mock_webdriver.find_element.return_value = mock_element
    mock_element.click.return_value = None
    result = execute_locator.click(sample_locator)
    assert result is True
    mock_element.click.assert_called_once()

def test_click_element_fails(execute_locator, mock_webdriver, sample_locator):
    """Test case for click failure when element is not clickable."""
    mock_element = MagicMock(spec=WebElement)
    mock_webdriver.find_element.return_value = mock_element
    mock_element.click.side_effect = Exception("Click failed")
    with pytest.raises(ExecuteLocatorException):
        execute_locator.click(sample_locator)
    mock_element.click.assert_called_once()


def test_get_webelement_as_screenshot_success(execute_locator, mock_webdriver, sample_locator):
    """Test case for get_webelement_as_screenshot successful single element screenshot."""
    mock_element = MagicMock(spec=WebElement)
    mock_webdriver.find_element.return_value = mock_element
    mock_element.screenshot_as_png = b'mock_png_data'

    result = execute_locator.get_webelement_as_screenshot(sample_locator)
    assert result == b'mock_png_data'
    mock_element.screenshot_as_png

def test_get_webelement_as_screenshot_element_not_found(execute_locator, mock_webdriver, sample_locator):
    """Test case for get_webelement_as_screenshot element not found."""
    mock_webdriver.find_element.side_effect = NoSuchElementException()

    result = execute_locator.get_webelement_as_screenshot(sample_locator)
    assert result is False

def test_get_webelement_as_screenshot_fails(execute_locator, mock_webdriver, sample_locator):
      """Test case for get_webelement_as_screenshot screenshot fails."""
      mock_element = MagicMock(spec=WebElement)
      mock_webdriver.find_element.return_value = mock_element
      mock_element.screenshot_as_png = Exception("Screenshot failed")
      with pytest.raises(ExecuteLocatorException):
          execute_locator.get_webelement_as_screenshot(sample_locator)
      mock_element.screenshot_as_png

def test_get_webelement_as_screenshot_list_elements(execute_locator, mock_webdriver, sample_locator_list):
    """Test case for get_webelement_as_screenshot multiple elements screenshot."""
    mock_element1 = MagicMock(spec=WebElement)
    mock_element2 = MagicMock(spec=WebElement)
    mock_webdriver.find_elements.return_value = [mock_element1,mock_element2]
    mock_element1.screenshot_as_png = b'mock_png_data1'
    mock_element2.screenshot_as_png = b'mock_png_data2'

    result = execute_locator.get_webelement_as_screenshot(sample_locator_list)
    assert result == [b'mock_png_data1', b'mock_png_data2']
    mock_webdriver.find_elements.assert_called_once()
    mock_element1.screenshot_as_png
    mock_element2.screenshot_as_png
```