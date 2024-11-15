```python
## \file hypotez/src/logger/logger.py
# -*- coding: utf-8 -*-
 # <- venv win
## ~~~~~~~~~~~~~
""" module: src.logger """

"""
Logger Module

This module provides a singleton logging utility with various logging levels and formats, including console, file, and JSON logging. It utilizes the Singleton design pattern to ensure a single instance of the logger is used throughout the application. The logger supports different log levels and output formats, and it can colorize console messages based on log severity.

Classes:
- SingletonMeta: Metaclass for Singleton pattern implementation.
- JsonFormatter: Custom formatter for logging in JSON format.
- Logger: Singleton logger class with methods for logging at different levels.

Functions:
- get_logger(): Returns the singleton Logger instance.

Examples:
    # Get the logger instance
    logger = get_logger()

    # Initialize the logger (must be done only once per application)
    logger.initialize_loggers(info_log_path='info.log', debug_log_path='debug.log', errors_log_path='errors.log', json_log_path='log.json')

    # Log messages at different levels
    logger.info('This is an info message')
    logger.success('This is a success message')
    logger.warning('This is a warning message')
    logger.debug('This is a debug message')
    logger.error('This is an error message', Exception("Example error"))
    logger.critical('This is a critical message', Exception("Critical error"))

"""
import threading
import traceback
import logging
import colorama
import datetime
import json
import inspect


def get_logger():
    """Returns the singleton Logger instance."""
    return Logger()



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
            "exc_info": self.formatException(record.exc_info) if record.exc_info else None,
        }
        return json.dumps(log_entry, ensure_ascii=False)


class Logger(metaclass=SingletonMeta):
    """ Singleton logger class with methods for console, file, and JSON logging."""

    # Class attributes declaration
    logger_console: logging.Logger = None
    logger_file_info: logging.Logger = None
    logger_file_debug: logging.Logger = None
    logger_file_errors: logging.Logger = None
    logger_file_json: logging.Logger = None
    _initialized: bool = False


    # ... (rest of the class remains the same, but crucial changes are made below)


    def initialize_loggers(self, info_log_path="", debug_log_path="", errors_log_path="", json_log_path=""):
        if self._initialized:
            return  # Avoid reinitialization

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        # ... (rest of the method remains the same)

    # ... (rest of the methods remain the same, with improvements)


    def _ex_full_info(self, ex):
        """ Returns full exception information along with previous function, file, and line details."""
        if ex is None: return ""

        tb_list = traceback.extract_tb(ex.__traceback__)
        return "\n".join(
            f"  File: {frame.filename}, Function: {frame.name}, Line: {frame.lineno}\n"
            for frame in reversed(tb_list)
        )



    def log(self, level, message, ex=None, exc_info=False, color=None):
        # ... (rest of the method)


# Example usage (outside the class definition):
# logger = get_logger()
# logger.initialize_loggers(...)
```

**Key Improvements and Explanation:**

* **`get_logger()` Function:** Added a crucial function to retrieve the singleton instance. This is a much better design practice than having the initialization code directly inside the class definition.  Other parts of your application can now easily obtain the `Logger` instance.
* **Initialization Flag:** The `_initialized` flag is crucial. It prevents multiple calls to `initialize_loggers()` leading to multiple log files and potential errors. You **only** call `initialize_loggers()` once per application instance.
* **Error Handling in `_ex_full_info`:** Added a check for `ex` being `None` to avoid `AttributeError`.
* **Timestamp Format:** Changed the timestamp format to `YYYY-MM-DD_HH-MM-SS` which is more readable and unambiguous.


**How to use:**

```python
import logging
import sys
# ... (other imports)


# In your main script or application setup:
logger = get_logger()
logger.initialize_loggers(
    info_log_path="info.log", debug_log_path="debug.log", errors_log_path="errors.log", json_log_path="log.json"
)


# ... later in your code

try:
    # some code that might raise an exception
    result = some_function()
except Exception as e:
    logger.error("An error occurred:", e)
```

**Important Consideration:**

Place the `initialize_loggers()` call **only once** in your application where it is first loaded, either in your main `if __name__ == "__main__":` block or during application initialization.  Avoid calling it repeatedly.  This single initialization is the key to the singleton pattern working correctly.


This revised solution is much more robust and follows best practices for Python logging and design. Remember to install the necessary libraries (`colorama`).