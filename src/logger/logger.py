import threading
import traceback
import logging
from typing import Optional
import colorama
import datetime
import json
import inspect

class SingletonMeta(type):
    """Metaclass for Singleton pattern implementation."""

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
    """Custom formatter for logging in JSON format."""

    def format(self, record: logging.LogRecord) -> str:
        """Format the log record as JSON.

        Args:
            record (logging.LogRecord): The log record.

        Returns:
            str: Formatted log record in JSON format.
        """
        log_entry = {
            "asctime": self.formatTime(record, self.datefmt),
            "name": record.name,
            "levelname": record.levelname,
            "message": record.getMessage(),
            "exc_info": self.formatException(record.exc_info) if record.exc_info else None,
        }
        return json.dumps(log_entry, ensure_ascii=False)

class Logger(metaclass=SingletonMeta):
    """Logger class implementing Singleton pattern with console, file, and JSON logging."""

    logger_console: Optional[logging.Logger] = None
    logger_file_info: Optional[logging.Logger] = None
    logger_file_debug: Optional[logging.Logger] = None
    logger_file_errors: Optional[logging.Logger] = None
    logger_file_json: Optional[logging.Logger] = None
    _initialized: bool = False

    def __init__(self):
        """Initialize the Logger instance."""
        self.logger_console = None
        self.logger_file_info = None
        self.logger_file_debug = None
        self.logger_file_errors = None
        self.logger_file_json = None
        self._initialized = False

    def _configure_logger(
        self, 
        name: str, 
        log_path: str, 
        level: Optional[int] = logging.DEBUG, 
        formatter: Optional[logging.Formatter] = None, 
        mode: Optional[str] = 'a'
    ) -> logging.Logger:
        """Configures and returns a logger.

        Args:
            name (str): Name of the logger.
            log_path (str): Path to the log file.
            level (Optional[int]): Logging level. Defaults to `logging.DEBUG`.
            formatter (Optional[logging.Formatter]): Custom formatter. Defaults to `None`.
            mode (Optional[str]): File mode. Defaults to `'a'`.

        Returns:
            logging.Logger: Configured logger instance.
        """
        logger = logging.getLogger(name)
        logger.setLevel(level)
        handler = logging.FileHandler(filename=log_path, mode=mode)
        handler.setFormatter(formatter or logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        logger.addHandler(handler)
        return logger

    def initialize_loggers(
        self, 
        info_log_path: Optional[str] = '', 
        debug_log_path: Optional[str] = '', 
        errors_log_path: Optional[str] = '', 
        json_log_path: Optional[str] = ''
    ):
        """Initializes loggers for console, info, debug, error, and JSON logging.

        Args:
            info_log_path (Optional[str]): Path to the info log file. Defaults to `''`.
            debug_log_path (Optional[str]): Path to the debug log file. Defaults to `''`.
            errors_log_path (Optional[str]): Path to the errors log file. Defaults to `''`.
            json_log_path (Optional[str]): Path to the JSON log file. Defaults to `''`.
        """
        if self._initialized:
            return

        timestamp = datetime.datetime.now().strftime('%d%m%y%H%M')

        if not self.logger_console:
            self.logger_console = logging.getLogger(f'console_{timestamp}')
            self.logger_console.setLevel(logging.DEBUG)
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))
            self.logger_console.addHandler(console_handler)

        if info_log_path:
            self.logger_file_info = self._configure_logger(f'info_{timestamp}', info_log_path, logging.INFO)

        if debug_log_path:
            self.logger_file_debug = self._configure_logger(f'debug_{timestamp}', debug_log_path, logging.DEBUG)

        if errors_log_path:
            self.logger_file_errors = self._configure_logger(f'errors_{timestamp}', errors_log_path, logging.ERROR)

        if json_log_path:
            self.logger_file_json = self._configure_logger(f'json_{timestamp}', json_log_path, logging.DEBUG, JsonFormatter())

        self._initialized = True


    def _format_message(self, message, ex=None, color=None):
        """ Returns formatted message with optional color and exception information."""
        if color:
            text_color, background_color = (
                color if isinstance(color, tuple) else (color, "")
            )
            message = f"{text_color}{background_color}{message} {ex or ''}{colorama.Style.RESET_ALL}"
        return message

    def _ex_full_info(self, ex):
        """ Returns full exception information along with the previous function, file, and line details."""
        frame_info = inspect.stack()[3]  # 0 is the current frame, 1 is `_ex_full_info`, 2 is the caller of the logger method
        file_name = frame_info.filename
        function_name = frame_info.function
        line_number = frame_info.lineno

        return f"\nFile: {file_name}, \n |\n  -Function: {function_name}, \n   |\n    --Line: {line_number}\n{ex if ex else ''}"

    def log(self, level, message, ex=None, exc_info=False, color=None):
        """ General method to log messages at specified level with optional color."""
        if not self._initialized:
            self.initialize_loggers()  # Ensure loggers are initialized if not already done

        formatted_message = self._format_message(message, ex, color)
        if exc_info:
            formatted_message += self._ex_full_info(ex)

        if self.logger_console:
            self.logger_console.log(level, formatted_message, exc_info=exc_info)

        if self.logger_file_json:
            self.logger_file_json.log(level, message, exc_info=exc_info)

        if level == logging.INFO and self.logger_file_info:
            self.logger_file_info.log(level, formatted_message)

        if level == logging.DEBUG and self.logger_file_debug:
            self.logger_file_debug.log(level, formatted_message)

        if level in [logging.ERROR, logging.CRITICAL] and self.logger_file_errors:
            self.logger_file_errors.log(level, formatted_message)

    def info(self, message, ex=None, exc_info=False, colors: Optional[tuple] = None):
        """ Logs an info message."""
        self.log(logging.INFO, 
                 message, 
                 ex, 
                 exc_info, 
                 colorama.Fore.GREEN if not colors else colors)

    def success(self, message, ex=None, exc_info=False, colors: Optional[tuple] = None):
        """ Logs a success message."""
        self.log(logging.INFO, 
                 message, 
                 ex, 
                 exc_info, 
                 colorama.Fore.CYAN if not colors else colors)

    def warning(self, 
                message, 
                ex=None, 
                exc_info=False, 
                colors: Optional[tuple] = None):
        """ Logs a warning message."""
        self.log(logging.WARNING, 
                 message, 
                 ex, 
                 exc_info, 
                 colorama.Fore.YELLOW if not colors else colors)

    def debug(self, message, ex=None, exc_info=True, colors: Optional[tuple] = None):
        """ Logs a debug message."""
        self.log(
            logging.DEBUG, 
            message, 
            ex, 
            exc_info, 
            colorama.Fore.CYAN if not colors else colors)

    def error(self, message, ex=None, exc_info=True, colors: Optional[tuple] = None):
        """ Logs an error message."""
        self.log(
            logging.ERROR,
            message,
            ex,
            exc_info,
            (colorama.Fore.WHITE, colorama.Back.RED),
        )

    def critical(self, message, ex=None, exc_info=True, colors: Optional[tuple] = None):
        """ Logs a critical message."""
        self.log(
            logging.CRITICAL,
            message,
            ex,
            exc_info,
            colors if colors else (colorama.Fore.WHITE, colorama.Back.RED),
        )

# Initialize logger
logger: Logger = Logger()