# Анализ кода модуля `src.logger.logger`

## Качество кода:
- **Соответствие стандартам**: 7
- **Плюсы**:
    - Реализован паттерн Singleton для класса Logger.
    - Используется `colorama` для цветного вывода в консоль.
    - Логирование в файл и JSON-формате.
    - Наличие различных уровней логирования (info, debug, error, critical).
    - Возможность добавлять цвет к логам.
    - Форматирование JSON-логирования с `JsonFormatter`.
    - Удобные методы для логирования: `info`, `debug`, `error`, `critical`
- **Минусы**:
    - Используется `json.loads` вместо `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    - Не все методы логирования используют передачу `exc_info=True` по умолчанию, в то время как при `debug` и `error` это поведение установлено по умолчанию.
    - Отсутствует RST-документация для функций, методов и классов.
    - Дублирование логики форматирования в методе `log`.
    - Не все логи записываются в файл. (закомментировано).
    - Код не соответствует стандарту PEP8 (отсутствуют пустые строки между определениями методов).
    - Закомментированный код.

## Рекомендации по улучшению:
1.  **Использовать `j_loads` или `j_loads_ns`**: заменить `json.loads` на `j_loads_ns` из `src.utils.jjson` для загрузки конфигурации.
2.  **Добавить RST-документацию**: добавить документацию в формате RST для всех классов, методов и функций, включая параметры, возвращаемые значения и примеры использования.
3.  **Стандартизация `exc_info`**: Сделать `exc_info=True` по умолчанию для всех методов логирования, если это требуется в данном контексте или явно указать `exc_info=False` в методах, где это не требуется.
4.  **Логика записи в файл**: исправить логику записи в файл. Все логи должны записываться в соответствующие файлы.
5.  **Удалить лишний код**: убрать закомментированный код.
6.  **Форматирование кода**: привести код в соответствие со стандартами PEP8.
7.  **Улучшение форматирования сообщений**:
    - Вынести общую логику форматирования сообщения и информации об исключении в отдельные методы.
    - Сделать форматирование более гибким, чтобы можно было настраивать вывод.
8.  **Улучшить метод `_ex_full_info`**:
    -  Обеспечить корректное извлечение информации об исключении.
    -  Форматировать вывод информации об исключении в более читаемом виде.
9. **Инициализация логгера**: перенести инициализацию логгера в отдельную функцию или метод, чтобы можно было настраивать его параметры.

## Оптимизированный код:
```python
"""
Модуль для работы с логгированием.
=================================

Этот модуль предоставляет класс :class:`Logger`, который реализует шаблон Singleton
и обеспечивает логирование в консоль, файлы и в формате JSON.

Пример использования
----------------------
.. code-block:: python

    from src.logger.logger import logger

    logger.info('Это информационное сообщение', exc_info=False)
    try:
        raise ValueError('Пример ошибки')
    except ValueError as e:
        logger.error('Произошла ошибка', ex=e, exc_info=True)
"""
import logging
import colorama
import datetime
import inspect
import threading
from pathlib import Path
from typing import Optional, Tuple
from types import SimpleNamespace

from src.utils.jjson import j_loads_ns # Используем j_loads_ns
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
    Метакласс для реализации Singleton.
    
    Этот метакласс гарантирует, что у класса будет только один экземпляр.

    :ivar _instances: Словарь для хранения экземпляров классов.
    :vartype _instances: dict
    :ivar _lock: Блокировка для обеспечения потокобезопасности.
    :vartype _lock: threading.Lock
    """
    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        """
        Возвращает экземпляр класса, создавая его при первом вызове.
        
        :param args: Произвольные позиционные аргументы.
        :type args: tuple
        :param kwargs: Произвольные именованные аргументы.
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

    Этот форматтер преобразует запись лога в JSON.
    """
    def format(self, record):
        """
        Форматирует запись лога в виде JSON.

        :param record: Запись лога.
        :type record: logging.LogRecord
        :return: JSON-представление записи лога.
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
        _json = j_loads_ns(log_entry) # Исправлено: j_loads_ns вместо json.dumps
        return _json


class Logger(metaclass=SingletonMeta):
    """
    Класс Logger, реализующий паттерн Singleton для логирования.

    Предоставляет методы для логирования в консоль, файлы и в JSON формате.
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

        :param info_log_path: Путь к файлу для информационных логов.
        :type info_log_path: str, optional
        :param debug_log_path: Путь к файлу для отладочных логов.
        :type debug_log_path: str, optional
        :param errors_log_path: Путь к файлу для логов ошибок.
        :type errors_log_path: str, optional
        :param json_log_path: Путь к файлу для JSON логов.
        :type json_log_path: str, optional
        """
        config = SimpleNamespace(
            **j_loads_ns(Path(__root__ / 'src' / 'config.json').read_text(encoding='UTF-8')) # Исправлено: j_loads_ns вместо json.loads
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

        self.logger_file_info = logging.getLogger(name='logger_file_info')
        self.logger_file_info.setLevel(logging.INFO)
        info_handler = logging.FileHandler(self.info_log_path)
        info_handler.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))
        self.logger_file_info.addHandler(info_handler)

        self.logger_file_debug = logging.getLogger(name='logger_file_debug')
        self.logger_file_debug.setLevel(logging.DEBUG)
        debug_handler = logging.FileHandler(self.debug_log_path)
        debug_handler.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))
        self.logger_file_debug.addHandler(debug_handler)

        self.logger_file_errors = logging.getLogger(name='logger_file_errors')
        self.logger_file_errors.setLevel(logging.ERROR)
        errors_handler = logging.FileHandler(self.errors_log_path)
        errors_handler.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))
        self.logger_file_errors.addHandler(errors_handler)

        self.logger_file_json = logging.getLogger(name='logger_json')
        self.logger_file_json.setLevel(logging.DEBUG)
        json_handler = logging.FileHandler(self.json_log_path)
        json_handler.setFormatter(JsonFormatter())
        self.logger_file_json.addHandler(json_handler)


        for handler in self.logger_file_json.handlers:
            if isinstance(handler, logging.StreamHandler):
                self.logger_file_json.removeHandler(handler)

    def _format_message(self, message, ex=None, color: Optional[Tuple[str, str]] = None):
        """
        Форматирует сообщение с учетом цвета и информации об исключении.

        :param message: Сообщение для форматирования.
        :type message: str
        :param ex: Информация об исключении.
        :type ex: Exception, optional
        :param color: Цвет текста и фона.
        :type color: tuple[str, str], optional
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
        Возвращает полную информацию об исключении.

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

    def log(self, level, message, ex=None, exc_info=True, color: Optional[Tuple[str, str]] = None):
        """
        Общий метод для логирования сообщений на определенном уровне.

        :param level: Уровень логирования.
        :type level: int
        :param message: Сообщение для логирования.
        :type message: str
        :param ex: Исключение.
        :type ex: Exception, optional
        :param exc_info: Флаг добавления информации об исключении.
        :type exc_info: bool, optional
        :param color: Цвет текста и фона.
        :type color: tuple[str, str], optional
        """
        formatted_message = self._format_message(message, ex, color)
        if exc_info and ex:
            formatted_message += self._ex_full_info(ex)
        
        if self.logger_console:
            self.logger_console.log(level, formatted_message, exc_info=exc_info)

        if level == logging.INFO and self.logger_file_info:
            self.logger_file_info.log(level, message, exc_info=exc_info) # Записываем только сообщение без форматирования
        if level == logging.DEBUG and self.logger_file_debug:
             self.logger_file_debug.log(level, message, exc_info=exc_info)
        if level in [logging.ERROR, logging.CRITICAL] and self.logger_file_errors:
            self.logger_file_errors.log(level, message, exc_info=exc_info)

        if self.logger_file_json:
            self.logger_file_json.log(level, message, exc_info=exc_info) # Записываем в json все логи


    def info(self, message, ex=None, exc_info=False, text_color: str = 'green', bg_color: str = ''):
        """
        Логирует информационное сообщение.

        :param message: Сообщение для логирования.
        :type message: str
        :param ex: Исключение.
        :type ex: Exception, optional
        :param exc_info: Флаг добавления информации об исключении.
        :type exc_info: bool, optional
        :param text_color: Цвет текста.
        :type text_color: str, optional
        :param bg_color: Цвет фона.
        :type bg_color: str, optional
        """
        color = (text_color, bg_color)
        self.log(logging.INFO, message, ex, exc_info, color)

    def success(self, message, ex=None, exc_info=False, text_color: str = 'yellow', bg_color: str = ''):
        """
        Логирует сообщение об успехе.

        :param message: Сообщение для логирования.
        :type message: str
        :param ex: Исключение.
        :type ex: Exception, optional
        :param exc_info: Флаг добавления информации об исключении.
        :type exc_info: bool, optional
        :param text_color: Цвет текста.
        :type text_color: str, optional
        :param bg_color: Цвет фона.
        :type bg_color: str, optional
        """
        color = (text_color, bg_color)
        self.log(logging.INFO, message, ex, exc_info, color)

    def warning(self, message, ex=None, exc_info=True, text_color: str = 'black', bg_color: str = 'yellow'):
        """
        Логирует предупреждающее сообщение.

        :param message: Сообщение для логирования.
        :type message: str
        :param ex: Исключение.
        :type ex: Exception, optional
        :param exc_info: Флаг добавления информации об исключении.
        :type exc_info: bool, optional
        :param text_color: Цвет текста.
        :type text_color: str, optional
        :param bg_color: Цвет фона.
        :type bg_color: str, optional
        """
        color = (text_color, bg_color)
        self.log(logging.WARNING, message, ex, exc_info, color)

    def debug(self, message, ex=None, exc_info=True, text_color: str = 'cyan', bg_color: str = ''):
        """
        Логирует отладочное сообщение.

        :param message: Сообщение для логирования.
        :type message: str
        :param ex: Исключение.
        :type ex: Exception, optional
        :param exc_info: Флаг добавления информации об исключении.
        :type exc_info: bool, optional
        :param text_color: Цвет текста.
        :type text_color: str, optional
        :param bg_color: Цвет фона.
        :type bg_color: str, optional
        """
        color = (text_color, bg_color)
        self.log(logging.DEBUG, message, ex, exc_info, color)

    def error(self, message, ex=None, exc_info=True, text_color: str = 'red', bg_color: str = ''):
        """
        Логирует сообщение об ошибке.

        :param message: Сообщение для логирования.
        :type message: str
        :param ex: Исключение.
        :type ex: Exception, optional
        :param exc_info: Флаг добавления информации об исключении.
        :type exc_info: bool, optional
        :param text_color: Цвет текста.
        :type text_color: str, optional
        :param bg_color: Цвет фона.
        :type bg_color: str, optional
        """
        color = (text_color, bg_color)
        self.log(logging.ERROR, message, ex, exc_info, color)

    def critical(self, message, ex=None, exc_info=True, text_color: str = 'red', bg_color: str = 'white'):
        """
        Логирует критическое сообщение.

        :param message: Сообщение для логирования.
        :type message: str
        :param ex: Исключение.
        :type ex: Exception, optional
        :param exc_info: Флаг добавления информации об исключении.
        :type exc_info: bool, optional
        :param text_color: Цвет текста.
        :type text_color: str, optional
        :param bg_color: Цвет фона.
        :type bg_color: str, optional
        """
        color = (text_color, bg_color)
        self.log(logging.CRITICAL, message, ex, exc_info, color)

logger: Logger = Logger()
```