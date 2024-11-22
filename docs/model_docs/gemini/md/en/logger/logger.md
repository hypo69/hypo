```markdown
# src.logger

## Overview

This module provides a singleton logging utility with various logging levels and formats, including console, file, and JSON logging. It utilizes the Singleton design pattern to ensure a single instance of the logger is used throughout the application. The logger supports different log levels and output formats, and it can colorize console messages based on log severity.


## Classes

### `SingletonMeta`

**Description**: Metaclass for Singleton pattern implementation.

**Methods**:
- `__call__`:  Initializes and returns the singleton instance of the class, ensuring only one instance exists.

### `JsonFormatter`

**Description**: Custom formatter for logging in JSON format.

**Methods**:
- `format`: Formats a log record as JSON.


### `Logger`

**Description**: Singleton logger class with methods for console, file, and JSON logging.  This class manages multiple logging targets.


**Methods**:

#### `__init__`

**Description**: Initializes the `Logger` instance.

#### `_configure_logger`

**Description**: Configures and returns a logger with the specified parameters.

**Parameters**:
- `name` (str): Name of the logger.
- `log_path` (str): Path to the log file.
- `level` (logging.Level): Log level (defaults to `logging.DEBUG`).
- `formatter` (logging.Formatter, optional): Formatter for the log messages. Defaults to a default formatter.
- `mode` (str, optional): File mode for opening the log file. Defaults to "a" (append).

**Returns**:
- `logging.Logger`: The configured logger.


#### `initialize_loggers`

**Description**: Initializes loggers for console, file, and JSON output.

**Parameters**:
- `info_log_path` (str, optional): Path to the info log file. Defaults to empty string.
- `debug_log_path` (str, optional): Path to the debug log file. Defaults to empty string.
- `errors_log_path` (str, optional): Path to the errors log file. Defaults to empty string.
- `json_log_path` (str, optional): Path to the JSON log file. Defaults to empty string.

#### `_format_message`

**Description**: Formats a message with optional color and exception information.

**Parameters**:
- `message` (str): The log message.
- `ex` (Optional[Exception], optional):  Exception information (if any). Defaults to None.
- `color` (Optional[str | tuple], optional): Color codes for the message display in console.


**Returns**:
- `str`: Formatted message.

#### `_ex_full_info`

**Description**: Provides detailed exception information, including the file, function, and line number where the log was called.

**Parameters**:
- `ex` (Optional[Exception], optional): Exception instance or None.

**Returns**:
- `str`: A string containing the exception and file/function/line information.


#### `log`

**Description**: Logs messages at a specified level with optional color and exception information.

**Parameters**:
- `level` (int): The logging level (e.g., `logging.INFO`, `logging.DEBUG`).
- `message` (str): The log message.
- `ex` (Optional[Exception], optional): Exception instance or None. Defaults to `None`.
- `exc_info` (bool, optional):  If `True`, includes stack trace information. Defaults to `False`.
- `color` (Optional[str | tuple], optional): Color codes for the message display in console.

**Raises**:
- `Exception`: Generic exception if the logger initialization fails.



#### `info`, `success`, `warning`, `debug`, `error`, `critical`, `info_red`, `info_black`

**Description**: Logging methods for specific log levels (INFO, SUCCESS, WARNING, DEBUG, ERROR, CRITICAL, INFO_RED, INFO_BLACK) with optional color parameters, which are simply wrappers around the `log` method.


## Functions

### `__init__`

- Initializes the Logger instance.

## Usage Example

```python
logger = Logger()
logger.initialize_loggers(info_log_path='info.log', debug_log_path='debug.log')
logger.info('This is an info message')
logger.error("An error occurred", Exception("error message"))
```
```
```
```
```
```

```
```
