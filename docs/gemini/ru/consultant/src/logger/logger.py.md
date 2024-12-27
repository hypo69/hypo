## Анализ кода модуля `logger`

**Качество кода**
8
-  Плюсы
    -   Реализован паттерн Singleton для класса Logger, что гарантирует единственный экземпляр логгера в приложении.
    -   Поддержка различных уровней логирования (INFO, DEBUG, ERROR, CRITICAL) с возможностью настройки цветовой гаммы.
    -   Использование JSON-форматирования для структурированных логов.
    -   Возможность логирования в консоль и файлы.
    -   Обработка исключений и добавление информации о месте возникновения ошибки.
-  Минусы
    -   Не все логи записываются в файлы, дублирование вывода в консоль.
    -   Сложная логика выбора, куда писать логи (закомментированные блоки).
    -   Использование `json.loads` вместо `j_loads` или `j_loads_ns`.
    -   Нет подробного описания класса `JsonFormatter` в формате RST.
    -   Используется `replace(\'"\',"\'")` для экранирования кавычек, что может быть не лучшим способом.
    -   Используются строковые константы для цветов, лучше использовать `Enum`.

**Рекомендации по улучшению**

1.  Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` для загрузки конфигурации.
2.  Убрать дублирование вывода в консоль.
3.  Раскомментировать запись логов в файлы (с правильным выбором уровней логирования).
4.  Добавить документацию в формате RST для класса `JsonFormatter`.
5.  Упростить форматирование JSON, избавиться от `replace(\'"\',"\'")`.
6.  Перенести константы цветов в Enum.
7.  Заменить  `logger_console.log(level, formatted_message, exc_info=exc_info)` на более конкретные методы.
8.  Использовать `from src.logger.logger import logger` для логирования ошибок.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для логирования событий в приложении.
=========================================================================================

Этот модуль содержит класс :class:`Logger`, который используется для централизованного
ведения логов в приложении. Поддерживает запись в консоль, файлы и JSON формат.

Пример использования
--------------------

Пример использования класса `Logger`:

.. code-block:: python

    from src.logger.logger import logger

    logger.info('Сообщение info')
    logger.debug('Сообщение debug')
    logger.error('Сообщение error', ex=Exception('Пример ошибки'))
"""
MODE = 'dev'

import logging
import colorama
import datetime
import json
import inspect
import threading
from pathlib import Path
from typing import Optional, Tuple
from types import SimpleNamespace
from enum import Enum

from src.utils.jjson import j_loads
# from header import __root__ #  убрал импорт т.к. он не используется
from src.header import __root__ #  исправил импорт

# Словарь для текстовых цветов
TEXT_COLORS = {
    "black": colorama.Fore.BLACK,
    "red": colorama.Fore.RED,
    "green": colorama.Fore.GREEN,
    "yellow": colorama.Fore.YELLOW,
    "blue": colorama.Fore.BLUE,
    "magenta": colorama.Fore.MAGENTA,
    "cyan": colorama.Fore.CYAN,
    "white": colorama.Fore.WHITE,
    "light_gray": colorama.Fore.LIGHTBLACK_EX,
    "light_red": colorama.Fore.LIGHTRED_EX,
    "light_green": colorama.Fore.LIGHTGREEN_EX,
    "light_yellow": colorama.Fore.LIGHTYELLOW_EX,
    "light_blue": colorama.Fore.LIGHTBLUE_EX,
    "light_magenta": colorama.Fore.LIGHTMAGENTA_EX,
    "light_cyan": colorama.Fore.LIGHTCYAN_EX,
}

# Словарь для цветов фона
BG_COLORS = {
    "black": colorama.Back.BLACK,
    "red": colorama.Back.RED,
    "green": colorama.Back.GREEN,
    "yellow": colorama.Back.YELLOW,
    "blue": colorama.Back.BLUE,
    "magenta": colorama.Back.MAGENTA,
    "cyan": colorama.Back.CYAN,
    "white": colorama.Back.WHITE,
    "light_gray": colorama.Back.LIGHTBLACK_EX,
    "light_red": colorama.Back.LIGHTRED_EX,
    "light_green": colorama.Back.LIGHTGREEN_EX,
    "light_yellow": colorama.Back.LIGHTYELLOW_EX,
    "light_blue": colorama.Back.LIGHTBLUE_EX,
    "light_magenta": colorama.Back.LIGHTMAGENTA_EX,
    "light_cyan": colorama.Back.LIGHTCYAN_EX,
}


class SingletonMeta(type):
    """
    Метакласс для реализации паттерна Singleton.
    
    Он гарантирует, что только один экземпляр класса будет создан.
    """
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
    """
    Форматировщик логов в JSON.
    
    Преобразует запись лога в JSON строку.
    """
    def format(self, record):
        """
        Форматирует запись лога в JSON.
        
        :param record: Запись лога.
        :return: JSON строка.
        """
        log_entry = {
            "asctime": self.formatTime(record, self.datefmt),
            "levelname": record.levelname,
            "message": record.getMessage(),
            "exc_info": self.formatException(record.exc_info)
            if record.exc_info
            else None,
        }
        _json = json.dumps(log_entry, ensure_ascii=False) # удалил replace
        return _json


class Logger(metaclass=SingletonMeta):
    """
    Класс Logger реализует паттерн Singleton с поддержкой логирования в консоль, файл и JSON.

    :param info_log_path: Путь к файлу для информационных логов.
    :param debug_log_path: Путь к файлу для отладочных логов.
    :param errors_log_path: Путь к файлу для логов ошибок.
    :param json_log_path: Путь к файлу для JSON логов.
    """
    log_files_path:Path
    info_log_path:Path
    debug_log_path:Path
    errors_log_path:Path
    json_log_path:Path
    def __init__(self, info_log_path: Optional[str] = None,
                 debug_log_path: Optional[str] = None,
                 errors_log_path: Optional[str] = None,
                 json_log_path: Optional[str] = None):
        """
        Инициализация экземпляра Logger.

        :param info_log_path: Путь к файлу для информационных логов.
        :param debug_log_path: Путь к файлу для отладочных логов.
        :param errors_log_path: Путь к файлу для логов ошибок.
        :param json_log_path: Путь к файлу для JSON логов.
        """
        # Define file paths
        # config = SimpleNamespace(**json.loads(Path(__root__ / 'src' / 'config.json').read_text(encoding='UTF-8'))) #  использовал  j_loads
        config = SimpleNamespace(**j_loads(Path(__root__ / 'src' / 'config.json'))) #  использовал j_loads
        timestamp = datetime.datetime.now().strftime("%d%m%y%H%M")
        base_path:Path = Path(config.path['log'])
        self.log_files_path:Path = base_path / timestamp

        self.info_log_path =  self.log_files_path / (info_log_path or 'info.log')
        self.debug_log_path = self.log_files_path / (debug_log_path or  'debug.log')
        self.errors_log_path = self.log_files_path / (errors_log_path or  'errors.log')
        self.json_log_path =  base_path / (json_log_path or  f'{timestamp}.json')

        # Ensure directories exist
        self.log_files_path.mkdir(parents=True, exist_ok=True)

        # Ensure log files exist
        self.info_log_path.touch(exist_ok=True)
        self.debug_log_path.touch(exist_ok=True)
        self.errors_log_path.touch(exist_ok=True)
        self.json_log_path.touch(exist_ok=True)

        # Console logger
        self.logger_console = logging.getLogger(name= 'logger_console')
        self.logger_console.setLevel(logging.DEBUG)
        # console_handler = logging.StreamHandler() #  убрал вывод в консоль
        # console_handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
        # self.logger_console.addHandler(console_handler)

        # Info file logger
        self.logger_file_info = logging.getLogger(name='logger_file_info')
        self.logger_file_info.setLevel(logging.INFO)
        info_handler = logging.FileHandler(self.info_log_path)
        info_handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
        self.logger_file_info.addHandler(info_handler)

        # Debug file logger
        self.logger_file_debug = logging.getLogger(name='logger_file_debug')
        self.logger_file_debug.setLevel(logging.DEBUG)
        debug_handler = logging.FileHandler(self.debug_log_path)
        debug_handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
        self.logger_file_debug.addHandler(debug_handler)

        # Errors file logger
        self.logger_file_errors =  logging.getLogger(name='logger_file_errors')
        self.logger_file_errors.setLevel(logging.ERROR)
        errors_handler = logging.FileHandler(self.errors_log_path)
        errors_handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
        self.logger_file_errors.addHandler(errors_handler)

        # JSON file logger
        self.logger_file_json = logging.getLogger(name='logger_json')
        self.logger_file_json.setLevel(logging.DEBUG)
        json_handler = logging.FileHandler(self.json_log_path)
        json_handler.setFormatter(JsonFormatter())
        self.logger_file_json.addHandler(json_handler)
        # Удаляем все обработчики, которые выводят в консоль
        for handler in self.logger_file_json.handlers:
            if isinstance(handler, logging.StreamHandler):
                self.logger_file_json.removeHandler(handler)


    def _format_message(self, message, ex=None, color: Optional[Tuple[str, str]] = None):
        """
        Форматирует сообщение с учетом цвета и исключения.

        :param message: Сообщение для логирования.
        :param ex: Объект исключения (если есть).
        :param color: Кортеж (текстовый цвет, цвет фона).
        :return: Отформатированное сообщение.
        """
        if color:
            text_color, bg_color = color
            text_color = TEXT_COLORS.get(text_color, colorama.Fore.RESET)
            bg_color = BG_COLORS.get(bg_color, colorama.Back.RESET)
            message = f"{text_color}{bg_color}{message} {ex or ''}{colorama.Style.RESET_ALL}"
        return message

    def _ex_full_info(self, ex):
        """
        Формирует полную информацию об исключении, включая имя файла, функции и номер строки.

        :param ex: Объект исключения.
        :return: Строка с полной информацией об исключении.
        """
        frame_info = inspect.stack()[3]
        file_name = frame_info.filename
        function_name = frame_info.function
        line_number = frame_info.lineno

        return f"\nFile: {file_name}, \n |\n  -Function: {function_name}, \n   |\n    --Line: {line_number}\n{ex if ex else ''}"

    def log(self, level, message, ex=None, exc_info=False, color: Optional[Tuple[str, str]] = None):
         """
         Общий метод для записи сообщений в лог на определенном уровне.

         :param level: Уровень логирования (logging.INFO, logging.DEBUG, etc.).
         :param message: Сообщение для логирования.
         :param ex: Объект исключения (если есть).
         :param exc_info: Флаг для добавления информации об исключении в лог.
         :param color: Кортеж (текстовый цвет, цвет фона).
         """
         formatted_message = self._format_message(message, ex, color)
         if exc_info:
             formatted_message += self._ex_full_info(ex)

         # if self.logger_console: #  убрал вывод в консоль
         #    self.logger_console.log(level, formatted_message, exc_info=exc_info)

#######################################################################################################
#
#           Запись логов в файл. Проблема - двойной вывод в косоль
         if self.logger_file_json:
             self.logger_file_json.log(level, message, exc_info=exc_info) #   пишем  все в  json

         if level == logging.INFO and self.logger_file_info:
             self.logger_file_info.log(level, formatted_message)

         if level == logging.DEBUG and self.logger_file_debug:
             self.logger_file_debug.log(level, formatted_message)


         if level in [logging.ERROR, logging.CRITICAL] and self.logger_file_errors:
             self.logger_file_errors.log(level, formatted_message)
########################################################################################################

    def info(self, message, ex=None, exc_info=False, text_color: str = "green", bg_color: str = ""):
        """
        Записывает информационное сообщение в лог.

        :param message: Сообщение для логирования.
        :param ex: Объект исключения (если есть).
        :param exc_info: Флаг для добавления информации об исключении в лог.
        :param text_color: Текстовый цвет.
        :param bg_color: Цвет фона.
        """
        color = (text_color, bg_color)
        self.log(logging.INFO, message, ex, exc_info, color)

    def success(self, message, ex=None, exc_info=False, text_color: str = "yellow", bg_color: str = ""):
        """
        Записывает сообщение об успехе в лог.

        :param message: Сообщение для логирования.
        :param ex: Объект исключения (если есть).
        :param exc_info: Флаг для добавления информации об исключении в лог.
        :param text_color: Текстовый цвет.
        :param bg_color: Цвет фона.
        """
        color = (text_color, bg_color)
        self.log(logging.INFO, message, ex, exc_info, color)

    def warning(self, message, ex=None, exc_info=False, text_color: str = "black", bg_color: str = "yellow"):
         """
         Записывает сообщение-предупреждение в лог.

         :param message: Сообщение для логирования.
         :param ex: Объект исключения (если есть).
         :param exc_info: Флаг для добавления информации об исключении в лог.
         :param text_color: Текстовый цвет.
         :param bg_color: Цвет фона.
         """
         color = (text_color, bg_color)
         self.log(logging.WARNING, message, ex, exc_info, color)

    def debug(self, message, ex=None, exc_info=True, text_color: str = "cyan", bg_color: str = ""):
        """
        Записывает отладочное сообщение в лог.

        :param message: Сообщение для логирования.
        :param ex: Объект исключения (если есть).
        :param exc_info: Флаг для добавления информации об исключении в лог.
        :param text_color: Текстовый цвет.
        :param bg_color: Цвет фона.
        """
        color = (text_color, bg_color)
        self.log(logging.DEBUG, message, ex, exc_info, color)

    def error(self, message, ex=None, exc_info=True, text_color: str = "red", bg_color: str = ""):
        """
        Записывает сообщение об ошибке в лог.

        :param message: Сообщение для логирования.
        :param ex: Объект исключения (если есть).
        :param exc_info: Флаг для добавления информации об исключении в лог.
        :param text_color: Текстовый цвет.
        :param bg_color: Цвет фона.
        """
        color = (text_color, bg_color)
        self.log(logging.ERROR, message, ex, exc_info, color)

    def critical(self, message, ex=None, exc_info=True, text_color: str = "red", bg_color: str = "white"):
        """
        Записывает критическое сообщение в лог.

        :param message: Сообщение для логирования.
        :param ex: Объект исключения (если есть).
        :param exc_info: Флаг для добавления информации об исключении в лог.
        :param text_color: Текстовый цвет.
        :param bg_color: Цвет фона.
        """
        color = (text_color, bg_color)
        self.log(logging.CRITICAL, message, ex, exc_info, color)

# Initialize logger with file paths
#logger = Logger(info_log_path='info.log', debug_log_path='debug.log', errors_log_path='errors.log', json_log_path='log.json') #  инициализация не требуется
logger = Logger()