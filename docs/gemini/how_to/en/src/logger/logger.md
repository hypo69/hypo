```python
# This is a usage guide for the logger.py module.

## Logging Usage Guide for `logger.py`

This module provides a singleton logger for your application, supporting various logging levels and output formats.  This guide explains how to use its features effectively.

### 1. Initialization

Before using the logger, you must initialize it.  This sets up the logging handlers (console, files, JSON).

```python
logger = Logger()
logger.initialize_loggers(
    info_log_path='info.log',
    debug_log_path='debug.log',
    errors_log_path='errors.log',
    json_log_path='log.json'
)
```

*   `info_log_path`, `debug_log_path`, `errors_log_path`, `json_log_path`: Specify the file paths where you want the respective log types to be saved.  Leave these empty if you don't need those file outputs.

This step is crucial; without initialization, logging functions won't work correctly.  The initialization happens only once per application.


### 2. Logging Messages

The `Logger` class provides methods for different log levels:

```python
# Log an info message
logger.info('This is an info message')

# Log a success message (same level as info, uses cyan color)
logger.success('Operation completed successfully.')

# Log a warning message (yellow color)
logger.warning('Resource usage is high.')

# Log a debug message (cyan color, include exception details)
logger.debug('Processing data...', ex=someException)

# Log an error message (white on red background)
logger.error('Database query failed.', ex=someException)

# Log a critical message (white on red background)
logger.critical('Application is shutting down.', ex=someException)
```


*   **`message`**: The string you want to log.
*   **`ex`**: An exception object (e.g., `Exception`, `TypeError`).  If provided, the logger includes exception details in the log.
*   **`exc_info=True`**:  If set to `True` (defaults to `False` for INFO and SUCCESS), the logger will include a complete traceback if an exception is provided.  Crucial for debugging!  This is automatically used for ERROR and CRITICAL level logs.
*   **`colors`**: A tuple like `(colorama.Fore.RED, colorama.Back.BLACK)` to set specific colors for the message.  If not provided, default colors are used (green for info, cyan for success, yellow for warning, and white/red for errors).

### 3. Colors and Exception Handling

The logger uses the `colorama` library for console colorization.  Ensure `colorama` is installed.

```bash
pip install colorama
```

Exception information (`ex`) is added automatically to the respective log type (except for INFO and SUCCESS).

### 4.  Custom Formatting

The module includes a `JsonFormatter` for generating JSON log entries. When you initialize with `json_log_path`, this formatter is used.



### 5.  Important Considerations

*   **Singleton:**  The `Logger` uses the Singleton pattern, meaning only one instance exists throughout your application.  You don't need to create multiple instances.
*   **File Handling:**  Specify log file paths during initialization for persistent storage.
*   **Error Handling:**  Use `ex` to include exception details when logging errors for debugging.  `exc_info` controls the level of detail.


This comprehensive guide should help you integrate the logger effectively into your applications. Remember to adapt the file paths according to your project structure. If you have further questions or specific formatting requirements, please provide more context.
```