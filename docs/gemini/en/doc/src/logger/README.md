# src.logger Module Documentation

## Overview

This module provides a flexible logging system for Python applications.  It supports console, file, and JSON logging, using the Singleton design pattern for a single logger instance.  Colorized output is available for console logs, and you can customize log formats and target different files.

## Table of Contents

- [Classes](#classes)
- [Functions](#functions)
- [Parameters for the Logger](#parameters-for-the-logger)
- [File Logging Configuration](#file-logging-configuration)
- [Example Usage](#example-usage)
- [Conclusion](#conclusion)


## Classes

### `SingletonMeta`

**Description**: Metaclass implementing the Singleton design pattern for the logger.  Ensures only one instance of the logger exists.


### `JsonFormatter`

**Description**: Custom formatter for JSON log output.  Formats log messages as JSON.


### `Logger`

**Description**: The main logger class, supporting console, file, and JSON logging.  It utilizes a Singleton pattern.

**Methods:**

- [`__init__(self)`](#__init__)
- [`_configure_logger(name: str, log_path: str, level: Optional[int] = logging.DEBUG, formatter: Optional[logging.Formatter] = None, mode: Optional[str] = 'a') -> logging.Logger`](#_configure_logger)
- [`initialize_loggers(info_log_path: Optional[str] = '', debug_log_path: Optional[str] = '', errors_log_path: Optional[str] = '', json_log_path: Optional[str] = '')`](#initialize_loggers)
- [`log(level, message, ex=None, exc_info=False, color=None)`](#log)
- [`info(message, ex=None, exc_info=False, colors: Optional[tuple] = None)`](#info)
- [`success(message, ex=None, exc_info=False, colors: Optional[tuple] = None)`](#success)
- [`warning(message, ex=None, exc_info=False, colors: Optional[tuple] = None)`](#warning)
- [`debug(message, ex=None, exc_info=True, colors: Optional[tuple] = None)`](#debug)
- [`error(message, ex=None, exc_info=True, colors: Optional[tuple] = None)`](#error)
- [`critical(message, ex=None, exc_info=True, colors: Optional[tuple] = None)`](#critical)


### `__init__`

**Description**: Initializes the `Logger` instance, creating placeholders for console, file, and JSON loggers.

```python
def __init__(self):
    """
    Initializes the Logger instance.
    """
    pass
```

### `_configure_logger`

**Description**: Configures and returns a logger instance.

```python
def _configure_logger(name: str, log_path: str, level: Optional[int] = logging.DEBUG, formatter: Optional[logging.Formatter] = None, mode: Optional[str] = 'a') -> logging.Logger:
    """
    Configures and returns a logger instance.

    Args:
        name (str): Name of the logger.
        log_path (str): Path to the log file.
        level (Optional[int], optional): Logging level, e.g., logging.DEBUG. Defaults to logging.DEBUG.
        formatter (Optional[logging.Formatter], optional): Custom formatter (optional). Defaults to None.
        mode (Optional[str], optional): File mode, e.g., 'a' for append. Defaults to 'a'.

    Returns:
        logging.Logger: Configured logging.Logger instance.
    """
    pass
```

### `initialize_loggers`

**Description**: Initializes loggers for console and file logging (info, debug, error, and JSON).

```python
def initialize_loggers(info_log_path: Optional[str] = '', debug_log_path: Optional[str] = '', errors_log_path: Optional[str] = '', json_log_path: Optional[str] = ''):
    """
    Initializes the loggers for console and file logging (info, debug, error, and JSON).

    Args:
        info_log_path (Optional[str], optional): Path for info log file (optional). Defaults to ''.
        debug_log_path (Optional[str], optional): Path for debug log file (optional). Defaults to ''.
        errors_log_path (Optional[str], optional): Path for error log file (optional). Defaults to ''.
        json_log_path (Optional[str], optional): Path for JSON log file (optional). Defaults to ''.
    """
    pass
```


### `log`

```python
def log(level, message, ex=None, exc_info=False, color=None):
    """
    Logs a message at the specified level with optional exception and color formatting.

    Args:
        level: Logging level (e.g., logging.INFO, logging.DEBUG).
        message: The log message.
        ex: Optional exception to log.
        exc_info: Whether to include exception information (default is False).
        color: Tuple with text and background colors for console output (optional).
    """
    pass
```

*(Other `log` methods like `info`, `success`, etc. are similarly documented using the provided format.)*


## Parameters for the Logger

* **Level**: Controls the severity of logged messages.  Common levels: `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`.

* **Formatter**: Defines the log message format.  Defaults to `'%(asctime)s - %(levelname)s - %(message)s'`.  Custom formatters, such as JSON, are supported.

* **Color**: Controls the color of log messages in the console output.  Specified as a tuple: `(text_color, background_color)`.  e.g. `(colorama.Fore.RED, colorama.Back.WHITE)`.

## File Logging Configuration

The configuration for file logging is stored in a dictionary, allowing easy customization.

```python
config = {
    'info_log_path': 'logs/info.log',
    'debug_log_path': 'logs/debug.log',
    'errors_log_path': 'logs/errors.log',
    'json_log_path': 'logs/log.json'
}
```

## Example Usage

*(The example usage sections are already included in the input.)*


## Conclusion

This module provides a flexible and configurable logging system for Python applications.  It supports various log levels, output formats (including JSON), and the ability to log to different files, offering significant control over logging behavior.