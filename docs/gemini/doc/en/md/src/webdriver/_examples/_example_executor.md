# hypotez/src/webdriver/_examples/_example_executor.py

## Overview

This module provides an example of using the `ExecuteLocator` class for interacting with web elements using Selenium WebDriver. It demonstrates various functionalities, including locating elements, handling different locator types and attributes, error handling, and sending messages to web elements.  The examples cover simple, complex, error handling, message sending, multi locator, evaluation, and exception handling situations.

## Table of Contents

* [Module Overview](#overview)
* [`main` Function](#main-function)
* [Locators and Their Usage](#locators-and-their-usage)
    * [`simple_locator`](#simple-locator)
    * [`complex_locator`](#complex-locator)
* [Error Handling](#error-handling)
* [Sending Messages](#sending-messages)
* [Multi Locator Example](#multi-locator-example)
* [`evaluate_locator` Example](#evaluate-locator-example)
* [Exception Handling Example](#exception-handling-example)
* [Full Test Example](#full-test-example)

## `main` Function

### `main()`

**Description**: This function is the entry point for the example. It creates a WebDriver instance, an `ExecuteLocator` instance, performs various locator operations, and finally closes the WebDriver.


**Code**:

```python
def main():
    # ... (code of the main function) ...
```

## Locators and Their Usage

### `simple_locator`

**Description**: This locator is used to get an element's text content by XPath.

**Parameters**:

- `simple_locator` (dict): A dictionary representing the locator.


**Returns**:

- `result` (any): The result of executing the locator.


**Code**:

```python
    simple_locator = {
        "by": "XPATH",
        "selector": "//h1",
        "attribute": "textContent",
        # ... (other parameters) ...
    }
```

### `complex_locator`

**Description**: This locator demonstrates more complex usage including different attributes and events, including `product_links` and nested `pagination` data.


**Parameters**:

- `complex_locator` (dict): A dictionary representing the locator, having nested structure for complex interactions.


**Returns**:

- `result` (any): The result of executing the locator.


**Code**:

```python
    complex_locator = {
        # ... (nested structure) ...
    }
```

## Error Handling

**Description**: This section demonstrates how to handle exceptions using a `try...except` block within the `execute_locator` method.

**Code**:

```python
    try:
        locator.execute_locator(complex_locator, continue_on_error=True)
    except ExecuteLocatorException as ex:
        print(f"An error occurred: {ex}")
```

## Sending Messages

**Description**: This section demonstrates how to send messages (e.g., type text into input fields) using the `send_message` method.

**Code**:

```python
    message_locator = {
        "by": "XPATH",
        "selector": "//input[@name=\'search\']",
        # ...
    }
    message = "Buy a new phone"
    result = locator.send_message(message_locator, message, typing_speed=0.05, continue_on_error=True)
    print(f"Result of sending message: {result}")
```

## Multi Locator Example


**Description**: This section demonstrates how to execute a locator with multiple elements.

**Code**:

```python
    multi_locator = {
        # ... (list of locators) ...
    }

    results = locator.execute_locator(multi_locator)
    print(f"Results of executing multiple locators: {results}")
```

## `evaluate_locator` Example


**Description**: This section demonstrates the `evaluate_locator` method, which is used to retrieve an attribute value.

**Code**:

```python
    attribute_locator = {
        # ... (locator details) ...
    }
    attribute_value = locator.evaluate_locator(attribute_locator['attribute'])
    print(f"Attribute value: {attribute_value}")
```

## Exception Handling Example

**Description**: This section demonstrates exception handling to catch and print specific exceptions related to the `ExecuteLocator` operations.

**Code**:

```python
    try:
        locator.execute_locator(simple_locator)
    except ExecuteLocatorException as ex:
        print(f"An error occurred during locator execution: {ex}")
```

## Full Test Example

**Description**: This section showcases a complete example that utilizes all the functionalities to perform a full test sequence.


**Code**:

```python
    test_locator = {
        # ... (locator details) ...
    }

    result = locator.execute_locator(test_locator)
    print(f"Result of executing test locator: {result}")
```


```
```