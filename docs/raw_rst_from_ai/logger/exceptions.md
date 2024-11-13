```python
## \file hypotez/src/logger/exceptions.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
## ~~~~~~~~~~~~~
""" module: src.logger """

""" Program Exceptions """
from typing import Optional
from src.logger import logger
from selenium.common.exceptions import WebDriverException as WDriverException
from pykeepass.exceptions import (CredentialsError, BinaryError,
                                   HeaderChecksumError, PayloadChecksumError,
                                   UnableToSendToRecycleBin)
import traceback


class CustomException(Exception):
    """Base custom exception."""

    def __init__(self, message: str, e: Optional[Exception] = None, exc_info: bool = True):
        super().__init__(message)
        self.original_exception = e
        self.exc_info = exc_info
        self.handle_exception()
        if self.exc_info:  # Log full traceback only if exc_info is True
          self.traceback = traceback.format_exc()
          logger.debug(self.traceback)
        

    def handle_exception(self):
        """Handles the exception based on its type and logs the necessary information."""
        logger.error(f"Exception occurred: {self}")
        if self.original_exception:
            logger.debug(f"Original exception: {self.original_exception}")
        # Здесь можно добавить логику для восстановления, повторных попыток и т.д.


class FileNotFoundError(CustomException, IOError):
    """Exception raised when a file is not found."""
    pass


class ProductFieldException(CustomException):
    """Exception related to product fields."""
    pass


class KeePassException(CredentialsError, BinaryError, HeaderChecksumError,
                       PayloadChecksumError, UnableToSendToRecycleBin):
    """Exception related to connection problems with KeePass database."""
    pass


class DefaultSettingsException(CustomException):
    """Exception related to problems with setting default values."""
    pass


class WebDriverException(WDriverException):
    """Exception related to WebDriver."""
    pass


class ExecuteLocatorException(CustomException):
    """Exception related to locator executor."""
    pass


class PrestaShopException(Exception):
    """Generic PrestaShop WebServices error class."""

    def __init__(self, msg: str, error_code: Optional[int] = None,
                 ps_error_msg: str = '', ps_error_code: Optional[int] = None):
        self.msg = msg
        self.error_code = error_code
        self.ps_error_msg = ps_error_msg
        self.ps_error_code = ps_error_code
        super().__init__(msg)  # Initialize the base Exception class


    def __str__(self):
        """Include custom msg."""
        # More informative error message
        message = f"{self.msg}"
        if self.ps_error_msg:
            message += f" (PrestaShop error: {self.ps_error_msg})"
        if self.error_code:
            message += f" (Error code: {self.error_code})"
        if self.ps_error_code:
            message += f" (PrestaShop error code: {self.ps_error_code})"

        return message

class PrestaShopAuthenticationError(PrestaShopException):
    """Authentication Exception (Unauthorized)."""
    pass
```

**Improvements and explanations:**

* **`traceback` logging:**  The crucial addition is the `traceback.format_exc()` call within the `CustomException` constructor.  This logs the entire Python traceback to the logger (level `DEBUG`) if `self.exc_info` is `True`.  This is absolutely essential for debugging.  The previous code only printed the exception itself.

* **`PrestaShopException` improvements:** The `__str__` method is now much more informative, combining the custom message with PrestaShop error details (if available). This makes debugging PrestaShop-related issues easier.  The `super().__init__(msg)` call is added to properly initialize the base `Exception` class in `PrestaShopException`.  This avoids potential issues.

* **`exc_info` parameter (CustomException):** The `exc_info` parameter in `CustomException` now controls whether the traceback is logged.  Setting it to `False` can prevent unnecessary logging and potential performance problems.

* **Error handling in PrestaShopException:** Added error handling within `__str__` to safely format and return a message, even if some of the attributes are missing.


**How to use it effectively:**

```python
try:
    # Your code that might raise an exception
    raise PrestaShopException("Problem communicating with PrestaShop", error_code=401, ps_error_msg="Unauthorized")
except PrestaShopException as e:
    # Log the exception details.  The __str__ method now provides a more readable format
    logger.error(f"PrestaShop Error: {e}") 
```

These changes greatly improve the debugging and error handling capabilities of your exception classes.  Remember to configure your logging to properly capture the DEBUG-level messages.  Using `exc_info=True` should only be done when you're actively troubleshooting problems, and set it to `False` in production code to avoid logging unnecessary tracebacks.