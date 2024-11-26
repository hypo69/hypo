```## File hypotez/src/webdriver/chrome/chrome.py
# -*- coding: utf-8 -*-\n#! venv/Scripts/python.exe\n#! venv/bin/python/python3.12\n\n"""\n.. module:: src.webdriver.chrome\n    :platform: Windows, Unix\n    :synopsis: Chrome WebDriver implementation.\n\nThis module provides a custom implementation of Selenium\'s Chrome WebDriver. It integrates\nsettings defined in the `chrome.json` configuration file, such as user-agent and browser\nprofile settings, to allow for flexible and automated browser interactions.\n\nKey Features:\n    - Centralized configuration through JSON files.\n    - Support for multiple browser profiles.\n    - Enhanced logging and exception handling.\n"""\nMODE = \'dev\'\n\nimport os\nimport sys\nimport threading\nimport socket\nfrom pathlib import Path\nfrom typing import List, Optional, Dict, Union\nfrom types import SimpleNamespace\nfrom selenium import webdriver\nfrom selenium.webdriver.chrome.service import Service as ChromeService\nfrom selenium.webdriver.chrome.options import Options as ChromeOptions\nfrom fake_useragent import UserAgent\nfrom selenium.common.exceptions import WebDriverException\n\nimport header\nfrom src import gs\nfrom src.webdriver.executor import ExecuteLocator\nfrom src.webdriver.js import JavaScript\nfrom src.utils.jjson import j_loads_ns\nfrom src.logger import logger\n\n\nclass Chrome(webdriver.Chrome):\n    """Class for Chrome WebDriver."""\n\n    _instance = None\n    driver_name: str = \'chrome\'\n    config: SimpleNamespace\n\n    def __new__(cls, *args, **kwargs):\n        """Ensure a single instance of Chrome WebDriver.\n\n        If an instance already exists, calls `window_open()`.\n\n        Returns:\n            Chrome: The singleton instance of the Chrome WebDriver.\n        """\n        if cls._instance is None:\n            cls._instance = super().__new__(cls)\n        else:\n            cls._instance.window_open()  # Open a new window if instance already exists\n        return cls._instance\n\n    def __init__(self, user_agent: Optional[str] = None, *args, **kwargs):\n        """Initializes the Chrome WebDriver with the specified options and profile.\n\n        Args:\n            user_agent (Optional[str]): The user agent string to be used. Defaults to a random user agent.\n        """\n        try:\n            user_agent = user_agent or UserAgent().random\n            self.config = j_loads_ns(Path(gs.path.src, \'webdriver\', \'chrome\', \'chrome.json\'))  # Load settings from JSON file\n            if not self.config:\n                logger.debug(f\'Ошибка в файле config `chrome.json`\')\n                return\n\n            options = ChromeOptions()\n\n            def normalize_path(path: str) -> str:\n                return path.replace(\'%APPDATA%\', os.environ.get(\'APPDATA\', \'\')).replace(\'%LOCALAPPDATA%\', os.getenv(\'LOCALAPPDATA\', \'\')) if path else \'\'\n\n            # Add arguments\n            if hasattr(self.config, \'options\') and self.config.options:\n                for key, value in vars(self.config.options).items():\n                    options.add_argument(f\'--{key}={value}\')\n            if hasattr(self.config, \'headers\') and self.config.headers:\n                for key, value in vars(self.config.headers).items():\n                    options.add_argument(f\'--{key}={value}\')\n\n            profile_directory = Path(gs.path.root / normalize_path(self.config.profile_directory.testing))\n            binary_location = Path(gs.path.root / normalize_path(self.config.binary_location.binary))\n\n            if profile_directory:\n                options.add_argument(f\'user-data-dir={profile_directory}\')\n\n            options.binary_location = str(binary_location)\n            service = ChromeService(executable_path=str(binary_location)) if binary_location else ChromeService()\n            super().__init__(options=options)\n\n        except WebDriverException as ex:\n            logger.critical(\'Error initializing Chrome WebDriver:\', ex)\n            return\n        except Exception as ex:\n            logger.critical(\'Chrome WebDriver crashed. General error:\', ex)\n            return\n\n        self._payload()\n\n    def _payload(self) -> None:\n        js_executor = JavaScript(self)\n        self.get_page_lang = js_executor.get_page_lang\n        self.ready_state = js_executor.ready_state\n        self.get_referrer = js_executor.get_referrer\n        self.unhide_DOM_element = js_executor.unhide_DOM_element\n        self.window_focus = js_executor.window_focus\n\n        execute_locator = ExecuteLocator(self)\n        self.execute_locator = execute_locator.execute_locator\n        self.get_webelement_as_screenshot = execute_locator.get_webelement_as_screenshot\n        self.get_webelement_by_locator = execute_locator.get_webelement_by_locator\n        self.get_attribute_by_locator = execute_locator.get_attribute_by_locator\n        self.send_message = self.send_key_to_webelement = execute_locator.send_message\n\n```

```algorithm
1. **Initialization (Chrome Class):**
   - Checks if a Chrome instance exists. If not, creates a new instance. If it exists, calls `window_open()` to open a new window.
   - Loads configuration from `chrome.json` using `j_loads_ns`.
   - **Example:** `self.config` contains settings like user-agent, browser profile paths, and additional Chrome options.
   - Validates the loaded config. If the config is empty, logs a message.
   - Creates a `ChromeOptions` object.
   - Defines `normalize_path` to handle environment variable placeholders.
   - **Example:**  `%APPDATA%` is replaced with the actual system environment variable value.
   - Adds arguments from `options` and `headers` sections in `chrome.json`.
   - **Example:** `--disable-extensions` or `--user-agent=your-user-agent`.
   - Gets `profile_directory` and `binary_location` from `chrome.json` after normalization.
   - **Example:**  `gs.path.root / %APPDATA%/MyChromeProfile`
   - Sets `user-data-dir` Chrome option.
   - Sets `binary_location` Chrome option.
   - Initializes `ChromeService` with binary path if available.
   - Initializes the `webdriver.Chrome` object.
   - **Example:** Calls `super().__init__(options=options, service=service)`

2. **Payload (Chrome Class):**
   - Creates `JavaScript` and `ExecuteLocator` objects.
   - **Example:** Instantiates `js_executor` to handle JavaScript interaction and `execute_locator` for general element interaction.
   - Adds methods related to page interaction and element manipulation from `JavaScript` and `ExecuteLocator`.
   - **Example:**  `self.get_page_lang`, `self.execute_locator`, `self.get_webelement_by_locator`.

**Data Flow:**

- Configuration data (from `chrome.json`) is passed to `Chrome` class's `__init__`.
- `Chrome` interacts with `gs.path`, `j_loads_ns` for configuration loading, and `normalize_path` for environment path handling.
- `ExecuteLocator` and `JavaScript` handle different functionalities (locating and interacting with elements in the browser) based on configuration and interaction events.

```

```explanation
- **Imports:**
    - `os`, `sys`, `threading`, `socket`: Standard library modules for operating system interaction, system information, thread management, and networking.
    - `pathlib`: Used for working with file paths in a platform-independent way.
    - `typing`: For type hinting, improving code readability and maintainability.
    - `types`: Used for the `SimpleNamespace` type, which is used to represent the structure of the config.
    - `selenium`, `selenium.webdriver.chrome.service`, `selenium.webdriver.chrome.options`: Selenium library modules for interacting with the web browser.
    - `fake_useragent`: Provides random user agents.
    - `selenium.common.exceptions`: Selenium's exceptions to handle potential errors.
    - `header`: This import is likely used for custom headers.
    - `gs`: Likely a package for handling global settings.
    - `src.webdriver.executor`, `src.webdriver.js`, `src.utils.jjson`, `src.logger`: Custom modules/packages within the project, likely providing functionalities related to web driver execution, JavaScript interaction, JSON handling, and logging respectively.

- **Classes:**
    - `Chrome(webdriver.Chrome)`: Extends Selenium's `webdriver.Chrome` to provide custom initialization, handling configuration from `chrome.json`, and adding additional functionality (like JavaScript interaction). It's a singleton, ensuring only one Chrome instance exists.

- **Functions:**
    - `normalize_path`: Takes a path string as input and replaces placeholders like `%APPDATA%` with their environment variable equivalents. Handles empty inputs preventing exceptions.
    - `__new__`: A static method overriding the default `__new__` to manage the creation of only one instance (singleton).
    - `_payload`: This method initializes the necessary elements for handling JavaScript interactions and locators for other modules.

- **Variables:**
    - `MODE`: A global variable representing the current execution mode ('dev' in this case).
    - `config`: A `SimpleNamespace` object containing the configuration from `chrome.json`, used throughout the class for accessing the settings.
    - `options`: A `ChromeOptions` object used to configure the Chrome browser instance.


- **Potential Errors/Improvements:**
    - **Error Handling:** The `try...except` blocks are crucial for handling potential errors during WebDriver initialization. However, the `...` placeholders within the error handling blocks should be replaced with specific error handling logic or logging. This is essential for robustness.
    - **Explicit type checking:**  `profile_directory` and `binary_location` could be explicitly typed.
    - **Robust path handling:**  `normalize_path` is a step towards robustness, but exception handling within the path normalization is missing.  More careful validation of paths and environment variable existence is needed.
    - **Configuration validation:** Ensure that `chrome.json` has the expected structure and values, especially `profile_directory` and `binary_location`.  Validation logic should be included.


**Relationship Chain:**

The code depends on `gs.path` for getting project root paths, which implies `gs` handles configuration loading (possibly from a global `settings.json`) and stores the root directory. `j_loads_ns` is in `src.utils.jjson` and loads settings. `Chrome` interacts with `webdriver.Chrome` and internally interacts with `ExecuteLocator` and `JavaScript` for more specific browser interactions, highlighting the layered architecture of the project.  `logger` and  `header` potentially inject logging or header information into the browser interactions.