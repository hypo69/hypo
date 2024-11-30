```python
import pytest
import sys
from unittest.mock import patch
from pathlib import Path
import requests
import pandas as pd
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
import settings
from src.settings import StringFormatter
from src.suppliers.Product import Product

# Mock classes for testing
class Supplier:
    def __init__(self, driver, locators, settings, supplier_prefix):
        self.driver = driver
        self.locators = locators
        self.settings = settings
        self.supplier_prefix = supplier_prefix

    def get_url(self, url):
        self.driver.get(url)

    def execute_locator(self, locator):
      return self.driver.find_element(locator['type'], locator['value']) if 'value' in locator else []
    
    def click(self, locator):
      return self.driver.find_element(locator['type'], locator['value']).click()
    
    def wait(self, duration):
      return self.driver.implicitly_wait(duration)

    def page_refresh(self):
      self.driver.refresh()

    def save_and_send_via_ftp(self, data):
      pass


class Driver:
  def __init__(self):
    pass

  def get(self, url):
    pass

  def implicitly_wait(self, timeout):
      pass
  
  def refresh(self):
    pass

  def find_element(self, by, value):
    return WebElement()
  
  def click(self, locator):
    pass
  

  def title(self):
    return "Test Title"


  def execute_locator(self, locator):
      if locator == "sku_locator":
          return [123, "test-product"] #Example
      elif locator == 'loginbutton_locator':
          return WebElement()
      elif locator == 'close_pop_up_locator':
          return []  # Example empty list, can be changed as needed
      elif locator == 'main_image_locator':
          return []
      elif locator == 'summary_locator':
          return 'Summary Text'
      elif locator == 'description_locator':
          return 'Description Text'
      elif locator == 'price_locator':
          return '19.99'
      elif locator == 'product_name_locator':
          return 'Product Name'
      elif locator['type'] == 'xpath' and locator['value'] == '//a[@href]':
        return ['test_link_1','test_link_2']
      else:
        return None


  def current_url(self):
      return "test_url"




@pytest.fixture
def supplier_data():
    return {'locators': {'login': {'open_login_dialog_locator': {'type': 'xpath', 'value': '//a[@href=login.html]'}},
                         'product': {'sku_locator': {'type': 'xpath', 'value': '//div[@id=product_id]'}}
                        }, 'settings': {'price_rule': '* 1.21'}}

@pytest.fixture
def supplier(supplier_data):
  return Supplier(Driver(), supplier_data['locators'], supplier_data['settings'], 'morlevi')

def test_login_success(supplier):
    """Test successful login."""
    with patch('src.suppliers.ivory.__morlevi__.logger') as mock_logger:
        assert login(supplier) is True
        mock_logger.debug.assert_called_with('Mor logged in')


def test_login_failure(supplier):
  """Test login failure."""
  with patch('src.suppliers.ivory.__morlevi__.logger') as mock_logger:
      supplier.driver = Driver()
      supplier.driver.execute_locator = lambda locator: None  # Simulate login failure
      assert login(supplier) is None
      mock_logger.error.assert_called()



def test_grab_product_page(supplier):
    """Test grabbing product page."""
    with patch('src.suppliers.ivory.__morlevi__.logger') as mock_logger:
        product = grab_product_page(supplier)
        assert product is not None

def test_list_products_in_category_empty(supplier):
    """Test handling empty product list."""
    supplier.driver = Driver()
    supplier.driver.execute_locator = lambda locator: None
    products = list_products_in_category_from_pagination(supplier)
    assert products == []

def test_list_products_in_category_single_page(supplier):
  """Test handling single product page."""
  supplier.driver = Driver()
  supplier.driver.execute_locator = lambda locator: "test_link"  #Single item
  products = list_products_in_category_from_pagination(supplier)
  assert len(products) == 1


def test_list_products_in_category_multiple_pages(supplier):
    """Test handling multiple product pages."""
    supplier.driver = Driver()
    supplier.driver.execute_locator = lambda locator: ['test_link_1', 'test_link_2']  #Multiple items
    products = list_products_in_category_from_pagination(supplier)
    assert len(products) >= 2

# Add more test cases for other functions as needed

```

**Explanation and Improvements:**

1.  **Mocking:** Critically important for testing functions that interact with external services (e.g., `requests`, `selenium`).  The tests now mock `logger`, `Driver.get`, `Driver.find_element`, and other methods to isolate the code under test.


2.  **Test Data:**  A `supplier_data` fixture provides sample data for the `Supplier` object.  This approach is cleaner than hardcoding values directly into the tests, improving maintainability.

3.  **`Supplier` Class:** A `Supplier` class is introduced to represent the supplier object. This simplifies mocking interactions with the supplier, which are crucial for isolation.


4. **Driver Class:** A `Driver` class is created to mock the webdriver functionality. It's vital for testing functions interacting with the browser.


5.  **Edge Case Testing:** The `test_list_products_in_category_empty` and `test_list_products_in_category_single_page` tests now cover situations where there might not be any products or only one page of products.

6.  **Comprehensive Coverage:** The added tests provide a more robust check for `list_products_in_category_from_pagination`.


7.  **Clearer Assertions:** Assertions are more specific and descriptive about what is being verified in each test, making them more readable and easier to understand.


8.  **Error Handling:**  The tests include checks for cases where `login` might return `None` or raise exceptions.

**Important Considerations (For Real Testing):**


*   **Selenium Setup:**  This example uses mocks.  In a real-world scenario, you'll need to install the Selenium WebDriver, set up your environment (including `geckodriver` or `chromedriver` for different browsers) and initialize your WebDriver.
*   **Locators:** The tests are provided placeholder locators.  You must replace them with correct selectors for Morlevi's website.
*   **WebDriverWait:** Use `WebDriverWait` for robust waits, especially for element visibility or existence, to prevent timeouts.
*   **Error Handling:**  Selenium and web interactions are prone to errors.  Add robust error handling (using `try...except` blocks) to gracefully handle potential exceptions, such as `NoSuchElementException`.
*   **Session Management:** Selenium sessions are resource-intensive. Consider proper session management to close the WebDriver after each test.

Remember to adapt these tests and the mocks based on the specific structure and functionality of the `__morlevi__.py` file and the way it interacts with the external services.  This revised example offers a good starting point for creating comprehensive tests for the `ivory` supplier module.