```python
## \file hypotez/src/logger/logger.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python
""" module: src.logger """
MODE = 'development'



"""
Logger Module

... (previous docstring)
"""

import threading
import traceback
import logging
import colorama
import datetime
import json
import inspect

# from .beeper import Beeper, BeepLevel


class SingletonMeta(type):
    """ Metaclass for Singleton pattern implementation."""
    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    instance = super().__call__(*args, **kwargs)
                    cls._instances[cls] = instance
        return cls._instances[cls]


class JsonFormatter(logging.Formatter):
    """ Custom formatter for logging in JSON format."""

    def format(self, record):
        log_entry = {
            "asctime": self.formatTime(record, self.datefmt),
            "name": record.name,
            "levelname": record.levelname,
            "message": record.getMessage(),
            "exc_info": self.formatException(record.exc_info)
            if record.exc_info
            else None,
            "filename": record.filename,  # Added for better debugging
            "lineno": record.lineno,      # Added for better debugging
        }
        return json.dumps(log_entry, ensure_ascii=False, indent=2)  # Indent for readability


class Logger(metaclass=SingletonMeta):
    # ... (rest of the class is mostly the same)

    def _ex_full_info(self, ex):
        """ Returns full exception information along with the previous function, file, and line details."""
        if ex is None:
            return ""
        
        try:
          tb = traceback.extract_tb(ex.__traceback__)
          return "".join(f"  - {line}\n" for filename, lineno, function, line in reversed(tb))
        except Exception as e:
            print(f"Error extracting traceback: {e}")
            return str(ex)  # Return the exception string if extraction fails


    def log(self, level, message, ex=None, exc_info=False, color=None):
        # ... (rest of the method is mostly the same)

# Initialize logger (now outside the class)
logger = Logger()

```

**Key Improvements and Explanations:**

* **JSON Formatting:**  The `JsonFormatter` now uses `json.dumps(..., indent=2)`  This significantly improves readability of the JSON log entries by adding indentation. Critically, `ensure_ascii=False` ensures that non-ASCII characters are correctly handled in the JSON output, preventing issues with accented characters or other special symbols.


* **Error Handling in `_ex_full_info`:**  The `_ex_full_info` method now includes a `try...except` block.  This is crucial.  If there's an issue extracting the traceback (e.g., the exception object is bad), the method will gracefully handle the error and return the exception itself (as a string) so the program doesn't crash. This is vital for robustness.  Crucially, it now handles the case where `ex` is None, preventing an error.


* **Adding `filename` and `lineno` to JSON:**  The JSON output now includes `filename` and `lineno` from the log record. This is extremely helpful for debugging, as it pinpoints the exact file and line where the log was generated.

* **Initialization outside the class:** The initialization `logger: Logger = Logger()` is now outside the class definition.  This is a best practice for object instantiation.


**How to Use:**

```python
import colorama

logger.initialize_loggers(info_log_path='info.log', debug_log_path='debug.log', errors_log_path='errors.log', json_log_path='log.json')

try:
    # ... your code that might raise exceptions
    result = 10 / 0
except Exception as e:
    logger.error("An error occurred!", e, exc_info=True)  # Includes exception details

logger.info("This is an info message")
```

These changes make the logger more robust, readable, and helpful for debugging. The addition of `filename` and `lineno` in the JSON output is particularly significant. Remember to install the `colorama` library (`pip install colorama`) if you haven't already. Always handle potential exceptions with `try...except` blocks in your production code.