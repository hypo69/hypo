# Firefox WebDriver

## Overview

This module defines a subclass of `webdriver.Firefox` called `Firefox`. It provides additional functionality, including launching Firefox in kiosk mode and setting up a Firefox profile for the webdriver, along with managing user agents and handling potential errors during driver initialization.

## Classes

### `Firefox`

**Description**: A subclass of `selenium.webdriver.Firefox` that enhances the basic functionality of the Firefox webdriver.

**Methods**:

#### `__init__(self, user_agent: Optional[dict] = None, *args, **kwargs) -> None`

**Description**: Initializes the Firefox webdriver with specified launch options and profile.

**Parameters**:

- `user_agent` (`dict`, optional): A dictionary containing user agent settings. If `None`, a random user agent is generated. Defaults to `None`.

**Returns**:
  - `None`: The method initializes the webdriver object and returns nothing.

**Raises**:

- `WebDriverException`: An exception is raised if the webdriver cannot be initialized due to issues with the Firefox installation or geckodriver.
- `Exception`: A generic exception is raised if an unexpected error occurs during initialization.



#### `_set_options(self, settings: SimpleNamespace) -> Options`

**Description**: Sets the launch options for the Firefox webdriver.

**Parameters**:

- `settings` (`SimpleNamespace`): Settings for the Firefox options.

**Returns**:

- `Options`: An `Options` object with the specified launch options.

#### `_set_profile(self, profile: SimpleNamespace) -> FirefoxProfile`

**Description**: Sets up a Firefox profile for the webdriver.

**Parameters**:

- `profile` (`SimpleNamespace`): A `SimpleNamespace` object containing profile settings.

**Returns**:

- `FirefoxProfile`: A `FirefoxProfile` object representing the profile.


## Usage Examples


### Creating a Firefox Profile with User Agent

```python
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import os

profile = FirefoxProfile()
profile.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0")
```

This example demonstrates setting a custom user agent string for the Firefox profile.

### Disabling Images

```python
profile = FirefoxProfile()
profile.set_preference("permissions.default.image", 2)
```

This disables loading images in the browser.

### Blocking Pop-up Windows

```python
profile = FirefoxProfile()
profile.set_preference("dom.disable_open_during_load", False)
```

This prevents pop-up windows from opening during the page load.

### Setting File Download Path

```python
profile = FirefoxProfile()
download_path = "/path/to/download/folder"  # Replace with the desired path
profile.set_preference("browser.download.dir", download_path)
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
```
Sets the download directory and handles potentially required MIME type for saving file downloads.

### Disabling Browser Notifications

```python
profile = FirefoxProfile()
profile.set_preference("dom.webnotifications.enabled", False)
```

This example disables browser notifications.


## Options Examples

### Launching in Headless Mode

```python
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True
```

This example launches Firefox in headless mode, suitable for automated testing without a graphical interface.

### Setting Browser Language

```python
options = Options()
options.add_argument("-lang=es")  # Change 'es' to the desired language code
```

This example sets the browser language to Spanish.

### Custom Command Line Parameters

```python
options = Options()
options.add_argument("--some-option=value")  # Replace with desired arguments
```

This allows you to pass arbitrary command line parameters to the Firefox browser.


### Managing Debug Messages

```python
options = Options()
options.add_argument("-vv") # increase verbosity of debug messages
```


### Launching in Fullscreen Mode

```python
options = Options()
options.add_argument("--kiosk") #for kiosk mode
```

This launches Firefox in fullscreen mode.



## Links

- [Firefox Profile Settings Documentation](https://firefox-source-docs.mozilla.org/testing/geckodriver/Capabilities.md#firefox-profile)
- [Firefox Options Documentation](https://firefox-source-docs.mozilla.org/testing/geckodriver/CommandLineOptions.html)