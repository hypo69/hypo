# Анализ кода модуля `src.logger`

**Качество кода: 8/10**

*   **Плюсы:**
    *   Модуль предоставляет гибкую систему логирования с поддержкой консоли, файлов и JSON.
    *   Используется паттерн Singleton для обеспечения единственного экземпляра логгера.
    *   Поддерживаются различные уровни логирования и настраиваемый вывод.
    *   Код организован в классы и функции, что способствует модульности.
    *   Предоставлена документация, хотя и не в формате RST.
*   **Минусы:**
    *   Документация представлена в формате Markdown, а не reStructuredText (RST).
    *   Отсутствуют явные импорты необходимых модулей (например, `logging`, `colorama`).
    *   В коде используются try-except блоки без необходимости, что можно заменить на `logger.error`.
    *   Не все методы документированы в формате RST.

**Рекомендации по улучшению:**

1.  **Переписать документацию:**
    *   Переписать всю документацию в формат reStructuredText (RST).
    *   Добавить docstring в формате RST для каждого класса, метода и функции.
2.  **Добавить импорты:**
    *   Явно добавить импорты необходимых модулей (например, `logging`, `colorama`, `typing`).
3.  **Улучшить обработку ошибок:**
    *   Избегать избыточного использования `try-except`, заменяя их на `logger.error` для обработки исключений.
4.  **Улучшить форматирование:**
    *   Сделать код более читаемым, добавив пустые строки и разделители.
5. **Использовать `j_loads` и `j_loads_ns`**
    * Убедиться что используется `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения файлов, если таковые используются.
6.  **Использовать `from src.logger.logger import logger`:**
     * Использовать явный импорт логгера `from src.logger.logger import logger`

**Оптимизированный код:**

```python
"""
Модуль для логирования приложения.
=========================================================================================

Этот модуль предоставляет гибкую систему логирования, поддерживающую вывод в консоль, файлы и JSON.
Он использует паттерн Singleton для обеспечения единственного экземпляра логгера в приложении.

Модуль включает:

    - :class:`SingletonMeta`: Метакласс для реализации паттерна Singleton.
    - :class:`JsonFormatter`: Пользовательский форматтер для вывода логов в JSON.
    - :class:`Logger`: Основной класс логгера.

Пример использования
--------------------

.. code-block:: python

    from src.logger.logger import Logger

    logger: Logger = Logger()
    config = {
        'info_log_path': 'logs/info.log',
        'debug_log_path': 'logs/debug.log',
        'errors_log_path': 'logs/errors.log',
        'json_log_path': 'logs/log.json'
    }
    logger.initialize_loggers(**config)
    logger.info('This is an info message')
    logger.error('This is an error message')
"""
import logging
import colorama
from typing import Optional, Tuple, Any
from src.utils.jjson import j_loads, j_loads_ns # исправлено использование j_loads
from functools import wraps

class SingletonMeta(type):
    """
    Метакласс для реализации паттерна Singleton.

    Это гарантирует, что существует только один экземпляр класса.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class JsonFormatter(logging.Formatter):
    """
    Пользовательский форматтер для вывода логов в формате JSON.

    Форматирует записи лога в виде JSON-строки.
    """
    def format(self, record: logging.LogRecord) -> str:
        """
        Форматирует запись лога в JSON.

        :param record: Запись лога.
        :return: JSON-представление записи лога.
        """
        log_data = {
            'time': self.formatTime(record, self.datefmt),
            'level': record.levelname,
            'message': record.getMessage(),
            'name': record.name,
        }
        if record.exc_info:
           log_data['exc_info'] = self.formatException(record.exc_info)
        return str(log_data)


class Logger(metaclass=SingletonMeta):
    """
    Основной класс логгера, поддерживающий вывод в консоль, файлы и JSON.

    Предоставляет методы для логирования сообщений различных уровней.
    """
    def __init__(self):
        """
        Инициализирует экземпляр логгера с плейсхолдерами для разных типов логгеров (консоль, файл, JSON).
        """
        self.console_logger = None
        self.info_logger = None
        self.debug_logger = None
        self.error_logger = None
        self.json_logger = None

    def _configure_logger(self, name: str, log_path: str, level: int = logging.DEBUG,
                         formatter: Optional[logging.Formatter] = None, mode: str = 'a') -> logging.Logger:
        """
        Конфигурирует и возвращает экземпляр логгера.

        :param name: Имя логгера.
        :param log_path: Путь к файлу лога.
        :param level: Уровень логирования (по умолчанию logging.DEBUG).
        :param formatter: Пользовательский форматтер (необязательно).
        :param mode: Режим файла (по умолчанию 'a' - append).
        :return: Сконфигурированный экземпляр logging.Logger.
        """
        logger = logging.getLogger(name)
        logger.setLevel(level)
        file_handler = logging.FileHandler(log_path, mode=mode, encoding='utf-8')
        if formatter:
           file_handler.setFormatter(formatter)
        else:
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        return logger

    def initialize_loggers(self, info_log_path: Optional[str] = '', debug_log_path: Optional[str] = '',
                           errors_log_path: Optional[str] = '', json_log_path: Optional[str] = '') -> None:
        """
        Инициализирует логгеры для консоли и файлов (info, debug, error, JSON).

        :param info_log_path: Путь к файлу для info логов (необязательно).
        :param debug_log_path: Путь к файлу для debug логов (необязательно).
        :param errors_log_path: Путь к файлу для error логов (необязательно).
        :param json_log_path: Путь к файлу для JSON логов (необязательно).
        """
        # Настройка консольного логгера
        self.console_logger = logging.getLogger('console')
        self.console_logger.setLevel(logging.DEBUG)
        console_handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)
        self.console_logger.addHandler(console_handler)

        # Настройка файловых логгеров
        if info_log_path:
            self.info_logger = self._configure_logger('info', info_log_path, logging.INFO)
        if debug_log_path:
            self.debug_logger = self._configure_logger('debug', debug_log_path, logging.DEBUG)
        if errors_log_path:
            self.error_logger = self._configure_logger('error', errors_log_path, logging.ERROR)
        if json_log_path:
            json_formatter = JsonFormatter()
            self.json_logger = self._configure_logger('json', json_log_path, formatter=json_formatter)


    def log(self, level: int, message: str, ex: Optional[Exception] = None, exc_info: bool = False,
            color: Optional[Tuple[str, str]] = None) -> None:
        """
        Логирует сообщение на указанном уровне с возможностью указания исключения и цвета.

        :param level: Уровень логирования (например, logging.INFO, logging.DEBUG).
        :param message: Сообщение для логирования.
        :param ex: Исключение для логирования (необязательно).
        :param exc_info: Включать ли информацию об исключении (по умолчанию False).
        :param color: Кортеж с цветом текста и фона для вывода в консоль (необязательно).
        """
        log_message = message

        if color:
            log_message = f"{color[0]}{color[1]}{message}{colorama.Style.RESET_ALL}"

        if self.console_logger:
          self.console_logger.log(level, log_message, exc_info=exc_info)

        if level >= logging.ERROR:
            if self.error_logger:
               self.error_logger.log(level, message, exc_info=exc_info)
        elif level == logging.DEBUG:
            if self.debug_logger:
                self.debug_logger.log(level, message, exc_info=exc_info)
        elif level == logging.INFO:
            if self.info_logger:
                self.info_logger.log(level, message, exc_info=exc_info)

        if self.json_logger:
           self.json_logger.log(level, message, exc_info=exc_info)

        if ex:
            if level >= logging.ERROR:
              if self.error_logger:
                self.error_logger.log(level, f"Exception: {ex}", exc_info=exc_info)
            elif level == logging.DEBUG:
              if self.debug_logger:
                 self.debug_logger.log(level, f"Exception: {ex}", exc_info=exc_info)
            elif level == logging.INFO:
              if self.info_logger:
                self.info_logger.log(level, f"Exception: {ex}", exc_info=exc_info)
            if self.json_logger:
              self.json_logger.log(level, f"Exception: {ex}", exc_info=exc_info)

    def info(self, message: str, ex: Optional[Exception] = None, exc_info: bool = False,
             colors: Optional[Tuple[str, str]] = None) -> None:
        """
        Логирует информационное сообщение.

        :param message: Сообщение для логирования.
        :param ex: Исключение для логирования (необязательно).
        :param exc_info: Включать ли информацию об исключении (по умолчанию False).
        :param colors: Кортеж с цветом текста и фона для вывода в консоль (необязательно).
        """
        self.log(logging.INFO, message, ex, exc_info, colors)

    def success(self, message: str, ex: Optional[Exception] = None, exc_info: bool = False,
                colors: Optional[Tuple[str, str]] = None) -> None:
        """
        Логирует сообщение об успехе.

        :param message: Сообщение для логирования.
        :param ex: Исключение для логирования (необязательно).
        :param exc_info: Включать ли информацию об исключении (по умолчанию False).
        :param colors: Кортеж с цветом текста и фона для вывода в консоль (необязательно).
        """
        self.log(logging.INFO, message, ex, exc_info, colors)

    def warning(self, message: str, ex: Optional[Exception] = None, exc_info: bool = False,
                colors: Optional[Tuple[str, str]] = None) -> None:
        """
        Логирует предупреждающее сообщение.

        :param message: Сообщение для логирования.
        :param ex: Исключение для логирования (необязательно).
        :param exc_info: Включать ли информацию об исключении (по умолчанию False).
        :param colors: Кортеж с цветом текста и фона для вывода в консоль (необязательно).
        """
        self.log(logging.WARNING, message, ex, exc_info, colors)

    def debug(self, message: str, ex: Optional[Exception] = None, exc_info: bool = True,
              colors: Optional[Tuple[str, str]] = None) -> None:
        """
        Логирует отладочное сообщение.

        :param message: Сообщение для логирования.
        :param ex: Исключение для логирования (необязательно).
        :param exc_info: Включать ли информацию об исключении (по умолчанию True).
        :param colors: Кортеж с цветом текста и фона для вывода в консоль (необязательно).
        """
        self.log(logging.DEBUG, message, ex, exc_info, colors)

    def error(self, message: str, ex: Optional[Exception] = None, exc_info: bool = True,
              colors: Optional[Tuple[str, str]] = None) -> None:
        """
        Логирует сообщение об ошибке.

        :param message: Сообщение для логирования.
        :param ex: Исключение для логирования (необязательно).
        :param exc_info: Включать ли информацию об исключении (по умолчанию True).
        :param colors: Кортеж с цветом текста и фона для вывода в консоль (необязательно).
        """
        self.log(logging.ERROR, message, ex, exc_info, colors)

    def critical(self, message: str, ex: Optional[Exception] = None, exc_info: bool = True,
                 colors: Optional[Tuple[str, str]] = None) -> None:
        """
        Логирует критическое сообщение.

        :param message: Сообщение для логирования.
        :param ex: Исключение для логирования (необязательно).
        :param exc_info: Включать ли информацию об исключении (по умолчанию True).
        :param colors: Кортеж с цветом текста и фона для вывода в консоль (необязательно).
        """
        self.log(logging.CRITICAL, message, ex, exc_info, colors)


# Пример использования
if __name__ == '__main__':
    logger: Logger = Logger()
    config = {
        'info_log_path': 'logs/info.log',
        'debug_log_path': 'logs/debug.log',
        'errors_log_path': 'logs/errors.log',
        'json_log_path': 'logs/log.json'
    }
    logger.initialize_loggers(**config)

    logger.info('This is an info message')
    logger.success('This is a success message')
    logger.warning('This is a warning message')
    logger.debug('This is a debug message')
    logger.error('This is an error message')
    logger.critical('This is a critical message')

    logger.info('This message will be green', colors=(colorama.Fore.GREEN, colorama.Back.BLACK))
    logger.error('This message will have a red background', colors=(colorama.Fore.WHITE, colorama.Back.RED))
```