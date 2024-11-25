# src.logger Module Documentation

## Overview

This module provides a singleton logging utility with various logging levels and formats, including console, file, and JSON logging. It utilizes the Singleton design pattern to ensure a single instance of the logger is used throughout the application. The logger supports different log levels and output formats, and it can colorize console messages based on log severity.

## Classes

### `SingletonMeta`

**Description**: Metaclass for Singleton pattern implementation.  Ensures only one instance of the `Logger` class can exist.

### `JsonFormatter`

**Description**: Custom formatter for logging in JSON format. Overrides the default formatter to output log records in JSON.


**Methods**

#### `format`

**Description**: Formats the log record as JSON.

**Parameters**

- `record` (logging.LogRecord): The log record to be formatted.

**Returns**

- `str`: Formatted log record in JSON format.


### `Logger`

**Description**: Singleton logger class with methods for console, file, and JSON logging.  Provides methods for logging at various levels and configurations, including multiple log files for different severity levels.  Uses the Singleton pattern for thread safety and preventing multiple logger instances.

**Methods**

#### `__init__`

**Description**: Initializes the `Logger` instance.  Sets initial values for logger attributes to `None` and `_initialized` to `False`.  This is crucial for proper initialization and ensuring loggers are only set up once.


#### `_configure_logger`

**Description**: Configures and returns a logger with the specified parameters.

**Parameters**

- `name` (str): Name of the logger.
- `log_path` (str): Path to the log file.
- `level` (Optional[int], optional): Logging level. Defaults to `logging.DEBUG`.
- `formatter` (Optional[logging.Formatter], optional): Custom formatter. Defaults to `None`.
- `mode` (Optional[str], optional): File mode. Defaults to `'a'`.

**Returns**

- `logging.Logger`: Configured logger instance.

#### `initialize_loggers`

**Description**: Initializes loggers for console, file (info, debug, error), and JSON output.  Creates and configures logging handlers for different log levels (info, debug, error, JSON) and outputs (console, file).  Critically, initializes loggers only once to avoid potential issues.

**Parameters**

- `info_log_path` (Optional[str]): Path to the info log file. Defaults to `''`.
- `debug_log_path` (Optional[str]): Path to the debug log file. Defaults to `''`.
- `errors_log_path` (Optional[str]): Path to the errors log file. Defaults to `''`.
- `json_log_path` (Optional[str]): Path to the JSON log file. Defaults to `''`.


#### `_format_message`

**Description**: Returns formatted message with optional color and exception information.


#### `_ex_full_info`

**Description**: Provides detailed exception information, including the file, function, and line number where the log was called. Extracts stack information to provide a useful traceback in the logs, aiding debugging.

#### `log`

**Description**: Logs messages at a specified level with optional color and exception information.

**Parameters**

- `level`: Logging level (e.g., logging.INFO).
- `message`: The message to log.
- `ex` (Optional[Exception], optional): Exception object if available, for error handling, helping to find source of an exception in the logs. Defaults to `None`.
- `exc_info` (bool, optional): If True, include the traceback of the exception if `ex` is provided. Defaults to `False`.
- `color` (Optional[tuple], optional):  Color code tuple for console output. Defaults to `None`.

#### `info`
#### `success`
#### `warning`
#### `debug`
#### `error`
#### `critical`

**Description**: Methods for logging messages at specific levels (INFO, SUCCESS, WARNING, DEBUG, ERROR, CRITICAL) with optional exception and color information.  These methods all delegate to the `log` method for consistency and central error handling.  Using different colors makes messages easier to distinguish in the logs.


## Functions

(No functions are present outside of class methods in this module)


## Examples

```python
# Initialize the logger
logger: Logger = Logger()
logger.initialize_loggers(info_log_path='info.log', debug_log_path='debug.log', errors_log_path='errors.log', json_log_path='log.json')

# Log messages at different levels
logger.info('This is an info message')
logger.success('This is a success message')
logger.warning('This is a warning message')
logger.debug('This is a debug message')
logger.error('This is an error message', ex=Exception("Example error"))
logger.critical('This is a critical message', ex=Exception("Example critical error"))
```
```
```