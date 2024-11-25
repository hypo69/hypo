# hypotez/src/webdriver/_examples/_example_executor_2.py

## Overview

This Python file demonstrates the usage of the `ExecuteLocator` class for various testing scenarios. It provides examples of creating an `ExecuteLocator` instance and executing different tasks using its methods, including handling errors and using lists of locators.


## Classes

### `ExecuteLocator`

**Description**:  This class is not defined within this file, but is assumed to be defined elsewhere, likely in a different file.  It handles locating and interacting with elements on a web page using various methods (XPATH, etc).

**Methods** (Not defined, assumed from usage):

- `execute_locator(locator: dict, continue_on_error: bool = False) -> dict | None`: Executes a locator to find and interact with a web element.
- `send_message(locator: dict, message: str, typing_speed: float = 0.1, continue_on_error: bool = False) -> str | None`: Sends a message to a text input field using the `send_keys` method, with optional typing speed control.
- `evaluate_locator(attribute: str) -> str | None`: Evaluates a locator to get an element's attribute value.


## Functions

(None defined in this file)


## Usage Examples


### Example 1: Simple Locator

**Description**: This example demonstrates a basic use case of `execute_locator` to retrieve the page title using XPath.

**Parameters**:

- `simple_locator (dict)`: Dictionary containing locator details.

**Returns**:

- `dict | None`: Returns a dictionary containing the element's text content if found. Returns `None` if no element is found or there's an error during execution.


### Example 2: Locator with Different Events and Attributes

**Description**: This example demonstrates a more complex use case, fetching attributes from product links and navigating through pagination.

**Parameters**:

- `complex_locator (dict)`: Dictionary containing complex locators for fetching multiple links or attributes and pagination.

**Returns**:

- `dict | None`: Returns a dictionary containing the result of the locator. `None` if there's a problem with element retrieval.

**Raises**:

- `ExecuteLocatorException`: Raised if an error occurs during the execution of the locator.




### Example 3: Error Handling and `continue_on_error`

**Description**: This example demonstrates how to handle potential errors during `execute_locator` execution using `continue_on_error = True`.

**Parameters**:

- `complex_locator (dict)`:  The locator dictionary (same as example 2).
- `continue_on_error (bool)`: Specifies if the script should continue executing even if an error occurs.


### Example 4: Sending Messages

**Description**:  This example shows how to use the `send_message` method to interact with input fields and simulating typing.

**Parameters**:

- `message_locator (dict)`: The locator dictionary for the text input field.
- `message (str)`: The message to be typed into the field.
- `typing_speed (float)`: The speed of typing.


### Example 5: Multiple Locators

**Description**: Demonstrates the usage of `execute_locator` with a list of locators.

**Parameters**:

- `multi_locator (dict)`: The dictionary containing a list of locators.


### Example 6: Evaluating Locators

**Description**:  This example showcases the `evaluate_locator` method to fetch an element's attribute value (in this case, meta description).

**Parameters**:

- `attribute_locator (dict)`: Locator dictionary including the attribute to evaluate.


### Example 7: Exception Handling

**Description**: This demonstrates how to catch and handle `ExecuteLocatorException` exceptions within the `try...except` block, which is crucial for robustness.

**Parameters**:
 - `simple_locator (dict)`: The locator dictionary.

**Raises**:

- `ExecuteLocatorException`: Raised if an error occurs during `execute_locator` execution.



### Example 8: Full Test Example

**Description**:  This example shows a complete usage scenario demonstrating the execution and handling of a locator within a test framework context.


## Setup

This example requires Selenium and other modules to be installed.


```
```
```python
from selenium import webdriver
```
```
```


## Usage

```python

# ... (Code examples from the file)
```

## Important Notes


- The examples assume that the necessary modules (`selenium`, `ExecuteLocator`, `gs`) have been imported and correctly configured.
- Error handling (`try...except`) is crucial for robustness.
- The `continue_on_error` parameter allows for more flexible error management.
- The `typing_speed` parameter provides more realistic typing simulations.
- The provided examples use a placeholder `gs['chrome_driver_path']`. Make sure to replace this with the actual path to your Chrome WebDriver executable.