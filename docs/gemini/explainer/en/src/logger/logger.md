
# -*- coding: utf-8 -*-\n#! venv/Scripts/python.exe\n#! venv/bin/python/python3.12\n\n"""\n.. module: src.logger \n\t:platform: Windows, Unix\n\t:synopsis: Logger Module\n"""\nMODE = \'dev\'\n\n"""This module provides a singleton logging utility with various logging levels and formats, including console, file, and JSON logging. It utilizes the Singleton design pattern to ensure a single instance of the logger is used throughout the application. The logger supports different log levels and output formats, and it can colorize console messages based on log severity.\n\nClasses:\n- SingletonMeta: Metaclass for Singleton pattern implementation.\n- JsonFormatter: Custom formatter for logging in JSON format.\n- Logger: Singleton logger class with methods for logging at different levels.\n\nClasses:\n    SingletonMeta\n    ----------\n    Metaclass for Singleton pattern implementation.\n    \n    JsonFormatter\n    -------------\n    Custom formatter for logging in JSON format.\n    \n    Logger\n    ------\n    Singleton logger class with methods for console, file, and JSON logging.\n\nFunctions:\n- __init__: Initializes the Logger instance.\n- _configure_logger: Configures and returns a logger with the specified parameters.\n- initialize_loggers: Initializes loggers for console, file, and JSON output.\n- _format_message: Formats a message with optional color and exception information.\n- _ex_full_info: Provides detailed exception information, including the file, function, and line number where the log was called.\n- log: Logs messages at a specified level with optional color and exception information.\n- info: Logs an info message.\n- success: Logs a success message.\n- warning: Logs a warning message.\n- debug: Logs a debug message.\n- error: Logs an error message.\n- critical: Logs a critical message.\n- info_red: Logs an info message in red.\n- info_black: Logs an info message in black with a white background.\n\nExamples:\n    # Initialize the logger\n    logger: Logger = Logger()\n    logger.initialize_loggers(info_log_path=\'info.log\', debug_log_path=\'debug.log\', errors_log_path=\'errors.log\', json_log_path=\'log.json\')\n\n    # Log messages at different levels\n    logger.info(\'This is an info message\')\n    logger.success(\'This is a success message\')\n    logger.warning(\'This is a warning message\',None,True)\n    logger.debug(\'This is a debug message\',None,exc_info=True)\n    logger.error(\'This is an error message\',ex)\n    logger.critical(\'This is a critical message\',ex)\n"""\n\n# -*- coding: utf-8 -*-\n#! venv/Scripts/python.exe\n#! venv/bin/python/python3.12\n\n"""\n.. module: src.logger\n    :platform: Windows, Unix\n    :synopsis: Logger Module\n"""\n\nimport threading\nimport traceback\nimport logging\nfrom typing import Optional\nimport colorama\nimport datetime\nimport json\nimport inspect\n\n# ... (rest of the code)\n\n# Initialize logger\nlogger: Logger = Logger()\n```

**<algorithm>**

```mermaid
graph TD
    A[Initialize Logger] --> B(initialize_loggers);
    B --> C{Check if initialized?};
    C -- Yes --> D[Return];
    C -- No --> E[Configure Loggers];
    E --> F[Console Logger];
    E --> G[Info File Logger];
    E --> H[Debug File Logger];
    E --> I[Error File Logger];
    E --> J[JSON Logger];
    F --> K[Set Level & Handler];
    G --> K;
    H --> K;
    I --> K;
    J --> K;
    K --> L[Set Formatter (if applicable)];
    L --> M[Add Handlers];
    M --> N[Set Initialized Flag];
    N --> D;
    subgraph Logging Operations
        O[log Method] --> P{Check Initialized?};
        P -- Yes --> Q[Format Message];
        P -- No --> R[Initialize Loggers];
        Q --> S[Log to Console];
        Q --> T[Log to Json File];
        Q --> U[Conditional Log to Other Files];
        S --> V[Exit];
        T --> V;
        U --> V;
        R --> P;
    end
```

**Example Data Flow:**

1.  `initialize_loggers` is called with file paths.
2.  `_configure_logger` configures individual loggers (console, info file, debug file, error file, JSON file).
3.  `log` is called with a message and logging level.
4.  `_format_message` formats the message (potentially adding color and exception info).
5.  Appropriate loggers (console, file, JSON) are called to log the formatted message.


**<explanation>**

**Imports:**

*   `threading`: Used for thread safety in the singleton implementation.
*   `traceback`: For retrieving exception details.
*   `logging`: Core Python logging module.
*   `typing`: Used for type hints (Optional).
*   `colorama`: For adding color to console output.
*   `datetime`: For timestamping logs.
*   `json`: For handling JSON formatted logs.
*   `inspect`: For getting the location of log calls


**Classes:**

*   **`SingletonMeta`**: A metaclass that ensures only one instance of the `Logger` class can exist. It uses a `_lock` for thread safety.
*   **`JsonFormatter`**: A custom formatter for creating JSON log entries, overriding the default formatting to output structured JSON logs.  Crucially, it handles `exc_info` which is important for detailed exception reports.
*   **`Logger`**:  The singleton logger.  It manages multiple loggers (console, info file, debug file, error file, JSON file) as attributes.  The `_initialized` flag is critical to prevent multiple logger instantiations or configurations.
    *   `__init__`: Initializes the logger instances to `None`.
    *   `_configure_logger`:  A helper function to efficiently configure a logger (name, path, level, formatter).  This avoids repeating the common steps of logging configuration.
    *   `initialize_loggers`: Initializes all the loggers;  critical for setting up logging output streams. Uses a timestamp to avoid conflicts if multiple loggers are initialized simultaneously. Importantly, it has initialization checks so loggers are not re-initialized.
    *   `_format_message`: Formats the log message with optional color and exception details.
    *   `_ex_full_info`:  Gets detailed exception info, including function, file, and line number where the log originated.  A critical component for understanding the context of the log entry.
    *   `log`: The core logging method; logs messages at different levels, handling color and exceptions.  It handles logging to multiple destinations.
    *   `info`, `success`, `warning`, `debug`, `error`, `critical`: Convenience methods for logging at specific levels with preset formatting, and optional color.


**Functions:**

*   `log`: The general logging method, taking the log level (`logging.INFO`, `logging.ERROR`, etc.) as the first argument.
*   Specific methods (`info`, `warning`, etc.): act as wrappers around `log` with preset log levels and colors.


**Variables:**

*   `MODE`: A string variable likely used for conditional logging or other aspects of the application, not directly part of logging but may affect its behavior.


**Potential Errors/Improvements:**

*   **Exception Handling in `_ex_full_info`:** The code currently has an `...` in the `_ex_full_info` function, which suggests that the exception handling might be incomplete. Add a complete `try-except` block to properly handle potential exceptions during traceback retrieval.
*   **Robustness of `_ex_full_info`:** The use of `inspect.stack()[3]` assumes a specific call stack depth. If the logging method is called in nested situations, it might need adjustments.
*   **Missing `close`:** The logging handlers are created but not closed.  Add `handler.close()` in `_configure_logger` to prevent resource leaks, especially if the application runs for extended periods.
*   **`colors` argument in various methods:** The `colors` argument is frequently used as a tuple of colors. This is fine but consider if a dedicated color class or enum would enhance readability and maintainability.

**Relationships with other parts of the project:**

This `logger` module is a crucial component in any application that needs structured logging.  It's likely used by other modules in the `src` package to record events, errors, and various informational data points.  The presence of file paths (`info_log_path`, etc.) indicates that the logs need to be stored for later analysis and debugging.  A dedicated analysis, archival, or monitoring system could further integrate with this functionality.
