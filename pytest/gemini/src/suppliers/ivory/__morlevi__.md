```python
import pytest
import os
from unittest.mock import patch
from hypotez.src.suppliers.ivory.__morlevi__ import login, grab_product_page, list_products_in_category_from_pagination, get_list_products_in_category, get_list_categories_from_site
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
import pandas as pd
from pathlib import Path


# Dummy classes and fixtures for testing (replace with actual implementation)
class Supplier:
    def __init__(self, driver, locators, settings, supplier_prefix):
        self.driver = driver
        self.locators = locators
        self.settings = settings
        self.supplier_prefix = supplier_prefix

    def get_url(self, url):
        self.driver.get(url)

    def page_refresh(self):
        self.driver.refresh()
    
    def execute_locator(self, locator):
        return [WebElement(i) for i in locator] # Dummy implementation

    def wait(self, seconds):
        pass # Dummy implementation

    def click(self, locator):
        pass # Dummy implementation
        

    def save_and_send_via_ftp(self, data):
        pass # Dummy implementation

class Driver:
    def __init__(self):
        self.current_url = ""
    def get(self, url):
        self.current_url = url
    def refresh(self):
        pass
    def switch_to_active_element(self):
        pass
    def execute_locator(self, locator):
        return [f"element{i}" for i in range(len(locator))] # Dummy implementation
    def title(self):
        return "Test Title"
    def current_url(self):
        return self.current_url

    def page_source(self):
        return "page source"


@pytest.fixture
def supplier_instance():
    driver = Driver()
    locators = {'login': {'open_login_dialog_locator': 'login_dialog', 'email_locator': 'email', 'password_locator': 'password', 'loginbutton_locator': 'login_button', 'close_pop_up_locator': 'close_popup'}, 'product': {'sku_locator': 'sku', 'summary_locator': 'summary', 'description_locator': 'description', 'price_locator': 'price', 'product_name_locator': 'product_name', 'link_to_product_locator': 'product_link', 'main_image_locator': 'main_image', 'product_delivery_locator': 'delivery'}, 'pagination':{'a': ['next_page_1','next_page_2']}}
    settings = {'price_rule': '*1'}
    supplier_prefix = 'test'
    return Supplier(driver, locators, settings, supplier_prefix)

def test_login_successful(supplier_instance):
    with patch('hypotez.src.suppliers.ivory.__morlevi__.logger') as mock_logger:
        result = login(supplier_instance)
        assert result is True
        mock_logger.debug.assert_any_call('Sobsno, login Morlevi')
        mock_logger.debug.assert_any_call('Mor logged in')
        

def test_login_failure(supplier_instance):
    with patch('hypotez.src.suppliers.ivory.__morlevi__.logger') as mock_logger:
        with patch('hypotez.src.suppliers.ivory.__morlevi__.Supplier.page_refresh') as mock_refresh:
            result = login(supplier_instance)
            assert result is None
            mock_logger.error.assert_called_with("Ошибка, пытаюсь закрыть popup")
            mock_refresh.assert_called_once()


# Add more test cases for other functions (grab_product_page, etc.)
def test_grab_product_page(supplier_instance):
    with patch('hypotez.src.suppliers.ivory.__morlevi__.logger') as mock_logger:
        result = grab_product_page(supplier_instance)
        assert result is not None  # Or check specific fields of the returned Product object
        mock_logger.error.assert_not_called()

def test_list_products_in_category_from_pagination(supplier_instance):
    with patch('hypotez.src.suppliers.ivory.__morlevi__.logger') as mock_logger:
        result = list_products_in_category_from_pagination(supplier_instance)
        assert isinstance(result, list) or result is None

# Add more test cases, covering various scenarios and edge cases
# Test cases for get_list_products_in_category, get_list_categories_from_site


```

**Explanation and Improvements:**

1. **Dummy Classes and Fixtures:**  Crucially, the code now includes `Supplier` and `Driver` classes, along with a `supplier_instance` fixture.  This is essential because the original code uses `self.driver`, `self.locators`, etc., which need concrete objects to work with during testing. The `Driver` and `Supplier` classes are *mocks* that simulate the actual behavior for testing.

2. **Mocking:** The `@patch` decorator from `unittest.mock` is used to mock the `logger` object.  This prevents your tests from relying on the actual logger (which might interact with external systems like files).  Also, a mock for `Supplier.page_refresh` is added.

3. **Assertions:** Assertions are added to verify that the expected behaviors happen.  For example, `assert result is True` for a successful login.  Also, assertions are now checking if the `result` from `grab_product_page` is not `None`.

4. **Clearer Test Cases:** Test names like `test_login_successful` and `test_login_failure` make the tests more understandable.

5. **Edge Case Testing:**  The `test_login_failure` test now includes a mock for `Supplier.page_refresh` to ensure that a refresh is attempted in case of login failure.

6. **Comprehensive Tests:** The example now includes more specific tests for `login` and `grab_product_page` but more are needed for the entire codebase.


**How to Use and Adapt:**


1. **Replace Dummy Implementations:** Replace the placeholder `...` implementations in the `Supplier` and `Driver` classes with actual code for interacting with your web driver and locators.

2. **Add Tests for Missing Functions:** Create test functions for the missing functions.  Analyze the functions' logic, consider different scenarios, valid/invalid inputs, boundary conditions, etc., and write specific tests to check their behavior.  Focus on testing exception handling and the various return values for different situations.



**Important Considerations:**

- **WebDriver Setup:** You need a way to initialize and control a web driver (e.g., using Selenium).  Ensure you've installed Selenium and other required libraries. This should be part of your test setup.

- **Locators:** The tests now need locator strings, or methods to get locators.

- **Data-Driven Tests:** For functions that take complex or various input data, create fixtures to provide test data.  This makes your tests more reusable and maintainable.

- **Error Handling:** The original code had many `except ...` blocks without handling exceptions effectively. Modify those for improved error handling in tests and your production code.
- **`pytest.raises`:** For exceptions, use `pytest.raises` to specifically test expected exceptions.


This revised response provides a solid starting point for your `pytest` test suite. Remember to replace the dummy implementations and add more comprehensive tests for the rest of the functions. Remember to install necessary libraries `pytest` and `unittest.mock`.