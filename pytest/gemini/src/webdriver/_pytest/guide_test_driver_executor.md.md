```python
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.options import Options

# Assuming the Driver and ExecuteLocator classes are defined in a file named driver_executor.py
# from your_module import Driver, ExecuteLocator  # Replace your_module
# Mock classes for testing purposes, replace with actual import when available

class ExecuteLocatorException(Exception):
    pass

class MockWebElement:
    def __init__(self, text, tag_name="div", attributes=None):
        self.text = text
        self.tag_name = tag_name
        self.attributes = attributes if attributes else {}

    def get_attribute(self, name):
        return self.attributes.get(name)

    def send_keys(self, keys):
        return True
    
    def click(self):
        return True
    
    
class MockWebDriver:
    def __init__(self):
        self.current_url = None
        self.elements = {
            "id": {
                "element_id": MockWebElement("Example Domain"),
                "missing_element_id": None
            },
            "xpath": {
                '//a[@href="https://www.iana.org/domains/example"]': MockWebElement("", tag_name="a", attributes={"href":"https://www.iana.org/domains/example"})
            }
            
        }

    def get(self, url):
        self.current_url = url

    def find_element(self, by, value):
        if by == By.ID:
          return self.elements['id'].get(value)
        elif by == By.XPATH:
           return self.elements['xpath'].get(value)

        return None
        

    def execute_script(self, script, element):
         return True
    

class Driver:
    def __init__(self, webdriver):
       self.driver = webdriver
    def navigate_to_page(self, url):
         self.driver.get(url)
         return self.driver.current_url == url

    def get_webelement_by_locator(self, locator):
      element = self.driver.find_element(locator['by'], locator['selector'])
      return element

    def send_message(self, locator, message):
      element = self.get_webelement_by_locator(locator)
      if element:
        return element.send_keys(message)
      return False

    def get_attribute_by_locator(self, locator, attribute_name):
       element = self.get_webelement_by_locator(locator)
       if element:
         return element.get_attribute(attribute_name)
       return None


class ExecuteLocator:
    def __init__(self, driver):
        self.driver = driver

    def execute_locator(self, locator):
        element = self.driver.get_webelement_by_locator(locator)
        if not element:
            raise ExecuteLocatorException("Element not found")

        if locator.get('event') == 'click':
          return element.click()
        
        return True
    
    def get_locator_keys(self):
      return [
            "attribute",
            "by",
            "selector",
            "event",
            "use_mouse",
            "mandatory",
            "locator_description",
        ]


# Fixture for Driver and ExecuteLocator classes
@pytest.fixture
def driver_instance():
    """Provides a Driver instance with a mock WebDriver."""
    webdriver = MockWebDriver()
    return Driver(webdriver)

@pytest.fixture
def execute_locator_instance(driver_instance):
    """Provides an ExecuteLocator instance with a Driver fixture."""
    return ExecuteLocator(driver_instance)

@pytest.fixture
def example_locator():
    """Provides a sample locator for testing."""
    return {
        "by": By.ID,
        "selector": "element_id",
        "event": None,
        "mandatory": True,
        "locator_description": "Sample element",
    }

@pytest.fixture
def example_locator_no_element():
    """Provides a sample locator that will not find an element for testing."""
    return {
        "by": By.ID,
        "selector": "missing_element_id",
        "event": None,
        "mandatory": True,
        "locator_description": "Sample element",
    }
@pytest.fixture
def example_locator_with_event():
    """Provides a sample locator with event for testing."""
    return {
        "by": By.ID,
        "selector": "element_id",
        "event": "click",
        "mandatory": True,
        "locator_description": "Sample element",
    }
@pytest.fixture
def example_locator_with_attribute():
    """Provides a sample locator with attribute for testing."""
    return {
        "by": By.XPATH,
        "selector": '//a[@href="https://www.iana.org/domains/example"]',
        "attribute": "href",
        "event": None,
        "mandatory": True,
        "locator_description": "Sample element",
    }
    


# Tests for Driver class
def test_navigate_to_page(driver_instance):
    """Checks if the WebDriver correctly loads the specified page."""
    assert driver_instance.navigate_to_page("http://example.com")

def test_get_webelement_by_locator_single_element(driver_instance, example_locator):
    """Checks if get_webelement_by_locator returns a WebElement instance."""
    element = driver_instance.get_webelement_by_locator(example_locator)
    assert isinstance(element, MockWebElement)
    assert element.text == "Example Domain"

def test_get_webelement_by_locator_no_element(driver_instance, example_locator_no_element):
    """Checks if get_webelement_by_locator returns None when the element is not found."""
    element = driver_instance.get_webelement_by_locator(example_locator_no_element)
    assert element is None


def test_send_message(driver_instance, example_locator):
    """Checks if the send_message method correctly sends a message to an element."""
    assert driver_instance.send_message(example_locator, "test message") is True

def test_get_attribute_by_locator(driver_instance, example_locator_with_attribute):
    """Checks if the get_attribute_by_locator method correctly returns an element's attribute."""
    attribute = driver_instance.get_attribute_by_locator(example_locator_with_attribute, "href")
    assert attribute == "https://www.iana.org/domains/example"

# Tests for ExecuteLocator class
def test_execute_locator_event(execute_locator_instance, example_locator_with_event):
    """Checks if the execute_locator method correctly executes an event on an element."""
    assert execute_locator_instance.execute_locator(example_locator_with_event) is True

def test_get_locator_keys(execute_locator_instance):
    """Checks if get_locator_keys method returns correct locator keys."""
    expected_keys = [
        "attribute",
        "by",
        "selector",
        "event",
        "use_mouse",
        "mandatory",
        "locator_description",
    ]
    assert execute_locator_instance.get_locator_keys() == expected_keys

def test_invalid_locator(execute_locator_instance, example_locator_no_element):
    """Checks if execute_locator method raises an exception with invalid locator."""
    with pytest.raises(ExecuteLocatorException):
        execute_locator_instance.execute_locator(example_locator_no_element)
```