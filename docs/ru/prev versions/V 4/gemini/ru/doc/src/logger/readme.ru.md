# Документация для модуля `src.logger`

## Обзор

Модуль `src.logger` предоставляет гибкую систему логирования для Python-приложений. Он поддерживает логирование в консоль, файлы и в формате JSON. Модуль использует паттерн Singleton, чтобы обеспечить использование единственного экземпляра логгера во всем приложении.

## Оглавление

- [Классы](#классы)
  - [SingletonMeta](#singletonmeta)
  - [JsonFormatter](#jsonformatter)
  - [Logger](#logger)
- [Функции](#функции)
  - [`_configure_logger`](#_configure_logger)
  - [`initialize_loggers`](#initialize_loggers)
  - [`log`](#log)
- [Параметры логгера](#параметры-логгера)
- [Конфигурация для логирования в файл (`config`)](#конфигурация-для-логирования-в-файл-config)
- [Примеры использования](#примеры-использования)

## Подробней

Модуль `src.logger` предназначен для централизованного и гибкого управления логированием в приложении `hypotez`. Он позволяет записывать сообщения различных уровней важности (например, `INFO`, `ERROR`, `DEBUG`) в консоль, файлы, а также в формате JSON. Использование Singleton гарантирует, что все компоненты приложения используют один и тот же экземпляр логгера, что упрощает настройку и управление логированием.

## Классы

### `SingletonMeta`

**Описание**: Метакласс, реализующий шаблон Singleton для логгера.

**Методы**:
- `__call__`: Обеспечивает создание только одного экземпляра класса.

### `JsonFormatter`

**Описание**: Кастомный форматтер для вывода логов в формате JSON.

**Методы**:
- `format`: Преобразует запись лога в формат JSON.

### `Logger`

**Описание**: Основной класс логгера, поддерживающий логирование в консоль, файлы и в формате JSON.

**Методы**:
- `__init__`: Инициализирует экземпляр класса Logger с плейсхолдерами для различных типов логгеров (консоль, файлы и JSON).
- `_configure_logger`: Настраивает и возвращает экземпляр логгера.
- `initialize_loggers`: Инициализирует логгеры для логирования в консоль и файлы (информация, отладка, ошибки и JSON).
- `log`: Логирует сообщение на указанном уровне с возможным исключением и цветовым форматированием.
- `info`: Логирует информационное сообщение.
- `success`: Логирует сообщение об успешной операции.
- `warning`: Логирует предупреждение.
- `debug`: Логирует сообщение для отладки.
- `error`: Логирует сообщение об ошибке.
- `critical`: Логирует критическое сообщение.

## Функции

### `_configure_logger`

```python
def _configure_logger(name: str, log_path: str, level: Optional[int] = logging.DEBUG, formatter: Optional[logging.Formatter] = None, mode: Optional[str] = 'a') -> logging.Logger:
    """
    Настраивает и возвращает экземпляр логгера.

    Args:
        name (str): Имя логгера.
        log_path (str): Путь к файлу логов.
        level (Optional[int], optional): Уровень логирования, например, `logging.DEBUG`. По умолчанию `logging.DEBUG`.
        formatter (Optional[logging.Formatter], optional): Кастомный форматтер (опционально). По умолчанию `None`.
        mode (Optional[str], optional): Режим работы с файлом, например, `'a'` для добавления. По умолчанию `'a'`.

    Returns:
        logging.Logger: Настроенный экземпляр `logging.Logger`.

    Raises:
        FileNotFoundError: Если указанный путь к файлу не существует.

    Example:
        >>> logger = _configure_logger('my_logger', 'logs/debug.log', logging.DEBUG)
    """
    ...
```

**Описание**: Настраивает и возвращает экземпляр логгера.

**Параметры**:
- `name` (str): Имя логгера.
- `log_path` (str): Путь к файлу логов.
- `level` (Optional[int], optional): Уровень логирования, например, `logging.DEBUG`. Значение по умолчанию — `logging.DEBUG`.
- `formatter` (Optional[logging.Formatter], optional): Кастомный форматтер (опционально).
- `mode` (Optional[str], optional): Режим работы с файлом, например, `'a'` для добавления (значение по умолчанию).

**Возвращает**:
- `logging.Logger`: Настроенный экземпляр `logging.Logger`.

### `initialize_loggers`

```python
def initialize_loggers(info_log_path: Optional[str] = '', debug_log_path: Optional[str] = '', errors_log_path: Optional[str] = '', json_log_path: Optional[str] = '') -> None:
    """
    Инициализирует логгеры для логирования в консоль и файлы (информация, отладка, ошибки и JSON).

    Args:
        info_log_path (Optional[str], optional): Путь к файлу логов информации (опционально). По умолчанию ''.
        debug_log_path (Optional[str], optional): Путь к файлу логов отладки (опционально). По умолчанию ''.
        errors_log_path (Optional[str], optional): Путь к файлу логов ошибок (опционально). По умолчанию ''.
        json_log_path (Optional[str], optional): Путь к файлу логов в формате JSON (опционально). По умолчанию ''.

    Raises:
        OSError: Если не удается создать файл лога.

    Example:
        >>> initialize_loggers(info_log_path='logs/info.log', debug_log_path='logs/debug.log')
    """
    ...
```

**Описание**: Инициализирует логгеры для логирования в консоль и файлы (информация, отладка, ошибки и JSON).

**Параметры**:
- `info_log_path` (Optional[str], optional): Путь к файлу логов информации (опционально).
- `debug_log_path` (Optional[str], optional): Путь к файлу логов отладки (опционально).
- `errors_log_path` (Optional[str], optional): Путь к файлу логов ошибок (опционально).
- `json_log_path` (Optional[str], optional): Путь к файлу логов в формате JSON (опционально).

### `log`

```python
def log(level: int, message: str, ex: Optional[Exception] = None, exc_info: bool = False, color: Optional[tuple[str, str]] = None) -> None:
    """
    Логирует сообщение на указанном уровне с возможным исключением и цветовым форматированием.

    Args:
        level (int): Уровень логирования (например, `logging.INFO`, `logging.DEBUG`).
        message (str): Логируемое сообщение.
        ex (Optional[Exception], optional): Исключение для логирования (опционально). По умолчанию `None`.
        exc_info (bool, optional): Включать информацию об исключении (значение по умолчанию — `False`).
        color (Optional[tuple[str, str]], optional): Кортеж цветов текста и фона для консольного вывода (опционально). По умолчанию `None`.

    Raises:
        ValueError: Если указан недопустимый уровень логирования.

    Example:
        >>> log(logging.INFO, 'Это информационное сообщение')
    """
    ...
```

**Описание**: Логирует сообщение на указанном уровне (например, `INFO`, `DEBUG`, `ERROR`) с возможным исключением и цветовым форматированием.

**Параметры**:
- `level` (int): Уровень логирования (например, `logging.INFO`, `logging.DEBUG`).
- `message` (str): Логируемое сообщение.
- `ex` (Optional[Exception], optional): Исключение для логирования (опционально).
- `exc_info` (bool, optional): Включать информацию об исключении (значение по умолчанию — `False`).
- `color` (Optional[tuple[str, str]], optional): Кортеж цветов текста и фона для консольного вывода (опционально).

## Параметры логгера

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

## Конфигурация для логирования в файл (`config`)

Для записи сообщений в файл можно указать пути в конфигурации.

```python
config = {
    'info_log_path': 'logs/info.log',
    'debug_log_path': 'logs/debug.log',
    'errors_log_path': 'logs/errors.log',
    'json_log_path': 'logs/log.json'
}
```

## Примеры использования

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

#### 2. Логирование сообщений:

```python
logger.info('Это информационное сообщение')
logger.success('Это сообщение об успешной операции')
logger.warning('Это предупреждение')
logger.debug('Это сообщение для отладки')
logger.error('Это сообщение об ошибке')
logger.critical('Это критическое сообщение')
```

#### 3. Настройка цветов:

```python
logger.info('Это сообщение будет зеленым', colors=(colorama.Fore.GREEN, colorama.Back.BLACK))
logger.error('Это сообщение с красным фоном', colors=(colorama.Fore.WHITE, colorama.Back.RED))