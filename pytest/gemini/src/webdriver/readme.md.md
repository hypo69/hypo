```python
import pytest
from unittest.mock import MagicMock
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from types import SimpleNamespace

from src.webdriver.executor import ExecuteLocator
# from src.logger.exceptions import WebDriverException, ExecuteLocatorException  # Assuming these exist


# Fixture for a mock WebDriver
@pytest.fixture
def mock_driver():
    driver = MagicMock(spec=webdriver.Chrome)
    driver.implicitly_wait = MagicMock()
    return driver

# Fixture for a sample locator
@pytest.fixture
def sample_locator():
     return {
      "product_links": {
        "attribute": "href",
        "by": "xpath",
        "selector": "//div[contains(@id,'node-galery')]//li[contains(@class,'item')]//a",
        "selector 2": "//span[@data-component-type='s-product-image']//a",
        "if_list":"first","use_mouse": False,
        "mandatory": True,
        "timeout":0,"timeout_for_event":"presence_of_element_located","event": None
      },
      "pagination": {
        "ul": {
          "attribute": None,
          "by": "xpath",
          "selector": "//ul[@class='pagination']",
          "timeout":0,"timeout_for_event":"presence_of_element_located","event": "click()"
        },
        "->": {
          "attribute": None,
          "by": "xpath",
          "selector": "//*[@class = 'ui-pagination-navi util-left']/a[@class='ui-pagination-next']",
          "timeout":0,"timeout_for_event":"presence_of_element_located","event": "click()",
          "if_list":"first","use_mouse": False
        }
      },
    "description": {
      "attribute": [
        None,
        None
      ],
      "by": [
        "xpath",
        "xpath"
      ],
      "selector": [
        "//a[contains(@href, '#tab-description')]",
        "//div[@id = 'tab-description']//p"
      ],
      "timeout":0,"timeout_for_event":"presence_of_element_located","event": [
        "click()",
        None
      ],
      "if_list":"first","use_mouse": [
        False,
        False
      ],
      "mandatory": [
        True,
        True
      ],
       "locator_description": [
        "Clicking on the tab to open the description field",
        "Reading data from div"
      ]
    }
    }


# Test for ExecuteLocator.__init__
def test_execute_locator_init(mock_driver):
    """Checks if ExecuteLocator initializes correctly."""
    executor = ExecuteLocator(mock_driver)
    assert executor.driver == mock_driver
    assert isinstance(executor.actions, ActionChains)

# Test for ExecuteLocator.execute_locator with valid locator
def test_execute_locator_valid_locator(mock_driver, sample_locator):
    """Checks if execute_locator processes a valid locator and returns a value."""
    executor = ExecuteLocator(mock_driver)
    mock_element = MagicMock(spec=WebElement)
    mock_element.get_attribute.return_value = "test_url"
    mock_driver.find_elements.return_value = [mock_element]
    
    result = executor.execute_locator(sample_locator["product_links"])
    
    assert result == "test_url"
    mock_driver.find_elements.assert_called()

def test_execute_locator_no_element_found(mock_driver, sample_locator):
    """Checks behavior when element isn't found"""
    executor = ExecuteLocator(mock_driver)
    mock_driver.find_elements.return_value = []
    result = executor.execute_locator(sample_locator["product_links"])
    assert result == False
    mock_driver.find_elements.assert_called()

def test_execute_locator_with_message(mock_driver, sample_locator):
     """Checks if execute_locator can send a message."""
     executor = ExecuteLocator(mock_driver)
     mock_element = MagicMock(spec=WebElement)
     mock_driver.find_elements.return_value = [mock_element]
     executor.send_message = MagicMock(return_value = True)
     message = "test message"
     typing_speed = 0.1

     result = executor.execute_locator(sample_locator["description"], message=message, typing_speed = typing_speed)
     assert executor.send_message.call_count == 1
     assert result == True

def test_execute_locator_with_attribute_none(mock_driver, sample_locator):
    """Checks if execute_locator can work with attribute none"""
    executor = ExecuteLocator(mock_driver)
    mock_element = MagicMock(spec=WebElement)
    mock_driver.find_elements.return_value = [mock_element]
    
    result = executor.execute_locator(sample_locator["pagination"]["ul"])
    
    assert result == mock_element
    mock_driver.find_elements.assert_called()


def test_execute_locator_click(mock_driver, sample_locator):
    """Checks if execute_locator processes a valid locator and returns a value."""
    executor = ExecuteLocator(mock_driver)
    mock_element = MagicMock(spec=WebElement)
    mock_driver.find_elements.return_value = [mock_element]
    mock_element.click = MagicMock()
    result = executor.execute_locator(sample_locator["pagination"]["->"])
    mock_element.click.assert_called()
    assert result == mock_element


def test_execute_locator_multiple_locators_list_elements(mock_driver, sample_locator):
    """Checks if execute_locator can work with multiple locators in list"""
    executor = ExecuteLocator(mock_driver)
    mock_element1 = MagicMock(spec=WebElement)
    mock_element2 = MagicMock(spec=WebElement)
    mock_element1.get_attribute.return_value = "test_attribute_1"
    mock_element2.get_attribute.return_value = "test_attribute_2"

    mock_driver.find_elements.side_effect = [[mock_element1], [mock_element2]]
    result = executor.execute_locator(sample_locator["description"])
    assert result == ["test_attribute_1", "test_attribute_2"]


def test_execute_locator_multiple_locators_click(mock_driver, sample_locator):
    """Checks if execute_locator can work with multiple locators in list"""
    executor = ExecuteLocator(mock_driver)
    mock_element1 = MagicMock(spec=WebElement)
    mock_element2 = MagicMock(spec=WebElement)
    mock_driver.find_elements.side_effect = [[mock_element1], [mock_element2]]
    mock_element1.click = MagicMock()
    
    result = executor.execute_locator(sample_locator["description"])
    mock_element1.click.assert_called()
    assert result ==  mock_element2

def test_get_webelement_by_locator_single_element(mock_driver, sample_locator):
    """Checks if get_webelement_by_locator returns a single WebElement."""
    executor = ExecuteLocator(mock_driver)
    mock_element = MagicMock(spec=WebElement)
    mock_driver.find_elements.return_value = [mock_element]
    result = executor.get_webelement_by_locator(sample_locator["product_links"])
    assert result == mock_element
    mock_driver.find_elements.assert_called()

def test_get_webelement_by_locator_multiple_elements(mock_driver, sample_locator):
    """Checks if get_webelement_by_locator returns a list of WebElements."""
    executor = ExecuteLocator(mock_driver)
    mock_element1 = MagicMock(spec=WebElement)
    mock_element2 = MagicMock(spec=WebElement)
    mock_driver.find_elements.return_value = [mock_element1, mock_element2]
    result = executor.get_webelement_by_locator(sample_locator["product_links"])

    assert result == [mock_element1, mock_element2]
    mock_driver.find_elements.assert_called()

def test_get_webelement_by_locator_no_elements(mock_driver, sample_locator):
    """Checks if get_webelement_by_locator returns False if no elements are found."""
    executor = ExecuteLocator(mock_driver)
    mock_driver.find_elements.return_value = []
    result = executor.get_webelement_by_locator(sample_locator["product_links"])
    assert result == False
    mock_driver.find_elements.assert_called()

def test_get_attribute_by_locator_single_attribute(mock_driver, sample_locator):
    """Checks if get_attribute_by_locator returns an attribute of a single element."""
    executor = ExecuteLocator(mock_driver)
    mock_element = MagicMock(spec=WebElement)
    mock_element.get_attribute.return_value = "test_attribute"
    mock_driver.find_elements.return_value = [mock_element]
    result = executor.get_attribute_by_locator(sample_locator["product_links"])
    assert result == "test_attribute"
    mock_element.get_attribute.assert_called_with("href")
    mock_driver.find_elements.assert_called()

def test_get_attribute_by_locator_multiple_attributes(mock_driver, sample_locator):
    """Checks if get_attribute_by_locator returns a list of attributes for multiple elements."""
    executor = ExecuteLocator(mock_driver)
    mock_element1 = MagicMock(spec=WebElement)
    mock_element2 = MagicMock(spec=WebElement)
    mock_element1.get_attribute.return_value = "attribute1"
    mock_element2.get_attribute.return_value = "attribute2"
    mock_driver.find_elements.return_value = [mock_element1, mock_element2]
    result = executor.get_attribute_by_locator(sample_locator["product_links"])
    assert result == ["attribute1", "attribute2"]
    mock_driver.find_elements.assert_called()

def test_get_attribute_by_locator_no_elements(mock_driver, sample_locator):
    """Checks if get_attribute_by_locator returns False if no elements are found."""
    executor = ExecuteLocator(mock_driver)
    mock_driver.find_elements.return_value = []
    result = executor.get_attribute_by_locator(sample_locator["product_links"])
    assert result == False
    mock_driver.find_elements.assert_called()

def test_send_message_success(mock_driver, sample_locator):
    """Checks if send_message sends a message successfully."""
    executor = ExecuteLocator(mock_driver)
    mock_element = MagicMock(spec=WebElement)
    mock_driver.find_elements.return_value = [mock_element]
    mock_element.send_keys = MagicMock()
    message = "test message"
    result = executor.send_message(sample_locator["product_links"], message, 0.1, continue_on_error = True)
    assert result == True
    mock_element.send_keys.assert_called_with(message)
    mock_driver.find_elements.assert_called()


def test_send_message_element_not_found(mock_driver, sample_locator):
     """Checks if send_message returns False if element not found."""
     executor = ExecuteLocator(mock_driver)
     mock_driver.find_elements.return_value = []
     message = "test message"
     result = executor.send_message(sample_locator["product_links"], message, 0.1, continue_on_error=True)
     assert result == False
     mock_driver.find_elements.assert_called()


def test_send_message_exception(mock_driver, sample_locator):
    """Checks if send_message handles an exception during message send."""
    executor = ExecuteLocator(mock_driver)
    mock_element = MagicMock(spec=WebElement)
    mock_driver.find_elements.return_value = [mock_element]
    mock_element.send_keys.side_effect = Exception("Test exception")
    message = "test message"
    result = executor.send_message(sample_locator["product_links"], message, 0.1, continue_on_error=True)
    assert result == False
    mock_driver.find_elements.assert_called()


def test_evaluate_locator_string(mock_driver, sample_locator):
    """Checks if evaluate_locator handles string attributes"""
    executor = ExecuteLocator(mock_driver)
    attribute = "test"
    result = executor.evaluate_locator(attribute)
    assert result == "test"

def test_evaluate_locator_dict(mock_driver, sample_locator):
    """Checks if evaluate_locator handles dict attributes"""
    executor = ExecuteLocator(mock_driver)
    attribute = {"external_message":"test"}
    result = executor.evaluate_locator(attribute)
    assert result == "%EXTERNAL_MESSAGE%"

def test_evaluate_locator_list(mock_driver, sample_locator):
    """Checks if evaluate_locator handles list attributes"""
    executor = ExecuteLocator(mock_driver)
    attribute = ["test1", "test2"]
    result = executor.evaluate_locator(attribute)
    assert result ==  "['test1', 'test2']"


def test_evaluate_locator_with_placeholder(mock_driver, sample_locator):
    """Checks if evaluate_locator returns the placeholder correctly"""
    executor = ExecuteLocator(mock_driver)
    attribute = "%EXTERNAL_MESSAGE%"
    result = executor.evaluate_locator(attribute)
    assert result == "%EXTERNAL_MESSAGE%"


def test__evaluate_with_valid_attribute(mock_driver, sample_locator):
    """Checks if _evaluate handles a valid attribute"""
    executor = ExecuteLocator(mock_driver)
    attribute = "test"
    result = executor._evaluate(attribute)
    assert result == "test"


def test__evaluate_with_placeholder(mock_driver, sample_locator):
    """Checks if _evaluate handles a placeholder correctly"""
    executor = ExecuteLocator(mock_driver)
    attribute = "%EXTERNAL_MESSAGE%"
    result = executor._evaluate(attribute)
    assert result == "%EXTERNAL_MESSAGE%"


def test_get_locator_keys():
    """Checks if get_locator_keys method returns a list of keys"""
    keys = ExecuteLocator.get_locator_keys()
    assert isinstance(keys, list)
    assert "by" in keys
    assert "selector" in keys
    assert "attribute" in keys

#Additional test needed
#Test for screenshots
#Test for click
#Test for continue_on_error flag
```