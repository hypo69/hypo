# Анализ кода модуля `logger`

**Качество кода**
9
-  Плюсы
    -   Реализован паттерн Singleton для класса Logger, что гарантирует единственный экземпляр логгера в приложении.
    -   Используются кастомные форматировщики для JSON и обычного текстового вывода логов.
    -   Логирование вынесено в отдельные файлы для разных уровней (INFO, DEBUG, ERROR), что облегчает их анализ.
    -   Используется библиотека `colorama` для цветного вывода в консоль.
    -   Добавлены методы для упрощенной записи сообщений разных уровней (`info`, `debug`, `error`, и т.д.).
    -   Исключение в методе `_ex_full_info` формируется с полной информацией о месте возникновения ошибки.
    -   Используется  `SimpleNamespace` для хранения настроек из файла конфигурации
    -   Наличие подробной документации
-  Минусы
    -   Используется `json.loads` для чтения конфигурационного файла, вместо `j_loads` из `src.utils.jjson`.
    -   Некоторые части кода закомментированы.
    -   Не во всех функциях есть подробная документация в формате RST.
    -   Дублирование кода при настройке обработчиков для разных файлов логов
    -   Не используется импорт `from src.logger.logger import logger`

**Рекомендации по улучшению**

1.  Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` вместо стандартного `json.loads`.
2.  Удалить или раскомментировать и переработать  закомментированный код с выводом в консоль.
3.  Добавить документацию в формате RST для всех функций, методов и класса.
4.  Использовать `from src.logger.logger import logger` для импорта логгера.
5.  Упростить код инициализации обработчиков логов, выделив повторяющийся код в отдельную функцию.
6.  Удалить излишние комментарии.
7.   Переработать использование `try-except`, предпочитая обработку ошибок с помощью `logger.error`.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для логирования событий приложения.
=========================================================================================

Этот модуль содержит класс :class:`Logger`, который реализует паттерн Singleton и обеспечивает
логирование в консоль, файлы и в JSON-формате. Поддерживается настройка уровней логирования,
цвета для вывода в консоль и запись полной информации об исключениях.

Пример использования
--------------------

Пример использования класса `Logger`:

.. code-block:: python

    from src.logger.logger import logger

    logger.info('Сообщение', exc_info=True)
    logger.error('Ошибка', ex=Exception('test'), exc_info=True)
"""
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
    """
    Метакласс для реализации паттерна Singleton.
    """
    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        """
        Возвращает единственный экземпляр класса.

        Если экземпляр не существует, то он создается.
        """
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    instance = super().__call__(*args, **kwargs)
                    cls._instances[cls] = instance
        return cls._instances[cls]

class JsonFormatter(logging.Formatter):
    """
    Кастомный форматтер для логирования в JSON-формате.
    """

    def format(self, record):
        """
        Форматирует запись лога в JSON.

        Args:
            record (LogRecord): Запись лога.

        Returns:
            str: JSON-представление записи лога.
        """
        log_entry = {
            'asctime': self.formatTime(record, self.datefmt),
            'levelname': record.levelname,
            'message': record.getMessage().replace('"', '\''),
            'exc_info': self.formatException(record.exc_info)
            if record.exc_info
            else None,
        }
        _json = j_loads(log_entry)
        return _json

class Logger(metaclass=SingletonMeta):
    """
    Класс логгера, реализующий паттерн Singleton с логированием в консоль, файл и JSON.

    Args:
        info_log_path (Optional[str]): Путь к файлу для INFO логов.
        debug_log_path (Optional[str]): Путь к файлу для DEBUG логов.
        errors_log_path (Optional[str]): Путь к файлу для ERROR логов.
        json_log_path (Optional[str]): Путь к файлу для JSON логов.
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
        Инициализация экземпляра Logger.
        """
        config = SimpleNamespace(
            **j_loads(Path(__root__ / 'src' / 'config.json').read_text(encoding='UTF-8'))
        )
        timestamp = datetime.datetime.now().strftime('%d%m%y%H%M')
        base_path: Path = Path(config.path['log'])
        self.log_files_path: Path = base_path / timestamp

        self.info_log_path = self.log_files_path / (info_log_path or 'info.log')
        self.debug_log_path = self.log_files_path / (debug_log_path or 'debug.log')
        self.errors_log_path = self.log_files_path / (errors_log_path or 'errors.log')
        self.json_log_path = base_path / (json_log_path or f'{timestamp}.json')

        self.log_files_path.mkdir(parents=True, exist_ok=True)

        self.info_log_path.touch(exist_ok=True)
        self.debug_log_path.touch(exist_ok=True)
        self.errors_log_path.touch(exist_ok=True)
        self.json_log_path.touch(exist_ok=True)

        self.logger_console = logging.getLogger(name='logger_console')
        self.logger_console.setLevel(logging.DEBUG)

        self._setup_file_logger(
            'logger_file_info',
            self.info_log_path,
            logging.INFO,
            logging.Formatter('%(levelname)s: %(message)s'),
        )
        self._setup_file_logger(
            'logger_file_debug',
            self.debug_log_path,
            logging.DEBUG,
            logging.Formatter('%(levelname)s: %(message)s'),
        )
        self._setup_file_logger(
            'logger_file_errors',
            self.errors_log_path,
            logging.ERROR,
            logging.Formatter('%(levelname)s: %(message)s'),
        )

        self.logger_file_json = logging.getLogger(name='logger_json')
        self.logger_file_json.setLevel(logging.DEBUG)
        json_handler = logging.FileHandler(self.json_log_path)
        json_handler.setFormatter(JsonFormatter())
        self.logger_file_json.addHandler(json_handler)

        for handler in self.logger_file_json.handlers:
            if isinstance(handler, logging.StreamHandler):
                self.logger_file_json.removeHandler(handler)

    def _setup_file_logger(self, name: str, file_path: Path, level: int, formatter: logging.Formatter):
        """
        Настраивает файловый логгер.
         Args:
            name (str): Имя логгера.
            file_path (Path): Путь к файлу лога.
            level (int): Уровень логирования.
            formatter (logging.Formatter): Форматтер для лога.
        """
        logger = logging.getLogger(name=name)
        logger.setLevel(level)
        file_handler = logging.FileHandler(file_path)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    def _format_message(self, message, ex=None, color: Optional[Tuple[str, str]] = None):
        """
        Форматирует сообщение с цветом и информацией об исключении.

        Args:
            message (str): Сообщение для логирования.
            ex (Optional[Exception]): Исключение.
            color (Optional[Tuple[str, str]]): Кортеж с цветом текста и фона.

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
           str: Строка с информацией об исключении.
        """
        frame_info = inspect.stack()[3]
        file_name = frame_info.filename
        function_name = frame_info.function
        line_number = frame_info.lineno

        return f'\\nFile: {file_name}, \\n |\\n  -Function: {function_name}, \\n   |\\n    --Line: {line_number}\\n{ex if ex else ""}'

    def log(self, level, message, ex=None, exc_info=False, color: Optional[Tuple[str, str]] = None):
        """
        Логирует сообщение на указанном уровне.

        Args:
            level (int): Уровень логирования.
            message (str): Сообщение для логирования.
            ex (Optional[Exception]): Исключение.
            exc_info (bool): Флаг, указывающий, нужно ли выводить информацию об исключении.
            color (Optional[Tuple[str, str]]): Кортеж с цветом текста и фона.
        """
        formatted_message = self._format_message(message, ex, color)
        if exc_info:
            formatted_message += self._ex_full_info(ex)

        if self.logger_console:
            self.logger_console.log(level, formatted_message, exc_info=exc_info)


    def info(self, message, ex=None, exc_info=False, text_color: str = 'green', bg_color: str = ''):
        """
        Логирует информационное сообщение.
         Args:
            message (str): Сообщение для логирования.
            ex (Optional[Exception]): Исключение.
            exc_info (bool): Флаг, указывающий, нужно ли выводить информацию об исключении.
            text_color (str): Цвет текста.
            bg_color (str): Цвет фона.
        """
        color = (text_color, bg_color)
        self.log(logging.INFO, message, ex, exc_info, color)

    def success(self, message, ex=None, exc_info=False, text_color: str = 'yellow', bg_color: str = ''):
        """
        Логирует сообщение об успехе.
         Args:
            message (str): Сообщение для логирования.
            ex (Optional[Exception]): Исключение.
            exc_info (bool): Флаг, указывающий, нужно ли выводить информацию об исключении.
            text_color (str): Цвет текста.
            bg_color (str): Цвет фона.
        """
        color = (text_color, bg_color)
        self.log(logging.INFO, message, ex, exc_info, color)

    def warning(self, message, ex=None, exc_info=False, text_color: str = 'black', bg_color: str = 'yellow'):
        """
        Логирует сообщение предупреждения.
         Args:
            message (str): Сообщение для логирования.
            ex (Optional[Exception]): Исключение.
            exc_info (bool): Флаг, указывающий, нужно ли выводить информацию об исключении.
            text_color (str): Цвет текста.
            bg_color (str): Цвет фона.
        """
        color = (text_color, bg_color)
        self.log(logging.WARNING, message, ex, exc_info, color)

    def debug(self, message, ex=None, exc_info=True, text_color: str = 'cyan', bg_color: str = ''):
        """
        Логирует отладочное сообщение.
         Args:
            message (str): Сообщение для логирования.
            ex (Optional[Exception]): Исключение.
            exc_info (bool): Флаг, указывающий, нужно ли выводить информацию об исключении.
            text_color (str): Цвет текста.
            bg_color (str): Цвет фона.
        """
        color = (text_color, bg_color)
        self.log(logging.DEBUG, message, ex, exc_info, color)

    def error(self, message, ex=None, exc_info=True, text_color: str = 'red', bg_color: str = ''):
        """
        Логирует сообщение об ошибке.
         Args:
            message (str): Сообщение для логирования.
            ex (Optional[Exception]): Исключение.
            exc_info (bool): Флаг, указывающий, нужно ли выводить информацию об исключении.
            text_color (str): Цвет текста.
            bg_color (str): Цвет фона.
        """
        color = (text_color, bg_color)
        self.log(logging.ERROR, message, ex, exc_info, color)

    def critical(self, message, ex=None, exc_info=True, text_color: str = 'red', bg_color: str = 'white'):
        """
        Логирует критическое сообщение.
         Args:
            message (str): Сообщение для логирования.
            ex (Optional[Exception]): Исключение.
            exc_info (bool): Флаг, указывающий, нужно ли выводить информацию об исключении.
            text_color (str): Цвет текста.
            bg_color (str): Цвет фона.
        """
        color = (text_color, bg_color)
        self.log(logging.CRITICAL, message, ex, exc_info, color)

from src.logger.logger import logger
```