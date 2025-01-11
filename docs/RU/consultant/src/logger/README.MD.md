# Анализ кода модуля `src.logger`

**Качество кода: 8/10**

- **Плюсы**
    - Модуль предоставляет гибкую систему логирования с поддержкой консоли, файлов и JSON.
    - Используется паттерн Singleton для обеспечения единственного экземпляра логгера.
    - Поддерживаются различные уровни логирования и форматирование сообщений с цветом для консоли.
    - Код достаточно хорошо документирован с использованием RST.
    - Наличие примеров использования облегчает понимание работы модуля.
- **Минусы**
    - Отсутствует описание модуля в начале файла.
    - Некоторые комментарии не соответствуют формату, описанному в инструкции.
    - Есть потенциал для улучшения форматирования документации функций.
    - Нет проверки корректности входных путей.
    - Использование `Optional[int] = logging.DEBUG` не очень информативно, лучше использовать `Optional[int] = logging.DEBUG`

**Рекомендации по улучшению**

1.  Добавить описание модуля в начале файла.
2.  Улучшить документацию функций, используя RST-формат и придерживаясь стандартов docstring в Python.
3.  Уточнить параметры функций в RST документации, использовать более информативные типы данных.
4.  Проверить и добавить отсутствующие импорты.
5.  Реализовать обработку ошибок и добавить логирование в методы `_configure_logger` и `initialize_loggers`.
6.  Добавить проверки на корректность входных путей для создания файлов логов.
7.  Переписать примеры использования, добавив импорт и более подробные случаи.
8.  Использовать константы для уровней логирования (например, DEBUG, INFO, ERROR).

**Оптимизированный код**
```python
"""
Модуль для гибкого логирования в консоль, файл и JSON.
=========================================================================================

Модуль `src.logger` предоставляет настраиваемую систему логирования с поддержкой вывода в консоль, файлы и JSON.
Использует паттерн Singleton для гарантии единственного экземпляра логгера в приложении.
Логгер поддерживает различные уровни важности (INFO, ERROR, DEBUG и т.д.) и вывод в консоль с цветами.
Есть возможность настраивать формат вывода и записывать логи в различные файлы.

Пример использования
--------------------

Инициализация логгера и запись сообщений разных уровней:

.. code-block:: python

    from src.logger.logger import Logger
    import logging
    import colorama

    # Инициализация логгера
    logger = Logger()
    config = {
        'info_log_path': 'logs/info.log',
        'debug_log_path': 'logs/debug.log',
        'errors_log_path': 'logs/errors.log',
        'json_log_path': 'logs/log.json'
    }
    logger.initialize_loggers(**config)

    # Логирование сообщений разных уровней
    logger.info('Информационное сообщение')
    logger.success('Успешное сообщение')
    logger.warning('Предупреждение')
    logger.debug('Отладочное сообщение')
    logger.error('Сообщение об ошибке')
    logger.critical('Критическое сообщение')

    # Логирование с пользовательскими цветами
    logger.info('Зеленый текст', colors=(colorama.Fore.GREEN, colorama.Back.BLACK))
    logger.error('Красный фон', colors=(colorama.Fore.WHITE, colorama.Back.RED))
"""
import logging
from typing import Optional, Tuple
import json
import colorama
from pathlib import Path

# Импорт логгера из src.logger
from src.logger.logger import logger


class SingletonMeta(type):
    """
    Метакласс для реализации Singleton.

    Этот метакласс гарантирует, что у класса будет только один экземпляр.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Возвращает существующий экземпляр класса или создает новый, если его нет.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class JsonFormatter(logging.Formatter):
    """
    Форматтер для логирования в JSON.

    Этот класс форматирует записи логов в виде JSON-строки.
    """

    def format(self, record: logging.LogRecord) -> str:
        """
        Форматирует запись лога в JSON.
        
        Args:
            record (logging.LogRecord): Запись лога для форматирования.
        Returns:
            str: JSON-строка с данными лога.
        """
        log_data = {
            'time': self.formatTime(record, self.datefmt),
            'level': record.levelname,
            'message': record.getMessage(),
            'name': record.name,
        }
        if record.exc_info:
            log_data['exc_info'] = self.formatException(record.exc_info)
        return json.dumps(log_data)


class Logger(metaclass=SingletonMeta):
    """
    Основной класс для логирования.

    Поддерживает логирование в консоль, файлы и JSON.
    """
    _console_logger: Optional[logging.Logger] = None
    _file_loggers: dict[str, Optional[logging.Logger]] = {}
    
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL

    def __init__(self):
        """
        Инициализирует экземпляр логгера.
        
        Создает пустые плейсхолдеры для различных типов логгеров.
        """
        self._console_logger = None
        self._file_loggers = {}


    def _configure_logger(self, name: str, log_path: str, level: int = logging.DEBUG, formatter: Optional[logging.Formatter] = None, mode: str = 'a') -> logging.Logger:
        """
        Настраивает и возвращает экземпляр логгера.
        
        Args:
           name (str): Имя логгера.
           log_path (str): Путь к файлу лога.
           level (int, optional): Уровень логирования. Defaults to logging.DEBUG.
           formatter (logging.Formatter, optional): Форматтер лога. Defaults to None.
           mode (str, optional): Режим файла. Defaults to 'a'.
        Returns:
            logging.Logger: Настроенный экземпляр логгера.
        Raises:
           Exception: При возникновении ошибки при создании файла или настройке логгера.
        """
        try:
            log_path = Path(log_path) # Преобразует путь к файлу
            log_path.parent.mkdir(parents=True, exist_ok=True) # Создает родительские директории
            handler = logging.FileHandler(str(log_path), mode=mode, encoding='utf-8') # Создает обработчик файла
            handler.setFormatter(formatter or logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')) # Устанавливает форматтер для обработчика
            logger_instance = logging.getLogger(name)  # Получает экземпляр логгера по имени
            logger_instance.setLevel(level)  # Устанавливает уровень логирования
            logger_instance.addHandler(handler)  # Добавляет обработчик к логгеру
            return logger_instance # Возвращает настроенный логгер
        except Exception as ex:
            # Логирование ошибки при настройке логгера
            logger.error(f'Ошибка при конфигурации логгера {name}', ex=ex, exc_info=True)
            ...
            return logging.getLogger(name)


    def initialize_loggers(self, info_log_path: Optional[str] = '', debug_log_path: Optional[str] = '', errors_log_path: Optional[str] = '', json_log_path: Optional[str] = '') -> None:
        """
        Инициализирует логгеры для консоли и файлов.
        
        Args:
           info_log_path (str, optional): Путь к файлу информационных логов. Defaults to ''.
           debug_log_path (str, optional): Путь к файлу отладочных логов. Defaults to ''.
           errors_log_path (str, optional): Путь к файлу логов ошибок. Defaults to ''.
           json_log_path (str, optional): Путь к файлу JSON логов. Defaults to ''.
        Raises:
           Exception: При возникновении ошибки во время инициализации логгеров
        """
        try:
           # Настраивает логгер для консоли
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
            self._console_logger = logging.getLogger('console')
            self._console_logger.setLevel(logging.DEBUG)
            self._console_logger.addHandler(console_handler)

            # Настраивает файловые логгеры, если указаны пути
            if info_log_path:
                self._file_loggers['info'] = self._configure_logger('info', info_log_path, level=logging.INFO)
            if debug_log_path:
                self._file_loggers['debug'] = self._configure_logger('debug', debug_log_path, level=logging.DEBUG)
            if errors_log_path:
                self._file_loggers['errors'] = self._configure_logger('errors', errors_log_path, level=logging.ERROR)
            if json_log_path:
                json_formatter = JsonFormatter()
                self._file_loggers['json'] = self._configure_logger('json', json_log_path, formatter=json_formatter)

        except Exception as ex:
           # Логирование ошибки инициализации логгеров
           logger.error('Ошибка инициализации логгеров', ex=ex, exc_info=True)
           ...


    def log(self, level: int, message: str, ex: Optional[Exception] = None, exc_info: bool = False, color: Optional[Tuple[str, str]] = None) -> None:
        """
        Логирует сообщение на указанном уровне.
        
        Args:
            level (int): Уровень логирования (например, logging.INFO, logging.DEBUG, logging.ERROR).
            message (str): Сообщение для логирования.
            ex (Exception, optional): Исключение для логирования. Defaults to None.
            exc_info (bool, optional): Включать ли информацию об исключении. Defaults to False.
            color (Tuple[str, str], optional): Кортеж с цветами текста и фона для консольного вывода. Defaults to None.
        """
        if self._console_logger:
           # Форматирует сообщение для консоли с цветом
            if color:
                colored_message = f'{color[0]}{color[1]}{message}{colorama.Style.RESET_ALL}'
            else:
                colored_message = message
            self._console_logger.log(level, colored_message, exc_info=exc_info)

        # Логирует сообщение в соответствующие файловые логгеры
        if level == logging.INFO and 'info' in self._file_loggers and self._file_loggers['info']:
            self._file_loggers['info'].log(level, message, exc_info=exc_info)
        elif level == logging.DEBUG and 'debug' in self._file_loggers and self._file_loggers['debug']:
            self._file_loggers['debug'].log(level, message, exc_info=exc_info)
        elif level >= logging.ERROR and 'errors' in self._file_loggers and self._file_loggers['errors']:
            self._file_loggers['errors'].log(level, message, exc_info=exc_info)
        elif 'json' in self._file_loggers and self._file_loggers['json']:
            self._file_loggers['json'].log(level, message, exc_info=exc_info)
        if ex:
            logger.error(f'Исключение: {ex}', exc_info=exc_info)

    def info(self, message: str, ex: Optional[Exception] = None, exc_info: bool = False, colors: Optional[Tuple[str, str]] = None) -> None:
        """
        Логирует информационное сообщение.
        
        Args:
            message (str): Информационное сообщение для логирования.
            ex (Exception, optional): Исключение для логирования. Defaults to None.
            exc_info (bool, optional): Включать ли информацию об исключении. Defaults to False.
            colors (Tuple[str, str], optional): Кортеж с цветами текста и фона для консольного вывода. Defaults to None.
        """
        self.log(logging.INFO, message, ex=ex, exc_info=exc_info, color=colors)

    def success(self, message: str, ex: Optional[Exception] = None, exc_info: bool = False, colors: Optional[Tuple[str, str]] = None) -> None:
        """
        Логирует сообщение об успехе.
        
        Args:
            message (str): Сообщение об успехе для логирования.
            ex (Exception, optional): Исключение для логирования. Defaults to None.
            exc_info (bool, optional): Включать ли информацию об исключении. Defaults to False.
            colors (Tuple[str, str], optional): Кортеж с цветами текста и фона для консольного вывода. Defaults to None.
        """
        self.log(logging.INFO, message, ex=ex, exc_info=exc_info, color=colors)

    def warning(self, message: str, ex: Optional[Exception] = None, exc_info: bool = False, colors: Optional[Tuple[str, str]] = None) -> None:
        """
        Логирует предупреждение.
        
        Args:
            message (str): Предупреждение для логирования.
            ex (Exception, optional): Исключение для логирования. Defaults to None.
            exc_info (bool, optional): Включать ли информацию об исключении. Defaults to False.
            colors (Tuple[str, str], optional): Кортеж с цветами текста и фона для консольного вывода. Defaults to None.
        """
        self.log(logging.WARNING, message, ex=ex, exc_info=exc_info, color=colors)

    def debug(self, message: str, ex: Optional[Exception] = None, exc_info: bool = True, colors: Optional[Tuple[str, str]] = None) -> None:
        """
        Логирует отладочное сообщение.
        
        Args:
            message (str): Отладочное сообщение для логирования.
            ex (Exception, optional): Исключение для логирования. Defaults to None.
            exc_info (bool, optional): Включать ли информацию об исключении. Defaults to True.
            colors (Tuple[str, str], optional): Кортеж с цветами текста и фона для консольного вывода. Defaults to None.
        """
        self.log(logging.DEBUG, message, ex=ex, exc_info=exc_info, color=colors)

    def error(self, message: str, ex: Optional[Exception] = None, exc_info: bool = True, colors: Optional[Tuple[str, str]] = None) -> None:
        """
        Логирует сообщение об ошибке.
        
        Args:
            message (str): Сообщение об ошибке для логирования.
            ex (Exception, optional): Исключение для логирования. Defaults to None.
            exc_info (bool, optional): Включать ли информацию об исключении. Defaults to True.
            colors (Tuple[str, str], optional): Кортеж с цветами текста и фона для консольного вывода. Defaults to None.
        """
        self.log(logging.ERROR, message, ex=ex, exc_info=exc_info, color=colors)

    def critical(self, message: str, ex: Optional[Exception] = None, exc_info: bool = True, colors: Optional[Tuple[str, str]] = None) -> None:
        """
        Логирует критическое сообщение.
        
        Args:
            message (str): Критическое сообщение для логирования.
            ex (Exception, optional): Исключение для логирования. Defaults to None.
            exc_info (bool, optional): Включать ли информацию об исключении. Defaults to True.
            colors (Tuple[str, str], optional): Кортеж с цветами текста и фона для консольного вывода. Defaults to None.
        """
        self.log(logging.CRITICAL, message, ex=ex, exc_info=exc_info, color=colors)

```