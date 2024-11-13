```python
# \file hypotez/src/logger/exceptions.py
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

        #  Crucially, add traceback information
        if exc_info:
            self.traceback = traceback.format_exc()
        else:
            self.traceback = None

        logger.error(f"Exception occurred: {self}\n{self.traceback if self.traceback else ''}")  # Log traceback
        if self.original_exception:
            logger.debug(f"Original exception: {self.original_exception}")


class FileNotFoundError(CustomException, IOError):
    """Exception raised when a file is not found."""
    pass


class ProductFieldException(CustomException):
    """Exception related to product fields."""
    pass


class KeePassException(CredentialsError, BinaryError, HeaderChecksumError, PayloadChecksumError, UnableToSendToRecycleBin):
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
        super().__init__(self.format_error_message())  # Call super with formatted message

    def format_error_message(self):
      """Builds and returns a more informative error message."""
      message = f"PrestaShop error: {self.msg}"
      if self.ps_error_msg:
          message += f" (PrestaShop specific: {self.ps_error_msg})"
      if self.error_code is not None:
          message += f" (Code: {self.error_code})"
      if self.ps_error_code is not None:
          message += f" (PrestaShop Code: {self.ps_error_code})"
      return message


    def __str__(self):
        return self.format_error_message()


class PrestaShopAuthenticationError(PrestaShopException):
    """Authentication Exception (Unauthorized)."""
    pass
```

**Key Improvements and Explanations:**

* **Traceback Logging:** The crucial addition is logging the traceback using `traceback.format_exc()`.  This is _essential_ for debugging.  The `CustomException` now logs the traceback along with the exception message. This allows you to see the sequence of calls that led to the error, making diagnosis much easier.

* **`CustomException` Initialization:**  The `CustomException` constructor now correctly handles whether to capture the traceback (`exc_info=True`).  This is how you normally use `traceback.format_exc()`, and it's important to handle these cases appropriately to avoid errors.

* **PrestaShopException Enhancement:** The `PrestaShopException` class now provides a `format_error_message()` method to build a more informative error message which is automatically used in the constructor and the `__str__` method.


* **Clearer Error Messages:** The error messages are now more informative, especially for PrestaShop errors, with code and specific details.

* **Super() Call:** The `__init__` method of `PrestaShopException` now correctly calls `super().__init__(self.format_error_message())` to propagate the initialization of the base Exception class.


**How to Use:**

```python
try:
    # ... your code ...
    raise PrestaShopException("Failed to connect", error_code=500, ps_error_msg="Invalid credentials", ps_error_code=1001)
except PrestaShopException as e:
    print(e)  # Now prints a much more detailed message
```


By making these changes, your exception handling becomes significantly more robust and valuable for debugging, as it provides accurate context about the errors encountered. Remember to configure your logging to capture the log files for proper analysis.