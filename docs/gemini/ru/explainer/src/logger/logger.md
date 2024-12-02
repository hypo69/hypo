# <input code>

```python
# -*- coding: utf-8 -*-\
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.logger 
	:platform: Windows, Unix
	:synopsis: Logger Module
"""
MODE = 'dev'

"""This module provides a singleton logging utility with various logging levels and formats, including console, file, and JSON logging. It utilizes the Singleton design pattern to ensure a single instance of the logger is used throughout the application. The logger supports different log levels and output formats, and it can colorize console messages based on log severity.

Classes:
- SingletonMeta: Metaclass for Singleton pattern implementation.
- JsonFormatter: Custom formatter for logging in JSON format.
- Logger: Singleton logger class with methods for logging at different levels.

Classes:
    SingletonMeta
    ----------
    Metaclass for Singleton pattern implementation.
    
    JsonFormatter
    ------------
    Custom formatter for logging in JSON format.
    
    Logger
    ------
    Singleton logger class with methods for console, file, and JSON logging.

Functions:
- __init__: Initializes the Logger instance.
- _configure_logger: Configures and returns a logger with the specified parameters.
- initialize_loggers: Initializes loggers for console, file, and JSON output.
- _format_message: Formats a message with optional color and exception information.
- _ex_full_info: Provides detailed exception information, including the file, function, and line number where the log was called.
- log: Logs messages at a specified level with optional color and exception information.
- info: Logs an info message.
- success: Logs a success message.
- warning: Logs a warning message.
- debug: Logs a debug message.
- error: Logs an error message.
- critical: Logs a critical message.
- info_red: Logs an info message in red.
- info_black: Logs an info message in black with a white background.

Examples:
    # Initialize the logger
    logger: Logger = Logger()
    logger.initialize_loggers(info_log_path='info.log', debug_log_path='debug.log', errors_log_path='errors.log', json_log_path='log.json')

    # Log messages at different levels
    logger.info('This is an info message')
    logger.success('This is a success message')
    logger.warning('This is a warning message',None,True)
    logger.debug('This is a debug message',None,exc_info=True)
    logger.error('This is an error message',ex)
    logger.critical('This is a critical message',ex)
"""

# -*- coding: utf-8 -*-\
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.logger
    :platform: Windows, Unix
    :synopsis: Logger Module
"""

import threading
import traceback
import logging
from typing import Optional
import colorama
import datetime
import json
import inspect

# ... (rest of the code)
```

# <algorithm>

The algorithm can be described as follows:

1. **Initialization (Singleton):** The `Logger` class uses the `SingletonMeta` metaclass to ensure only one instance of the logger exists.  This is achieved through a `_lock` (for thread safety) and `_instances` dictionary.

2. **Configuration (loggers):**
    * The `initialize_loggers` method configures different loggers: console, file (info, debug, errors), and JSON.
    * It creates loggers using `_configure_logger` with specific parameters: log path, log level, and formatter.
    * For JSON, a custom `JsonFormatter` is used.

3. **Logging (log and other methods):**
    * The `log` method handles the common logic for logging at different levels (info, success, warning, etc.)
    * It formats the message, potentially including color and exception details.
    * It logs the message to the console, to the relevant file loggers if initialized, and to the JSON logger.

4. **Formatting:**
    * `_format_message` formats messages, including colorization (using `colorama`).
    * `_ex_full_info` extracts exception details (file, function, line number) to provide better context in the log.

5. **Thread Safety:**
    * `threading.Lock()` is crucial to ensure thread safety when creating and accessing the logger instance.

**Example Data Flow:**

```
User Call -> Logger.info() -> Logger._format_message(color=green) -> Logger.log(level=INFO, message=formatted) ->
Logger.logger_console -> logging.Handler -> terminal (colored)
Logger.logger_file_info -> logging.Handler -> info.log
Logger.logger_file_json -> logging.Handler -> log.json (JSON format)
```

# <mermaid>

```mermaid
graph TD
    subgraph Logger Initialization
        A[User Calls Logger()] --> B{Check Instance Exists?};
        B -- Yes --> C[Return Existing Instance];
        B -- No --> D[Create Logger Instance];
        D --> E[initialize_loggers()];
        E --> F[Configure Loggers];
        F --> G[Set Loggers (console, files, JSON)];
    end
    subgraph Logging
        H[User Call: Logger.info()];
        H --> I[Logger.log(level=INFO)];
        I --> J[Logger._format_message()];
        J --> K[Logger._ex_full_info(optional)];
        J -- message --> L[Output to console (using logger_console)];
        J -- message --> M[Output to info log file (using logger_file_info)];
        J -- message --> N[Output to json log file (using logger_file_json)];
    end
    F -- Loggers -- G;
    L --> O[Terminal];
    M --> P[info.log];
    N --> Q[log.json];
```

# <explanation>

**Imports:**

- `threading`: For thread safety in the singleton implementation.
- `traceback`: To provide detailed exception information.
- `logging`: The core Python logging module.
- `typing`: For type hints (Optional).
- `colorama`: For text colorization in the console output.
- `datetime`: To include timestamp in log files.
- `json`: For JSON formatting.
- `inspect`: To get the file, function, and line number where the log was called.


**Classes:**

- **`SingletonMeta`:** This metaclass implements the Singleton pattern, ensuring only one instance of the `Logger` class is created.  The `_instances` and `_lock` attributes maintain this uniqueness.

- **`JsonFormatter`:** This class extends `logging.Formatter` to provide a custom formatter for logging in JSON format.  It's tailored to format the log records into a JSON-serializable structure.

- **`Logger`:** This is the main logger class.
    - It uses `SingletonMeta` for its single-instance behavior.
    - It stores references to various loggers (`logger_console`, `logger_file_info`, etc.). These are initialized, with different log levels and output destinations.
    - `_configure_logger` creates and configures a specific logger with a log level and file destination.
    - `initialize_loggers` sets up all the log handlers, including the console handler, for the loggers to function correctly.
    - Methods like `info`, `success`, `warning`, etc., all delegate to `log`, enabling consistent handling of message formatting and output.


**Functions:**

- **`__init__`:** Initializes the `Logger` instance, but is overridden in the singleton pattern to avoid double creation.
- **`_configure_logger`:**  Configures and returns a `logging.Logger` object.  Takes the logger name, path, level, formatter, and optional file mode to control the log output.
- **`initialize_loggers`:** Sets up all the logging handlers and loggers. It's crucial for initiating the logging system with specified log paths and log levels.
- **`_format_message`:** Formats the message, potentially adding colors using `colorama` and handling exception information.
- **`_ex_full_info`:** Retrieves detailed exception information, including the file, function, and line number where the log method was called. This is extremely valuable for debugging and tracing errors.
- **`log`:** The core logging method that logs messages with specified levels and options.

**Variables:**

- `MODE`: A string representing the current mode (e.g., 'dev', 'prod').
- `self.logger_console`, `self.logger_file_info`, etc.: `logging.Logger` objects for specific logging destinations.
- `self._initialized`: A flag to prevent redundant logger initialization.

**Possible Errors/Improvements:**

- **Error Handling:** The `_ex_full_info` method has an `...` placeholder. Consider adding more robust error handling for exception cases.
- **File Permissions:**  Ensure the user has the necessary permissions to write to the specified log file paths (e.g., 'info.log', 'debug.log').
- **Log Rotation:** For production environments, the logger should handle log rotation, preventing log files from becoming excessively large.  The `logging` module has features for this.
- **Log Levels:** Consider adding logging levels for other events, like `WARNING` for data validation issues, etc.
- **Documentation:** Improve docstrings for better clarity, especially in `_ex_full_info` and similar functions.
- **`colors` Parameter:** The `colors` parameter in `info`, `success`, etc., is unused and could be removed, simplified, or documented for future use.

**Relationships with Other Parts of the Project:**

This `logger` module is a critical component for any application. It provides a standardized way to record various events, errors, and information throughout the code execution.   It's crucial for debugging, monitoring, and understanding the application's behavior. Other parts of the project would likely interact with the logger to record events, making it a fundamental part of the application's infrastructure.