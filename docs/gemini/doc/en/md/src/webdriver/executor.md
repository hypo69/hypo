# hypotez/src/webdriver/executor.py

## Overview

This module, `executor`, provides functionalities for interacting with web elements using Selenium. It handles various tasks like parsing locators, performing actions (clicks, sending messages, executing events), retrieving attributes, and error handling.  The module supports both single and multiple locators, allowing for versatile web automation scenarios.

## Classes

### `ExecuteLocator`

**Description**:  This class acts as a handler for web elements, using Selenium for interactions. It takes the driver, locator data, and optional parameters to control actions and error handling.


**Methods**:

- `__post_init__`: Initializes the ActionChains object if a driver is provided.

- `execute_locator`: Executes actions on web elements based on the provided locator data.  It supports different actions (clicks, sending messages, retrieving attributes) and error handling.

- `evaluate_locator`: Evaluates and processes locator attributes, handling potential attribute transformations.

- `get_attribute_by_locator`: Retrieves attributes from an element or list of elements found by the given locator.  Supports retrieving a single attribute or a dictionary of attributes.

- `get_webelement_by_locator`: Fetches web elements according to the locator, using Selenium's `WebDriverWait` for potential element presence.

- `get_webelement_as_screenshot`: Captures a screenshot of the located web element.

- `execute_event`: Executes various events, including clicks, pauses, sending messages, taking screenshots, clearing elements, and using ActionChains for key press events, including typing.

- `send_message`: Sends a message to a web element, supporting typing speed and character replacement (e.g., for special characters like semi-colons).  Includes detailed flowchart.


## Functions

(None)


## Data Structures

(None)


## Modules