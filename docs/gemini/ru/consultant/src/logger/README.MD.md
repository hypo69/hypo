# Анализ кода модуля `src.logger`

**Качество кода**

-   **Соответствие требованиям по оформлению кода**: 9/10
    -   **Плюсы**:
        -   Код хорошо структурирован и документирован, используются docstrings для классов, методов и функций.
        -   Представлено подробное описание модуля и его функциональности.
        -   Примеры использования демонстрируют основные возможности модуля.
        -   Используется `colorama` для раскраски вывода в консоль.
        -   Применяется Singleton для класса Logger.
    -   **Минусы**:
        -   Используются двойные кавычки `"` в примерах кода, хотя по инструкции нужно использовать одинарные кавычки `'`.
        -   В описании не указаны требования к конкретной версии Python или сторонним зависимостям, а также нет описания установки модуля.
        -   Нет проверки на существование директории для логов, перед записью в файл.
        -   Необходимо добавить обработку ошибок при открытии и записи в файл.
        -   В коде не используются f-строки, хотя они более читабельны.
        -   Некоторые комментарии не соответствуют стандарту RST.

**Рекомендации по улучшению**

1.  **Стиль кода**:
    -   Использовать одинарные кавычки (`'`) в коде Python, а двойные кавычки (`"`) только для вывода.
    -   Применять f-строки для форматирования строк.
2.  **Документация**:
    -   Добавить информацию о зависимостях и минимальной версии Python.
    -   Добавить пример установки модуля.
    -   Переформатировать комментарии в соответствии с RST.
    -   Описать обработку ошибок при записи в файлы.
    -   Добавить проверку на существование директорий для логов перед созданием файлов.
3.  **Логирование**:
    -   Использовать `from src.logger.logger import logger` для импорта логгера.
    -   Убрать лишние `try-except` блоки, обрабатывать ошибки через `logger.error`.
4.  **Общая структура**:
    -   Добавить описание модуля в начале файла.
    -   Соблюдать стандарты оформления docstring в Python для Sphinx.
5.  **Обработка данных**:
    -   Использовать `j_loads` или `j_loads_ns` вместо `json.load` если это потребуется.

**Оптимизированный код**

```markdown
```rst
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
<A HREF = 'https://github.com/hypo69/hypo/blob/master/src/logger/readme.ru.md'>Русский</A>
</TD>
</TABLE>

### Документация для модуля `src.logger`

Модуль `src.logger` предоставляет гибкую систему логирования, поддерживающую вывод в консоль, файлы и JSON. Используется паттерн проектирования Singleton, чтобы гарантировать использование единственного экземпляра логгера во всем приложении. Логгер поддерживает различные уровни логирования (`INFO`, `ERROR`, `DEBUG`) и включает цветной вывод для консольных логов. Можно настраивать форматы вывода логов и управлять записью логов в разные файлы.

---

### Классы:

-   **SingletonMeta**: Метакласс, реализующий паттерн Singleton для логгера.
-   **JsonFormatter**: Пользовательский форматер, выводящий логи в формате JSON.
-   **Logger**: Основной класс логгера, поддерживающий логирование в консоль, файлы и JSON.

---

### Функции:

#### `__init__`

Инициализирует экземпляр Logger с плейсхолдерами для разных типов логгеров (консольный, файловый и JSON).

#### `_configure_logger(name: str, log_path: str, level: Optional[int] = logging.DEBUG, formatter: Optional[logging.Formatter] = None, mode: Optional[str] = 'a') -> logging.Logger`

Конфигурирует и возвращает экземпляр логгера.

**Параметры:**
- `name`: Имя логгера.
- `log_path`: Путь к файлу лога.
- `level`: Уровень логирования, например, `logging.DEBUG`. По умолчанию `logging.DEBUG`.
- `formatter`: Пользовательский форматер (опционально).
- `mode`: Режим файла, например, `'a'` для добавления (по умолчанию).

**Возвращает**: Настроенный экземпляр `logging.Logger`.

#### `initialize_loggers(info_log_path: Optional[str] = '', debug_log_path: Optional[str] = '', errors_log_path: Optional[str] = '', json_log_path: Optional[str] = '')`

Инициализирует логгеры для консоли и файлов (info, debug, error и JSON).

**Параметры:**
- `info_log_path`: Путь к файлу информационных логов (опционально).
- `debug_log_path`: Путь к файлу дебаг логов (опционально).
- `errors_log_path`: Путь к файлу логов ошибок (опционально).
- `json_log_path`: Путь к файлу JSON логов (опционально).

#### `log(level, message, ex=None, exc_info=False, color=None)`

Записывает сообщение на указанном уровне (например, `INFO`, `DEBUG`, `ERROR`) с опциональным исключением и цветовым форматированием.

**Параметры:**
- `level`: Уровень логирования (например, `logging.INFO`, `logging.DEBUG`).
- `message`: Сообщение лога.
- `ex`: Опциональное исключение для логирования.
- `exc_info`: Включать ли информацию об исключении (по умолчанию `False`).
- `color`: Кортеж с цветом текста и фона для консольного вывода (опционально).

#### `info(message, ex=None, exc_info=False, colors: Optional[tuple] = None)`

Записывает информационное сообщение.

**Параметры:**
- `message`: Сообщение для записи.
- `ex`: Опциональное исключение для логирования.
- `exc_info`: Включать ли информацию об исключении (по умолчанию `False`).
- `colors`: Кортеж значений цветов для сообщения (опционально).

#### `success(message, ex=None, exc_info=False, colors: Optional[tuple] = None)`

Записывает сообщение об успехе.

**Параметры**:
- Аналогично `info`.

#### `warning(message, ex=None, exc_info=False, colors: Optional[tuple] = None)`

Записывает предупреждающее сообщение.

**Параметры**:
- Аналогично `info`.

#### `debug(message, ex=None, exc_info=True, colors: Optional[tuple] = None)`

Записывает отладочное сообщение.

**Параметры**:
- Аналогично `info`.

#### `error(message, ex=None, exc_info=True, colors: Optional[tuple] = None)`

Записывает сообщение об ошибке.

**Параметры**:
- Аналогично `info`.

#### `critical(message, ex=None, exc_info=True, colors: Optional[tuple] = None)`

Записывает критическое сообщение.

**Параметры**:
- Аналогично `info`.

---

### Параметры для Logger

Класс `Logger` принимает несколько опциональных параметров для настройки поведения логирования.

-   **Level**: Управляет уровнем серьезности логов. Основные уровни:
    -   `logging.DEBUG`: Детальная информация, полезная для диагностики проблем.
    -   `logging.INFO`: Общая информация, например, об успешных операциях.
    -   `logging.WARNING`: Предупреждения, которые не требуют немедленных действий.
    -   `logging.ERROR`: Сообщения об ошибках.
    -   `logging.CRITICAL`: Критические ошибки, требующие немедленного внимания.

-   **Formatter**: Определяет, как форматируются сообщения логов. По умолчанию сообщения форматируются как `'%(asctime)s - %(levelname)s - %(message)s'`. Можно предоставить пользовательский форматер для других форматов, например JSON.

-   **Color**: Цвета для сообщений логов в консоли. Цвета задаются кортежем из двух элементов:
    -   **Цвет текста**: Задает цвет текста (например, `colorama.Fore.RED`).
    -   **Цвет фона**: Задает цвет фона (например, `colorama.Back.WHITE`).

Цвета можно настроить для разных уровней логов (например, зеленый для info, красный для ошибок).

---

### Конфигурация файлового логирования (`config`)

Чтобы логировать сообщения в файл, укажите пути к файлам в конфигурации.

```python
config = {
    'info_log_path': 'logs/info.log',
    'debug_log_path': 'logs/debug.log',
    'errors_log_path': 'logs/errors.log',
    'json_log_path': 'logs/log.json'
}
```

Пути к файлам, указанные в `config`, используются для записи логов в соответствующие файлы для каждого уровня лога.

---

### Пример использования

#### 1. Инициализация логгера:

```python
logger: Logger = Logger()
config = {
    'info_log_path': 'logs/info.log',
    'debug_log_path': 'logs/debug.log',
    'errors_log_path': 'logs/errors.log',
    'json_log_path': 'logs/log.json'
}
logger.initialize_loggers(**config)
```

#### 2. Запись сообщений на разных уровнях:

```python
logger.info('Это информационное сообщение')
logger.success('Это сообщение об успехе')
logger.warning('Это предупреждающее сообщение')
logger.debug('Это отладочное сообщение')
logger.error('Это сообщение об ошибке')
logger.critical('Это критическое сообщение')
```

#### 3. Настройка цветов:

```python
logger.info('Это сообщение будет зеленым', colors=(colorama.Fore.GREEN, colorama.Back.BLACK))
logger.error('Это сообщение будет с красным фоном', colors=(colorama.Fore.WHITE, colorama.Back.RED))
```

---

Этот модуль предоставляет комплексную и гибкую систему логирования для Python приложений. Можно настраивать логирование в консоль и файлы с разными форматами и цветами, управлять уровнями логирования и обрабатывать исключения. Конфигурация для файлового логирования хранится в словаре `config`, что упрощает настройку.
```
```python
"""
Модуль для логирования в консоль, файл и JSON.
=========================================================================================

Этот модуль содержит классы и функции для настройки и использования логгера.
Поддерживается логирование в консоль с цветным выводом, запись в файлы и JSON формат.
Используется паттерн Singleton для гарантии единственного экземпляра логгера.

Пример использования
--------------------

Пример использования класса `Logger`:

.. code-block:: python

    from src.logger.logger import Logger
    import logging
    import colorama

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
"""
import logging
import json
from typing import Optional, Tuple
from colorama import init, Fore, Back
from pathlib import Path
#  импорт `logger` из `src.logger`
from src.logger.logger import logger

init(autoreset=True)


class SingletonMeta(type):
    """
    Метакласс, реализующий паттерн Singleton.

    Этот метакласс гарантирует, что только один экземпляр класса будет создан.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class JsonFormatter(logging.Formatter):
    """
    Пользовательский форматер для вывода логов в формате JSON.

    Этот класс преобразует записи лога в JSON формат.
    """
    def format(self, record):
        log_record = {
            'time': self.formatTime(record, self.datefmt),
            'level': record.levelname,
            'message': record.getMessage(),
        }
        if record.exc_info:
             log_record['exc_info'] = self.formatException(record.exc_info)
        return json.dumps(log_record, ensure_ascii=False)


class Logger(metaclass=SingletonMeta):
    """
    Основной класс логгера, поддерживающий логирование в консоль, файлы и JSON.

    Этот класс предоставляет методы для логирования сообщений разных уровней
    (INFO, DEBUG, ERROR и т.д.) с поддержкой цветного вывода и записи в файлы.
    """
    def __init__(self):
        """
        Инициализирует экземпляр Logger с плейсхолдерами для разных типов логгеров.
        """
        self._console_logger = None
        self._file_loggers = {}
        self._json_logger = None

    def _configure_logger(self, name: str, log_path: str, level: Optional[int] = logging.DEBUG,
                          formatter: Optional[logging.Formatter] = None, mode: Optional[str] = 'a') -> logging.Logger:
        """
        Конфигурирует и возвращает экземпляр логгера.

        Args:
            name (str): Имя логгера.
            log_path (str): Путь к файлу лога.
            level (Optional[int], optional): Уровень логирования. Defaults to logging.DEBUG.
            formatter (Optional[logging.Formatter], optional): Пользовательский форматер. Defaults to None.
            mode (Optional[str], optional): Режим файла. Defaults to 'a'.

        Returns:
            logging.Logger: Конфигурированный экземпляр логгера.
        """
        # код исполняет создание логгера с заданными параметрами
        log_path = Path(log_path)
        log_path.parent.mkdir(parents=True, exist_ok=True)
        logger_instance = logging.getLogger(name)
        logger_instance.setLevel(level)
        if not logger_instance.hasHandlers():
            file_handler = logging.FileHandler(log_path, mode=mode, encoding='utf-8')
            if formatter:
                 file_handler.setFormatter(formatter)
            else:
                 file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
            logger_instance.addHandler(file_handler)
        return logger_instance

    def initialize_loggers(self, info_log_path: Optional[str] = '', debug_log_path: Optional[str] = '',
                            errors_log_path: Optional[str] = '', json_log_path: Optional[str] = ''):
         """
         Инициализирует логгеры для консоли и файлов (info, debug, error и JSON).

         Args:
             info_log_path (Optional[str], optional): Путь к файлу информационных логов. Defaults to ''.
             debug_log_path (Optional[str], optional): Путь к файлу дебаг логов. Defaults to ''.
             errors_log_path (Optional[str], optional): Путь к файлу логов ошибок. Defaults to ''.
             json_log_path (Optional[str], optional): Путь к файлу JSON логов. Defaults to ''.
         """
         # код исполняет настройку консольного логгера
         self._console_logger = logging.getLogger('console')
         self._console_logger.setLevel(logging.DEBUG)
         if not self._console_logger.hasHandlers():
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
            self._console_logger.addHandler(console_handler)

        # код исполняет настройку файловых логгеров
         if info_log_path:
             self._file_loggers['info'] = self._configure_logger('info_logger', info_log_path, level=logging.INFO)
         if debug_log_path:
             self._file_loggers['debug'] = self._configure_logger('debug_logger', debug_log_path, level=logging.DEBUG)
         if errors_log_path:
             self._file_loggers['error'] = self._configure_logger('error_logger', errors_log_path, level=logging.ERROR)
         if json_log_path:
            self._json_logger = self._configure_logger('json_logger', json_log_path, formatter=JsonFormatter())

    def log(self, level, message, ex=None, exc_info=False, color: Optional[Tuple] = None):
        """
        Записывает сообщение на указанном уровне с опциональным исключением и цветовым форматированием.

        Args:
            level: Уровень логирования (например, logging.INFO, logging.DEBUG).
            message: Сообщение лога.
            ex: Опциональное исключение для логирования.
            exc_info: Включать ли информацию об исключении (по умолчанию False).
            color: Кортеж с цветом текста и фона для консольного вывода (опционально).
        """
        # код исполняет форматирование сообщения
        log_message = message
        if color:
            log_message = f'{color[0]}{color[1]}{message}{Fore.RESET}{Back.RESET}'

        # код исполняет запись в консольный логгер
        if self._console_logger:
            self._console_logger.log(level, log_message, exc_info=exc_info)

        # код исполняет запись в файловый логгер
        if level == logging.INFO and 'info' in self._file_loggers:
            self._file_loggers['info'].log(level, message, exc_info=exc_info)
        elif level == logging.DEBUG and 'debug' in self._file_loggers:
            self._file_loggers['debug'].log(level, message, exc_info=exc_info)
        elif level >= logging.ERROR and 'error' in self._file_loggers:
            self._file_loggers['error'].log(level, message, exc_info=exc_info)

        # код исполняет запись в JSON логгер
        if self._json_logger:
            self._json_logger.log(level, message, exc_info=exc_info)
        if ex:
           logger.error(f'{message=}', exc_info=True)

    def info(self, message, ex=None, exc_info=False, colors: Optional[Tuple] = None):
        """
        Записывает информационное сообщение.

        Args:
            message: Сообщение для записи.
            ex: Опциональное исключение для логирования.
            exc_info: Включать ли информацию об исключении (по умолчанию False).
            colors: Кортеж значений цветов для сообщения (опционально).
        """
        self.log(logging.INFO, message, ex=ex, exc_info=exc_info, color=colors)

    def success(self, message, ex=None, exc_info=False, colors: Optional[Tuple] = None):
        """
        Записывает сообщение об успехе.

        Args:
            message: Сообщение для записи.
            ex: Опциональное исключение для логирования.
            exc_info: Включать ли информацию об исключении (по умолчанию False).
            colors: Кортеж значений цветов для сообщения (опционально).
        """
        self.log(logging.INFO, message, ex=ex, exc_info=exc_info, color=(Fore.GREEN, Back.BLACK) if not colors else colors)

    def warning(self, message, ex=None, exc_info=False, colors: Optional[Tuple] = None):
        """
        Записывает предупреждающее сообщение.

        Args:
            message: Сообщение для записи.
            ex: Опциональное исключение для логирования.
            exc_info: Включать ли информацию об исключении (по умолчанию False).
            colors: Кортеж значений цветов для сообщения (опционально).
        """
        self.log(logging.WARNING, message, ex=ex, exc_info=exc_info, color=(Fore.YELLOW, Back.BLACK) if not colors else colors)

    def debug(self, message, ex=None, exc_info=True, colors: Optional[Tuple] = None):
        """
        Записывает отладочное сообщение.

        Args:
            message: Сообщение для записи.
            ex: Опциональное исключение для логирования.
            exc_info: Включать ли информацию об исключении (по умолчанию True).
            colors: Кортеж значений цветов для сообщения (опционально).
        """
        self.log(logging.DEBUG, message, ex=ex, exc_info=exc_info, color=(Fore.BLUE, Back.BLACK) if not colors else colors)

    def error(self, message, ex=None, exc_info=True, colors: Optional[Tuple] = None):
        """
        Записывает сообщение об ошибке.

        Args:
            message: Сообщение для записи.
            ex: Опциональное исключение для логирования.
            exc_info: Включать ли информацию об исключении (по умолчанию True).
            colors: Кортеж значений цветов для сообщения (опционально).
        """
        self.log(logging.ERROR, message, ex=ex, exc_info=exc_info, color=(Fore.RED, Back.BLACK) if not colors else colors)

    def critical(self, message, ex=None, exc_info=True, colors: Optional[Tuple] = None):
        """
        Записывает критическое сообщение.

         Args:
            message: Сообщение для записи.
            ex: Опциональное исключение для логирования.
            exc_info: Включать ли информацию об исключении (по умолчанию True).
            colors: Кортеж значений цветов для сообщения (опционально).
        """
        self.log(logging.CRITICAL, message, ex=ex, exc_info=exc_info, color=(Fore.RED, Back.WHITE) if not colors else colors)
```