## \file /src/logger/logger.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module:: src.logger.logger
	:platform: Windows, Unix
	:synopsis: Модуль определяющий корневой путь к проекту. Все импорты строятся относительно этого пути.
    :TODO: В дальнейшем перенести в системную переменную"""
MODE = 'dev'


import logging
import colorama
import datetime
import json
import inspect
import threading
from pathlib import Path
from typing import Optional
from types import SimpleNamespace

import header
from header import __root__
from src.utils.jjson import j_loads_ns


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

    def __init__(self, info_log_path: Optional[str] = None, 
                 debug_log_path: Optional[str] = None, 
                 errors_log_path: Optional[str] = None, 
                 json_log_path: Optional[str] = None):
        """ Initialize the Logger instance."""
        ...

        # Define file paths
        config = j_loads_ns(__root__ / 'src' / 'config.json')
        timestamp = datetime.datetime.now().strftime("%d%m%y%H%M")
        base_path:Path = Path(getattr(config.path, 'log', __root__ / 'log') / timestamp ) 
        info_log_path =  base_path / info_log_path or 'info.log'
        debug_log_path = base_path / debug_log_path or  'debug.log'
        errors_log_path = base_path / errors_log_path or  'errors.log'
        json_log_path =  base_path / json_log_path or  'LOG.json'

        # Console logger
        self.logger_console = logging.getLogger(name= 'logger_console')
        self.logger_console.setLevel(logging.DEBUG)
        # console_handler = logging.StreamHandler()
        # console_handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
        # self.logger_console.addHandler(console_handler)

        # Info file logger
        self.logger_file_info = logging.getLogger(name='logger_file_info')
        self.logger_file_info.setLevel(logging.INFO)
        info_handler = logging.FileHandler(info_log_path)
        info_handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
        self.logger_file_info.addHandler(info_handler)

        # Debug file logger
        self.logger_file_debug = logging.getLogger(name='logger_file_debug')
        self.logger_file_debug.setLevel(logging.DEBUG)
        debug_handler = logging.FileHandler(debug_log_path)
        debug_handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
        self.logger_file_debug.addHandler(debug_handler)

        # Errors file logger
        self.logger_file_errors =  logging.getLogger(name='logger_file_errors')
        self.logger_file_errors.setLevel(logging.ERROR)
        errors_handler = logging.FileHandler(errors_log_path)
        errors_handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
        self.logger_file_errors.addHandler(errors_handler)

        # JSON file logger
        self.logger_file_json = logging.getLogger(name='logger_json')
        self.logger_file_json.setLevel(logging.DEBUG)
        json_handler = logging.FileHandler(json_log_path)
        json_handler.setFormatter(JsonFormatter())
        self.logger_file_json.addHandler(json_handler)

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
        frame_info = inspect.stack()[3]
        file_name = frame_info.filename
        function_name = frame_info.function
        line_number = frame_info.lineno

        return f"\nFile: {file_name}, \n |\n  -Function: {function_name}, \n   |\n    --Line: {line_number}\n{ex if ex else ''}"

    def log(self, level, message, ex=None, exc_info=False, color=None):
        """ General method to log messages at specified level with optional color."""
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

    # Other logging methods (info, success, warning, debug, error, critical, etc.) remain the same

# Initialize logger with file paths
logger = Logger(info_log_path='info.log', debug_log_path='debug.log', errors_log_path='errors.log', json_log_path='log.json')