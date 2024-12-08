# src.logger Module

## Overview

This module provides a singleton logging utility with various logging levels and formats, including console, file, and JSON logging. It utilizes the Singleton design pattern to ensure a single instance of the logger is used throughout the application. The logger supports different log levels and output formats, and it can colorize console messages based on log severity.


## Classes

### `SingletonMeta`

**Description**: Metaclass for the Singleton pattern implementation.  It ensures that only one instance of a class can be created.

**Methods** (Note:  `__call__` is a special method, not explicitly declared):
- `__call__`: Creates and returns the single instance of the class if it doesn't exist yet. It uses a lock (`_lock`) to ensure thread safety during instantiation.


### `JsonFormatter`

**Description**: Custom formatter for logging in JSON format.  This formatter overrides the default logging formatter to produce log entries in JSON format.

**Methods**

- `format(record: logging.LogRecord) -> str`: Formats the log record as JSON.

**Parameters**:
- `record` (logging.LogRecord): The log record to be formatted.

**Returns**:
- `str`: The formatted log record in JSON format.


### `Logger`

**Description**: Singleton logger class with methods for console, file, and JSON logging. Implements the Singleton pattern.

**Methods**

- `__init__(self)`: Initializes the Logger instance, setting instance variables to `None` and `_initialized` to `False`.
- `_configure_logger(self, name: str, log_path: str, level: Optional[int] = logging.DEBUG, formatter: Optional[logging.Formatter] = None, mode: Optional[str] = 'a') -> logging.Logger`: Configures and returns a logger with the specified parameters.
- `initialize_loggers(self, info_log_path: Optional[str] = '', debug_log_path: Optional[str] = '', errors_log_path: Optional[str] = '', json_log_path: Optional[str] = '')`: Initializes loggers for console, info, debug, error, and JSON logging.  Crucially initializes loggers only if they haven't already been initialized.
- `_format_message(self, message, ex=None, color=None)`: Returns formatted message with optional color and exception information.
- `_ex_full_info(self, ex)`: Provides detailed exception information, including the file, function, and line number where the log was called.  This function needs to be carefully reviewed as it currently contains `...` which indicates incomplete code.
- `log(self, level, message, ex=None, exc_info=False, color=None)`: General method to log messages at a specified level with optional color and exception information.  Handles console and file loggers.
- `info(self, message, ex=None, exc_info=False, colors: Optional[tuple] = None)`: Logs an info message.
- `success(self, message, ex=None, exc_info=False, colors: Optional[tuple] = None)`: Logs a success message.
- `warning(self, message, ex=None, exc_info=False, colors: Optional[tuple] = None)`: Logs a warning message.
- `debug(self, message, ex=None, exc_info=True, colors: Optional[tuple] = None)`: Logs a debug message.
- `error(self, message, ex=None, exc_info=True, colors: Optional[tuple] = None)`: Logs an error message.
- `critical(self, message, ex=None, exc_info=True, colors: Optional[tuple] = None)`: Logs a critical message.



## Functions

### `__init__`

**Description**: Initializes the Logger instance.


### `_configure_logger`

**Description**: Configures and returns a logger with the specified parameters.

**Parameters**:
- `name` (str): Name of the logger.
- `log_path` (str): Path to the log file.
- `level` (Optional[int], optional): Logging level. Defaults to `logging.DEBUG`.
- `formatter` (Optional[logging.Formatter], optional): Custom formatter. Defaults to `None`.
- `mode` (Optional[str], optional): File mode. Defaults to `'a'`.

**Returns**:
- `logging.Logger`: Configured logger instance.


### `initialize_loggers`

**Description**: Initializes loggers for console, info, debug, error, and JSON logging.

**Parameters**:
- `info_log_path` (Optional[str], optional): Path to the info log file. Defaults to `''`.
- `debug_log_path` (Optional[str], optional): Path to the debug log file. Defaults to `''`.
- `errors_log_path` (Optional[str], optional): Path to the errors log file. Defaults to `''`.
- `json_log_path` (Optional[str], optional): Path to the JSON log file. Defaults to `''`.


### `_format_message`

**Description**: Formats a message with optional color and exception information.

**Parameters**:
 - `message`: The message to format.
 - `ex`: Optional exception information.
 - `color`: Optional color to apply to the message.

**Returns**:
- `str`: The formatted message.


### `_ex_full_info`

**Description**: Returns full exception information, including the file, function, and line number where the log was called.

**Parameters**:
 - `ex`: The exception object.

**Returns**:
 - `str`: The formatted exception information with file, function, and line details.


### `log`

**Description**: General method to log messages at specified level with optional color and exception information.

**Parameters**:
 - `level`: Logging level (e.g., `logging.INFO`).
 - `message`: The message to log.
 - `ex`: Optional exception information.
 - `exc_info`: Whether to include exception information.
 - `color`: Optional color to apply to the message.

**Raises**:
- No explicit exception handling is documented.


### `info`, `success`, `warning`, `debug`, `error`, `critical`
These methods are wrappers around the `log` method, setting the logging level and sometimes color for specific message types.  They follow the same parameter structure and exception handling as `log`.


## Example Usage (from docstring):

```python
logger: Logger = Logger()
logger.initialize_loggers(info_log_path='info.log', debug_log_path='debug.log', errors_log_path='errors.log', json_log_path='log.json')

logger.info('This is an info message')
logger.success('This is a success message')
logger.warning('This is a warning message', None, True)
logger.debug('This is a debug message', None, exc_info=True)
logger.error('This is an error message', ex)
logger.critical('This is a critical message', ex)
```
```