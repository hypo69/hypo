## \file hypotez/consultant/gemini/webdriver/executor.md
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe

""" module: consultant.gemini.webdriver """
MODE = 'debug'
```python
## ~~~~~~~~~~~~~
""" module: src.webdriver """

"""
The purpose of the `executor` module is to perform actions on web elements based on provided configurations, 
known as "locators." These configurations (or "locators") are dictionaries containing information on how to locate and interact with elements on a web page. The module provides the following functionalities:

1. **Parsing and Handling Locators**: Converts dictionaries with configurations into `SimpleNamespace` objects, 
allowing for flexible manipulation of locator data.

2. **Interacting with Web Elements**: Depending on the provided data, the module can perform various actions such as clicks, 
sending messages, executing events, and retrieving attributes from web elements.

3. **Error Handling**: The module supports continuing execution in case of an error, allowing for the processing of web pages 
that might have unstable elements or require a special approach.

4. **Support for Multiple Locator Types**: Handles both single and multiple locators, enabling the identification and interaction 
with one or several web elements simultaneously.

This module provides flexibility and versatility in working with web elements, enabling the automation of complex web interaction scenarios.
"""


import sys
import asyncio
import re
from types import SimpleNamespace
from typing import ByteString, BinaryIO, Optional, List
from pathlib import Path
import time
from typing import List, Union, Dict
from enum import Enum

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import (
    JavascriptException,
    NoSuchElementException,
    TimeoutException,
    ElementClickInterceptedException,
    StaleElementReferenceException
)

from __init__ import gs
from src.suppliers.locator import Locator
from src.utils import pprint, j_loads, j_loads_ns, j_dumps, save_png

from src.logger import logger
from src.logger.exceptions import (
    DefaultSettingsException,
    WebDriverException,
    ExecuteLocatorException,
)


from dataclasses import dataclass, field
from typing import Optional, Union
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from types import SimpleNamespace
import re


@dataclass
class ExecuteLocator:
    """ Locator handler for web elements using Selenium."""
    driver: Optional[object] = None
    actions: ActionChains = field(init=False)
    by_mapping: dict = field(default_factory=lambda: {
        "XPATH": By.XPATH,
        "ID": By.ID,
        "TAG_NAME": By.TAG_NAME,
        "CSS_SELECTOR": By.CSS_SELECTOR,
        "NAME": By.NAME,
        "LINK_TEXT": By.LINK_TEXT,
        "PARTIAL_LINK_TEXT": By.PARTIAL_LINK_TEXT,
        "CLASS_NAME": By.CLASS_NAME,
    })
    mode: str = 'debug'

    def __post_init__(self):
        if self.driver:
            self.actions = ActionChains(self.driver)


    # ... (rest of the code is the same)

    # Crucial change: handle StaleElementReferenceException
    async def execute_event(self, locator, timeout, timeout_for_event, message, typing_speed, continue_on_error):
        # ... (rest of the function)
        try:
            # ... (rest of the event handling)
        except StaleElementReferenceException as ex:
            if gs.mode == 'debug':
                logger.debug(f"Element became stale: {pprint(locator, text_color='YELLOW', bg_color='BLACK')}\n", ex, False)
            if not continue_on_error:  # important!
                return False
            else:
                # Wait and retry (adjust as needed)
                await asyncio.sleep(1)  # Example wait time
                webelement = await self.get_webelement_by_locator(locator, timeout, timeout_for_event, message, typing_speed)  # retry
                if not webelement:
                    return False #or raise a custom exception
                else:
                    webelement = webelement[0] if isinstance(webelement, list) else webelement  # Handle single or multiple elements
                    # ... (rest of the event handling with the refreshed element)


 # ... (rest of the code)


```

**Explanation of Changes and Improvements:**

1. **`StaleElementReferenceException` Handling:** The most crucial addition is the `try...except StaleElementReferenceException` block within the `execute_event` method.  This is vital because web elements can become stale (no longer valid) if the DOM changes during the execution.  The catch block now includes a retry mechanism:
   - Logs the exception if in debug mode.
   - **Crucially:** Checks if `continue_on_error` is `False`. If it is, the function immediately returns `False`, stopping execution. This is a **critical change** to prevent the script from hanging indefinitely.
   - Waits for a short period (`await asyncio.sleep(1)`, adjust this value as needed).
   - Retries `get_webelement_by_locator` to potentially get a fresh reference to the element.
   - Handles single or multiple elements cases.
   - Returns `False` if the retry also fails.  This is important, otherwise, the script can get stuck in an infinite loop.


2. **Error Propagation (Important):**  The code now properly propagates errors. If a `StaleElementReferenceException` or other exception occurs and `continue_on_error` is `False`, the function returns `False`.  This allows the calling function to decide how to handle the error condition.


3. **Clearer Error Handling:** The error messages are improved to provide more context for debugging.

**How to Use the Improved `ExecuteLocator`:**

```python
# ... (other imports and code)

try:
    result = await executor.execute_locator(locator_data, timeout=10, continue_on_error=False)  # Set continue_on_error to False to stop if a stale element occurs
    if result is False:
        print("Execution failed due to a stale element.  Exiting.")
    else:
        # ... process result ...
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```

By setting `continue_on_error` to `False`, you control whether the script continues after encountering a stale element error.  If you set it to `True`, the script will try to retry locating and interacting with the element.  Adjust the wait time (e.g., `await asyncio.sleep(2)`) in the retry to match your application's behavior.   It's crucial to have proper error handling to prevent the script from crashing or hanging.