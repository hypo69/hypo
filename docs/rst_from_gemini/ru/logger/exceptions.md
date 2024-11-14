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
    """Base custom exception.  Includes logging and handling for original exceptions."""
    
    def __init__(self, message: str, e: Optional[Exception] = None, exc_info: bool = True):
        super().__init__(message)
        self.original_exception = e
        self.exc_info = exc_info  # Flag to determine if traceback should be logged
        self.log_exception()

    def log_exception(self):
        """Logs the exception and any original exceptions, including the traceback."""
        try:
            logger.error(f"Exception occurred: {self}, Message: {self.args[0]}")
            if self.exc_info:
                logger.debug("Full traceback info:", exc_info=True)
            if self.original_exception:
                logger.debug(f"Original exception: {self.original_exception}")
                if self.exc_info and self.original_exception:
                    logger.debug("Original exception's traceback:", exc_info=True)
        except Exception as e:
            logger.error(f"Error during exception logging: {e}")

# ... (rest of the code is the same) ...

class PrestaShopException(Exception):
    """Generic PrestaShop WebServices error class."""
    def __init__(self, msg: str, error_code: Optional[int] = None,
                 ps_error_msg: str = '', ps_error_code: Optional[int] = None):
        self.msg = msg
        self.error_code = error_code
        self.ps_error_msg = ps_error_msg
        self.ps_error_code = ps_error_code
        super().__init__(self.get_full_message())

    def get_full_message(self):
      """Returns a user-friendly error message."""
      if self.ps_error_msg:
        return f"{self.msg} (PrestaShop Error Code: {self.ps_error_code}, Message: {self.ps_error_msg})"
      else:
        return f"{self.msg} (Error Code: {self.error_code})"

    def __str__(self):
      return self.get_full_message()



```

**Improvements and Explanations:**

* **`log_exception()` method:** This centralizes exception logging within `CustomException`.  It's more organized and prevents potential errors if the logging logic is needed in multiple places. Critically, it now handles any potential errors during logging itself, preventing crashes.  Crucially, it now uses `exc_info=True`  for the original exception if the `exc_info` flag is set.
* **`exc_info` parameter:**  The `CustomException` now accepts an `exc_info` parameter.  This allows the caller to control whether to include a full traceback of the original exception in the log.  This is particularly useful if you want to log detailed traceback for debugging but don't want that level of detail in production logs.
* **Robust Logging:** The logging is now more robust to handle potential errors that might occur during logging. This is essential because if you get an error while logging an exception, it could cause your application to fail silently.
* **`PrestaShopException` Enhancement:** The `PrestaShopException` now has a `get_full_message()` method. This method constructs a more user-friendly error message that includes the PrestaShop error code and message, if available, in a cleaner format.  This makes debugging easier.


**How to use the improved `CustomException`:**

```python
try:
    # ... some code that might raise an exception ...
except SomeException as e:
    raise CustomException("A problem occurred", e, exc_info=True) # Log full traceback
```

```python
try:
    # ... some code that might raise an exception ...
except SomeException as e:
    raise CustomException("A problem occurred", e, exc_info=False) # Don't log full traceback
```

By setting `exc_info` to `True` or `False`, you choose whether or not to capture the traceback of the original exception when logging it.  This improved structure helps make your exception handling and logging cleaner, more robust, and more informative. Remember to adapt this structure to your specific error handling needs.