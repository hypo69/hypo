# Документация для модуля `src.logger`

## Обзор

Модуль `src.logger` предоставляет гибкую систему логирования, поддерживающую логирование в консоль, файлы и в формате JSON. Он использует шаблон проектирования Singleton, чтобы обеспечить использование единственного экземпляра логгера во всем приложении. Логгер поддерживает различные уровни логирования (например, `INFO`, `ERROR`, `DEBUG`) и включает цветное отображение для вывода в консоль. Также доступны настройки форматов вывода и управление логированием в различные файлы.

## Подробнее

Модуль `src.logger` предназначен для централизованного управления логированием в приложении. Он позволяет записывать сообщения различных уровней важности (информация, отладка, предупреждения, ошибки, критические сообщения) в разные места назначения, такие как консоль, отдельные файлы или JSON-файлы. Использование шаблона Singleton гарантирует, что все компоненты приложения используют один и тот же экземпляр логгера, что упрощает управление и конфигурирование логирования.

## Классы

### `SingletonMeta`

**Описание**: Метакласс, реализующий шаблон Singleton для логгера.

**Как работает класс**:
Этот метакласс гарантирует, что при попытке создать экземпляр класса `Logger` будет возвращен уже существующий экземпляр, если он был создан ранее. Если экземпляр еще не существует, он будет создан и сохранен для последующего использования.

### `JsonFormatter`

**Описание**: Кастомный форматтер для вывода логов в формате JSON.

**Как работает класс**:
Этот класс используется для форматирования сообщений лога в формате JSON. Он преобразует запись лога в JSON-строку, что позволяет легко интегрировать логи в системы, требующие структурированные данные.

### `Logger`

**Описание**: Основной класс логгера, поддерживающий логирование в консоль, файлы и в формате JSON.

**Как работает класс**:
Класс `Logger` предоставляет методы для логирования сообщений различных уровней важности. Он позволяет настраивать, куда будут записываться логи (консоль, файлы) и в каком формате. Класс использует другие компоненты, такие как форматтеры и обработчики, для выполнения фактической записи логов.

**Методы**:
- `__init__`: Инициализирует экземпляр класса Logger с плейсхолдерами для различных типов логгеров (консоль, файлы и JSON).
- `_configure_logger`: Настраивает и возвращает экземпляр логгера.
- `initialize_loggers`: Инициализирует логгеры для логирования в консоль и файлы (информация, отладка, ошибки и JSON).
- `log`: Логирует сообщение на указанном уровне (например, `INFO`, `DEBUG`, `ERROR`) с возможным исключением и цветовым форматированием.
- `info`: Логирует информационное сообщение.
- `success`: Логирует сообщение об успешной операции.
- `warning`: Логирует предупреждение.
- `debug`: Логирует сообщение для отладки.
- `error`: Логирует сообщение об ошибке.
- `critical`: Логирует критическое сообщение.

**Параметры**:
- `name` (str): Имя логгера.
- `log_path` (str): Путь к файлу логов.
- `level` (Optional[int], optional): Уровень логирования, например, `logging.DEBUG`. Значение по умолчанию — `logging.DEBUG`.
- `formatter` (Optional[logging.Formatter], optional): Кастомный форматтер (опционально).
- `mode` (Optional[str], optional): Режим работы с файлом, например, `'a'` для добавления (значение по умолчанию).
- `info_log_path` (Optional[str], optional): Путь к файлу логов информации (опционально).
- `debug_log_path` (Optional[str], optional): Путь к файлу логов отладки (опционально).
- `errors_log_path` (Optional[str], optional): Путь к файлу логов ошибок (опционально).
- `json_log_path` (Optional[str], optional): Путь к файлу логов в формате JSON (опционально).
- `level` (int): Уровень логирования (например, `logging.INFO`, `logging.DEBUG`).
- `message` (str): Логируемое сообщение.
- `ex` (Exception, optional): Исключение для логирования (опционально).
- `exc_info` (bool, optional): Включать информацию об исключении (значение по умолчанию — `False`).
- `color` (Tuple[str, str], optional): Кортеж цветов текста и фона для консольного вывода (опционально).

**Примеры**:
```python
logger: Logger = Logger()
config = {
    'info_log_path': 'logs/info.log',
    'debug_log_path': 'logs/debug.log',
    'errors_log_path': 'logs/errors.log',
    'json_log_path': 'logs/log.json'
}
logger.initialize_loggers(**config)

logger.info('Это информационное сообщение')
logger.success('Это сообщение об успешной операции')
logger.warning('Это предупреждение')
logger.debug('Это сообщение для отладки')
logger.error('Это сообщение об ошибке')
logger.critical('Это критическое сообщение')

logger.info('Это сообщение будет зеленым', colors=(colorama.Fore.GREEN, colorama.Back.BLACK))
logger.error('Это сообщение с красным фоном', colors=(colorama.Fore.WHITE, colorama.Back.RED))
```

## Функции

### `__init__`

```python
def __init__(self):
    """
    Инициализирует экземпляр класса Logger с плейсхолдерами для различных типов логгеров (консоль, файлы и JSON).
    
    Args:
        self (Logger): Экземпляр класса Logger.

    Returns:
        None
        
    Example:
        >>> logger = Logger()
    """
```

**Как работает функция**:
Функция `__init__` является конструктором класса `Logger`. Она инициализирует атрибуты класса, устанавливая значения `None` для логгеров консоли, файлов и JSON. Это подготавливает класс к дальнейшей настройке логгеров с использованием метода `initialize_loggers`.

**Параметры**:
- `self`: Ссылка на экземпляр класса `Logger`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- Отсутствуют

**Примеры**:
```python
logger: Logger = Logger()
```

### `_configure_logger`

```python
def _configure_logger(name: str, log_path: str, level: Optional[int] = logging.DEBUG, formatter: Optional[logging.Formatter] = None, mode: Optional[str] = 'a') -> logging.Logger:
    """
    Настраивает и возвращает экземпляр логгера.
    
    Args:
        name (str): Имя логгера.
        log_path (str): Путь к файлу логов.
        level (Optional[int], optional): Уровень логирования, например, `logging.DEBUG`. Значение по умолчанию — `logging.DEBUG`.
        formatter (Optional[logging.Formatter], optional): Кастомный форматтер (опционально).
        mode (Optional[str], optional): Режим работы с файлом, например, `'a'` для добавления (значение по умолчанию).

    Returns:
        logging.Logger: Настроенный экземпляр `logging.Logger`.
        
    Example:
        >>> logger = Logger()
        >>> configured_logger = logger._configure_logger('info', 'logs/info.log')
    """
```

**Как работает функция**:
Функция `_configure_logger` создает и настраивает экземпляр логгера (`logging.Logger`). Она устанавливает уровень логирования, форматтер и обработчик (handler) для логгера. Если указан путь к файлу, она добавляет обработчик файла. Если указан форматтер, он устанавливается для обработчика. Функция возвращает настроенный экземпляр логгера.

**Параметры**:
- `name` (str): Имя логгера.
- `log_path` (str): Путь к файлу логов.
- `level` (Optional[int], optional): Уровень логирования, например, `logging.DEBUG`. Значение по умолчанию — `logging.DEBUG`.
- `formatter` (Optional[logging.Formatter], optional): Кастомный форматтер (опционально).
- `mode` (Optional[str], optional): Режим работы с файлом, например, `'a'` для добавления (значение по умолчанию).

**Возвращает**:
- `logging.Logger`: Настроенный экземпляр `logging.Logger`.

**Вызывает исключения**:
- Отсутствуют

**Примеры**:
```python
logger = Logger()
configured_logger = logger._configure_logger('info', 'logs/info.log')
```

### `initialize_loggers`

```python
def initialize_loggers(info_log_path: Optional[str] = '', debug_log_path: Optional[str] = '', errors_log_path: Optional[str] = '', json_log_path: Optional[str] = ''):
    """
    Инициализирует логгеры для логирования в консоль и файлы (информация, отладка, ошибки и JSON).
    
    Args:
        info_log_path (Optional[str], optional): Путь к файлу логов информации (опционально).
        debug_log_path (Optional[str], optional): Путь к файлу логов отладки (опционально).
        errors_log_path (Optional[str], optional): Путь к файлу логов ошибок (опционально).
        json_log_path (Optional[str], optional): Путь к файлу логов в формате JSON (опционально).

    Returns:
        None
        
    Example:
        >>> logger = Logger()
        >>> config = {
        ...    'info_log_path': 'logs/info.log',
        ...    'debug_log_path': 'logs/debug.log',
        ...    'errors_log_path': 'logs/errors.log',
        ...    'json_log_path': 'logs/log.json'
        ... }
        >>> logger.initialize_loggers(**config)
    """
```

**Как работает функция**:
Функция `initialize_loggers` инициализирует различные логгеры для записи информации, отладочных сообщений, ошибок и JSON-логирования. Она настраивает логгеры для записи в файлы, если указаны соответствующие пути. Также настраивается логгер для вывода в консоль.

**Параметры**:
- `info_log_path` (Optional[str], optional): Путь к файлу логов информации (опционально).
- `debug_log_path` (Optional[str], optional): Путь к файлу логов отладки (опционально).
- `errors_log_path` (Optional[str], optional): Путь к файлу логов ошибок (опционально).
- `json_log_path` (Optional[str], optional): Путь к файлу логов в формате JSON (опционально).

**Возвращает**:
- `None`

**Вызывает исключения**:
- Отсутствуют

**Примеры**:
```python
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
def log(self, level: int, message: str, ex: Exception = None, exc_info: bool = False, color: tuple[str, str] | None = None):
    """
    Логирует сообщение на указанном уровне (например, `INFO`, `DEBUG`, `ERROR`) с возможным исключением и цветовым форматированием.
    
    Args:
        level (int): Уровень логирования (например, `logging.INFO`, `logging.DEBUG`).
        message (str): Логируемое сообщение.
        ex (Exception, optional): Исключение для логирования (опционально).
        exc_info (bool, optional): Включать информацию об исключении (значение по умолчанию — `False`).
        color (tuple[str, str] | None, optional): Кортеж цветов текста и фона для консольного вывода (опционально).

    Returns:
        None
    
    Example:
        >>> import logging
        >>> from colorama import Fore, Back
        >>> logger = Logger()
        >>> config = {
        ...    'info_log_path': 'logs/info.log',
        ...    'debug_log_path': 'logs/debug.log',
        ...    'errors_log_path': 'logs/errors.log',
        ...    'json_log_path': 'logs/log.json'
        ... }
        >>> logger.initialize_loggers(**config)
        >>> logger.log(logging.INFO, 'Это информационное сообщение')
        >>> logger.log(logging.ERROR, 'Это сообщение об ошибке', Exception('Test error'), exc_info=True)
        >>> logger.log(logging.INFO, 'Это сообщение будет зеленым', color=(Fore.GREEN, Back.BLACK))
    """
```

**Как работает функция**:
Функция `log` выполняет фактическую запись сообщения в лог. Она определяет, какой логгер использовать (консольный, файловый или JSON) на основе уровня логирования. Если указано исключение, оно также записывается в лог. Если включена опция `exc_info`, в лог добавляется информация о трассировке стека. Для консольного вывода можно указать цвета текста и фона.

**Параметры**:
- `level` (int): Уровень логирования (например, `logging.INFO`, `logging.DEBUG`).
- `message` (str): Логируемое сообщение.
- `ex` (Exception, optional): Исключение для логирования (опционально).
- `exc_info` (bool, optional): Включать информацию об исключении (значение по умолчанию — `False`).
- `color` (tuple[str, str] | None, optional): Кортеж цветов текста и фона для консольного вывода (опционально).

**Возвращает**:
- `None`

**Вызывает исключения**:
- Отсутствуют

**Примеры**:
```python
import logging
from colorama import Fore, Back

logger = Logger()
config = {
    'info_log_path': 'logs/info.log',
    'debug_log_path': 'logs/debug.log',
    'errors_log_path': 'logs/errors.log',
    'json_log_path': 'logs/log.json'
}
logger.initialize_loggers(**config)

logger.log(logging.INFO, 'Это информационное сообщение')
logger.log(logging.ERROR, 'Это сообщение об ошибке', Exception('Test error'), exc_info=True)
logger.log(logging.INFO, 'Это сообщение будет зеленым', color=(Fore.GREEN, Back.BLACK))
```

### `info`

```python
def info(self, message: str, colors: tuple[str, str] | None = None):
    """
    Логирует информационное сообщение.
    
    Args:
        message (str): Логируемое сообщение.
        colors (tuple[str, str] | None, optional): Кортеж цветов текста и фона для консольного вывода (опционально).

    Returns:
        None
        
    Example:
        >>> logger = Logger()
        >>> config = {
        ...    'info_log_path': 'logs/info.log',
        ...    'debug_log_path': 'logs/debug.log',
        ...    'errors_log_path': 'logs/errors.log',
        ...    'json_log_path': 'logs/log.json'
        ... }
        >>> logger.initialize_loggers(**config)
        >>> logger.info('Это информационное сообщение')
    """
```

**Как работает функция**:
Функция `info` логирует сообщение с уровнем `INFO`. Она вызывает метод `log` с уровнем `logging.INFO` и переданным сообщением.

**Параметры**:
- `message` (str): Логируемое сообщение.
- `colors` (tuple[str, str] | None, optional): Кортеж цветов текста и фона для консольного вывода (опционально).

**Возвращает**:
- `None`

**Вызывает исключения**:
- Отсутствуют

**Примеры**:
```python
logger = Logger()
config = {
    'info_log_path': 'logs/info.log',
    'debug_log_path': 'logs/debug.log',
    'errors_log_path': 'logs/errors.log',
    'json_log_path': 'logs/log.json'
}
logger.initialize_loggers(**config)
logger.info('Это информационное сообщение')
```

### `success`

```python
def success(self, message: str, colors: tuple[str, str] | None = None):
    """
    Логирует сообщение об успешной операции.
    
    Args:
        message (str): Логируемое сообщение.
        colors (tuple[str, str] | None, optional): Кортеж цветов текста и фона для консольного вывода (опционально).

    Returns:
        None
        
    Example:
        >>> logger = Logger()
        >>> config = {
        ...    'info_log_path': 'logs/info.log',
        ...    'debug_log_path': 'logs/debug.log',
        ...    'errors_log_path': 'logs/errors.log',
        ...    'json_log_path': 'logs/log.json'
        ... }
        >>> logger.initialize_loggers(**config)
        >>> logger.success('Операция успешно завершена')
    """
```

**Как работает функция**:
Функция `success` логирует сообщение об успешной операции. Она вызывает метод `log` с уровнем `SUCCESS` и переданным сообщением.

**Параметры**:
- `message` (str): Логируемое сообщение.
- `colors` (tuple[str, str] | None, optional): Кортеж цветов текста и фона для консольного вывода (опционально).

**Возвращает**:
- `None`

**Вызывает исключения**:
- Отсутствуют

**Примеры**:
```python
logger = Logger()
config = {
    'info_log_path': 'logs/info.log',
    'debug_log_path': 'logs/debug.log',
    'errors_log_path': 'logs/errors.log',
    'json_log_path': 'logs/log.json'
}
logger.initialize_loggers(**config)
logger.success('Операция успешно завершена')
```

### `warning`

```python
def warning(self, message: str, colors: tuple[str, str] | None = None):
    """
    Логирует предупреждение.
    
    Args:
        message (str): Логируемое сообщение.
        colors (tuple[str, str] | None, optional): Кортеж цветов текста и фона для консольного вывода (опционально).

    Returns:
        None
        
    Example:
        >>> logger = Logger()
        >>> config = {
        ...    'info_log_path': 'logs/info.log',
        ...    'debug_log_path': 'logs/debug.log',
        ...    'errors_log_path': 'logs/errors.log',
        ...    'json_log_path': 'logs/log.json'
        ... }
        >>> logger.initialize_loggers(**config)
        >>> logger.warning('Внимание: ресурс может быть недоступен')
    """
```

**Как работает функция**:
Функция `warning` логирует предупреждение. Она вызывает метод `log` с уровнем `logging.WARNING` и переданным сообщением.

**Параметры**:
- `message` (str): Логируемое сообщение.
- `colors` (tuple[str, str] | None, optional): Кортеж цветов текста и фона для консольного вывода (опционально).

**Возвращает**:
- `None`

**Вызывает исключения**:
- Отсутствуют

**Примеры**:
```python
logger = Logger()
config = {
    'info_log_path': 'logs/info.log',
    'debug_log_path': 'logs/debug.log',
    'errors_log_path': 'logs/errors.log',
    'json_log_path': 'logs/log.json'
}
logger.initialize_loggers(**config)
logger.warning('Внимание: ресурс может быть недоступен')
```

### `debug`

```python
def debug(self, message: str, colors: tuple[str, str] | None = None):
    """
    Логирует сообщение для отладки.
    
    Args:
        message (str): Логируемое сообщение.
        colors (tuple[str, str] | None, optional): Кортеж цветов текста и фона для консольного вывода (опционально).

    Returns:
        None
        
    Example:
        >>> logger = Logger()
        >>> config = {
        ...    'info_log_path': 'logs/info.log',
        ...    'debug_log_path': 'logs/debug.log',
        ...    'errors_log_path': 'logs/errors.log',
        ...    'json_log_path': 'logs/log.json'
        ... }
        >>> logger.initialize_loggers(**config)
        >>> logger.debug('Отладочное сообщение: значение переменной x = 5')
    """
```

**Как работает функция**:
Функция `debug` логирует сообщение для отладки. Она вызывает метод `log` с уровнем `logging.DEBUG` и переданным сообщением.

**Параметры**:
- `message` (str): Логируемое сообщение.
- `colors` (tuple[str, str] | None, optional): Кортеж цветов текста и фона для консольного вывода (опционально).

**Возвращает**:
- `None`

**Вызывает исключения**:
- Отсутствуют

**Примеры**:
```python
logger = Logger()
config = {
    'info_log_path': 'logs/info.log',
    'debug_log_path': 'logs/debug.log',
    'errors_log_path': 'logs/errors.log',
    'json_log_path': 'logs/log.json'
}
logger.initialize_loggers(**config)
logger.debug('Отладочное сообщение: значение переменной x = 5')
```

### `error`

```python
def error(self, message: str, ex: Exception = None, exc_info: bool = False, colors: tuple[str, str] | None = None):
    """
    Логирует сообщение об ошибке.
    
    Args:
        message (str): Логируемое сообщение.
        ex (Exception, optional): Исключение для логирования (опционально).
        exc_info (bool, optional): Включать информацию об исключении (значение по умолчанию — `False`).
        colors (tuple[str, str] | None, optional): Кортеж цветов текста и фона для консольного вывода (опционально).

    Returns:
        None
        
    Example:
        >>> logger = Logger()
        >>> config = {
        ...    'info_log_path': 'logs/info.log',
        ...    'debug_log_path': 'logs/debug.log',
        ...    'errors_log_path': 'logs/errors.log',
        ...    'json_log_path': 'logs/log.json'
        ... }
        >>> logger.initialize_loggers(**config)
        >>> logger.error('Произошла ошибка при выполнении операции', Exception('Test error'), exc_info=True)
    """
```

**Как работает функция**:
Функция `error` логирует сообщение об ошибке. Она вызывает метод `log` с уровнем `logging.ERROR` и переданным сообщением, исключением и информацией об исключении.

**Параметры**:
- `message` (str): Логируемое сообщение.
- `ex` (Exception, optional): Исключение для логирования (опционально).
- `exc_info` (bool, optional): Включать информацию об исключении (значение по умолчанию — `False`).
- `colors` (tuple[str, str] | None, optional): Кортеж цветов текста и фона для консольного вывода (опционально).

**Возвращает**:
- `None`

**Вызывает исключения**:
- Отсутствуют

**Примеры**:
```python
logger = Logger()
config = {
    'info_log_path': 'logs/info.log',
    'debug_log_path': 'logs/debug.log',
    'errors_log_path': 'logs/errors.log',
    'json_log_path': 'logs/log.json'
}
logger.initialize_loggers(**config)
logger.error('Произошла ошибка при выполнении операции', Exception('Test error'), exc_info=True)
```

### `critical`

```python
def critical(self, message: str, ex: Exception = None, exc_info: bool = False, colors: tuple[str, str] | None = None):
    """
    Логирует критическое сообщение.
    
    Args:
        message (str): Логируемое сообщение.
        ex (Exception, optional): Исключение для логирования (опционально).
        exc_info (bool, optional): Включать информацию об исключении (значение по умолчанию — `False`).
        colors (tuple[str, str] | None, optional): Кортеж цветов текста и фона для консольного вывода (опционально).

    Returns:
        None
        
    Example:
        >>> logger = Logger()
        >>> config = {
        ...    'info_log_path': 'logs/info.log',
        ...    'debug_log_path': 'logs/debug.log',
        ...    'errors_log_path': 'logs/errors.log',
        ...    'json_log_path': 'logs/log.json'
        ... }
        >>> logger.initialize_loggers(**config)
        >>> logger.critical('Критическая ошибка: приложение будет завершено', Exception('Critical error'), exc_info=True)
    """
```

**Как работает функция**:
Функция `critical` логирует критическое сообщение. Она вызывает метод `log` с уровнем `logging.CRITICAL` и переданным сообщением, исключением и информацией об исключении.

**Параметры**:
- `message` (str): Логируемое сообщение.
- `ex` (Exception, optional): Исключение для логирования (опционально).
- `exc_info` (bool, optional): Включать информацию об исключении (значение по умолчанию — `False`).
- `colors` (tuple[str, str] | None, optional): Кортеж цветов текста и фона для консольного вывода (опционально).

**Возвращает**:
- `None`

**Вызывает исключения**:
- Отсутствуют

**Примеры**:
```python
logger = Logger()
config = {
    'info_log_path': 'logs/info.log',
    'debug_log_path': 'logs/debug.log',
    'errors_log_path': 'logs/errors.log',
    'json_log_path': 'logs/log.json'
}
logger.initialize_loggers(**config)
logger.critical('Критическая ошибка: приложение будет завершено', Exception('Critical error'), exc_info=True)
```

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
```

Модуль `src.logger` предоставляет полноценную систему логирования для Python-приложений. Вы можете настроить логирование в консоль и файлы с различными форматами и цветами, управлять уровнями логирования и обрабатывать исключения. Конфигурация логирования в файлы задается через словарь `config`, что позволяет легко изменять настройки.