# Анализ кода модуля `src.logger`

**Качество кода**
9
 -  Плюсы
    -   Хорошая документация в формате `markdown`.
    -   Присутствует описание модуля и классов.
    -   Описаны функции и параметры с их назначением.
    -   Примеры использования логирования.
 -  Минусы
    -  Документация в формате `markdown`, а не в `RST`.
    -  Отсутствует docstring для классов и функций в самом коде.
    -  Не используется `from src.logger.logger import logger` для логирования.
    -  Не везде используются `logger.error` вместо try-except.

**Рекомендации по улучшению**

1.  Переписать документацию в формате `reStructuredText (RST)`.
2.  Добавить docstring для классов, методов и функций в формате `RST`.
3.  Использовать `from src.logger.logger import logger` для логирования ошибок.
4.  Избегать избыточного использования стандартных блоков `try-except`, предпочитая обработку ошибок с помощью `logger.error`.
5.  Добавить обработку исключений при инициализации логгеров.
6.  Внести комментарии к коду в стиле `RST`.

**Оптимизированный код**

```python
"""
Модуль для реализации системы логирования.
=========================================================================================

Этот модуль предоставляет гибкую систему логирования, поддерживающую вывод в консоль, файлы и формат JSON.
Используется паттерн Singleton для гарантии единственного экземпляра логгера в приложении.

Пример использования
--------------------

.. code-block:: python

    from src.logger.logger import Logger

    logger = Logger()
    config = {
        'info_log_path': 'logs/info.log',
        'debug_log_path': 'logs/debug.log',
        'errors_log_path': 'logs/errors.log',
        'json_log_path': 'logs/log.json'
    }
    logger.initialize_loggers(**config)
    logger.info('This is an info message')
    logger.error('This is an error message', Exception('Test error'))
"""
import logging
from typing import Optional, Tuple
import json
import colorama
from src.utils.jjson import j_loads_ns
from functools import wraps
from src.logger.logger import logger

class SingletonMeta(type):
    """
    Метакласс, реализующий паттерн Singleton.

    Это гарантирует, что у класса будет только один экземпляр.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Создает или возвращает существующий экземпляр класса.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class JsonFormatter(logging.Formatter):
    """
    Форматировщик для вывода логов в формате JSON.

    Этот класс преобразует записи лога в формат JSON.
    """
    def format(self, record):
        """
        Форматирует запись лога в JSON.

        :param record: Запись лога.
        :return: JSON-представление записи лога.
        """
        log_record = {
            'time': self.formatTime(record, self.datefmt),
            'level': record.levelname,
            'message': record.getMessage(),
            'name': record.name,
        }
        if record.exc_info:
             log_record['exc_info'] = self.formatException(record.exc_info)
        return json.dumps(log_record, ensure_ascii=False)

class Logger(metaclass=SingletonMeta):
    """
    Основной класс логгера.

    Поддерживает логирование в консоль, файлы и JSON.
    """
    def __init__(self):
        """
        Инициализирует экземпляр Logger.

        Создает placeholders для различных типов логгеров (консоль, файл, JSON).
        """
        self.console_logger = None
        self.info_logger = None
        self.debug_logger = None
        self.error_logger = None
        self.json_logger = None
        self.config = j_loads_ns('config.json') or {}

    def _configure_logger(self, name: str, log_path: str, level: Optional[int] = logging.DEBUG, formatter: Optional[logging.Formatter] = None, mode: Optional[str] = 'a') -> logging.Logger:
        """
        Конфигурирует и возвращает экземпляр логгера.

        :param name: Имя логгера.
        :param log_path: Путь к файлу лога.
        :param level: Уровень логирования, например, logging.DEBUG. По умолчанию logging.DEBUG.
        :param formatter: Кастомный форматировщик (опционально).
        :param mode: Режим открытия файла, например 'a' для добавления (по умолчанию).
        :return: Сконфигурированный экземпляр logging.Logger.
        """
        logger = logging.getLogger(name)
        logger.setLevel(level)
        if log_path:
            try:
                file_handler = logging.FileHandler(log_path, mode=mode, encoding='utf-8')
                if formatter:
                    file_handler.setFormatter(formatter)
                else:
                    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
                    file_handler.setFormatter(formatter)
                logger.addHandler(file_handler)
            except Exception as ex:
                print(f'Ошибка инициализации файлового логгера {log_path=}', ex)
        else:
            print(f'Логер {name} не инициализирован')
        return logger

    def initialize_loggers(self, info_log_path: Optional[str] = None, debug_log_path: Optional[str] = None, errors_log_path: Optional[str] = None, json_log_path: Optional[str] = None):
        """
        Инициализирует логгеры для консольного и файлового логирования (info, debug, error, JSON).

        :param info_log_path: Путь к файлу информационных логов (опционально).
        :param debug_log_path: Путь к файлу дебаг логов (опционально).
        :param errors_log_path: Путь к файлу логов ошибок (опционально).
        :param json_log_path: Путь к файлу JSON логов (опционально).
        """
        try:
            # Код конфигурирует основной логгер для консоли
            self.console_logger = self._configure_logger(
                'console',
                None,
                formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            )

            # Код конфигурирует логгер для информационных сообщений
            self.info_logger = self._configure_logger(
                'info',
                info_log_path or self.config.get('info_log_path'),
                level=logging.INFO
            )

            # Код конфигурирует логгер для дебаг сообщений
            self.debug_logger = self._configure_logger(
                'debug',
                debug_log_path or self.config.get('debug_log_path'),
                level=logging.DEBUG
            )

            # Код конфигурирует логгер для ошибок
            self.error_logger = self._configure_logger(
                'error',
                errors_log_path or self.config.get('errors_log_path'),
                level=logging.ERROR
            )

            # Код конфигурирует логгер для JSON
            self.json_logger = self._configure_logger(
                'json',
                json_log_path or self.config.get('json_log_path'),
                formatter = JsonFormatter(),
            )
        except Exception as ex:
             print(f'Ошибка инициализации логгеров', ex)

    def log(self, level, message, ex=None, exc_info=False, color: Optional[Tuple[str, str]] = None):
        """
        Логирует сообщение на указанном уровне (например, INFO, DEBUG, ERROR) с опциональным исключением и цветовым форматированием.

        :param level: Уровень логирования (например, logging.INFO, logging.DEBUG).
        :param message: Сообщение лога.
        :param ex: Опциональное исключение для логирования.
        :param exc_info: Включать ли информацию об исключении (по умолчанию False).
        :param color: Кортеж с цветом текста и фона для консольного вывода (опционально).
        """
        log_message = message
        if ex:
            log_message = f'{message}. {ex}'
        if color and self.console_logger:
            # Код добавляет цветовое форматирование
            colored_message = f'{color[0]}{color[1]}{log_message}{colorama.Style.RESET_ALL}'
            self.console_logger.log(level, colored_message, exc_info=exc_info)
        else:
            if self.console_logger:
                # Код выполняет логирование без цветового оформления
                 self.console_logger.log(level, log_message, exc_info=exc_info)

        if level >= logging.ERROR and self.error_logger:
             # Код логирует ошибки
             self.error_logger.log(level, log_message, exc_info=exc_info)
        if level == logging.DEBUG and self.debug_logger:
            # Код логирует отладочные сообщения
            self.debug_logger.log(level, log_message, exc_info=exc_info)
        if level == logging.INFO and self.info_logger:
            # Код логирует информационные сообщения
            self.info_logger.log(level, log_message, exc_info=exc_info)
        if self.json_logger:
             # Код логирует в JSON формат
            self.json_logger.log(level, log_message, exc_info=exc_info)

    def info(self, message, ex=None, exc_info=False, colors: Optional[Tuple[str, str]] = None):
        """
        Логирует информационное сообщение.

        :param message: Информационное сообщение для логирования.
        :param ex: Опциональное исключение для логирования.
        :param exc_info: Включать ли информацию об исключении (по умолчанию False).
        :param colors: Кортеж значений цвета для сообщения (опционально).
        """
        self.log(logging.INFO, message, ex, exc_info, colors)

    def success(self, message, ex=None, exc_info=False, colors: Optional[Tuple[str, str]] = None):
        """
        Логирует сообщение об успехе.

        :param message: Сообщение об успехе для логирования.
        :param ex: Опциональное исключение для логирования.
        :param exc_info: Включать ли информацию об исключении (по умолчанию False).
        :param colors: Кортеж значений цвета для сообщения (опционально).
        """
        self.log(logging.INFO, message, ex, exc_info, colors)

    def warning(self, message, ex=None, exc_info=False, colors: Optional[Tuple[str, str]] = None):
        """
        Логирует предупреждающее сообщение.

        :param message: Предупреждающее сообщение для логирования.
        :param ex: Опциональное исключение для логирования.
        :param exc_info: Включать ли информацию об исключении (по умолчанию False).
        :param colors: Кортеж значений цвета для сообщения (опционально).
        """
        self.log(logging.WARNING, message, ex, exc_info, colors)

    def debug(self, message, ex=None, exc_info=True, colors: Optional[Tuple[str, str]] = None):
        """
        Логирует сообщение отладки.

        :param message: Сообщение отладки для логирования.
        :param ex: Опциональное исключение для логирования.
        :param exc_info: Включать ли информацию об исключении (по умолчанию True).
        :param colors: Кортеж значений цвета для сообщения (опционально).
        """
        self.log(logging.DEBUG, message, ex, exc_info, colors)

    def error(self, message, ex=None, exc_info=True, colors: Optional[Tuple[str, str]] = None):
         """
         Логирует сообщение об ошибке.

         :param message: Сообщение об ошибке для логирования.
         :param ex: Опциональное исключение для логирования.
         :param exc_info: Включать ли информацию об исключении (по умолчанию True).
         :param colors: Кортеж значений цвета для сообщения (опционально).
         """
         self.log(logging.ERROR, message, ex, exc_info, colors)

    def critical(self, message, ex=None, exc_info=True, colors: Optional[Tuple[str, str]] = None):
        """
        Логирует критическое сообщение.

        :param message: Критическое сообщение для логирования.
        :param ex: Опциональное исключение для логирования.
        :param exc_info: Включать ли информацию об исключении (по умолчанию True).
        :param colors: Кортеж значений цвета для сообщения (опционально).
        """
        self.log(logging.CRITICAL, message, ex, exc_info, colors)

if __name__ == '__main__':
    colorama.init()
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
    logger.error('This is an error message', Exception('Test error'))
    logger.critical('This is a critical message')
    logger.info('This message will be green', colors=(colorama.Fore.GREEN, colorama.Back.BLACK))
    logger.error('This message will have a red background', colors=(colorama.Fore.WHITE, colorama.Back.RED))
```