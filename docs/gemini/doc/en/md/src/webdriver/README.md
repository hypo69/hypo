# WebDriver Executor

## Overview

This module provides an execution framework for navigating and interacting with web pages using a WebDriver. It processes scripts and locators to perform automated actions on web elements.

## Table of Contents

* [ExecuteLocator](#executelocator)
* [Driver](#driver)

## ExecuteLocator

### Description

The `ExecuteLocator` class is the core component for performing actions on web page elements using Selenium WebDriver. It handles locators, interactions, and error handling.

### Attributes

*   `driver`: The Selenium WebDriver instance.
*   `actions`: An `ActionChains` instance for complex actions.
*   `by_mapping`: A dictionary mapping locator strings to Selenium `By` objects.


### Methods

#### `__init__(self, driver, *args, **kwargs)`

**Description**: Initializes the WebDriver and `ActionChains`.

**Args**:
    *   `driver`: The Selenium WebDriver instance.
    *   `*args`: Variable positional arguments.
    *   `**kwargs`: Variable keyword arguments.

**Raises**:
    *   `WebDriverException`: If there's an issue initializing the WebDriver.



#### `execute_locator(self, locator: dict, message: str = None, typing_speed: float = 0, continue_on_error: bool = True) -> Union[str, list, dict, WebElement, bool]`

**Description**: Executes actions specified in the locator dictionary.

**Args**:
    *   `locator (dict)`: A dictionary containing the locator information and actions to perform.
    *   `message (str, optional)`: The message to send to an element. Defaults to `None`.
    *   `typing_speed (float, optional)`: The typing speed for sending the message. Defaults to `0`.
    *   `continue_on_error (bool, optional)`: Whether to continue on errors. Defaults to `True`.

**Returns**:
    *   `Union[str, list, dict, WebElement, bool]`: The result of the executed locator action.

**Raises**:
    *   `ExecuteLocatorException`: If there's an issue executing the locator.


#### `get_webelement_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> WebElement | List[WebElement] | bool`

**Description**: Retrieves web elements based on the provided locator.

**Args**:
    *   `locator`: Locator dictionary or SimpleNamespace object.
    *   `message (str, optional)`: Message for logging. Defaults to `None`.

**Returns**:
    *   `WebElement | List[WebElement] | bool`: The retrieved element(s) or `False` if no element is found.

**Raises**:
    *   `NoSuchElementException`: If the element is not found.
    *   `TimeoutException`: If the element is not found within the specified time.


#### `get_attribute_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> str | list | dict | bool`

**Description**: Retrieves an attribute from a web element based on the locator.

**Args**:
    *   `locator (dict | SimpleNamespace)`: Locator dictionary or SimpleNamespace object.
    *   `message (str, optional)`: Message for logging. Defaults to `None`.

**Returns**:
    *   `str | list | dict | bool`: The retrieved attribute(s) or `False` if no element is found.


#### `send_message(...)`:  (Detailed documentation to be filled in based on the function's specifics.)


#### `evaluate_locator(...)`: (Detailed documentation to be filled in based on the function's specifics.)


## Driver

### Description

The `Driver` module provides a dynamic WebDriver implementation that integrates common functionalities with additional methods for interacting with web pages.

### Detailed Description

(Expand with detailed description of the `Driver` class structure, attributes, and methods.)  This section is currently incomplete and should contain detailed descriptions of the `Driver` methods.


## Example Usage

```python
# Example usage for Driver
# (This section needs example usage for ExecuteLocator, and should have appropriate imports.)
```


```python
# Example imports (for Driver)
from src.webdriver import Driver, Chrome
from selenium.webdriver.common.by import By

```


```
```


This documentation needs further elaboration with detailed explanations, specific parameters for each method, and complete example usage sections for both `ExecuteLocator` and `Driver` classes.