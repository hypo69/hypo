```rst
.. module:: src.webdriver.playwright
```
# Playwright Crawler Module for Browser Automation

This module provides a custom implementation of `PlaywrightCrawler` using the Playwright library. It allows you to configure browser launch parameters such as user-agent, proxy settings, viewport size, and other options defined in the `playwrid.json` file.

## Key Features

- **Centralized Configuration**: Configuration is managed via the `playwrid.json` file.
- **Custom Options Support**: Ability to pass custom options during initialization.
- **Enhanced Logging and Error Handling**: Provides detailed logs for initialization, configuration issues, and WebDriver errors.
- **Proxy Support**: Configure proxy servers to bypass restrictions.
- **Flexible Browser Settings**: Customize viewport size, user-agent, and other browser parameters.

## Requirements

Before using this module, ensure the following dependencies are installed:

- Python 3.x
- Playwright
- Crawlee

Install the required Python dependencies:

```bash
pip install playwright crawlee
```

Additionally, ensure that Playwright is installed and configured to work with the browser. Install the browsers using the command:

```bash
playwright install
```

## Configuration

The configuration for the Playwright Crawler is stored in the `playwrid.json` file. Below is an example structure of the configuration file and its description:

### Example Configuration (`playwrid.json`)

```json
{
  "browser_type": "chromium",
  "headless": true,
  "options": [
    "--disable-dev-shm-usage",
    "--no-sandbox",
    "--disable-gpu"
  ],
  "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
  "proxy": {
    "enabled": false,
    "server": "http://proxy.example.com:8080",
    "username": "user",
    "password": "password"
  },
  "viewport": {
    "width": 1280,
    "height": 720
  },
  "timeout": 30000,
  "ignore_https_errors": false
}
```

### Configuration Fields Description

#### 1. `browser_type`
The type of browser to be used. Possible values:
- `chromium` (default)
- `firefox`
- `webkit`

#### 2. `headless`
A boolean value indicating whether the browser should run in headless mode. Default is `true`.

#### 3. `options`
A list of command-line arguments passed to the browser. Examples:
- `--disable-dev-shm-usage`: Disables the use of `/dev/shm` in Docker containers.
- `--no-sandbox`: Disables the sandbox mode.
- `--disable-gpu`: Disables GPU hardware acceleration.

#### 4. `user_agent`
The user-agent string to be used for browser requests.

#### 5. `proxy`
Proxy server settings:
- **enabled**: A boolean value indicating whether to use a proxy.
- **server**: The address of the proxy server.
- **username**: The username for proxy authentication.
- **password**: The password for proxy authentication.

#### 6. `viewport`
The dimensions of the browser window:
- **width**: The width of the window.
- **height**: The height of the window.

#### 7. `timeout`
The maximum waiting time for operations (in milliseconds). Default is `30000` (30 seconds).

#### 8. `ignore_https_errors`
A boolean value indicating whether to ignore HTTPS errors. Default is `false`.

## Usage

To use `Playwrid` in your project, simply import and initialize it:

```python
from src.webdriver.playwright import Playwrid

# Initialize Playwright Crawler with custom options
browser = Playwrid(options=["--headless"])

# Start the browser and navigate to a website
browser.start("https://www.example.com")
```

The `Playwrid` class automatically loads settings from the `playwrid.json` file and uses them to configure the WebDriver. You can also specify a custom user-agent and pass additional options during WebDriver initialization.

## Logging and Debugging

The WebDriver class uses the `logger` from `src.logger` to log errors, warnings, and general information. All issues encountered during initialization, configuration, or execution will be logged for easy debugging.

### Example Logs

- **Error during WebDriver initialization**: `Error initializing Playwright Crawler: <error details>`
- **Configuration issues**: `Error in playwrid.json file: <issue details>`

## License

This project is licensed under the MIT License. See the [LICENSE](../../LICENSE) file for details.
