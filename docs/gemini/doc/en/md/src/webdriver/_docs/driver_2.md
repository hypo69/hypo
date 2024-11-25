# DriverBase Module

## Overview

This module defines the `DriverBase` class, a base class for web driver implementations. It encapsulates common methods and attributes applicable to various web drivers (e.g., Chrome, Firefox, Edge).  This class provides functionalities for page interaction, JavaScript execution, and cookie management.


## Table of Contents

* [DriverBase](#driverbase)
* [DriverMeta](#drivermeta)
* [Driver](#driver)


## Classes

### `DriverBase`

**Description**: This is the base class for all WebDriver implementations.  It contains common methods and attributes for interacting with a web page.

**Attributes**:

- `previous_url`: Stores the URL of the previous page.
- `referrer`: Stores the referrer URL.
- `page_lang`: Stores the language of the current page.
- `ready_state`: Stores the page's ready state.
- `js`: An instance of the `JavaScript` class, used for executing JavaScript.
- `locator`: An instance of the `ExecuteLocator` class, used for locating elements.

**Methods**:

#### `driver_payload()`

**Description**: Initializes `js` and `locator` instances.

#### `scroll(scrolls: int, frame_size: int, direction: str, delay: float)`

**Description**: Scrolls the page in the specified direction.

**Parameters**:
- `scrolls` (int): Number of scrolls to execute.
- `frame_size` (int): Size of the scroll frame.
- `direction` (str): Direction of the scroll ('forward' or 'backward').
- `delay` (float): Delay between scrolls in seconds.

**Raises**:
- `WebDriverException`: If an error occurs during scrolling.


#### `locale()`

**Description**: Returns the detected language of the current page.

**Returns**:
- `str`: The language of the page, or `None` if not found.


#### `get_url(url: str)`

**Description**: Navigates to the specified URL and verifies successful navigation.

**Parameters**:
- `url` (str): The URL to navigate to.

**Returns**:
- `bool`: `True` if navigation is successful, `False` otherwise.

**Raises**:
- `WebDriverException`: If an error occurs during navigation.


#### `extract_domain(url: str)`

**Description**: Extracts the domain name from the given URL.

**Parameters**:
- `url` (str): The URL to extract the domain from.

**Returns**:
- `str`: The domain name, or `None` if the URL is invalid or doesn't contain a domain.

**Raises**:
- `WebDriverException`: If the URL is not a valid URL.


#### `_save_cookies_localy(to_file: Union[str, Path])`

**Description**: Saves the current cookies to a file.

**Parameters**:
- `to_file` (Union[str, Path]): The file path to save the cookies to.

**Raises**:
- `WebDriverException`: If an error occurs during cookie saving.

#### `page_refresh()`

**Description**: Refreshes the current page.

**Raises**:
- `WebDriverException`: If an error occurs during page refresh.

#### `window_focus()`

**Description**: Restores focus to the browser window.


#### `wait(interval: float)`

**Description**: Pauses execution for a specified interval.

**Parameters**:
- `interval` (float): The duration of the pause in seconds.


#### `delete_driver_logs()`

**Description**: Deletes temporary files and logs associated with the WebDriver.

**Raises**:
- `WebDriverException`: If an error occurs during log deletion.


### `DriverMeta`

**Description**: A metaclass for dynamically creating `Driver` classes that inherit from `DriverBase` and a specific WebDriver implementation.

**Methods**:

#### `__call__(cls, webdriver_cls: Type, *args, **kwargs)`

**Description**: Creates a new `Driver` class.

**Parameters**:
- `webdriver_cls` (Type): The WebDriver class to inherit from.
- `*args`, `**kwargs`: Arguments passed to the `webdriver_cls` constructor.

**Returns**:
- `Driver`: The newly created `Driver` class.


### `Driver`

**Description**: A dynamically created WebDriver class that inherits from `DriverBase` and a specified WebDriver implementation.

**Usage Example**:
```python
from src.webdriver import Driver, Chrome, Firefox, Edge
d = Driver(Chrome)
```

This section provides detailed documentation for the `Driver` class.  Further details regarding initialization and usage would be added if the corresponding Python file included the necessary information and docstrings.