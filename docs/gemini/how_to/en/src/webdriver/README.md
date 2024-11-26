# Usage Guide: WebDriver Executor (`hypotez/src/webdriver`)

This guide explains how to use the `Driver` module, specifically the `ExecuteLocator` class, within the `hypotez/src/webdriver` directory for web automation tasks using Selenium WebDriver.

## `Driver` Module Overview

The `Driver` module provides a framework for interacting with web pages using a WebDriver. It enhances basic WebDriver functionality with methods for scrolling, cookie management, and more.  Crucially, it integrates with the `ExecuteLocator` class for sophisticated interactions based on locator dictionaries.

### Key Components

* **`Driver` class:** This class acts as a wrapper around a specific WebDriver implementation (e.g., Chrome, Firefox).  It's designed to be easily extended and customized.
* **`ExecuteLocator` class:**  This class is the core of the locator-based interaction logic.  It takes a `Driver` instance and a locator dictionary to perform actions on web elements.

### `ExecuteLocator` Class in Depth

The `ExecuteLocator` class handles the bulk of the element interaction.

#### Initialization (`__init__`)

```python
from src.webdriver import ExecuteLocator, Chrome  # Or your WebDriver class

driver = Chrome()  # Or any other WebDriver instance
locator_executor = ExecuteLocator(driver)
```

This creates an `ExecuteLocator` instance tied to a specific WebDriver.  Any further interactions will leverage this driver.

#### Locator Execution (`execute_locator`)

This is the core method for performing actions based on a locator dictionary:

```python
locator_data = {
    "element_to_locate": {
        "by": "xpath",  # Or "id", "css_selector", etc.
        "value": "//element[@id='my_element']",
        "action": "click"  # Or "send_keys", etc.
    }
}

result = locator_executor.execute_locator(locator_data)
```

The `locator_data` dictionary defines how and what to interact with. The `action` key specifies the desired interaction.  The return value (`result`) may vary depending on the action (e.g., a boolean indicating success/failure, the retrieved element, etc.).

#### Element Retrieval (`get_webelement_by_locator`)

Locates web elements.

```python
element = locator_executor.get_webelement_by_locator({"by": "id", "value": "some_id"})
```

This method returns the located element or `False` if not found, handling potential exceptions (e.g., `NoSuchElementException`).

#### Attribute Retrieval (`get_attribute_by_locator`)

Retrieves attributes from elements.

```python
attribute_value = locator_executor.get_attribute_by_locator({"by": "xpath", "value": "//element[@id='my_element']", "attribute": "href"})
```

#### Message Sending (`send_message`)

Sends text to an element.

```python
locator_executor.send_message({"by": "id", "value": "input_field"}, "My Input Text", typing_speed=0.1)
```

The `typing_speed` parameter controls the input speed.

#### Screenshots (`get_webelement_as_screenshot`)

Captures screenshots of elements.

```python
screenshot = locator_executor.get_webelement_as_screenshot({"by": "id", "value": "some_id"})
```

#### Click Action (`click`)

Performs a click operation.

```python
locator_executor.click({"by": "xpath", "value": "//button[@id='submit']"})
```


## Example Usage (from your code)


```python
from selenium.webdriver.common.by import By
from src.webdriver import Driver, Chrome

def main():
    driver = Driver(Chrome)  # Initialize the driver
    driver.get_url("https://www.example.com")  # Navigate to a URL

    # Example usage of ExecuteLocator (using a simplified locator)
    locator_executor = ExecuteLocator(driver)  # Initialize the locator executor with the driver

    try:
        element = locator_executor.get_webelement_by_locator({"by": By.ID, "value": "myElementID"})

        if element:
            driver.save_screenshot("screenshot.png")  # Save a full page screenshot
            attribute_value = locator_executor.get_attribute_by_locator({"by": By.ID, "value": "myElementID", "attribute": "text"})
            print(f"Element Text: {attribute_value}")  # Print the text attribute
            locator_executor.click({"by": By.ID, "value": "someButtonID"})
            print("Button clicked successfully")
    except Exception as e:
        print(f"Error: {e}")  # Handle errors gracefully


if __name__ == "__main__":
    main()

```

**Important Considerations:**

* **Error Handling:** The code demonstrates basic error handling with `try...except`. Implement comprehensive error handling to manage various potential exceptions within your specific use cases.
* **Locator Format:**  Ensure your locator dictionaries conform to the expected format, as shown in the examples.  Refer to the module's docstrings for detailed information about locator requirements and return types.


This guide provides a starting point. Consult the module's source code (`hypotez/src/webdriver/__init__.py` and other related files) for detailed method signatures, exception handling specifications, and specific examples.  Adjust the example usage to match your precise needs. Remember to install the necessary dependencies, especially Selenium.