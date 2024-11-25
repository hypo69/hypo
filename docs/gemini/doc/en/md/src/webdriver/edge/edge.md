# Edge WebDriver

## Overview

This module defines a custom `Edge` WebDriver class for enhanced functionality and simplified configuration using `fake_useragent`. It aims to provide a more user-friendly and robust way to interact with Edge browsers.  It includes loading JavaScript executors for various operations like getting page language, checking ready state, and interacting with DOM elements.  The configuration relies on a JSON file (`edge.json`) for specifying the path to the Edge WebDriver executable.


## Table of Contents

* [Edge Class](#edge-class)
    * [Initialization (`__init__`) Method](#initialization-__init__-method)
    * [_payload Method](#_payload-method)
    * [set_options Method](#set-options-method)


## Classes

### `Edge`

**Description**: This class extends the `selenium.webdriver.Edge` class to provide custom functionality.  It handles the initialization and configuration of the Edge WebDriver, including loading of necessary executors for locators and JavaScript interactions.


**Attributes**:

- `driver_name` (str): The name of the WebDriver, defaults to 'edge'.


**Methods**:

#### `__init__`

**Description**: Initializes the Edge WebDriver with specified user agent and options.

**Parameters**:

- `user_agent` (Optional[dict], optional): A dictionary specifying the user agent. If `None`, a random user agent is generated using `fake_useragent`.


**Raises**:

- `WebDriverException`: If there's an error during WebDriver initialization.
- `Exception`: If a general error occurs during initialization.


#### `_payload`

**Description**: Loads executors for locators and JavaScript operations. This method is crucial for providing access to external utility methods.


**Raises**:

- `Exception`: A catch-all exception for potential errors during payload loading.


#### `set_options`

**Description**: Creates and configures launch options for the Edge WebDriver.

**Parameters**:

- `opts` (Optional[List[str]], optional): A list of options to add to the Edge WebDriver. Defaults to `None`.


**Returns**:

- `EdgeOptions`: The configured `EdgeOptions` object.