rst
How to use the `ExecuteLocator` class
========================================================================================

Description
-------------------------
The `ExecuteLocator` class provides a framework for interacting with web pages using a WebDriver. It handles locators (e.g., XPath, ID, CSS) to find and manipulate web elements, send messages, take screenshots, and more.  It's designed to process actions specified in dictionaries, enabling automated web interactions.

Execution steps
-------------------------
1. **Import necessary modules:**  Import the `ExecuteLocator` class and other required Selenium components, along with utility functions.

2. **Create a WebDriver instance:** Instantiate a WebDriver object (e.g., `Chrome`, `Firefox`).

3. **Initialize the `ExecuteLocator` object:** Create an instance of the `ExecuteLocator` class, passing the WebDriver instance as an argument.

4. **Define a locator dictionary:** Create a dictionary containing instructions for finding and interacting with the desired web element(s).  The format for the locator is crucial.

5. **Execute the locator:** Call the `execute_locator` method of the `ExecuteLocator` object, passing the locator dictionary and any additional parameters (e.g., message to send, typing speed).

6. **Handle results:** The `execute_locator` method returns the result of the action.  Interpret the result based on the intended operation (e.g., if it's a WebElement, further methods can be called).  Error handling is crucial.


Usage example
-------------------------
.. code-block:: python

    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from src.webdriver.executor import ExecuteLocator  # Replace with the actual path

    # Replace with your actual WebDriver
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)

    # Initialize the ExecuteLocator
    executor = ExecuteLocator(driver)

    # Example locator dictionary (adjust as needed)
    locator = {
        "by": "xpath",
        "selector": "//input[@id='myInput']",
        "action": "send_message",
        "message": "Hello world!",
        "typing_speed": 0.2,
        "timeout": 10,  # timeout in seconds
        "timeout_for_event":"presence_of_element_located",
        "event": null,
        "mandatory":True
    }

    # Execute the locator
    result = executor.execute_locator(locator)

    # Check the result (error handling is crucial!)
    if result is True:
        print("Action completed successfully.")
    elif result is False:
      print("Action failed.")
    elif isinstance(result, Exception):
      print(f"An exception occurred: {result}")
    else:
        print(f"Element found with text: {result.text}")

    driver.quit()