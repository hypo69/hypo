```python
import pytest
from unittest.mock import MagicMock, AsyncMock
from types import SimpleNamespace
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import asyncio
from src.webdriver.executor import ExecuteLocator

# Fixture for creating a mock WebDriver instance
@pytest.fixture
def mock_driver():
    """Provides a mock WebDriver instance."""
    mock_driver = MagicMock(spec=WebDriver)
    mock_driver.execute_script = AsyncMock()
    return mock_driver

# Fixture for creating an instance of ExecuteLocator
@pytest.fixture
def executor(mock_driver):
    """Provides an instance of ExecuteLocator with a mock driver."""
    return ExecuteLocator(driver=mock_driver, mode='dev')


@pytest.mark.asyncio
async def test_execute_locator_with_simple_namespace(executor, mock_driver):
    """Tests execute_locator with a SimpleNamespace locator."""
    locator = SimpleNamespace(by="ID", selector="some_id", event="click()")
    mock_element = MagicMock()
    mock_driver.find_element.return_value = mock_element
    
    result = await executor.execute_locator(locator)
    
    mock_driver.find_element.assert_called_once_with(By.ID, "some_id")
    mock_element.click.assert_called_once()
    assert result is None  # Corrected assertion to check for None

@pytest.mark.asyncio
async def test_execute_locator_with_dict(executor, mock_driver):
    """Tests execute_locator with a dictionary locator."""
    locator = {"by": "CSS_SELECTOR", "selector": ".some_class", "attribute": "text"}
    mock_element = MagicMock()
    mock_element.text = "Some Text"
    mock_driver.find_element.return_value = mock_element
    
    result = await executor.execute_locator(locator)
    
    mock_driver.find_element.assert_called_once_with(By.CSS_SELECTOR, ".some_class")
    assert result == "Some Text"

@pytest.mark.asyncio
async def test_execute_locator_no_action(executor, mock_driver):
    """Tests execute_locator with no action specified."""
    locator = {"by": "XPATH", "selector": "//some/xpath"}
    mock_element = MagicMock()
    mock_driver.find_element.return_value = mock_element
    
    result = await executor.execute_locator(locator)
    
    mock_driver.find_element.assert_called_once_with(By.XPATH, "//some/xpath")
    assert result == mock_element  # Check that it returns the web element

@pytest.mark.asyncio
async def test_execute_locator_element_not_found(executor, mock_driver):
    """Tests execute_locator when an element is not found."""
    locator = {"by": "ID", "selector": "non_existent_id", "event":"click()"}
    mock_driver.find_element.side_effect = Exception("Element not found")
    
    result = await executor.execute_locator(locator)
    
    mock_driver.find_element.assert_called_once_with(By.ID, "non_existent_id")
    assert result is None  # Should return None when element not found and exception is handled


@pytest.mark.asyncio
async def test_execute_locator_invalid_locator_type(executor):
    """Tests execute_locator with an invalid locator type."""
    locator = {"by": "INVALID_TYPE", "selector": "some_selector"}
    
    with pytest.raises(AttributeError):
        await executor.execute_locator(locator)

@pytest.mark.asyncio
async def test_evaluate_locator_single_attribute(executor, mock_driver):
    """Tests evaluate_locator with a single attribute."""
    mock_element = MagicMock()
    mock_element.get_attribute.return_value = "attribute_value"
    mock_driver.find_element.return_value = mock_element
    locator = SimpleNamespace(by="ID", selector="some_id", attribute="some_attribute")
    
    result = await executor.evaluate_locator(locator)
    
    mock_driver.find_element.assert_called_once_with(By.ID, "some_id")
    mock_element.get_attribute.assert_called_once_with("some_attribute")
    assert result == "attribute_value"

@pytest.mark.asyncio
async def test_evaluate_locator_list_of_attributes(executor, mock_driver):
   """Tests evaluate_locator with a list of attributes."""
   mock_element = MagicMock()
   mock_element.get_attribute.side_effect = ["attr1", "attr2"]
   mock_driver.find_element.return_value = mock_element
   locator = SimpleNamespace(by="ID", selector="some_id", attribute=["attr1", "attr2"])

   result = await executor.evaluate_locator(locator)
   
   mock_driver.find_element.assert_called_once_with(By.ID, "some_id")
   assert mock_element.get_attribute.call_count == 2
   assert result == ["attr1", "attr2"]

@pytest.mark.asyncio
async def test_get_attribute_by_locator_single_element(executor, mock_driver):
    """Tests get_attribute_by_locator for a single element."""
    mock_element = MagicMock()
    mock_element.get_attribute.return_value = "test_value"
    mock_driver.find_element.return_value = mock_element
    locator = {"by": "ID", "selector": "element_id", "attribute": "test_attribute"}
    
    result = await executor.get_attribute_by_locator(locator)
    
    mock_driver.find_element.assert_called_once_with(By.ID, "element_id")
    mock_element.get_attribute.assert_called_once_with("test_attribute")
    assert result == "test_value"

@pytest.mark.asyncio
async def test_get_attribute_by_locator_list_of_elements(executor, mock_driver):
    """Tests get_attribute_by_locator for a list of elements."""
    mock_elements = [MagicMock(get_attribute=MagicMock(return_value=f"value_{i}")) for i in range(2)]
    mock_driver.find_elements.return_value = mock_elements
    locator = {"by": "CLASS_NAME", "selector": "test_class", "attribute": "test_attribute"}
    
    result = await executor.get_attribute_by_locator(locator)

    mock_driver.find_elements.assert_called_once_with(By.CLASS_NAME, "test_class")
    for element in mock_elements:
         element.get_attribute.assert_called_once_with("test_attribute")
    assert result == ["value_0", "value_1"]

@pytest.mark.asyncio
async def test_get_attribute_by_locator_element_not_found(executor, mock_driver):
    """Tests get_attribute_by_locator when no elements are found."""
    mock_driver.find_element.return_value = None
    locator = {"by": "ID", "selector": "non_existent_id", "attribute": "test_attribute"}
    
    result = await executor.get_attribute_by_locator(locator)

    mock_driver.find_element.assert_called_once_with(By.ID, "non_existent_id")
    assert result is None

@pytest.mark.asyncio
async def test_get_attribute_by_locator_dict_like_string(executor, mock_driver):
   """Tests get_attribute_by_locator when attribute is a dictionary-like string."""
   mock_element = MagicMock()
   mock_element.get_attribute.return_value = '{"key": "value"}'
   mock_driver.find_element.return_value = mock_element
   locator = {"by": "ID", "selector": "element_id", "attribute": '{"attr": "test"}'}

   result = await executor.get_attribute_by_locator(locator)
   
   mock_driver.find_element.assert_called_once_with(By.ID, "element_id")
   assert result == {'key': 'value'}
   
@pytest.mark.asyncio
async def test_get_webelement_by_locator_single(executor, mock_driver):
    """Tests get_webelement_by_locator for a single element."""
    mock_element = MagicMock()
    mock_driver.find_element.return_value = mock_element
    locator = {"by": "ID", "selector": "some_id"}
    
    result = await executor.get_webelement_by_locator(locator)
    
    mock_driver.find_element.assert_called_once_with(By.ID, "some_id")
    assert result == mock_element

@pytest.mark.asyncio
async def test_get_webelement_by_locator_multiple(executor, mock_driver):
    """Tests get_webelement_by_locator for multiple elements."""
    mock_elements = [MagicMock(), MagicMock()]
    mock_driver.find_elements.return_value = mock_elements
    locator = {"by": "CLASS_NAME", "selector": "some_class"}
    
    result = await executor.get_webelement_by_locator(locator)
    
    mock_driver.find_elements.assert_called_once_with(By.CLASS_NAME, "some_class")
    assert result == mock_elements

@pytest.mark.asyncio
async def test_get_webelement_by_locator_not_found(executor, mock_driver):
    """Tests get_webelement_by_locator when element is not found."""
    mock_driver.find_element.return_value = None
    locator = {"by": "ID", "selector": "non_existent_id"}
    
    result = await executor.get_webelement_by_locator(locator)

    mock_driver.find_element.assert_called_once_with(By.ID, "non_existent_id")
    assert result is None

@pytest.mark.asyncio
async def test_get_webelement_as_screenshot(executor, mock_driver):
    """Tests get_webelement_as_screenshot."""
    mock_element = MagicMock()
    mock_element.screenshot_as_base64 = "some_base64_string"
    mock_driver.find_element.return_value = mock_element
    locator = {"by": "ID", "selector": "some_id"}
    
    result = await executor.get_webelement_as_screenshot(locator)
    
    mock_driver.find_element.assert_called_once_with(By.ID, "some_id")
    assert result == "some_base64_string"

@pytest.mark.asyncio
async def test_execute_event(executor, mock_driver):
    """Tests execute_event with a click event."""
    mock_element = MagicMock()
    mock_driver.find_element.return_value = mock_element
    locator = SimpleNamespace(by="ID", selector="some_id", event="click()")
    
    await executor.execute_event(locator, mock_element)
    
    mock_element.click.assert_called_once()


@pytest.mark.asyncio
async def test_execute_event_with_send_keys(executor, mock_driver):
    """Tests execute_event with a send_keys event."""
    mock_element = MagicMock()
    mock_driver.find_element.return_value = mock_element
    locator = SimpleNamespace(by="ID", selector="some_id", event='send_keys("test_value")')

    await executor.execute_event(locator,mock_element)

    mock_element.send_keys.assert_called_once_with("test_value")
    
@pytest.mark.asyncio
async def test_execute_event_with_javascript(executor, mock_driver):
    """Tests execute_event with javascript execution"""
    mock_element = MagicMock()
    mock_driver.find_element.return_value = mock_element
    locator = SimpleNamespace(by="ID", selector="some_id", event='execute_script("arguments[0].scrollIntoView();", element)')

    await executor.execute_event(locator, mock_element)

    mock_driver.execute_script.assert_called_once()

@pytest.mark.asyncio
async def test_send_message(executor, mock_driver):
    """Tests send_message method."""
    mock_element = MagicMock()
    mock_driver.find_element.return_value = mock_element
    locator = {"by": "ID", "selector": "some_id"}
    
    await executor.send_message(locator, "test message")
    
    mock_driver.find_element.assert_called_once_with(By.ID, "some_id")
    mock_element.send_keys.assert_called_once_with("test message")

@pytest.mark.asyncio
async def test_send_message_element_not_found(executor, mock_driver):
    """Tests send_message when element is not found."""
    mock_driver.find_element.return_value = None
    locator = {"by": "ID", "selector": "non_existent_id"}
    
    await executor.send_message(locator, "test message")
    
    mock_driver.find_element.assert_called_once_with(By.ID, "non_existent_id")

def test_execute_locator_post_init_with_driver(mock_driver):
    """Test __post_init__ when a driver is passed"""
    executor = ExecuteLocator(driver=mock_driver)
    assert isinstance(executor.actions, ActionChains)
    assert executor.actions.driver == mock_driver

def test_execute_locator_post_init_no_driver():
    """Test __post_init__ when no driver is passed"""
    executor = ExecuteLocator()
    assert executor.actions is None
```