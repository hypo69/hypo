# WebDriver Executor

## Overview

This module provides the `ExecuteLocator` class for interacting with web pages using Selenium WebDriver. It handles various actions based on locator dictionaries, including element selection, attribute retrieval, message sending, and more.  Error handling is implemented to gracefully manage potential issues.


## Table of Contents

- [Overview](#overview)
- [ExecuteLocator Class](#executelocator-class)
    - [Class Attributes](#class-attributes)
    - [Class Methods](#class-methods)
        - [`__init__(self, driver, *args, **kwargs)`](#init-self-driver-args-kwargs)
        - [`execute_locator(self, locator: dict, message: str = None, typing_speed: float = 0, continue_on_error: bool = True)`](#executelocator-self-locator-message-typing_speed-continue_on_error)
        - [`get_webelement_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> WebElement | List[WebElement] | bool`](#getwebelementbylocator-self-locator-message)
        - [`get_attribute_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> str | list | dict | bool`](#getattributebylocator-self-locator-message)
        - [`_get_element_attribute(self, element: WebElement, attribute: str) -> str | None`](#_getelementattribute-self-element-attribute)
        - [`send_message(self, locator: dict | SimpleNamespace, message: str, typing_speed: float, continue_on_error:bool) -> bool`](#sendmessage-self-locator-message-typing_speed-continue_on_error)
        - [`evaluate_locator(self, attribute: str | list | dict) -> str`](#evaluatelocator-self-attribute)
        - [`_evaluate(self, attribute: str) -> str | None`](#_evaluate-self-attribute)
        - [`get_locator_keys() -> list`](#getlocatorkeys-self)
- [Locator Examples](#locator-examples)
- [Error Handling](#error-handling)
- [Dependencies](#dependencies)
- [Example Usage](#example-usage)


## ExecuteLocator Class

### Class Attributes

- **`driver`**: A `webdriver` instance for browser interaction.
- **`actions`**: An `ActionChains` instance for complex actions.
- **`by_mapping`**: A dictionary mapping locator strings to `By` objects.


### Class Methods

#### `__init__(self, driver, *args, **kwargs)`

**Description**: Initializes the `ExecuteLocator` object with a `driver` instance.

**Args**:
    - `driver`: The WebDriver instance.

**Raises**:
    - `TypeError`: If `driver` is not a valid WebDriver instance.


#### `execute_locator(self, locator: dict, message: str = None, typing_speed: float = 0, continue_on_error: bool = True)`

**Description**: Executes the actions defined in the `locator` dictionary.

**Args**:
    - `locator` (dict): A dictionary containing locator information (e.g., `By`, selector, attribute).
    - `message` (str, optional): The message to send (if applicable). Defaults to None.
    - `typing_speed` (float, optional): Typing speed for sending messages. Defaults to 0.
    - `continue_on_error` (bool, optional): Whether to continue on error. Defaults to True.

**Returns**:
    Union[str, list, dict, WebElement, bool]: The result of the execution or `False` if an error occurs.


#### `get_webelement_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> WebElement | List[WebElement] | bool`

**Description**: Retrieves web elements based on the provided locator.

**Args**:
    - `locator` (dict | SimpleNamespace): A dictionary or SimpleNamespace containing locator information.
    - `message` (str, optional): An optional message for logging. Defaults to None.

**Returns**:
    WebElement | List[WebElement] | bool: A `WebElement` object, a list of `WebElement` objects or `False` if no elements are found.


#### `get_attribute_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> str | list | dict | bool`

**Description**: Retrieves an attribute from a web element identified by the locator.


**Args**:
    - `locator` (dict | SimpleNamespace): Locator information.
    - `message` (str, optional): An optional message.


**Returns**:
    str | list | dict | bool: The attribute value or `False`.


#### `_get_element_attribute(self, element: WebElement, attribute: str) -> str | None`

**Description**: Helper method to get an attribute from a web element.


**Args**:
    - `element`: The web element.
    - `attribute`: The attribute name.


**Returns**:
    str | None: The attribute value, or `None` if not found.



#### Other Methods (similar structure): `send_message`, `evaluate_locator`, `_evaluate`, `get_locator_keys`


## Locator Examples

Provides examples of locator dictionaries used for targeting web elements.


## Error Handling

The code includes comprehensive `try...except` blocks to catch and log various exceptions during web element interaction, including `NoSuchElementException`, `TimeoutException`, and others.

## Dependencies

Relies on Selenium WebDriver, internal modules, and standard Python libraries.

## Example Usage

(Example code block from input is included here.)



```