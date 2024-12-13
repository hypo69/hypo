```python
import pytest
from selenium import webdriver
from src.webdriver.executor import ExecuteLocator
from src.logger.exceptions import ExecuteLocatorException
from unittest.mock import MagicMock


@pytest.fixture
def mock_driver():
    """Provides a mock WebDriver instance for testing."""
    mock_driver = MagicMock(spec=webdriver.Chrome)
    mock_driver.get.return_value = None
    mock_driver.quit.return_value = None
    return mock_driver

@pytest.fixture
def execute_locator(mock_driver):
    """Provides an ExecuteLocator instance with a mock driver."""
    return ExecuteLocator(mock_driver)


def test_execute_locator_simple_valid(execute_locator, mock_driver):
    """Checks correct behavior of execute_locator with a valid simple locator."""
    # Setup
    mock_element = MagicMock()
    mock_element.text = "Test Title"
    mock_driver.find_element.return_value = mock_element
    simple_locator = {
        "by": "XPATH",
        "selector": "//h1",
        "attribute": "textContent",
        "timeout":0,"timeout_for_event":"presence_of_element_located","event": None,
        "if_list":"first","use_mouse": False,
        "mandatory": True,
        "locator_description": "Getting the page title"
    }

    # Execution
    result = execute_locator.execute_locator(simple_locator)

    # Verification
    mock_driver.find_element.assert_called_once_with(by="xpath", value="//h1")
    assert result == "Test Title"

def test_execute_locator_complex_valid(execute_locator, mock_driver):
    """Checks correct behavior of execute_locator with a valid complex locator."""
    # Setup
    mock_link_element = MagicMock()
    mock_link_element.get_attribute.return_value = "https://example.com/product1"
    mock_pagination_ul = MagicMock()
    mock_pagination_next = MagicMock()
    mock_driver.find_elements.return_value = [mock_link_element]
    mock_driver.find_element.side_effect = [mock_pagination_ul, mock_pagination_next]

    complex_locator = {
        "product_links": {
            "attribute": "href",
            "by": "XPATH",
            "selector": "//a[contains(@class, \'product\')]",
            "timeout":0,"timeout_for_event":"presence_of_element_located","event": None,
            "if_list":"first","use_mouse": False,
            "mandatory": True,
            "locator_description": "Getting the product link"
        },
        "pagination": {
            "ul": {
                "attribute": None,
                "by": "XPATH",
                "selector": "//ul[@class=\'pagination\']",
                "timeout":0,"timeout_for_event":"presence_of_element_located","event": "click()",
                "if_list":"first","use_mouse": False,
                "mandatory": True,
                "locator_description": "Click on pagination"
            },
            "->": {
                "attribute": None,
                "by": "XPATH",
                "selector": "//*[@class = \'ui-pagination-navi util-left\']/a[@class=\'ui-pagination-next\']",
                "timeout":0,"timeout_for_event":"presence_of_element_located","event": "click()",
                "if_list":"first","use_mouse": False,
                "mandatory": True,
                "locator_description": "Click on the next page"
            }
        }
    }
    # Execution
    result = execute_locator.execute_locator(complex_locator)
    # Verification
    mock_driver.find_elements.assert_called_once_with(by="xpath", value="//a[contains(@class, 'product')]")
    assert result == {"product_links":"https://example.com/product1"}

def test_execute_locator_error_handling_continue(execute_locator, mock_driver):
    """Checks that error is handled and execution continues when continue_on_error=True."""
    # Setup
    mock_driver.find_element.side_effect = Exception("Element not found")
    simple_locator = {
        "by": "XPATH",
        "selector": "//h1",
        "attribute": "textContent",
        "timeout":0,"timeout_for_event":"presence_of_element_located","event": None,
        "if_list":"first","use_mouse": False,
        "mandatory": True,
        "locator_description": "Getting the page title"
    }
    # Execution
    try:
        result = execute_locator.execute_locator(simple_locator, continue_on_error=True)
        assert result is None
    except ExecuteLocatorException:
       pytest.fail("Should not raise an exception when continue_on_error=True")

    # Verification
    mock_driver.find_element.assert_called_once_with(by="xpath", value="//h1")


def test_execute_locator_error_handling_no_continue(execute_locator, mock_driver):
    """Checks that an exception is raised when an error occurs and continue_on_error=False."""
    # Setup
    mock_driver.find_element.side_effect = Exception("Element not found")
    simple_locator = {
        "by": "XPATH",
        "selector": "//h1",
        "attribute": "textContent",
        "timeout":0,"timeout_for_event":"presence_of_element_located","event": None,
        "if_list":"first","use_mouse": False,
        "mandatory": True,
        "locator_description": "Getting the page title"
    }
    # Execution and Verification
    with pytest.raises(ExecuteLocatorException, match="Error during locator execution: Element not found"):
        execute_locator.execute_locator(simple_locator, continue_on_error=False)

    mock_driver.find_element.assert_called_once_with(by="xpath", value="//h1")


def test_send_message_valid(execute_locator, mock_driver):
    """Checks correct behavior of send_message with valid input."""
    # Setup
    mock_element = MagicMock()
    mock_driver.find_element.return_value = mock_element
    message_locator = {
        "by": "XPATH",
        "selector": "//input[@name=\'search\']",
        "attribute": None,
        "timeout":0,"timeout_for_event":"presence_of_element_located","event": "%SEARCH%",
        "if_list":"first","use_mouse": False,
        "mandatory": True,
        "locator_description": "Sending a search query"
    }
    message = "Test message"

    # Execution
    result = execute_locator.send_message(message_locator, message, typing_speed=0.05)

    # Verification
    mock_driver.find_element.assert_called_once_with(by="xpath", value="//input[@name='search']")
    mock_element.send_keys.assert_called_once_with("Test message")
    assert result is None


def test_send_message_error_handling(execute_locator, mock_driver):
    """Checks that an exception is raised when an error occurs during send_message."""
    # Setup
    mock_driver.find_element.side_effect = Exception("Element not found")
    message_locator = {
        "by": "XPATH",
        "selector": "//input[@name=\'search\']",
        "attribute": None,
        "timeout":0,"timeout_for_event":"presence_of_element_located","event": "%SEARCH%",
        "if_list":"first","use_mouse": False,
        "mandatory": True,
        "locator_description": "Sending a search query"
    }
    message = "Test message"

    # Execution and Verification
    with pytest.raises(ExecuteLocatorException, match="Error during locator execution: Element not found"):
        execute_locator.send_message(message_locator, message)
    mock_driver.find_element.assert_called_once_with(by="xpath", value="//input[@name='search']")



def test_execute_locator_multi_valid(execute_locator, mock_driver):
    """Checks correct behavior with multiple locators."""
    # Setup
    mock_button_element = MagicMock()
    mock_button_element.text = "Submit"
    mock_input_element = MagicMock()
    mock_input_element.get_attribute.return_value = "user"
    mock_driver.find_elements.side_effect = [[mock_button_element], [mock_input_element]]
    
    multi_locator = {
        "by": ["XPATH", "XPATH"],
        "selector": ["//button[@id=\'submit\']", "//input[@id=\'username\']"],
        "attribute": ["textContent", "value"],
        "timeout":0,"timeout_for_event":"presence_of_element_located","event": ["click()", "send_keys(\'user\')"],
        "if_list":"first","use_mouse": [True, False],
        "mandatory": [True, True],
        "locator_description": ["Click the submit button", "Enter username"]
    }

    # Execution
    results = execute_locator.execute_locator(multi_locator)

    # Verification
    mock_driver.find_elements.assert_called_with(by='xpath', value='//button[@id=\'submit\']')
    mock_driver.find_elements.assert_called_with(by='xpath', value='//input[@id=\'username\']')
    assert results == ["Submit", "user"]

def test_evaluate_locator_valid(execute_locator, mock_driver):
    """Checks correct behavior of evaluate_locator with valid input."""
    # Setup
    mock_element = MagicMock()
    mock_element.get_attribute.return_value = "Test description"
    mock_driver.find_element.return_value = mock_element
    attribute_locator = {
        "by": "XPATH",
        "selector": "//meta[@name=\'description\']",
        "attribute": "content",
        "timeout":0,"timeout_for_event":"presence_of_element_located","event": None,
        "if_list":"first","use_mouse": False,
        "mandatory": True,
        "locator_description": "Getting the page meta-description"
    }

    # Execution
    result = execute_locator.evaluate_locator(attribute_locator['attribute'], attribute_locator)

    # Verification
    mock_driver.find_element.assert_called_once_with(by="xpath", value="//meta[@name='description']")
    assert result == "Test description"

def test_evaluate_locator_error_handling(execute_locator, mock_driver):
    """Checks that an exception is raised if an error occurs during evaluate_locator."""
    # Setup
    mock_driver.find_element.side_effect = Exception("Element not found")
    attribute_locator = {
        "by": "XPATH",
        "selector": "//meta[@name=\'description\']",
        "attribute": "content",
         "timeout":0,"timeout_for_event":"presence_of_element_located","event": None,
        "if_list":"first","use_mouse": False,
        "mandatory": True,
        "locator_description": "Getting the page meta-description"
    }
    # Execution and Verification
    with pytest.raises(ExecuteLocatorException, match="Error during locator evaluation: Element not found"):
        execute_locator.evaluate_locator(attribute_locator['attribute'], attribute_locator)

    mock_driver.find_element.assert_called_once_with(by="xpath", value="//meta[@name='description']")
```