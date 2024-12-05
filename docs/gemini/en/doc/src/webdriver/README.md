# WebDriver Executor

## Overview

This module provides a framework for interacting with web pages using a WebDriver. It handles various actions like navigation, element interaction, screenshot capture, and more, based on locator dictionaries.  It uses Selenium WebDriver under the hood.

## Table of Contents

* [ExecuteLocator](#executelocator)
* [Driver](#driver)


## ExecuteLocator

### Description

The `ExecuteLocator` class is the core of this module. It processes locator dictionaries to perform actions on web elements. It handles various locator types, actions, and exception handling.

### Attributes

* `driver`: The Selenium WebDriver instance.
* `actions`: ActionChains object for complex interactions.
* `by_mapping`: A dictionary mapping locator strings to Selenium `By` constants.


### Methods

#### `__init__(self, driver, *args, **kwargs)`

**Description:** Initializes the `ExecuteLocator` with the WebDriver instance and optional arguments.

**Args:**
  * `driver`: The Selenium WebDriver instance.
  * `*args`: Variable positional arguments.
  * `**kwargs`: Variable keyword arguments.

**Returns:**
  None

#### `execute_locator(self, locator: dict, message: str = None, typing_speed: float = 0, continue_on_error: bool = True) -> Union[str, list, dict, WebElement, bool]`

**Description:** Executes the actions defined in the `locator` dictionary.

**Args:**
  * `locator (dict)`: A dictionary containing instructions for locating and interacting with elements.
  * `message (str, optional)`: The text to type into a field. Defaults to None.
  * `typing_speed (float, optional)`: Typing speed for text input (in seconds per character). Defaults to 0 (no delay).
  * `continue_on_error (bool, optional)`: Whether to continue execution if an error occurs. Defaults to True.

**Returns:**
  `Union[str, list, dict, WebElement, bool]`: The result of the executed action (e.g., retrieved text, list of elements, etc.) or False if an error occurred and `continue_on_error` is False.


#### `get_webelement_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> WebElement | List[WebElement] | bool`

**Description:** Retrieves web elements based on the provided locator.

**Args:**
  * `locator (dict | SimpleNamespace)`: The locator dictionary or object containing the element location details.
  * `message (str, optional)`: The message for logging purposes. Defaults to None.


**Returns:**
  `WebElement | List[WebElement] | bool`: A `WebElement` object or list of `WebElement` objects representing the found element(s), or False if no element is found.


#### `get_attribute_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> str | list | dict | bool`

**Description:** Retrieves an attribute from a web element identified by the locator.

**Args:**
  * `locator (dict | SimpleNamespace)`: The locator dictionary or object containing the element location details.
  * `message (str, optional)`: The message for logging purposes. Defaults to None.

**Returns:**
  `str | list | dict | bool`: The retrieved attribute value or False if no element or attribute is found.


#### `send_message(self, locator: dict | SimpleNamespace, message: str, typing_speed: float, continue_on_error: bool) -> bool`

**Description:** Sends text input to a web element identified by the locator.

**Args:**
 * `locator (dict | SimpleNamespace)`: The locator dictionary or object containing the element location details.
 * `message (str)`: The text to input.
 * `typing_speed (float)`: The typing speed in seconds per character.
 * `continue_on_error (bool)`: Continue on error.

**Returns:**
  `bool`: True if the message was sent successfully, False otherwise.


#### Other Methods (Refer to the original code for detailed documentation):


## Driver

### Description

The `Driver` class provides a wrapper around various WebDriver implementations (e.g., Chrome, Firefox), extending base functionality.

### Attributes (Refer to the original code for details)


### Methods (Refer to the original code for details)


## Error Handling

The module employs `try...except` blocks to catch and log various exceptions, such as `NoSuchElementException`, `TimeoutException`, and others.


## Dependencies

* Selenium
* Python Standard Library modules (e.g., `time`, `sys`)
* Internal modules (e.g., `src.utils`, `src.logger`)

## Usage (Examples provided in the original Python code)



```