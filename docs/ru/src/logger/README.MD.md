# Документация модуля `src.logger`

## Обзор

Модуль `src.logger` предоставляет гибкую систему логирования, поддерживающую логирование в консоль, файлы и JSON. Он использует шаблон проектирования Singleton, чтобы гарантировать использование только одного экземпляра логгера во всем приложении. Логгер поддерживает различные уровни логирования (например, `INFO`, `ERROR`, `DEBUG`) и включает цветной вывод для консольных логов. Вы также можете настроить форматы вывода логов и управлять логированием в разные файлы.

## Подробней

Этот модуль обеспечивает централизованное и удобное управление логированием в проекте `hypotez`. Он позволяет записывать сообщения разных уровней важности в различные источники, такие как консоль, файлы и JSON. Использование паттерна Singleton гарантирует, что все компоненты приложения используют один и тот же экземпляр логгера, что упрощает настройку и управление логированием. Модуль также предоставляет возможность настройки цветов для консольного вывода, что делает логи более читаемыми и информативными.

## Классы

### `SingletonMeta`

**Описание**: Метакласс, реализующий шаблон проектирования Singleton для логгера.

**Как работает класс**:
Метакласс `SingletonMeta` используется для создания Singleton-классов. Он переопределяет метод `__call__`, чтобы гарантировать, что при создании экземпляра класса возвращается один и тот же экземпляр. Если экземпляр класса еще не создан, он создается и сохраняется в атрибуте `_instances` класса. При последующих вызовах возвращается сохраненный экземпляр.

### `JsonFormatter`

**Описание**: Пользовательский форматтер, выводящий логи в формате JSON.

**Как работает класс**:
Класс `JsonFormatter` наследуется от класса `logging.Formatter` и переопределяет метод `format`, чтобы форматировать записи логов в формате JSON. Он преобразует запись лога в словарь и использует модуль `json` для преобразования словаря в строку JSON. Это позволяет легко записывать логи в файлы JSON или отправлять их в системы агрегации логов, которые поддерживают формат JSON.

### `Logger`

**Описание**: Основной класс логгера, поддерживающий логирование в консоль, файлы и JSON.

**Как работает класс**:
Класс `Logger` является основным классом логгера в модуле. Он использует метакласс `SingletonMeta`, чтобы гарантировать, что существует только один экземпляр класса. Класс предоставляет методы для настройки и инициализации логгеров для консоли и файлов, а также методы для записи сообщений различных уровней важности. Логгер поддерживает цветной вывод в консоль и позволяет настраивать форматы вывода для файлов и JSON.

**Методы**:
- `__init__`: Инициализирует экземпляр Logger с заполнителями для различных типов логгеров (консоль, файл и JSON).
- `_configure_logger`: Настраивает и возвращает экземпляр логгера.
- `initialize_loggers`: Инициализирует логгеры для консоли и файлового логирования (info, debug, error и JSON).
- `log`: Записывает сообщение на указанном уровне (например, `INFO`, `DEBUG`, `ERROR`) с дополнительным исключением и форматированием цвета.
- `info`: Записывает информационное сообщение.
- `success`: Записывает сообщение об успехе.
- `warning`: Записывает предупреждающее сообщение.
- `debug`: Записывает отладочное сообщение.
- `error`: Записывает сообщение об ошибке.
- `critical`: Записывает критическое сообщение.

## Функции

### `__init__`

```python
def __init__(self) -> None:
    """
    Инициализирует экземпляр Logger с заполнителями для различных типов логгеров (консоль, файл и JSON).

    Args:
        None

    Returns:
        None

    Raises:
        None

    Example:
        >>> logger = Logger()
    """
```

**Как работает функция**:
Метод `__init__` является конструктором класса `Logger`. Он инициализирует атрибуты экземпляра класса, такие как `console_logger`, `info_file_logger`, `debug_file_logger`, `error_file_logger` и `json_file_logger`, значением `None`. Эти атрибуты будут использоваться для хранения экземпляров логгеров для консоли и файлов.

### `_configure_logger`

```python
def _configure_logger(
    name: str,
    log_path: str,
    level: Optional[int] = logging.DEBUG,
    formatter: Optional[logging.Formatter] = None,
    mode: Optional[str] = 'a'
) -> logging.Logger:
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

    Raises:
        None

    Example:
        >>> logger = Logger()
        >>> log = logger._configure_logger('test_logger', 'test.log')
    """
```

**Как работает функция**:
Метод `_configure_logger` создает и настраивает экземпляр логгера. Он принимает имя логгера, путь к файлу лога, уровень логирования, форматтер и режим файла в качестве аргументов. Метод создает экземпляр `logging.Logger` с указанным именем, создает обработчик файла (`logging.FileHandler`) с указанным путем и режимом, устанавливает уровень логирования и форматтер для обработчика и добавляет обработчик к логгеру.

**Параметры**:
- `name` (str): Имя логгера.
- `log_path` (str): Путь к файлу лога.
- `level` (Optional[int], optional): Уровень логирования, например, `logging.DEBUG`. По умолчанию `logging.DEBUG`.
- `formatter` (Optional[logging.Formatter], optional): Пользовательский форматтер (необязательно).
- `mode` (Optional[str], optional): Режим файла, например, `'a'` для добавления (по умолчанию).

**Возвращает**:
- `logging.Logger`: Настроенный экземпляр `logging.Logger`.

### `initialize_loggers`

```python
def initialize_loggers(
    info_log_path: Optional[str] = '',
    debug_log_path: Optional[str] = '',
    errors_log_path: Optional[str] = '',
    json_log_path: Optional[str] = ''
) -> None:
    """
    Инициализирует логгеры для консоли и файлового логирования (info, debug, error и JSON).

    Args:
        info_log_path (Optional[str], optional): Путь к файлу информационных логов (необязательно).
        debug_log_path (Optional[str], optional): Путь к файлу отладочных логов (необязательно).
        errors_log_path (Optional[str], optional): Путь к файлу логов ошибок (необязательно).
        json_log_path (Optional[str], optional): Путь к файлу JSON логов (необязательно).

    Returns:
        None

    Raises:
        None

    Example:
        >>> logger = Logger()
        >>> logger.initialize_loggers(info_log_path='info.log', debug_log_path='debug.log')
    """
```

**Как работает функция**:
Метод `initialize_loggers` инициализирует логгеры для консоли и файлов. Он принимает пути к файлам логов для информационных, отладочных логов, логов ошибок и JSON логов в качестве аргументов. Если путь к файлу лога указан, метод создает и настраивает файловый логгер с использованием метода `_configure_logger`. Если путь к файлу JSON лога указан, метод также создает и настраивает файловый логгер с использованием пользовательского форматтера `JsonFormatter`.

**Параметры**:
- `info_log_path` (Optional[str], optional): Путь к файлу информационных логов (необязательно).
- `debug_log_path` (Optional[str], optional): Путь к файлу отладочных логов (необязательно).
- `errors_log_path` (Optional[str], optional): Путь к файлу логов ошибок (необязательно).
- `json_log_path` (Optional[str], optional): Путь к файлу JSON логов (необязательно).

**Возвращает**:
- `None`

### `log`

```python
def log(self, level: int, message: str, ex: Optional[Exception] = None, exc_info: bool = False, color: Optional[tuple] = None) -> None:
    """
    Записывает сообщение на указанном уровне (например, `INFO`, `DEBUG`, `ERROR`) с дополнительным исключением и форматированием цвета.

    Args:
        level (int): Уровень логирования (например, `logging.INFO`, `logging.DEBUG`).
        message (str): Сообщение лога.
        ex (Optional[Exception], optional): Дополнительное исключение для логирования.
        exc_info (bool, optional): Следует ли включать информацию об исключении (по умолчанию `False`).
        color (Optional[tuple], optional): Кортеж с цветами текста и фона для вывода в консоль (необязательно).

    Returns:
        None

    Raises:
        None

    Example:
        >>> logger = Logger()
        >>> logger.log(logging.INFO, 'This is an info message')
    """
```

**Как работает функция**:
Метод `log` является основным методом для записи сообщений в лог. Он принимает уровень логирования, сообщение, исключение (если есть), флаг для включения информации об исключении и кортеж с цветами для консольного вывода в качестве аргументов. Метод записывает сообщение в консольный логгер, если он инициализирован. Если указано исключение, метод также записывает информацию об исключении. Если указаны цвета, метод применяет их к сообщению перед записью в консоль.

**Параметры**:
- `level` (int): Уровень логирования (например, `logging.INFO`, `logging.DEBUG`).
- `message` (str): Сообщение лога.
- `ex` (Optional[Exception], optional): Дополнительное исключение для логирования.
- `exc_info` (bool, optional): Следует ли включать информацию об исключении (по умолчанию `False`).
- `color` (Optional[tuple], optional): Кортеж с цветами текста и фона для вывода в консоль (необязательно).

**Возвращает**:
- `None`

### `info`

```python
def info(self, message: str, ex: Optional[Exception] = None, exc_info: bool = False, colors: Optional[tuple] = None) -> None:
    """
    Записывает информационное сообщение.

    Args:
        message (str): Информационное сообщение для логирования.
        ex (Optional[Exception], optional): Дополнительное исключение для логирования.
        exc_info (bool, optional): Следует ли включать информацию об исключении (по умолчанию `False`).
        colors (Optional[tuple], optional): Кортеж значений цвета для сообщения (необязательно).

    Returns:
        None

    Raises:
        None

    Example:
        >>> logger = Logger()
        >>> logger.info('This is an info message')
    """
```

**Как работает функция**:
Метод `info` записывает информационное сообщение в лог. Он вызывает метод `log` с уровнем логирования `logging.INFO` и переданными аргументами.

**Параметры**:
- `message` (str): Информационное сообщение для логирования.
- `ex` (Optional[Exception], optional): Дополнительное исключение для логирования.
- `exc_info` (bool, optional): Следует ли включать информацию об исключении (по умолчанию `False`).
- `colors` (Optional[tuple], optional): Кортеж значений цвета для сообщения (необязательно).

**Возвращает**:
- `None`

### `success`

```python
def success(self, message: str, ex: Optional[Exception] = None, exc_info: bool = False, colors: Optional[tuple] = None) -> None:
    """
    Записывает сообщение об успехе.

    Args:
        message (str): Сообщение об успехе для логирования.
        ex (Optional[Exception], optional): Дополнительное исключение для логирования.
        exc_info (bool, optional): Следует ли включать информацию об исключении (по умолчанию `False`).
        colors (Optional[tuple], optional): Кортеж значений цвета для сообщения (необязательно).

    Returns:
        None

    Raises:
        None

    Example:
        >>> logger = Logger()
        >>> logger.success('This is a success message')
    """
```

**Как работает функция**:
Метод `success` записывает сообщение об успехе в лог. Он вызывает метод `log` с уровнем логирования `logging.INFO` и переданными аргументами.

**Параметры**:
- `message` (str): Сообщение об успехе для логирования.
- `ex` (Optional[Exception], optional): Дополнительное исключение для логирования.
- `exc_info` (bool, optional): Следует ли включать информацию об исключении (по умолчанию `False`).
- `colors` (Optional[tuple], optional): Кортеж значений цвета для сообщения (необязательно).

**Возвращает**:
- `None`

### `warning`

```python
def warning(self, message: str, ex: Optional[Exception] = None, exc_info: bool = False, colors: Optional[tuple] = None) -> None:
    """
    Записывает предупреждающее сообщение.

    Args:
        message (str): Предупреждающее сообщение для логирования.
        ex (Optional[Exception], optional): Дополнительное исключение для логирования.
        exc_info (bool, optional): Следует ли включать информацию об исключении (по умолчанию `False`).
        colors (Optional[tuple], optional): Кортеж значений цвета для сообщения (необязательно).

    Returns:
        None

    Raises:
        None

    Example:
        >>> logger = Logger()
        >>> logger.warning('This is a warning message')
    """
```

**Как работает функция**:
Метод `warning` записывает предупреждающее сообщение в лог. Он вызывает метод `log` с уровнем логирования `logging.WARNING` и переданными аргументами.

**Параметры**:
- `message` (str): Предупреждающее сообщение для логирования.
- `ex` (Optional[Exception], optional): Дополнительное исключение для логирования.
- `exc_info` (bool, optional): Следует ли включать информацию об исключении (по умолчанию `False`).
- `colors` (Optional[tuple], optional): Кортеж значений цвета для сообщения (необязательно).

**Возвращает**:
- `None`

### `debug`

```python
def debug(self, message: str, ex: Optional[Exception] = None, exc_info: bool = True, colors: Optional[tuple] = None) -> None:
    """
    Записывает отладочное сообщение.

    Args:
        message (str): Отладочное сообщение для логирования.
        ex (Optional[Exception], optional): Дополнительное исключение для логирования.
        exc_info (bool, optional): Следует ли включать информацию об исключении (по умолчанию `True`).
        colors (Optional[tuple], optional): Кортеж значений цвета для сообщения (необязательно).

    Returns:
        None

    Raises:
        None

    Example:
        >>> logger = Logger()
        >>> logger.debug('This is a debug message')
    """
```

**Как работает функция**:
Метод `debug` записывает отладочное сообщение в лог. Он вызывает метод `log` с уровнем логирования `logging.DEBUG` и переданными аргументами.

**Параметры**:
- `message` (str): Отладочное сообщение для логирования.
- `ex` (Optional[Exception], optional): Дополнительное исключение для логирования.
- `exc_info` (bool, optional): Следует ли включать информацию об исключении (по умолчанию `True`).
- `colors` (Optional[tuple], optional): Кортеж значений цвета для сообщения (необязательно).

**Возвращает**:
- `None`

### `error`

```python
def error(self, message: str, ex: Optional[Exception] = None, exc_info: bool = True, colors: Optional[tuple] = None) -> None:
    """
    Записывает сообщение об ошибке.

    Args:
        message (str): Сообщение об ошибке для логирования.
        ex (Optional[Exception], optional): Дополнительное исключение для логирования.
        exc_info (bool, optional): Следует ли включать информацию об исключении (по умолчанию `True`).
        colors (Optional[tuple], optional): Кортеж значений цвета для сообщения (необязательно).

    Returns:
        None

    Raises:
        None

    Example:
        >>> logger = Logger()
        >>> logger.error('This is an error message')
    """
```

**Как работает функция**:
Метод `error` записывает сообщение об ошибке в лог. Он вызывает метод `log` с уровнем логирования `logging.ERROR` и переданными аргументами.

**Параметры**:
- `message` (str): Сообщение об ошибке для логирования.
- `ex` (Optional[Exception], optional): Дополнительное исключение для логирования.
- `exc_info` (bool, optional): Следует ли включать информацию об исключении (по умолчанию `True`).
- `colors` (Optional[tuple], optional): Кортеж значений цвета для сообщения (необязательно).

**Возвращает**:
- `None`

### `critical`

```python
def critical(self, message: str, ex: Optional[Exception] = None, exc_info: bool = True, colors: Optional[tuple] = None) -> None:
    """
    Записывает критическое сообщение.

    Args:
        message (str): Критическое сообщение для логирования.
        ex (Optional[Exception], optional): Дополнительное исключение для логирования.
        exc_info (bool, optional): Следует ли включать информацию об исключении (по умолчанию `True`).
        colors (Optional[tuple], optional): Кортеж значений цвета для сообщения (необязательно).

    Returns:
        None

    Raises:
        None

    Example:
        >>> logger = Logger()
        >>> logger.critical('This is a critical message')
    """
```

**Как работает функция**:
Метод `critical` записывает критическое сообщение в лог. Он вызывает метод `log` с уровнем логирования `logging.CRITICAL` и переданными аргументами.

**Параметры**:
- `message` (str): Критическое сообщение для логирования.
- `ex` (Optional[Exception], optional): Дополнительное исключение для логирования.
- `exc_info` (bool, optional): Следует ли включать информацию об исключении (по умолчанию `True`).
- `colors` (Optional[tuple], optional): Кортеж значений цвета для сообщения (необязательно).

**Возвращает**:
- `None`

## Параметры для Logger

Класс `Logger` принимает несколько дополнительных параметров для настройки поведения логирования.

- **Level**: Контролирует серьезность захватываемых логов. Общие уровни включают:
  - `logging.DEBUG`: Подробная информация, полезная для диагностики проблем.
  - `logging.INFO`: Общая информация, например, об успешных операциях.
  - `logging.WARNING`: Предупреждения, которые не обязательно требуют немедленных действий.
  - `logging.ERROR`: Сообщения об ошибках.
  - `logging.CRITICAL`: Критические ошибки, требующие немедленного внимания.

- **Formatter**: Определяет, как форматируются сообщения логов. По умолчанию сообщения форматируются как `'%(asctime)s - %(levelname)s - %(message)s'`. Вы можете предоставить пользовательский форматтер для разных форматов, например, JSON.

- **Color**: Цвета для сообщений логов в консоли. Цвета указываются как кортеж с двумя элементами:
  - **Text color**: Указывает цвет текста (например, `colorama.Fore.RED`).
  - **Background color**: Указывает цвет фона (например, `colorama.Back.WHITE`).

Цвет можно настроить для разных уровней логов (например, зеленый для info, красный для ошибок и т. д.).

## Конфигурация файлового логирования (`config`)

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

## Пример использования

#### 1. Инициализация Logger:

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
logger.info('This is an info message')
logger.success('This is a success message')
logger.warning('This is a warning message')
logger.debug('This is a debug message')
logger.error('This is an error message')
logger.critical('This is a critical message')
```

#### 3. Настройка цветов:

```python
logger.info('This message will be green', colors=(colorama.Fore.GREEN, colorama.Back.BLACK))
logger.error('This message will have a red background', colors=(colorama.Fore.WHITE, colorama.Back.RED))
```

Этот модуль предоставляет комплексную и гибкую систему логирования для Python-приложений. Вы можете настроить консольное и файловое логирование с различными форматами и цветами, управлять уровнями логирования и корректно обрабатывать исключения. Конфигурация для файлового логирования хранится в словаре `config`, что обеспечивает простую настройку.