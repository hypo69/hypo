# Анализ кода модуля src.logger

**Качество кода**
7
- Плюсы
    - Хорошая документация в формате reStructuredText, подробно описывающая функциональность модуля.
    - Использование Singleton для обеспечения единственного экземпляра логгера.
    - Гибкая настройка уровней логирования и форматов вывода.
    - Поддержка цветного вывода в консоль.
    - Разделение логов по уровням в разные файлы.
    - Наличие примеров использования.

- Минусы
   -  В тексте документации есть `код исполняет ...` и другие формулировки, которые следует заменить на более точные.
   -  Не везде описаны параметры функций, включая их типы и возвращаемые значения.
   -  Не хватает подробного описания работы `JsonFormatter`.
   -  Не везде соблюдается стандартизация использования терминологии (например, в описании параметров).

**Рекомендации по улучшению**

1.  **Улучшение документации**:
    -  Заменить все фразы типа "код исполняет", "получаем" на более точные формулировки (например, "осуществляет проверку", "выполняется получение").
    -  Добавить полные описания для всех параметров функций, включая типы и возвращаемые значения.
    -  Добавить описание работы `JsonFormatter`.
    -  Уточнить описания уровней логирования и их влияния на вывод.
2.  **Форматирование комментариев**:
    -  Переписать комментарии в соответствии с требованиями к RST (например, использовать `:param`, `:return`, `:raises`).
3.  **Консистентность**:
    -   Уточнить использование `logger.error` для обработки ошибок и его консистентное применение.
    -   Проверить терминологию на соответствие с другими файлами.
4. **Примеры**:
    -  Добавить пример использования `JsonFormatter`

**Оптимизированный код**

```markdown
````rst
.. module:: src.logger

   :platform: Unix, Windows
   :synopsis: Модуль для логирования с поддержкой различных уровней, форматов и цветов.

.. moduleauthor:: HypoTeam

```
<TABLE >
<TR>
<TD>
<A HREF = 'https://github.com/hypo69/hypo/blob/master/README.MD'>[Root ↑]</A>
</TD>
<TD>
<A HREF = 'https://github.com/hypo69/hypo/blob/master/src/README.MD'>src</A> /
</TD>
<TD>
<A HREF = 'https://github.com/hypo69/hypo/blob/master/src/logger/readme.ru.md'>Русский</A>
</TD>
</TABLE>

### Документация для модуля `src.logger`

Модуль `src.logger` предоставляет гибкую систему логирования, поддерживающую вывод в консоль, файлы и JSON. Он использует шаблон Singleton для гарантии единого экземпляра логгера в приложении. Логгер поддерживает различные уровни логирования (`INFO`, `ERROR`, `DEBUG` и т.д.) и включает цветной вывод для консольных логов. Можно настраивать форматы вывода и управление логированием в разные файлы.

---

### Классы:

-   **SingletonMeta**: Метакласс, реализующий шаблон Singleton для логгера.

-   **JsonFormatter**: Пользовательский форматтер, выводящий логи в формате JSON.

-   **Logger**: Основной класс логгера, поддерживающий вывод в консоль, файлы и JSON.

---

### Функции:

#### `__init__`

Инициализирует экземпляр `Logger` с плейсхолдерами для различных типов логгеров (консольного, файлового и JSON).

#### `_configure_logger(name: str, log_path: str, level: Optional[int] = logging.DEBUG, formatter: Optional[logging.Formatter] = None, mode: Optional[str] = 'a') -> logging.Logger`

Настраивает и возвращает экземпляр логгера.

:param name: Имя логгера.
:type name: str
:param log_path: Путь к файлу журнала.
:type log_path: str
:param level: Уровень логирования (например, `logging.DEBUG`). По умолчанию `logging.DEBUG`.
:type level: Optional[int]
:param formatter: Пользовательский форматтер (опционально).
:type formatter: Optional[logging.Formatter]
:param mode: Режим открытия файла (например, `'a'` для добавления). По умолчанию `'a'`.
:type mode: Optional[str]
:return: Настроенный экземпляр `logging.Logger`.
:rtype: logging.Logger

#### `initialize_loggers(info_log_path: Optional[str] = '', debug_log_path: Optional[str] = '', errors_log_path: Optional[str] = '', json_log_path: Optional[str] = '')`

Инициализирует логгеры для консоли и файлов (info, debug, error и JSON).

:param info_log_path: Путь к файлу журнала info (опционально).
:type info_log_path: Optional[str]
:param debug_log_path: Путь к файлу журнала debug (опционально).
:type debug_log_path: Optional[str]
:param errors_log_path: Путь к файлу журнала error (опционально).
:type errors_log_path: Optional[str]
:param json_log_path: Путь к файлу журнала JSON (опционально).
:type json_log_path: Optional[str]

#### `log(level, message, ex=None, exc_info=False, color=None)`

Записывает сообщение с указанным уровнем (например, `INFO`, `DEBUG`, `ERROR`) с возможностью добавления исключения и цветового оформления.

:param level: Уровень логирования (например, `logging.INFO`, `logging.DEBUG`).
:type level: int
:param message: Сообщение для записи в журнал.
:type message: str
:param ex: Исключение для записи в журнал (опционально).
:type ex: Optional[Exception]
:param exc_info: Флаг для включения информации об исключении (по умолчанию `False`).
:type exc_info: bool
:param color: Кортеж с цветом текста и фона для вывода в консоль (опционально).
:type color: Optional[tuple]

#### `info(message, ex=None, exc_info=False, colors: Optional[tuple] = None)`

Записывает сообщение уровня info.

:param message: Сообщение для записи в журнал.
:type message: str
:param ex: Исключение для записи в журнал (опционально).
:type ex: Optional[Exception]
:param exc_info: Флаг для включения информации об исключении (по умолчанию `False`).
:type exc_info: bool
:param colors: Кортеж с цветом текста и фона для вывода в консоль (опционально).
:type colors: Optional[tuple]

#### `success(message, ex=None, exc_info=False, colors: Optional[tuple] = None)`

Записывает сообщение об успехе.

:param message: Сообщение для записи в журнал.
:type message: str
:param ex: Исключение для записи в журнал (опционально).
:type ex: Optional[Exception]
:param exc_info: Флаг для включения информации об исключении (по умолчанию `False`).
:type exc_info: bool
:param colors: Кортеж с цветом текста и фона для вывода в консоль (опционально).
:type colors: Optional[tuple]

#### `warning(message, ex=None, exc_info=False, colors: Optional[tuple] = None)`

Записывает сообщение-предупреждение.

:param message: Сообщение для записи в журнал.
:type message: str
:param ex: Исключение для записи в журнал (опционально).
:type ex: Optional[Exception]
:param exc_info: Флаг для включения информации об исключении (по умолчанию `False`).
:type exc_info: bool
:param colors: Кортеж с цветом текста и фона для вывода в консоль (опционально).
:type colors: Optional[tuple]

#### `debug(message, ex=None, exc_info=True, colors: Optional[tuple] = None)`

Записывает сообщение уровня debug.

:param message: Сообщение для записи в журнал.
:type message: str
:param ex: Исключение для записи в журнал (опционально).
:type ex: Optional[Exception]
:param exc_info: Флаг для включения информации об исключении (по умолчанию `True`).
:type exc_info: bool
:param colors: Кортеж с цветом текста и фона для вывода в консоль (опционально).
:type colors: Optional[tuple]

#### `error(message, ex=None, exc_info=True, colors: Optional[tuple] = None)`

Записывает сообщение об ошибке.

:param message: Сообщение для записи в журнал.
:type message: str
:param ex: Исключение для записи в журнал (опционально).
:type ex: Optional[Exception]
:param exc_info: Флаг для включения информации об исключении (по умолчанию `True`).
:type exc_info: bool
:param colors: Кортеж с цветом текста и фона для вывода в консоль (опционально).
:type colors: Optional[tuple]

#### `critical(message, ex=None, exc_info=True, colors: Optional[tuple] = None)`

Записывает критическое сообщение.

:param message: Сообщение для записи в журнал.
:type message: str
:param ex: Исключение для записи в журнал (опционально).
:type ex: Optional[Exception]
:param exc_info: Флаг для включения информации об исключении (по умолчанию `True`).
:type exc_info: bool
:param colors: Кортеж с цветом текста и фона для вывода в консоль (опционально).
:type colors: Optional[tuple]

---

### Параметры для `Logger`

Класс `Logger` принимает несколько необязательных параметров для настройки поведения логирования.

-   **Level**: Управляет уровнем важности сообщений, которые регистрируются. Общие уровни включают:
    -   `logging.DEBUG`: Детальная информация для диагностики.
    -   `logging.INFO`: Общая информация, например, об успешных операциях.
    -   `logging.WARNING`: Предупреждения, не требующие немедленных действий.
    -   `logging.ERROR`: Сообщения об ошибках.
    -   `logging.CRITICAL`: Критические ошибки, требующие немедленного внимания.

-   **Formatter**: Определяет формат сообщений журнала. По умолчанию сообщения имеют формат `'%(asctime)s - %(levelname)s - %(message)s'`. Можно задать пользовательский форматтер, например, JSON.

-   **Color**: Цвета для сообщений в консоли. Цвета задаются кортежем из двух элементов:
    -   **Цвет текста**: Цвет текста (например, `colorama.Fore.RED`).
    -   **Цвет фона**: Цвет фона (например, `colorama.Back.WHITE`).

Цвет можно настраивать для разных уровней логирования (например, зеленый для info, красный для errors).

---

### Конфигурация файлового логирования (`config`)

Для записи сообщений в файл, можно задать пути к файлам в конфигурации.

```python
config = {
    'info_log_path': 'logs/info.log',
    'debug_log_path': 'logs/debug.log',
    'errors_log_path': 'logs/errors.log',
    'json_log_path': 'logs/log.json'
}
```

Пути к файлам из `config` используются для записи логов в соответствующие файлы для каждого уровня.

---

### Примеры использования

#### 1. Инициализация `Logger`:

```python
from src.logger.logger import Logger #
logger: Logger = Logger()
config = {
    'info_log_path': 'logs/info.log',
    'debug_log_path': 'logs/debug.log',
    'errors_log_path': 'logs/errors.log',
    'json_log_path': 'logs/log.json'
}
logger.initialize_loggers(**config)
```

#### 2. Запись сообщений разных уровней:

```python
logger.info('Это информационное сообщение')
logger.success('Это сообщение об успехе')
logger.warning('Это сообщение-предупреждение')
logger.debug('Это сообщение debug')
logger.error('Это сообщение об ошибке')
logger.critical('Это критическое сообщение')
```

#### 3. Настройка цветов:

```python
import colorama #
logger.info('Это сообщение будет зеленым', colors=(colorama.Fore.GREEN, colorama.Back.BLACK)) #
logger.error('Это сообщение будет с красным фоном', colors=(colorama.Fore.WHITE, colorama.Back.RED)) #
```

#### 4. Пример использования JSON Formatter

```python
import logging
from src.logger.logger import Logger, JsonFormatter  #
logger: Logger = Logger()
config = {
    'info_log_path': 'logs/info.log',
    'debug_log_path': 'logs/debug.log',
    'errors_log_path': 'logs/errors.log',
    'json_log_path': 'logs/log.json'
}
logger.initialize_loggers(**config)

json_logger = logging.getLogger("json_logger") #
json_handler = logging.FileHandler("logs/json_example.log") #
json_formatter = JsonFormatter() #
json_handler.setFormatter(json_formatter) #
json_logger.addHandler(json_handler)  #
json_logger.setLevel(logging.DEBUG) #


json_logger.info("JSON log message", extra={"key": "value"})  #
```
---

Этот модуль предоставляет гибкую и комплексную систему логирования для Python приложений. Можно настроить вывод в консоль и файлы с различными форматами и цветами, управлять уровнями логирования и обрабатывать исключения. Конфигурация для файлового логирования хранится в словаре `config`, что позволяет легко настраивать поведение системы.
```python
"""
Модуль для настройки и использования системы логирования.
=========================================================================================

Этот модуль предоставляет класс `Logger`, который реализует гибкую систему логирования,
поддерживающую вывод в консоль, файлы и JSON. Используется шаблон Singleton для обеспечения
единственного экземпляра логгера в приложении.

Пример использования
--------------------

Пример использования класса `Logger`:

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
    logger.info('Сообщение информационного уровня')

"""
import logging
from typing import Optional, Tuple
import colorama
import json

class SingletonMeta(type):
    """
    Метакласс, реализующий шаблон Singleton.

    Гарантирует, что у класса будет только один экземпляр.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class JsonFormatter(logging.Formatter):
    """
    Форматтер для логирования в формате JSON.

    Преобразует записи лога в JSON-строку.
    """
    def format(self, record: logging.LogRecord) -> str:
        """
        Форматирует запись лога в JSON-строку.

        :param record: Запись лога.
        :type record: logging.LogRecord
        :return: JSON-строка.
        :rtype: str
        """
        log_record = {
            'time': self.formatTime(record, self.datefmt),
            'level': record.levelname,
            'message': record.getMessage(),
            'name': record.name,
            'pathname': record.pathname,
            'lineno': record.lineno,
            'funcName': record.funcName
        }

        if record.exc_info:
            log_record['exc_info'] = self.formatException(record.exc_info)

        if hasattr(record, 'extra'):
            log_record.update(record.extra)

        return json.dumps(log_record)


class Logger(metaclass=SingletonMeta):
    """
    Класс Logger для гибкой настройки системы логирования.

    Поддерживает вывод в консоль, файлы и JSON.
    """
    def __init__(self):
        """
        Инициализирует экземпляр Logger с плейсхолдерами для логгеров.
        """
        self._console_logger = None
        self._info_logger = None
        self._debug_logger = None
        self._error_logger = None
        self._json_logger = None

    def _configure_logger(self, name: str, log_path: str, level: Optional[int] = logging.DEBUG,
                          formatter: Optional[logging.Formatter] = None, mode: Optional[str] = 'a') -> logging.Logger:
        """
        Настраивает и возвращает экземпляр логгера.

        :param name: Имя логгера.
        :type name: str
        :param log_path: Путь к файлу журнала.
        :type log_path: str
        :param level: Уровень логирования (например, `logging.DEBUG`). По умолчанию `logging.DEBUG`.
        :type level: Optional[int]
        :param formatter: Пользовательский форматтер (опционально).
        :type formatter: Optional[logging.Formatter]
        :param mode: Режим открытия файла (например, `'a'` для добавления). По умолчанию `'a'`.
        :type mode: Optional[str]
        :return: Настроенный экземпляр `logging.Logger`.
        :rtype: logging.Logger
        """
        logger = logging.getLogger(name)
        logger.setLevel(level)

        if log_path:
            file_handler = logging.FileHandler(log_path, mode=mode)
            if formatter:
                file_handler.setFormatter(formatter)
            else:
                formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s') #
                file_handler.setFormatter(formatter) #
            logger.addHandler(file_handler) #
        return logger

    def initialize_loggers(self, info_log_path: Optional[str] = '', debug_log_path: Optional[str] = '',
                           errors_log_path: Optional[str] = '', json_log_path: Optional[str] = ''):
        """
        Инициализирует логгеры для консоли и файлов (info, debug, error и JSON).

        :param info_log_path: Путь к файлу журнала info (опционально).
        :type info_log_path: Optional[str]
        :param debug_log_path: Путь к файлу журнала debug (опционально).
        :type debug_log_path: Optional[str]
        :param errors_log_path: Путь к файлу журнала error (опционально).
        :type errors_log_path: Optional[str]
        :param json_log_path: Путь к файлу журнала JSON (опционально).
        :type json_log_path: Optional[str]
        """
        self._console_logger = self._configure_logger(name='console', log_path='') #
        self._info_logger = self._configure_logger(name='info', log_path=info_log_path, level=logging.INFO) #
        self._debug_logger = self._configure_logger(name='debug', log_path=debug_log_path, level=logging.DEBUG) #
        self._error_logger = self._configure_logger(name='error', log_path=errors_log_path, level=logging.ERROR) #
        self._json_logger = self._configure_logger(name='json', log_path=json_log_path, level=logging.DEBUG, formatter=JsonFormatter()) #


    def log(self, level: int, message: str, ex: Optional[Exception] = None, exc_info: bool = False,
            color: Optional[Tuple[str, str]] = None):
        """
        Записывает сообщение с указанным уровнем и форматированием.

        :param level: Уровень логирования (например, `logging.INFO`, `logging.DEBUG`).
        :type level: int
        :param message: Сообщение для записи в журнал.
        :type message: str
        :param ex: Исключение для записи в журнал (опционально).
        :type ex: Optional[Exception]
        :param exc_info: Флаг для включения информации об исключении (по умолчанию `False`).
        :type exc_info: bool
        :param color: Кортеж с цветом текста и фона для вывода в консоль (опционально).
        :type color: Optional[tuple]
        """
        log_message = message
        if color:
            log_message = f'{color[0]}{color[1]}{message}{colorama.Style.RESET_ALL}'
        if self._console_logger: #
             self._console_logger.log(level, log_message, exc_info=exc_info) #

        if level == logging.INFO and self._info_logger:  #
            self._info_logger.log(level, message, exc_info=exc_info,  exc_info=exc_info) #
        if level == logging.DEBUG and self._debug_logger:  #
            self._debug_logger.log(level, message, exc_info=exc_info,  exc_info=exc_info) #
        if level >= logging.ERROR and self._error_logger:  #
            self._error_logger.log(level, message, exc_info=exc_info, exc_info=exc_info) #
        if level >= logging.DEBUG and self._json_logger:
              extra = {}
              if ex:
                extra = {'exception': str(ex)}
              self._json_logger.log(level, message, exc_info=exc_info, extra=extra)  #

    def info(self, message: str, ex: Optional[Exception] = None, exc_info: bool = False,
             colors: Optional[Tuple[str, str]] = None):
        """
        Записывает сообщение уровня info.

        :param message: Сообщение для записи в журнал.
        :type message: str
        :param ex: Исключение для записи в журнал (опционально).
        :type ex: Optional[Exception]
        :param exc_info: Флаг для включения информации об исключении (по умолчанию `False`).
        :type exc_info: bool
        :param colors: Кортеж с цветом текста и фона для вывода в консоль (опционально).
        :type colors: Optional[tuple]
        """
        self.log(logging.INFO, message, ex, exc_info, colors) #

    def success(self, message: str, ex: Optional[Exception] = None, exc_info: bool = False,
                colors: Optional[Tuple[str, str]] = None):
        """
        Записывает сообщение об успехе.

        :param message: Сообщение для записи в журнал.
        :type message: str
        :param ex: Исключение для записи в журнал (опционально).
        :type ex: Optional[Exception]
        :param exc_info: Флаг для включения информации об исключении (по умолчанию `False`).
        :type exc_info: bool
        :param colors: Кортеж с цветом текста и фона для вывода в консоль (опционально).
        :type colors: Optional[tuple]
        """
        self.log(logging.INFO, message, ex, exc_info, (colorama.Fore.GREEN, colorama.Back.BLACK) if colors is None else colors ) #

    def warning(self, message: str, ex: Optional[Exception] = None, exc_info: bool = False,
                colors: Optional[Tuple[str, str]] = None):
        """
         Записывает сообщение-предупреждение.

        :param message: Сообщение для записи в журнал.
        :type message: str
        :param ex: Исключение для записи в журнал (опционально).
        :type ex: Optional[Exception]
        :param exc_info: Флаг для включения информации об исключении (по умолчанию `False`).
        :type exc_info: bool
        :param colors: Кортеж с цветом текста и фона для вывода в консоль (опционально).
        :type colors: Optional[tuple]
        """
        self.log(logging.WARNING, message, ex, exc_info, (colorama.Fore.YELLOW, colorama.Back.BLACK) if colors is None else colors) #


    def debug(self, message: str, ex: Optional[Exception] = None, exc_info: bool = True,
              colors: Optional[Tuple[str, str]] = None):
        """
        Записывает сообщение уровня debug.

        :param message: Сообщение для записи в журнал.
        :type message: str
        :param ex: Исключение для записи в журнал (опционально).
        :type ex: Optional[Exception]
        :param exc_info: Флаг для включения информации об исключении (по умолчанию `True`).
        :type exc_info: bool
        :param colors: Кортеж с цветом текста и фона для вывода в консоль (опционально).
        :type colors: Optional[tuple]
        """
        self.log(logging.DEBUG, message, ex, exc_info, colors) #

    def error(self, message: str, ex: Optional[Exception] = None, exc_info: bool = True,
              colors: Optional[Tuple[str, str]] = None):
        """
        Записывает сообщение об ошибке.

        :param message: Сообщение для записи в журнал.
        :type message: str
        :param ex: Исключение для записи в журнал (опционально).
        :type ex: Optional[Exception]
        :param exc_info: Флаг для включения информации об исключении (по умолчанию `True`).
        :type exc_info: bool
         :param colors: Кортеж с цветом текста и фона для вывода в консоль (опционально).
        :type colors: Optional[tuple]
        """
        self.log(logging.ERROR, message, ex, exc_info, (colorama.Fore.RED, colorama.Back.BLACK) if colors is None else colors) #


    def critical(self, message: str, ex: Optional[Exception] = None, exc_info: bool = True,
                 colors: Optional[Tuple[str, str]] = None):
        """
        Записывает критическое сообщение.

        :param message: Сообщение для записи в журнал.
        :type message: str
        :param ex: Исключение для записи в журнал (опционально).
        :type ex: Optional[Exception]
        :param exc_info: Флаг для включения информации об исключении (по умолчанию `True`).
        :type exc_info: bool
        :param colors: Кортеж с цветом текста и фона для вывода в консоль (опционально).
        :type colors: Optional[tuple]
        """
        self.log(logging.CRITICAL, message, ex, exc_info,  (colorama.Fore.RED, colorama.Back.WHITE) if colors is None else colors) #
```