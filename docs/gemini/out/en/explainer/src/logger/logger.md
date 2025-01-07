# Logger Module Analysis

## <input code>

```python
# -*- coding: utf-8 -*-\n\n#! venv/bin/python/python3.12\n\n"""\n.. module: src.logger \n\t:platform: Windows, Unix\n\t:synopsis: Logger Module\n"""\nMODE = \'dev\'\n\n"""This module provides a singleton logging utility with various logging levels and formats, including console, file, and JSON logging. It utilizes the Singleton design pattern to ensure a single instance of the logger is used throughout the application. The logger supports different log levels and output formats, and it can colorize console messages based on log severity.\n\nClasses:\n- SingletonMeta: Metaclass for Singleton pattern implementation.\n- JsonFormatter: Custom formatter for logging in JSON format.\n- Logger: Singleton logger class with methods for logging at different levels.\n\nClasses:\n    SingletonMeta\n    ----------\n    Metaclass for Singleton pattern implementation.\n    \n    JsonFormatter\n    -------------\n    Custom formatter for logging in JSON format.\n    \n    Logger\n    ------\n    Singleton logger class with methods for console, file, and JSON logging.\n\nFunctions:\n- __init__: Initializes the Logger instance.\n- _configure_logger: Configures and returns a logger with the specified parameters.\n- initialize_loggers: Initializes loggers for console, file, and JSON output.\n- _format_message: Formats a message with optional color and exception information.\n- _ex_full_info: Provides detailed exception information, including the file, function, and line number where the log was called.\n- log: Logs messages at a specified level with optional color and exception information.\n- info: Logs an info message.\n- success: Logs a success message.\n- warning: Logs a warning message.\n- debug: Logs a debug message.\n- error: Logs an error message.\n- critical: Logs a critical message.\n- info_red: Logs an info message in red.\n- info_black: Logs an info message in black with a white background.\n\nExamples:\n    # Initialize the logger\n    logger: Logger = Logger()\n    logger.initialize_loggers(info_log_path=\'info.log\', debug_log_path=\'debug.log\', errors_log_path=\'errors.log\', json_log_path=\'log.json\')\n\n    # Log messages at different levels\n    logger.info(\'This is an info message\')\n    logger.success(\'This is a success message\')\n    logger.warning(\'This is a warning message\',None,True)\n    logger.debug(\'This is a debug message\',None,exc_info=True)\n    logger.error(\'This is an error message\',ex)\n    logger.critical(\'This is a critical message\',ex)\n"""\n\n# -*- coding: utf-8 -*-\n\n#! venv/bin/python/python3.12\n\n"""\n.. module: src.logger\n    :platform: Windows, Unix\n    :synopsis: Logger Module\n"""\n\nimport threading\nimport traceback\nimport logging\nfrom typing import Optional\nimport colorama\nimport datetime\nimport json\nimport inspect\n\n# ... (rest of the code)
```

## <algorithm>

The code implements a singleton logger that supports console, file, and JSON logging with different levels and colorization options.

**1. Initialization:**

   - The `Logger` class utilizes the `SingletonMeta` metaclass to ensure only one instance exists.
   - `initialize_loggers` method is called to configure loggers for console, info, debug, error, and JSON files.


**2. Logger Configuration:**

   - `_configure_logger` method creates and configures a logger instance with a specified name, log path, level, formatter (optional), and mode.
   - It sets up a `FileHandler` to write logs to the specified file and a `Formatter` to format the log entries.
   - Returns the configured `logging.Logger` object.


**3. Log Formatting:**

   - `_format_message` formats the log message, optionally including color codes and exception information using the `colorama` library.
   - `_ex_full_info` provides detailed exception information, including the file, function, and line number where the log was called.


**4. Logging Operations:**

   - `log` method is a generic function for different log levels. It formats the message, optionally adds exception details, and logs to the console and file handlers.
   - Level-specific logging methods (e.g., `info`, `warning`, `error`) call the `log` method with the appropriate logging level and colorization.
   - `log` method checks if the `logger` is initialized; if not, it initializes the logger first.


**Data Flow Example:**

```
User calls logger.info("Message")
|
V
Logger.info -> Logger.log(logging.INFO, "Message")
|
V
Logger.log -> _format_message("Message") // Formats message (optionally with color).
|
V
Logger.log -> _ex_full_info(ex) // Adds detailed exception info (if available).
|
V
Logger.log -> logging.getLogger(logger_name).log(logging.INFO, formatted_message) // Logs the message to console and file handlers (if configured)
```


## <mermaid>

```mermaid
graph LR
    subgraph Initialization
        Logger --> initialize_loggers
    end
    subgraph Logger Configuration
        initialize_loggers --> _configure_logger
        _configure_logger --> logger
    end
    subgraph Log Formatting
        log --> _format_message
        log --> _ex_full_info
    end
    subgraph Logging Operations
        log --> console_handler
        log --> file_handler_info{info_log}
        log --> file_handler_debug{debug_log}
        log --> file_handler_errors{error_log}
        log --> file_handler_json{json_log}
    end

    initialize_loggers --> _initialized(True)
    _initialized --|--> log
    log -- _format_message
    log -- _ex_full_info

    subgraph Level Specific Logging
        info --> log
        success --> log
        warning --> log
        debug --> log
        error --> log
        critical --> log
    end

    console_handler --> console{Console Output}
    file_handler_info --> info_log{info Log File}
    file_handler_debug --> debug_log{debug Log File}
    file_handler_errors --> error_log{error Log File}
    file_handler_json --> json_log{JSON Log File}
```


**Dependencies Analysis:**

- `threading`: Used for thread safety in the Singleton implementation.
- `traceback`:  For handling exceptions and generating traceback information, which is used for detailed exception logging.
- `logging`: The core Python logging module for handling log messages, levels, handlers, and formatters.
- `typing`:  For type hinting, enabling better code readability and maintainability.
- `colorama`: For console output colorization.
- `datetime`: For formatting timestamps in log messages.
- `json`: For handling JSON log format.
- `inspect`: For getting the stack trace and getting source file info.


## <explanation>

**Imports:**

- `threading`: Essential for ensuring thread safety in the `SingletonMeta` implementation, preventing race conditions when creating multiple instances.
- `traceback`: Used to gather detailed information about exceptions for more informative log entries.
- `logging`: The core Python logging module, providing the fundamental logging functionality.
- `typing`: Used for type hinting, improves code clarity and maintainability.
- `colorama`: Needed to add colors to the console output; critical for visually distinguishing different log levels (e.g., error messages in red).
- `datetime`: For formatting timestamps in log messages.
- `json`: For generating and parsing JSON log records.
- `inspect`: Enables retrieval of the current source code location where a log is called.

**Classes:**

- `SingletonMeta`: Implements the Singleton pattern using a metaclass. This ensures that only one instance of the `Logger` class can exist.
- `JsonFormatter`: A custom formatter for log messages in JSON format. This extends the `logging.Formatter` class to tailor the JSON output of log records.
- `Logger`: The singleton logger class. It's designed to handle multiple logging levels (console, info file, debug file, errors file, JSON file) and formats. It manages the creation, configuration, and usage of these loggers via its methods.


**Functions:**

- `__init__`: Initializes the internal logger attributes and sets the `_initialized` flag to False. This function is called when an instance of `Logger` is created.
- `_configure_logger`: This function takes various parameters (name, log path, level, formatter) to configure and return a new logger instance with the provided settings.
- `initialize_loggers`: This function sets up the loggers for console, file (info, debug, error), and JSON output. This method handles the creation and configuration of all handlers based on the provided log paths. This method calls `_configure_logger` to manage the setup.
- `_format_message`: Formats a log message, including colorization (optional), and exception information. This is called from the `log` method to format the log.
- `_ex_full_info`: Returns detailed exception information including file, function, and line number.
- `log`: The core logging method, accepting various arguments for levels, messages, and exceptions. It handles the actual logging to the configured handlers.
- `info`, `success`, `warning`, `debug`, `error`, `critical`: These methods act as helper functions for logging at specific levels, taking messages and optional colorization as arguments.

**Variables:**

- `MODE`: A variable set to 'dev'. It might be used for conditional logic elsewhere in the code.  
- `logger_console`, `logger_file_info`, etc.: These are attributes of the Logger class, holding references to the configured logging handlers for different types of logs.


**Potential Errors/Improvements:**

- **Error Handling:** The `_ex_full_info` method contains an ellipsis (`...`) placeholder.  It should handle potential exceptions during traceback retrieval and provide more robust error handling.
- **Resource Management:** While using a singleton is fine for this use case, there should be a mechanism for cleaning up log files or closing handlers when the application shuts down to release resources.
- **Exception Formatting:**  The JsonFormatter currently handles `record.exc_info` in a somewhat generic manner. Consider better formatting and handling of different exception types (e.g., `TypeError`, `ValueError`).  Consider handling exceptions that might be thrown during JSON serialization.


**Chain of Relationships:**

This logger module likely interacts with other parts of the project to log events. It's designed to be called from other modules in the application, passing log data.  The method signatures (`info`, `warning`, etc.) suggest calling this module from other parts of the application.  Logging is a cross-cutting concern, so it would be called by many other parts of the program.