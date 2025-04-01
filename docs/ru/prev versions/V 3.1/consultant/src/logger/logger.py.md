## Анализ кода модуля `logger`

**Качество кода:**

- **Соответствие стандартам**: 7/10
- **Плюсы**:
    - Реализация паттерна Singleton для класса `Logger`.
    - Использование `colorama` для цветного вывода в консоль.
    - Наличие уровней логирования (INFO, DEBUG, ERROR, CRITICAL).
    - Возможность логирования в JSON-формате.
    - Добавлены символы для отображения уровней логирования.
- **Минусы**:
    - Использование устаревшего способа чтения конфига: `json.loads(Path(__root__ / "src" / "config.json").read_text(encoding="UTF-8"))`.
    - Смешение форматирования строк (f-strings и конкатенация).
    - Не все методы документированы.
    - Отсутствуют проверки типов для параметров методов логирования.

**Рекомендации по улучшению:**

1.  **Использование `j_loads` или `j_loads_ns`**:
    - Замените чтение конфигурационного файла с использованием `json.loads` на `j_loads_ns` из `src.utils.jjson`.

2.  **Документирование методов**:
    - Добавьте docstring к методам, чтобы улучшить понимание их назначения и использования.

3.  **Унифицировать форматирование строк**:
    - Используйте только f-strings для форматирования лог-сообщений.
        ```python
        message = f'{log_symbol} {text_color}{bg_color}{message} {ex or ""}{colorama.Style.RESET_ALL}'
        ```

4.  **Улучшение читаемости**:
    - Упростить метод `_ex_full_info`, уменьшив количество конкатенаций строк.

5.  **Проверки типов**:
    - Добавить аннотации типов для параметров методов логирования (info, debug, error и т.д.).

6.  **Удалить неиспользуемый код**:
    - Закомментированная строка `#self.logger_console.log(level, formatted_message, exc_info=exc_info)` в методе `log`.

**Оптимизированный код:**

```python
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
.. module:: src.logger.logger
    :platform: Windows, Unix
    :synopsis: Модуль логгера

"""

import logging
import colorama
import datetime
import json
import inspect
import threading
from pathlib import Path
from typing import Optional, Tuple
from types import SimpleNamespace

from src.utils.jjson import j_loads_ns # Импорт j_loads_ns
from header import __root__


TEXT_COLORS = {
    'black': colorama.Fore.BLACK,
    'red': colorama.Fore.RED,
    'green': colorama.Fore.GREEN,
    'yellow': colorama.Fore.YELLOW,
    'blue': colorama.Fore.BLUE,
    'magenta': colorama.Fore.MAGENTA,
    'cyan': colorama.Fore.CYAN,
    'white': colorama.Fore.WHITE,
    'light_gray': colorama.Fore.LIGHTBLACK_EX,
    'light_red': colorama.Fore.LIGHTRED_EX,
    'light_green': colorama.Fore.LIGHTGREEN_EX,
    'light_yellow': colorama.Fore.LIGHTYELLOW_EX,
    'light_blue': colorama.Fore.LIGHTBLUE_EX,
    'light_magenta': colorama.Fore.LIGHTMAGENTA_EX,
    'light_cyan': colorama.Fore.LIGHTCYAN_EX,
}

# Словарь для цветов фона
BG_COLORS = {
    'black': colorama.Back.BLACK,
    'red': colorama.Back.RED,
    'green': colorama.Back.GREEN,
    'yellow': colorama.Back.YELLOW,
    'blue': colorama.Back.BLUE,
    'magenta': colorama.Back.MAGENTA,
    'cyan': colorama.Back.CYAN,
    'white': colorama.Back.WHITE,
    'light_gray': colorama.Back.LIGHTBLACK_EX,
    'light_red': colorama.Back.LIGHTRED_EX,
    'light_green': colorama.Back.LIGHTGREEN_EX,
    'light_yellow': colorama.Back.LIGHTYELLOW_EX,
    'light_blue': colorama.Back.LIGHTBLUE_EX,
    'light_magenta': colorama.Back.LIGHTMAGENTA_EX,
    'light_cyan': colorama.Back.LIGHTCYAN_EX,
}

LOG_SYMBOLS = {
    logging.INFO: 'ℹ️',  # Information
    logging.WARNING: '⚠️',  # Warning
    logging.ERROR: '❌',  # Error
    logging.CRITICAL: '🔥',  # Critical
    logging.DEBUG: '🐛',  # Debug
    'EXCEPTION': '🚨',  # Exception
    'SUCCESS': '✅' # Success
}


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

    def format(self, record):
        """Format the log record as JSON."""
        log_entry = {
            'asctime': self.formatTime(record, self.datefmt),
            'levelname': record.levelname,
            'message': record.getMessage().replace('"', '\''),
            'exc_info': self.formatException(record.exc_info)
            if record.exc_info
            else None,
        }
        _json = json.dumps(log_entry, ensure_ascii=False)
        return _json


class Logger(metaclass=SingletonMeta):
    """Logger class implementing Singleton pattern with console, file, and JSON logging."""

    log_files_path: Path
    info_log_path: Path
    debug_log_path: Path
    errors_log_path: Path
    json_log_path: Path

    def __init__(
        self,
        info_log_path: Optional[str] = None,
        debug_log_path: Optional[str] = None,
        errors_log_path: Optional[str] = None,
        json_log_path: Optional[str] = None,
    ):
        """
        Initialize the Logger instance.

        Args:
            info_log_path (Optional[str], optional): Путь к файлу информационного лога. Defaults to None.
            debug_log_path (Optional[str], optional): Путь к файлу дебаг лога. Defaults to None.
            errors_log_path (Optional[str], optional): Путь к файлу лога ошибок. Defaults to None.
            json_log_path (Optional[str], optional): Путь к файлу JSON лога. Defaults to None.
        """
        # Define file paths
        config = j_loads_ns(__root__ / 'src' / 'config.json') # Используем j_loads_ns
        timestamp = datetime.datetime.now().strftime('%d%m%y%H%M')
        base_path: Path = Path(config.path['log'])
        self.log_files_path: Path = base_path / timestamp

        self.info_log_path = self.log_files_path / (info_log_path or 'info.log')
        self.debug_log_path = self.log_files_path / (debug_log_path or 'debug.log')
        self.errors_log_path = self.log_files_path / (errors_log_path or 'errors.log')
        self.json_log_path = base_path / (json_log_path or f'{timestamp}.json')

        # Ensure directories exist
        self.log_files_path.mkdir(parents=True, exist_ok=True)

        # Ensure log files exist
        self.info_log_path.touch(exist_ok=True)
        self.debug_log_path.touch(exist_ok=True)
        self.errors_log_path.touch(exist_ok=True)
        self.json_log_path.touch(exist_ok=True)

        # Console logger
        self.logger_console = logging.getLogger(name='logger_console')
        self.logger_console.setLevel(logging.DEBUG)

        # Info file logger
        self.logger_file_info = logging.getLogger(name='logger_file_info')
        self.logger_file_info.setLevel(logging.INFO)
        info_handler = logging.FileHandler(self.info_log_path)
        info_handler.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))
        self.logger_file_info.addHandler(info_handler)

        # Debug file logger
        self.logger_file_debug = logging.getLogger(name='logger_file_debug')
        self.logger_file_debug.setLevel(logging.DEBUG)
        debug_handler = logging.FileHandler(self.debug_log_path)
        debug_handler.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))
        self.logger_file_debug.addHandler(debug_handler)

        # Errors file logger
        self.logger_file_errors = logging.getLogger(name='logger_file_errors')
        self.logger_file_errors.setLevel(logging.ERROR)
        errors_handler = logging.FileHandler(self.errors_log_path)
        errors_handler.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))
        self.logger_file_errors.addHandler(errors_handler)

        # JSON file logger
        self.logger_file_json = logging.getLogger(name='logger_json')
        self.logger_file_json.setLevel(logging.DEBUG)
        json_handler = logging.FileHandler(self.json_log_path)
        json_handler.setFormatter(JsonFormatter())  # Используем наш кастомный форматтер
        self.logger_file_json.addHandler(json_handler)

        # Удаляем все обработчики, которые выводят в консоль
        for handler in self.logger_file_json.handlers:
            if isinstance(handler, logging.StreamHandler):
                self.logger_file_json.removeHandler(handler)

    def _format_message(self, message: str, ex: Optional[Exception] = None, color: Optional[Tuple[str, str]] = None, level: Optional[int] = None) -> str:
        """
        Returns formatted message with optional color and exception information.

        Args:
            message (str): The log message.
            ex (Optional[Exception], optional): The exception object. Defaults to None.
            color (Optional[Tuple[str, str]], optional): Text and background colors. Defaults to None.
            level (Optional[int], optional): Logging level. Defaults to None.

        Returns:
            str: The formatted log message.
        """
        log_symbol = LOG_SYMBOLS.get(level, '')  # Get log symbol based on level
        if color:
            text_color, bg_color = color
            text_color = TEXT_COLORS.get(text_color, colorama.Fore.RESET)
            bg_color = BG_COLORS.get(bg_color, colorama.Back.RESET)
            message = f'{log_symbol} {text_color}{bg_color}{message} {ex or ""}{colorama.Style.RESET_ALL}'
        else:
            message = f'{log_symbol} {message} {ex or ""}'
        return message

    def _ex_full_info(self, ex: Exception) -> str:
        """
        Returns full exception information along with the previous function, file, and line details.

        Args:
            ex (Exception): The exception object.

        Returns:
            str: Formatted exception information.
        """
        frame_info = inspect.stack()[3]
        file_name = frame_info.filename
        function_name = frame_info.function
        line_number = frame_info.lineno

        return f'\nFile: {file_name}, \n |\n  -Function: {function_name}, \n   |\n    --Line: {line_number}\n{ex if ex else ""}'

    def log(self, level: int, message: str, ex: Optional[Exception] = None, exc_info: bool = False, color: Optional[Tuple[str, str]] = None):
        """
        General method to log messages at specified level with optional color.

        Args:
            level (int): Logging level.
            message (str): The log message.
            ex (Optional[Exception], optional): The exception object. Defaults to None.
            exc_info (bool, optional): Whether to include exception info. Defaults to False.
            color (Optional[Tuple[str, str]], optional): Text and background colors. Defaults to None.
        """
        formatted_message = self._format_message(message, ex, color, level=level)

        if self.logger_console:
            # self.logger_console.log(level, formatted_message, exc_info=exc_info) # Old code
            if exc_info and ex:
                self.logger_console.exception(formatted_message)
            else:
                self.logger_console.log(level, formatted_message, exc_info=exc_info)

    def info(self, message: str, ex: Optional[Exception] = None, exc_info: bool = False, text_color: str = 'green', bg_color: str = ''):
        """
        Logs an info message with optional text and background colors.

        Args:
            message (str): The log message.
            ex (Optional[Exception], optional): The exception object. Defaults to None.
            exc_info (bool, optional): Whether to include exception info. Defaults to False.
            text_color (str, optional): Text color. Defaults to "green".
            bg_color (str, optional): Background color. Defaults to "".
        """
        color = (text_color, bg_color)
        self.log(logging.INFO, message, ex, exc_info, color)

    def success(self, message: str, ex: Optional[Exception] = None, exc_info: bool = False, text_color: str = 'yellow', bg_color: str = ''):
        """
        Logs a success message with optional text and background colors.

        Args:
            message (str): The log message.
            ex (Optional[Exception], optional): The exception object. Defaults to None.
            exc_info (bool, optional): Whether to include exception info. Defaults to False.
            text_color (str, optional): Text color. Defaults to "yellow".
            bg_color (str, optional): Background color. Defaults to "".
        """
        color = (text_color, bg_color)
        self.log(logging.INFO, message, ex, exc_info, color)

    def warning(self, message: str, ex: Optional[Exception] = None, exc_info: bool = False, text_color: str = 'light_red', bg_color: str = ''):
        """
        Logs a warning message with optional text and background colors.

        Args:
            message (str): The log message.
            ex (Optional[Exception], optional): The exception object. Defaults to None.
            exc_info (bool, optional): Whether to include exception info. Defaults to False.
            text_color (str, optional): Text color. Defaults to "light_red".
            bg_color (str, optional): Background color. Defaults to "".
        """
        color = (text_color, bg_color)
        self.log(logging.WARNING, message, ex, exc_info, color)

    def debug(self, message: str, ex: Optional[Exception] = None, exc_info: bool = True, text_color: str = 'cyan', bg_color: str = ''):
        """
        Logs a debug message with optional text and background colors.

        Args:
            message (str): The log message.
            ex (Optional[Exception], optional): The exception object. Defaults to None.
            exc_info (bool, optional): Whether to include exception info. Defaults to True.
            text_color (str, optional): Text color. Defaults to "cyan".
            bg_color (str, optional): Background color. Defaults to "".
        """
        color = (text_color, bg_color)
        self.log(logging.DEBUG, message, ex, exc_info, color)

    def exception(self, message: str, ex: Optional[Exception] = None, exc_info: bool = True, text_color: str = 'cyan', bg_color: str = 'light_gray'):
        """
        Logs an exception message with optional text and background colors.

        Args:
            message (str): The log message.
            ex (Optional[Exception], optional): The exception object. Defaults to None.
            exc_info (bool, optional): Whether to include exception info. Defaults to True.
            text_color (str, optional): Text color. Defaults to "cyan".
            bg_color (str, optional): Background color. Defaults to "light_gray".
        """
        color = (text_color, bg_color)
        self.log(logging.ERROR, message, ex, exc_info, color) #Log as error

    def error(self, message: str, ex: Optional[Exception] = None, exc_info: bool = True, text_color: str = 'red', bg_color: str = ''):
        """
        Logs an error message with optional text and background colors.

        Args:
            message (str): The log message.
            ex (Optional[Exception], optional): The exception object. Defaults to None.
            exc_info (bool, optional): Whether to include exception info. Defaults to True.
            text_color (str, optional): Text color. Defaults to "red".
            bg_color (str, optional): Background color. Defaults to "".
        """
        color = (text_color, bg_color)
        self.log(logging.ERROR, message, ex, exc_info, color)

    def critical(self, message: str, ex: Optional[Exception] = None, exc_info: bool = True, text_color: str = 'red', bg_color: str = 'white'):
        """
        Logs a critical message with optional text and background colors.

        Args:
            message (str): The log message.
            ex (Optional[Exception], optional): The exception object. Defaults to None.
            exc_info (bool, optional): Whether to include exception info. Defaults to True.
            text_color (str, optional): Text color. Defaults to "red".
            bg_color (str, optional): Background color. Defaults to "white".
        """
        color = (text_color, bg_color)
        self.log(logging.CRITICAL, message, ex, exc_info, color)


# Initialize logger with file paths
# logger = Logger(info_log_path='info.log', debug_log_path='debug.log', errors_log_path='errors.log', json_log_path='log.json')
logger: Logger = Logger()
```