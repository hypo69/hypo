```python
import threading
import traceback
import logging
import colorama
import datetime
import json
import inspect

# from .beeper import Beeper, BeepLevel  # Assuming you have this import


class SingletonMeta(type):
    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    instance = super().__call__(*args, **kwargs)
                    cls._instances[cls] = instance
        return cls._instances[cls]


class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_entry = {
            "asctime": self.formatTime(record, self.datefmt),
            "name": record.name,
            "levelname": record.levelname,
            "message": record.getMessage(),
            "exc_info": (
                self.formatException(record.exc_info)
                if record.exc_info
                else None
            ),
            "timestamp": record.created,  # Add timestamp
            "filename": record.filename if hasattr(record, "filename") else None,
            "lineno": record.lineno if hasattr(record, "lineno") else None,
            "funcName": record.funcName if hasattr(record, "funcName") else None
        }
        return json.dumps(log_entry, ensure_ascii=False, indent=4)


class Logger(metaclass=SingletonMeta):
    def __init__(self):
        self.logger_console = None
        self.logger_file_info = None
        self.logger_file_debug = None
        self.logger_file_errors = None
        self.logger_file_json = None
        self._initialized = False

    def _configure_logger(
        self, name, log_path, level=logging.DEBUG, formatter=None, mode="a"
    ):
        logger = logging.getLogger(name)
        logger.setLevel(level)
        handler = logging.FileHandler(filename=log_path, mode=mode)
        handler.setFormatter(formatter or logging.Formatter("%(message)s"))
        logger.addHandler(handler)
        return logger

    def initialize_loggers(
        self, info_log_path="", debug_log_path="", errors_log_path="", json_log_path=""
    ):
        if self._initialized:
            return

        # Use a more descriptive timestamp
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        
        self.logger_console = logging.getLogger(f"console_{timestamp}")
        self.logger_console.setLevel(logging.DEBUG)
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
        self.logger_console.addHandler(console_handler)
        
        if info_log_path:
            self.logger_file_info = self._configure_logger(
                f"info_{timestamp}", info_log_path, logging.INFO, logging.Formatter('%(message)s')
            )
        if debug_log_path:
            self.logger_file_debug = self._configure_logger(
                f"debug_{timestamp}", debug_log_path, logging.DEBUG, logging.Formatter('%(message)s')
            )
        if errors_log_path:
            self.logger_file_errors = self._configure_logger(
                f"errors_{timestamp}", errors_log_path, logging.ERROR, logging.Formatter('%(message)s')
            )
        if json_log_path:
            self.logger_file_json = self._configure_logger(
                f"json_{timestamp}", json_log_path, logging.DEBUG, JsonFormatter()
            )

        self._initialized = True


    def _format_message(self, message, ex, color):  
        formatted_message = message
        if color:
            formatted_message = f"{color}{message}{colorama.Style.RESET_ALL}"
        if ex:
            formatted_message += "\n" + self._ex_full_info(ex)
        return formatted_message

    def _ex_full_info(self, ex):
        """Returns full exception information."""
        tb_list = traceback.extract_tb(ex.__traceback__)
        tb_string = traceback.format_list(tb_list)
        return "\n".join(tb_string)

    def log(self, level, message, ex=None, exc_info=False, color=None):
        if not self._initialized:
            self.initialize_loggers()
        
        formatted_message = self._format_message(message, ex, color)

        if self.logger_console:
          self.logger_console.log(level, formatted_message, exc_info=exc_info)
        if self.logger_file_json:
          self.logger_file_json.log(level, formatted_message, exc_info=exc_info)
        
        if level == logging.INFO and self.logger_file_info:
          self.logger_file_info.log(level, formatted_message)

        if level == logging.DEBUG and self.logger_file_debug:
            self.logger_file_debug.log(level, formatted_message)

        if level in (logging.ERROR, logging.CRITICAL) and self.logger_file_errors:
            self.logger_file_errors.log(level, formatted_message)


    # ... (rest of the methods)
```

**Key improvements and explanations:**

* **Clearer `_format_message`:**  Now correctly handles `ex` (exception) for formatting. Also, it prepends the optional color if provided.  This significantly improves clarity.
* **Robust `_ex_full_info`:**
    * Uses `traceback.extract_tb` to get the traceback information.
    * Uses `traceback.format_list` to format the traceback into a string.
    * **Crucially:** This avoids the previously problematic recursion and directly uses the traceback information to create a more informative log entry.
* **JSON Formatting Enhancements:**
    * Added `timestamp` to the JSON log entry.
    * Included `filename` and `lineno` in JSON output.  This is incredibly useful for debugging.
* **Initialization Check:** The `initialize_loggers` method now correctly checks if the logger is already initialized. This is critical for preventing multiple initializations that might have issues.


**How to use:**

```python
import colorama
colorama.init() # Initialize colorama

logger = Logger()
logger.initialize_loggers(info_log_path='info.log', debug_log_path='debug.log', errors_log_path='errors.log', json_log_path='log.json')

try:
    # ... your code that might raise exceptions ...
    raise ZeroDivisionError("Division by zero")
except Exception as ex:
    logger.error("An error occurred", ex, exc_info=True)

logger.info("This is an info message")
logger.debug("This is a debug message")
```

Remember to install the necessary packages:

```bash
pip install colorama
```

This revised code is much more robust, efficient, and produces more helpful logs. Remember to replace placeholders like `'info.log'` with your desired file paths. Also, make sure the necessary imports (like `from .beeper import Beeper, BeepLevel`) are in place if you need them.