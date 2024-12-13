```python
import pytest
from types import SimpleNamespace

# Mock Executor class to avoid actual web interactions during testing
class MockExecutor:
    def __init__(self):
        self.last_action = None
        self.elements = {}
        self.screenshot_data = b"mock_screenshot"

    def find_elements(self, by, selector):
        if selector in self.elements:
            return self.elements[selector]
        return []

    def click(self, element):
        self.last_action = f"Clicked on {element}"

    def get_attribute(self, element, attribute):
       if isinstance(element, dict) and attribute in element:
            return element[attribute]
       return f"Attribute {attribute} of {element}"

    def get_inner_text(self, element):
      if isinstance(element, dict) and "innerText" in element:
        return element["innerText"]
      return f"innerText of {element}"
      
    def screenshot(self, element):
        self.last_action = f"Took screenshot of {element}"
        return self.screenshot_data

    def execute_locator(self, locator):
       
        if not isinstance(locator, SimpleNamespace):
            locator = SimpleNamespace(**locator)
        
        if locator.by == "VALUE":
            return locator.attribute
        
        elements = self.find_elements(locator.by, locator.selector)
        
        if not elements and locator.mandatory:
            raise Exception("Element not found and action is mandatory")
        
        if not elements:
            return None
        
        element = elements[0] if locator.if_list == "first" else elements
        
        if locator.event == "click()":
           self.click(element)
        elif locator.event == "screenshot()":
            return self.screenshot(element)

        if locator.attribute == "src":
           if isinstance(element, list):
              return [self.get_attribute(e, locator.attribute) for e in element]
           return self.get_attribute(element, locator.attribute)
        elif locator.attribute == "innerText":
           return self.get_inner_text(element)
        elif locator.attribute:
           if isinstance(element,list):
            return [self.get_attribute(e, locator.attribute) for e in element]
           return self.get_attribute(element,locator.attribute)
        
        return None
        

@pytest.fixture
def mock_executor():
    return MockExecutor()

# Test case for close_banner locator
def test_close_banner_valid_input(mock_executor):
    """Test successful click on banner element when element is found."""
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
        "locator_description": "Close the pop-up window, if it does not appear - it's okay (`mandatory`:`false`)"
    }
    mock_executor.elements["//button[@id = 'closeXButton']"] = ["mock_element"]
    mock_executor.execute_locator(locator)
    assert mock_executor.last_action == "Clicked on mock_element"

def test_close_banner_element_not_found_not_mandatory(mock_executor):
    """Test when element not found and action is not mandatory."""
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
        "locator_description": "Close the pop-up window, if it does not appear - it's okay (`mandatory`:`false`)"
    }
    result = mock_executor.execute_locator(locator)
    assert result is None
    assert mock_executor.last_action is None


# Test case for id_manufacturer locator
def test_id_manufacturer_valid_input(mock_executor):
    """Test returning the attribute value when 'by' is set to 'VALUE'."""
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
    result = mock_executor.execute_locator(locator)
    assert result == 11290

# Test case for additional_images_urls locator
def test_additional_images_urls_valid_input(mock_executor):
    """Test extracting 'src' attribute values from multiple elements."""
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
    mock_executor.elements["//ol[contains(@class, 'flex-control-thumbs')]//img"] = [
        {"src": "url1"}, {"src": "url2"}
    ]
    result = mock_executor.execute_locator(locator)
    assert result == "Attribute src of {'src': 'url1'}"

def test_additional_images_urls_element_not_found_not_mandatory(mock_executor):
    """Test when element not found and action is not mandatory."""
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
    result = mock_executor.execute_locator(locator)
    assert result is None


# Test case for default_image_url locator
def test_default_image_url_valid_input(mock_executor):
    """Test screenshot action on an element."""
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
        "locator_description": "Attention! In Morlevi, the image is obtained via screenshot and returned as png (`bytes`)"
    }
    mock_executor.elements["//a[@id = 'mainpic']//img"] = ["mock_element"]
    result = mock_executor.execute_locator(locator)
    assert result == mock_executor.screenshot_data
    assert mock_executor.last_action == "Took screenshot of mock_element"
    

def test_default_image_url_element_not_found_mandatory(mock_executor):
    """Test exception is raised when element not found and action is mandatory."""
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
        "locator_description": "Attention! In Morlevi, the image is obtained via screenshot and returned as png (`bytes`)"
    }
    with pytest.raises(Exception, match="Element not found and action is mandatory"):
        mock_executor.execute_locator(locator)

# Test case for id_supplier locator
def test_id_supplier_valid_input(mock_executor):
    """Test extracting the text content of an element."""
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
    mock_executor.elements["//span[@class = 'ltr sku-copy']"] = [{"innerText":"SKU123"}]
    result = mock_executor.execute_locator(locator)
    assert result == "innerText of {'innerText': 'SKU123'}"

def test_id_supplier_element_not_found_mandatory(mock_executor):
    """Test exception is raised when element not found and action is mandatory."""
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
        mock_executor.execute_locator(locator)
```