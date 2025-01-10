# Анализ кода модуля `src.logger`

**Качество кода**
9
- Плюсы
    - Хорошая и подробная документация в формате Markdown, описывающая функциональность модуля.
    - Четкое описание классов, функций, параметров и их назначения.
    - Приведены примеры использования и конфигурации логгера.
    - Описаны основные уровни логирования и форматы сообщений.
- Минусы
    - Не хватает примеров кода с использованием `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    - Нет подробной документации в формате RST для каждого метода.
    - Нет примеров использования кастомных форматтеров.
    - Не все параметры функций описаны в формате RST.

**Рекомендации по улучшению**
1.  Добавить примеры использования `j_loads` или `j_loads_ns` в разделе с примерами.
2.  Преобразовать документацию в формате Markdown в формат RST для интеграции со Sphinx.
3.  Добавить документацию в формате RST для каждого метода и класса, включая параметры и возвращаемые значения.
4.  Включить примеры использования кастомных форматтеров для JSON.
5.  Указать типы возвращаемых значений для функций и методов в RST документации.
6.  Добавить примеры обработки исключений и логирования ошибок с использованием `logger.error`.
7.  Убедиться, что все функции и методы, а так же параметры имеют документацию.
8.  Устранить избыточное использование стандартных блоков `try-except`, и использовать обработку ошибок с помощью `logger.error`.

**Оптимизированный код**
```markdown
.. module:: src.logger

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
<A HREF = 'https://github.com/hypo69/hypo/blob/master/src/logger/README.MD'>English</A>
</TD>
</TABLE>

Документация для модуля `src.logger`
=====================================================================================

Модуль `src.logger` предоставляет гибкую систему логирования, поддерживающую логирование в консоль, файлы и в формате JSON. Он использует шаблон проектирования Singleton, чтобы обеспечить использование единственного экземпляра логгера во всем приложении. Логгер поддерживает различные уровни логирования (например, `INFO`, `ERROR`, `DEBUG`) и включает цветное отображение для вывода в консоль. Также доступны настройки форматов вывода и управление логированием в различные файлы.

---

### Классы:
- **SingletonMeta**: Метакласс, реализующий шаблон Singleton для логгера.
- **JsonFormatter**: Кастомный форматтер для вывода логов в формате JSON.
- **Logger**: Основной класс логгера, поддерживающий логирование в консоль, файлы и в формате JSON.

---

### Функции:

#### `__init__`
Инициализирует экземпляр класса Logger с плейсхолдерами для различных типов логгеров (консоль, файлы и JSON).
```rst
    .. method:: __init__
        
        Инициализирует экземпляр класса Logger с плейсхолдерами для различных типов логгеров (консоль, файлы и JSON).
        
        :return: None
```
#### `_configure_logger(name: str, log_path: str, level: Optional[int] = logging.DEBUG, formatter: Optional[logging.Formatter] = None, mode: Optional[str] = 'a') -> logging.Logger`
Настраивает и возвращает экземпляр логгера.
```rst
    .. function:: _configure_logger(name: str, log_path: str, level: Optional[int] = logging.DEBUG, formatter: Optional[logging.Formatter] = None, mode: Optional[str] = 'a')
        
        Настраивает и возвращает экземпляр логгера.
        
        :param name: Имя логгера.
        :type name: str
        :param log_path: Путь к файлу логов.
        :type log_path: str
        :param level: Уровень логирования, например, `logging.DEBUG`. Значение по умолчанию — `logging.DEBUG`.
        :type level: Optional[int], optional
        :param formatter: Кастомный форматтер (опционально).
        :type formatter: Optional[logging.Formatter], optional
        :param mode: Режим работы с файлом, например, `'a'` для добавления (значение по умолчанию).
        :type mode: Optional[str], optional
        :return: Настроенный экземпляр `logging.Logger`.
        :rtype: logging.Logger
```
**Параметры:**
- `name`: Имя логгера.
- `log_path`: Путь к файлу логов.
- `level`: Уровень логирования, например, `logging.DEBUG`. Значение по умолчанию — `logging.DEBUG`.
- `formatter`: Кастомный форматтер (опционально).
- `mode`: Режим работы с файлом, например, `'a'` для добавления (значение по умолчанию).

**Возвращает**: Настроенный экземпляр `logging.Logger`.

#### `initialize_loggers(info_log_path: Optional[str] = '', debug_log_path: Optional[str] = '', errors_log_path: Optional[str] = '', json_log_path: Optional[str] = '')`
Инициализирует логгеры для логирования в консоль и файлы (информация, отладка, ошибки и JSON).
```rst
    .. function:: initialize_loggers(info_log_path: Optional[str] = '', debug_log_path: Optional[str] = '', errors_log_path: Optional[str] = '', json_log_path: Optional[str] = '')
    
        Инициализирует логгеры для логирования в консоль и файлы (информация, отладка, ошибки и JSON).
        
        :param info_log_path: Путь к файлу логов информации (опционально).
        :type info_log_path: Optional[str], optional
        :param debug_log_path: Путь к файлу логов отладки (опционально).
        :type debug_log_path: Optional[str], optional
        :param errors_log_path: Путь к файлу логов ошибок (опционально).
        :type errors_log_path: Optional[str], optional
        :param json_log_path: Путь к файлу логов в формате JSON (опционально).
        :type json_log_path: Optional[str], optional
        :return: None
```
**Параметры:**
- `info_log_path`: Путь к файлу логов информации (опционально).
- `debug_log_path`: Путь к файлу логов отладки (опционально).
- `errors_log_path`: Путь к файлу логов ошибок (опционально).
- `json_log_path`: Путь к файлу логов в формате JSON (опционально).

#### `log(level, message, ex=None, exc_info=False, color=None)`
Логирует сообщение на указанном уровне (например, `INFO`, `DEBUG`, `ERROR`) с возможным исключением и цветовым форматированием.
```rst
    .. function:: log(level, message, ex=None, exc_info=False, color=None)
    
        Логирует сообщение на указанном уровне (например, `INFO`, `DEBUG`, `ERROR`) с возможным исключением и цветовым форматированием.
        
        :param level: Уровень логирования (например, `logging.INFO`, `logging.DEBUG`).
        :type level: int
        :param message: Логируемое сообщение.
        :type message: str
        :param ex: Исключение для логирования (опционально).
        :type ex: Optional[Exception], optional
        :param exc_info: Включать информацию об исключении (значение по умолчанию — `False`).
        :type exc_info: bool, optional
        :param color: Кортеж цветов текста и фона для консольного вывода (опционально).
        :type color: Optional[tuple[str, str]], optional
        :return: None
```
**Параметры:**
- `level`: Уровень логирования (например, `logging.INFO`, `logging.DEBUG`).
- `message`: Логируемое сообщение.
- `ex`: Исключение для логирования (опционально).
- `exc_info`: Включать информацию об исключении (значение по умолчанию — `False`).
- `color`: Кортеж цветов текста и фона для консольного вывода (опционально).

#### Другие методы:
- `info`: Логирует информационное сообщение.
```rst
    .. method:: info(message: str, ex: Optional[Exception] = None, exc_info: bool = False, color: Optional[tuple[str, str]] = None)
    
        Логирует информационное сообщение.
        
        :param message: Логируемое сообщение.
        :type message: str
        :param ex: Исключение для логирования (опционально).
        :type ex: Optional[Exception], optional
        :param exc_info: Включать информацию об исключении (значение по умолчанию — `False`).
        :type exc_info: bool, optional
        :param color: Кортеж цветов текста и фона для консольного вывода (опционально).
        :type color: Optional[tuple[str, str]], optional
        :return: None
```
- `success`: Логирует сообщение об успешной операции.
```rst
    .. method:: success(message: str, ex: Optional[Exception] = None, exc_info: bool = False, color: Optional[tuple[str, str]] = None)
    
        Логирует сообщение об успешной операции.
        
        :param message: Логируемое сообщение.
        :type message: str
        :param ex: Исключение для логирования (опционально).
        :type ex: Optional[Exception], optional
        :param exc_info: Включать информацию об исключении (значение по умолчанию — `False`).
        :type exc_info: bool, optional
        :param color: Кортеж цветов текста и фона для консольного вывода (опционально).
        :type color: Optional[tuple[str, str]], optional
        :return: None
```
- `warning`: Логирует предупреждение.
```rst
    .. method:: warning(message: str, ex: Optional[Exception] = None, exc_info: bool = False, color: Optional[tuple[str, str]] = None)
    
        Логирует предупреждение.
        
        :param message: Логируемое сообщение.
        :type message: str
        :param ex: Исключение для логирования (опционально).
        :type ex: Optional[Exception], optional
        :param exc_info: Включать информацию об исключении (значение по умолчанию — `False`).
        :type exc_info: bool, optional
        :param color: Кортеж цветов текста и фона для консольного вывода (опционально).
        :type color: Optional[tuple[str, str]], optional
        :return: None
```
- `debug`: Логирует сообщение для отладки.
```rst
    .. method:: debug(message: str, ex: Optional[Exception] = None, exc_info: bool = False, color: Optional[tuple[str, str]] = None)
    
        Логирует сообщение для отладки.
        
        :param message: Логируемое сообщение.
        :type message: str
        :param ex: Исключение для логирования (опционально).
        :type ex: Optional[Exception], optional
        :param exc_info: Включать информацию об исключении (значение по умолчанию — `False`).
        :type exc_info: bool, optional
        :param color: Кортеж цветов текста и фона для консольного вывода (опционально).
        :type color: Optional[tuple[str, str]], optional
        :return: None
```
- `error`: Логирует сообщение об ошибке.
```rst
    .. method:: error(message: str, ex: Optional[Exception] = None, exc_info: bool = False, color: Optional[tuple[str, str]] = None)
    
        Логирует сообщение об ошибке.
        
        :param message: Логируемое сообщение.
        :type message: str
        :param ex: Исключение для логирования (опционально).
        :type ex: Optional[Exception], optional
        :param exc_info: Включать информацию об исключении (значение по умолчанию — `False`).
        :type exc_info: bool, optional
        :param color: Кортеж цветов текста и фона для консольного вывода (опционально).
        :type color: Optional[tuple[str, str]], optional
        :return: None
```
- `critical`: Логирует критическое сообщение.
```rst
    .. method:: critical(message: str, ex: Optional[Exception] = None, exc_info: bool = False, color: Optional[tuple[str, str]] = None)
    
        Логирует критическое сообщение.
        
        :param message: Логируемое сообщение.
        :type message: str
        :param ex: Исключение для логирования (опционально).
        :type ex: Optional[Exception], optional
        :param exc_info: Включать информацию об исключении (значение по умолчанию — `False`).
        :type exc_info: bool, optional
        :param color: Кортеж цветов текста и фона для консольного вывода (опционально).
        :type color: Optional[tuple[str, str]], optional
        :return: None
```
---

### Параметры логгера
Класс `Logger` принимает несколько опциональных параметров для настройки поведения логирования.

- **Уровень**: Контролирует, какие сообщения будут записаны. Основные уровни:
  - `logging.DEBUG`: Подробная информация для диагностики.
  - `logging.INFO`: Общая информация, например, успешные операции.
  - `logging.WARNING`: Предупреждения, не требующие немедленного действия.
  - `logging.ERROR`: Сообщения об ошибках.
  - `logging.CRITICAL`: Критические ошибки, требующие немедленного внимания.

- **Форматтер**: Определяет формат сообщений. По умолчанию используется `'%(asctime)s - %(levelname)s - %(message)s'`. Можно задать кастомный форматтер, например для JSON.

- **Цвета**: Задают цвет текста и фона в консоли. Цвета указываются кортежем:
  - **Цвет текста**: Например, `colorama.Fore.RED`.
  - **Цвет фона**: Например, `colorama.Back.WHITE`.

---

### Конфигурация для логирования в файл (`config`)
Для записи сообщений в файл можно указать пути в конфигурации.

```python
config = {
    'info_log_path': 'logs/info.log',
    'debug_log_path': 'logs/debug.log',
    'errors_log_path': 'logs/errors.log',
    'json_log_path': 'logs/log.json'
}
```

---

### Примеры использования

#### 1. Инициализация логгера:
```python
# logger: Logger = Logger() - Инициализация экземпляра логгера
logger: Logger = Logger()
# config - Словарь с путями для файлов логов
config = {
    'info_log_path': 'logs/info.log',
    'debug_log_path': 'logs/debug.log',
    'errors_log_path': 'logs/errors.log',
    'json_log_path': 'logs/log.json'
}
# logger.initialize_loggers(**config) - Инициализация логгеров с заданной конфигурацией
logger.initialize_loggers(**config)
```

#### 2. Логирование сообщений:
```python
# logger.info('Это информационное сообщение') - Логирование информационного сообщения
logger.info('Это информационное сообщение')
# logger.success('Это сообщение об успешной операции') - Логирование сообщения об успешной операции
logger.success('Это сообщение об успешной операции')
# logger.warning('Это предупреждение') - Логирование предупреждения
logger.warning('Это предупреждение')
# logger.debug('Это сообщение для отладки') - Логирование сообщения для отладки
logger.debug('Это сообщение для отладки')
# logger.error('Это сообщение об ошибке') - Логирование сообщения об ошибке
logger.error('Это сообщение об ошибке')
# logger.critical('Это критическое сообщение') - Логирование критического сообщения
logger.critical('Это критическое сообщение')
```

#### 3. Настройка цветов:
```python
# logger.info('Это сообщение будет зеленым', colors=(colorama.Fore.GREEN, colorama.Back.BLACK)) - Логирование сообщения с зеленым текстом и черным фоном
logger.info('Это сообщение будет зеленым', colors=(colorama.Fore.GREEN, colorama.Back.BLACK))
# logger.error('Это сообщение с красным фоном', colors=(colorama.Fore.WHITE, colorama.Back.RED)) - Логирование сообщения с белым текстом и красным фоном
logger.error('Это сообщение с красным фоном', colors=(colorama.Fore.WHITE, colorama.Back.RED))
```

---

Модуль `src.logger` предоставляет полноценную систему логирования для Python-приложений. Вы можете настроить логирование в консоль и файлы с различными форматами и цветами, управлять уровнями логирования и обрабатывать исключения. Конфигурация логирования в файлы задается через словарь `config`, что позволяет легко изменять настройки.
```
```python
"""
Модуль для реализации логирования в приложении.
=========================================================================================

Этот модуль содержит классы и методы для настройки и использования логгера,
который может выводить сообщения в консоль, файлы и в формате JSON.
"""

import logging
from typing import Optional, Tuple, Any
import json
import colorama
from src.utils.jjson import j_loads, j_loads_ns
from pathlib import Path
# from src.logger.logger import logger
# from src.logger import logger

class SingletonMeta(type):
    """
    Метакласс, реализующий шаблон Singleton.
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
    Кастомный форматтер для вывода логов в формате JSON.
    """
    def format(self, record):
        """
        Форматирует запись лога в JSON.
        """
        log_record = {
            'time': self.formatTime(record, self.datefmt),
            'level': record.levelname,
            'message': record.getMessage(),
            'name': record.name,
            'pathname': record.pathname,
            'lineno': record.lineno,
        }
        if record.exc_info:
             log_record['exc_info'] = self.formatException(record.exc_info)
        return json.dumps(log_record)

class Logger(metaclass=SingletonMeta):
    """
    Основной класс логгера, поддерживающий логирование в консоль, файлы и в формате JSON.
    """
    def __init__(self):
        """
        Инициализирует экземпляр класса Logger с плейсхолдерами для различных типов логгеров (консоль, файлы и JSON).
        """
        self.console_logger: Optional[logging.Logger] = None
        self.info_logger: Optional[logging.Logger] = None
        self.debug_logger: Optional[logging.Logger] = None
        self.errors_logger: Optional[logging.Logger] = None
        self.json_logger: Optional[logging.Logger] = None
        self.formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s') # Форматтер по умолчанию
    
    def _configure_logger(
        self, 
        name: str, 
        log_path: str, 
        level: Optional[int] = logging.DEBUG, 
        formatter: Optional[logging.Formatter] = None, 
        mode: Optional[str] = 'a'
    ) -> logging.Logger:
        """
        Настраивает и возвращает экземпляр логгера.
        
        :param name: Имя логгера.
        :type name: str
        :param log_path: Путь к файлу логов.
        :type log_path: str
        :param level: Уровень логирования, например, `logging.DEBUG`. Значение по умолчанию — `logging.DEBUG`.
        :type level: Optional[int], optional
        :param formatter: Кастомный форматтер (опционально).
        :type formatter: Optional[logging.Formatter], optional
        :param mode: Режим работы с файлом, например, `'a'` для добавления (значение по умолчанию).
        :type mode: Optional[str], optional
        :return: Настроенный экземпляр `logging.Logger`.
        :rtype: logging.Logger
        """
        logger = logging.getLogger(name) # получение экземпляра логгера
        logger.setLevel(level) # установка уровня логирования
        if log_path:
            # if not Path(log_path).exists(): #проверка существования пути
            Path(log_path).parent.mkdir(parents=True, exist_ok=True) #создания родительских директорий
            file_handler = logging.FileHandler(log_path, mode=mode, encoding='utf-8') #создание обработчика файла
            if formatter:
                file_handler.setFormatter(formatter) #установка форматтера
            else:
                file_handler.setFormatter(self.formatter) #установка форматтера по умолчанию
            logger.addHandler(file_handler) #добавления обработчика файла
        return logger #возврат настроенного логгера

    def initialize_loggers(
        self, 
        info_log_path: Optional[str] = '', 
        debug_log_path: Optional[str] = '', 
        errors_log_path: Optional[str] = '', 
        json_log_path: Optional[str] = ''
    ):
        """
        Инициализирует логгеры для логирования в консоль и файлы (информация, отладка, ошибки и JSON).
        
        :param info_log_path: Путь к файлу логов информации (опционально).
        :type info_log_path: Optional[str], optional
        :param debug_log_path: Путь к файлу логов отладки (опционально).
        :type debug_log_path: Optional[str], optional
        :param errors_log_path: Путь к файлу логов ошибок (опционально).
        :type errors_log_path: Optional[str], optional
        :param json_log_path: Путь к файлу логов в формате JSON (опционально).
        :type json_log_path: Optional[str], optional
        :return: None
        """
        self.console_logger = self._configure_logger('console', None, logging.DEBUG) #настройка логгера консоли
        if info_log_path:
            self.info_logger = self._configure_logger('info', info_log_path, logging.INFO) #настройка логгера для информации
        if debug_log_path:
           self.debug_logger = self._configure_logger('debug', debug_log_path, logging.DEBUG) #настройка логгера для отладки
        if errors_log_path:
           self.errors_logger = self._configure_logger('errors', errors_log_path, logging.ERROR) #настройка логгера для ошибок
        if json_log_path:
            json_formatter = JsonFormatter() #создание кастомного форматтера
            self.json_logger = self._configure_logger('json', json_log_path, logging.DEBUG, formatter=json_formatter) #настройка логгера для json

    def log(self, level: int, message: str, ex: Optional[Exception] = None, exc_info: bool = False, color: Optional[Tuple[str, str]] = None):
        """
        Логирует сообщение на указанном уровне (например, `INFO`, `DEBUG`, `ERROR`) с возможным исключением и цветовым форматированием.
        
        :param level: Уровень логирования (например, `logging.INFO`, `logging.DEBUG`).
        :type level: int
        :param message: Логируемое сообщение.
        :type message: str
        :param ex: Исключение для логирования (опционально).
        :type ex: Optional[Exception], optional
        :param exc_info: Включать информацию об исключении (значение по умолчанию — `False`).
        :type exc_info: bool, optional
        :param color: Кортеж цветов текста и фона для консольного вывода (опционально).
        :type color: Optional[tuple[str, str]], optional
        :return: None
        """
        if color:
            message = f'{color[0]}{color[1]}{message}{colorama.Style.RESET_ALL}' #добавление цветового оформления

        if self.console_logger:
             self.console_logger.log(level, message, exc_info=exc_info) #логирование в консоль
        if level == logging.INFO and self.info_logger:
            self.info_logger.log(level, message, exc_info=exc_info) #логирование информации
        if level == logging.DEBUG and self.debug_logger:
            self.debug_logger.log(level, message, exc_info=exc_info) #логирование отладочной информации
        if level == logging.ERROR and self.errors_logger:
            self.errors_logger.log(level, message, exc_info=exc_info)  #логирование ошибок
        if self.json_logger:
             self.json_logger.log(level, message, exc_info=exc_info)  #логирование в json
        if ex:
            # Обработка исключения и запись в лог
            if self.console_logger:
                 self.console_logger.error(f"Exception: {ex}", exc_info=exc_info)
            if self.info_logger:
                 self.info_logger.error(f"Exception: {ex}", exc_info=exc_info)
            if self.debug_logger:
                 self.debug_logger.error(f"Exception: {ex}", exc_info=exc_info)
            if self.errors_logger:
                 self.errors_logger.error(f"Exception: {ex}", exc_info=exc_info)
            if self.json_logger:
                self.json_logger.error(f"Exception: {ex}", exc_info=exc_info)


    def info(self, message: str, ex: Optional[Exception] = None, exc_info: bool = False, color: Optional[Tuple[str, str]] = None):
        """
        Логирует информационное сообщение.
        
        :param message: Логируемое сообщение.
        :type message: str
        :param ex: Исключение для логирования (опционально).
        :type ex: Optional[Exception], optional
        :param exc_info: Включать информацию об исключении (значение по умолчанию — `False`).
        :type exc_info: bool, optional
        :param color: Кортеж цветов текста и фона для консольного вывода (опционально).
        :type color: Optional[tuple[str, str]], optional
        :return: None
        """
        self.log(logging.INFO, message, ex, exc_info, color) #вызов основного метода логирования
    
    def success(self, message: str, ex: Optional[Exception] = None, exc_info: bool = False, color: Optional[Tuple[str, str]] = None):
        """
        Логирует сообщение об успешной операции.
        
        :param message: Логируемое сообщение.
        :type message: str
        :param ex: Исключение для логирования (опционально).
        :type ex: Optional[Exception], optional
        :param exc_info: Включать информацию об исключении (значение по умолчанию — `False`).
        :type exc_info: bool, optional
        :param color: Кортеж цветов текста и фона для консольного вывода (опционально).
        :type color: Optional[tuple[str, str]], optional
        :return: None
        """
        self.log(logging.INFO, message, ex, exc_info, color) #вызов основного метода логирования

    def warning(self, message: str, ex: Optional[Exception] = None, exc_info: bool = False, color: Optional[Tuple[str, str]] = None):
        """
        Логирует предупреждение.
        
        :param message: Логируемое сообщение.
        :type message: str
        :param ex: Исключение для логирования (опционально).
        :type ex: Optional[Exception], optional
        :param exc_info: Включать информацию об исключении (значение по умолчанию — `False`).
        :type exc_info: bool, optional
        :param color: Кортеж цветов текста и фона для консольного вывода (опционально).
        :type color: Optional[tuple[str, str]], optional
        :return: None
        """
        self.log(logging.WARNING, message, ex, exc_info, color) #вызов основного метода логирования

    def debug(self, message: str, ex: Optional[Exception] = None, exc_info: bool = False, color: Optional[Tuple[str, str]] = None):
        """
        Логирует сообщение для отладки.
        
        :param message: Логируемое сообщение.
        :type message: str
        :param ex: Исключение для логирования (опционально).
        :type ex: Optional[Exception], optional
        :param exc_info: Включать информацию об исключении (значение по умолчанию — `False`).
        :type exc_info: bool, optional
        :param color: Кортеж цветов текста и фона для консольного вывода (опционально).
        :type color: Optional[tuple[str, str]], optional
        :return: None
        """
        self.log(logging.DEBUG, message, ex, exc_info, color) #вызов основного метода логирования

    def error(self, message: str, ex: Optional[Exception] = None, exc_info: bool = False, color: Optional[Tuple[str, str]] = None):
        """
        Логирует сообщение об ошибке.
        
        :param message: Логируемое сообщение.
        :type message: str
        :param ex: Исключение для логирования (опционально).
        :type ex: Optional[Exception], optional
        :param exc_info: Включать информацию об исключении (значение по умолчанию — `False`).
        :type exc_info: bool, optional
        :param color: Кортеж цветов текста и фона для консольного вывода (опционально).
        :type color: Optional[tuple[str, str]], optional
        :return: None
        """
        self.log(logging.ERROR, message, ex, exc_info, color) #вызов основного метода логирования

    def critical(self, message: str, ex: Optional[Exception] = None, exc_info: bool = False, color: Optional[Tuple[str, str]] = None):
        """
        Логирует критическое сообщение.
        
        :param message: Логируемое сообщение.
        :type message: str
        :param ex: Исключение для логирования (опционально).
        :type ex: Optional[Exception], optional
        :param exc_info: Включать информацию об исключении (значение по умолчанию — `False`).
        :type exc_info: bool, optional
        :param color: Кортеж цветов текста и фона для консольного вывода (опционально).
        :type color: Optional[tuple[str, str]], optional
        :return: None
        """
        self.log(logging.CRITICAL, message, ex, exc_info, color) #вызов основного метода логирования
```