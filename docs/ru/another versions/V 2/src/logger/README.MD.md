# Документация модуля `src.logger`

## Оглавление
1. [Обзор](#обзор)
2. [Классы](#классы)
    - [`SingletonMeta`](#singletonmeta)
    - [`JsonFormatter`](#jsonformatter)
    - [`Logger`](#logger)
3. [Функции](#функции)
    - [`__init__`](#__init__)
    - [`_configure_logger`](#_configure_logger)
    - [`initialize_loggers`](#initialize_loggers)
    - [`log`](#log)
    - [`info`](#info)
    - [`success`](#success)
    - [`warning`](#warning)
    - [`debug`](#debug)
    - [`error`](#error)
    - [`critical`](#critical)
4. [Параметры Logger](#параметры-logger)
5. [Конфигурация файлового логирования](#конфигурация-файлового-логирования-config)
6. [Примеры использования](#примеры-использования)
    - [Инициализация Logger](#1-инициализация-logger)
    - [Логирование сообщений на разных уровнях](#2-логирование-сообщений-на-разных-уровнях)
    - [Настройка цветов](#3-настройка-цветов)
    
## Обзор

Модуль `src.logger` предоставляет гибкую систему логирования, поддерживающую вывод в консоль, файлы и JSON-формат. Он использует шаблон проектирования Singleton, чтобы гарантировать использование только одного экземпляра логгера во всем приложении. Логгер поддерживает различные уровни логирования (например, `INFO`, `ERROR`, `DEBUG`) и включает цветной вывод для консольных логов. Вы также можете настраивать форматы вывода логов и управлять записью логов в разные файлы.

---

## Классы

### `SingletonMeta`
**Описание**: Метакласс, реализующий шаблон проектирования Singleton для логгера.

### `JsonFormatter`
**Описание**: Пользовательский форматтер, выводящий логи в формате JSON.

### `Logger`
**Описание**: Основной класс логгера, поддерживающий вывод в консоль, файлы и JSON.

**Методы**:
- `__init__`: Инициализирует экземпляр Logger с заполнителями для различных типов логгеров (консоль, файл и JSON).
- `_configure_logger`: Настраивает и возвращает экземпляр логгера.
- `initialize_loggers`: Инициализирует логгеры для консольного и файлового логирования (info, debug, error и JSON).
- `log`: Записывает сообщение на указанном уровне.
- `info`: Записывает информационное сообщение.
- `success`: Записывает сообщение об успешном выполнении.
- `warning`: Записывает предупреждающее сообщение.
- `debug`: Записывает отладочное сообщение.
- `error`: Записывает сообщение об ошибке.
- `critical`: Записывает критическое сообщение.

---

## Функции

### `__init__`
**Описание**: Инициализирует экземпляр `Logger` с заполнителями для различных типов логгеров (консоль, файл и JSON).

### `_configure_logger`
```python
def _configure_logger(name: str, log_path: str, level: Optional[int] = logging.DEBUG, formatter: Optional[logging.Formatter] = None, mode: Optional[str] = 'a') -> logging.Logger:
    """
    Args:
        name (str): Имя логгера.
        log_path (str): Путь к файлу лога.
        level (Optional[int], optional): Уровень логирования, например, `logging.DEBUG`. По умолчанию `logging.DEBUG`.
        formatter (Optional[logging.Formatter], optional): Пользовательский форматтер (опционально).
        mode (Optional[str], optional): Режим файла, например, `'a'` для добавления (по умолчанию).

    Returns:
        logging.Logger: Настроенный экземпляр `logging.Logger`.
    """
```
**Описание**: Настраивает и возвращает экземпляр логгера.

**Параметры**:
- `name` (str): Имя логгера.
- `log_path` (str): Путь к файлу лога.
- `level` (Optional[int], optional): Уровень логирования, например, `logging.DEBUG`. По умолчанию `logging.DEBUG`.
- `formatter` (Optional[logging.Formatter], optional): Пользовательский форматтер (опционально).
- `mode` (Optional[str], optional): Режим файла, например, `'a'` для добавления (по умолчанию).

**Возвращает**:
- `logging.Logger`: Настроенный экземпляр `logging.Logger`.

### `initialize_loggers`
```python
def initialize_loggers(info_log_path: Optional[str] = '', debug_log_path: Optional[str] = '', errors_log_path: Optional[str] = '', json_log_path: Optional[str] = '') -> None:
    """
    Args:
        info_log_path (Optional[str], optional): Путь для файла информационных логов (опционально).
        debug_log_path (Optional[str], optional): Путь для файла отладочных логов (опционально).
        errors_log_path (Optional[str], optional): Путь для файла логов ошибок (опционально).
        json_log_path (Optional[str], optional): Путь для файла JSON логов (опционально).
    """
```
**Описание**: Инициализирует логгеры для консольного и файлового логирования (info, debug, error и JSON).

**Параметры**:
- `info_log_path` (Optional[str], optional): Путь для файла информационных логов (опционально).
- `debug_log_path` (Optional[str], optional): Путь для файла отладочных логов (опционально).
- `errors_log_path` (Optional[str], optional): Путь для файла логов ошибок (опционально).
- `json_log_path` (Optional[str], optional): Путь для файла JSON логов (опционально).

### `log`
```python
def log(level: int, message: str, ex: Optional[Exception] = None, exc_info: bool = False, color: Optional[tuple] = None) -> None:
    """
    Args:
        level (int): Уровень логирования (например, `logging.INFO`, `logging.DEBUG`).
        message (str): Сообщение лога.
        ex (Optional[Exception], optional): Опциональное исключение для логирования.
        exc_info (bool, optional): Включать ли информацию об исключении (по умолчанию `False`).
        color (Optional[tuple], optional): Кортеж с цветами текста и фона для вывода в консоль (опционально).
    """
```
**Описание**: Записывает сообщение на указанном уровне (например, `INFO`, `DEBUG`, `ERROR`) с возможностью добавления исключения и форматирования цвета.

**Параметры**:
- `level` (int): Уровень логирования (например, `logging.INFO`, `logging.DEBUG`).
- `message` (str): Сообщение лога.
- `ex` (Optional[Exception], optional): Опциональное исключение для логирования.
- `exc_info` (bool, optional): Включать ли информацию об исключении (по умолчанию `False`).
- `color` (Optional[tuple], optional): Кортеж с цветами текста и фона для вывода в консоль (опционально).

### `info`
```python
def info(message: str, ex: Optional[Exception] = None, exc_info: bool = False, colors: Optional[tuple] = None) -> None:
    """
    Args:
        message (str): Информационное сообщение для записи в лог.
        ex (Optional[Exception], optional): Опциональное исключение для логирования.
        exc_info (bool, optional): Включать ли информацию об исключении (по умолчанию `False`).
        colors (Optional[tuple], optional): Кортеж с цветами текста и фона для сообщения (опционально).
    """
```
**Описание**: Записывает информационное сообщение.

**Параметры**:
- `message` (str): Информационное сообщение для записи в лог.
- `ex` (Optional[Exception], optional): Опциональное исключение для логирования.
- `exc_info` (bool, optional): Включать ли информацию об исключении (по умолчанию `False`).
- `colors` (Optional[tuple], optional): Кортеж с цветами текста и фона для сообщения (опционально).

### `success`
```python
def success(message: str, ex: Optional[Exception] = None, exc_info: bool = False, colors: Optional[tuple] = None) -> None:
    """
    Args:
        message (str): Сообщение об успехе для записи в лог.
        ex (Optional[Exception], optional): Опциональное исключение для логирования.
        exc_info (bool, optional): Включать ли информацию об исключении (по умолчанию `False`).
        colors (Optional[tuple], optional): Кортеж с цветами текста и фона для сообщения (опционально).
    """
```
**Описание**: Записывает сообщение об успешном выполнении.

**Параметры**:
- `message` (str): Сообщение об успехе для записи в лог.
- `ex` (Optional[Exception], optional): Опциональное исключение для логирования.
- `exc_info` (bool, optional): Включать ли информацию об исключении (по умолчанию `False`).
- `colors` (Optional[tuple], optional): Кортеж с цветами текста и фона для сообщения (опционально).

### `warning`
```python
def warning(message: str, ex: Optional[Exception] = None, exc_info: bool = False, colors: Optional[tuple] = None) -> None:
    """
    Args:
        message (str): Предупреждающее сообщение для записи в лог.
        ex (Optional[Exception], optional): Опциональное исключение для логирования.
        exc_info (bool, optional): Включать ли информацию об исключении (по умолчанию `False`).
        colors (Optional[tuple], optional): Кортеж с цветами текста и фона для сообщения (опционально).
    """
```
**Описание**: Записывает предупреждающее сообщение.

**Параметры**:
- `message` (str): Предупреждающее сообщение для записи в лог.
- `ex` (Optional[Exception], optional): Опциональное исключение для логирования.
- `exc_info` (bool, optional): Включать ли информацию об исключении (по умолчанию `False`).
- `colors` (Optional[tuple], optional): Кортеж с цветами текста и фона для сообщения (опционально).

### `debug`
```python
def debug(message: str, ex: Optional[Exception] = None, exc_info: bool = True, colors: Optional[tuple] = None) -> None:
    """
    Args:
        message (str): Отладочное сообщение для записи в лог.
        ex (Optional[Exception], optional): Опциональное исключение для логирования.
        exc_info (bool, optional): Включать ли информацию об исключении (по умолчанию `True`).
        colors (Optional[tuple], optional): Кортеж с цветами текста и фона для сообщения (опционально).
    """
```
**Описание**: Записывает отладочное сообщение.

**Параметры**:
- `message` (str): Отладочное сообщение для записи в лог.
- `ex` (Optional[Exception], optional): Опциональное исключение для логирования.
- `exc_info` (bool, optional): Включать ли информацию об исключении (по умолчанию `True`).
- `colors` (Optional[tuple], optional): Кортеж с цветами текста и фона для сообщения (опционально).

### `error`
```python
def error(message: str, ex: Optional[Exception] = None, exc_info: bool = True, colors: Optional[tuple] = None) -> None:
    """
    Args:
        message (str): Сообщение об ошибке для записи в лог.
        ex (Optional[Exception], optional): Опциональное исключение для логирования.
        exc_info (bool, optional): Включать ли информацию об исключении (по умолчанию `True`).
        colors (Optional[tuple], optional): Кортеж с цветами текста и фона для сообщения (опционально).
    """
```
**Описание**: Записывает сообщение об ошибке.

**Параметры**:
- `message` (str): Сообщение об ошибке для записи в лог.
- `ex` (Optional[Exception], optional): Опциональное исключение для логирования.
- `exc_info` (bool, optional): Включать ли информацию об исключении (по умолчанию `True`).
- `colors` (Optional[tuple], optional): Кортеж с цветами текста и фона для сообщения (опционально).

### `critical`
```python
def critical(message: str, ex: Optional[Exception] = None, exc_info: bool = True, colors: Optional[tuple] = None) -> None:
    """
    Args:
        message (str): Критическое сообщение для записи в лог.
        ex (Optional[Exception], optional): Опциональное исключение для логирования.
        exc_info (bool, optional): Включать ли информацию об исключении (по умолчанию `True`).
        colors (Optional[tuple], optional): Кортеж с цветами текста и фона для сообщения (опционально).
    """
```
**Описание**: Записывает критическое сообщение.

**Параметры**:
- `message` (str): Критическое сообщение для записи в лог.
- `ex` (Optional[Exception], optional): Опциональное исключение для логирования.
- `exc_info` (bool, optional): Включать ли информацию об исключении (по умолчанию `True`).
- `colors` (Optional[tuple], optional): Кортеж с цветами текста и фона для сообщения (опционально).

---

## Параметры Logger

Класс `Logger` принимает несколько необязательных параметров для настройки поведения логирования.

- **Уровень (Level)**: Контролирует серьезность логов, которые записываются. Общие уровни включают:
    - `logging.DEBUG`: Подробная информация, полезная для диагностики проблем.
    - `logging.INFO`: Общая информация, например, об успешных операциях.
    - `logging.WARNING`: Предупреждения, которые не обязательно требуют немедленных действий.
    - `logging.ERROR`: Сообщения об ошибках.
    - `logging.CRITICAL`: Критические ошибки, требующие немедленного внимания.
- **Форматтер (Formatter)**: Определяет, как форматируются сообщения лога. По умолчанию сообщения форматируются как `'%(asctime)s - %(levelname)s - %(message)s'`. Вы можете предоставить пользовательский форматтер для других форматов, таких как JSON.
- **Цвет (Color)**: Цвета для сообщений лога в консоли. Цвета указываются в виде кортежа с двумя элементами:
    - **Цвет текста**: Задает цвет текста (например, `colorama.Fore.RED`).
    - **Цвет фона**: Задает цвет фона (например, `colorama.Back.WHITE`).

Цвет можно настраивать для разных уровней лога (например, зеленый для info, красный для ошибок и т.д.).

---

## Конфигурация файлового логирования (`config`)

Чтобы записывать сообщения в файл, вы можете указать пути к файлам в конфигурации.
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

## Примеры использования

### 1. Инициализация Logger
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

### 2. Логирование сообщений на разных уровнях
```python
logger.info('Это информационное сообщение')
logger.success('Это сообщение об успехе')
logger.warning('Это предупреждающее сообщение')
logger.debug('Это отладочное сообщение')
logger.error('Это сообщение об ошибке')
logger.critical('Это критическое сообщение')
```

### 3. Настройка цветов
```python
logger.info('Это сообщение будет зеленым', colors=(colorama.Fore.GREEN, colorama.Back.BLACK))
logger.error('У этого сообщения будет красный фон', colors=(colorama.Fore.WHITE, colorama.Back.RED))
```

---

Модуль предоставляет комплексную и гибкую систему логирования для Python-приложений. Вы можете настраивать консольное и файловое логирование с различными форматами и цветами, управлять уровнями логирования и обрабатывать исключения. Конфигурация для файлового логирования хранится в словаре `config`, что позволяет легко ее настраивать.