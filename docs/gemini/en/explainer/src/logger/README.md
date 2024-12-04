# src.logger Module Documentation

## <input code>

```
### Documentation for the `src.logger` Module

The `src.logger` module provides a flexible logging system that supports console, file, and JSON logging. It utilizes the Singleton design pattern to ensure only a single instance of the logger is used across the application. The logger supports various log levels (e.g., `INFO`, `ERROR`, `DEBUG`) and includes colorized output for console logs. You can also customize the log output formats and control logging to different files.

---

### Classes:
- **SingletonMeta**: Metaclass that implements the Singleton design pattern for the logger.
- **JsonFormatter**: A custom formatter that outputs logs in JSON format.
- **Logger**: The main logger class that supports console, file, and JSON logging.

---

### Functions:

#### `__init__`
Initializes the Logger instance with placeholders for different logger types (console, file, and JSON).

#### `_configure_logger(name: str, log_path: str, level: Optional[int] = logging.DEBUG, formatter: Optional[logging.Formatter] = None, mode: Optional[str] = 'a') -> logging.Logger`
Configures and returns a logger instance.

**Parameters:**
- `name`: Name of the logger.
- `log_path`: Path to the log file.
- `level`: Logging level, e.g., `logging.DEBUG`. Default is `logging.DEBUG`.
- `formatter`: Custom formatter (optional).
- `mode`: File mode, e.g., `'a'` for append (default).

**Returns**: Configured `logging.Logger` instance.

#### `initialize_loggers(info_log_path: Optional[str] = '', debug_log_path: Optional[str] = '', errors_log_path: Optional[str] = '', json_log_path: Optional[str] = '')`
Initializes the loggers for console and file logging (info, debug, error, and JSON).

**Parameters:**
- `info_log_path`: Path for info log file (optional).
- `debug_log_path`: Path for debug log file (optional).
- `errors_log_path`: Path for error log file (optional).
- `json_log_path`: Path for JSON log file (optional).

#### `log(level, message, ex=None, exc_info=False, color=None)`
Logs a message at the specified level (e.g., `INFO`, `DEBUG`, `ERROR`) with optional exception and color formatting.

**Parameters:**
- `level`: Logging level (e.g., `logging.INFO`, `logging.DEBUG`).
- `message`: The log message.
- `ex`: Optional exception to log.
- `exc_info`: Whether to include exception information (default is `False`).
- `color`: Tuple with text and background colors for console output (optional).

#### `info(message, ex=None, exc_info=False, colors: Optional[tuple] = None)`
Logs an info message.

**Parameters:**
- `message`: The info message to log.
- `ex`: Optional exception to log.
- `exc_info`: Whether to include exception info (default is `False`).
- `colors`: Tuple of color values for the message (optional).

#### `success(message, ex=None, exc_info=False, colors: Optional[tuple] = None)`
Logs a success message.

**Parameters:**
Same as `info`.

#### `warning(message, ex=None, exc_info=False, colors: Optional[tuple] = None)`
Logs a warning message.

**Parameters:** Same as `info`.

#### `debug(message, ex=None, exc_info=True, colors: Optional[tuple] = None)`
Logs a debug message.

**Parameters:** Same as `info`.

#### `error(message, ex=None, exc_info=True, colors: Optional[tuple] = None)`
Logs an error message.

**Parameters:** Same as `info`.

#### `critical(message, ex=None, exc_info=True, colors: Optional[tuple] = None)`
Logs a critical message.

**Parameters:** Same as `info`.

---

### Parameters for the Logger
The `Logger` class accepts several optional parameters for customizing the logging behavior.

- **Level**: Controls the severity of logs that are captured.
- **Formatter**: Defines how the log messages are formatted.
- **Color**: Colors for the log messages in the console.

---

### File Logging Configuration (`config`)

To log messages to a file, you can specify the file paths in the configuration.

```python
config = {
    'info_log_path': 'logs/info.log',
    'debug_log_path': 'logs/debug.log',
    'errors_log_path': 'logs/errors.log',
    'json_log_path': 'logs/log.json'
}
```

---

### Example Usage

```python
# ... (Example usage as provided in the documentation)
```
```

## <algorithm>

The algorithm workflow can be described in a step-by-step manner:

1. **Initialization:** The Logger is instantiated (`Logger()`).
2. **Configuration:** The `initialize_loggers()` function is called with paths to log files. For each log type, it creates a logger using `_configure_logger()`.
3. **Logging:** User code calls logging functions (e.g., `logger.info()`). Each function checks the log level against the configured logger level, then it uses the appropriate formatter for output (console, file, or JSON).

## <mermaid>

```mermaid
graph LR
    A[Logger()] --> B{initialize_loggers(config)};
    B --> C{_configure_logger(info_log_path)};
    B --> D{_configure_logger(debug_log_path)};
    B --> E{_configure_logger(errors_log_path)};
    B --> F{_configure_logger(json_log_path)};
    C --> G[info Log];
    D --> H[debug Log];
    E --> I[error Log];
    F --> J[json Log];
    K[User Code] --> L[logger.info()];
    L --> M[Log Message Processing];
    M --> [Console Output];
    M --> [File Output];
    M --> [JSON Output];
```

**Dependencies Analysis:**

The mermaid diagram utilizes the `logging` module extensively and implicitly references the `colorama` module for color support (evident from the example usage).  The `Optional` type hinting suggests the `typing` module is in use. The diagram doesn't explicitly show `JsonFormatter` and `SingletonMeta` as direct components of the logging process, but rather assumes these contribute to the overall functionality through `Logger`.


## <explanation>

**Imports:**

The code heavily utilizes the `logging` module.  There are implicit dependencies on `typing` (from type hints), and `colorama` for colored console output, inferred from the example usages.

**Classes:**

*   **SingletonMeta:** This metaclass ensures that only one instance of the Logger exists. It's a fundamental part of the Singleton design pattern.
*   **JsonFormatter:** This custom formatter modifies the log format to JSON, potentially using methods from `json` module.
*   **Logger:**  This is the core class. It manages different loggers (console, file, JSON) and levels. It likely employs `logging.Logger` internally.


**Functions:**

*   **`__init__`:** Initializes internal variables, probably for future use by methods.
*   **`_configure_logger`:** This function is crucial for configuring individual log handlers, responsible for writing logs to different destinations (e.g., console, file).
*   **`initialize_loggers`:** This function acts as a central point to set up all the log targets using the `_configure_logger` for each log type.
*   **Logging methods (e.g., `info`, `error`):** These are responsible for creating log records at specified levels and appending them to the appropriate destinations. They often involve handling exceptions, using formatters, and colorization (from colorama).


**Variables:**

*   `config`: A dictionary holding configuration parameters, like the paths to log files (`info_log_path`, `debug_log_path`, etc.).  Data flow is critical as this dictionary drives the `initialize_loggers` which controls what and how logging is done.
*   `logger`: A variable holding the singleton instance of the Logger class.

**Potential Errors and Improvements:**

* **Error Handling:**  While the `log` method potentially handles exceptions, the `initialize_loggers` function could benefit from checking for invalid log paths. Robust error handling (e.g., `try...except` blocks) would make the module more resilient if the configuration files do not exist.
* **File Locking:** If multiple threads/processes are accessing the log files, proper locking mechanisms are necessary to avoid corruption.
* **Logging Level Management:** The default logging level for the module is `logging.DEBUG`.  Consider if this is appropriate for all circumstances; it might need to be configurable as an external parameter.

**Relationships with Other Parts of the Project:**

The `src.logger` module is a utility module, enabling logging in other parts of the application.  Other parts of the application, such as business logic (`src.business_logic`) or presentation layers, likely use this logger for recording events. The relationship is functional:  the logger is used in other `src` packages.

```
src.business_logic --> src.logger <-- src.presentation_layer