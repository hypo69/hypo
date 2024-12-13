```python
import pytest
from types import SimpleNamespace
from unittest.mock import MagicMock

# Mock executor and webdriver functionalities
class MockWebElement:
    def __init__(self, text="mock text", src="mock_src"):
        self.text = text
        self.src = src

    def click(self):
        pass

    def get_attribute(self, attribute):
        if attribute == 'innerText':
            return self.text
        if attribute == 'src':
            return self.src
        return None

class MockWebDriver:
    def __init__(self):
        self.elements = []
        self.last_screenshot_element = None
    def find_elements(self, by, selector):
        if not self.elements:
            return []
        return self.elements

    def execute_script(self, script, element):
      pass

    def get_screenshot_as_png(self):
        if self.last_screenshot_element:
          return b'mock_screenshot'
        return None
    
    def find_element(self, by, selector):
      if not self.elements:
            return None
      return self.elements[0]
    
    
class MockExecutor:
    def __init__(self, webdriver):
      self.driver = webdriver
    
    def _find_element(self, locator, element=None):
      if locator.by == "VALUE":
        return locator.attribute
      if element:
        return element
      if locator.by == "XPATH":
        if locator.if_list == "first":
          elements = self.driver.find_elements(locator.by, locator.selector)
          if elements:
              return elements[0]
        return self.driver.find_elements(locator.by, locator.selector)


    def execute(self, locator):
        locator = SimpleNamespace(**locator)
        element = self._find_element(locator)
        if not element:
            if locator.mandatory:
                raise Exception("Element not found and action is mandatory")
            return None
        if locator.event == "click()":
           element.click()
           return None
        if locator.event == "screenshot()":
           self.driver.last_screenshot_element = element
           return self.driver.get_screenshot_as_png()
        if locator.attribute:
           if isinstance(element, list):
             return [el.get_attribute(locator.attribute) for el in element]
           return element.get_attribute(locator.attribute)
        return element


@pytest.fixture
def mock_webdriver():
    """Provides a mock webdriver instance."""
    return MockWebDriver()

@pytest.fixture
def mock_executor(mock_webdriver):
    """Provides a mock executor instance."""
    return MockExecutor(mock_webdriver)

# Tests for close_banner locator
def test_close_banner_valid_input(mock_webdriver, mock_executor):
    """Checks correct behavior when the banner is found and clicked."""
    mock_webdriver.elements = [MockWebElement()]
    locator = {
        "attribute": None,
        "by": "XPATH",
        "selector": "//button[@id = 'closeXButton']",
        "if_list": "first",
        "use_mouse": False,
        "mandatory": False,
        "timeout": 0,
        "timeout_for_event": "presence_of_element_located",
        "event": "click()",
        "locator_description": "Закрываю pop-up окно, если оно не появилось - не страшно (`mandatory`:`false`)"
    }
    result = mock_executor.execute(locator)
    assert result is None

def test_close_banner_element_not_found(mock_webdriver, mock_executor):
    """Checks that no error is raised when the element is not found and it's not mandatory."""
    mock_webdriver.elements = []
    locator = {
        "attribute": None,
        "by": "XPATH",
        "selector": "//button[@id = 'closeXButton']",
        "if_list": "first",
        "use_mouse": False,
        "mandatory": False,
        "timeout": 0,
        "timeout_for_event": "presence_of_element_located",
        "event": "click()",
        "locator_description": "Закрываю pop-up окно, если оно не появилось - не страшно (`mandatory`:`false`)"
    }
    result = mock_executor.execute(locator)
    assert result is None


# Tests for id_manufacturer locator
def test_id_manufacturer_valid_input(mock_webdriver, mock_executor):
    """Checks that the attribute value is returned correctly."""
    locator = {
        "attribute": 11290,
        "by": "VALUE",
        "selector": None,
        "if_list": "first",
        "use_mouse": False,
        "mandatory": True,
        "timeout": 0,
        "timeout_for_event": "presence_of_element_located",
        "event": None,
        "locator_description": "id_manufacturer"
    }
    result = mock_executor.execute(locator)
    assert result == 11290

# Tests for additional_images_urls locator
def test_additional_images_urls_valid_input(mock_webdriver, mock_executor):
    """Checks correct behavior when images are found and their src attributes extracted."""
    mock_webdriver.elements = [MockWebElement(src='url1'), MockWebElement(src='url2')]
    locator = {
        "attribute": "src",
        "by": "XPATH",
        "selector": "//ol[contains(@class, 'flex-control-thumbs')]//img",
        "if_list": "first",
        "use_mouse": False,
        "mandatory": False,
        "timeout": 0,
        "timeout_for_event": "presence_of_element_located",
        "event": None
    }
    result = mock_executor.execute(locator)
    assert result == ['url1', 'url2']


def test_additional_images_urls_no_elements(mock_webdriver, mock_executor):
    """Checks correct behavior when no elements are found."""
    mock_webdriver.elements = []
    locator = {
        "attribute": "src",
        "by": "XPATH",
        "selector": "//ol[contains(@class, 'flex-control-thumbs')]//img",
        "if_list": "first",
        "use_mouse": False,
        "mandatory": False,
        "timeout": 0,
        "timeout_for_event": "presence_of_element_located",
        "event": None
    }
    result = mock_executor.execute(locator)
    assert result is None


# Tests for default_image_url locator
def test_default_image_url_valid_input(mock_webdriver, mock_executor):
    """Checks correct behavior when the image is found and a screenshot is taken."""
    mock_webdriver.elements = [MockWebElement()]
    locator = {
        "attribute": None,
        "by": "XPATH",
        "selector": "//a[@id = 'mainpic']//img",
        "if_list": "first",
        "use_mouse": False,
        "timeout": 0,
        "timeout_for_event": "presence_of_element_located",
        "event": "screenshot()",
        "mandatory": True,
        "locator_description": "Внимание! в морлеви картинка получается через screenshot и возвращается как png (`bytes`)"
    }
    result = mock_executor.execute(locator)
    assert result == b'mock_screenshot'

def test_default_image_url_element_not_found(mock_webdriver, mock_executor):
    """Checks exception is raised when the element is not found and is mandatory."""
    mock_webdriver.elements = []
    locator = {
        "attribute": None,
        "by": "XPATH",
        "selector": "//a[@id = 'mainpic']//img",
        "if_list": "first",
        "use_mouse": False,
        "timeout": 0,
        "timeout_for_event": "presence_of_element_located",
        "event": "screenshot()",
        "mandatory": True,
        "locator_description": "Внимание! в морлеви картинка получается через screenshot и возвращается как png (`bytes`)"
    }
    with pytest.raises(Exception, match="Element not found and action is mandatory"):
         mock_executor.execute(locator)

# Tests for id_supplier locator
def test_id_supplier_valid_input(mock_webdriver, mock_executor):
    """Checks correct behavior when the element is found and the text is extracted."""
    mock_webdriver.elements = [MockWebElement(text='test_sku')]
    locator = {
        "attribute": "innerText",
        "by": "XPATH",
        "selector": "//span[@class = 'ltr sku-copy']",
        "if_list": "first",
        "use_mouse": False,
        "mandatory": True,
        "timeout": 0,
        "timeout_for_event": "presence_of_element_located",
        "event": None,
        "locator_description": "SKU morlevi"
    }
    result = mock_executor.execute(locator)
    assert result == 'test_sku'


def test_id_supplier_element_not_found(mock_webdriver, mock_executor):
    """Checks exception is raised when the element is not found and is mandatory."""
    mock_webdriver.elements = []
    locator = {
       "attribute": "innerText",
        "by": "XPATH",
        "selector": "//span[@class = 'ltr sku-copy']",
        "if_list": "first",
        "use_mouse": False,
        "mandatory": True,
        "timeout": 0,
        "timeout_for_event": "presence_of_element_located",
        "event": None,
        "locator_description": "SKU morlevi"
    }
    with pytest.raises(Exception, match="Element not found and action is mandatory"):
        mock_executor.execute(locator)
```