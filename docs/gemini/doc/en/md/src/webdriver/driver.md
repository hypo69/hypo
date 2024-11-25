# hypotez/src/webdriver/driver.py

## Overview

This module provides a class `Driver` for working with Selenium webdrivers in a unified way. It handles driver initialization, navigation, cookie management, and exception handling, promoting a consistent interface across various WebDriver types (e.g., Chrome, Firefox, Edge).

## Table of Contents

- [Driver Class](#driver-class)
    - [\_\_init\_\_](#__init__)
    - [\_\_init\_\_\_subclass\_\_](#__init__subclass__)
    - [\_\_getattr\_\_](#__getattr__)
    - [scroll](#scroll)
        - [carousel](#carousel)
    - [locale](#locale)
    - [get\_url](#get_url)
    - [window\_open](#window_open)
    - [wait](#wait)
    - [\_save\_cookies\_localy](#_save_cookies_localy)
    - [fetch\_html](#fetch_html)

## Driver Class

### `Driver`

**Description**: A unified class for interacting with Selenium WebDriver.  It provides a convenient interface for working with different drivers, such as Chrome, Firefox, and Edge.

**Attributes**:

- `driver` (selenium.webdriver): The Selenium WebDriver instance.

### `__init__`

**Description**: Initializes a Driver instance.

**Parameters**:

- `webdriver_cls` (type): The WebDriver class (e.g., Chrome or Firefox).
- `*args`: Positional arguments for the driver.
- `**kwargs`: Keyword arguments for the driver.

**Raises**:

- `TypeError`: If `webdriver_cls` is not a valid WebDriver class.


### `__init_subclass__`

**Description**: Automatically called when a subclass of `Driver` is created.

**Parameters**:

- `browser_name` (str, optional): The name of the browser.  Must be provided.
- `**kwargs`: Additional arguments.

**Raises**:

- `ValueError`: If `browser_name` is not provided.


### `__getattr__`

**Description**: A proxy for accessing driver attributes.

**Parameters**:

- `item` (str): The name of the attribute.

**Returns**:

- The attribute value.


### `scroll`

**Description**: Scrolls the page in the specified direction.

**Parameters**:

- `scrolls` (int, optional): Number of scrolls (default is 1).
- `frame_size` (int, optional): Scroll size in pixels (default is 600).
- `direction` (str, optional): Scroll direction ('both', 'down', 'up'; default is 'both').
- `delay` (float, optional): Delay between scrolls (default is 0.3).

**Returns**:

- `bool`: `True` if successful, `False` otherwise.


### `carousel`

**Description**: Local method for scrolling the screen.

**Parameters**:

- `direction` (str, optional): Scroll direction ('down', 'up').
- `scrolls` (int, optional): Number of scrolls.
- `frame_size` (int, optional): Scroll size.
- `delay` (float, optional): Delay between scrolls.

**Returns**:

- `bool`: `True` if successful, `False` otherwise.


**Raises**:

- `Exception`: For any errors during scrolling.


### `locale`

**Description**: Determines the page language based on meta tags or JavaScript.

**Parameters**:

- None

**Returns**:

- `Optional[str]`: Language code if found, otherwise `None`.


### `get_url`

**Description**: Navigates to a URL and saves the current, previous URL, and cookies.

**Parameters**:

- `url` (str): The URL to navigate to.

**Returns**:

- `bool`: `True` if navigation is successful and the current URL matches the expected one, `False` otherwise.


**Raises**:

- `WebDriverException`: If a WebDriver error occurs.
- `InvalidArgumentException`: If the URL is invalid.
- `Exception`: For any other errors during navigation.


### `window_open`

**Description**: Opens a new tab in the current browser window and switches to it.

**Parameters**:

- `url` (Optional[str], optional): URL to open in the new tab (defaults to `None`).


### `wait`

**Description**: Waits for a specified amount of time.

**Parameters**:

- `delay` (float, optional): Delay time in seconds (default is 0.3).


### `_save_cookies_locally`

**Description**: Saves current WebDriver cookies to a local file.

**Returns**:
- `None`

**Raises**:
- `Exception`: If an error occurs while saving cookies.


### `fetch_html`

**Description**: Retrieves HTML content from a file or webpage.

**Parameters**:

- `url` (str): File path or URL for HTML content.

**Returns**:

- `Optional[bool]`: `True` if content is successfully retrieved, `None` otherwise.


**Raises**:

- `Exception`: If an error occurs while retrieving content.