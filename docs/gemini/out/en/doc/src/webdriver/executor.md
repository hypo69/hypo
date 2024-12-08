# hypotez/src/webdriver/executor.py

## Overview

This module, `executor`, provides functionalities for interacting with web elements using Selenium. It handles locator parsing, web element interaction (clicks, sending messages, executing events, retrieving attributes), error handling, and support for multiple locator types. It aims to automate complex web interaction scenarios.


## Classes

### `ExecuteLocator`

**Description**: This class encapsulates the logic for interacting with web elements based on provided locators. It utilizes Selenium and handles various actions like clicking, typing, sending messages, and retrieving attributes.

**Attributes**:

- `driver`: The Selenium WebDriver instance.
- `actions`: Selenium ActionChains instance, initialized if `driver` is provided.
- `by_mapping`: A dictionary mapping locator strings to Selenium `By` constants.
- `mode`: String representing the current mode (e.g., 'debug', 'dev').


**Methods**:

- `execute_locator`: Executes actions defined by the locator. (Detailed below)
- `evaluate_locator`: Evaluates attributes within a locator. (Detailed below)
- `get_attribute_by_locator`: Retrieves attributes from an element or list of elements found by the locator. (Detailed below)
- `get_webelement_by_locator`: Retrieves a web element or a list of web elements by the given locator.  (Detailed below)
- `get_webelement_as_screenshot`: Takes a screenshot of the located web element. (Detailed below)
- `execute_event`: Executes events (click, pause, send_keys, screenshot, clear) associated with a locator. (Detailed below)
- `send_message`: Sends a message to a web element, handling potential typing speed.  (Detailed below)


## Functions

### `execute_locator`

**Description**:  Executes actions on a web element based on the provided locator data.

**Parameters**:

- `locator`: Locator data (dict or `SimpleNamespace`).
- `timeout`: Timeout for locating the element.
- `timeout_for_event`: Type of wait condition.
- `message`: Optional message to send.
- `typing_speed`: Typing speed for send_keys events.
- `continue_on_error`: Whether to continue execution on error.

**Returns**:

- `str | list | dict | WebElement | bool`: Result of the locator execution.

**Raises**:
  - `ValueError`: if locator is invalid.
  - Various Selenium exceptions: If issues arise during element interaction (e.g., `ElementClickInterceptedException`, `NoSuchElementException`, `TimeoutException`).
  - `Exception`: Other possible exceptions during execution.


### `evaluate_locator`

**Description**: Evaluates and processes locator attributes (e.g. keyboard shortcuts).

**Parameters**:

- `attribute`: Attribute to evaluate.

**Returns**:

- `str | list | dict`: Evaluated attribute.

**Raises**:
 - `Exception`: Any exceptions raised during attribute evaluation.


### `get_attribute_by_locator`

**Description**: Retrieves attributes from an element or list of elements.

**Parameters**:

- `locator`: Locator information (dict or `SimpleNamespace`).
- `timeout`: Timeout for locating the element.
- `timeout_for_event`: Wait condition type.
- `message`: Optional message.
- `typing_speed`: Typing speed.
- `continue_on_error`: Whether to continue on error.


**Returns**:

- `WebElement | list[WebElement] | None`: Web element(s) with attributes or `None`.

**Raises**:
  - `Exception`: Various exceptions related to attribute retrieval or element location.


### `get_webelement_by_locator`

**Description**: Retrieves a web element or list of web elements by the given locator.

**Parameters**:

- `locator`: Locator as a dict or `SimpleNamespace`.
- `timeout`: Maximum wait time in seconds.
- `timeout_for_event`: The wait condition.

**Returns**:

- `WebElement | List[WebElement] | None`: Located element(s) or `None` if not found.

**Raises**:
  - `ValueError`: If locator is invalid.
  - `TimeoutException`: If element is not found within the specified timeout.
  - `Exception`: Other potential errors during element retrieval.


### `get_webelement_as_screenshot`

**Description**: Captures a screenshot of a web element.

**Parameters**:

- `locator`: Locator of the element to capture.
- `timeout`, `timeout_for_event`, `message`, `typing_speed`, `continue_on_error`, `webelement`: Parameters for element interaction and screenshot capturing.


**Returns**:

- `BinaryIO | None`: Binary stream of the screenshot or `None` if failed.


**Raises**:
  - `Exception`: Any exceptions encountered during screenshot capturing.


### `execute_event`

**Description**: Executes events associated with a locator, like click, pause, typing, sending message.


**Parameters**:

- `locator`: Locator specifying the element and event.
- `timeout`, `timeout_for_event`, `message`, `typing_speed`, `continue_on_error`: Parameters for element interaction and event handling.


**Returns**:

- `bool`: `True` if execution successful, `False` otherwise.

**Raises**:
  - `Exception`: Various exceptions, such as `ElementClickInterceptedException`, during event execution.


### `send_message`

**Description**: Sends a message to a web element, handling typing speed.

**Parameters**:

- `locator`: Locator of the element.
- `message`: The message to send.
- `typing_speed`: Typing speed for the message in seconds.


**Returns**:

- `bool`: `True` if message was sent, `False` otherwise.


**Raises**:
 - `Exception`: Any exceptions during message sending.


## Additional Notes

- The code extensively utilizes `SimpleNamespace` for structured data handling.
- Error handling is implemented using `try...except` blocks, with logging using `logger`.
- Asynchronous operations (`async`/`await`) are used for handling tasks concurrently.
- Robust error handling for various Selenium exceptions is incorporated.