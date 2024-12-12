# Документация модуля `src.logger`

## Оглавление
- [Обзор](#обзор)
- [Классы](#классы)
    - [SingletonMeta](#singletonmeta)
    - [JsonFormatter](#jsonformatter)
    - [Logger](#logger)
- [Функции](#функции)
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
- [Параметры Logger](#параметры-logger)
- [Конфигурация файлового логирования](#конфигурация-файлового-логирования-config)
- [Пример использования](#пример-использования)
    - [Инициализация Logger](#1-инициализация-logger)
    - [Логирование сообщений на разных уровнях](#2-логирование-сообщений-на-разных-уровнях)
    - [Настройка цветов](#3-настройка-цветов)

## Обзор

Модуль `src.logger` предоставляет гибкую систему логирования, поддерживающую вывод в консоль, запись в файлы и логирование в формате JSON. Он использует паттерн проектирования Singleton, чтобы обеспечить использование только одного экземпляра логгера во всем приложении. Логгер поддерживает различные уровни логирования (например, `INFO`, `ERROR`, `DEBUG`) и включает цветной вывод для консольных логов. Вы также можете настраивать форматы вывода логов и управлять логированием в разные файлы.

---

## Классы

### `SingletonMeta`

**Описание**: Метакласс, реализующий паттерн проектирования Singleton для логгера.

### `JsonFormatter`

**Описание**: Пользовательский форматтер, выводящий логи в формате JSON.

### `Logger`

**Описание**: Основной класс логгера, поддерживающий вывод в консоль, запись в файлы и логирование в формате JSON.

**Методы**:
- [`__init__`](#__init__): Инициализирует экземпляр Logger.
- [`_configure_logger`](#_configure_logger): Конфигурирует и возвращает экземпляр логгера.
- [`initialize_loggers`](#initialize_loggers): Инициализирует логгеры для консольного и файлового логирования (info, debug, error и JSON).
- [`log`](#log): Логирует сообщение на указанном уровне с возможностью добавления исключения и форматирования цвета.
- [`info`](#info): Логирует информационное сообщение.
- [`success`](#success): Логирует сообщение об успехе.
- [`warning`](#warning): Логирует предупреждающее сообщение.
- [`debug`](#debug): Логирует отладочное сообщение.
- [`error`](#error): Логирует сообщение об ошибке.
- [`critical`](#critical): Логирует критическое сообщение.

---

## Функции

### `__init__`

**Описание**: Инициализирует экземпляр `Logger` с плейсхолдерами для разных типов логгеров (консоль, файл и JSON).

### `_configure_logger`

```python
def _configure_logger(name: str, log_path: str, level: Optional[int] = logging.DEBUG, formatter: Optional[logging.Formatter] = None, mode: Optional[str] = 'a') -> logging.Logger
```

**Описание**: Конфигурирует и возвращает экземпляр логгера.

**Параметры**:
- `name` (str): Имя логгера.
- `log_path` (str): Путь к файлу журнала.
- `level` (Optional[int], optional): Уровень логирования, например, `logging.DEBUG`. По умолчанию `logging.DEBUG`.
- `formatter` (Optional[logging.Formatter], optional): Пользовательский форматтер (опционально).
- `mode` (Optional[str], optional): Режим файла, например, `'a'` для добавления (по умолчанию).

**Возвращает**:
- `logging.Logger`: Сконфигурированный экземпляр `logging.Logger`.

### `initialize_loggers`

```python
def initialize_loggers(info_log_path: Optional[str] = '', debug_log_path: Optional[str] = '', errors_log_path: Optional[str] = '', json_log_path: Optional[str] = '')
```

**Описание**: Инициализирует логгеры для консольного и файлового логирования (info, debug, error и JSON).

**Параметры**:
- `info_log_path` (Optional[str], optional): Путь к файлу журнала info (опционально).
- `debug_log_path` (Optional[str], optional): Путь к файлу журнала debug (опционально).
- `errors_log_path` (Optional[str], optional): Путь к файлу журнала ошибок (опционально).
- `json_log_path` (Optional[str], optional): Путь к файлу журнала JSON (опционально).

### `log`

```python
def log(level, message, ex=None, exc_info=False, color=None)
```

**Описание**: Логирует сообщение на указанном уровне (например, `INFO`, `DEBUG`, `ERROR`) с возможностью добавления исключения и форматирования цвета.

**Параметры**:
- `level`: Уровень логирования (например, `logging.INFO`, `logging.DEBUG`).
- `message`: Сообщение журнала.
- `ex` (optional): Опциональное исключение для логирования.
- `exc_info` (bool, optional): Включать ли информацию об исключении (по умолчанию `False`).
- `color` (tuple, optional): Кортеж с цветами текста и фона для вывода в консоль (опционально).

### `info`

```python
def info(message, ex=None, exc_info=False, colors: Optional[tuple] = None)
```

**Описание**: Логирует информационное сообщение.

**Параметры**:
- `message`: Информационное сообщение для логирования.
- `ex` (optional): Опциональное исключение для логирования.
- `exc_info` (bool, optional): Включать ли информацию об исключении (по умолчанию `False`).
- `colors` (tuple, optional): Кортеж значений цвета для сообщения (опционально).

### `success`

```python
def success(message, ex=None, exc_info=False, colors: Optional[tuple] = None)
```

**Описание**: Логирует сообщение об успехе.

**Параметры**:
- Аналогично `info`.

### `warning`

```python
def warning(message, ex=None, exc_info=False, colors: Optional[tuple] = None)
```

**Описание**: Логирует предупреждающее сообщение.

**Параметры**:
- Аналогично `info`.

### `debug`

```python
def debug(message, ex=None, exc_info=True, colors: Optional[tuple] = None)
```

**Описание**: Логирует отладочное сообщение.

**Параметры**:
- Аналогично `info`.

### `error`

```python
def error(message, ex=None, exc_info=True, colors: Optional[tuple] = None)
```

**Описание**: Логирует сообщение об ошибке.

**Параметры**:
- Аналогично `info`.

### `critical`

```python
def critical(message, ex=None, exc_info=True, colors: Optional[tuple] = None)
```

**Описание**: Логирует критическое сообщение.

**Параметры**:
- Аналогично `info`.

---

## Параметры Logger

Класс `Logger` принимает несколько необязательных параметров для настройки поведения логирования.

- **Уровень**: Контролирует серьезность записываемых логов. Распространенные уровни включают:
    - `logging.DEBUG`: Подробная информация, полезная для диагностики проблем.
    - `logging.INFO`: Общая информация, например, об успешных операциях.
    - `logging.WARNING`: Предупреждения, не обязательно требующие немедленных действий.
    - `logging.ERROR`: Сообщения об ошибках.
    - `logging.CRITICAL`: Критические ошибки, требующие немедленного внимания.

- **Форматтер**: Определяет способ форматирования сообщений журнала. По умолчанию сообщения форматируются как `'%(asctime)s - %(levelname)s - %(message)s'`. Вы можете предоставить пользовательский форматтер для других форматов, например, JSON.

- **Цвет**: Цвета для сообщений журнала в консоли. Цвета указываются в виде кортежа из двух элементов:
    - **Цвет текста**: Указывает цвет текста (например, `colorama.Fore.RED`).
    - **Цвет фона**: Указывает цвет фона (например, `colorama.Back.WHITE`).

Цвет можно настроить для различных уровней логов (например, зеленый для info, красный для ошибок и т.д.).

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

Пути к файлам, предоставленные в `config`, используются для записи логов в соответствующие файлы для каждого уровня логирования.

---

## Пример использования

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

Этот модуль предоставляет всеобъемлющую и гибкую систему логирования для Python-приложений. Вы можете настраивать вывод в консоль и запись в файлы с разными форматами и цветами, управлять уровнями логирования и корректно обрабатывать исключения. Конфигурация для файлового логирования хранится в словаре `config`, что обеспечивает легкую настройку.