# src.webdriver.driver

## Overview

This module provides a base class for interacting with web drivers, offering methods for various actions like clicking elements, scrolling, handling exceptions, and more. It leverages other modules like `src.settings.gs`, `src.webdriver.executor.ExecuteLocator`, and `src.webdriver.javascript.js.JavaScript` for advanced functionalities.  The `Driver` class serves as a metaclass, allowing for instantiation of different web driver types (Chrome, Firefox, Edge) through inheritance.

## Table of Contents

* [DriverBase](#driverbase)
* [DriverMeta](#drivermeta)
* [Driver](#driver)


## DriverBase

**Description**: This class acts as the base for all driver implementations, defining common methods and attributes for interaction.

**Attributes**:

* `previous_url` (str): The previous URL visited by the browser.
* `referrer` (str): The referrer URL.
* `page_lang` (str): The language of the current webpage.
* `ready_state`: (Variable): Indicates the loading status of the webpage.
* `get_page_lang()`: Method for retrieving the webpage language.
* `unhide_DOM_element(self, locator: str)`:  Method for unhiding a DOM element given its locator.
* `get_referrer()`: Method for retrieving the referrer URL.
* `window_focus()`: Method for bringing the browser window to the foreground.
* `execute_locator(self, locator: str, **kwargs)`: Method to interact with an element using a locator strategy.
* `click(self, locator: str)`: Clicks on an element with the given locator.
* `get_webelement_as_screenshot(self, locator: str)`: Captures a screenshot of an element based on a locator.
* `get_attribute_by_locator(self, locator: str, attribute_name: str) -> str | None`: Retrieves the specified attribute value for an element.
* `send_message(self, message: str)`: Sends a message to the browser.
* `send_key_to_webelement(self, locator: str, keys: Keys)`: Sends specified keys to a Webelement.

**Methods**:

* `driver_payload(self)`:  Method to return the payload of the driver.  Handles JavaScript and `ExecuteLocator` methods within this payload.

* `scroll(self, scrolls: int, frame_size: int, direction: str, delay: float) -> None | bool`: Scrolls the page.
    - `scrolls` (int): Number of scrolls to perform.
    - `frame_size` (int): Size of the scroll frame.
    - `direction` (str): Direction of the scroll ("up", "down", "left", "right").
    - `delay` (float): Delay between scrolls.
    - Returns `None` or `bool` indicating success.

* `carousel(self, direction: str, scrolls: int, frame_size: int, delay: float) -> bool`:  Handles carousel-style scrolling.
    - `direction` (str): Direction of the scroll.
    - `scrolls` (int): Number of scrolls to perform.
    - `frame_size` (int): Size of the scroll frame.
    - `delay` (float): Delay between scrolls.
    - Returns `bool` indicating success.

* `locale(self) -> None | str`: Returns the locale of the webpage.
* `get_url(self, url: str) -> bool`: Changes the browser URL.
    - `url` (str): The new URL.
    - Returns `bool` indicating success.
* `extract_domain(self, url: str) -> str`: Extracts the domain from a given URL.
* `_save_cookies_localy(self, to_file: str | Path) -> bool`: Saves cookies to a file.
* `page_refresh(self) -> bool`: Refreshes the current page.
    - Returns `bool` indicating success.

* `wait(self, interval: float)`: Waits for a specified time.
    - `interval` (float): The duration to wait.

* `delete_driver_logs(self) -> bool`: Deletes the driver logs.
    - Returns `bool` indicating success.


## DriverMeta

**Description**: This is a metaclass that enables dynamic instantiation of different web driver classes (e.g., Chrome, Firefox, Edge) based on the passed class as an argument.

**Methods**:

* `__call__(cls, webdriver_cls, *args, **kwargs)`: Dynamically instantiates the specified webdriver class.
    - `webdriver_cls`: The class of the web driver to instantiate.
    - `*args`: Additional positional arguments.
    - `**kwargs`: Additional keyword arguments.


## Driver

**Description**:  This class is a metaclass that handles the creation of webdriver objects.


**Usage Example**:

```python
from src.webdriver import Driver, Chrome
# ... other imports

d = Driver(Chrome)
# Use d to interact with the webdriver
```
```