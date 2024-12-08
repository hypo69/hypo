# hypotez/src/webdriver/driver.py

## Overview

This module provides a class `Driver` for working with Selenium webdrivers, offering a unified interface for interacting with various browsers like Chrome, Firefox, and Edge.  It handles driver initialization, navigation, cookie management, and exception handling.

## Table of Contents

* [Classes](#classes)
    * [Driver](#driver)
* [Functions](#functions)
    * [N/A]


## Classes

### Driver

**Description**: A unified class for interacting with Selenium WebDrivers. This class provides a user-friendly interface for working with different drivers like Chrome, Firefox, and Edge.

**Attributes**:

- `driver` (selenium.webdriver): The Selenium WebDriver instance.


**Methods**:

#### `__init__(self, webdriver_cls, *args, **kwargs)`

**Description**: Initializes a Driver instance.

**Parameters**:

- `webdriver_cls` (type): The WebDriver class (e.g., `Chrome`, `Firefox`).
- `*args`: Positional arguments for the webdriver constructor.
- `**kwargs`: Keyword arguments for the webdriver constructor.

**Example**:

```python
from selenium.webdriver import Chrome
driver = Driver(Chrome, executable_path='/path/to/chromedriver')
```

**Raises**:

- `TypeError`: If `webdriver_cls` is not a valid WebDriver class.


#### `__init_subclass__(cls, *, browser_name=None, **kwargs)`

**Description**: Automatically called when a subclass of `Driver` is created.

**Parameters**:

- `browser_name` (str, optional): The browser name (e.g., 'Chrome').
- `**kwargs`: Additional keyword arguments for the subclass.

**Raises**:

- `ValueError`: If `browser_name` is not provided.


#### `__getattr__(self, item)`

**Description**: A proxy method for accessing driver attributes.

**Parameters**:

- `item` (str): The attribute name.

**Returns**:

- The value of the accessed attribute.

**Example**:

```python
driver.current_url
```


#### `scroll(self, scrolls=1, frame_size=600, direction='both', delay=.3)`

**Description**: Scrolls the page in the specified direction.

**Parameters**:

- `scrolls` (int, optional): Number of scrolls (defaults to 1).
- `frame_size` (int, optional): Scroll size in pixels (defaults to 600).
- `direction` (str, optional): Scroll direction ('both', 'down', 'up') (defaults to 'both').
- `delay` (float, optional): Delay between scrolls (defaults to 0.3).

**Returns**:

- `bool`: True if successful, False otherwise.

**Raises**:

- `Exception`: If any error occurs during scrolling.


#### `carousel(direction='', scrolls=1, frame_size=600, delay=.3)`

**Description**: (Internal) Method for scrolling the screen.


#### `locale(self)`

**Description**: Determines the page language based on meta tags or JavaScript.

**Returns**:

- `Optional[str]`: Language code if found, otherwise `None`.

**Raises**:

- `Exception`: If errors occur during language detection.


#### `get_url(self, url: str) -> bool`

**Description**: Navigates to the specified URL and saves the current URL, previous URL, and cookies.


**Parameters**:

- `url` (str): The URL to navigate to.


**Returns**:

- `bool`: True if navigation is successful and the current URL matches the expected URL, False otherwise.


**Raises**:

- `WebDriverException`: If a WebDriver error occurs.
- `InvalidArgumentException`: If the URL is invalid.
- `Exception`: For any other errors during navigation.



#### `window_open(self, url: Optional[str] = None)`

**Description**: Opens a new tab in the current browser window and switches to it.


**Parameters**:

- `url` (Optional[str], optional): The URL to open in the new tab (defaults to None).


#### `wait(self, delay: float = .3)`

**Description**: Pauses execution for the specified delay.

**Parameters**:

- `delay` (float, optional): The delay time in seconds (defaults to 0.3).


#### `_save_cookies_localy(self)`

**Description**: Saves current cookies of the WebDriver to a local file.

**Returns**:

- `None`

**Raises**:

- `Exception`: If an error occurs during cookie saving.


#### `fetch_html(self, url: str) -> Optional[bool]`

**Description**: Fetches HTML content from a file or a webpage.


**Parameters**:

- `url` (str): The file path or URL to fetch the HTML from.


**Returns**:

- `Optional[bool]`: True if content is fetched successfully, otherwise None.


**Raises**:

- `Exception`: If an error occurs during content retrieval.