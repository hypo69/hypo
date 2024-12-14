```python
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Fixture for setting up the Firefox webdriver with the test extension
@pytest.fixture(scope="module")
def firefox_driver_with_extension():
    """Sets up a Firefox webdriver instance with the test extension loaded."""
    
    # Path to the extension directory
    extension_path = "hypotez/src/webdriver/firefox/extentions/test_extention"  
    
    # Configure Firefox options
    options = Options()
    options.add_extension(extension_path)
    
    # Initialize the webdriver
    driver = webdriver.Firefox(options=options)
    
    yield driver # provide the driver to the tests
    
    driver.quit()  # Clean up driver after all tests in module

def test_borderify_extension_applies_border(firefox_driver_with_extension):
    """
    Test that the borderify extension correctly applies a red border to the document body.
    This verifies that the extension is loaded and executes its JavaScript code successfully.
    """
    driver = firefox_driver_with_extension
    
    # Open a basic test HTML page (can be a local file or a simple online page)
    driver.get("data:text/html;charset=utf-8,<html><body><h1>Test Page</h1></body></html>")
    
    # Wait for some time to let extension load and execute, which may need time to complete. 
    time.sleep(1)

    # Get the border style of the body element.
    body_element = driver.find_element("tag name", "body")
    border_style = body_element.get_property('style').get("border")
    
    # Check if the border style is as expected.
    assert border_style == "5px solid red", f"Expected '5px solid red' border, but got: {border_style}"
    
def test_borderify_extension_does_not_interfere_with_page(firefox_driver_with_extension):
    """
    Test that the borderify extension does not interfere with the page's content or structure.
    This is to make sure the extension is only changing the CSS border and nothing else.
    """
    driver = firefox_driver_with_extension

    # Open a page
    driver.get("data:text/html;charset=utf-8,<html><body><h1>Test Page</h1><p>Some Content.</p></body></html>")
   
    time.sleep(1) # wait for extension
    
    # Test if h1 element is still present
    h1_element = driver.find_element("tag name", "h1")
    assert h1_element.text == "Test Page", "h1 element should still display 'Test Page'."
    
    # Test if the p element is still present
    p_element = driver.find_element("tag name", "p")
    assert p_element.text == "Some Content.", "p element should still display 'Some Content'."

def test_borderify_extension_alert_not_present(firefox_driver_with_extension):
    """
    Test that the alert function that is present in the extension's code is NOT executed.
    This tests that the alert is suppressed and doesn't appear.
    """
    driver = firefox_driver_with_extension
    
    # Load test page
    driver.get("data:text/html;charset=utf-8,<html><body><h1>Test Page</h1></body></html>")

    # Use WebDriverWait to check if an alert is present (with a timeout).
    # Expected to raise a timeout exception which indicates the alert did NOT appear
    with pytest.raises(Exception) as excinfo:
      WebDriverWait(driver, 1).until(EC.alert_is_present())
    assert "Message: timeout" in str(excinfo.value) , "alert should NOT appear, but it seems it is"
    
```