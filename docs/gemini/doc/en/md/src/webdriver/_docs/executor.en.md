# WebDriver Executor

## Overview

This module provides the `ExecuteLocator` class for executing navigation algorithms and interactions with web pages based on locator dictionaries. It utilizes Selenium WebDriver for browser automation and incorporates error handling and logging mechanisms.

## Table of Contents

- [Classes](#classes)
    - [ExecuteLocator](#executelocator)
- [Functions](#functions)
    - [get_locator_keys](#get_locator_keys)
- [Locator Examples](#locator-examples)


## Classes

### ExecuteLocator

**Description**: The `ExecuteLocator` class handles actions on web elements based on provided locator dictionaries. It utilizes Selenium WebDriver and `ActionChains` for interaction with the browser.

**Attributes**:

- `driver`: A reference to the Selenium WebDriver instance.
- `actions`: An `ActionChains` instance for complex actions.
- `by_mapping`: A dictionary mapping locator strings to Selenium `By` objects.

**Methods**:

#### `__init__(self, driver, *args, **kwargs)`

**Description**: Initializes the `ExecuteLocator` object.

**Parameters**:
- `driver`: (WebDriver): The Selenium WebDriver instance.
- `*args`: Variable positional arguments.
- `**kwargs`: Variable keyword arguments.

**Returns**:
- None


#### `execute_locator(self, locator: dict, message: str = None, typing_speed: float = 0, continue_on_error: bool = True) -> Union[str, list, dict, WebElement, bool]`

**Description**: Executes actions specified by the `locator` dictionary.

**Parameters**:
- `locator` (dict): A dictionary containing instructions for the action.
- `message` (str, optional): The message to be typed. Defaults to None.
- `typing_speed` (float, optional): The typing speed. Defaults to 0 (default Selenium speed).
- `continue_on_error` (bool, optional): Whether to continue execution on error. Defaults to True.

**Returns**:
- Union[str, list, dict, WebElement, bool]: The result of the action or `False` if an error occurred.

**Raises**:
- `ExecuteLocatorException`: If there's an error during the execution.
- `WebDriverException`: If there's a WebDriver-specific error.


#### `get_webelement_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> WebElement | List[WebElement] | bool`

**Description**: Retrieves web elements based on the provided locator.

**Parameters**:
- `locator` (dict | SimpleNamespace): The locator dictionary or SimpleNamespace object.
- `message` (str, optional): A message to be displayed. Defaults to None.


**Returns**:
- WebElement | List[WebElement] | bool: The web element(s) found or `False` if no elements were found.

**Raises**:
- `ExecuteLocatorException`: If there's an error during element retrieval.
- `WebDriverException`: If there's a WebDriver-specific error.


#### `get_attribute_by_locator(self, locator: dict | SimpleNamespace, message: str = None) -> str | list | dict | bool`

**Description**: Retrieves an attribute from a web element based on the locator.

**Parameters**:
- `locator` (dict | SimpleNamespace): The locator for the element.
- `message` (str, optional): A message associated with the locator. Defaults to None.

**Returns**:
- str | list | dict | bool: The attribute value or `False` if retrieval fails.

**Raises**:
- `ExecuteLocatorException`: If there's an error during attribute retrieval.
- `WebDriverException`: If there's a WebDriver-specific error.


#### `_get_element_attribute(self, element: WebElement, attribute: str) -> str | None`

**Description**: Helper method for retrieving an element attribute.

**Parameters**:
- `element` (WebElement): The element to retrieve the attribute from.
- `attribute` (str): The attribute name.

**Returns**:
- str | None: The attribute value or `None` if it doesn't exist.


#### `send_message(self, locator: dict | SimpleNamespace, message: str, typing_speed: float, continue_on_error:bool) -> bool`

**Description**: Sends a message to a web element.


**Parameters**:
- `locator` (dict | SimpleNamespace): The locator to target.
- `message` (str): The message to send.
- `typing_speed` (float): The typing speed.
- `continue_on_error` (bool): Continue on error flag.

**Returns**:
- bool: True if successful, False otherwise.



#### `evaluate_locator(self, attribute: str | list | dict) -> str`

**Description**: Evaluates a locator attribute.

**Parameters**:
- `attribute` (str | list | dict): The attribute to evaluate.

**Returns**:
- str: The evaluated attribute.


#### `_evaluate(self, attribute: str) -> str | None`

**Description**: Helper method for evaluating a single attribute.

**Parameters**:
- `attribute` (str): The attribute to evaluate.

**Returns**:
- str | None: The evaluated attribute or None.

#### `get_locator_keys() -> list`

**Description**: Returns a list of available locator keys.

**Returns**:
- list: List of locator keys.


## Functions

### `get_locator_keys()`

**Description**: Returns a list of available locator keys.

**Returns**:
- list: A list of available locator keys.


## Locator Examples

Example locator dictionaries for different use cases (refer to the input code for comprehensive examples).


```json
{
  "product_links": {
    "attribute": "href",
    "by": "xpath",
    "selector": "//div[contains(@id,\'node-galery\')]//li[contains(@class,\'item\')]//a",
    "selector2": "//span[@data-component-type=\'s-product-image\']//a",
    "if_list": "first",
    "use_mouse": false,
    "mandatory": true,
    "event": null
  },
  // ... other locators
}
```

```json
{
 "pagination": {
   "ul": {
     "attribute": null,
     "by": "xpath",
     "selector": "//ul[@class=\'pagination\']",
     "event": "click()"
    },
    // ... other pagination locators
 }
}
```
```
```