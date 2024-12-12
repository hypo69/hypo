# <input code>

```python
## \file hypotez/src/logger/logger.py
# -*- coding: utf-8 -*-\
#! venv/Scripts/python.exe # <- venv win
## ~~~~~~~~~~~~~\
""" module: src.logger """

"""
Logger Module

This module provides a singleton logging utility with various logging levels and formats, including console, file, and JSON logging. It utilizes the Singleton design pattern to ensure a single instance of the logger is used throughout the application. The logger supports different log levels and output formats, and it can colorize console messages based on log severity.

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

import header
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
        """ Format the log record as JSON."""
        log_entry = {
            "asctime": self.formatTime(record, self.datefmt),
            "name": record.name,
            "levelname": record.levelname,
            "message": record.getMessage(),
            "exc_info": self.formatException(record.exc_info)
            if record.exc_info
            else None,
        }
        return json.dumps(log_entry, ensure_ascii=False)


class Logger(metaclass=SingletonMeta):
    """ Logger class implementing Singleton pattern with console, file, and JSON logging."""
    # ... (rest of the code)
```

# <algorithm>

The algorithm can be visualized as follows:

1. **Initialization (Logger.__init__):**
   - Initializes logger attributes (console, file, JSON).
   - Calls `initialize_loggers()` to configure loggers.
   - Sets `_initialized` flag to `False`.

2. **Logger Configuration (initialize_loggers):**
   - Checks if `_initialized` flag is `True`. If yes, it returns without doing anything (avoid reinitializing).
   - Creates timestamp for logger names.
   - Configures the console logger (`logger_console`) with a simple format.
   - Optionally configures file loggers for info, debug, error, and JSON. Each logger is configured with its own file handler and formatter, using `_configure_logger`.

3. **Log Entry (log):**
   - Formats the message with optional color and exception details using `_format_message`.
   - If `exc_info` is True, adds exception stack trace using `_ex_full_info`.
   - Logs the message to the console logger (`logger_console`).
   - Logs the message to the JSON logger (`logger_file_json`).
   - Logs the message to specific file loggers based on the `level`.

Example Data Flow:

```
User calls logger.info("My message") -> Logger.info() -> Logger.log(level=INFO, message="My message") -> Logger.log() -> _format_message("My message", None, Fore.GREEN) -> logs to console and (potentially) info file.
```


# <mermaid>

```mermaid
graph TD
    subgraph Initialization
        A[User calls Logger()] --> B{Logger.__init__};
        B --> C[initialize_loggers];
        C -- success --> D[Logger Initialized];
        C -- failure --> E[Error];
    end
    subgraph Logging
        D --> F[log(level, message, ...)];
        F --> G{_format_message};
        G -- success --> H[Logs to console];
        G -- success --> I[Logs to file(s) based on level];
        H -- success --> J[Console output];
        I -- success --> K[File output];
    end
    subgraph Logger Dependencies
        F --> L[logging];
        F --> M[colorama];
        F --> N[datetime];
        F --> O[json];
        F --> P[inspect];
        F --> Q[header];
    end
    
    subgraph File Handlers
        C --> R{_configure_logger(name, path, level)};
        R --> S[Creates FileHandler];
        S --> T[Sets Formatter];
        T --> U[Adds Handler to Logger];
    end

```

# <explanation>

**1. Imports:**

- `header`: This is likely a custom import from a different module within the same project.  Its purpose is unclear from the given code snippet.
- `threading`: Used to create a thread lock to implement the singleton pattern, ensuring only one instance of the `Logger` class exists.
- `traceback`: Used for handling and displaying exception details in the log messages.
- `logging`: The core Python logging module.  Provides the foundation for logging functionality.
- `colorama`: Provides colored output in the console.  The logger utilizes it for color-coding log messages according to their severity.
- `datetime`: Used for timestamping log entries.
- `json`: Used for formatting log entries in JSON.
- `inspect`:  Used for obtaining the caller's file name, function name, and line number when an exception occurs.

**2. Classes:**

- `SingletonMeta`: Implements the singleton pattern using a metaclass.  This ensures only one instance of the `Logger` class is ever created. The `_instances` dictionary and the `_lock` are critical for achieving thread safety.
- `JsonFormatter`: A custom formatter for the `logging` module. It formats log records into JSON format, crucial for structured logging.
- `Logger`:  The main singleton class responsible for managing and sending log messages to various destinations (console, file, JSON). It maintains separate loggers for different log levels and destinations.  The `_initialized` flag is important for preventing reinitialization.  The use of logging.Logger and its methods is a standard approach for managing log messages.

**3. Functions:**

- `__init__`: Initializes the Logger instance, sets attributes for the loggers, and initializes them.
- `_configure_logger`: Creates and configures a logger for a specific file destination. It takes the name of the logger, file path, logging level, and a formatter (optional).
- `initialize_loggers`: Initializes all loggers for the console, info, debug, error, and JSON output with their respective paths and levels.  It sets the `_initialized` flag to prevent re-initialization, which is a critical aspect of preventing errors.
- `_format_message`: Formats log messages with optional color and exception information.
- `_ex_full_info`: Extracts and returns detailed exception information, including file name, function name, and line number.
- `log`: The general logging method. It handles logging to console, files, and JSON based on specified parameters.
- `info`, `success`, `warning`, `debug`, `error`, `critical`:  These functions provide convenience for logging messages at specific levels with optional color and exception information.  Colorization improves readability.
- `info_red`, `info_black`: Provide logging functions with specific color formats.

**4. Variables:**

- `logger_console`, `logger_file_info`, etc.: These variables hold references to the individual loggers.  Their types are `logging.Logger`.
- `_initialized`: A boolean variable to manage the initialization state of the logger.

**5. Potential Errors/Improvements:**

- **Error Handling:** While the code includes error handling in `initialize_loggers` to prevent re-initialization, there's no explicit handling of exceptions during file operations.  Consider adding `try...except` blocks to handle potential `IOError`s or other file-related issues.
- **Flexibility:**  The `initialize_loggers` function could be improved to accept a dictionary of log paths and levels for easier configuration.
- **Logging Levels:** The code uses `logging.DEBUG`, `logging.INFO`, etc.  These are good, but having a custom enumeration for logging levels could enhance readability.
- **Reusability:** The code could potentially benefit from a more generalized configuration mechanism to avoid hard-coding file paths and logging levels. For instance, using a config file.
- **_ex_full_info:**  It might be more robust to use the `traceback` module to generate the exception information (instead of relying on `inspect`) for better exception handling.

**Relationships to other parts of the project (header):**

The `header` import suggests a dependency on another module (`hypotez/src`) likely containing other components of the project. The exact nature of this module's purpose, and its relationship to this `logger` module, isn't discernible from the provided code, but it's an important context to consider for full project understanding. This `header` module is likely to contain the base configuration of the application.