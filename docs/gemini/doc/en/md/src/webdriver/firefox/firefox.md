# hypotez/src/webdriver/firefox/firefox.py

## Overview

This module defines the `Firefox` class, a subclass of `selenium.webdriver.Firefox`. It extends the base class with features like launching Firefox in kiosk mode and setting up a Firefox profile for the WebDriver.  It also includes integration with JavaScript execution and locator handling utilities.

## Classes

### `Firefox`

**Description**: A subclass of `selenium.webdriver.Firefox` providing additional functionality for launching Firefox in specific configurations.

**Attributes**:

- `driver_name` (str): The name of the WebDriver, defaults to 'firefox'.

**Methods**:

#### `__init__`

**Description**: Initializes the Firefox WebDriver with specified options, profile, geckodriver version, and Firefox version.

**Parameters**:

- `profile_name` (Optional[str], optional): The name of the Firefox profile to use. Defaults to `None`.
- `geckodriver_version` (Optional[str], optional): The version of the geckodriver to use. Defaults to `None`.
- `firefox_version` (Optional[str], optional): The version of Firefox to use. Defaults to `None`.
- `user_agent` (Optional[dict], optional): A dictionary containing user agent settings. Defaults to `None`.
- `*args`, `**kwargs`: Additional arguments and keyword arguments passed to the parent `WebDriver` constructor.

**Returns**:

- `None`

**Raises**:

- `WebDriverException`: Raised if there's an error starting the Firefox WebDriver.  This includes issues like missing or incorrect geckodriver version, missing Firefox installation, or profile errors.
- `Exception`: Raised for any other exception during initialization.


#### `_payload`

**Description**: Loads executors for locators and JavaScript scenarios.


**Parameters**:

- None

**Returns**:

- `None`



## Functions

(No functions defined outside of the class.)


## Usage Example

```python
if __name__ == "__main__":
    profile_name = "custom_profile"
    geckodriver_version = "v0.29.0"
    firefox_version = "78.0"

    browser = Firefox(profile_name=profile_name, geckodriver_version=geckodriver_version, firefox_version=firefox_version)
    browser.get("https://www.example.com")
    browser.quit()
```


```python
# Example of using the class
driver = Firefox()
driver.get(r"https://google.com")
```


## Notes

- The code relies on external configuration (`firefox.json`) for paths and settings, demonstrating good practices for configuration management.
- Error handling is improved using specific exceptions for clarity and better debugging.
- The `_payload` method demonstrates that the class likely prepares necessary functions and object properties to interact with the browser instance.



```