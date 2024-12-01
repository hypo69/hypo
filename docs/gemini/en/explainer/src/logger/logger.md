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

The code implements a logger with multiple output targets (console, files, and JSON). The key steps are:

1. **Initialization (Singleton):** The `Logger` class uses the `SingletonMeta` metaclass to ensure only one instance exists.  
2. **Logger Configuration:** The `_configure_logger` method creates and configures a logger instance, specifying the log level, formatter, and file path.
3. **Logger Initialization:** The `initialize_loggers` method creates loggers for console output, info, debug, error, and JSON log files, and configures them.  
4. **Logging Levels:**  `log`, `info`, `success`, `warning`, `debug`, `error`, and `critical` methods handle logging at different severity levels.  
5. **Formatting:** `_format_message` method handles message formatting, potentially adding color and exception details. `_ex_full_info` adds detailed traceback information.
6. **Output:** The `log` method writes to the console and, if configured, to the appropriate file-based log, including JSON.

**Example Data Flow:**

```
[User Call] -> log(INFO, "message") -> _format_message("message") -> _ex_full_info(None) ->  console_logger.log(INFO, formatted_message, exc_info=False)
```


# <mermaid>

```mermaid
graph LR
    subgraph Logger Class
        A[Logger()] --> B{initialize_loggers(paths)};
        B --> C[console_logger];
        B --> D{info_logger};
        B --> E{debug_logger};
        B --> F{error_logger};
        B --> G[json_logger];
    end
    C --> H[console output];
    D --> I[info log file];
    E --> J[debug log file];
    F --> K[error log file];
    G --> L[json log file];
    subgraph Dependencies
        B --> M[threading];
        B --> N[logging];
        B --> O[colorama];
        B --> P[datetime];
        B --> Q[json];
        B --> R[inspect];
    end
    style B fill:#f9f,stroke:#333,stroke-width:2px
    classDef logger fill:#ccf,stroke:#333,stroke-width:2px
```

**Dependencies Analysis:**

- `threading`: Used for thread safety in the singleton implementation.
- `logging`: Core Python logging library for handling log messages and output.
- `colorama`: Used to colorize console output.
- `datetime`: Used for timestamping log entries.
- `json`: Used for formatting logs in JSON format.
- `inspect`: Used to get stack trace information.


# <explanation>

**Imports:**

- `threading`: Ensures thread safety when creating the singleton `Logger` instance. Crucial for multi-threaded applications to prevent race conditions.
- `traceback`: Enables capturing detailed exception information.  Used for obtaining the source location of exception events.
- `logging`: Provides the core logging functionality, including logging levels, handlers, and formatters.
- `typing`: Used for type hinting, improves code readability and maintainability.
- `colorama`: Used to add color to console output.
- `datetime`: Used for timestamping log entries.
- `json`: Used for serializing logs to JSON format.
- `inspect`: Used to extract source code location data in log entries.

**Classes:**

- `SingletonMeta`: A metaclass that implements the Singleton design pattern, ensuring only one instance of the `Logger` class is created.  Crucial for managing the logger globally.
- `JsonFormatter`: A custom formatter for logging in JSON format. Overrides the `format` method from `logging.Formatter` to handle JSON serialization of log records.
- `Logger`: The main logging class. It's a singleton, meaning only one instance of this class can be created.  It uses various logging handlers (console, files, JSON) and defines methods for different log levels (e.g., `info`, `error`). It manages the logging process and has methods to handle console coloring.


**Functions:**

- `__init__`: Initializes the `Logger` instance by setting logger attributes to `None` and `_initialized` to `False`.  Important for creating logger objects.
- `_configure_logger`: Configures a logger with a given name, path, level, formatter, and mode. It creates a file handler, sets the formatter, and adds it to the logger. Crucial for creating and configuring individual log handlers.
- `initialize_loggers`: Initializes the loggers for console, info, debug, error, and JSON output. This method handles setting up the logger instance with different outputs based on the paths provided. Crucial for setting up the logger instance to handle different outputs.
- `_format_message`, `_ex_full_info`: These methods format log messages, including optional colorization and detailed exception information (file, function, and line number).  These are used to format and include extra information in the log messages.
- `log`: The general-purpose logging method. It handles formatting the log message, writing to console and files, and includes exception information if provided. This method acts as a central point for handling logging operations.
- `info`, `success`, `warning`, `debug`, `error`, `critical`: These methods provide convenience wrappers for logging at different levels, automatically setting the logging level and optionally applying color.

**Variables:**

- `MODE`:  A global variable that is likely used for configuration purposes (e.g., determining if logging is set to `dev` or `prod`).
- Instance variables (`logger_console`, etc.): Contain the logging instances for different targets (console, files, JSON). These variables store the logger objects created by the `_configure_logger` method to handle log outputs.


**Potential Errors/Improvements:**

- **Error Handling:** The `_ex_full_info` function seems to have incomplete error handling. The "..." indicates that exception information might not be properly handled in the function. Robust error handling should be implemented to ensure that exceptions are caught and handled gracefully.


**Relationships with Other Project Parts:**

This logger module is likely a part of a larger application and could be used by other modules to log events and messages. This code assumes that any necessary exception types or formatting information are imported from other relevant Python packages within the application project.  The logger module would interact with the business logic of the rest of the project to log events as they happen.