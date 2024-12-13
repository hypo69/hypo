```python
import asyncio
import pytest
from unittest.mock import MagicMock, AsyncMock
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from types import SimpleNamespace
from hypotez.src.webdriver.executor import ExecuteLocator
from hypotez.src.logger.exceptions import DefaultSettingsException, ExecuteLocatorException, WebDriverException

# Fixture definitions
@pytest.fixture
def mock_driver():
    """Provides a mock driver object."""
    mock = MagicMock()
    mock.find_elements = AsyncMock(return_value=[MagicMock()])
    return mock

@pytest.fixture
def execute_locator(mock_driver):
    """Provides an instance of ExecuteLocator with a mock driver."""
    return ExecuteLocator(driver=mock_driver, mode='debug')

@pytest.fixture
def mock_webelement():
    """Provides a mock WebElement object."""
    mock = MagicMock(spec=WebElement)
    mock.get_attribute.return_value = "test_attribute_value"
    mock.screenshot_as_png = b'test_screenshot_data'
    mock.text = "test text"
    return mock

@pytest.fixture
def mock_list_webelement(mock_webelement):
    """Provides a list of mock WebElement objects."""
    return [mock_webelement, MagicMock(spec=WebElement)]


# --- Tests for execute_locator function ---
@pytest.mark.asyncio
async def test_execute_locator_no_locator_attribute_and_selector(execute_locator):
    """Checks that None is returned if no attribute and selector provided."""
    locator = SimpleNamespace()
    result = await execute_locator.execute_locator(locator=locator)
    assert result is None

@pytest.mark.asyncio
async def test_execute_locator_with_attribute_value(execute_locator, mock_webelement):
    """Checks correct behavior with 'VALUE' by and attribute."""
    locator = SimpleNamespace(by="VALUE", attribute='test_attribute_value', selector='test_selector')
    result = await execute_locator.execute_locator(locator=locator)
    assert result == 'test_attribute_value'

@pytest.mark.asyncio
async def test_execute_locator_with_event(execute_locator, mock_driver, mock_webelement):
    """Checks correct behavior when an event is provided."""
    mock_driver.find_elements = AsyncMock(return_value=[mock_webelement])
    locator = SimpleNamespace(by="ID", selector="test_id", event="click()")
    result = await execute_locator.execute_locator(locator=locator)
    assert result is True
    mock_webelement.click.assert_called_once()

@pytest.mark.asyncio
async def test_execute_locator_with_attribute(execute_locator, mock_driver, mock_webelement):
    """Checks correct behavior when an attribute is provided."""
    mock_driver.find_elements = AsyncMock(return_value=[mock_webelement])
    locator = SimpleNamespace(by="ID", selector="test_id", attribute="text")
    result = await execute_locator.execute_locator(locator=locator)
    assert result == "test_attribute_value"
    mock_webelement.get_attribute.assert_called_once_with("text")

@pytest.mark.asyncio
async def test_execute_locator_with_no_event_no_attribute(execute_locator, mock_driver, mock_webelement):
    """Checks correct behavior when no event or attribute is provided, should return the web element."""
    mock_driver.find_elements = AsyncMock(return_value=[mock_webelement])
    locator = SimpleNamespace(by="ID", selector="test_id")
    result = await execute_locator.execute_locator(locator=locator)
    assert result == mock_webelement

@pytest.mark.asyncio
async def test_execute_locator_invalid_locator_type(execute_locator):
    """Checks the behavior when an invalid locator type is passed."""
    with pytest.raises(AttributeError):
       await execute_locator.execute_locator(locator='invalid')

@pytest.mark.asyncio
async def test_execute_locator_with_default_values(execute_locator, mock_driver, mock_webelement):
    """Checks execute_locator with default timeout and message values."""
    mock_driver.find_elements = AsyncMock(return_value=[mock_webelement])
    locator = SimpleNamespace(by="ID", selector="test_id")
    result = await execute_locator.execute_locator(locator)
    assert result == mock_webelement

@pytest.mark.asyncio
async def test_execute_locator_with_no_element(execute_locator, mock_driver):
    """Checks the behavior of execute_locator when the element is not found."""
    mock_driver.find_elements = AsyncMock(side_effect=TimeoutException)
    locator = SimpleNamespace(by="ID", selector="nonexistent_id")
    result = await execute_locator.execute_locator(locator)
    assert result is None

# --- Tests for evaluate_locator function ---
@pytest.mark.asyncio
async def test_evaluate_locator_with_keys_attribute(execute_locator):
    """Checks evaluate_locator when attribute is a Keys enum."""
    attribute = "%ENTER%"
    result = await execute_locator.evaluate_locator(attribute)
    assert result == Keys.ENTER

@pytest.mark.asyncio
async def test_evaluate_locator_with_string_attribute(execute_locator):
    """Checks evaluate_locator when attribute is a string."""
    attribute = "test_attribute"
    result = await execute_locator.evaluate_locator(attribute)
    assert result == "test_attribute"

@pytest.mark.asyncio
async def test_evaluate_locator_with_list_attribute(execute_locator):
    """Checks evaluate_locator when attribute is a list."""
    attribute = ["%ENTER%", "test_attribute"]
    result = await execute_locator.evaluate_locator(attribute)
    assert result == [Keys.ENTER, "test_attribute"]

@pytest.mark.asyncio
async def test_evaluate_locator_with_empty_attribute(execute_locator):
    """Checks evaluate_locator with an empty attribute string."""
    attribute = ""
    result = await execute_locator.evaluate_locator(attribute)
    assert result == ""

# --- Tests for get_attribute_by_locator function ---
@pytest.mark.asyncio
async def test_get_attribute_by_locator_with_valid_attribute(execute_locator, mock_driver, mock_webelement):
    """Checks the behavior of get_attribute_by_locator with valid locator and attribute."""
    mock_driver.find_elements = AsyncMock(return_value=[mock_webelement])
    locator = SimpleNamespace(by="ID", selector="test_id", attribute="text")
    result = await execute_locator.get_attribute_by_locator(locator=locator)
    assert result == "test_attribute_value"
    mock_webelement.get_attribute.assert_called_once_with("text")

@pytest.mark.asyncio
async def test_get_attribute_by_locator_with_dict_attribute(execute_locator, mock_driver, mock_webelement):
     """Checks the behavior of get_attribute_by_locator when the attribute is a dict-like string."""
     mock_driver.find_elements = AsyncMock(return_value=[mock_webelement])
     mock_webelement.get_attribute.side_effect = ["attr1_value", "attr2_value"]
     locator = SimpleNamespace(by="ID", selector="test_id", attribute="{attr1:attr2}")
     result = await execute_locator.get_attribute_by_locator(locator=locator)
     assert result == {"attr1_value": "attr2_value"}

@pytest.mark.asyncio
async def test_get_attribute_by_locator_with_list_elements(execute_locator, mock_driver, mock_list_webelement):
    """Checks the behavior of get_attribute_by_locator with list of webelements"""
    mock_driver.find_elements = AsyncMock(return_value=mock_list_webelement)
    locator = SimpleNamespace(by="ID", selector="test_id", attribute="text")
    result = await execute_locator.get_attribute_by_locator(locator=locator)
    assert result == ["test_attribute_value", "test_attribute_value"]

@pytest.mark.asyncio
async def test_get_attribute_by_locator_no_element(execute_locator, mock_driver):
    """Checks the behavior of get_attribute_by_locator when no element is found."""
    mock_driver.find_elements = AsyncMock(side_effect=TimeoutException)
    locator = SimpleNamespace(by="ID", selector="nonexistent_id", attribute="text")
    result = await execute_locator.get_attribute_by_locator(locator=locator)
    assert result is None

@pytest.mark.asyncio
async def test_get_attribute_by_locator_invalid_attribute_format(execute_locator, mock_driver, mock_webelement):
    """Checks get_attribute_by_locator with an invalid attribute format."""
    mock_driver.find_elements = AsyncMock(return_value=[mock_webelement])
    locator = SimpleNamespace(by="ID", selector="test_id", attribute="invalid_format")
    result = await execute_locator.get_attribute_by_locator(locator)
    assert result == "test_attribute_value"


# --- Tests for get_webelement_by_locator function ---
@pytest.mark.asyncio
async def test_get_webelement_by_locator_with_valid_locator(execute_locator, mock_driver, mock_webelement):
    """Checks correct behavior with a valid locator."""
    mock_driver.find_elements = AsyncMock(return_value=[mock_webelement])
    locator = SimpleNamespace(by="ID", selector="test_id")
    result = await execute_locator.get_webelement_by_locator(locator=locator)
    assert result == mock_webelement

@pytest.mark.asyncio
async def test_get_webelement_by_locator_with_list_elements_and_if_list_first(execute_locator, mock_driver, mock_list_webelement):
    """Checks correct behavior with a valid locator and if_list == 'first'."""
    mock_driver.find_elements = AsyncMock(return_value=mock_list_webelement)
    locator = SimpleNamespace(by="ID", selector="test_id", if_list="first")
    result = await execute_locator.get_webelement_by_locator(locator=locator)
    assert result == mock_list_webelement[0]

@pytest.mark.asyncio
async def test_get_webelement_by_locator_with_list_elements_and_if_list_last(execute_locator, mock_driver, mock_list_webelement):
    """Checks correct behavior with a valid locator and if_list == 'last'."""
    mock_driver.find_elements = AsyncMock(return_value=mock_list_webelement)
    locator = SimpleNamespace(by="ID", selector="test_id", if_list="last")
    result = await execute_locator.get_webelement_by_locator(locator=locator)
    assert result == mock_list_webelement[-1]


@pytest.mark.asyncio
async def test_get_webelement_by_locator_with_list_elements_and_if_list_even(execute_locator, mock_driver, mock_list_webelement):
    """Checks correct behavior with a valid locator and if_list == 'even'."""
    mock_driver.find_elements = AsyncMock(return_value=[mock_list_webelement[0], mock_list_webelement[1], MagicMock(spec=WebElement)])
    locator = SimpleNamespace(by="ID", selector="test_id", if_list="even")
    result = await execute_locator.get_webelement_by_locator(locator=locator)
    assert result == [mock_list_webelement[0], MagicMock(spec=WebElement)]

@pytest.mark.asyncio
async def test_get_webelement_by_locator_with_list_elements_and_if_list_odd(execute_locator, mock_driver, mock_list_webelement):
    """Checks correct behavior with a valid locator and if_list == 'odd'."""
    mock_driver.find_elements = AsyncMock(return_value=[MagicMock(spec=WebElement), mock_list_webelement[0], mock_list_webelement[1]])
    locator = SimpleNamespace(by="ID", selector="test_id", if_list="odd")
    result = await execute_locator.get_webelement_by_locator(locator=locator)
    assert result == [mock_list_webelement[0]]


@pytest.mark.asyncio
async def test_get_webelement_by_locator_with_list_elements_and_if_list_list(execute_locator, mock_driver, mock_list_webelement):
    """Checks correct behavior with a valid locator and if_list == [1,2]"""
    mock_driver.find_elements = AsyncMock(return_value=[MagicMock(spec=WebElement), mock_list_webelement[0], mock_list_webelement[1], MagicMock(spec=WebElement)])
    locator = SimpleNamespace(by="ID", selector="test_id", if_list=[2,3])
    result = await execute_locator.get_webelement_by_locator(locator=locator)
    assert result == [mock_list_webelement[0], mock_list_webelement[1]]


@pytest.mark.asyncio
async def test_get_webelement_by_locator_with_list_elements_and_if_list_int(execute_locator, mock_driver, mock_list_webelement):
    """Checks correct behavior with a valid locator and if_list == 1"""
    mock_driver.find_elements = AsyncMock(return_value=[mock_list_webelement[0], mock_list_webelement[1]])
    locator = SimpleNamespace(by="ID", selector="test_id", if_list=1)
    result = await execute_locator.get_webelement_by_locator(locator=locator)
    assert result == mock_list_webelement[0]

@pytest.mark.asyncio
async def test_get_webelement_by_locator_no_element_found(execute_locator, mock_driver):
    """Checks behavior when no element is found."""
    mock_driver.find_elements = AsyncMock(side_effect=TimeoutException)
    locator = SimpleNamespace(by="ID", selector="nonexistent_id")
    result = await execute_locator.get_webelement_by_locator(locator=locator)
    assert result is None


@pytest.mark.asyncio
async def test_get_webelement_by_locator_invalid_locator(execute_locator):
    """Checks behavior when an invalid locator is passed."""
    with pytest.raises(ValueError, match='Некорректный локатор.'):
        await execute_locator.get_webelement_by_locator(locator=None)


# --- Tests for get_webelement_as_screenshot function ---
@pytest.mark.asyncio
async def test_get_webelement_as_screenshot_with_valid_locator(execute_locator, mock_driver, mock_webelement):
    """Checks correct behavior when a valid locator is provided."""
    mock_driver.find_elements = AsyncMock(return_value=[mock_webelement])
    locator = SimpleNamespace(by="ID", selector="test_id")
    result = await execute_locator.get_webelement_as_screenshot(locator=locator)
    assert result == b'test_screenshot_data'


@pytest.mark.asyncio
async def test_get_webelement_as_screenshot_no_element_found(execute_locator, mock_driver):
     """Checks behavior when no element is found."""
     mock_driver.find_elements = AsyncMock(side_effect=TimeoutException)
     locator = SimpleNamespace(by="ID", selector="nonexistent_id")
     result = await execute_locator.get_webelement_as_screenshot(locator=locator)
     assert result is None

@pytest.mark.asyncio
async def test_get_webelement_as_screenshot_prefetched_element(execute_locator, mock_webelement):
    """Checks get_webelement_as_screenshot with pre-fetched web element."""
    result = await execute_locator.get_webelement_as_screenshot(locator=None, webelement=mock_webelement)
    assert result == b'test_screenshot_data'

# --- Tests for execute_event function ---
@pytest.mark.asyncio
async def test_execute_event_click(execute_locator, mock_driver, mock_webelement):
    """Checks the behavior of execute_event with a click event."""
    mock_driver.find_elements = AsyncMock(return_value=[mock_webelement])
    locator = SimpleNamespace(by="ID", selector="test_id", event="click()")
    result = await execute_locator.execute_event(locator=locator)
    assert result is True
    mock_webelement.click.assert_called_once()

@pytest.mark.asyncio
async def test_execute_event_pause(execute_locator, mock_driver, mock_webelement):
    """Checks the behavior of execute_event with a pause event."""
    mock_driver.find_elements = AsyncMock(return_value=[mock_webelement])
    locator = SimpleNamespace(by="ID", selector="test_id", event="pause(1)")
    result = await execute_locator.execute_event(locator=locator)
    assert result is True

@pytest.mark.asyncio
async def test_execute_event_pause_invalid_format(execute_locator, mock_driver, mock_webelement):
    """Checks the behavior of execute_event with an invalid pause event."""
    mock_driver.find_elements = AsyncMock(return_value=[mock_webelement])
    locator = SimpleNamespace(by="ID", selector="test_id", event="pause()")
    result = await execute_locator.execute_event(locator=locator)
    assert result is False


@pytest.mark.asyncio
async def test_execute_event_upload_media(execute_locator, mock_driver, mock_webelement):
    """Checks the behavior of execute_event with an upload_media event."""
    mock_driver.find_elements = AsyncMock(return_value=[mock_webelement])
    locator = SimpleNamespace(by="ID", selector="test_id", event="upload_media()")
    result = await execute_locator.execute_event(locator=locator, message="test_file_path")
    assert result is True
    mock_webelement.send_keys.assert_called_once_with("test_file_path")

@pytest.mark.asyncio
async def test_execute_event_upload_media_no_message(execute_locator, mock_driver, mock_webelement):
    """Checks the behavior of execute_event with an upload_media event, but no message is provided."""
    mock_driver.find_elements = AsyncMock(return_value=[mock_webelement])
    locator = SimpleNamespace(by="ID", selector="test_id", event="upload_media()")
    result = await execute_locator.execute_event(locator=locator)
    assert result is False

@pytest.mark.asyncio
async def test_execute_event_screenshot(execute_locator, mock_driver, mock_webelement):
    """Checks the behavior of execute_event with a screenshot event."""
    mock_driver.find_elements = AsyncMock(return_value=[mock_webelement])
    locator = SimpleNamespace(by="ID", selector="test_id", event="screenshot()")
    result = await execute_locator.execute_event(locator=locator)
    assert result == [b'test_screenshot_data']

@pytest.mark.asyncio
async def test_execute_event_clear(execute_locator, mock_driver, mock_webelement):
    """Checks the behavior of execute_event with a clear event."""
    mock_driver.find_elements = AsyncMock(return_value=[mock_webelement])
    locator = SimpleNamespace(by="ID", selector="test_id", event="clear()")
    result = await execute_locator.execute_event(locator=locator)
    assert result is True
    mock_webelement.clear.assert_called_once()


@pytest.mark.asyncio
async def test_execute_event_send_keys(execute_locator, mock_driver, mock_webelement):
    """Checks the behavior of execute_event with a send_keys event."""
    mock_driver.find_elements = AsyncMock(return_value=[mock_webelement])
    locator = SimpleNamespace(by="ID", selector="test_id", event="send_keys(ENTER)")
    result = await execute_locator.execute_event(locator=locator)
    assert result is True

@pytest.mark.asyncio
async def test_execute_event_send_keys_with_plus(execute_locator, mock_driver, mock_webelement):
    """Checks the behavior of execute_event with a send_keys event with '+'."""
    mock_driver.find_elements = AsyncMock(return_value=[mock_webelement])
    locator = SimpleNamespace(by="ID", selector="test_id", event="send_keys(SHIFT+ENTER)")
    result = await execute_locator.execute_event(locator=locator)
    assert result is True

@pytest.mark.asyncio
async def test_execute_event_type(execute_locator, mock_driver, mock_webelement):
    """Checks the behavior of execute_event with a type event."""
    mock_driver.find_elements = AsyncMock(return_value=[mock_webelement])
    locator = SimpleNamespace(by="ID", selector="test_id", event="type(test_message)")
    result = await execute_locator.execute_event(locator=locator)
    assert result is True
    mock_webelement.send_keys.assert_called_once_with("test_message")

@pytest.mark.asyncio
async def test_execute_event_type_with_typing_speed(execute_locator, mock_driver, mock_webelement):
    """Checks the behavior of execute_event with a type event and typing speed."""
    mock_driver.find_elements = AsyncMock(return_value=[mock_webelement])
    locator = SimpleNamespace(by="ID", selector="test_id", event="type(test)")
    result = await execute_locator.execute_event(locator=locator, typing_speed=0.01)
    assert result is True
    assert mock_webelement.send_keys.call_count == 4

@pytest.mark.asyncio
async def test_execute_event_no_element(execute_locator, mock_driver):
    """Checks the behavior of execute_event when no element is found."""
    mock_driver.find_elements = AsyncMock(side_effect=TimeoutException)
    locator = SimpleNamespace(by="ID", selector="nonexistent_id", event="click()")
    result = await execute_locator.execute_event(locator=locator)
    assert result is False

@pytest.mark.asyncio
async def test_execute_event_click_intercepted(execute_locator, mock_driver, mock_webelement):
    """Checks the behavior of execute_event with a click event when click is intercepted."""
    mock_driver.find_elements = AsyncMock(return_value=[mock_webelement])
    mock_webelement.click.side_effect = ElementClickInterceptedException
    locator = SimpleNamespace(by="ID", selector="test_id", event="click()")
    result = await execute_locator.execute_event(locator=locator)
    assert result is None


# --- Tests for send_message function ---
@pytest.mark.asyncio
async def test_send_message_valid_input(execute_locator, mock_driver, mock_webelement):
    """Checks send_message with valid locator and message."""
    mock_driver.find_elements = AsyncMock(return_value=[mock_webelement])
    locator = SimpleNamespace(by="ID", selector="test_id")
    result = await execute_locator.send_message(locator=locator, message="test message")
    assert result is True


@pytest.mark.asyncio
async def test_send_message_with_replace_dict(execute_locator, mock_driver, mock_webelement):
    """Checks send_message with a replace dictionary."""
    mock_driver.find_elements = AsyncMock(return_value=[mock_webelement])
    locator = SimpleNamespace(by="ID", selector="test_id")
    result = await execute_locator.send_message(locator=locator, message="test ; message")
    assert result is True

@pytest.mark.asyncio
async def test_send_message_with_typing_speed(execute_locator, mock_driver, mock_webelement):
    """Checks send_message with a typing speed."""
    mock_driver.find_elements = AsyncMock(return_value=[mock_webelement])
    locator = SimpleNamespace(by="ID", selector="test_id")
    result = await execute_locator.send_message(locator=locator, message="test message", typing_speed=0.01)
    assert result is True

@pytest.mark.asyncio
async def test_send_message_no_element(execute_locator, mock_driver):
    """Checks send_message when no element is found."""
    mock_driver.find_elements = AsyncMock(side_effect=TimeoutException)
    locator = SimpleNamespace(by="ID", selector="nonexistent_id")
    result = await execute_locator.send_message(locator=locator, message="test message")
    assert result is None


@pytest.mark.asyncio
async def test_send_message_empty_message(execute_locator, mock_driver, mock_webelement):
    """Checks send_message with an empty message."""
    mock_driver.find_elements = AsyncMock(return_value=[mock_webelement])
    locator = SimpleNamespace(by="ID", selector="test_id")
    result = await execute_locator.send_message(locator=locator, message="")
    assert result is True
```