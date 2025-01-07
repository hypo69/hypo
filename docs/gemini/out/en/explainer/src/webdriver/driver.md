# Analysis of hypotez/src/webdriver/driver.py

## <input code>

```python
## \file hypotez/src/webdriver/driver.py
# -*- coding: utf-8 -*-\n
#! venv/bin/python/python3.12
# ... (rest of the code)
```

## <algorithm>

The algorithm of the `driver.py` file can be broken down into the following steps:

1. **Initialization:** The `Driver` class is initialized with a `webdriver_cls` (e.g., `Chrome`, `Firefox`), along with optional positional and keyword arguments for the webdriver.  A new `webdriver_cls` instance is created and assigned to `self.driver`.


   * **Example:** `driver = Driver(Chrome, executable_path='/path/to/chromedriver')`


2. **Subclass Initialization:** The `__init_subclass__` method is automatically called when a subclass of `Driver` is created.  It validates that the `browser_name` is provided.

   * **Example:** `class MyChromeDriver(Driver, browser_name='chrome'): ...`


3. **Attribute Access Proxy:** The `__getattr__` method acts as a proxy for accessing attributes of the underlying `webdriver` instance.

   * **Example:** `driver.current_url`


4. **Scrolling:** The `scroll` method allows scrolling the page, either up, down, or both. It calls the `carousel` method for the task.

   * **Example:** `driver.scroll(scrolls=3, direction='down')`


5. **Language Detection:** The `locale` method tries to detect the page language from meta tags and, if necessary, from Javascript.

   * **Example:** `lang = driver.locale`


6. **URL Navigation:** The `get_url` method navigates to a given URL. It handles potential `WebDriverException`, `InvalidArgumentException`, and other exceptions. It also saves the current, previous URL, and cookies.

   * **Example:** `driver.get_url('https://example.com')`


7. **Window Management:** The `window_open` method opens a new tab/window and switches to it, optionally navigating to a URL.

   * **Example:** `driver.window_open('https://anothersite.com')`


8. **Waiting:** The `wait` method introduces a pause.


9. **Cookie Saving:** The `_save_cookies_locally` method saves the current cookies to a local file (`gs.cookies_filepath`).


10. **HTML Fetching:** The `fetch_html` method fetches HTML from either a file (if URL starts with 'file://') or a web page (if starts with 'http://' or 'https://').


   * **Example:** `driver.fetch_html('file:///path/to/file.html')` or `driver.fetch_html('https://example.com')`


## <mermaid>

```mermaid
graph LR
    A[Driver] --> B{__init__};
    B --> C[webdriver_cls instance];
    A --> D{__getattr__};
    A --> E[scroll];
    A --> F[locale];
    A --> G[get_url];
    A --> H[window_open];
    A --> I[wait];
    A --> J{_save_cookies_localy};
    A --> K[fetch_html];
    E --> L[carousel];
    F --> M[find_element];
    G --> N[driver.get];
    G --> O[self.ready_state check];
    G --> P[save current URL];
    G --> Q[save previous URL];
    G --> R[save cookies];
    K --> S[if file];
    K --> T[if http/https];
    S --> U[open file];
    T --> V[driver.get_url];
    subgraph Selenium Imports
        A --> |selenium|
        A --> |header|
        A --> |gs|
        A --> |logger|
    end
```

**Dependencies Analysis:**

The diagram shows dependencies on `selenium` (for webdriver interaction), `header` (likely for project-specific headers or configurations), `gs` (possibly for global settings), and `logger` (for logging).


## <explanation>

* **Imports:**
    * `copy`, `pickle`, `time`, `re`, `pathlib`, `typing`: Standard Python libraries for copying objects, saving data, timing, regular expressions, file paths, and type hinting, respectively.
    * `selenium.webdriver.common.by`, `selenium.common.exceptions`: Selenium library for interacting with webdrivers and handling exceptions during interaction. These are crucial for web automation tasks.
    * `header`: Likely contains project-specific configuration or helper functions.
    * `src.gs`, `src.logger`, `src.logger.exceptions`: Modules from the `src` package, likely for global settings, logging, and custom exceptions related to web driver interactions.  The `gs` (likely for global settings) and `logger` (for handling errors during execution) is vital for the project's structure, organization, and error handling.


* **Classes:**
    * `Driver`: A class providing a unified interface for interacting with Selenium WebDriver instances. It handles driver initialization, navigation, scrolling, language detection, saving cookies, and more.  The `Driver` class serves as an abstraction layer, allowing the code to work with different WebDriver implementations (Chrome, Firefox, etc.) without needing to change the core logic.  The `__init_subclass__` method is a nice touch for enforcing certain configurations on subclasses.

* **Functions:**
    * `__init__(self, webdriver_cls, *args, **kwargs)`: Initializes the `Driver` object with the WebDriver class and its parameters. It validates `webdriver_cls` to ensure it's a valid WebDriver class.
    * `scroll(self, scrolls=1, frame_size=600, direction='both', delay=.3)`: Scrolls the page in the specified direction. The `carousel` function is an excellent local helper function for cleaner and more understandable scrolling logic.
    * `locale(self)`: Detects the page language using meta tags or JavaScript.
    * `get_url(self, url: str)`: Navigates to a given URL, handling potential errors robustly.  It's important to handle exceptions in web automation scripts to prevent failures and ensure robustness.
    * `window_open(self, url=None)`: Opens a new tab/window and switches to it, optionally loading a URL.
    * `wait(self, delay=.3)`: Introduces a delay (often necessary for web page elements to load).
    * `_save_cookies_localy(self)`: Saves the current driver cookies to a file.
    * `fetch_html(self, url: str)`: Fetches HTML content from either a file or a web page.  The implementation correctly handles both local and remote URL fetching.


* **Variables:**
    * `MODE`: A string variable representing the current mode (likely 'dev' for development).
    * `gs.cookies_filepath`: A variable (likely from the `gs` module) holding the path to the file where cookies will be stored.
    * `self.driver`: An instance of a Selenium WebDriver.
    * `self.html_content`: A variable storing the fetched HTML content.


* **Potential Errors/Improvements:**
    * The `_save_cookies_localy` method is currently returning `True`, which is likely a placeholder. The code should raise an exception if there's a problem saving the cookies.
    * While handling exceptions, consider providing more informative messages to the user to help diagnose the problem.
    * The logic to handle different URL schemes (file, http, https) within `fetch_html` is well-structured.


**Relationships with Other Parts of the Project:**

The `Driver` class relies heavily on the `src.gs` (likely for global settings) and `src.logger` (for logging) modules.  The `gs` module likely defines configurations (e.g., the cookie storage path). The `logger` module provides centralized error handling and logging capabilities.

The project likely uses the `webdriver` module to automate web interactions within a larger system.