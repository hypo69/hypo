# Анализ кода модуля `src.logger`

**Качество кода**
8
- Плюсы
    - Документация хорошо структурирована и предоставляет полное описание модуля, классов, функций и их параметров.
    - Присутствует описание настройки логгера, уровней логирования и форматов вывода.
    - Есть примеры использования, которые помогают понять, как использовать логгер.
- Минусы
    - Документация представлена в формате Markdown, но должна быть в reStructuredText (RST).
    - Не хватает примеров использования с обработкой исключений и логированием в JSON.
    - Некоторые параметры функций, например, `colors` , требуют более детального объяснения в документации.
    - Описание классов `SingletonMeta` и `JsonFormatter` в основном описании модуля не достаточно детализировано.

**Рекомендации по улучшению**
1.  Переписать документацию в формат reStructuredText (RST) для совместимости со Sphinx.
2.  Добавить более подробное описание классов `SingletonMeta` и `JsonFormatter`.
3.  Включить примеры использования с обработкой исключений и логированием в JSON.
4.  Добавить подробное описание параметра `colors`, а также добавить примеры его использования.
5.  Добавить описание к каждому параметру и возвращаемому значению в docstrings функций.

**Оптимизированный код**

```rst
.. module:: src.logger
   :platform: Unix, Windows
   :synopsis: Модуль для управления логированием в приложении.

.. moduleauthor:: hypotez

    Модуль ``src.logger`` предоставляет гибкую систему логирования, поддерживающую вывод в консоль, запись в файлы и форматирование в JSON.
    Он использует шаблон проектирования Singleton, чтобы гарантировать использование единственного экземпляра логгера в приложении.
    Логгер поддерживает различные уровни логирования (такие как `INFO`, `ERROR`, `DEBUG`) и включает цветное форматирование для консольного вывода.
    Также доступны настройки форматов вывода и управление записью логов в различные файлы.

    :Example:

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
        logger.info('Это информационное сообщение')
        logger.error('Это сообщение об ошибке', exc_info=True)

----

.. contents:: Содержание
    :depth: 2

Классы
-------
    - :class:`SingletonMeta`: Метакласс, реализующий шаблон Singleton для логгера.
    - :class:`JsonFormatter`: Кастомный форматтер для вывода логов в формате JSON.
    - :class:`Logger`: Основной класс логгера.

---

Функции
---------

    .. py:function:: __init__()
        :module: src.logger.logger

        Инициализирует экземпляр класса Logger с плейсхолдерами для различных типов логгеров (консоль, файлы и JSON).

    .. py:function:: _configure_logger(name: str, log_path: str, level: Optional[int] = logging.DEBUG, formatter: Optional[logging.Formatter] = None, mode: Optional[str] = 'a') -> logging.Logger
        :module: src.logger.logger

        Настраивает и возвращает экземпляр логгера.

        :param name: Имя логгера.
        :type name: str
        :param log_path: Путь к файлу логов.
        :type log_path: str
        :param level: Уровень логирования, например, ``logging.DEBUG``. Значение по умолчанию — ``logging.DEBUG``.
        :type level: Optional[int]
        :param formatter: Кастомный форматтер (опционально).
        :type formatter: Optional[logging.Formatter]
        :param mode: Режим работы с файлом, например, ``'a'`` для добавления (значение по умолчанию).
        :type mode: Optional[str]
        :return: Настроенный экземпляр `logging.Logger`.
        :rtype: logging.Logger


    .. py:function:: initialize_loggers(info_log_path: Optional[str] = '', debug_log_path: Optional[str] = '', errors_log_path: Optional[str] = '', json_log_path: Optional[str] = '')
        :module: src.logger.logger

        Инициализирует логгеры для логирования в консоль и файлы (информация, отладка, ошибки и JSON).

        :param info_log_path: Путь к файлу логов информации (опционально).
        :type info_log_path: Optional[str]
        :param debug_log_path: Путь к файлу логов отладки (опционально).
        :type debug_log_path: Optional[str]
        :param errors_log_path: Путь к файлу логов ошибок (опционально).
        :type errors_log_path: Optional[str]
        :param json_log_path: Путь к файлу логов в формате JSON (опционально).
        :type json_log_path: Optional[str]

    .. py:function:: log(level, message, ex=None, exc_info=False, color=None)
        :module: src.logger.logger

        Логирует сообщение на указанном уровне (например, `INFO`, `DEBUG`, `ERROR`) с возможным исключением и цветовым форматированием.

        :param level: Уровень логирования (например, `logging.INFO`, `logging.DEBUG`).
        :type level: int
        :param message: Логируемое сообщение.
        :type message: str
        :param ex: Исключение для логирования (опционально).
        :type ex: Optional[Exception]
        :param exc_info: Включать информацию об исключении (значение по умолчанию — `False`).
        :type exc_info: bool
        :param color: Кортеж цветов текста и фона для консольного вывода (опционально).
        :type color: Optional[tuple]

    .. py:function:: info(message, ex=None, exc_info=False, color=None)
        :module: src.logger.logger
        Логирует информационное сообщение.

        :param message: Логируемое сообщение.
        :type message: str
        :param ex: Исключение для логирования (опционально).
        :type ex: Optional[Exception]
        :param exc_info: Включать информацию об исключении (значение по умолчанию — `False`).
        :type exc_info: bool
        :param color: Кортеж цветов текста и фона для консольного вывода (опционально).
        :type color: Optional[tuple]

    .. py:function:: success(message, ex=None, exc_info=False, color=None)
        :module: src.logger.logger
        Логирует сообщение об успешной операции.

        :param message: Логируемое сообщение.
        :type message: str
        :param ex: Исключение для логирования (опционально).
        :type ex: Optional[Exception]
        :param exc_info: Включать информацию об исключении (значение по умолчанию — `False`).
        :type exc_info: bool
        :param color: Кортеж цветов текста и фона для консольного вывода (опционально).
        :type color: Optional[tuple]

    .. py:function:: warning(message, ex=None, exc_info=False, color=None)
        :module: src.logger.logger
        Логирует предупреждение.

        :param message: Логируемое сообщение.
        :type message: str
        :param ex: Исключение для логирования (опционально).
        :type ex: Optional[Exception]
        :param exc_info: Включать информацию об исключении (значение по умолчанию — `False`).
        :type exc_info: bool
        :param color: Кортеж цветов текста и фона для консольного вывода (опционально).
        :type color: Optional[tuple]

    .. py:function:: debug(message, ex=None, exc_info=False, color=None)
        :module: src.logger.logger
        Логирует сообщение для отладки.

        :param message: Логируемое сообщение.
        :type message: str
        :param ex: Исключение для логирования (опционально).
        :type ex: Optional[Exception]
        :param exc_info: Включать информацию об исключении (значение по умолчанию — `False`).
        :type exc_info: bool
        :param color: Кортеж цветов текста и фона для консольного вывода (опционально).
        :type color: Optional[tuple]

    .. py:function:: error(message, ex=None, exc_info=False, color=None)
        :module: src.logger.logger
        Логирует сообщение об ошибке.

        :param message: Логируемое сообщение.
        :type message: str
        :param ex: Исключение для логирования (опционально).
        :type ex: Optional[Exception]
        :param exc_info: Включать информацию об исключении (значение по умолчанию — `False`).
        :type exc_info: bool
        :param color: Кортеж цветов текста и фона для консольного вывода (опционально).
        :type color: Optional[tuple]

    .. py:function:: critical(message, ex=None, exc_info=False, color=None)
        :module: src.logger.logger
        Логирует критическое сообщение.

        :param message: Логируемое сообщение.
        :type message: str
        :param ex: Исключение для логирования (опционально).
        :type ex: Optional[Exception]
        :param exc_info: Включать информацию об исключении (значение по умолчанию — `False`).
        :type exc_info: bool
        :param color: Кортеж цветов текста и фона для консольного вывода (опционально).
        :type color: Optional[tuple]


---

Параметры логгера
-------------------

Класс `Logger` принимает несколько опциональных параметров для настройки поведения логирования:

-   **Уровень**: Контролирует, какие сообщения будут записаны. Основные уровни:
    -   `logging.DEBUG`: Подробная информация для диагностики.
    -   `logging.INFO`: Общая информация, например, успешные операции.
    -   `logging.WARNING`: Предупреждения, не требующие немедленного действия.
    -   `logging.ERROR`: Сообщения об ошибках.
    -   `logging.CRITICAL`: Критические ошибки, требующие немедленного внимания.

-   **Форматтер**: Определяет формат сообщений. По умолчанию используется `'%(asctime)s - %(levelname)s - %(message)s'`. Можно задать кастомный форматтер, например, для JSON.

-   **Цвета**: Задают цвет текста и фона в консоли. Цвета указываются кортежем:
    -   **Цвет текста**: Например, ``colorama.Fore.RED``.
    -   **Цвет фона**: Например, ``colorama.Back.WHITE``.
        Пример использования: ``colors=(colorama.Fore.GREEN, colorama.Back.BLACK)``

---

Конфигурация для логирования в файл (``config``)
-------------------------------------------------

Для записи сообщений в файл можно указать пути в конфигурации.

.. code-block:: python

    config = {
        'info_log_path': 'logs/info.log',
        'debug_log_path': 'logs/debug.log',
        'errors_log_path': 'logs/errors.log',
        'json_log_path': 'logs/log.json'
    }

---

Примеры использования
---------------------

#### 1. Инициализация логгера:

.. code-block:: python

    from src.logger.logger import Logger
    import colorama
    logger: Logger = Logger()
    config = {
        'info_log_path': 'logs/info.log',
        'debug_log_path': 'logs/debug.log',
        'errors_log_path': 'logs/errors.log',
        'json_log_path': 'logs/log.json'
    }
    logger.initialize_loggers(**config)

#### 2. Логирование сообщений:

.. code-block:: python

    logger.info('Это информационное сообщение')
    logger.success('Это сообщение об успешной операции')
    logger.warning('Это предупреждение')
    logger.debug('Это сообщение для отладки')
    logger.error('Это сообщение об ошибке', exc_info=True)
    logger.critical('Это критическое сообщение')

#### 3. Настройка цветов:

.. code-block:: python

    logger.info('Это сообщение будет зеленым', color=(colorama.Fore.GREEN, colorama.Back.BLACK))
    logger.error('Это сообщение с красным фоном', color=(colorama.Fore.WHITE, colorama.Back.RED), exc_info=True)

#### 4. Логирование в JSON:

.. code-block:: python

    try:
        1/0
    except Exception as ex:
       logger.error('Ошибка деления на ноль', ex=ex, exc_info=True)

---

Модуль `src.logger` предоставляет полноценную систему логирования для Python-приложений. Вы можете настроить логирование в консоль и файлы с различными форматами и цветами, управлять уровнями логирования и обрабатывать исключения. Конфигурация логирования в файлы задается через словарь `config`, что позволяет легко изменять настройки.

```
```python
# -*- coding: utf-8 -*-
"""
Модуль для управления логированием в приложении.
=========================================================================================

Модуль ``src.logger`` предоставляет гибкую систему логирования, поддерживающую вывод в консоль, запись в файлы и форматирование в JSON.
Он использует шаблон проектирования Singleton, чтобы гарантировать использование единственного экземпляра логгера в приложении.
Логгер поддерживает различные уровни логирования (такие как `INFO`, `ERROR`, `DEBUG`) и включает цветное форматирование для консольного вывода.
Также доступны настройки форматов вывода и управление записью логов в различные файлы.

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
    logger.info('Это информационное сообщение')
    logger.error('Это сообщение об ошибке', exc_info=True)
"""
import logging
import json
from typing import Optional, Any
from colorama import Fore, Back, Style  # Added colorama import
# from src.utils.jjson import j_loads, j_dumps  #  j_loads не используется, j_dumps не нужен.

class SingletonMeta(type):
    """
    Метакласс, реализующий шаблон Singleton.

    Этот метакласс гарантирует, что только один экземпляр класса будет создан.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Вызывает метод, проверяет наличие экземпляра и возвращает его.

        Если экземпляр класса уже существует, возвращает его; в противном случае создаёт новый.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class JsonFormatter(logging.Formatter):
    """
    Кастомный форматтер для вывода логов в формате JSON.
    """
    def format(self, record):
        """
        Преобразует запись лога в JSON формат.

        :param record: Запись лога.
        :type record: logging.LogRecord
        :return: Строка, содержащая запись лога в формате JSON.
        :rtype: str
        """
        log_record = {
            'time': self.formatTime(record, self.datefmt),
            'level': record.levelname,
            'message': record.getMessage(),
            'name': record.name,
            'module': record.module,
            'funcName': record.funcName,
            'lineno': record.lineno,
            'path': record.pathname
            }
        if record.exc_info:
            log_record['exc_info'] = self.formatException(record.exc_info)
        return json.dumps(log_record, ensure_ascii=False)

class Logger(metaclass=SingletonMeta):
    """
    Основной класс логгера, поддерживающий логирование в консоль, файлы и в формате JSON.
    """
    def __init__(self):
        """
        Инициализирует экземпляр класса Logger с плейсхолдерами для различных типов логгеров (консоль, файлы и JSON).
        """
        self.console_logger = None
        self.info_logger = None
        self.debug_logger = None
        self.errors_logger = None
        self.json_logger = None
    def _configure_logger(self, name: str, log_path: str, level: Optional[int] = logging.DEBUG, formatter: Optional[logging.Formatter] = None, mode: Optional[str] = 'a') -> logging.Logger:
        """
        Настраивает и возвращает экземпляр логгера.

        :param name: Имя логгера.
        :type name: str
        :param log_path: Путь к файлу логов.
        :type log_path: str
        :param level: Уровень логирования, например, ``logging.DEBUG``. Значение по умолчанию — ``logging.DEBUG``.
        :type level: Optional[int]
        :param formatter: Кастомный форматтер (опционально).
        :type formatter: Optional[logging.Formatter]
        :param mode: Режим работы с файлом, например, ``'a'`` для добавления (значение по умолчанию).
        :type mode: Optional[str]
        :return: Настроенный экземпляр `logging.Logger`.
        :rtype: logging.Logger
        """
        logger = logging.getLogger(name)
        logger.setLevel(level)
        if log_path:
            file_handler = logging.FileHandler(log_path, mode=mode, encoding='utf-8')
            if formatter:
                 file_handler.setFormatter(formatter)
            else:
                formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s') #  Добавил дефолтный форматтер
                file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
        return logger

    def initialize_loggers(self, info_log_path: Optional[str] = '', debug_log_path: Optional[str] = '', errors_log_path: Optional[str] = '', json_log_path: Optional[str] = ''):
        """
        Инициализирует логгеры для логирования в консоль и файлы (информация, отладка, ошибки и JSON).

        :param info_log_path: Путь к файлу логов информации (опционально).
        :type info_log_path: Optional[str]
        :param debug_log_path: Путь к файлу логов отладки (опционально).
        :type debug_log_path: Optional[str]
        :param errors_log_path: Путь к файлу логов ошибок (опционально).
        :type errors_log_path: Optional[str]
        :param json_log_path: Путь к файлу логов в формате JSON (опционально).
        :type json_log_path: Optional[str]
        """
        self.console_logger = self._configure_logger(name='console', log_path=None)
        self.info_logger = self._configure_logger(name='info', log_path=info_log_path, level=logging.INFO)
        self.debug_logger = self._configure_logger(name='debug', log_path=debug_log_path, level=logging.DEBUG)
        self.errors_logger = self._configure_logger(name='errors', log_path=errors_log_path, level=logging.ERROR)
        self.json_logger = self._configure_logger(name='json', log_path=json_log_path, formatter=JsonFormatter())

    def log(self, level: int, message: str, ex: Optional[Exception] = None, exc_info: bool = False, color: Optional[tuple] = None):
        """
        Логирует сообщение на указанном уровне (например, `INFO`, `DEBUG`, `ERROR`) с возможным исключением и цветовым форматированием.

        :param level: Уровень логирования (например, `logging.INFO`, `logging.DEBUG`).
        :type level: int
        :param message: Логируемое сообщение.
        :type message: str
        :param ex: Исключение для логирования (опционально).
        :type ex: Optional[Exception]
        :param exc_info: Включать информацию об исключении (значение по умолчанию — `False`).
        :type exc_info: bool
        :param color: Кортеж цветов текста и фона для консольного вывода (опционально).
        :type color: Optional[tuple]
        """
        log_message = message
        if color:
             log_message = f'{color[0]}{color[1]}{message}{Style.RESET_ALL}'

        if self.console_logger:
            self.console_logger.log(level, log_message, exc_info=exc_info)
        if level == logging.INFO and self.info_logger:
            self.info_logger.log(level, message, exc_info=exc_info)
        elif level == logging.DEBUG and self.debug_logger:
            self.debug_logger.log(level, message, exc_info=exc_info)
        elif level >= logging.ERROR and self.errors_logger:
            self.errors_logger.log(level, message, exc_info=exc_info, exc_text= str(ex) if ex else '')

        if self.json_logger:
            if ex and exc_info:
                 log_message = f'{message} error = {str(ex)}'
            self.json_logger.log(level, log_message, exc_info=exc_info)

    def info(self, message: str, ex: Optional[Exception] = None, exc_info: bool = False, color: Optional[tuple] = None):
        """
        Логирует информационное сообщение.

        :param message: Логируемое сообщение.
        :type message: str
        :param ex: Исключение для логирования (опционально).
        :type ex: Optional[Exception]
        :param exc_info: Включать информацию об исключении (значение по умолчанию — `False`).
        :type exc_info: bool
        :param color: Кортеж цветов текста и фона для консольного вывода (опционально).
        :type color: Optional[tuple]
        """
        self.log(logging.INFO, message, ex, exc_info, color)

    def success(self, message: str, ex: Optional[Exception] = None, exc_info: bool = False, color: Optional[tuple] = None):
        """
        Логирует сообщение об успешной операции.

        :param message: Логируемое сообщение.
        :type message: str
        :param ex: Исключение для логирования (опционально).
        :type ex: Optional[Exception]
        :param exc_info: Включать информацию об исключении (значение по умолчанию — `False`).
        :type exc_info: bool
        :param color: Кортеж цветов текста и фона для консольного вывода (опционально).
        :type color: Optional[tuple]
        """
        self.log(logging.INFO, message, ex, exc_info, color or (Fore.GREEN, Back.BLACK))

    def warning(self, message: str, ex: Optional[Exception] = None, exc_info: bool = False, color: Optional[tuple] = None):
        """
        Логирует предупреждение.

        :param message: Логируемое сообщение.
        :type message: str
        :param ex: Исключение для логирования (опционально).
        :type ex: Optional[Exception]
        :param exc_info: Включать информацию об исключении (значение по умолчанию — `False`).
        :type exc_info: bool
        :param color: Кортеж цветов текста и фона для консольного вывода (опционально).
        :type color: Optional[tuple]
        """
        self.log(logging.WARNING, message, ex, exc_info, color or (Fore.YELLOW, Back.BLACK))

    def debug(self, message: str, ex: Optional[Exception] = None, exc_info: bool = False, color: Optional[tuple] = None):
        """
        Логирует сообщение для отладки.

        :param message: Логируемое сообщение.
        :type message: str
        :param ex: Исключение для логирования (опционально).
        :type ex: Optional[Exception]
        :param exc_info: Включать информацию об исключении (значение по умолчанию — `False`).
        :type exc_info: bool
        :param color: Кортеж цветов текста и фона для консольного вывода (опционально).
        :type color: Optional[tuple]
        """
        self.log(logging.DEBUG, message, ex, exc_info, color)

    def error(self, message: str, ex: Optional[Exception] = None, exc_info: bool = False, color: Optional[tuple] = None):
        """
        Логирует сообщение об ошибке.

        :param message: Логируемое сообщение.
        :type message: str
        :param ex: Исключение для логирования (опционально).
        :type ex: Optional[Exception]
        :param exc_info: Включать информацию об исключении (значение по умолчанию — `False`).
        :type exc_info: bool
        :param color: Кортеж цветов текста и фона для консольного вывода (опционально).
        :type color: Optional[tuple]
        """
        self.log(logging.ERROR, message, ex, exc_info, color or (Fore.RED, Back.BLACK))

    def critical(self, message: str, ex: Optional[Exception] = None, exc_info: bool = False, color: Optional[tuple] = None):
        """
        Логирует критическое сообщение.

        :param message: Логируемое сообщение.
        :type message: str
        :param ex: Исключение для логирования (опционально).
        :type ex: Optional[Exception]
        :param exc_info: Включать информацию об исключении (значение по умолчанию — `False`).
        :type exc_info: bool
        :param color: Кортеж цветов текста и фона для консольного вывода (опционально).
        :type color: Optional[tuple]
        """
        self.log(logging.CRITICAL, message, ex, exc_info, color or (Fore.RED, Back.WHITE))
```