rst
How to use the `hypotez/src/webdriver/driver.py` code block
============================================================================================

Description
-------------------------
This Python code defines a `Driver` class for interacting with Selenium web drivers in a standardized way.  It handles driver initialization, navigation, cookie management, and exception handling.  Crucially, it aims for a consistent interface across different web driver types (like Chrome, Firefox, and Edge). The code also includes methods for scrolling, fetching HTML content (from files or URLs), and determining the page's locale.

Execution steps
-------------------------
1. **Import the necessary modules:** The code imports various modules like `copy`, `pickle`, `time`, regular expressions, `pathlib`, `typing`, Selenium classes, custom modules (`header`, `gs`, `logger`), and exception handling classes. These are crucial for the functionality of the driver.
2. **Define the `Driver` class:** This class acts as a wrapper around the actual Selenium web driver.
    - The `__init__` method initializes the Selenium web driver instance using the provided `webdriver_cls` (e.g., `Chrome` from Selenium).
    - The `__init_subclass__` method is a special method that runs automatically when you create a subclass of the `Driver` class.  This method is crucial for enforcing the presence of `browser_name` for correct class instantiation.
    - `__getattr__` is a method that delegates requests to the underlying Selenium webdriver. This allows using the object like the selenium webdriver itself.
3. **Implement `scroll` method:**  This method handles page scrolling in various directions (both, up, down) with customizable parameters.  It uses a `carousel` helper function for error handling and more controlled scrolling.
4. **Implement `locale` property:** This property determines the language of the web page based on metadata tags or JavaScript checks.  Crucially, this handles the case if one approach fails and gracefully falls back to the other.
5. **Implement `get_url` method:** This method navigates to a specified URL. It includes error handling for `WebDriverException`, incorrect URLs (`InvalidArgumentException`), and general exceptions. It also saves the current URL and cookies to ensure state management.
6. **Implement `window_open` method:** This method opens a new tab in the browser window and optionally navigates to a specific URL.
7. **Implement `wait` method:** This method provides a simple delay, useful for waiting for page elements to load.
8. **Implement `_save_cookies_localy` method:** This method saves the cookies from the current session to a local file. The debug comment suggests the method is actually not functional.
9. **Implement `fetch_html` method:** This method fetches HTML content from either a local file or a web URL. It correctly handles `file://` URLs for local files, preventing errors. It also includes error handling for all types of file reading and web request errors.

Usage example
-------------------------
.. code-block:: python

    from selenium import webdriver
    from hypotez.src.webdriver.driver import Driver
    from pathlib import Path
    
    # Replace with the actual path to your chromedriver executable
    chromedriver_path = Path("/path/to/chromedriver") 
    
    # Create a Chrome driver instance, specifying the path to chromedriver
    driver = Driver(webdriver.Chrome, executable_path=str(chromedriver_path))
    
    # Navigate to a URL
    driver.get_url("https://www.example.com")

    # Fetch HTML content
    success = driver.fetch_html("https://www.example.com")

    #Check whether the page load was successful
    if success:
        # Access the HTML content
        print(driver.html_content) 

    driver.quit()