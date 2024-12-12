# Анализ кода модуля `logger`

**Качество кода: 7/10**
-  **Плюсы**
    -   Используется Singleton для класса `Logger`, что обеспечивает единую точку доступа к логгеру.
    -   Применяется `colorama` для цветного вывода в консоль, что улучшает читаемость логов.
    -   Реализован кастомный JSON-форматтер для структурированного логирования в JSON.
    -   Логи разделены на разные файлы по уровням (info, debug, errors).
    -   Добавлена возможность логирования с цветовым оформлением и выводом информации об исключениях.
-   **Минусы**
    -   Не все логи пишутся в файлы (проблема двойного вывода в консоль не решена).
    -   Присутствует избыточность при создании и настройке логгеров (можно упростить).
    -   Не все методы используют форматирование исключений.
    -   Стиль комментариев и документации не унифицирован (не везде используется reStructuredText).
    -   Используется `json.loads` вместо `j_loads` или `j_loads_ns`.

**Рекомендации по улучшению**
1.  **Использование `j_loads_ns`**: Замените `json.loads` на `j_loads_ns` из `src.utils.jjson` для загрузки конфигурации.
2.  **Унификация логгирования**: Используйте один метод `log` для всех уровней логирования. Упростите запись в файлы, убрав лишние проверки.
3.  **Форматирование исключений**: Применяйте `self._ex_full_info(ex)` во всех методах логирования для единообразия.
4.  **Улучшение документации**: Приведите все docstring и комментарии к формату reStructuredText.
5.  **Упрощение создания логгеров**: Избавьтесь от дублирования кода при создании и настройке разных логгеров, вынесите это в отдельную функцию.
6. **Исправление двойного вывода**: Устраните проблему двойного вывода логов в консоль.
7. **Импорты**: Добавьте импорты `src.utils.jjson` и `src.logger.logger`
8. **Именование переменных**: Приведите все имена переменных к общему стилю и переименуйте `base_path` в `log_base_path`, `message` в `msg`.
9. **Улучшение обработки ошибок**: Уберите избыточное использование `try-except`. Логируйте ошибки, используя `logger.error`.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для настройки и использования системы логирования.
========================================================

Этот модуль предоставляет класс :class:`Logger` для управления логированием сообщений
в консоль, файлы и JSON. Поддерживает разные уровни логирования,
цветовое оформление и добавление информации об исключениях.

Пример использования
--------------------

.. code-block:: python

    from src.logger.logger import logger

    logger.info("Информационное сообщение", text_color="blue")
    logger.debug("Отладочное сообщение", ex=Exception("Пример исключения"))
    logger.error("Сообщение об ошибке", ex=Exception("Пример ошибки"), exc_info=True)
"""

import logging
import colorama
import datetime
import inspect
import threading
from pathlib import Path
from typing import Optional, Tuple, Any
from types import SimpleNamespace

from src.utils.jjson import j_loads_ns
from src.logger.logger import logger

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

    Обеспечивает создание только одного экземпляра класса.
    """
    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        """
        Возвращает существующий экземпляр класса, или создаёт новый, если он ещё не существует.
        """
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    instance = super().__call__(*args, **kwargs)
                    cls._instances[cls] = instance
        return cls._instances[cls]


class JsonFormatter(logging.Formatter):
    """
    Форматтер для логирования в JSON формате.

    Преобразует записи лога в JSON строку.
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
            "message": record.getMessage().replace('"', "'"),
            "exc_info": self.formatException(record.exc_info) if record.exc_info else None,
        }
        _json = logging.json.dumps(log_entry, ensure_ascii=False)
        return _json


class Logger(metaclass=SingletonMeta):
    """
    Класс Logger, реализующий паттерн Singleton, для логирования в консоль, файлы и JSON.
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

        :param info_log_path: Путь к файлу для информационных логов.
        :param debug_log_path: Путь к файлу для отладочных логов.
        :param errors_log_path: Путь к файлу для логов ошибок.
        :param json_log_path: Путь к файлу для JSON логов.
        """
        # Читаем конфигурационный файл.
        config = SimpleNamespace(**j_loads_ns(Path(__root__ / 'src' / 'config.json').read_text(encoding='UTF-8')))
        timestamp = datetime.datetime.now().strftime("%d%m%y%H%M")
        log_base_path:Path = Path(config.path['log'])
        self.log_files_path = log_base_path / timestamp

        # Определение путей к файлам логов.
        self.info_log_path = self.log_files_path / (info_log_path or 'info.log')
        self.debug_log_path = self.log_files_path / (debug_log_path or 'debug.log')
        self.errors_log_path = self.log_files_path / (errors_log_path or 'errors.log')
        self.json_log_path = log_base_path / (json_log_path or f'{timestamp}.json')

        # Создание директорий и файлов.
        self.log_files_path.mkdir(parents=True, exist_ok=True)
        self.info_log_path.touch(exist_ok=True)
        self.debug_log_path.touch(exist_ok=True)
        self.errors_log_path.touch(exist_ok=True)
        self.json_log_path.touch(exist_ok=True)

        # Настройка логгера для консоли
        self.logger_console = self._setup_logger('logger_console', logging.DEBUG, is_console=True)
        # Настройка файловых логгеров
        self.logger_file_info = self._setup_logger('logger_file_info', logging.INFO, self.info_log_path)
        self.logger_file_debug = self._setup_logger('logger_file_debug', logging.DEBUG, self.debug_log_path)
        self.logger_file_errors = self._setup_logger('logger_file_errors', logging.ERROR, self.errors_log_path)
        self.logger_file_json = self._setup_logger('logger_json', logging.DEBUG, self.json_log_path, formatter=JsonFormatter())

        # Удаляем все обработчики, которые выводят в консоль из json логера
        for handler in self.logger_file_json.handlers:
            if isinstance(handler, logging.StreamHandler):
                self.logger_file_json.removeHandler(handler)

    def _setup_logger(self, name: str, level: int, file_path: Optional[Path] = None, formatter = logging.Formatter("%(levelname)s: %(message)s"), is_console: bool = False) -> logging.Logger:
        """
        Настраивает и возвращает экземпляр логгера.

        :param name: Имя логгера.
        :param level: Уровень логирования.
        :param file_path: Путь к файлу лога (если нужно).
        :param formatter: Форматтер лога.
        :param is_console: Флаг, указывающий, что логгер для консоли.
        :return: Настроенный логгер.
        """
        logger = logging.getLogger(name=name)
        logger.setLevel(level)
        if is_console:
            handler = logging.StreamHandler()
        else:
            handler = logging.FileHandler(file_path)
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger

    def _format_message(self, msg: str, ex: Optional[Exception] = None, color: Optional[Tuple[str, str]] = None) -> str:
        """
        Форматирует сообщение с опциональным цветом и информацией об исключении.

        :param msg: Сообщение для логирования.
        :param ex: Исключение (если есть).
        :param color: Цвета текста и фона.
        :return: Отформатированное сообщение.
        """
        if color:
            text_color, bg_color = color
            text_color = TEXT_COLORS.get(text_color, colorama.Fore.RESET)
            bg_color = BG_COLORS.get(bg_color, colorama.Back.RESET)
            msg = f"{text_color}{bg_color}{msg} {ex or ''}{colorama.Style.RESET_ALL}"
        return msg

    def _ex_full_info(self, ex: Optional[Exception]) -> str:
        """
        Возвращает полную информацию об исключении, включая данные о функции, файле и строке.

        :param ex: Исключение (если есть).
        :return: Строка с полной информацией об исключении.
        """
        if not ex:
            return ""
        frame_info = inspect.stack()[3]
        file_name = frame_info.filename
        function_name = frame_info.function
        line_number = frame_info.lineno
        return f"\nFile: {file_name}, \n |\n  -Function: {function_name}, \n   |\n    --Line: {line_number}\n{ex}"

    def log(self, level: int, msg: str, ex: Optional[Exception] = None, exc_info: bool = False, color: Optional[Tuple[str, str]] = None):
        """
        Общий метод для логирования сообщений на указанном уровне.

        :param level: Уровень логирования.
        :param msg: Сообщение для логирования.
        :param ex: Исключение (если есть).
        :param exc_info: Флаг для вывода информации об исключении.
        :param color: Цвета текста и фона.
        """
        formatted_message = self._format_message(msg, ex, color)
        if exc_info:
            formatted_message += self._ex_full_info(ex)
        if self.logger_console:
             self.logger_console.log(level, formatted_message, exc_info=exc_info)
        self.logger_file_json.log(level, msg, exc_info=exc_info)

        if level == logging.INFO:
            self.logger_file_info.log(level, formatted_message)
        elif level == logging.DEBUG:
            self.logger_file_debug.log(level, formatted_message)
        elif level in [logging.ERROR, logging.CRITICAL]:
            self.logger_file_errors.log(level, formatted_message)


    def info(self, msg: str, ex: Optional[Exception] = None, exc_info: bool = False, text_color: str = "green", bg_color: str = ""):
        """
        Логирует информационное сообщение.

        :param msg: Сообщение для логирования.
        :param ex: Исключение (если есть).
        :param exc_info: Флаг для вывода информации об исключении.
        :param text_color: Цвет текста.
        :param bg_color: Цвет фона.
        """
        color = (text_color, bg_color)
        self.log(logging.INFO, msg, ex, exc_info, color)

    def success(self, msg: str, ex: Optional[Exception] = None, exc_info: bool = False, text_color: str = "yellow", bg_color: str = ""):
        """
        Логирует сообщение об успехе.

        :param msg: Сообщение для логирования.
        :param ex: Исключение (если есть).
        :param exc_info: Флаг для вывода информации об исключении.
        :param text_color: Цвет текста.
        :param bg_color: Цвет фона.
        """
        color = (text_color, bg_color)
        self.log(logging.INFO, msg, ex, exc_info, color)

    def warning(self, msg: str, ex: Optional[Exception] = None, exc_info: bool = False, text_color: str = "black", bg_color: str = "yellow"):
        """
        Логирует предупреждающее сообщение.

        :param msg: Сообщение для логирования.
        :param ex: Исключение (если есть).
        :param exc_info: Флаг для вывода информации об исключении.
        :param text_color: Цвет текста.
        :param bg_color: Цвет фона.
        """
        color = (text_color, bg_color)
        self.log(logging.WARNING, msg, ex, exc_info, color)

    def debug(self, msg: str, ex: Optional[Exception] = None, exc_info: bool = True, text_color: str = "cyan", bg_color: str = ""):
        """
        Логирует отладочное сообщение.

        :param msg: Сообщение для логирования.
        :param ex: Исключение (если есть).
        :param exc_info: Флаг для вывода информации об исключении.
        :param text_color: Цвет текста.
        :param bg_color: Цвет фона.
        """
        color = (text_color, bg_color)
        self.log(logging.DEBUG, msg, ex, exc_info, color)

    def error(self, msg: str, ex: Optional[Exception] = None, exc_info: bool = True, text_color: str = "red", bg_color: str = ""):
        """
        Логирует сообщение об ошибке.

        :param msg: Сообщение для логирования.
        :param ex: Исключение (если есть).
        :param exc_info: Флаг для вывода информации об исключении.
        :param text_color: Цвет текста.
        :param bg_color: Цвет фона.
        """
        color = (text_color, bg_color)
        self.log(logging.ERROR, msg, ex, exc_info, color)

    def critical(self, msg: str, ex: Optional[Exception] = None, exc_info: bool = True, text_color: str = "red", bg_color: str = "white"):
        """
        Логирует критическое сообщение.

        :param msg: Сообщение для логирования.
        :param ex: Исключение (если есть).
        :param exc_info: Флаг для вывода информации об исключении.
        :param text_color: Цвет текста.
        :param bg_color: Цвет фона.
        """
        color = (text_color, bg_color)
        self.log(logging.CRITICAL, msg, ex, exc_info, color)

# Инициализация логгера
logger = Logger()
```