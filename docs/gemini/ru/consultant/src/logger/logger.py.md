# Анализ кода модуля `logger.py`

**Качество кода**
8
- Плюсы
    - Код хорошо структурирован, используется паттерн Singleton для класса `Logger`.
    - Применяется `colorama` для цветного вывода в консоль.
    - Логирование реализовано с различными уровнями (INFO, DEBUG, ERROR, CRITICAL).
    - Имеется кастомный JSON-форматтер для логов.
    - Присутствует форматирование сообщений с возможностью добавления цветов.
    - Определены константы для цветов текста и фона.
    - Используется `Path` для работы с путями, что является хорошей практикой.
    - Исключения обрабатываются и форматируются с дополнительной информацией (имя файла, функции, строка).
- Минусы
    -  Отсутствуют docstring для модуля, классов и методов, что затрудняет понимание кода.
    -  Часть кода закомментирована, что говорит о незаконченной работе.
    -  Использование `json.loads`  вместо `j_loads_ns` или `j_loads` .
    -  Не все методы logger выводят в файл.
    -  Не везде используется `logger.error` для обработки ошибок.
    -  Не все импорты используются.

**Рекомендации по улучшению**

1.  Добавить docstring для модуля, классов и методов в формате reStructuredText.
2.  Заменить `json.loads` на `j_loads` или `j_loads_ns` для чтения конфигурационных файлов.
3.  Раскомментировать код записи логов в файл.
4.  Вместо закомментированного кода,  реализовать вывод логов всех уровней в файлы.
5.  Использовать `logger.error` для обработки исключений, убрав избыточные `try-except` блоки.
6.  Удалить неиспользуемые импорты.
7.  Удалить закомментированный код.
8.  Использовать `from src.logger.logger import logger` для логирования ошибок.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль :mod:`src.logger.logger`
=========================================================================================

Этот модуль определяет класс :class:`Logger`, который используется для логирования сообщений в консоль, файлы и JSON формат.
Он также реализует паттерн Singleton для обеспечения единственного экземпляра логгера в приложении.
Поддерживает форматирование сообщений, включая цветной вывод и добавление информации об исключениях.

Пример использования
--------------------

Пример использования класса `Logger`:

.. code-block:: python

    from src.logger.logger import logger
    
    logger.info('Сообщение информационного уровня')
    logger.debug('Сообщение отладочного уровня', exc_info=True)
    try:
        raise ValueError('Пример ошибки')
    except Exception as e:
       logger.error('Произошла ошибка', ex=e)
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

from src.utils.jjson import j_loads_ns
from header import __root__


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

    Этот метакласс гарантирует, что только один экземпляр класса будет создан.
    """

    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        """
        Возвращает единственный экземпляр класса.
        
        Если экземпляр класса ещё не создан, он создаётся.
        
        :param args: Позиционные аргументы для конструктора класса.
        :param kwargs: Именованные аргументы для конструктора класса.
        :return: Единственный экземпляр класса.
        """
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    instance = super().__call__(*args, **kwargs)
                    cls._instances[cls] = instance
        return cls._instances[cls]


class JsonFormatter(logging.Formatter):
    """
    Кастомный форматтер для логирования в JSON формате.
    
    Преобразует запись лога в JSON строку.
    """

    def format(self, record):
        """
        Форматирует запись лога в JSON.
        
        :param record: Запись лога для форматирования.
        :return: JSON строка представления записи лога.
        """
        log_entry = {
            "asctime": self.formatTime(record, self.datefmt),
            "levelname": record.levelname,
            "message": record.getMessage().replace('"', "'"),
            "exc_info": self.formatException(record.exc_info)
            if record.exc_info
            else None,
        }
        _json = json.dumps(log_entry, ensure_ascii=False)
        return _json


class Logger(metaclass=SingletonMeta):
    """
    Класс Logger реализующий паттерн Singleton.
    
    Предоставляет функциональность для логирования в консоль, файлы и JSON формат.
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
        Инициализирует экземпляр Logger.
        
        Настраивает пути к файлам логов, создает каталоги и файлы, а также настраивает обработчики логов.

        :param info_log_path: Путь к файлу для INFO логов.
        :param debug_log_path: Путь к файлу для DEBUG логов.
        :param errors_log_path: Путь к файлу для ERROR логов.
        :param json_log_path: Путь к файлу для JSON логов.
        """
        # Определяет пути к файлам
        config = SimpleNamespace(**j_loads_ns(Path(__root__ / 'src' / 'config.json'))) # заменен json.loads на j_loads_ns
        timestamp = datetime.datetime.now().strftime("%d%m%y%H%M")
        base_path:Path = Path(config.path['log'])  
        self.log_files_path:Path = base_path / timestamp 

        self.info_log_path =  self.log_files_path / (info_log_path or 'info.log')
        self.debug_log_path = self.log_files_path / (debug_log_path or  'debug.log')
        self.errors_log_path = self.log_files_path / (errors_log_path or  'errors.log')
        self.json_log_path =  base_path / (json_log_path or  f'{timestamp}.json')

        # Создаёт директории
        self.log_files_path.mkdir(parents=True, exist_ok=True)

        # Создаёт файлы логов
        self.info_log_path.touch(exist_ok=True)
        self.debug_log_path.touch(exist_ok=True)
        self.errors_log_path.touch(exist_ok=True)
        self.json_log_path.touch(exist_ok=True)

        # Настраивает логгер консоли
        self.logger_console = logging.getLogger(name= 'logger_console')
        self.logger_console.setLevel(logging.DEBUG)


        # Настраивает файловый логгер для INFO
        self.logger_file_info = logging.getLogger(name='logger_file_info')
        self.logger_file_info.setLevel(logging.INFO)
        info_handler = logging.FileHandler(self.info_log_path)
        info_handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
        self.logger_file_info.addHandler(info_handler)

        # Настраивает файловый логгер для DEBUG
        self.logger_file_debug = logging.getLogger(name='logger_file_debug')
        self.logger_file_debug.setLevel(logging.DEBUG)
        debug_handler = logging.FileHandler(self.debug_log_path)
        debug_handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
        self.logger_file_debug.addHandler(debug_handler)

        # Настраивает файловый логгер для ERROR
        self.logger_file_errors =  logging.getLogger(name='logger_file_errors')
        self.logger_file_errors.setLevel(logging.ERROR)
        errors_handler = logging.FileHandler(self.errors_log_path)
        errors_handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
        self.logger_file_errors.addHandler(errors_handler)

        # Настраивает файловый логгер для JSON
        self.logger_file_json = logging.getLogger(name='logger_json')
        self.logger_file_json.setLevel(logging.DEBUG)
        json_handler = logging.FileHandler(self.json_log_path)
        json_handler.setFormatter(JsonFormatter())  # Использует кастомный форматтер
        self.logger_file_json.addHandler(json_handler)
        # Удаляет все обработчики, которые выводят в консоль
        for handler in self.logger_file_json.handlers:
            if isinstance(handler, logging.StreamHandler):
                self.logger_file_json.removeHandler(handler)

    def _format_message(self, message, ex=None, color: Optional[Tuple[str, str]] = None):
        """
        Форматирует сообщение с опциональным цветом и информацией об исключении.
        
        :param message: Сообщение для форматирования.
        :param ex: Исключение, которое нужно добавить в сообщение.
        :param color: Кортеж с цветом текста и фона.
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
        Возвращает полную информацию об исключении.
        
        Включает имя файла, имя функции и номер строки.

        :param ex: Исключение, информацию о котором нужно получить.
        :return: Полная информация об исключении.
        """
        frame_info = inspect.stack()[3]
        file_name = frame_info.filename
        function_name = frame_info.function
        line_number = frame_info.lineno

        return f"\nFile: {file_name}, \n |\n  -Function: {function_name}, \n   |\n    --Line: {line_number}\n{ex if ex else ''}"

    def log(self, level, message, ex=None, exc_info=False, color: Optional[Tuple[str, str]] = None):
        """
        Общий метод для записи сообщений в лог.
        
        Выводит сообщения на указанном уровне с возможностью добавления цвета и информации об исключении.
        
        :param level: Уровень логирования.
        :param message: Сообщение для записи.
        :param ex: Исключение, информацию о котором нужно добавить.
        :param exc_info: Флаг, указывающий, нужно ли добавлять информацию об исключении.
        :param color: Кортеж с цветом текста и фона.
        """
        formatted_message = self._format_message(message, ex, color)
        if exc_info:
            formatted_message += self._ex_full_info(ex)
        if self.logger_console:
            self.logger_console.log(level, formatted_message, exc_info=exc_info)

        if self.logger_file_json: # Вывод в json файл
            self.logger_file_json.log(level, message, exc_info=exc_info)
        if level == logging.INFO and self.logger_file_info:
            self.logger_file_info.log(level, formatted_message)
        if level == logging.DEBUG and self.logger_file_debug:
             self.logger_file_debug.log(level, formatted_message)
        if level in [logging.ERROR, logging.CRITICAL] and self.logger_file_errors:
            self.logger_file_errors.log(level, formatted_message)

    def info(self, message, ex=None, exc_info=False, text_color: str = "green", bg_color: str = ""):
        """
        Записывает информационное сообщение в лог.

        :param message: Сообщение для записи.
        :param ex: Исключение, информацию о котором нужно добавить.
        :param exc_info: Флаг, указывающий, нужно ли добавлять информацию об исключении.
        :param text_color: Цвет текста.
        :param bg_color: Цвет фона.
        """
        color = (text_color, bg_color)
        self.log(logging.INFO, message, ex, exc_info, color)

    def success(self, message, ex=None, exc_info=False, text_color: str = "yellow", bg_color: str = ""):
        """
        Записывает сообщение об успехе в лог.
        
        :param message: Сообщение для записи.
        :param ex: Исключение, информацию о котором нужно добавить.
        :param exc_info: Флаг, указывающий, нужно ли добавлять информацию об исключении.
        :param text_color: Цвет текста.
        :param bg_color: Цвет фона.
        """
        color = (text_color, bg_color)
        self.log(logging.INFO, message, ex, exc_info, color)

    def warning(self, message, ex=None, exc_info=False, text_color: str = "black", bg_color: str = "yellow"):
        """
        Записывает предупреждающее сообщение в лог.
        
        :param message: Сообщение для записи.
        :param ex: Исключение, информацию о котором нужно добавить.
        :param exc_info: Флаг, указывающий, нужно ли добавлять информацию об исключении.
        :param text_color: Цвет текста.
        :param bg_color: Цвет фона.
        """
        color = (text_color, bg_color)
        self.log(logging.WARNING, message, ex, exc_info, color)

    def debug(self, message, ex=None, exc_info=True, text_color: str = "cyan", bg_color: str = ""):
        """
        Записывает отладочное сообщение в лог.
        
        :param message: Сообщение для записи.
        :param ex: Исключение, информацию о котором нужно добавить.
        :param exc_info: Флаг, указывающий, нужно ли добавлять информацию об исключении.
        :param text_color: Цвет текста.
        :param bg_color: Цвет фона.
        """
        color = (text_color, bg_color)
        self.log(logging.DEBUG, message, ex, exc_info, color)

    def error(self, message, ex=None, exc_info=True, text_color: str = "red", bg_color: str = ""):
        """
        Записывает сообщение об ошибке в лог.
        
        :param message: Сообщение для записи.
        :param ex: Исключение, информацию о котором нужно добавить.
        :param exc_info: Флаг, указывающий, нужно ли добавлять информацию об исключении.
        :param text_color: Цвет текста.
        :param bg_color: Цвет фона.
        """
        color = (text_color, bg_color)
        self.log(logging.ERROR, message, ex, exc_info, color)

    def critical(self, message, ex=None, exc_info=True, text_color: str = "red", bg_color: str = "white"):
        """
        Записывает критическое сообщение в лог.
        
        :param message: Сообщение для записи.
        :param ex: Исключение, информацию о котором нужно добавить.
        :param exc_info: Флаг, указывающий, нужно ли добавлять информацию об исключении.
        :param text_color: Цвет текста.
        :param bg_color: Цвет фона.
        """
        color = (text_color, bg_color)
        self.log(logging.CRITICAL, message, ex, exc_info, color)

# Инициализация логгера
logger = Logger()
```