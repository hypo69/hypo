# Chrome WebDriver

## Overview

This module implements a custom Chrome WebDriver class, extending the `selenium.webdriver.Chrome` class, for enhanced control and configuration. It leverages `chrome.json` for configuration of various aspects like ChromeDriver and Chrome binary paths.  The class handles user-agent settings, finding free ports, and setting up options for a more robust WebDriver initialization process.


## Table of Contents

* [Chrome Class](#chrome-class)
* [chrome.json File Summary](#chromejson-file-summary)
* [find_free_port Function](#find-free-port-function)
* [set_options Function](#set-options-function)


## Chrome Class

### `Chrome`

**Description**: A subclass of `selenium.webdriver.Chrome` providing additional functionality. It takes care of loading configurations, finding free ports, and setting up Chrome options.

**Attributes**:

- `driver_name`:  (str) Name of the WebDriver, which is 'chrome'.
- `d`: (webdriver.Chrome) A WebDriver instance.
- `options`: (ChromeOptions) Chrome options for configuration.
- `user_agent`: (dict) User-agent settings for the WebDriver.

**Methods**:

#### `__init__`

**Description**: Initializes the Chrome WebDriver with the specified options and profile.

**Parameters**:

- `user_agent` (dict, optional): User-agent settings for the Chrome WebDriver. Defaults to a randomly generated user-agent.  Reference: [https://chatgpt.com/share/c12e9951-dcfe-455a-a5b6-0d5d3e412066](https://chatgpt.com/share/c12e9951-dcfe-455a-a5b6-0d5d3e412066).


**Returns**:

- None


**Raises**:

- `Exception`: If there's an error setting up the WebDriver.


#### `find_free_port`

**Description**: Finds a free port in the specified range.

**Parameters**:

- `start_port` (int): The starting port of the range.
- `end_port` (int): The ending port of the range.

**Returns**:

- int | None: A free port if available, or `None` if no free port is found.


**Raises**:

- `OSError`: If an `OSError` occurs during port binding.


#### `set_options`

**Description**: Sets launch options for the Chrome WebDriver.

**Parameters**:

- `settings` (list | dict | None, optional): Configuration settings for Chrome options. Defaults to `None`.

**Returns**:

- ChromeOptions: A `ChromeOptions` object with the specified launch options.

**Raises**:

- `Exception`: If there's an error parsing the options.


## `chrome.json` File Summary

The `chrome.json` file is used to configure various aspects of the Chrome WebDriver.

**Key Components**:

- `profiles`: Configuration for different Chrome profiles. Includes directories for default, user-specific, and testing profiles.  Example:
```json
"profiles": {
    "one.last.bit": { ... }
}
```
- `driver`: Crucial configuration for ChromeDriver and Chrome binary paths. Example:
```json
"driver": {
    "chromedriver": [ ... ],
    "chrome_binary": [ ... ]
}
```
- `headers`: Default HTTP headers, including `User-Agent` and other relevant headers, for the WebDriver.  Example:
```json
"headers": {
    "User-Agent": "...",
    ...
}
```

Note: The example `chrome.json` shows a structure for different profiles and potential error handling in the code.


```