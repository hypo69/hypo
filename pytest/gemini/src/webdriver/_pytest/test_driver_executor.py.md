```python
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from src.webdriver.executor import ExecuteLocator
from src.logger.exceptions import ExecuteLocatorException


@pytest.fixture(scope="module")
def driver():
    """Fixture to set up and tear down the WebDriver."""
    options = Options()
    options.add_argument("--headless")  # Run headless browser for testing
    service = Service(executable_path="/path/to/chromedriver")  # Path to your chromedriver
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("http://example.com")  # URL for the tests
    yield driver
    driver.quit()


@pytest.fixture
def execute_locator(driver):
    """Fixture to initialize the ExecuteLocator instance."""
    return ExecuteLocator(driver)


def test_navigate_to_page(execute_locator, driver):
    """Test to ensure that the WebDriver can navigate to a page."""
    assert driver.current_url == "http://example.com"


def test_get_webelement_by_locator_single_element(execute_locator, driver):
    """Test to get a single web element by locator."""
    locator = {
        "by": "XPATH",
        "selector": "//h1"
    }
    element = execute_locator.get_webelement_by_locator(locator)
    assert isinstance(element, WebElement)
    assert element.text == "Example Domain"


def test_get_webelement_by_locator_no_element(execute_locator, driver):
    """Test when no element is found by the locator."""
    locator = {
        "by": "XPATH",
        "selector": "//div[@id='nonexistent']"
    }
    result = execute_locator.get_webelement_by_locator(locator)
    assert result is False


def test_send_message(execute_locator, driver):
    """Test sending a message to a web element."""
    locator = {
        "by": "XPATH",
        "selector": "//input[@type='text']"  # Changed to a more general input field
    }
    message = "Hello World"
    # Clear the input field first to ensure the test is isolated
    element = execute_locator.get_webelement_by_locator(locator)
    element.clear()
    result = execute_locator.send_message(locator, message, typing_speed=0, continue_on_error=True)
    assert result is True
    # Verify that the message was sent to the input field
    assert element.get_attribute('value') == message


def test_send_message_with_error(execute_locator, driver):
    """Test sending a message to a non-existing element with continue_on_error=True."""
    locator = {
        "by": "XPATH",
        "selector": "//input[@id='nonexistent']"
    }
    message = "Hello World"
    result = execute_locator.send_message(locator, message, typing_speed=0, continue_on_error=True)
    assert result is True


def test_get_attribute_by_locator(execute_locator, driver):
    """Test to get an attribute value from a web element."""
    locator = {
        "by": "XPATH",
        "selector": "//a[contains(text(), 'More information')]"
    }
    attribute_value = execute_locator.get_attribute_by_locator(locator, message="href")
    assert attribute_value == "https://www.iana.org/domains/example"


def test_get_attribute_by_locator_nonexistent_attribute(execute_locator, driver):
    """Test to get non existent attribute"""
    locator = {
        "by": "XPATH",
        "selector": "//a[contains(text(), 'More information')]"
    }
    attribute_value = execute_locator.get_attribute_by_locator(locator, message="nonexistent_attribute")
    assert attribute_value is None


def test_execute_locator_event(execute_locator, driver):
    """Test to ensure that an event is correctly triggered on the locator."""
    locator = {
        "by": "XPATH",
        "selector": "//a[contains(text(), 'More information')]"
    }
    result = execute_locator.execute_locator(locator, message="click")
    assert result is True


def test_execute_locator_event_non_clickable(execute_locator, driver):
    """Test that event won't be triggered when element is not clickable"""
    locator = {
        "by": "XPATH",
        "selector": "//h1[contains(text(), 'Example Domain')]"
    }
    result = execute_locator.execute_locator(locator, message="click")
    assert result is False


def test_get_locator_keys(execute_locator, driver):
    """Test to get available locator keys."""
    expected_keys = [
        'attribute',
        'by',
        'selector',
        'event',
        'use_mouse',
        'mandatory',
        'locator_description',
    ]
    result = ExecuteLocator.get_locator_keys()
    assert set(result) == set(expected_keys)


def test_navigate_and_interact(execute_locator, driver):
    """Test to navigate to a page and interact with elements."""
    # Navigate to a new page
    driver.get("https://www.wikipedia.org/")
    assert driver.current_url == "https://www.wikipedia.org/"

    # Find and send message to the search input field
    locator = {
        "by": "XPATH",
        "selector": "//input[@id='searchInput']"
    }
    execute_locator.send_message(locator, "Selenium", typing_speed=0, continue_on_error=True)

    # Find and click the search button
    locator = {
        "by": "XPATH",
        "selector": "//button[@type='submit']"
    }
    execute_locator.execute_locator(locator, message="click")

    # Validate that the search results page is loaded
    assert "Selenium" in driver.title

    # Optionally check for an element on the results page
    result_locator = {
        "by": "XPATH",
        "selector": "//h1[contains(text(), 'Selenium')]"
    }
    result = execute_locator.get_webelement_by_locator(result_locator)
    assert isinstance(result, WebElement)
    assert result.text == "Selenium"


def test_invalid_locator(execute_locator, driver):
    """Test handling of invalid locators."""
    locator = {
        "by": "INVALID_BY",
        "selector": "//div[@id='test']"
    }
    with pytest.raises(ExecuteLocatorException):
        execute_locator.execute_locator(locator, message="click")


def test_invalid_locator_message(execute_locator, driver):
    """Test handling of invalid locators."""
    locator = {
        "by": "INVALID_BY",
        "selector": "//div[@id='test']"
    }
    with pytest.raises(ExecuteLocatorException, match="Locator error: Invalid locator by type: INVALID_BY"):
        execute_locator.send_message(locator, message="test", typing_speed=0, continue_on_error=True)


def test_invalid_locator_get_attribute(execute_locator, driver):
    """Test handling of invalid locators."""
    locator = {
        "by": "INVALID_BY",
        "selector": "//div[@id='test']"
    }
    with pytest.raises(ExecuteLocatorException, match="Locator error: Invalid locator by type: INVALID_BY"):
        execute_locator.get_attribute_by_locator(locator, message="href")
```