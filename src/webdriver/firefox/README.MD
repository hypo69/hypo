```rst
.. module: src.webdriver.firefox
```
# Firefox WebDriver Module

This module contains the `Firefox` class, which extends the functionality of the standard Firefox WebDriver. It allows you to configure a custom profile, run the WebDriver in kiosk mode, and set proxy settings.

## Requirements

- Python 3.12+
- Selenium
- Fake User-Agent
- Proxy handling module

## Installation

1. Install all dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Ensure that the following components are installed:
   - **geckodriver** (for WebDriver support)
   - **Firefox** (supported version)

3. To work with proxies, provide the path to the proxy file using the `proxy_file_path` parameter.

## Example Usage

Example of using the `Firefox` class:

```python
from src.webdriver.firefox import Firefox

if __name__ == "__main__":
    profile_name = "custom_profile"
    geckodriver_version = "v0.29.0"
    firefox_version = "78.0"
    proxy_file_path = "path/to/proxies.txt"

    # Initialize and launch the browser
    browser = Firefox(
        profile_name=profile_name, 
        geckodriver_version=geckodriver_version, 
        firefox_version=firefox_version,
        proxy_file_path=proxy_file_path
    )
    browser.get("https://www.example.com")
    browser.quit()
```

## Class and Method Descriptions

### `Firefox` Class

- Extends the standard Firefox WebDriver, adding functionality such as:
  - Setting a custom profile
  - Proxy settings
  - Setting a custom user agent
  - Integration with JavaScript and executing locators

#### `__init__` Constructor

```python
def __init__(self, profile_name: Optional[str] = None,
             geckodriver_version: Optional[str] = None,
             firefox_version: Optional[str] = None,
             user_agent: Optional[str] = None,
             proxy_file_path: Optional[str] = None,
             *args, **kwargs) -> None:
```

- **profile_name**: The name of the custom Firefox profile.
- **geckodriver_version**: The version of geckodriver.
- **firefox_version**: The version of Firefox.
- **user_agent**: The user agent string.
- **proxy_file_path**: The path to the proxy file.

#### `set_proxy` Method

```python
def set_proxy(self, options: Options) -> None:
```

- Configures the proxy for Firefox, selecting a random working proxy from the provided proxy file.

#### `_payload` Method

```python
def _payload(self) -> None:
```

- Loads necessary executors for locators and JavaScript.

## Additional Configuration

- **Proxy**: The module automatically selects an available working proxy from the provided file, specified by the `proxy_file_path` parameter.
- **Firefox Profile**: You can specify a path to a custom Firefox profile.
- **User Agent**: The module allows you to set a custom user agent for the WebDriver.

## Logging

The module uses `logger` for logging errors and warnings.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
