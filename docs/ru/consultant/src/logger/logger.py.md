# Анализ кода модуля `src.logger.logger`

## Качество кода:

- **Соответствие стандартам**: 7/10
- **Плюсы**:
    - Реализован паттерн Singleton для класса Logger.
    - Используется кастомный JSON-форматтер для логирования.
    - Поддержка цветного вывода в консоль.
    - Разделение логов на разные уровни (info, debug, error).
    - Добавлены методы для удобного логирования с разными уровнями и цветами.
    - Включена информация об исключении и месте его возникновения.
- **Минусы**:
    -  Используется стандартный `json.load` вместо `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    - Не все функции и классы документированы в формате RST.
    -  Временные отключения вывода в файлы  через комментирование кода (вместо использования отдельных обработчиков).
    -  Наличие множества `if` условий для логирования.
    -  Не стандартизирован формат кавычек.
    -  Дублирование логики определения пути к файлам.
    -  Не все переменные и импорты отсортированы по алфавиту.

## Рекомендации по улучшению:

1. **Импорты и форматирование**:
   - Отсортировать импорты по алфавиту.
   - Использовать `from src.utils.jjson import j_loads` для загрузки конфигурации.
   - Использовать одинарные кавычки (`'`) в коде, двойные кавычки (`"`) только для вывода.
2. **Документация**:
   - Добавить RST-документацию для модуля, класса `Logger` и всех его методов.
3. **Логирование**:
   - Использовать  `logger.error` для обработки ошибок вместо стандартных `try-except` блоков.
   - Улучшить логику записи в файлы, убрав комментированный код и дублирование.
   -  Использовать более понятные названия переменных, например `log_level` вместо `level`.
4. **Структура кода**:
   -  Убрать дублирование логики определения пути к файлам.
   -  Рефакторинг метода `log` с использованием `match case` для определения уровня логирования.
5. **Обработка исключений**:
    -  Более детально проработать обработку ошибок при создании директорий и файлов.
6. **Общее**:
    - Следовать стандартам PEP8 для форматирования.
    - Избегать неясных формулировок в комментариях.

## Оптимизированный код:

```python
## \file /src/logger/logger.py
# -*- coding: utf-8 -*-
"""
Модуль для логирования событий в приложении.
===========================================

Модуль предоставляет класс :class:`Logger`, который реализует паттерн Singleton
и обеспечивает гибкое логирование в консоль и файлы.

Пример использования:
----------------------
.. code-block:: python

    from src.logger.logger import logger

    logger.info('Сообщение информации')
    logger.debug('Сообщение отладки', exc_info=True)
    logger.error('Сообщение об ошибке', ex=ValueError('Неверное значение'), exc_info=True)
"""
import datetime
import inspect
import logging
import threading
from pathlib import Path
from types import SimpleNamespace
from typing import Optional, Tuple

import colorama

from src.utils.jjson import j_loads  #  Используем j_loads вместо json.loads
from header import __root__

TEXT_COLORS = {
    'black': colorama.Fore.BLACK,
    'blue': colorama.Fore.BLUE,
    'cyan': colorama.Fore.CYAN,
    'green': colorama.Fore.GREEN,
    'light_blue': colorama.Fore.LIGHTBLUE_EX,
    'light_cyan': colorama.Fore.LIGHTCYAN_EX,
    'light_gray': colorama.Fore.LIGHTBLACK_EX,
    'light_green': colorama.Fore.LIGHTGREEN_EX,
    'light_magenta': colorama.Fore.LIGHTMAGENTA_EX,
    'light_red': colorama.Fore.LIGHTRED_EX,
    'light_yellow': colorama.Fore.LIGHTYELLOW_EX,
    'magenta': colorama.Fore.MAGENTA,
    'red': colorama.Fore.RED,
    'white': colorama.Fore.WHITE,
    'yellow': colorama.Fore.YELLOW,
}
# Словарь для цветов фона
BG_COLORS = {
    'black': colorama.Back.BLACK,
    'blue': colorama.Back.BLUE,
    'cyan': colorama.Back.CYAN,
    'green': colorama.Back.GREEN,
    'light_blue': colorama.Back.LIGHTBLUE_EX,
    'light_cyan': colorama.Back.LIGHTCYAN_EX,
    'light_gray': colorama.Back.LIGHTBLACK_EX,
    'light_green': colorama.Back.LIGHTGREEN_EX,
    'light_magenta': colorama.Back.LIGHTMAGENTA_EX,
    'light_red': colorama.Back.LIGHTRED_EX,
    'light_yellow': colorama.Back.LIGHTYELLOW_EX,
    'magenta': colorama.Back.MAGENTA,
    'red': colorama.Back.RED,
    'white': colorama.Back.WHITE,
    'yellow': colorama.Back.YELLOW,
}


class SingletonMeta(type):
    """
    Метакласс для реализации паттерна Singleton.

    Этот метакласс гарантирует, что класс будет иметь только один экземпляр.

    :ivar _instances: Словарь для хранения экземпляров классов.
    :vartype _instances: dict
    :ivar _lock: Блокировка для предотвращения гонок при создании экземпляров.
    :vartype _lock: threading.Lock
    """

    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        """
        Создает или возвращает существующий экземпляр класса.

        Если экземпляр класса не существует, он создается с использованием
        блокировки для обеспечения потокобезопасности.

        :param args: Позиционные аргументы для конструктора класса.
        :type args: tuple
        :param kwargs: Именованные аргументы для конструктора класса.
        :type kwargs: dict
        :return: Экземпляр класса.
        :rtype: object
        """
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    instance = super().__call__(*args, **kwargs)
                    cls._instances[cls] = instance
        return cls._instances[cls]


class JsonFormatter(logging.Formatter):
    """
    Кастомный форматтер для логирования в формате JSON.

    Преобразует записи лога в JSON-формат, включая время, уровень, сообщение и информацию об исключении.
    """

    def format(self, record):
        """
        Форматирует запись лога в виде JSON.

        :param record: Запись лога.
        :type record: logging.LogRecord
        :return: Запись лога в формате JSON.
        :rtype: str
        """
        log_entry = {
            'asctime': self.formatTime(record, self.datefmt),
            'levelname': record.levelname,
            'message': record.getMessage().replace('"', '\''),
            'exc_info': self.formatException(record.exc_info)
            if record.exc_info
            else None,
        }
        _json = str(j_loads(log_entry))  #  Используем j_loads вместо json.dumps
        return _json


class Logger(metaclass=SingletonMeta):
    """
    Класс логгера, реализующий паттерн Singleton.

    Обеспечивает логирование в консоль, файлы и в формате JSON.

    :ivar log_files_path: Путь к директории с файлами логов.
    :vartype log_files_path: Path
    :ivar info_log_path: Путь к файлу информационных логов.
    :vartype info_log_path: Path
    :ivar debug_log_path: Путь к файлу отладочных логов.
    :vartype debug_log_path: Path
    :ivar errors_log_path: Путь к файлу логов ошибок.
    :vartype errors_log_path: Path
    :ivar json_log_path: Путь к файлу JSON логов.
    :vartype json_log_path: Path
    """

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

        Определяет пути к файлам логов, создает директории и файлы,
        а также настраивает различные обработчики для логирования.

        :param info_log_path: Путь к файлу информационных логов (по умолчанию 'info.log').
        :type info_log_path: Optional[str]
        :param debug_log_path: Путь к файлу отладочных логов (по умолчанию 'debug.log').
        :type debug_log_path: Optional[str]
        :param errors_log_path: Путь к файлу логов ошибок (по умолчанию 'errors.log').
        :type errors_log_path: Optional[str]
        :param json_log_path: Путь к файлу JSON логов (по умолчанию 'timestamp.json').
        :type json_log_path: Optional[str]
        """
        # Define file paths
        config = SimpleNamespace(
            **j_loads(Path(__root__ / 'src' / 'config.json').read_text(encoding='UTF-8'))  # Используем j_loads
        )
        timestamp = datetime.datetime.now().strftime('%d%m%y%H%M')
        base_path: Path = Path(config.path['log'])
        self.log_files_path: Path = base_path / timestamp

        self.info_log_path = self.log_files_path / (info_log_path or 'info.log')
        self.debug_log_path = self.log_files_path / (debug_log_path or 'debug.log')
        self.errors_log_path = self.log_files_path / (errors_log_path or 'errors.log')
        self.json_log_path = base_path / (json_log_path or f'{timestamp}.json')

        # Ensure directories exist
        try:  #  Добавляем обработку ошибок при создании директории
            self.log_files_path.mkdir(parents=True, exist_ok=True)
        except OSError as e:
            self.error(f'Ошибка при создании директории {self.log_files_path}: {e}', exc_info=True)

        # Ensure log files exist
        try:  #  Добавляем обработку ошибок при создании файлов
            self.info_log_path.touch(exist_ok=True)
            self.debug_log_path.touch(exist_ok=True)
            self.errors_log_path.touch(exist_ok=True)
            self.json_log_path.touch(exist_ok=True)
        except OSError as e:
            self.error(f'Ошибка при создании файлов логов: {e}', exc_info=True)

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
        json_handler.setFormatter(JsonFormatter())
        self.logger_file_json.addHandler(json_handler)

        # Удаляем все обработчики, которые выводят в консоль
        for handler in self.logger_file_json.handlers:
            if isinstance(handler, logging.StreamHandler):
                self.logger_file_json.removeHandler(handler)

    def _format_message(self, message, ex=None, color: Optional[Tuple[str, str]] = None):
        """
        Форматирует сообщение с опциональным цветом и информацией об исключении.

        :param message: Сообщение для форматирования.
        :type message: str
        :param ex: Исключение (если есть).
        :type ex: Optional[Exception]
        :param color: Кортеж с цветом текста и фона.
        :type color: Optional[Tuple[str, str]]
        :return: Форматированное сообщение.
        :rtype: str
        """
        if color:
            text_color, bg_color = color
            text_color = TEXT_COLORS.get(text_color, colorama.Fore.RESET)
            bg_color = BG_COLORS.get(bg_color, colorama.Back.RESET)
            message = f'{text_color}{bg_color}{message} {ex or ""}{colorama.Style.RESET_ALL}'
        return message

    def _ex_full_info(self, ex):
        """
        Возвращает полную информацию об исключении, включая имя функции, файла и номер строки.

         :param ex: Исключение.
         :type ex: Exception
         :return: Строка с информацией об исключении.
         :rtype: str
        """
        frame_info = inspect.stack()[3]
        file_name = frame_info.filename
        function_name = frame_info.function
        line_number = frame_info.lineno

        return f'\\nFile: {file_name}, \\n |\\n  -Function: {function_name}, \\n   |\\n    --Line: {line_number}\\n{ex if ex else ""}'

    def log(self, log_level, message, ex=None, exc_info=False, color: Optional[Tuple[str, str]] = None):
        """
        Записывает сообщение лога с заданным уровнем, цветом и информацией об исключении.

        :param log_level: Уровень логирования (например, logging.INFO, logging.DEBUG).
        :type log_level: int
        :param message: Сообщение для записи в лог.
        :type message: str
        :param ex: Исключение (если есть).
        :type ex: Optional[Exception]
        :param exc_info: Флаг для включения информации об исключении в лог.
        :type exc_info: bool
        :param color: Кортеж с цветом текста и фона.
        :type color: Optional[Tuple[str, str]]
        """
        formatted_message = self._format_message(message, ex, color)
        if exc_info:
            formatted_message += self._ex_full_info(ex)

        if self.logger_console:
            self.logger_console.log(log_level, formatted_message, exc_info=exc_info)

        if log_level == logging.INFO and self.logger_file_info:  #  Упрощаем логику вывода в файлы
            self.logger_file_info.log(log_level, formatted_message)

        if log_level == logging.DEBUG and self.logger_file_debug:
            self.logger_file_debug.log(log_level, formatted_message)

        if log_level in [logging.ERROR, logging.CRITICAL] and self.logger_file_errors:
            self.logger_file_errors.log(log_level, formatted_message)
    

    def info(self, message, ex=None, exc_info=False, text_color: str = 'green', bg_color: str = ''):
        """
        Записывает информационное сообщение в лог.

        :param message: Сообщение для записи в лог.
        :type message: str
        :param ex: Исключение (если есть).
        :type ex: Optional[Exception]
        :param exc_info: Флаг для включения информации об исключении в лог.
        :type exc_info: bool
        :param text_color: Цвет текста.
        :type text_color: str
        :param bg_color: Цвет фона.
        :type bg_color: str
        """
        color = (text_color, bg_color)
        self.log(logging.INFO, message, ex, exc_info, color)

    def success(self, message, ex=None, exc_info=False, text_color: str = 'yellow', bg_color: str = ''):
        """
         Записывает сообщение об успешном выполнении в лог.

        :param message: Сообщение для записи в лог.
        :type message: str
        :param ex: Исключение (если есть).
        :type ex: Optional[Exception]
        :param exc_info: Флаг для включения информации об исключении в лог.
        :type exc_info: bool
        :param text_color: Цвет текста.
        :type text_color: str
        :param bg_color: Цвет фона.
        :type bg_color: str
        """
        color = (text_color, bg_color)
        self.log(logging.INFO, message, ex, exc_info, color)

    def warning(self, message, ex=None, exc_info=False, text_color: str = 'black', bg_color: str = 'yellow'):
        """
         Записывает предупреждающее сообщение в лог.

        :param message: Сообщение для записи в лог.
        :type message: str
        :param ex: Исключение (если есть).
        :type ex: Optional[Exception]
        :param exc_info: Флаг для включения информации об исключении в лог.
        :type exc_info: bool
        :param text_color: Цвет текста.
        :type text_color: str
        :param bg_color: Цвет фона.
        :type bg_color: str
        """
        color = (text_color, bg_color)
        self.log(logging.WARNING, message, ex, exc_info, color)

    def debug(self, message, ex=None, exc_info=True, text_color: str = 'cyan', bg_color: str = ''):
        """
         Записывает отладочное сообщение в лог.

        :param message: Сообщение для записи в лог.
        :type message: str
        :param ex: Исключение (если есть).
        :type ex: Optional[Exception]
        :param exc_info: Флаг для включения информации об исключении в лог.
        :type exc_info: bool
        :param text_color: Цвет текста.
        :type text_color: str
        :param bg_color: Цвет фона.
        :type bg_color: str
        """
        color = (text_color, bg_color)
        self.log(logging.DEBUG, message, ex, exc_info, color)

    def error(self, message, ex=None, exc_info=True, text_color: str = 'red', bg_color: str = ''):
        """
        Записывает сообщение об ошибке в лог.

        :param message: Сообщение для записи в лог.
        :type message: str
        :param ex: Исключение (если есть).
        :type ex: Optional[Exception]
        :param exc_info: Флаг для включения информации об исключении в лог.
        :type exc_info: bool
        :param text_color: Цвет текста.
        :type text_color: str
        :param bg_color: Цвет фона.
        :type bg_color: str
        """
        color = (text_color, bg_color)
        self.log(logging.ERROR, message, ex, exc_info, color)

    def critical(self, message, ex=None, exc_info=True, text_color: str = 'red', bg_color: str = 'white'):
        """
         Записывает критическое сообщение в лог.

        :param message: Сообщение для записи в лог.
        :type message: str
        :param ex: Исключение (если есть).
        :type ex: Optional[Exception]
        :param exc_info: Флаг для включения информации об исключении в лог.
        :type exc_info: bool
        :param text_color: Цвет текста.
        :type text_color: str
        :param bg_color: Цвет фона.
        :type bg_color: str
        """
        color = (text_color, bg_color)
        self.log(logging.CRITICAL, message, ex, exc_info, color)


# Инициализируем логгер
logger: Logger = Logger()
```