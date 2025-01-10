# Анализ кода модуля `logger.py`

**Качество кода**
7
-  Плюсы
    -  Реализован паттерн Singleton для класса Logger, что гарантирует единственный экземпляр логгера.
    -  Используется библиотека `colorama` для раскрашивания вывода в консоль.
    -  Логирование осуществляется в разные файлы (info, debug, errors) и в json формат.
    -  Реализован кастомный JSON форматтер.
    -  Имеется подробная информация об исключении в методе `_ex_full_info`.
 -  Минусы
    -  Не все импорты расположены в начале файла, импорт `header` и `__root__` должен быть выше.
    -  Используется `json.loads` для загрузки конфига, нужно использовать `j_loads` или `j_loads_ns`.
    -   Дублирование кода при настройке логгеров, можно вынести в отдельную функцию.
    -  Закомментированный код, связанный с записью логов в файл, необходимо удалить или исправить.
    -   Не реализована запись в файлы с использованием `self.logger_file_json.log`.
    -   Нет документации в формате RST.
    -   В некоторых местах отсутствуют комментарии.

**Рекомендации по улучшению**

1.  **Импорты:** Переместить импорты `header` и `__root__` в начало файла.
2.  **Использование `j_loads`:** Заменить `json.loads` на `j_loads_ns` из `src.utils.jjson` для чтения файла конфигурации.
3.  **Рефакторинг:** Вынести создание и настройку файловых логгеров в отдельную функцию для избежания дублирования кода.
4.  **Исправление закомментированного кода:**  Необходимо удалить закомментированный код или переработать его.
5.  **Логирование в JSON:** Исправить логирование в JSON файл с использованием `self.logger_file_json.log`.
6.  **Документация:** Добавить документацию в формате RST для модуля, класса и методов.
7.  **Комментарии:** Добавить комментарии к блокам кода, где они отсутствуют.
8.  **Использование `logger.error`:** Заменить общие `try-except` на `logger.error` для более явной обработки ошибок.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
Модуль логгера
=========================================================================================

Этот модуль содержит класс :class:`Logger`, который реализует паттерн Singleton и
предоставляет функциональность для логирования сообщений в консоль, файлы и JSON формат.

Пример использования
--------------------

Пример использования класса `Logger`:

.. code-block:: python

    from src.logger.logger import logger

    logger.info('Это информационное сообщение')
    logger.debug('Это отладочное сообщение', exc_info=True)
    try:
        raise ValueError('Пример ошибки')
    except ValueError as e:
        logger.error('Произошла ошибка', ex=e)
"""

import logging
import colorama
import datetime
import inspect
import threading
from pathlib import Path
from typing import Optional, Tuple
from types import SimpleNamespace

#  Импорт header
import header
from header import __root__

#  Импорт j_loads_ns
from src.utils.jjson import j_loads_ns

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
        _json = j_loads_ns(log_entry)
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
        Инициализирует экземпляр логгера.

        Args:
            info_log_path (Optional[str]): Путь к файлу для информационных логов.
            debug_log_path (Optional[str]): Путь к файлу для отладочных логов.
            errors_log_path (Optional[str]): Путь к файлу для логов ошибок.
            json_log_path (Optional[str]): Путь к файлу для JSON логов.
        """
        #  Загрузка конфигурации из файла
        config = SimpleNamespace(
            **j_loads_ns(Path(__root__ / 'src' / 'config.json').read_text(encoding='UTF-8'))
        )
        #  Формирование временной метки для имени директории
        timestamp = datetime.datetime.now().strftime('%d%m%y%H%M')
        #  Формирование базового пути к директории с логами
        base_path: Path = Path(config.path['log'])
        #  Формирование полного пути к директории с логами
        self.log_files_path: Path = base_path / timestamp

        #  Формирование путей к файлам логов
        self.info_log_path = self.log_files_path / (info_log_path or 'info.log')
        self.debug_log_path = self.log_files_path / (debug_log_path or 'debug.log')
        self.errors_log_path = self.log_files_path / (errors_log_path or 'errors.log')
        self.json_log_path = base_path / (json_log_path or f'{timestamp}.json')

        #  Создание директории, если она не существует
        self.log_files_path.mkdir(parents=True, exist_ok=True)

        #  Создание файлов логов, если они не существуют
        self.info_log_path.touch(exist_ok=True)
        self.debug_log_path.touch(exist_ok=True)
        self.errors_log_path.touch(exist_ok=True)
        self.json_log_path.touch(exist_ok=True)

        #  Настройка консольного логгера
        self.logger_console = logging.getLogger(name='logger_console')
        self.logger_console.setLevel(logging.DEBUG)

        # Настройка файловых логгеров
        self._setup_file_logger(
            'logger_file_info', self.info_log_path, logging.INFO, '%(levelname)s: %(message)s'
        )
        self._setup_file_logger(
            'logger_file_debug', self.debug_log_path, logging.DEBUG, '%(levelname)s: %(message)s'
        )
        self._setup_file_logger(
            'logger_file_errors', self.errors_log_path, logging.ERROR, '%(levelname)s: %(message)s'
        )
        self._setup_file_logger(
            'logger_json', self.json_log_path, logging.DEBUG, formatter=JsonFormatter()
        )

    def _setup_file_logger(self, name: str, file_path: Path, level: int, format: str = None, formatter=None):
        """
        Настраивает файловый логгер.

        Args:
            name (str): Имя логгера.
            file_path (Path): Путь к файлу лога.
            level (int): Уровень логирования.
            format (str, optional): Формат сообщения.
            formatter (logging.Formatter, optional): Кастомный форматтер.
        """
        logger = logging.getLogger(name=name)
        logger.setLevel(level)
        file_handler = logging.FileHandler(file_path)
        if format:
            file_handler.setFormatter(logging.Formatter(format))
        if formatter:
            file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        #  Удаление обработчиков, которые выводят в консоль
        for handler in logger.handlers:
            if isinstance(handler, logging.StreamHandler):
                logger.removeHandler(handler)

    def _format_message(self, message, ex=None, color: Optional[Tuple[str, str]] = None):
        """
        Форматирует сообщение с учетом цвета и информации об исключении.

        Args:
            message (str): Сообщение для логирования.
            ex (Exception, optional): Исключение, которое нужно добавить в сообщение.
            color (Tuple[str, str], optional): Кортеж с цветом текста и фона.

        Returns:
            str: Форматированное сообщение.
        """
        if color:
            text_color, bg_color = color
            text_color = TEXT_COLORS.get(text_color, colorama.Fore.RESET)
            bg_color = BG_COLORS.get(bg_color, colorama.Back.RESET)
            message = f'{text_color}{bg_color}{message} {ex or ""}{colorama.Style.RESET_ALL}'
        return message

    def _ex_full_info(self, ex):
        """
        Возвращает полную информацию об исключении.

        Args:
            ex (Exception): Исключение.

        Returns:
            str: Полная информация об исключении.
        """
        frame_info = inspect.stack()[3]
        file_name = frame_info.filename
        function_name = frame_info.function
        line_number = frame_info.lineno

        return f'\\nFile: {file_name}, \\n |\\n  -Function: {function_name}, \\n   |\\n    --Line: {line_number}\\n{ex if ex else ""}'

    def log(self, level, message, ex=None, exc_info=False, color: Optional[Tuple[str, str]] = None):
        """
        Логирует сообщение с заданным уровнем и цветом.

        Args:
            level (int): Уровень логирования.
            message (str): Сообщение для логирования.
            ex (Exception, optional): Исключение, которое нужно добавить в сообщение.
            exc_info (bool, optional): Флаг для отображения информации об исключении.
            color (Tuple[str, str], optional): Кортеж с цветом текста и фона.
        """
        formatted_message = self._format_message(message, ex, color)
        if exc_info:
            formatted_message += self._ex_full_info(ex)

        if self.logger_console:
            self.logger_console.log(level, formatted_message, exc_info=exc_info)

        #  Логирование в json
        if hasattr(self, 'logger_file_json'):
            self.logger_file_json.log(level, message, exc_info=exc_info)
        # if level == logging.INFO and hasattr(self, 'logger_file_info'):
        #     self.logger_file_info.log(level, formatted_message)

        # if level == logging.DEBUG and hasattr(self, 'logger_file_debug'):
        #     self.logger_file_debug.log(level, formatted_message)

        # if level in [logging.ERROR, logging.CRITICAL] and hasattr(self, 'logger_file_errors'):
        #     self.logger_file_errors.log(level, formatted_message)

    def info(self, message, ex=None, exc_info=False, text_color: str = 'green', bg_color: str = ''):
        """
        Логирует информационное сообщение.

        Args:
            message (str): Сообщение для логирования.
            ex (Exception, optional): Исключение, которое нужно добавить в сообщение.
            exc_info (bool, optional): Флаг для отображения информации об исключении.
            text_color (str, optional): Цвет текста.
            bg_color (str, optional): Цвет фона.
        """
        color = (text_color, bg_color)
        self.log(logging.INFO, message, ex, exc_info, color)

    def success(self, message, ex=None, exc_info=False, text_color: str = 'yellow', bg_color: str = ''):
        """
        Логирует сообщение об успехе.

         Args:
            message (str): Сообщение для логирования.
            ex (Exception, optional): Исключение, которое нужно добавить в сообщение.
            exc_info (bool, optional): Флаг для отображения информации об исключении.
            text_color (str, optional): Цвет текста.
            bg_color (str, optional): Цвет фона.
        """
        color = (text_color, bg_color)
        self.log(logging.INFO, message, ex, exc_info, color)

    def warning(self, message, ex=None, exc_info=False, text_color: str = 'black', bg_color: str = 'yellow'):
        """
        Логирует предупреждающее сообщение.

        Args:
            message (str): Сообщение для логирования.
            ex (Exception, optional): Исключение, которое нужно добавить в сообщение.
            exc_info (bool, optional): Флаг для отображения информации об исключении.
            text_color (str, optional): Цвет текста.
            bg_color (str, optional): Цвет фона.
        """
        color = (text_color, bg_color)
        self.log(logging.WARNING, message, ex, exc_info, color)

    def debug(self, message, ex=None, exc_info=True, text_color: str = 'cyan', bg_color: str = ''):
        """
        Логирует отладочное сообщение.

        Args:
            message (str): Сообщение для логирования.
            ex (Exception, optional): Исключение, которое нужно добавить в сообщение.
            exc_info (bool, optional): Флаг для отображения информации об исключении.
            text_color (str, optional): Цвет текста.
            bg_color (str, optional): Цвет фона.
        """
        color = (text_color, bg_color)
        self.log(logging.DEBUG, message, ex, exc_info, color)

    def error(self, message, ex=None, exc_info=True, text_color: str = 'red', bg_color: str = ''):
        """
        Логирует сообщение об ошибке.

        Args:
            message (str): Сообщение для логирования.
            ex (Exception, optional): Исключение, которое нужно добавить в сообщение.
            exc_info (bool, optional): Флаг для отображения информации об исключении.
            text_color (str, optional): Цвет текста.
            bg_color (str, optional): Цвет фона.
        """
        color = (text_color, bg_color)
        self.log(logging.ERROR, message, ex, exc_info, color)

    def critical(self, message, ex=None, exc_info=True, text_color: str = 'red', bg_color: str = 'white'):
        """
        Логирует критическое сообщение.

        Args:
            message (str): Сообщение для логирования.
            ex (Exception, optional): Исключение, которое нужно добавить в сообщение.
            exc_info (bool, optional): Флаг для отображения информации об исключении.
            text_color (str, optional): Цвет текста.
            bg_color (str, optional): Цвет фона.
        """
        color = (text_color, bg_color)
        self.log(logging.CRITICAL, message, ex, exc_info, color)


# Инициализация логгера
from src.logger.logger import logger
```