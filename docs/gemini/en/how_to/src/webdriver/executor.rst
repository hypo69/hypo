rst
How to use the `hypotez/src/webdriver/executor.py` code block
========================================================================================

Description
-------------------------
This Python code defines the `ExecuteLocator` class for interacting with web elements using Selenium.  It handles various actions like clicking, sending messages, executing events, getting attributes, and taking screenshots of web elements.  The code supports flexible locator configurations, error handling to gracefully manage unstable elements, and supports both single and multiple web element interactions.

Execution steps
-------------------------
1. **Initialization**: Create an instance of the `ExecuteLocator` class, passing the Selenium WebDriver instance as an argument (`self.driver`).  This initializes the `ActionChains` object for interacting with elements.


2. **Locator Parsing**: The `execute_locator` method accepts a `locator` (either a dictionary or a `SimpleNamespace` object), timeout settings, and optional event details.


3. **Conversion (if needed)**: If the `locator` is a dictionary, it converts it to a `SimpleNamespace` for easier attribute access.


4. **Locator Parsing (async function `_parse_locator`):** This function:
    - Checks if the locator has specified event, attribute, or mandatory actions.
    - If not, returns `None`.
    - Parses and validates locator information (e.g., extracts the locator type from `locator.by`).
    - Handles potential exceptions (e.g., invalid locator type).


5. **Event Execution (if present):** If the locator includes an `event`, it calls the `execute_event` method to handle the requested action (e.g., clicking, typing).


6. **Attribute Retrieval (if present):** If the locator includes an `attribute`, it calls `get_attribute_by_locator` to retrieve the requested element attribute.


7. **Element Retrieval (if no event or attribute):** If no event or attribute is defined, it calls `get_webelement_by_locator` to fetch the web element(s) matching the locator. This step handles timeout settings (`timeout`) and wait conditions (`timeout_for_event`).


8. **Result Handling**: The results of event execution, attribute retrieval, or element retrieval are returned to the caller based on the requested actions.  Error handling is implemented for robust operation, including logging for debugging.



Usage example
-------------------------
.. code-block:: python

    from hypotez.src.webdriver.executor import ExecuteLocator
    from selenium import webdriver

    # Initialize the WebDriver (replace with your initialization)
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)

    # Create an instance of the ExecuteLocator class
    locator_executor = ExecuteLocator(driver=driver)


    # Example using a dictionary locator
    locator_data = {"by": "id", "selector": "myElementId", "event": "click()"}
    try:
        # Execute the locator and handle potential errors
        result = asyncio.run(locator_executor.execute_locator(locator_data))
        print(f"Result: {result}")  
    except Exception as e:
        print(f"An error occurred: {e}")
    
    # Close the WebDriver
    driver.quit()