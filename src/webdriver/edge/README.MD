```rst
.. module:: src.webdriver.edge
```
# Edge WebDriver Module for Selenium

This module provides a custom implementation of the Edge WebDriver using Selenium. It integrates configuration settings defined in the `edge.json` file, such as user-agent and browser profile settings, to enable flexible and automated browser interactions.

## Key Features

- **Centralized Configuration**: Configuration is managed via the `edge.json` file.
- **Multiple Browser Profiles**: Supports multiple browser profiles, allowing you to configure different settings for testing.
- **Enhanced Logging and Error Handling**: Provides detailed logs for initialization, configuration issues, and WebDriver errors.
- **Ability to Pass Custom Options**: Supports passing custom options during WebDriver initialization.

## Requirements

Before using this WebDriver, ensure the following dependencies are installed:

- Python 3.x
- Selenium
- Fake User Agent
- Edge WebDriver binary (e.g., `msedgedriver`)

Install the required Python dependencies:

```bash
pip install selenium fake_useragent
```

Additionally, ensure the `msedgedriver` binary is available in your system's `PATH` or specify its path in the configuration.

## Configuration

The configuration for the Edge WebDriver is stored in the `edge.json` file. Below is an example structure of the configuration file and its description:

### Example Configuration (`edge.json`)

```json
{
  "options": [
    "--disable-dev-shm-usage",
    "--remote-debugging-port=0"
  ],
  "profiles": {
    "os": "%LOCALAPPDATA%\\Microsoft\\Edge\\User Data\\Default",
    "internal": "webdriver\\edge\\profiles\\default"
  },
  "executable_path": {
    "default": "webdrivers\\edge\\123.0.2420.97\\msedgedriver.exe"
  },
  "headers": {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
    "Accept-Encoding": "none",
    "Accept-Language": "en-US,en;q=0.8",
    "Connection": "keep-alive"
  }
}
```

### Configuration Fields Description

#### 1. `options`
A list of command-line arguments passed to Edge. Examples:
- `--disable-dev-shm-usage`: Disables the use of `/dev/shm` in Docker containers (useful to prevent errors in containerized environments).
- `--remote-debugging-port=0`: Sets the port for remote debugging in Edge. A value of `0` means a random port will be assigned.

#### 2. `profiles`
Paths to Edge user data directories for different environments:
- **os**: Path to the default user data directory (typically for Windows systems).
- **internal**: Internal path for the default WebDriver profile.

#### 3. `executable_path`
Path to the Edge WebDriver binary:
- **default**: Path to the `msedgedriver.exe` binary.

#### 4. `headers`
Custom HTTP headers used in browser requests:
- **User-Agent**: Sets the user-agent string for the browser.
- **Accept**: Sets the types of data the browser is willing to accept.
- **Accept-Charset**: Sets the character encoding supported by the browser.
- **Accept-Encoding**: Sets the supported encoding methods (set to `none` to disable).
- **Accept-Language**: Sets the preferred languages.
- **Connection**: Sets the connection type the browser should use (e.g., `keep-alive`).

## Usage

To use the `Edge` WebDriver in your project, simply import and initialize it:

```python
from src.webdriver.edge import Edge

# Initialize Edge WebDriver with user-agent settings and custom options
browser = Edge(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)", options=["--headless", "--disable-gpu"])

# Open a website
browser.get("https://www.example.com")

# Close the browser
browser.quit()
```

The `Edge` class automatically loads settings from the `edge.json` file and uses them to configure the WebDriver. You can also specify a custom user-agent and pass additional options during WebDriver initialization.

### Singleton Pattern

The `Edge` WebDriver uses the Singleton pattern. This means only one instance of the WebDriver will be created. If an instance already exists, the same instance will be reused, and a new window will be opened.

## Logging and Debugging

The WebDriver class uses the `logger` from `src.logger` to log errors, warnings, and general information. All issues encountered during initialization, configuration, or execution will be logged for easy debugging.

### Example Logs

- **Error during WebDriver initialization**: `Error initializing Edge WebDriver: <error details>`
- **Configuration issues**: `Error in edge.json file: <issue details>`

## License

This project is licensed under the MIT License. See the [LICENSE](../../LICENSE) file for details.
