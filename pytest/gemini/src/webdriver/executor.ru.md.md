```python
import pytest
from unittest.mock import MagicMock, patch
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from types import SimpleNamespace
from src.webdriver.executor import ExecuteLocator


@pytest.fixture
def mock_driver():
    """Provides a mock WebDriver instance."""
    driver = MagicMock(spec=WebDriver)
    driver.find_element.return_value = MagicMock()
    driver.find_elements.return_value = [MagicMock(), MagicMock()]
    return driver

@pytest.fixture
def executor(mock_driver):
    """Provides an instance of ExecuteLocator with the mock WebDriver."""
    return ExecuteLocator(driver=mock_driver)


@pytest.fixture
def sample_locator_dict():
    """Provides a sample locator dictionary."""
    return {"by": "id", "selector": "test_id"}

@pytest.fixture
def sample_locator_simple_namespace(sample_locator_dict):
    """Provides a sample locator as SimpleNamespace."""
    return SimpleNamespace(**sample_locator_dict)


def test_execute_locator_with_dict(executor, mock_driver, sample_locator_dict):
    """Tests execute_locator with a locator dictionary."""
    mock_element = MagicMock()
    mock_driver.find_element.return_value = mock_element
    result = executor.execute_locator(sample_locator_dict)
    assert result is not None
    mock_driver.find_element.assert_called_once_with(By.ID, "test_id")

def test_execute_locator_with_simple_namespace(executor, mock_driver, sample_locator_simple_namespace):
    """Tests execute_locator with a locator SimpleNamespace."""
    mock_element = MagicMock()
    mock_driver.find_element.return_value = mock_element
    result = executor.execute_locator(sample_locator_simple_namespace)
    assert result is not None
    mock_driver.find_element.assert_called_once_with(By.ID, "test_id")


def test_execute_locator_with_event(executor, mock_driver, sample_locator_dict):
    """Tests execute_locator with an event."""
    mock_element = MagicMock()
    mock_driver.find_element.return_value = mock_element
    locator = sample_locator_dict.copy()
    locator['event'] = 'click()'
    result = executor.execute_locator(locator)
    assert result is not None
    mock_element.click.assert_called_once()

def test_execute_locator_with_attribute(executor, mock_driver, sample_locator_dict):
     """Tests execute_locator with an attribute."""
     mock_element = MagicMock()
     mock_driver.find_element.return_value = mock_element
     locator = sample_locator_dict.copy()
     locator['attribute'] = 'text'
     mock_element.text = "test text"
     result = executor.execute_locator(locator)
     assert result == "test text"


def test_execute_locator_no_element_found(executor, mock_driver, sample_locator_dict):
    """Tests execute_locator when no element is found."""
    mock_driver.find_element.side_effect = Exception("Element not found")
    result = executor.execute_locator(sample_locator_dict)
    assert result is None


def test_execute_locator_with_invalid_locator_type(executor):
    """Tests execute_locator with an invalid locator type."""
    with pytest.raises(AttributeError):
      executor.execute_locator(locator=123)


def test_evaluate_locator_single_attribute(executor, mock_driver, sample_locator_dict):
    """Tests evaluate_locator with a single attribute."""
    mock_element = MagicMock()
    mock_driver.find_element.return_value = mock_element
    mock_element.text = "test text"
    locator = sample_locator_dict.copy()
    locator['attribute'] = 'text'
    result = executor.evaluate_locator(locator)
    assert result == "test text"

def test_evaluate_locator_list_of_attributes(executor, mock_driver, sample_locator_dict):
    """Tests evaluate_locator with a list of attributes."""
    mock_element = MagicMock()
    mock_driver.find_element.return_value = mock_element
    mock_element.get_attribute.side_effect = lambda attr: f"value_{attr}"
    locator = sample_locator_dict.copy()
    locator['attribute'] = ['text', 'class']
    result = executor.evaluate_locator(locator)
    assert result == ["value_text", "value_class"]

def test_get_attribute_by_locator_single_element(executor, mock_driver, sample_locator_dict):
    """Tests get_attribute_by_locator for a single element."""
    mock_element = MagicMock()
    mock_driver.find_element.return_value = mock_element
    mock_element.get_attribute.return_value = "test_attribute"
    locator = sample_locator_dict.copy()
    locator['attribute'] = 'text'
    result = executor.get_attribute_by_locator(locator)
    assert result == "test_attribute"

def test_get_attribute_by_locator_list_of_elements(executor, mock_driver, sample_locator_dict):
    """Tests get_attribute_by_locator for a list of elements."""
    mock_elements = [MagicMock(), MagicMock()]
    mock_driver.find_elements.return_value = mock_elements
    for i, el in enumerate(mock_elements):
         el.get_attribute.return_value = f"test_attribute_{i}"
    locator = sample_locator_dict.copy()
    locator['selector'] = "test_elements"
    locator['by'] = "class name"
    locator['attribute'] = 'text'
    result = executor.get_attribute_by_locator(locator)
    assert result == ["test_attribute_0", "test_attribute_1"]

def test_get_attribute_by_locator_attribute_as_dict_string(executor, mock_driver, sample_locator_dict):
    """Tests get_attribute_by_locator when attribute is a dictionary-like string."""
    mock_element = MagicMock()
    mock_driver.find_element.return_value = mock_element
    mock_element.get_attribute.return_value = "value_1"
    locator = sample_locator_dict.copy()
    locator['attribute'] = '{"text": null}'
    result = executor.get_attribute_by_locator(locator)
    assert result == "value_1"

def test_get_attribute_by_locator_element_not_found(executor, mock_driver, sample_locator_dict):
    """Tests get_attribute_by_locator when element not found."""
    mock_driver.find_element.side_effect = Exception("Element not found")
    locator = sample_locator_dict.copy()
    locator['attribute'] = 'text'
    result = executor.get_attribute_by_locator(locator)
    assert result is None

def test_get_webelement_by_locator_single_element(executor, mock_driver, sample_locator_dict):
    """Tests get_webelement_by_locator for a single element."""
    mock_element = MagicMock()
    mock_driver.find_element.return_value = mock_element
    result = executor.get_webelement_by_locator(sample_locator_dict)
    assert result == mock_element
    mock_driver.find_element.assert_called_once_with(By.ID, "test_id")

def test_get_webelement_by_locator_multiple_elements(executor, mock_driver, sample_locator_dict):
    """Tests get_webelement_by_locator for multiple elements."""
    mock_elements = [MagicMock(), MagicMock()]
    mock_driver.find_elements.return_value = mock_elements
    locator = sample_locator_dict.copy()
    locator['selector'] = "test_elements"
    locator['by'] = "class name"
    result = executor.get_webelement_by_locator(locator)
    assert result == mock_elements
    mock_driver.find_elements.assert_called_once_with(By.CLASS_NAME, "test_elements")


def test_get_webelement_by_locator_no_element_found(executor, mock_driver, sample_locator_dict):
    """Tests get_webelement_by_locator when no element is found."""
    mock_driver.find_element.side_effect = Exception("Element not found")
    result = executor.get_webelement_by_locator(sample_locator_dict)
    assert result is None


def test_get_webelement_as_screenshot(executor, mock_driver, sample_locator_dict):
    """Tests get_webelement_as_screenshot."""
    mock_element = MagicMock()
    mock_driver.find_element.return_value = mock_element
    mock_element.screenshot.return_value = b'test_screenshot_data'
    result = executor.get_webelement_as_screenshot(sample_locator_dict)
    assert result == b'test_screenshot_data'
    mock_element.screenshot.assert_called_once()

def test_get_webelement_as_screenshot_element_not_found(executor, mock_driver, sample_locator_dict):
    """Tests get_webelement_as_screenshot when element is not found."""
    mock_driver.find_element.side_effect = Exception("Element not found")
    result = executor.get_webelement_as_screenshot(sample_locator_dict)
    assert result is None
    

def test_execute_event(executor, mock_driver, sample_locator_dict):
    """Tests execute_event."""
    mock_element = MagicMock()
    mock_driver.find_element.return_value = mock_element
    locator = sample_locator_dict.copy()
    locator['event'] = 'click()'
    result = executor.execute_event(locator)
    assert result is None
    mock_element.click.assert_called_once()

def test_execute_event_element_not_found(executor, mock_driver, sample_locator_dict):
    """Tests execute_event when element is not found."""
    mock_driver.find_element.side_effect = Exception("Element not found")
    locator = sample_locator_dict.copy()
    locator['event'] = 'click()'
    result = executor.execute_event(locator)
    assert result is None


def test_send_message(executor, mock_driver, sample_locator_dict):
    """Tests send_message."""
    mock_element = MagicMock()
    mock_driver.find_element.return_value = mock_element
    message = "test message"
    executor.send_message(sample_locator_dict, message)
    mock_element.send_keys.assert_called_once_with(message)

def test_send_message_element_not_found(executor, mock_driver, sample_locator_dict):
    """Tests send_message when element not found."""
    mock_driver.find_element.side_effect = Exception("Element not found")
    message = "test message"
    executor.send_message(sample_locator_dict, message)
    mock_driver.find_element.assert_called_once()
    
def test_execute_locator_with_custom_by_mapping(mock_driver):
    """Tests execute_locator with a custom by mapping."""
    custom_by_mapping = {"custom_type": By.CLASS_NAME}
    executor = ExecuteLocator(driver=mock_driver, by_mapping=custom_by_mapping)
    locator = {"by": "custom_type", "selector": "test_class"}
    mock_element = MagicMock()
    mock_driver.find_element.return_value = mock_element

    executor.execute_locator(locator)
    mock_driver.find_element.assert_called_once_with(By.CLASS_NAME, "test_class")
```