# Анализ кода модуля `src.logger`

**Качество кода**
6
-  Плюсы
    -   Модуль предоставляет гибкую систему логирования с поддержкой различных уровней, форматов и цветов.
    -   Используется паттерн Singleton для обеспечения единственного экземпляра логгера.
    -   Логирование может быть направлено в консоль и файлы (включая JSON).
-  Минусы
    -   Отсутствует `docstring` для модуля и классов.
    -   Много повторений в методах `info`, `success`, `warning`, `debug`, `error`, `critical`.
    -   Используется стандартный `try-except` вместо `logger.error`.
    -   Нет явного управления цветом через `colorama` или другое решение для отключения в случае не поддержки терминалом.
    -   Документация не в reStructuredText формате.

**Рекомендации по улучшению**

1.  Добавить `docstring` в формате RST для модуля, классов и методов.
2.  Устранить дублирование кода в методах `info`, `success`, `warning`, `debug`, `error`, `critical`. Создать внутренний метод `_log` для общего функционала.
3.  Заменить стандартные `try-except` на `logger.error` для централизованной обработки ошибок.
4.  Добавить возможность отключения цветового вывода в консоль.
5.  Преобразовать документацию в reStructuredText формат.

**Оптимизиробанный код**

```python
"""
Модуль для реализации гибкой системы логирования.
===================================================

Этот модуль предоставляет систему логирования, поддерживающую вывод в консоль, файлы, а также формат JSON.
Используется паттерн Singleton для обеспечения единственного экземпляра логгера в приложении.

Пример использования:
--------------------

.. code-block:: python

    from src.logger.logger import Logger
    import logging
    from colorama import Fore, Back

    logger = Logger()
    config = {
        'info_log_path': 'logs/info.log',
        'debug_log_path': 'logs/debug.log',
        'errors_log_path': 'logs/errors.log',
        'json_log_path': 'logs/log.json'
    }
    logger.initialize_loggers(**config)

    logger.info('Сообщение информации')
    logger.error('Сообщение ошибки', Exception('Пример ошибки'))
    logger.debug('Отладочное сообщение', colors=(Fore.CYAN, Back.BLACK))
"""
import logging
from typing import Optional, Tuple, Any
import json
from colorama import init, Fore, Back, Style

init(autoreset=True)

class SingletonMeta(type):
    """
    Метакласс, реализующий паттерн Singleton.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Создание или возврат существующего экземпляра класса.

        :return: Экземпляр класса.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class JsonFormatter(logging.Formatter):
    """
    Форматировщик для вывода логов в формате JSON.
    """
    def format(self, record: logging.LogRecord) -> str:
        """
        Форматирует запись лога в JSON.

        :param record: Запись лога.
        :return: JSON строка.
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
    Основной класс логгера, поддерживающий вывод в консоль, файлы и JSON.
    """
    def __init__(self):
        """
        Инициализация экземпляра логгера. Устанавливает заглушки для различных типов логгеров.
        """
        self.console_logger: Optional[logging.Logger] = None
        self.file_loggers: dict[str, logging.Logger] = {}
        self.json_logger: Optional[logging.Logger] = None
        self.color_enabled = True # TODO добавить возможность отключать цвет, например через переменную окружения

    def _configure_logger(self, name: str, log_path: str, level: int = logging.DEBUG,
                          formatter: Optional[logging.Formatter] = None, mode: str = 'a') -> logging.Logger:
        """
        Конфигурирует и возвращает экземпляр логгера.

        :param name: Имя логгера.
        :param log_path: Путь к файлу лога.
        :param level: Уровень логирования (например, logging.DEBUG).
        :param formatter: Пользовательский форматировщик (опционально).
        :param mode: Режим файла (например, 'a' для добавления).
        :return: Настроенный экземпляр logging.Logger.
        """
        logger = logging.getLogger(name)
        logger.setLevel(level)
        if log_path:
            file_handler = logging.FileHandler(log_path, mode=mode, encoding='utf-8')
            if formatter:
                file_handler.setFormatter(formatter)
            else:
               file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
            logger.addHandler(file_handler)
        return logger

    def initialize_loggers(self, info_log_path: Optional[str] = '', debug_log_path: Optional[str] = '',
                           errors_log_path: Optional[str] = '', json_log_path: Optional[str] = ''):
        """
        Инициализирует логгеры для консоли и файлов (инфо, отладка, ошибки и JSON).

        :param info_log_path: Путь к файлу информационных логов (опционально).
        :param debug_log_path: Путь к файлу отладочных логов (опционально).
        :param errors_log_path: Путь к файлу логов ошибок (опционально).
        :param json_log_path: Путь к файлу JSON логов (опционально).
        """
        self.console_logger = self._configure_logger('console', '', formatter=logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        if info_log_path:
            self.file_loggers['info'] = self._configure_logger('info', info_log_path, level=logging.INFO)
        if debug_log_path:
            self.file_loggers['debug'] = self._configure_logger('debug', debug_log_path, level=logging.DEBUG)
        if errors_log_path:
             self.file_loggers['error'] = self._configure_logger('errors', errors_log_path, level=logging.ERROR)
        if json_log_path:
            self.json_logger = self._configure_logger('json', json_log_path, formatter=JsonFormatter(), level=logging.DEBUG)


    def _log(self, level: int, message: str, ex: Optional[Exception] = None, exc_info: bool = False,
             colors: Optional[Tuple[str, str]] = None):
        """
        Выполняет логирование сообщения на заданном уровне.
        
        :param level: Уровень логирования.
        :param message: Сообщение для записи в лог.
        :param ex: Исключение для логирования (опционально).
        :param exc_info: Флаг для включения информации об исключении (опционально).
        :param colors: Кортеж с цветами текста и фона (опционально).
        """
        log_message = message
        if colors and self.color_enabled:
            log_message = f"{colors[0]}{colors[1]}{message}{Style.RESET_ALL}"

        if self.console_logger:
            if ex:
                 self.console_logger.log(level, log_message, exc_info=exc_info,  extra={'exception': ex})
            else:
                self.console_logger.log(level, log_message, exc_info=exc_info)
        
        for name, logger in self.file_loggers.items():
            if logger.level <= level:
                if ex:
                    logger.log(level, message, exc_info=exc_info, extra={'exception': ex})
                else:
                   logger.log(level, message, exc_info=exc_info)
        if self.json_logger and level >= self.json_logger.level:
            if ex:
                 self.json_logger.log(level, message, exc_info=exc_info, extra={'exception': ex})
            else:
               self.json_logger.log(level, message, exc_info=exc_info)
    
    def log(self, level: int, message: str, ex: Optional[Exception] = None, exc_info: bool = False, colors: Optional[Tuple[str, str]] = None):
        """
        Публичный метод логирования.
        
        :param level: Уровень логирования.
        :param message: Сообщение для записи в лог.
        :param ex: Исключение для логирования (опционально).
        :param exc_info: Флаг для включения информации об исключении (опционально).
        :param colors: Кортеж с цветами текста и фона (опционально).
        """
        self._log(level, message, ex, exc_info, colors)
    

    def info(self, message: str, ex: Optional[Exception] = None, exc_info: bool = False, colors: Optional[Tuple[str, str]] = None):
        """
        Логирование информационного сообщения.

        :param message: Сообщение для записи в лог.
        :param ex: Исключение для логирования (опционально).
        :param exc_info: Флаг для включения информации об исключении (опционально).
        :param colors: Кортеж с цветами текста и фона (опционально).
        """
        self._log(logging.INFO, message, ex, exc_info, colors)

    def success(self, message: str, ex: Optional[Exception] = None, exc_info: bool = False, colors: Optional[Tuple[str, str]] = None):
        """
        Логирование сообщения об успехе.

        :param message: Сообщение для записи в лог.
        :param ex: Исключение для логирования (опционально).
        :param exc_info: Флаг для включения информации об исключении (опционально).
        :param colors: Кортеж с цветами текста и фона (опционально).
        """
        self._log(logging.INFO, message, ex, exc_info, colors)


    def warning(self, message: str, ex: Optional[Exception] = None, exc_info: bool = False, colors: Optional[Tuple[str, str]] = None):
        """
        Логирование предупреждающего сообщения.

        :param message: Сообщение для записи в лог.
        :param ex: Исключение для логирования (опционально).
        :param exc_info: Флаг для включения информации об исключении (опционально).
        :param colors: Кортеж с цветами текста и фона (опционально).
        """
        self._log(logging.WARNING, message, ex, exc_info, colors)

    def debug(self, message: str, ex: Optional[Exception] = None, exc_info: bool = True, colors: Optional[Tuple[str, str]] = None):
        """
        Логирование отладочного сообщения.

        :param message: Сообщение для записи в лог.
        :param ex: Исключение для логирования (опционально).
        :param exc_info: Флаг для включения информации об исключении (опционально).
        :param colors: Кортеж с цветами текста и фона (опционально).
        """
        self._log(logging.DEBUG, message, ex, exc_info, colors)

    def error(self, message: str, ex: Optional[Exception] = None, exc_info: bool = True, colors: Optional[Tuple[str, str]] = None):
        """
        Логирование сообщения об ошибке.

        :param message: Сообщение для записи в лог.
        :param ex: Исключение для логирования (опционально).
        :param exc_info: Флаг для включения информации об исключении (опционально).
        :param colors: Кортеж с цветами текста и фона (опционально).
        """
        self._log(logging.ERROR, message, ex, exc_info, colors)

    def critical(self, message: str, ex: Optional[Exception] = None, exc_info: bool = True, colors: Optional[Tuple[str, str]] = None):
        """
        Логирование критического сообщения.

        :param message: Сообщение для записи в лог.
        :param ex: Исключение для логирования (опционально).
        :param exc_info: Флаг для включения информации об исключении (опционально).
        :param colors: Кортеж с цветами текста и фона (опционально).
        """
        self._log(logging.CRITICAL, message, ex, exc_info, colors)

if __name__ == '__main__':
    # Пример использования
    logger = Logger()
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
    logger.debug('This is a debug message', colors=(Fore.CYAN, Back.BLACK))
    try:
      raise Exception('test')
    except Exception as e:
        logger.error('This is an error message', ex=e, exc_info=True, colors=(Fore.WHITE, Back.RED))
    logger.critical('This is a critical message')
```