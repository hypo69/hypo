# src.logger Module

## Overview

This module provides a flexible logging system that supports console, file, and JSON logging. It utilizes the Singleton design pattern to ensure only a single instance of the logger is used across the application.  The logger supports various log levels (e.g., `INFO`, `ERROR`, `DEBUG`) and includes colorized output for console logs. You can also customize the log output formats and control logging to different files.

## Table of Contents

* [Classes](#classes)
* [Functions](#functions)
* [Parameters for the Logger](#parameters-for-the-logger)
* [File Logging Configuration](#file-logging-configuration)
* [Example Usage](#example-usage)
* [Conclusion](#conclusion)


## Classes

### `SingletonMeta`

**Description**: Metaclass that implements the Singleton design pattern for the logger.

### `JsonFormatter`

**Description**: A custom formatter that outputs logs in JSON format.

### `Logger`

**Description**: The main logger class that supports console, file, and JSON logging.


## Functions

### `__init__`

**Description**: Initializes the `Logger` instance with placeholders for different logger types (console, file, and JSON).

### `_configure_logger`

**Description**: Configures and returns a logger instance.

```python
def _configure_logger(name: str, log_path: str, level: Optional[int] = logging.DEBUG, formatter: Optional[logging.Formatter] = None, mode: Optional[str] = 'a') -> logging.Logger:
    """
    Args:
        name (str): Name of the logger.
        log_path (str): Path to the log file.
        level (Optional[int], optional): Logging level, e.g., `logging.DEBUG`. Defaults to `logging.DEBUG`.
        formatter (Optional[logging.Formatter], optional): Custom formatter (optional).
        mode (Optional[str], optional): File mode, e.g., 'a' for append (default).

    Returns:
        logging.Logger: Configured logging.Logger instance.
    """
```


### `initialize_loggers`

**Description**: Initializes the loggers for console and file logging (info, debug, error, and JSON).

```python
def initialize_loggers(info_log_path: Optional[str] = '', debug_log_path: Optional[str] = '', errors_log_path: Optional[str] = '', json_log_path: Optional[str] = '') -> None:
    """
    Args:
        info_log_path: Path for info log file (optional).
        debug_log_path: Path for debug log file (optional).
        errors_log_path: Path for error log file (optional).
        json_log_path: Path for JSON log file (optional).
    """
```


### `log`

**Description**: Logs a message at the specified level (e.g., `INFO`, `DEBUG`, `ERROR`) with optional exception and color formatting.

```python
def log(level, message, ex=None, exc_info=False, color=None):
    """
    Args:
        level: Logging level (e.g., logging.INFO, logging.DEBUG).
        message: The log message.
        ex: Optional exception to log.
        exc_info: Whether to include exception information (default is False).
        color: Tuple with text and background colors for console output (optional).
    """
```

### `info`, `success`, `warning`, `debug`, `error`, `critical`

**Description**: These functions are wrappers for logging messages at specific levels (INFO, SUCCESS, WARNING, DEBUG, ERROR, CRITICAL).  They are functionally identical, differing only in the logging level.

```python
def info(message, ex=None, exc_info=False, colors: Optional[tuple] = None):
    """
    Logs an info message.

    Args:
      Same as log()
    """

def success(message, ex=None, exc_info=False, colors: Optional[tuple] = None):
    """
    Logs a success message.

    Args:
      Same as log()
    """

# (Similar definitions for warning, debug, error, critical, each with the same argument details as log)
```



## Parameters for the Logger

The `Logger` class accepts several optional parameters for customizing the logging behavior.

* **Level**: Controls the severity of logs that are captured. Common levels include:
    * `logging.DEBUG`: Detailed information, useful for diagnosing issues.
    * `logging.INFO`: General information, such as successful operations.
    * `logging.WARNING`: Warnings that do not necessarily require immediate action.
    * `logging.ERROR`: Error messages.
    * `logging.CRITICAL`: Critical errors that require immediate attention.

* **Formatter**: Defines how the log messages are formatted.  By default, messages are formatted as `'%(asctime)s - %(levelname)s - %(message)s'`. You can provide a custom formatter for different formats, such as JSON.

* **Color**: Colors for the log messages in the console.  The colors are specified as a tuple with two elements:
    * **Text color**: Specifies the text color (e.g., `colorama.Fore.RED`).
    * **Background color**: Specifies the background color (e.g., `colorama.Back.WHITE`).

The color can be customized for different log levels (e.g., green for info, red for errors, etc.).


## File Logging Configuration

To log messages to a file, you can specify the file paths in the configuration.

```python
config = {
    'info_log_path': 'logs/info.log',
    'debug_log_path': 'logs/debug.log',
    'errors_log_path': 'logs/errors.log',
    'json_log_path': 'logs/log.json'
}
```

The file paths provided in `config` are used to write logs to the respective files for each log level.

## Example Usage

(The example code blocks are included as is, but with added Markdown formatting.)

## Conclusion

This module provides a comprehensive and flexible logging system for Python applications. You can configure console and file logging with different formats and colors, manage logging levels, and handle exceptions gracefully. The configuration for file logging is stored in a `config` dictionary, which allows for easy customization.