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
#### `warning(message, ex=None, exc_info=False, colors: Optional[tuple] = None)`
#### `debug(message, ex=None, exc_info=True, colors: Optional[tuple] = None)`
#### `error(message, ex=None, exc_info=True, colors: Optional[tuple] = None)`
#### `critical(message, ex=None, exc_info=True, colors: Optional[tuple] = None)`

All these functions log messages with varying levels of severity and optional exception information.  The `colors` parameter allows for colored console output.


---

### Algorithm

```
+-----------------+
|  Initialization  |
+-----------------+
|   Logger()      |---> Logger Instance
+-----------------+
| Initialize_loggers|
|   (config)       |---> Logging setup
+-----------------+
|    Log message   |
+-----------------+
|    info(msg)   |--->  check level; call _log
+-----------------+
|    error(msg)   |--->  check level; call _log
+-----------------+
|      ...        |
+-----------------+
|  Log to console |--->  print message
|   or file       |--->  write to file
|   or JSON       |--->  create json object
+-----------------+
```


### Explanation

* **Imports:** The code likely imports the `logging` module for general logging functionality.  Crucially, it likely also imports `colorama` for colorized output.  The relationship is that `src.logger` relies on these standard Python packages for basic logging and color support.

* **Classes:**
    * **`Logger`**: This is the core class.  Its `__init__` initializes attributes for different logger types (console, file, JSON) without setting them up initially. The `_configure_logger` method is likely responsible for creating and returning the actual logger instances. The `initialize_loggers` method creates those individual loggers for each log type (file or console).  The `log`, `info`, `error` etc., methods are just convenience functions that call the underlying `logging.Logger` methods.  `SingletonMeta` ensures only one logger instance is ever created.
    * **`JsonFormatter`**: This class likely creates a custom formatter that transforms log messages into JSON format. It's designed for different output formats.

* **Functions:**
    * **`__init__`**: Sets up the initial state of the logger instance.
    * **`_configure_logger`**:  Creates and configures the individual logging handlers for each log type (console, file, JSON). This is critical for handling different log streams.
    * **`initialize_loggers`**: Sets up the loggers based on provided file paths.
    * **`log` and variations (`info`, `success`, `warning`, `debug`, `error`, `critical`)**:  These are higher-level functions that encapsulate logging for different levels. The core `log` function takes care of the common logic, making the log methods more usable.
* **Variables:** The `config` dictionary is used to store paths for different log files, making the logging configuration more configurable.

* **Potential Errors/Improvements:**
    * **Error Handling:** While it uses `Optional`, the code would benefit from more comprehensive checks for file paths (e.g., if `log_path` or `info_log_path` etc., is invalid or if files can't be opened).
    * **Log Rotation:** The code lacks log rotation; files might grow indefinitely, affecting performance or even system stability.
    * **Thread Safety:** If multiple threads might access the logger concurrently, thread-safety mechanisms (e.g., locks) could be required.


**Relationships to Other Parts of the Project:**

This logger is a critical component, likely used by various parts of the application (`src.services`, `src.models`, etc.).  They'd call methods like `logger.info()` or `logger.error()` to record events within their execution flow. This logger module is responsible for sending the logs to the designated locations (console, file, and potentially JSON files). The logger's functionality is dependent on the `logging` and `colorama` libraries.  The config structure would likely be part of a broader configuration system for the application.