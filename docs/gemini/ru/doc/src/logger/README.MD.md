# Документация для модуля `src.logger`

## Обзор

Модуль `src.logger` предоставляет гибкую систему логирования, поддерживающую консольный вывод, запись в файлы и логирование в формате JSON. В модуле используется паттерн проектирования "Singleton", чтобы гарантировать использование только одного экземпляра логгера во всем приложении. Логгер поддерживает различные уровни логирования (например, `INFO`, `ERROR`, `DEBUG`) и включает цветной вывод для консольных логов. Также можно настроить форматы вывода логов и управлять записью логов в разные файлы.

## Подробнее

Модуль `src.logger` предназначен для централизованного управления логированием в проекте `hypotez`. Он обеспечивает возможность записи сообщений различной степени важности (информация, отладка, предупреждения, ошибки, критические ошибки) в консоль, файлы или в формате JSON. Использование паттерна Singleton гарантирует, что все компоненты приложения будут использовать один и тот же экземпляр логгера, что упрощает настройку и управление логированием. Модуль также позволяет настраивать форматирование и цветовое оформление логов, что повышает удобство их анализа.

## Классы

### `SingletonMeta`

**Описание**: Метакласс, реализующий паттерн проектирования "Singleton" для логгера.

**Принцип работы**:
Метакласс `SingletonMeta` гарантирует, что при создании экземпляра класса будет возвращен существующий экземпляр, если он уже существует. Если экземпляр класса еще не создан, метакласс создает его и сохраняет для последующего использования.

### `JsonFormatter`

**Описание**: Пользовательский форматтер, выводящий логи в формате JSON.

**Принцип работы**:
Класс `JsonFormatter` наследуется от `logging.Formatter` и переопределяет метод `format`, чтобы форматировать записи лога в виде JSON-строки. Это позволяет легко записывать логи в формате, удобном для машинной обработки и анализа.

### `Logger`

**Описание**: Основной класс логгера, поддерживающий консольный вывод, запись в файлы и логирование в формате JSON.

**Принцип работы**:
Класс `Logger` предоставляет методы для инициализации логгеров, настройки форматов и уровней логирования, а также для записи сообщений различной степени важности. Он использует другие классы и функции модуля для реализации своей функциональности.

**Методы**:

- `__init__`: Инициализирует экземпляр Logger с заполнителями для различных типов логгеров (консольный, файловый и JSON).
- `_configure_logger`: Настраивает и возвращает экземпляр логгера.
- `initialize_loggers`: Инициализирует логгеры для консольного и файлового логирования (информация, отладка, ошибки и JSON).
- `log`: Записывает сообщение на указанном уровне (например, `INFO`, `DEBUG`, `ERROR`) с возможностью добавления исключения и цветового форматирования.
- `info`: Записывает информационное сообщение.
- `success`: Записывает сообщение об успешном выполнении.
- `warning`: Записывает сообщение-предупреждение.
- `debug`: Записывает отладочное сообщение.
- `error`: Записывает сообщение об ошибке.
- `critical`: Записывает критическое сообщение.

## Функции

### `_configure_logger`

```python
def _configure_logger(name: str, log_path: str, level: Optional[int] = logging.DEBUG, formatter: Optional[logging.Formatter] = None, mode: Optional[str] = 'a') -> logging.Logger:
    """
    Настраивает и возвращает экземпляр логгера.

    Args:
        name (str): Имя логгера.
        log_path (str): Путь к файлу лога.
        level (Optional[int], optional): Уровень логирования, например, `logging.DEBUG`. По умолчанию `logging.DEBUG`.
        formatter (Optional[logging.Formatter], optional): Пользовательский форматтер (необязательно).
        mode (Optional[str], optional): Режим файла, например, `'a'` для добавления (по умолчанию).

    Returns:
        logging.Logger: Настроенный экземпляр `logging.Logger`.
    """
```

**Назначение**: Настраивает и возвращает экземпляр логгера с указанными параметрами.

**Параметры**:
- `name` (str): Имя логгера. Используется для идентификации логгера.
- `log_path` (str): Путь к файлу, в который будут записываться логи. Если путь не указан, логи будут выводиться только в консоль.
- `level` (Optional[int], optional): Уровень логирования. Определяет, какие сообщения будут записываться в лог. По умолчанию `logging.DEBUG`.
- `formatter` (Optional[logging.Formatter], optional): Пользовательский форматтер логов. Позволяет задать формат записи логов. Если не указан, используется формат по умолчанию.
- `mode` (Optional[str], optional): Режим открытия файла лога. По умолчанию `'a'` (добавление в конец файла).

**Возвращает**:
- `logging.Logger`: Настроенный экземпляр `logging.Logger`.

**Как работает функция**:

1.  **Создание логгера**: Создается экземпляр класса `logging.Logger` с указанным именем.
2.  **Настройка уровня логирования**: Устанавливается уровень логирования для логгера.
3.  **Создание обработчика**: Создается обработчик (`logging.StreamHandler` для консоли или `logging.FileHandler` для файла) в зависимости от наличия пути к файлу лога.
4.  **Настройка форматтера**: Устанавливается форматтер для обработчика. Если форматтер не указан, используется форматтер по умолчанию.
5.  **Добавление обработчика к логгеру**: Обработчик добавляется к логгеру.
6.  **Возврат логгера**: Возвращается настроенный экземпляр логгера.

```
Создание логгера
    ↓
Настройка уровня логирования
    ↓
Создание обработчика
    ↓
Настройка форматтера
    ↓
Добавление обработчика к логгеру
    ↓
Возврат логгера
```

**Примеры**:

```python
import logging
from src.logger import Logger

# Настройка логгера для записи в файл
logger = Logger._configure_logger(name='file_logger', log_path='logs/file.log', level=logging.INFO)

# Настройка логгера для вывода в консоль с пользовательским форматтером
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
logger = Logger._configure_logger(name='console_logger', log_path='', level=logging.DEBUG, formatter=formatter)
```

### `initialize_loggers`

```python
def initialize_loggers(info_log_path: Optional[str] = '', debug_log_path: Optional[str] = '', errors_log_path: Optional[str] = '', json_log_path: Optional[str] = '') -> None:
    """
    Инициализирует логгеры для консольного и файлового логирования (информация, отладка, ошибки и JSON).

    Args:
        info_log_path (Optional[str], optional): Путь для файла информационных логов (необязательно).
        debug_log_path (Optional[str], optional): Путь для файла отладочных логов (необязательно).
        errors_log_path (Optional[str], optional): Путь для файла логов ошибок (необязательно).
        json_log_path (Optional[str], optional): Путь для файла JSON-логов (необязательно).
    """
```

**Назначение**: Инициализирует логгеры для различных типов логирования, таких как информационные логи, отладочные логи, логи ошибок и логи в формате JSON.

**Параметры**:
- `info_log_path` (Optional[str], optional): Путь к файлу для записи информационных логов. Если не указан, информационные логи не будут записываться в файл. По умолчанию ''.
- `debug_log_path` (Optional[str], optional): Путь к файлу для записи отладочных логов. Если не указан, отладочные логи не будут записываться в файл. По умолчанию ''.
- `errors_log_path` (Optional[str], optional): Путь к файлу для записи логов ошибок. Если не указан, логи ошибок не будут записываться в файл. По умолчанию ''.
- `json_log_path` (Optional[str], optional): Путь к файлу для записи логов в формате JSON. Если не указан, логи в формате JSON не будут записываться в файл. По умолчанию ''.

**Как работает функция**:
1. **Проверка наличия путей**: Проверяется, указаны ли пути к файлам логов для каждого типа логирования (информация, отладка, ошибки, JSON).
2. **Настройка логгеров**: Для каждого указанного пути вызывается функция `_configure_logger` для настройки соответствующего логгера. Если путь не указан, логгер для данного типа логирования не настраивается.

```
Проверка наличия путей
    ↓
Настройка логгеров (info)
    ↓
Настройка логгеров (debug)
    ↓
Настройка логгеров (errors)
    ↓
Настройка логгеров (json)
```

**Примеры**:

```python
from src.logger import Logger

# Инициализация логгеров с указанием путей к файлам логов
Logger.initialize_loggers(
    info_log_path='logs/info.log',
    debug_log_path='logs/debug.log',
    errors_log_path='logs/errors.log',
    json_log_path='logs/log.json'
)
```

### `log`

```python
def log(level: int, message: str, ex: Optional[Exception] = None, exc_info: bool = False, color: Optional[tuple] = None) -> None:
    """
    Записывает сообщение на указанном уровне (например, `INFO`, `DEBUG`, `ERROR`) с возможностью добавления исключения и цветового форматирования.

    Args:
        level (int): Уровень логирования (например, `logging.INFO`, `logging.DEBUG`).
        message (str): Сообщение лога.
        ex (Optional[Exception], optional): Исключение для записи в лог (необязательно).
        exc_info (bool, optional): Флаг, указывающий, нужно ли включать информацию об исключении (по умолчанию `False`).
        color (Optional[tuple], optional): Кортеж с цветами текста и фона для вывода в консоль (необязательно).
    """
```

**Назначение**: Записывает сообщение в лог с указанным уровнем важности, возможностью добавления информации об исключении и цветовым форматированием.

**Параметры**:
- `level` (int): Уровень логирования, определяющий степень важности сообщения (например, `logging.INFO`, `logging.DEBUG`, `logging.ERROR`).
- `message` (str): Текст сообщения, которое необходимо записать в лог.
- `ex` (Optional[Exception], optional): Объект исключения, которое произошло. Если указан, информация об исключении будет добавлена в лог. По умолчанию `None`.
- `exc_info` (bool, optional): Флаг, указывающий, нужно ли включать подробную информацию об исключении (трассировку стека) в лог. По умолчанию `False`.
- `color` (Optional[tuple], optional): Кортеж, содержащий цвета текста и фона для вывода сообщения в консоль. Позволяет выделить сообщение цветом. По умолчанию `None`.

**Как работает функция**:

1.  **Проверка наличия консольного логгера**: Проверяется, был ли инициализирован консольный логгер.
2.  **Форматирование сообщения**: Формируется строка сообщения для вывода в консоль с учетом цветового оформления (если указано).
3.  **Запись сообщения в консоль**: Записывается отформатированное сообщение в консоль с использованием консольного логгера.
4.  **Запись сообщения в файл**: Записывается сообщение в файл лога (если файловый логгер был инициализирован) с учетом уровня логирования и информации об исключении (если указаны).

```
Проверка наличия консольного логгера
    ↓
Форматирование сообщения
    ↓
Запись сообщения в консоль
    ↓
Запись сообщения в файл
```

**Примеры**:

```python
import logging
from src.logger import Logger

# Запись информационного сообщения
Logger.log(level=logging.INFO, message='This is an info message')

# Запись сообщения об ошибке с информацией об исключении
try:
    raise ValueError('Something went wrong')
except ValueError as ex:
    Logger.log(level=logging.ERROR, message='An error occurred', ex=ex, exc_info=True)

# Запись сообщения с цветовым оформлением
from colorama import Fore, Back
Logger.log(level=logging.WARNING, message='This is a warning message', color=(Fore.YELLOW, Back.BLACK))
```

### `info`

```python
def info(message: str, ex: Optional[Exception] = None, exc_info: bool = False, colors: Optional[tuple] = None) -> None:
    """
    Записывает информационное сообщение.

    Args:
        message (str): Информационное сообщение для записи в лог.
        ex (Optional[Exception], optional): Исключение для записи в лог (необязательно).
        exc_info (bool, optional): Флаг, указывающий, нужно ли включать информацию об исключении (по умолчанию `False`).
        colors (Optional[tuple], optional): Кортеж с цветами текста и фона для вывода в консоль (необязательно).
    """
```

**Назначение**: Записывает информационное сообщение в лог.

**Параметры**:
- `message` (str): Текст информационного сообщения.
- `ex` (Optional[Exception], optional): Исключение, которое необходимо зарегистрировать вместе с сообщением. По умолчанию `None`.
- `exc_info` (bool, optional): Флаг, указывающий, нужно ли включать информацию об исключении в лог. По умолчанию `False`.
- `colors` (Optional[tuple], optional): Кортеж с цветами текста и фона для вывода сообщения в консоль. По умолчанию `None`.

**Как работает функция**:
Вызывает функцию `log` с уровнем логирования `logging.INFO` и переданными параметрами.

**Примеры**:

```python
from src.logger import Logger
import logging

# Запись информационного сообщения
Logger.info('This is an info message')

# Запись информационного сообщения с исключением
try:
    result = 1 / 0
except Exception as ex:
    Logger.info('Division by zero error', ex=ex, exc_info=True)

# Запись информационного сообщения с цветовым оформлением
from colorama import Fore, Back
Logger.info('This message will be green', colors=(Fore.GREEN, Back.BLACK))
```

### `success`

```python
def success(message: str, ex: Optional[Exception] = None, exc_info: bool = False, colors: Optional[tuple] = None) -> None:
    """
    Записывает сообщение об успешном выполнении.

    Args:
        message (str): Сообщение об успешном выполнении для записи в лог.
        ex (Optional[Exception], optional): Исключение для записи в лог (необязательно).
        exc_info (bool, optional): Флаг, указывающий, нужно ли включать информацию об исключении (по умолчанию `False`).
        colors (Optional[tuple], optional): Кортеж с цветами текста и фона для вывода в консоль (необязательно).
    """
```

**Назначение**: Записывает сообщение об успешном выполнении операции в лог.

**Параметры**:
- `message` (str): Текст сообщения об успешном выполнении.
- `ex` (Optional[Exception], optional): Исключение, которое произошло во время выполнения операции (если есть). По умолчанию `None`.
- `exc_info` (bool, optional): Флаг, указывающий, нужно ли включать информацию об исключении в лог. По умолчанию `False`.
- `colors` (Optional[tuple], optional): Кортеж, содержащий цвета текста и фона для вывода сообщения в консоль. По умолчанию `None`.

**Как работает функция**:
Вызывает функцию `log` с уровнем логирования `logging.INFO` и переданными параметрами. Используется для обозначения успешного завершения операций.

**Примеры**:

```python
from src.logger import Logger
import logging

# Запись сообщения об успешном выполнении
Logger.success('Operation completed successfully')

# Запись сообщения об успешном выполнении с исключением (например, если операция завершилась успешно после обработки исключения)
try:
    result = int('abc')
except ValueError as ex:
    Logger.success('Operation completed successfully after handling ValueError', ex=ex, exc_info=True)

# Запись сообщения об успешном выполнении с цветовым оформлением
from colorama import Fore, Back
Logger.success('Data saved successfully', colors=(Fore.GREEN, Back.BLACK))
```

### `warning`

```python
def warning(message: str, ex: Optional[Exception] = None, exc_info: bool = False, colors: Optional[tuple] = None) -> None:
    """
    Записывает сообщение-предупреждение.

    Args:
        message (str): Предупреждающее сообщение для записи в лог.
        ex (Optional[Exception], optional): Исключение для записи в лог (необязательно).
        exc_info (bool, optional): Флаг, указывающий, нужно ли включать информацию об исключении (по умолчанию `False`).
        colors (Optional[tuple], optional): Кортеж с цветами текста и фона для вывода в консоль (необязательно).
    """
```

**Назначение**: Записывает предупреждающее сообщение в лог. Предупреждения используются для обозначения ситуаций, которые не являются ошибками, но могут привести к проблемам в будущем.

**Параметры**:
- `message` (str): Текст предупреждающего сообщения.
- `ex` (Optional[Exception], optional): Исключение, связанное с предупреждением (если есть). По умолчанию `None`.
- `exc_info` (bool, optional): Флаг, указывающий, нужно ли включать информацию об исключении в лог. По умолчанию `False`.
- `colors` (Optional[tuple], optional): Кортеж с цветами текста и фона для вывода сообщения в консоль. По умолчанию `None`.

**Как работает функция**:
Вызывает функцию `log` с уровнем логирования `logging.WARNING` и переданными параметрами.

**Примеры**:

```python
from src.logger import Logger
import logging

# Запись предупреждающего сообщения
Logger.warning('This is a warning message')

# Запись предупреждающего сообщения с исключением
try:
    value = int('abc')
except ValueError as ex:
    Logger.warning('Invalid input value', ex=ex, exc_info=True)

# Запись предупреждающего сообщения с цветовым оформлением
from colorama import Fore, Back
Logger.warning('Disk space is running low', colors=(Fore.YELLOW, Back.BLACK))
```

### `debug`

```python
def debug(message: str, ex: Optional[Exception] = None, exc_info: bool = True, colors: Optional[tuple] = None) -> None:
    """
    Записывает отладочное сообщение.

    Args:
        message (str): Отладочное сообщение для записи в лог.
        ex (Optional[Exception], optional): Исключение для записи в лог (необязательно).
        exc_info (bool, optional): Флаг, указывающий, нужно ли включать информацию об исключении (по умолчанию `True`).
        colors (Optional[tuple], optional): Кортеж с цветами текста и фона для вывода в консоль (необязательно).
    """
```

**Назначение**: Записывает отладочное сообщение в лог. Отладочные сообщения используются для предоставления подробной информации о работе приложения, которая может быть полезна при отладке.

**Параметры**:
- `message` (str): Текст отладочного сообщения.
- `ex` (Optional[Exception], optional): Исключение, которое необходимо зарегистрировать вместе с сообщением. По умолчанию `None`.
- `exc_info` (bool, optional): Флаг, указывающий, нужно ли включать информацию об исключении в лог. По умолчанию `True`.
- `colors` (Optional[tuple], optional): Кортеж с цветами текста и фона для вывода сообщения в консоль. По умолчанию `None`.

**Как работает функция**:
Вызывает функцию `log` с уровнем логирования `logging.DEBUG` и переданными параметрами.

**Примеры**:

```python
from src.logger import Logger
import logging

# Запись отладочного сообщения
Logger.debug('This is a debug message')

# Запись отладочного сообщения с исключением
try:
    result = 1 / 0
except Exception as ex:
    Logger.debug('Division by zero error', ex=ex, exc_info=True)

# Запись отладочного сообщения с цветовым оформлением
from colorama import Fore, Back
Logger.debug('Variable x has value: 10', colors=(Fore.CYAN, Back.BLACK))
```

### `error`

```python
def error(message: str, ex: Optional[Exception] = None, exc_info: bool = True, colors: Optional[tuple] = None) -> None:
    """
    Записывает сообщение об ошибке.

    Args:
        message (str): Сообщение об ошибке для записи в лог.
        ex (Optional[Exception], optional): Исключение для записи в лог (необязательно).
        exc_info (bool, optional): Флаг, указывающий, нужно ли включать информацию об исключении (по умолчанию `True`).
        colors (Optional[tuple], optional): Кортеж с цветами текста и фона для вывода в консоль (необязательно).
    """
```

**Назначение**: Записывает сообщение об ошибке в лог. Сообщения об ошибках используются для обозначения ситуаций, когда в приложении произошла ошибка, которая может привести к непредсказуемым последствиям.

**Параметры**:
- `message` (str): Текст сообщения об ошибке.
- `ex` (Optional[Exception], optional): Объект исключения, которое произошло. Если указан, информация об исключении будет добавлена в лог. По умолчанию `None`.
- `exc_info` (bool, optional): Флаг, указывающий, нужно ли включать подробную информацию об исключении (трассировку стека) в лог. По умолчанию `True`.
- `colors` (Optional[tuple], optional): Кортеж, содержащий цвета текста и фона для вывода сообщения в консоль. Позволяет выделить сообщение цветом. По умолчанию `None`.

**Как работает функция**:
Вызывает функцию `log` с уровнем логирования `logging.ERROR` и переданными параметрами.

**Примеры**:

```python
from src.logger import Logger
import logging

# Запись сообщения об ошибке
Logger.error('This is an error message')

# Запись сообщения об ошибке с информацией об исключении
try:
    raise ValueError('Invalid input')
except ValueError as ex:
    Logger.error('ValueError occurred', ex=ex, exc_info=True)

# Запись сообщения об ошибке с цветовым оформлением
from colorama import Fore, Back
Logger.error('Failed to connect to database', colors=(Fore.WHITE, Back.RED))
```

### `critical`

```python
def critical(message: str, ex: Optional[Exception] = None, exc_info: bool = True, colors: Optional[tuple] = None) -> None:
    """
    Записывает критическое сообщение.

    Args:
        message (str): Критическое сообщение для записи в лог.
        ex (Optional[Exception], optional): Исключение для записи в лог (необязательно).
        exc_info (bool, optional): Флаг, указывающий, нужно ли включать информацию об исключении (по умолчанию `True`).
        colors (Optional[tuple], optional): Кортеж с цветами текста и фона для вывода в консоль (необязательно).
    """
```

**Назначение**: Записывает критическое сообщение в лог. Критические сообщения используются для обозначения ситуаций, когда в приложении произошла серьезная ошибка, которая может привести к остановке работы приложения или потере данных.

**Параметры**:
- `message` (str): Текст критического сообщения.
- `ex` (Optional[Exception], optional): Объект исключения, которое произошло. Если указан, информация об исключении будет добавлена в лог. По умолчанию `None`.
- `exc_info` (bool, optional): Флаг, указывающий, нужно ли включать подробную информацию об исключении (трассировку стека) в лог. По умолчанию `True`.
- `colors` (Optional[tuple], optional): Кортеж, содержащий цвета текста и фона для вывода сообщения в консоль. Позволяет выделить сообщение цветом. По умолчанию `None`.

**Как работает функция**:
Вызывает функцию `log` с уровнем логирования `logging.CRITICAL` и переданными параметрами.

**Примеры**:

```python
from src.logger import Logger
import logging

# Запись критического сообщения
Logger.critical('This is a critical message')

# Запись критического сообщения с информацией об исключении
try:
    raise RuntimeError('Application is shutting down')
except RuntimeError as ex:
    Logger.critical('RuntimeError occurred', ex=ex, exc_info=True)

# Запись критического сообщения с цветовым оформлением
from colorama import Fore, Back
Logger.critical('Data corruption detected', colors=(Fore.WHITE, Back.RED))
```

## Параметры для логгера

Класс `Logger` принимает несколько необязательных параметров для настройки поведения логирования.

- **Level**: Управляет серьезностью регистрируемых логов. Общие уровни включают:
  - `logging.DEBUG`: Подробная информация, полезная для диагностики проблем.
  - `logging.INFO`: Общая информация, например, об успешных операциях.
  - `logging.WARNING`: Предупреждения, которые не обязательно требуют немедленных действий.
  - `logging.ERROR`: Сообщения об ошибках.
  - `logging.CRITICAL`: Критические ошибки, требующие немедленного внимания.

- **Formatter**: Определяет, как форматируются сообщения журнала. По умолчанию сообщения форматируются как `'%(asctime)s - %(levelname)s - %(message)s'`. Вы можете предоставить пользовательский форматтер для различных форматов, таких как JSON.

- **Color**: Цвета для сообщений журнала в консоли. Цвета указываются в виде кортежа с двумя элементами:
  - **Text color**: Указывает цвет текста (например, `colorama.Fore.RED`).
  - **Background color**: Указывает цвет фона (например, `colorama.Back.WHITE`).

Цвет можно настроить для различных уровней журнала (например, зеленый для информации, красный для ошибок и т. д.).

## Конфигурация файлового логирования (`config`)

Чтобы регистрировать сообщения в файл, можно указать пути к файлам в конфигурации.

```python
config = {
    'info_log_path': 'logs/info.log',
    'debug_log_path': 'logs/debug.log',
    'errors_log_path': 'logs/errors.log',
    'json_log_path': 'logs/log.json'
}
```

Пути к файлам, указанные в `config`, используются для записи логов в соответствующие файлы для каждого уровня логирования.

## Примеры использования

#### 1. Инициализация логгера:

```python
from src.logger import Logger

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
from src.logger import Logger

Logger.info('This is an info message')
Logger.success('This is a success message')
Logger.warning('This is a warning message')
Logger.debug('This is a debug message')
Logger.error('This is an error message')
Logger.critical('This is a critical message')
```

#### 3. Настройка цветов:

```python
from src.logger import Logger
import colorama

Logger.info('This message will be green', colors=(colorama.Fore.GREEN, colorama.Back.BLACK))
Logger.error('This message will have a red background', colors=(colorama.Fore.WHITE, colorama.Back.RED))
```

Этот модуль предоставляет комплексную и гибкую систему логирования для Python-приложений. Вы можете настроить консольное и файловое логирование с различными форматами и цветами, управлять уровнями логирования и корректно обрабатывать исключения. Конфигурация для файлового логирования хранится в словаре `config`, что позволяет легко настраивать его.