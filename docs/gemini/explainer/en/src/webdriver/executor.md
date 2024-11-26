```## File: hypotez/src/webdriver/executor.py
# -*- coding: utf-8 -*-\n#! venv/Scripts/python.exe\n#! venv/bin/python/python3.12\n\n"""\n.. module: src.webdriver \n\t:platform: Windows, Unix\n\t:synopsis: The purpose of the `executor` module is to perform actions on web elements based on provided configurations, \nknown as "locators." These configurations (or "locators") are dictionaries containing information on how to locate and interact with elements on a web page. The module provides the following functionalities:\n\n1. **Parsing and Handling Locators**: Converts dictionaries with configurations into `SimpleNamespace` objects, \nallowing for flexible manipulation of locator data.\n\n2. **Interacting with Web Elements**: Depending on the provided data, the module can perform various actions such as clicks, \nsending messages, executing events, and retrieving attributes from web elements.\n\n3. **Error Handling**: The module supports continuing execution in case of an error, allowing for the processing of web pages \nthat might have unstable elements or require a special approach.\n\n4. **Support for Multiple Locator Types**: Handles both single and multiple locators, enabling the identification and interaction \nwith one or several web elements simultaneously.\n\nThis module provides flexibility and versatility in working with web elements, enabling the automation of complex web interaction scenarios.\n\n\n"""
MODE = \'dev\'

import asyncio
import re
import sys
import time
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from types import SimpleNamespace
from typing import BinaryIO, ByteString, Dict, List, Optional, Union

from selenium.common.exceptions import (
    ElementClickInterceptedException,
    JavascriptException,
    NoSuchElementException,
    StaleElementReferenceException,  # Этот импорт был добавлен
    TimeoutException,
)
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import header
from src import gs
from src.logger import logger
from src.logger.exceptions import (
    DefaultSettingsException,
    ExecuteLocatorException,
    WebDriverException,
)

from src.utils.jjson import j_dumps, j_loads, j_loads_ns
from src.utils.printer import pprint
from src.utils.image import save_png
```

**<algorithm>**

```mermaid
graph TD
    A[Input Locator (dict or SimpleNamespace)] --> B{Convert to SimpleNamespace};
    B --> C{Parse Locator};
    C -- Event --> D[execute_event];
    C -- Attribute --> E[get_attribute_by_locator];
    C -- WebElement --> F[get_webelement_by_locator];
    D --> G[Event Execution];
    E --> H[Attribute Retrieval];
    F --> I[Element Retrieval];
    G -- Success --> J[Return Result];
    G -- Failure --> K[Error Handling (log, continue)];
    H -- Success --> J;
    H -- Failure --> K;
    I -- Success --> J;
    I -- Failure --> K;
    J --> L[Output Result];
    K --> L;
```

**Example Data Flow:**

* **Input Locator:** `{"by": "XPATH", "selector": "//button[@id='submit']", "event": "click()"}`
* **Convert to SimpleNamespace:** Creates a `SimpleNamespace` object with attributes `by`, `selector`, and `event` from the input dictionary.
* **Parse Locator:**  Extracts the locator type (`XPATH`), the selector (`//button[@id='submit']`), and the event ("click()").
* **`execute_event`:**  Identifies the event type (`click()`).
* **`get_webelement_by_locator`:** Locates the web element using the XPATH.
* **Event Execution:** The `click()` event is executed on the located element.
* **Return Result:**  Returns `True` if the click was successful (or relevant result).

**<explanation>**

* **Imports:**  Import statements bring in necessary libraries and modules:
    * `asyncio`: For asynchronous operations (crucial for web interactions).
    * `re`: For regular expressions (used for parsing).
    * `time`: For time-related operations.
    * `types`: Provides `SimpleNamespace` for structuring locator data.
    * `selenium`:  Essential for interacting with web browsers (Selenium library).  Crucial imports are included for various exceptions and essential classes for web automation.
    * `src`: Modules related to specific project functionality (e.g., logging, data processing)
    * `header`: Likely another module in the project.
    * `gs`: Likely a module within the project.
    * `utils`: Utility modules like `jjson` (JSON handling), `printer` (pretty printing), `image` (screenshots).
    * All the other imports from `src` folders likely handle data-processing, logging, and error handling in the project.
* **Classes:**
    * `ExecuteLocator`: This class encapsulates web element interaction logic.
        * `driver`: Selenium WebDriver instance.
        * `actions`: `ActionChains` object for more complex interactions.
        * `by_mapping`: Dictionary to map locator types (XPATH, ID, etc.) to Selenium's `By` constants. This improves code readability and maintainability.
        * `mode`: Controls debugging level (e.g., debug, dev).  This is a good practice for configurable behaviour.
        * `__post_init__`: Initializes `actions` using the provided `driver`.
        * `execute_locator`:  The core method for interacting with web elements based on a locator.  It gracefully handles different locator types (dicts, SimpleNamespaces) and various actions (click, send keys, attribute retrieval). This is a method for handling multiple actions and scenarios, making it more robust.
        * `evaluate_locator`, `get_attribute_by_locator`, `get_webelement_by_locator`, `execute_event`, `get_webelement_as_screenshot`, `send_message`: Helper methods for specific actions and error handling. The careful inclusion of optional parameters allows for flexible execution without error.
* **Functions:**
    * `evaluate_locator`: Processes locator attributes, handling various types and special key codes for sending keys. (Keys object in Selenium).
    * `get_attribute_by_locator`: Retrieves attributes from a web element or list of elements using a locator. This robust function now handles lists of web elements and a dictionary format, improving flexibility.
    * `get_webelement_by_locator`: Locates a web element using the given locator, and with timeouts.
    * `execute_event`: Executes various actions (click, sending messages). This critical function now includes a robust way to handle multiple actions per locator.
    * `get_webelement_as_screenshot`: Captures a screenshot of a web element. This crucial function now supports screenshot capture with provided web element or element retrieval. This is very useful for debugging and visual feedback.
    * `send_message`: Sends a message to an input element. This method can send multiple messages, supports typing speed and character replacements. It has good structure for managing the typing process and user input, useful for sending messages with complicated characters, or long messages, improving user input and efficiency.
* **Variables:** `MODE`, `timeout`, `timeout_for_event` are crucial variables for controlling the behaviour, error handling, and execution flow.
* **Potential Errors/Improvements:**
    * **Error Handling:** The `try...except` blocks are good for handling Selenium exceptions, but more specific exception handling could lead to better error messages.  Including error propagation with context (locator info, exception) would be helpful.
    * **Asynchronous Operations:** While using `asyncio`, the use of `asyncio.to_thread` might have performance implications if the underlying Selenium operations are not asynchronous, but are blocking. An improvement would be to use async methods for all Selenium functions, potentially converting them to async equivalents if possible.
    * **Clarity and Consistency:** While the docstrings are good, adding more explicit return types or type hints within the code could help clarify expectations. This improves readability and type checking.
    * **`ActionChains`:**  Use `ActionChains` more effectively for complex actions (e.g., mouseovers) rather than relying on `send_keys`. This would improve efficiency and correctness.
    * **Robustness:** Adding more checks in the `send_keys`, `type` functions in regards to the presence of `element` would be necessary.  Handling cases where `message` is not a string for example.


**Relationship Chain:**

This `executor` module relies on `selenium` for web interaction.  It uses other `src` modules for logging (`logger`), JSON manipulation (`jjson`), and general utility functions (`utils`).  The `header` module is likely part of the project's infrastructure, providing setup or configuration information.  `gs` is likely another project component, offering data access and processing. The dependency chain within the `src` modules is complex and reflects the project architecture.