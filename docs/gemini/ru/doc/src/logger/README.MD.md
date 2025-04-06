# Документация для модуля `src.logger`

## Обзор

Модуль `src.logger` предоставляет гибкую систему логирования, поддерживающую логирование в консоль, файлы и JSON. Он использует шаблон проектирования Singleton для гарантии использования только одного экземпляра логгера во всем приложении. Логгер поддерживает различные уровни логирования (например, `INFO`, `ERROR`, `DEBUG`) и включает цветной вывод для консольных логов. Можно также настраивать форматы вывода логов и управлять логированием в разные файлы.

## Подробнее

Этот модуль предназначен для централизованного управления логированием в приложении. Он обеспечивает возможность гибкой настройки уровней логирования, форматов вывода и мест хранения логов (консоль, файлы, JSON). Использование Singleton гарантирует, что все компоненты приложения будут использовать один и тот же экземпляр логгера, что упрощает управление и конфигурацию.

## Классы

### `SingletonMeta`

**Описание**: Метакласс, реализующий шаблон проектирования Singleton для логгера.

**Принцип работы**:
SingletonMeta гарантирует, что при попытке создать новый экземпляр класса, будет возвращен существующий экземпляр, если он уже был создан. Это достигается за счет хранения экземпляра класса в атрибуте `_instances` и переопределения метода `__call__`.

### `JsonFormatter`

**Описание**: Пользовательский форматтер, выводящий логи в формате JSON.

**Принцип работы**:
`JsonFormatter` наследуется от `logging.Formatter` и переопределяет метод `format`, чтобы форматировать записи лога в виде JSON-строк. Это позволяет легко записывать логи в формате, удобном для машинной обработки и анализа.

### `Logger`

**Описание**: Основной класс логгера, поддерживающий логирование в консоль, файлы и JSON.

**Принцип работы**:
Класс `Logger` предоставляет методы для настройки и инициализации логгеров для различных целей (информация, отладка, ошибки, JSON). Он использует стандартный модуль `logging` Python и добавляет функциональность для цветного вывода в консоль и форматирования логов в JSON. Класс также реализует Singleton, чтобы гарантировать наличие только одного экземпляра логгера во всем приложении.

**Аттрибуты**:

- `console_handler (logging.StreamHandler | None)`: Обработчик для вывода логов в консоль.
- `file_handler (logging.FileHandler | None)`: Обработчик для записи логов в файл.
- `json_handler (logging.FileHandler | None)`: Обработчик для записи логов в JSON-файл.
- `logger (logging.Logger)`: Основной объект логгера.

**Методы**:

- `_configure_logger()`: Настраивает и возвращает экземпляр логгера.
- `initialize_loggers()`: Инициализирует логгеры для консоли и файлов (информация, отладка, ошибки и JSON).
- `log()`: Записывает сообщение в лог на указанном уровне с дополнительным исключением и цветовым форматированием.
- `info()`: Записывает информационное сообщение.
- `success()`: Записывает сообщение об успехе.
- `warning()`: Записывает предупреждающее сообщение.
- `debug()`: Записывает отладочное сообщение.
- `error()`: Записывает сообщение об ошибке.
- `critical()`: Записывает критическое сообщение.

## Функции

### `_configure_logger`

```python
def _configure_logger(name: str, log_path: str, level: Optional[int] = logging.DEBUG, formatter: Optional[logging.Formatter] = None, mode: Optional[str] = 'a') -> logging.Logger:
    """
    Args:
        name (str): Имя логгера.
        log_path (str): Путь к файлу лога.
        level (Optional[int], optional): Уровень логирования, например, `logging.DEBUG`. По умолчанию `logging.DEBUG`.
        formatter (Optional[logging.Formatter], optional): Пользовательский форматтер (необязательно).
        mode (Optional[str], optional): Режим файла, например, `'a'` для добавления (по умолчанию).

    Returns:
        logging.Logger: Настроенный экземпляр `logging.Logger`.

    Raises:
        FileNotFoundError: Если указанный `log_path` не существует.
        PermissionError: Если нет прав для создания или записи в файл по указанному пути.

    Example:
        >>> logger = _configure_logger('my_logger', 'logs/debug.log', logging.DEBUG)
        >>> logger.debug('This is a debug message')
    """
```

**Назначение**: Настраивает и возвращает экземпляр логгера.

**Параметры**:

- `name` (str): Имя логгера.
- `log_path` (str): Путь к файлу лога.
- `level` (Optional[int], optional): Уровень логирования, например, `logging.DEBUG`. По умолчанию `logging.DEBUG`.
- `formatter` (Optional[logging.Formatter], optional): Пользовательский форматтер (необязательно).
- `mode` (Optional[str], optional): Режим файла, например, `'a'` для добавления (по умолчанию).

**Возвращает**:

- `logging.Logger`: Настроенный экземпляр `logging.Logger`.

**Вызывает исключения**:

- `FileNotFoundError`: Если указанный `log_path` не существует.
- `PermissionError`: Если нет прав для создания или записи в файл по указанному пути.

**Как работает функция**:

1.  Функция получает имя логгера, путь к файлу лога, уровень логирования, форматтер и режим файла.
2.  Создает экземпляр `logging.Logger` с указанным именем.
3.  Создает обработчик файла (`logging.FileHandler`) с указанным путем и режимом.
4.  Устанавливает уровень логирования для обработчика.
5.  Если указан форматтер, устанавливает его для обработчика.
6.  Добавляет обработчик к логгеру.
7.  Возвращает настроенный экземпляр логгера.

```
_configure_logger
│
├───Создание экземпляра logging.Logger
│
├───Создание обработчика файла (logging.FileHandler)
│
├───Установка уровня логирования для обработчика
│
├───Установка форматтера для обработчика (если указан)
│
└───Добавление обработчика к логгеру
│
Возврат настроенного экземпляра логгера
```

**Примеры**:

```python
import logging
from src.logger import Logger

# Пример настройки логгера для записи отладочных сообщений в файл
logger = Logger._configure_logger(name='debug_logger', log_path='debug.log', level=logging.DEBUG)
logger.debug('This is a debug message')

# Пример настройки логгера с пользовательским форматтером
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
logger = Logger._configure_logger(name='custom_logger', log_path='custom.log', formatter=formatter)
logger.info('This is an info message with custom format')
```

### `initialize_loggers`

```python
def initialize_loggers(info_log_path: Optional[str] = '', debug_log_path: Optional[str] = '', errors_log_path: Optional[str] = '', json_log_path: Optional[str] = '') -> None:
    """
    Args:
        info_log_path (Optional[str], optional): Путь для файла информационных логов (необязательно).
        debug_log_path (Optional[str], optional): Путь для файла отладочных логов (необязательно).
        errors_log_path (Optional[str], optional): Путь для файла логов ошибок (необязательно).
        json_log_path (Optional[str], optional): Путь для файла JSON логов (необязательно).

    Raises:
        FileNotFoundError: Если какой-либо из указанных путей не существует.
        PermissionError: Если нет прав для создания или записи в файл по указанному пути.

    Example:
        >>> logger = Logger()
        >>> logger.initialize_loggers(info_log_path='logs/info.log', debug_log_path='logs/debug.log')
    """
```

**Назначение**: Инициализирует логгеры для консоли и файлов (информация, отладка, ошибки и JSON).

**Параметры**:

- `info_log_path` (Optional[str], optional): Путь для файла информационных логов (необязательно).
- `debug_log_path` (Optional[str], optional): Путь для файла отладочных логов (необязательно).
- `errors_log_path` (Optional[str], optional): Путь для файла логов ошибок (необязательно).
- `json_log_path` (Optional[str], optional): Путь для файла JSON логов (необязательно).

**Возвращает**:

- `None`

**Вызывает исключения**:

- `FileNotFoundError`: Если какой-либо из указанных путей не существует.
- `PermissionError`: Если нет прав для создания или записи в файл по указанному пути.

**Как работает функция**:

1.  Функция получает пути к файлам для различных уровней логирования (информация, отладка, ошибки, JSON).
2.  Если указан путь для информационных логов, настраивает логгер для записи информационных сообщений в файл.
3.  Если указан путь для отладочных логов, настраивает логгер для записи отладочных сообщений в файл.
4.  Если указан путь для логов ошибок, настраивает логгер для записи сообщений об ошибках в файл.
5.  Если указан путь для JSON логов, настраивает логгер для записи сообщений в формате JSON в файл.
6.  Настраивает обработчик консоли для вывода сообщений в консоль с цветным форматированием.

```
initialize_loggers
│
├───Проверка наличия путей к файлам логов
│
├───Настройка логгера для информационных сообщений (если указан путь)
│
├───Настройка логгера для отладочных сообщений (если указан путь)
│
├───Настройка логгера для сообщений об ошибках (если указан путь)
│
├───Настройка логгера для JSON логов (если указан путь)
│
└───Настройка обработчика консоли для цветного вывода
│
Возврат None
```

**Примеры**:

```python
from src.logger import Logger

# Пример инициализации логгеров для записи в файлы и вывода в консоль
logger = Logger()
config = {
    'info_log_path': 'logs/info.log',
    'debug_log_path': 'logs/debug.log',
    'errors_log_path': 'logs/errors.log',
    'json_log_path': 'logs/log.json'
}
logger.initialize_loggers(**config)
```

### `log`

```python
def log(level: int, message: str, ex: Optional[Exception] = None, exc_info: bool = False, color: Optional[tuple] = None) -> None:
    """
    Args:
        level (int): Уровень логирования (например, `logging.INFO`, `logging.DEBUG`).
        message (str): Сообщение лога.
        ex (Optional[Exception], optional): Опциональное исключение для логирования.
        exc_info (bool, optional): Следует ли включать информацию об исключении (по умолчанию `False`).
        color (Optional[tuple], optional): Кортеж с цветами текста и фона для вывода в консоль (необязательно).

    Raises:
        ValueError: Если указан недопустимый уровень логирования.
        TypeError: Если `color` не является кортежем.

    Example:
        >>> logger = Logger()
        >>> logger.log(logging.INFO, 'This is an info message')
    """
```

**Назначение**: Записывает сообщение в лог на указанном уровне с дополнительным исключением и цветовым форматированием.

**Параметры**:

- `level` (int): Уровень логирования (например, `logging.INFO`, `logging.DEBUG`).
- `message` (str): Сообщение лога.
- `ex` (Optional[Exception], optional): Опциональное исключение для логирования.
- `exc_info` (bool, optional): Следует ли включать информацию об исключении (по умолчанию `False`).
- `color` (Optional[tuple], optional): Кортеж с цветами текста и фона для вывода в консоль (необязательно).

**Возвращает**:

- `None`

**Вызывает исключения**:

- `ValueError`: Если указан недопустимый уровень логирования.
- `TypeError`: Если `color` не является кортежем.

**Как работает функция**:

1.  Функция получает уровень логирования, сообщение лога, исключение (если есть), флаг для включения информации об исключении и цвета для консольного вывода (если указаны).
2.  Форматирует сообщение лога, добавляя информацию об исключении, если это необходимо.
3.  Если указаны цвета для консольного вывода, применяет их к сообщению.
4.  Записывает сообщение в лог с указанным уровнем.

```
log
│
├───Форматирование сообщения лога
│
├───Применение цветов к сообщению (если указаны)
│
└───Запись сообщения в лог с указанным уровнем
│
Возврат None
```

**Примеры**:

```python
import logging
import colorama
from src.logger import Logger

# Пример записи информационного сообщения
logger = Logger()
logger.log(logging.INFO, 'This is an info message')

# Пример записи сообщения об ошибке с информацией об исключении
try:
    1 / 0
except Exception as ex:
    logger.log(logging.ERROR, 'Error during division', ex=ex, exc_info=True)

# Пример записи сообщения с пользовательскими цветами
logger.log(logging.INFO, 'This message will be green', color=(colorama.Fore.GREEN, colorama.Back.BLACK))
```

### `info`

```python
def info(message: str, ex: Optional[Exception] = None, exc_info: bool = False, colors: Optional[tuple] = None) -> None:
    """
    Args:
        message (str): Информационное сообщение для логирования.
        ex (Optional[Exception], optional): Опциональное исключение для логирования.
        exc_info (bool, optional): Включать ли информацию об исключении (по умолчанию `False`).
        colors (Optional[tuple], optional): Кортеж цветовых значений для сообщения (необязательно).

    Example:
        >>> logger = Logger()
        >>> logger.info('This is an info message')
    """
```

**Назначение**: Записывает информационное сообщение.

**Параметры**:

- `message` (str): Информационное сообщение для логирования.
- `ex` (Optional[Exception], optional): Опциональное исключение для логирования.
- `exc_info` (bool, optional): Включать ли информацию об исключении (по умолчанию `False`).
- `colors` (Optional[tuple], optional): Кортеж цветовых значений для сообщения (необязательно).

**Как работает функция**:

Функция `info` вызывает метод `log` с уровнем логирования `logging.INFO` и переданными параметрами.

```
info
│
└───Вызов метода log с уровнем logging.INFO
│
Возврат None
```

**Примеры**:

```python
from src.logger import Logger
import logging
# Пример записи информационного сообщения
logger = Logger()
logger.info('This is an info message')
```

### `success`

```python
def success(message: str, ex: Optional[Exception] = None, exc_info: bool = False, colors: Optional[tuple] = None) -> None:
    """
    Args:
        message (str): Сообщение об успехе для логирования.
        ex (Optional[Exception], optional): Опциональное исключение для логирования.
        exc_info (bool, optional): Включать ли информацию об исключении (по умолчанию `False`).
        colors (Optional[tuple], optional): Кортеж цветовых значений для сообщения (необязательно).

    Example:
        >>> logger = Logger()
        >>> logger.success('This is a success message')
    """
```

**Назначение**: Записывает сообщение об успехе.

**Параметры**:

- `message` (str): Сообщение об успехе для логирования.
- `ex` (Optional[Exception], optional): Опциональное исключение для логирования.
- `exc_info` (bool, optional): Включать ли информацию об исключении (по умолчанию `False`).
- `colors` (Optional[tuple], optional): Кортеж цветовых значений для сообщения (необязательно).

**Как работает функция**:

Функция `success` вызывает метод `log` с уровнем логирования `logging.INFO` и переданными параметрами.

```
success
│
└───Вызов метода log с уровнем logging.INFO
│
Возврат None
```

**Примеры**:

```python
from src.logger import Logger
import logging
# Пример записи сообщения об успехе
logger = Logger()
logger.success('This is a success message')
```

### `warning`

```python
def warning(message: str, ex: Optional[Exception] = None, exc_info: bool = False, colors: Optional[tuple] = None) -> None:
    """
    Args:
        message (str): Предупреждающее сообщение для логирования.
        ex (Optional[Exception], optional): Опциональное исключение для логирования.
        exc_info (bool, optional): Включать ли информацию об исключении (по умолчанию `False`).
        colors (Optional[tuple], optional): Кортеж цветовых значений для сообщения (необязательно).

    Example:
        >>> logger = Logger()
        >>> logger.warning('This is a warning message')
    """
```

**Назначение**: Записывает предупреждающее сообщение.

**Параметры**:

- `message` (str): Предупреждающее сообщение для логирования.
- `ex` (Optional[Exception], optional): Опциональное исключение для логирования.
- `exc_info` (bool, optional): Включать ли информацию об исключении (по умолчанию `False`).
- `colors` (Optional[tuple], optional): Кортеж цветовых значений для сообщения (необязательно).

**Как работает функция**:

Функция `warning` вызывает метод `log` с уровнем логирования `logging.WARNING` и переданными параметрами.

```
warning
│
└───Вызов метода log с уровнем logging.WARNING
│
Возврат None
```

**Примеры**:

```python
from src.logger import Logger
import logging
# Пример записи предупреждающего сообщения
logger = Logger()
logger.warning('This is a warning message')
```

### `debug`

```python
def debug(message: str, ex: Optional[Exception] = None, exc_info: bool = True, colors: Optional[tuple] = None) -> None:
    """
    Args:
        message (str): Отладочное сообщение для логирования.
        ex (Optional[Exception], optional): Опциональное исключение для логирования.
        exc_info (bool, optional): Включать ли информацию об исключении (по умолчанию `True`).
        colors (Optional[tuple], optional): Кортеж цветовых значений для сообщения (необязательно).

    Example:
        >>> logger = Logger()
        >>> logger.debug('This is a debug message')
    """
```

**Назначение**: Записывает отладочное сообщение.

**Параметры**:

- `message` (str): Отладочное сообщение для логирования.
- `ex` (Optional[Exception], optional): Опциональное исключение для логирования.
- `exc_info` (bool, optional): Включать ли информацию об исключении (по умолчанию `True`).
- `colors` (Optional[tuple], optional): Кортеж цветовых значений для сообщения (необязательно).

**Как работает функция**:

Функция `debug` вызывает метод `log` с уровнем логирования `logging.DEBUG` и переданными параметрами.

```
debug
│
└───Вызов метода log с уровнем logging.DEBUG
│
Возврат None
```

**Примеры**:

```python
from src.logger import Logger
import logging
# Пример записи отладочного сообщения
logger = Logger()
logger.debug('This is a debug message')
```

### `error`

```python
def error(message: str, ex: Optional[Exception] = None, exc_info: bool = True, colors: Optional[tuple] = None) -> None:
    """
    Args:
        message (str): Сообщение об ошибке для логирования.
        ex (Optional[Exception], optional): Опциональное исключение для логирования.
        exc_info (bool, optional): Включать ли информацию об исключении (по умолчанию `True`).
        colors (Optional[tuple], optional): Кортеж цветовых значений для сообщения (необязательно).

    Example:
        >>> logger = Logger()
        >>> logger.error('This is an error message')
    """
```

**Назначение**: Записывает сообщение об ошибке.

**Параметры**:

- `message` (str): Сообщение об ошибке для логирования.
- `ex` (Optional[Exception], optional): Опциональное исключение для логирования.
- `exc_info` (bool, optional): Включать ли информацию об исключении (по умолчанию `True`).
- `colors` (Optional[tuple], optional): Кортеж цветовых значений для сообщения (необязательно).

**Как работает функция**:

Функция `error` вызывает метод `log` с уровнем логирования `logging.ERROR` и переданными параметрами.

```
error
│
└───Вызов метода log с уровнем logging.ERROR
│
Возврат None
```

**Примеры**:

```python
from src.logger import Logger
import logging
# Пример записи сообщения об ошибке
logger = Logger()
logger.error('This is an error message')
```

### `critical`

```python
def critical(message: str, ex: Optional[Exception] = None, exc_info: bool = True, colors: Optional[tuple] = None) -> None:
    """
    Args:
        message (str): Критическое сообщение для логирования.
        ex (Optional[Exception], optional): Опциональное исключение для логирования.
        exc_info (bool, optional): Включать ли информацию об исключении (по умолчанию `True`).
        colors (Optional[tuple], optional): Кортеж цветовых значений для сообщения (необязательно).

    Example:
        >>> logger = Logger()
        >>> logger.critical('This is a critical message')
    """
```

**Назначение**: Записывает критическое сообщение.

**Параметры**:

- `message` (str): Критическое сообщение для логирования.
- `ex` (Optional[Exception], optional): Опциональное исключение для логирования.
- `exc_info` (bool, optional): Включать ли информацию об исключении (по умолчанию `True`).
- `colors` (Optional[tuple], optional): Кортеж цветовых значений для сообщения (необязательно).

**Как работает функция**:

Функция `critical` вызывает метод `log` с уровнем логирования `logging.CRITICAL` и переданными параметрами.

```
critical
│
└───Вызов метода log с уровнем logging.CRITICAL
│
Возврат None
```

**Примеры**:

```python
from src.logger import Logger
import logging
# Пример записи критического сообщения
logger = Logger()
logger.critical('This is a critical message')
```

## Параметры для логгера

Класс `Logger` принимает несколько необязательных параметров для настройки поведения логирования.

- **Level**: Управляет серьезностью захватываемых логов. Общие уровни включают:
  - `logging.DEBUG`: Подробная информация, полезная для диагностики проблем.
  - `logging.INFO`: Общая информация, такая как успешные операции.
  - `logging.WARNING`: Предупреждения, которые не обязательно требуют немедленных действий.
  - `logging.ERROR`: Сообщения об ошибках.
  - `logging.CRITICAL`: Критические ошибки, требующие немедленного внимания.

- **Formatter**: Определяет, как форматируются сообщения лога. По умолчанию сообщения форматируются как `'%(asctime)s - %(levelname)s - %(message)s'`. Вы можете предоставить пользовательский форматтер для различных форматов, таких как JSON.

- **Color**: Цвета для сообщений лога в консоли. Цвета указываются в виде кортежа с двумя элементами:
  - **Цвет текста**: Указывает цвет текста (например, `colorama.Fore.RED`).
  - **Цвет фона**: Указывает цвет фона (например, `colorama.Back.WHITE`).

Цвет можно настроить для разных уровней лога (например, зеленый для информации, красный для ошибок и т. д.).

## Конфигурация логирования в файл (`config`)

Чтобы записывать сообщения в файл, можно указать пути к файлам в конфигурации.

```python
config = {
    'info_log_path': 'logs/info.log',
    'debug_log_path': 'logs/debug.log',
    'errors_log_path': 'logs/errors.log',
    'json_log_path': 'logs/log.json'
}
```

Пути к файлам, указанные в `config`, используются для записи логов в соответствующие файлы для каждого уровня лога.

## Примеры использования

#### 1. Инициализация логгера:

```python
from src.logger import Logger
import logging

logger = Logger()
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
from src.logger import Logger
import logging

logger = Logger()
logger.info('Это информационное сообщение')
logger.success('Это сообщение об успехе')
logger.warning('Это предупреждающее сообщение')
logger.debug('Это отладочное сообщение')
logger.error('Это сообщение об ошибке')
logger.critical('Это критическое сообщение')
```

#### 3. Настройка цветов:

```python
from src.logger import Logger
import logging
import colorama

logger = Logger()
logger.info('Это сообщение будет зеленым', colors=(colorama.Fore.GREEN, colorama.Back.BLACK))
logger.error('У этого сообщения будет красный фон', colors=(colorama.Fore.WHITE, colorama.Back.RED))
```

Этот модуль предоставляет комплексную и гибкую систему логирования для Python-приложений. Вы можете настроить логирование в консоль и файл с различными форматами и цветами, управлять уровнями логирования и корректно обрабатывать исключения. Конфигурация для логирования в файл хранится в словаре `config`, что позволяет легко настраивать параметры.