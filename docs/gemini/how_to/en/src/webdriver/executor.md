```python
# Usage Guide for hypotez/src/webdriver/executor.py

This module, `executor.py`, provides functions for interacting with web elements using Selenium. It handles various actions like clicking, sending messages, executing events, and retrieving attributes from elements, while offering robust error handling and support for multiple locator types.

**Key Concepts:**

* **Locators:**  Configurations (dictionaries or `SimpleNamespace` objects) defining how to locate web elements.  The `by` key in the locator specifies the locating method (e.g., "XPATH", "ID").  The `selector` key provides the actual locator value.
* **`ExecuteLocator` Class:** The central class for executing actions on web elements.  It takes a `driver` object (from Selenium) and a locator.
* **Error Handling:** The module is designed to continue execution even if an error occurs during locating or interacting with an element.  This is crucial for automating complex web interactions where elements might be unstable.  Error messages include debugging information to aid in troubleshooting.
* **Flexibility:**  The module handles different locator formats (dicts, `SimpleNamespace`) seamlessly.  It supports various actions (clicks, sending messages, pausing).
* **Asynchronous Operations:** The `async`/`await` syntax is used for efficient handling of tasks.  This allows the script to continue working with other elements while waiting for elements to appear.

**How to use:**

1. **Initialization:**

   ```python
   from hypotez.src.webdriver import executor  # Import the module
   from selenium import webdriver  # Import Selenium webdriver

   # Create a webdriver instance (replace with your driver type)
   driver = webdriver.Chrome()  

   # Initialize the ExecuteLocator class
   executor_instance = executor.ExecuteLocator(driver=driver)
   ```

2. **Creating a Locator:**

   ```python
   locator_data = {
       "by": "XPATH",
       "selector": "//button[@id='submit']",
       "event": "click()"  # Add event
   }
   ```

   You can also create a `SimpleNamespace` object for the locator:

   ```python
   from types import SimpleNamespace

   locator = SimpleNamespace(
       by="ID",
       selector="submitButton",
       event="click()",
   )
   ```

3. **Executing the Locator:**

   ```python
   try:
       result = await executor_instance.execute_locator(locator=locator_data)
       print(f"Result: {result}")
   except Exception as e:
       print(f"An error occurred: {e}")
   ```

**Important Functions and their parameters:**

* **`execute_locator`:**  The main function to execute actions based on the provided locator. Takes the `locator` (dict or `SimpleNamespace`) and optional parameters like `timeout`, `timeout_for_event` (for wait conditions), `message` (for sending text).

* **`get_webelement_by_locator`:** Locates a web element based on the provided locator and waits for it to be present. Crucial for robust interactions.

* **`get_attribute_by_locator`:** Retrieves attributes from the found element(s).  Note the support for retrieving multiple attributes and for parsing of attribute dictionaries.

* **`execute_event`:** Executes various actions like clicking, sending keys, pausing, uploading media, and taking screenshots.  This function is the heart of the interaction logic.

* **`send_message`:** Sends a message to a web element, handling special character replacements and typing speed.

**Example using `send_message`:**

```python
message_locator = {
    "by": "ID",
    "selector": "messageBox",
    "event": "type(Hello, World)",  # Use type event with arguments
}
await executor_instance.send_message(message_locator, message="Hello World", typing_speed=0.1)

```


**Error Handling:**

The `try...except` block is crucial for catching and handling exceptions during locator execution. The use of `logger` ensures that errors are logged with helpful information.

**Best Practices:**

* Always close the `driver` object when finished:
  ```python
  driver.quit()
  ```
* Use appropriate `timeout` values to prevent indefinite waits.
* Thoroughly test your locators to ensure accuracy.

This guide provides a structured overview of how to use the `executor` module.  Remember to consult the `hypotez/src/webdriver/executor.py` code for detailed function signatures and behavior. Remember to run the code in an asynchronous context (e.g., using `asyncio.run(main())`) if you are using the async functions.
```