# Анализ кода модуля `logger`

**Качество кода: 7/10**

-   **Плюсы**
    -   Реализован паттерн Singleton для класса `Logger`, что обеспечивает единственный экземпляр логгера в приложении.
    -   Поддерживается логирование в консоль, файлы и JSON-формате.
    -   Используются `colorama` для цветного вывода в консоль.
    -   Настроены разные уровни логирования (INFO, DEBUG, ERROR, CRITICAL).
    -   Добавлены методы `info`, `success`, `warning`, `debug`, `error`, `critical` для удобства логирования с различными уровнями и цветами.
    -   Используется кастомный `JsonFormatter` для логирования в JSON.
    -   Форматирование сообщений и исключений с указанием файла, функции и строки.

-   **Минусы**
    -   Некоторые части кода закомментированы.
    -   Использован `json.loads` для чтения файла конфигурации, вместо `j_loads` или `j_loads_ns`.
    -   Отсутствуют docstring для некоторых методов и класса.
    -   Имена переменных `_instances`, `_lock` не соответствуют общепринятым стандартам.
    -   Не все импорты соответствуют ранее обработанным файлам.
    -   Не используется `from src.logger.logger import logger` для логирования ошибок.
    -   Не используется `logger.error` для обработки ошибок.
    -   В текущей версии кода, логирование в файлы и в json отключено.

**Рекомендации по улучшению**

1.  Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` для загрузки конфигурации.
2.  Добавить docstring в формате RST для класса `Logger` и всех его методов.
3.  Использовать `from src.logger.logger import logger` для логирования ошибок.
4.  Вместо стандартных блоков `try-except`, предпочитать обработку ошибок с помощью `logger.error`.
5.  Раскомментировать и исправить логику записи логов в файл и в json
6.  Привести имена переменных, функций, импортов к единому стандарту с ранее обработанными файлами
7.  Улучшить читаемость и поддерживаемость кода, например, убрав закомментированные блоки кода.
8.  Использовать более конкретные имена для переменных: `_instances` -> `_instance`, `_lock` -> `_instance_lock`.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для настройки и управления логированием в приложении.
=========================================================================================

Этот модуль предоставляет класс :class:`Logger` для удобного логирования сообщений
в консоль, файлы и в формате JSON.
Использует паттерн Singleton, гарантирующий единственный экземпляр логгера в приложении.

Пример использования
--------------------

.. code-block:: python

    from src.logger.logger import logger

    logger.info("Это информационное сообщение")
    logger.debug("Это отладочное сообщение")
    logger.error("Это сообщение об ошибке", ex=ValueError("Пример ошибки"))
"""

MODE = 'dev'

import logging
import colorama
import datetime
import inspect
import threading
from pathlib import Path
from typing import Optional, Tuple
from types import SimpleNamespace

from src.utils.jjson import j_loads
from header import __root__
# from header import __root__ #  Исправлено импортирование

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

    _instance = {} #  Исправлено имя переменной
    _instance_lock = threading.Lock() #  Исправлено имя переменной

    def __call__(cls, *args, **kwargs):
        """
        Создает или возвращает существующий экземпляр класса.

        :param args: Позиционные аргументы для конструктора класса.
        :param kwargs: Именованные аргументы для конструктора класса.
        :return: Экземпляр класса.
        """
        if cls not in cls._instance:
            with cls._instance_lock:
                if cls not in cls._instance:
                    instance = super().__call__(*args, **kwargs)
                    cls._instance[cls] = instance
        return cls._instance[cls]


class JsonFormatter(logging.Formatter):
    """
    Кастомный форматтер для логирования в формате JSON.

    Преобразует запись лога в строку JSON.
    """

    def format(self, record):
        """
        Форматирует запись лога как JSON.

        :param record: Запись лога.
        :return: Строка JSON, представляющая запись лога.
        """
        log_entry = {
            "asctime": self.formatTime(record, self.datefmt),
            "levelname": record.levelname,
            "message": record.getMessage().replace('"', '\''),
            "exc_info": self.formatException(record.exc_info)
            if record.exc_info
            else None,
        }
        _json = j_loads(log_entry) #  Заменено json.dumps
        return _json


class Logger(metaclass=SingletonMeta):
    """
    Класс Logger реализующий паттерн Singleton с консольным, файловым и JSON-логированием.

     :ivar log_files_path: Путь к директории с лог файлами.
     :vartype log_files_path: Path
     :ivar info_log_path: Путь к файлу с информационными логами.
     :vartype info_log_path: Path
     :ivar debug_log_path: Путь к файлу с отладочными логами.
     :vartype debug_log_path: Path
     :ivar errors_log_path: Путь к файлу с логами ошибок.
     :vartype errors_log_path: Path
     :ivar json_log_path: Путь к файлу с JSON логами.
     :vartype json_log_path: Path
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

        :param info_log_path: Путь к файлу для информационных логов (необязательно).
        :param debug_log_path: Путь к файлу для отладочных логов (необязательно).
        :param errors_log_path: Путь к файлу для логов ошибок (необязательно).
        :param json_log_path: Путь к файлу для JSON логов (необязательно).
        """
        # Определяем пути к файлам
        config = SimpleNamespace(**j_loads(Path(__root__ / 'src' / 'config.json').read_text(encoding='UTF-8'))) #  Заменено json.loads на j_loads
        timestamp = datetime.datetime.now().strftime("%d%m%y%H%M")
        base_path:Path = Path(config.path['log'])
        self.log_files_path:Path = base_path / timestamp

        self.info_log_path =  self.log_files_path / (info_log_path or 'info.log')
        self.debug_log_path = self.log_files_path / (debug_log_path or  'debug.log')
        self.errors_log_path = self.log_files_path / (errors_log_path or  'errors.log')
        self.json_log_path =  base_path / (json_log_path or  f'{timestamp}.json')

        # Проверяем существование директорий
        self.log_files_path.mkdir(parents=True, exist_ok=True)

        # Создаем файлы логирования
        self.info_log_path.touch(exist_ok=True)
        self.debug_log_path.touch(exist_ok=True)
        self.errors_log_path.touch(exist_ok=True)
        self.json_log_path.touch(exist_ok=True)

        # Консольный логгер
        self.logger_console = logging.getLogger(name= 'logger_console')
        self.logger_console.setLevel(logging.DEBUG)
        # console_handler = logging.StreamHandler()
        # console_handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
        # self.logger_console.addHandler(console_handler)

        # Инфо логгер
        self.logger_file_info = logging.getLogger(name='logger_file_info')
        self.logger_file_info.setLevel(logging.INFO)
        info_handler = logging.FileHandler(self.info_log_path)
        info_handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
        self.logger_file_info.addHandler(info_handler)

        # Дебаг логгер
        self.logger_file_debug = logging.getLogger(name='logger_file_debug')
        self.logger_file_debug.setLevel(logging.DEBUG)
        debug_handler = logging.FileHandler(self.debug_log_path)
        debug_handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
        self.logger_file_debug.addHandler(debug_handler)

        # Логгер ошибок
        self.logger_file_errors =  logging.getLogger(name='logger_file_errors')
        self.logger_file_errors.setLevel(logging.ERROR)
        errors_handler = logging.FileHandler(self.errors_log_path)
        errors_handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
        self.logger_file_errors.addHandler(errors_handler)

        # JSON логгер
        self.logger_file_json = logging.getLogger(name='logger_json')
        self.logger_file_json.setLevel(logging.DEBUG)
        json_handler = logging.FileHandler(self.json_log_path)
        json_handler.setFormatter(JsonFormatter())  # Используем наш кастомный форматтер
        self.logger_file_json.addHandler(json_handler)
        # Удаляем все обработчики, которые выводят в консоль
        for handler in self.logger_file_json.handlers:
            if isinstance(handler, logging.StreamHandler):
                self.logger_file_json.removeHandler(handler)

    def _format_message(self, message, ex=None, color: Optional[Tuple[str, str]] = None):
        """
        Форматирует сообщение с опциональным цветом и информацией об исключении.

        :param message: Сообщение для форматирования.
        :param ex: Исключение, которое нужно добавить в сообщение (необязательно).
        :param color: Кортеж из текстового и фонового цветов (необязательно).
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
        Возвращает полную информацию об исключении, включая функцию, файл и строку, где возникло исключение.

         :param ex: Исключение, для которого нужно получить информацию.
         :return: Строка с информацией об исключении.
        """
        frame_info = inspect.stack()[3]
        file_name = frame_info.filename
        function_name = frame_info.function
        line_number = frame_info.lineno

        return f"\nFile: {file_name}, \n |\n  -Function: {function_name}, \n   |\n    --Line: {line_number}\n{ex if ex else ''}"

    def log(self, level, message, ex=None, exc_info=False, color: Optional[Tuple[str, str]] = None):
        """
        Записывает сообщение в лог на указанном уровне с опциональным цветом.

        :param level: Уровень логирования.
        :param message: Сообщение для записи в лог.
        :param ex: Исключение, которое нужно добавить в сообщение (необязательно).
        :param exc_info: Флаг, указывающий, нужно ли добавлять информацию об исключении.
        :param color: Кортеж из текстового и фонового цветов (необязательно).
        """
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


    def info(self, message, ex=None, exc_info=False, text_color: str = "green", bg_color: str = ""):
        """
        Записывает информационное сообщение в лог с опциональными цветами.

        :param message: Сообщение для записи в лог.
        :param ex: Исключение, которое нужно добавить в сообщение (необязательно).
        :param exc_info: Флаг, указывающий, нужно ли добавлять информацию об исключении.
        :param text_color: Цвет текста (по умолчанию "green").
        :param bg_color: Цвет фона (по умолчанию "").
        """
        color = (text_color, bg_color)
        self.log(logging.INFO, message, ex, exc_info, color)

    def success(self, message, ex=None, exc_info=False, text_color: str = "yellow", bg_color: str = ""):
        """
        Записывает сообщение об успехе в лог с опциональными цветами.

        :param message: Сообщение для записи в лог.
        :param ex: Исключение, которое нужно добавить в сообщение (необязательно).
        :param exc_info: Флаг, указывающий, нужно ли добавлять информацию об исключении.
        :param text_color: Цвет текста (по умолчанию "yellow").
        :param bg_color: Цвет фона (по умолчанию "").
        """
        color = (text_color, bg_color)
        self.log(logging.INFO, message, ex, exc_info, color)

    def warning(self, message, ex=None, exc_info=False, text_color: str = "black", bg_color: str = "yellow"):
        """
        Записывает предупреждающее сообщение в лог с опциональными цветами.

        :param message: Сообщение для записи в лог.
        :param ex: Исключение, которое нужно добавить в сообщение (необязательно).
        :param exc_info: Флаг, указывающий, нужно ли добавлять информацию об исключении.
        :param text_color: Цвет текста (по умолчанию "black").
        :param bg_color: Цвет фона (по умолчанию "yellow").
        """
        color = (text_color, bg_color)
        self.log(logging.WARNING, message, ex, exc_info, color)

    def debug(self, message, ex=None, exc_info=True, text_color: str = "cyan", bg_color: str = ""):
        """
        Записывает отладочное сообщение в лог с опциональными цветами.

        :param message: Сообщение для записи в лог.
        :param ex: Исключение, которое нужно добавить в сообщение (необязательно).
        :param exc_info: Флаг, указывающий, нужно ли добавлять информацию об исключении.
        :param text_color: Цвет текста (по умолчанию "cyan").
        :param bg_color: Цвет фона (по умолчанию "").
        """
        color = (text_color, bg_color)
        self.log(logging.DEBUG, message, ex, exc_info, color)

    def error(self, message, ex=None, exc_info=True, text_color: str = "red", bg_color: str = ""):
        """
        Записывает сообщение об ошибке в лог с опциональными цветами.

        :param message: Сообщение для записи в лог.
        :param ex: Исключение, которое нужно добавить в сообщение (необязательно).
        :param exc_info: Флаг, указывающий, нужно ли добавлять информацию об исключении.
        :param text_color: Цвет текста (по умолчанию "red").
        :param bg_color: Цвет фона (по умолчанию "").
        """
        color = (text_color, bg_color)
        self.log(logging.ERROR, message, ex, exc_info, color)

    def critical(self, message, ex=None, exc_info=True, text_color: str = "red", bg_color: str = "white"):
        """
         Записывает критическое сообщение в лог с опциональными цветами.

         :param message: Сообщение для записи в лог.
         :param ex: Исключение, которое нужно добавить в сообщение (необязательно).
         :param exc_info: Флаг, указывающий, нужно ли добавлять информацию об исключении.
         :param text_color: Цвет текста (по умолчанию "red").
         :param bg_color: Цвет фона (по умолчанию "white").
        """
        color = (text_color, bg_color)
        self.log(logging.CRITICAL, message, ex, exc_info, color)

# Инициализация логгера с файловыми путями
# logger = Logger(info_log_path='info.log', debug_log_path='debug.log', errors_log_path='errors.log', json_log_path='log.json')
logger = Logger()
```