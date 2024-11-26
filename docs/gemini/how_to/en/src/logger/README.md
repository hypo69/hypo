How to use the `src.logger` module

This guide demonstrates how to use the `src.logger` module for flexible and customizable logging in your Python application.

**1. Installation (if necessary):**

Ensure you have the necessary dependencies installed, including `colorama` for colored console output:

```bash
pip install colorama
```

**2. Import the Logger:**

Import the `Logger` class from the `src.logger` module:

```python
from src.logger import Logger
```

**3. Configuration:**

Define a dictionary `config` to specify the paths for your log files:

```python
config = {
    'info_log_path': 'logs/info.log',
    'debug_log_path': 'logs/debug.log',
    'errors_log_path': 'logs/errors.log',
    'json_log_path': 'logs/log.json'
}
```

*   Replace `'logs/info.log'`, etc., with the actual desired paths for your log files.  Create the `logs` directory if it doesn't exist.

**4. Initialize the Logger:**

Create a `Logger` instance and initialize it with your configuration:

```python
logger = Logger()
logger.initialize_loggers(**config)
```

This step sets up the logging handlers for console, info file, debug file, error file, and JSON file logging.

**5. Logging Messages:**

Use the various logging methods (e.g., `info`, `debug`, `error`) to log messages with different severity levels:

```python
logger.info('This is an informational message.')
logger.debug('This is a debugging message.')
logger.warning('This is a warning message.')
logger.error('An error occurred: %s', 'Some error description') #  Use format strings for more complex messages
logger.critical('Critical system error.')
```

**Important Considerations:**

*   **Log Levels:**  Choose the appropriate log level (`logging.DEBUG`, `logging.INFO`, `logging.WARNING`, `logging.ERROR`, `logging.CRITICAL`) for each message.  This allows you to filter logs based on severity.

*   **Exception Handling:** You can include exception information:

```python
try:
    # Some code that might raise an exception
    result = some_function()
except Exception as e:
    logger.error('An error occurred:', exc_info=True)  # Full traceback
```

*   **Colorization (Optional):**  Use the `colors` parameter to control the console log colors (requires `colorama`):

```python
import colorama

logger.info('Success!', colors=(colorama.Fore.GREEN, colorama.Back.BLACK))
logger.error('Error', colors=(colorama.Fore.RED, colorama.Back.YELLOW))
```

**6. Custom Formatters (Advanced):**

For more complex log formatting (e.g., JSON), use the `formatter` parameter in `_configure_logger`:

```python
from logging import Formatter

# Example JSON formatter
json_formatter = Formatter('{"timestamp": "%(asctime)s", "level": "%(levelname)s", "message": "%(message)s"}')

# ... (previous initialization code) ...
logger._configure_logger("json_logger", config['json_log_path'], formatter=json_formatter)

```

This will create log entries in the specified file in a JSON format. Replace the JSON string with your desired JSON format string.

**7. Troubleshooting:**

*   **File not found:** Double-check file paths and directory permissions.
*   **No output:**  Verify that the logger instance is correctly initialized and used in your application.

This comprehensive guide provides a clear understanding of how to use the `src.logger` module effectively in your Python projects. Remember to tailor the configuration and logging methods to best suit your specific needs and application requirements.