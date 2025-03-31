# Модуль логирования

## Обзор

Модуль `src.logger.logger` предоставляет функциональность для логирования сообщений различных уровней (INFO, DEBUG, ERROR, WARNING, CRITICAL) в консоль и файлы. Он использует паттерн Singleton для обеспечения единственного экземпляра логгера в приложении. Модуль также поддерживает цветное логирование в консоли и логирование в формате JSON.

## Подробнее

Этот модуль предназначен для централизованного управления логированием в проекте. Он позволяет записывать логи в файлы разных уровней детализации (info, debug, errors) и в формате JSON для удобного анализа. Использование цветного вывода в консоль помогает визуально различать сообщения разного уровня важности. Реализация Singleton гарантирует, что все части приложения используют один и тот же экземпляр логгера.

## Классы

### `SingletonMeta`

**Описание**: Метакласс, реализующий паттерн Singleton.

**Методы**:
- `__call__(cls, *args, **kwargs)`: Обеспечивает создание только одного экземпляра класса.

### `JsonFormatter`

**Описание**: Пользовательский форматер для логирования в формате JSON.

**Методы**:
- `format(self, record)`: Форматирует запись лога в JSON.

### `Logger`

**Описание**: Класс логгера, реализующий паттерн Singleton с возможностью логирования в консоль, файлы и JSON.

**Методы**:
- `__init__(self, info_log_path: Optional[str] = None, debug_log_path: Optional[str] = None, errors_log_path: Optional[str] = None, json_log_path: Optional[str] = None)`: Инициализирует экземпляр логгера.
- `_format_message(self, message, ex=None, color: Optional[Tuple[str, str]] = None, level=None)`: Форматирует сообщение с учетом уровня логирования, цвета и информации об исключении.
- `_ex_full_info(self, ex)`: Возвращает полную информацию об исключении, включая имя файла, имя функции и номер строки.
- `log(self, level, message, ex=None, exc_info=False, color: Optional[Tuple[str, str]] = None)`: Общий метод для логирования сообщений на указанном уровне.
- `info(self, message, ex=None, exc_info=False, text_color: str = "green", bg_color: str = "")`: Логирует информационное сообщение.
- `success(self, message, ex=None, exc_info=False, text_color: str = "yellow", bg_color: str = "")`: Логирует сообщение об успехе.
- `warning(self, message, ex=None, exc_info=False, text_color: str = "light_red", bg_color: str = "")`: Логирует предупреждающее сообщение.
- `debug(self, message, ex=None, exc_info=True, text_color: str = "cyan", bg_color: str = "")`: Логирует отладочное сообщение.
- `exception(self, message, ex=None, exc_info=True, text_color: str = "cyan", bg_color: str = "light_gray")`: Логирует сообщение об исключении.
- `error(self, message, ex=None, exc_info=True, text_color: str = "red", bg_color: str = "")`: Логирует сообщение об ошибке.
- `critical(self, message, ex=None, exc_info=True, text_color: str = "red", bg_color: str = "white")`: Логирует критическое сообщение.

## Функции

### `__init__`

```python
def __init__(
        self,
        info_log_path: Optional[str] = None,
        debug_log_path: Optional[str] = None,
        errors_log_path: Optional[str] = None,
        json_log_path: Optional[str] = None,
    ):
    """Initialize the Logger instance."""
    ...
```

**Описание**: Инициализирует экземпляр класса `Logger`.

**Параметры**:
- `info_log_path` (Optional[str], optional): Путь к файлу для информационных логов. По умолчанию `None`.
- `debug_log_path` (Optional[str], optional): Путь к файлу для отладочных логов. По умолчанию `None`.
- `errors_log_path` (Optional[str], optional): Путь к файлу для логов ошибок. По умолчанию `None`.
- `json_log_path` (Optional[str], optional): Путь к файлу для JSON-логов. По умолчанию `None`.

**Примеры**:

```python
from src.logger.logger import Logger

logger = Logger(info_log_path='info.log', debug_log_path='debug.log')
logger.info('Сообщение INFO')
```

### `_format_message`

```python
 def _format_message(self, message, ex=None, color: Optional[Tuple[str, str]] = None, level=None):
    """Returns formatted message with optional color and exception information."""
    ...
```

**Описание**: Форматирует сообщение лога с учетом уровня, цвета и информации об исключении.

**Параметры**:
- `message` (str): Сообщение для логирования.
- `ex` (Exception, optional): Объект исключения. По умолчанию `None`.
- `color` (Optional[Tuple[str, str]], optional): Кортеж с цветами текста и фона. По умолчанию `None`.
- `level` (int, optional): Уровень логирования. По умолчанию `None`.

**Возвращает**:
- `str`: Отформатированное сообщение.

**Примеры**:

```python
from src.logger.logger import Logger
import logging

logger = Logger()
formatted_message = logger._format_message('Test message', level=logging.INFO)
print(formatted_message)
```

### `_ex_full_info`

```python
 def _ex_full_info(self, ex):
    """Returns full exception information along with the previous function, file, and line details."""
    ...
```

**Описание**: Возвращает полную информацию об исключении, включая имя файла, имя функции и номер строки, где произошло исключение.

**Параметры**:
- `ex` (Exception): Объект исключения.

**Возвращает**:
- `str`: Полная информация об исключении.

**Примеры**:

```python
from src.logger.logger import Logger

logger = Logger()
try:
    raise ValueError('Test exception')
except ValueError as ex:
    full_info = logger._ex_full_info(ex)
    print(full_info)
```

### `log`

```python
 def log(self, level, message, ex=None, exc_info=False, color: Optional[Tuple[str, str]] = None):
    """General method to log messages at specified level with optional color."""
    ...
```

**Описание**: Общий метод для логирования сообщений на указанном уровне.

**Параметры**:
- `level` (int): Уровень логирования (например, `logging.INFO`, `logging.ERROR`).
- `message` (str): Сообщение для логирования.
- `ex` (Exception, optional): Объект исключения. По умолчанию `None`.
- `exc_info` (bool, optional): Флаг, указывающий, нужно ли включать информацию об исключении в лог. По умолчанию `False`.
- `color` (Optional[Tuple[str, str]], optional): Кортеж с цветами текста и фона. По умолчанию `None`.

**Примеры**:

```python
from src.logger.logger import Logger
import logging

logger = Logger()
logger.log(logging.INFO, 'Test message', exc_info=True)
```

### `info`

```python
def info(self, message, ex=None, exc_info=False, text_color: str = "green", bg_color: str = ""):
    """Logs an info message with optional text and background colors."""
    ...
```

**Описание**: Логирует информационное сообщение с возможностью указания цвета текста и фона.

**Параметры**:
- `message` (str): Сообщение для логирования.
- `ex` (Exception, optional): Объект исключения. По умолчанию `None`.
- `exc_info` (bool, optional): Флаг, указывающий, нужно ли включать информацию об исключении в лог. По умолчанию `False`.
- `text_color` (str, optional): Цвет текста. По умолчанию `"green"`.
- `bg_color` (str, optional): Цвет фона. По умолчанию `""`.

**Примеры**:

```python
from src.logger.logger import Logger

logger = Logger()
logger.info('Test info message')
```

### `success`

```python
def success(self, message, ex=None, exc_info=False, text_color: str = "yellow", bg_color: str = ""):
    """Logs a success message with optional text and background colors."""
    ...
```

**Описание**: Логирует сообщение об успехе с возможностью указания цвета текста и фона.

**Параметры**:
- `message` (str): Сообщение для логирования.
- `ex` (Exception, optional): Объект исключения. По умолчанию `None`.
- `exc_info` (bool, optional): Флаг, указывающий, нужно ли включать информацию об исключении в лог. По умолчанию `False`.
- `text_color` (str, optional): Цвет текста. По умолчанию `"yellow"`.
- `bg_color` (str, optional): Цвет фона. По умолчанию `""`.

**Примеры**:

```python
from src.logger.logger import Logger

logger = Logger()
logger.success('Test success message')
```

### `warning`

```python
def warning(self, message, ex=None, exc_info=False, text_color: str = "light_red", bg_color: str = ""):
    """Logs a warning message with optional text and background colors."""
    ...
```

**Описание**: Логирует предупреждающее сообщение с возможностью указания цвета текста и фона.

**Параметры**:
- `message` (str): Сообщение для логирования.
- `ex` (Exception, optional): Объект исключения. По умолчанию `None`.
- `exc_info` (bool, optional): Флаг, указывающий, нужно ли включать информацию об исключении в лог. По умолчанию `False`.
- `text_color` (str, optional): Цвет текста. По умолчанию `"light_red"`.
- `bg_color` (str, optional): Цвет фона. По умолчанию `""`.

**Примеры**:

```python
from src.logger.logger import Logger

logger = Logger()
logger.warning('Test warning message')
```

### `debug`

```python
def debug(self, message, ex=None, exc_info=True, text_color: str = "cyan", bg_color: str = ""):
    """Logs a debug message with optional text and background colors."""
    ...
```

**Описание**: Логирует отладочное сообщение с возможностью указания цвета текста и фона.

**Параметры**:
- `message` (str): Сообщение для логирования.
- `ex` (Exception, optional): Объект исключения. По умолчанию `None`.
- `exc_info` (bool, optional): Флаг, указывающий, нужно ли включать информацию об исключении в лог. По умолчанию `True`.
- `text_color` (str, optional): Цвет текста. По умолчанию `"cyan"`.
- `bg_color` (str, optional): Цвет фона. По умолчанию `""`.

**Примеры**:

```python
from src.logger.logger import Logger

logger = Logger()
logger.debug('Test debug message')
```

### `exception`

```python
def exception(self, message, ex=None, exc_info=True, text_color: str = "cyan", bg_color: str = "light_gray"):
    """Logs an exception message with optional text and background colors."""
    ...
```

**Описание**: Логирует сообщение об исключении с возможностью указания цвета текста и фона.

**Параметры**:
- `message` (str): Сообщение для логирования.
- `ex` (Exception, optional): Объект исключения. По умолчанию `None`.
- `exc_info` (bool, optional): Флаг, указывающий, нужно ли включать информацию об исключении в лог. По умолчанию `True`.
- `text_color` (str, optional): Цвет текста. По умолчанию `"cyan"`.
- `bg_color` (str, optional): Цвет фона. По умолчанию `"light_gray"`.

**Примеры**:

```python
from src.logger.logger import Logger

logger = Logger()
try:
    raise ValueError('Test exception')
except ValueError as ex:
    logger.exception('Test exception message', ex=ex)
```

### `error`

```python
def error(self, message, ex=None, exc_info=True, text_color: str = "red", bg_color: str = ""):
    """Logs an error message with optional text and background colors."""
    ...
```

**Описание**: Логирует сообщение об ошибке с возможностью указания цвета текста и фона.

**Параметры**:
- `message` (str): Сообщение для логирования.
- `ex` (Exception, optional): Объект исключения. По умолчанию `None`.
- `exc_info` (bool, optional): Флаг, указывающий, нужно ли включать информацию об исключении в лог. По умолчанию `True`.
- `text_color` (str, optional): Цвет текста. По умолчанию `"red"`.
- `bg_color` (str, optional): Цвет фона. По умолчанию `""`.

**Примеры**:

```python
from src.logger.logger import Logger

logger = Logger()
logger.error('Test error message')
```

### `critical`

```python
def critical(self, message, ex=None, exc_info=True, text_color: str = "red", bg_color: str = "white"):
    """Logs a critical message with optional text and background colors."""
    ...
```

**Описание**: Логирует критическое сообщение с возможностью указания цвета текста и фона.

**Параметры**:
- `message` (str): Сообщение для логирования.
- `ex` (Exception, optional): Объект исключения. По умолчанию `None`.
- `exc_info` (bool, optional): Флаг, указывающий, нужно ли включать информацию об исключении в лог. По умолчанию `True`.
- `text_color` (str, optional): Цвет текста. По умолчанию `"red"`.
- `bg_color` (str, optional): Цвет фона. По умолчанию `"white"`.

**Примеры**:

```python
from src.logger.logger import Logger

logger = Logger()
logger.critical('Test critical message')