```rst
.. module:: src.webdriver.chrome
```
# Custom Chrome WebDriver Module for Selenium

This module provides a custom implementation of the Chrome WebDriver using Selenium. It integrates configuration settings defined in the `chrome.json` file, such as user-agent and browser profile settings, to enable flexible and automated browser interactions.

## Key Features

- **Centralized Configuration**: Configuration is managed via the `chrome.json` file.
- **Multiple Browser Profiles**: Supports multiple browser profiles, allowing you to configure different settings for testing.
- **Enhanced Logging and Error Handling**: Provides detailed logs for initialization, configuration issues, and WebDriver errors.
- **Ability to Pass Custom Options**: Supports passing custom options during WebDriver initialization.

## Requirements

Before using this WebDriver, ensure the following dependencies are installed:

- Python 3.x
- Selenium
- Fake User Agent
- Chrome WebDriver binary (e.g., `chromedriver`)

Install the required Python dependencies:

```bash
pip install selenium fake_useragent
```

Additionally, ensure the `chromedriver` binary is available in your system's `PATH` or specify its path in the configuration.

## Configuration

The configuration for the Chrome WebDriver is stored in the `chrome.json` file. Below is an example structure of the configuration file and its description:

### Example Configuration (`chrome.json`)

```json
{
  "options": {
    "log-level": "5",
    "disable-dev-shm-usage": "",
    "remote-debugging-port": "0",
    "arguments": [ "--kiosk", "--disable-gpu" ]
  },

  "disabled_options": { "headless": "" },

  "profile_directory": {
    "os": "%LOCALAPPDATA%\\Google\\Chrome\\User Data",
    "internal": "webdriver\\chrome\\profiles\\default",
    "testing": "%LOCALAPPDATA%\\Google\\Chrome for Testing\\User Data"
  },

  "binary_location": {
    "os": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    "exe": "bin\\webdrivers\\chrome\\125.0.6422.14\\chromedriver.exe",
    "binary": "bin\\webdrivers\\chrome\\125.0.6422.14\\win64-125.0.6422.14\\chrome-win64\\chrome.exe",
    "chromium": "bin\\webdrivers\\chromium\\chrome-win\\chrome.exe"
  },

  "headers": {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml,application/json;q=0.9,*/*;q=0.8",
    "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
    "Accept-Encoding": "none",
    "Accept-Language": "en-US,en;q=0.8",
    "Connection": "keep-alive"
  },
  "proxy_enabled": false
}
```

### Configuration Fields Description

#### 1. `options`
A dictionary of Chrome parameters to modify browser behavior:
- **log-level**: Sets the logging level. A value of `5` corresponds to the most detailed logging level.
- **disable-dev-shm-usage**: Disables the use of `/dev/shm` in Docker containers (useful to prevent errors in containerized environments).
- **remote-debugging-port**: Sets the port for remote debugging in Chrome. A value of `0` means a random port will be assigned.
- **arguments**: A list of command-line arguments passed to Chrome. Examples: `--kiosk` for kiosk mode and `--disable-gpu` to disable GPU hardware acceleration.

#### 2. `disabled_options`
Options explicitly disabled. In this case, the `headless` mode is disabled, meaning Chrome will run in a visible window rather than headless mode.

#### 3. `profile_directory`
Paths to Chrome user data directories for different environments:
- **os**: Path to the default user data directory (typically for Windows systems).
- **internal**: Internal path for the default WebDriver profile.
- **testing**: Path to the user data directory specifically configured for testing.

#### 4. `binary_location`
Paths to various Chrome binaries:
- **os**: Path to the installed Chrome binary for the operating system.
- **exe**: Path to the ChromeDriver executable.
- **binary**: Specific path to the Chrome binary for testing.
- **chromium**: Path to the Chromium binary, which can be used as an alternative to Chrome.

#### 5. `headers`
Custom HTTP headers used in browser requests:
- **User-Agent**: Sets the user-agent string for the browser.
- **Accept**: Sets the types of data the browser is willing to accept.
- **Accept-Charset**: Sets the character encoding supported by the browser.
- **Accept-Encoding**: Sets the supported encoding methods (set to `none` to disable).
- **Accept-Language**: Sets the preferred languages.
- **Connection**: Sets the connection type the browser should use (e.g., `keep-alive`).

#### 6. `proxy_enabled`
A boolean value indicating whether to use a proxy server for the WebDriver. Defaults to `false`.

## Usage

To use the `Chrome` WebDriver in your project, simply import and initialize it:

```python
from src.webdriver.chrome import Chrome

# Initialize Chrome WebDriver with user-agent settings and custom options
browser = Chrome(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)", options=["--headless", "--disable-gpu"])

# Open a website
browser.get("https://www.example.com")

# Close the browser
browser.quit()
```

The `Chrome` class automatically loads settings from the `chrome.json` file and uses them to configure the WebDriver. You can also specify a custom user-agent and pass additional options during WebDriver initialization.

### Singleton Pattern

The `Chrome` WebDriver uses the Singleton pattern. This means only one instance of the WebDriver will be created. If an instance already exists, the same instance will be reused, and a new window will be opened.

## Logging and Debugging

The WebDriver class uses the `logger` from `src.logger` to log errors, warnings, and general information. All issues encountered during initialization, configuration, or execution will be logged for easy debugging.

### Example Logs

- **Error during WebDriver initialization**: `Error initializing Chrome WebDriver: <error details>`
- **Configuration issues**: `Error in chrome.json file: <issue details>`

## License

This project is licensed under the MIT License. See the [LICENSE](../../LICENSE) file for details.
