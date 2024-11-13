## \file hypotez/src/logger/logger.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
## ~~~~~~~~~~~~~
""" module: src.logger """

"""
Logger Module

This module provides a singleton logging utility with various logging levels and formats, including console, file, and JSON logging. It utilizes the Singleton design pattern to ensure a single instance of the logger is used throughout the application. The logger supports different log levels and output formats, and it can colorize console messages based on log severity.

Classes:
- SingletonMeta: Metaclass for Singleton pattern implementation.
- JsonFormatter: Custom formatter for logging in JSON format.
- Logger: Singleton logger class with methods for logging at different levels.

Classes:
    SingletonMeta
    ----------
    Metaclass for Singleton pattern implementation.
    
    JsonFormatter
    -------------
    Custom formatter for logging in JSON format.
    
    Logger
    ------
    Singleton logger class with methods for console, file, and JSON logging.

Functions:
- __init__: Initializes the Logger instance.
- _configure_logger: Configures and returns a logger with the specified parameters.
- initialize_loggers: Initializes loggers for console, file, and JSON output.
- _format_message: Formats a message with optional color and exception information.
- _ex_full_info: Provides detailed exception information, including the file, function, and line number where the log was called.
- log: Logs messages at a specified level with optional color and exception information.
- info: Logs an info message.
- success: Logs a success message.
- warning: Logs a warning message.
- debug: Logs a debug message.
- error: Logs an error message.
- critical: Logs a critical message.
- info_red: Logs an info message in red.
- info_black: Logs an info message in black with a white background.

Examples:
    # Initialize the logger
    logger: Logger = Logger()
    logger.initialize_loggers(info_log_path='info.log', debug_log_path='debug.log', errors_log_path='errors.log', json_log_path='log.json')

    # Log messages at different levels
    logger.info('This is an info message')
    logger.success('This is a success message')
    logger.warning('This is a warning message',None,True)
    logger.debug('This is a debug message',None,exc_info=True)
    logger.error('This is an error message',ex)
    logger.critical('This is a critical message',ex)

"""
...

import threading
import traceback
import logging
import colorama
import datetime
import json
import inspect

# from .beeper import Beeper, BeepLevel


class SingletonMeta(type):
    """ Metaclass for Singleton pattern implementation."""

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
    """ Custom formatter for logging in JSON format."""

    def format(self, record):
        """ Format the log record as JSON."""
        log_entry = {
            "asctime": self.formatTime(record, self.datefmt),
            "name": record.name,
            "levelname": record.levelname,
            "message": record.getMessage(),
            "exc_info": self.formatException(record.exc_info)
            if record.exc_info
            else None,
        }
        return json.dumps(log_entry, ensure_ascii=False)


class Logger(metaclass=SingletonMeta):
    """ Logger class implementing Singleton pattern with console, file, and JSON logging."""

    # Class attributes declaration
    logger_console: logging.Logger = None
    logger_file_info: logging.Logger = None
    logger_file_debug: logging.Logger = None
    logger_file_errors: logging.Logger = None
    logger_file_json: logging.Logger = None
    _initialized: bool = False  # Flag to check initialization

    def __init__(self):
        """ Initialize the Logger instance."""
        self.logger_console = None
        self.logger_file_info = None
        self.logger_file_debug = None
        self.logger_file_errors = None
        self.logger_file_json = None
        self._initialized = False  # Flag to check initialization

    def _configure_logger(
        self, name, log_path, level=logging.DEBUG, formatter=None, mode="a"
    ):
        """ Configures and returns a logger."""
        logger = logging.getLogger(name)
        logger.setLevel(level)
        handler = logging.FileHandler(filename=log_path, mode=mode)
        handler.setFormatter(
            formatter or logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        )
        logger.addHandler(handler)
        return logger

    def initialize_loggers(
        self, info_log_path="", debug_log_path="", errors_log_path="", json_log_path=""
    ):
        """ Initializes loggers for console, info, debug, error, and JSON logging."""
        if self._initialized:
            return  # Avoid reinitialization

        timestamp = datetime.datetime.now().strftime("%d%m%y%H%M")

        if not self.logger_console:
            self.logger_console = logging.getLogger(f"console_{timestamp}")
            self.logger_console.setLevel(logging.DEBUG)
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(
                logging.Formatter("%(levelname)s: %(message)s")
            )
            self.logger_console.addHandler(console_handler)

        if info_log_path:
            self.logger_file_info = self._configure_logger(
                f"info_{timestamp}", info_log_path, logging.INFO
            )

        if debug_log_path:
            self.logger_file_debug = self._configure_logger(
                f"debug_{timestamp}", debug_log_path, logging.DEBUG
            )

        if errors_log_path:
            self.logger_file_errors = self._configure_logger(
                f"errors_{timestamp}", errors_log_path, logging.ERROR
            )

        if json_log_path:
            self.logger_file_json = self._configure_logger(
                f"json_{timestamp}", json_log_path, logging.DEBUG, JsonFormatter()
            )

        self._initialized = True  # Mark as initialized

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
        ...
        # Get the previous frame in the stack to find where the log was called
        # Adjust the stack index based on the depth of the call
        frame_info = inspect.stack()[
            3
        ]  # 0 is the current frame, 1 is `_ex_full_info`, 2 is the caller of the logger method
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

    def info(self, message, ex=None, exc_info=False):
        """ Logs an info message."""
        self.log(logging.INFO, message, ex, exc_info, colorama.Fore.GREEN)

    def success(self, message, ex=None, exc_info=False):
        """ Logs a success message."""
        self.log(logging.INFO, message, ex, exc_info, colorama.Fore.CYAN)

    def warning(self, message, ex=None, exc_info=False):
        """ Logs a warning message."""
        self.log(logging.WARNING, message, ex, exc_info, colorama.Fore.YELLOW)

    def debug(self, message, ex=None, exc_info=True):
        """ Logs a debug message."""
        self.log(logging.DEBUG, message, ex, exc_info, colorama.Fore.CYAN)

    def error(self, message, ex=None, exc_info=True):
        """ Logs an error message."""
        self.log(
            logging.ERROR,
            message,
            ex,
            exc_info,
            (colorama.Fore.WHITE, colorama.Back.RED),
        )

    def critical(self, message, ex=None, exc_info=True):
        """ Logs a critical message."""
        self.log(
            logging.CRITICAL,
            message,
            ex,
            exc_info,
            (colorama.Fore.BLACK, colorama.Back.YELLOW),
        )

    def info_red(self, message):
        """ Logs an info message in red."""
        self.log(logging.INFO, message, color=colorama.Fore.RED)

    def info_black(self, message):
        """ Logs an info message in black with a white background."""
        self.log(
            logging.INFO, message, color=(colorama.Fore.BLACK, colorama.Back.WHITE)
        )


# Initialize logger
logger: Logger = Logger()
