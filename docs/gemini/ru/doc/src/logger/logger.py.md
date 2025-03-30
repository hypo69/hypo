# Модуль logger

## Обзор

Модуль `logger` предназначен для реализации гибкой системы логирования в проекте `hypotez`. Он предоставляет класс `Logger`, использующий паттерн Singleton, для обеспечения единственного экземпляра логгера во всем приложении. Модуль поддерживает логирование в консоль, файлы (info, debug, errors) и в JSON-формате.

## Подробней

Этот модуль предназначен для централизованного и стандартизированного логирования событий, происходящих в приложении `hypotez`. Он позволяет записывать информацию, отладочные сообщения, предупреждения, ошибки и критические ситуации в различные источники, такие как консоль и файлы. Использование паттерна Singleton гарантирует, что все компоненты приложения используют один и тот же экземпляр логгера, что упрощает управление и конфигурирование логирования. Логи записываются с указанием уровня важности, времени и, при необходимости, дополнительной информацией об исключениях. Это помогает разработчикам отслеживать работу приложения, выявлять и устранять ошибки.

## Классы

### `SingletonMeta`

**Описание**: Метакласс для реализации паттерна Singleton.

**Методы**:
- `__call__(cls, *args, **kwargs)`: Обеспечивает создание только одного экземпляра класса.

### `JsonFormatter`

**Описание**: Пользовательский форматтер для логирования в формате JSON.

**Методы**:
- `format(self, record)`: Форматирует запись лога как JSON.

### `Logger`

**Описание**: Класс логгера, реализующий паттерн Singleton с возможностью логирования в консоль, файлы и JSON.

**Методы**:
- `__init__(self, info_log_path: Optional[str] = None, debug_log_path: Optional[str] = None, errors_log_path: Optional[str] = None, json_log_path: Optional[str] = None)`: Инициализирует экземпляр логгера.
- `_format_message(self, message, ex=None, color: Optional[Tuple[str, str]] = None, level=None)`: Форматирует сообщение с учетом цвета и информации об исключении.
- `_ex_full_info(self, ex)`: Возвращает полную информацию об исключении, включая имя файла, функции и номер строки.
- `log(self, level, message, ex=None, exc_info=False, color: Optional[Tuple[str, str]] = None)`: Общий метод для логирования сообщений на указанном уровне с возможностью добавления цвета.
- `info(self, message, ex=None, exc_info=False, text_color: str = "green", bg_color: str = "")`: Логирует информационное сообщение с опциональными цветами текста и фона.
- `success(self, message, ex=None, exc_info=False, text_color: str = "yellow", bg_color: str = "")`: Логирует сообщение об успехе с опциональными цветами текста и фона.
- `warning(self, message, ex=None, exc_info=False, text_color: str = "light_red", bg_color: str = "")`: Логирует предупреждение с опциональными цветами текста и фона.
- `debug(self, message, ex=None, exc_info=True, text_color: str = "cyan", bg_color: str = "")`: Логирует отладочное сообщение с опциональными цветами текста и фона.
- `exception(self, message, ex=None, exc_info=True, text_color: str = "cyan", bg_color: str = "light_gray")`: Логирует сообщение об исключении с опциональными цветами текста и фона.
- `error(self, message, ex=None, exc_info=True, text_color: str = "red", bg_color: str = "")`: Логирует сообщение об ошибке с опциональными цветами текста и фона.
- `critical(self, message, ex=None, exc_info=True, text_color: str = "red", bg_color: str = "white")`: Логирует критическое сообщение с опциональными цветами текста и фона.

**Параметры**:
- `info_log_path` (Optional[str], optional): Путь к файлу для информационных логов. По умолчанию `info.log`.
- `debug_log_path` (Optional[str], optional): Путь к файлу для отладочных логов. По умолчанию `debug.log`.
- `errors_log_path` (Optional[str], optional): Путь к файлу для логов ошибок. По умолчанию `errors.log`.
- `json_log_path` (Optional[str], optional): Путь к файлу для JSON-логов. По умолчанию `log.json`.

**Примеры**:
```python
# Инициализация логгера
logger = Logger(info_log_path='info.log', debug_log_path='debug.log', errors_log_path='errors.log', json_log_path='log.json')

# Логирование информации
logger.info('Программа запущена')

# Логирование отладочной информации
logger.debug('Значение переменной x = 5')

# Логирование предупреждения
logger.warning('Предупреждение: недостаточно памяти')

# Логирование ошибки
try:
    x = 1 / 0
except Exception as ex:
    logger.error('Ошибка при делении на ноль', ex, exc_info=True)

# Логирование критической ошибки
logger.critical('Критическая ошибка: программа завершена')
```

## Функции

### `_format_message`

```python
def _format_message(self, message, ex=None, color: Optional[Tuple[str, str]] = None, level=None):
    """Returns formatted message with optional color and exception information."""
    ...
```

**Описание**: Возвращает отформатированное сообщение с информацией об исключении и цветом.

**Параметры**:
- `message` (str): Сообщение для логирования.
- `ex` (Optional[Exception], optional): Объект исключения. По умолчанию `None`.
- `color` (Optional[Tuple[str, str]], optional): Кортеж, содержащий цвет текста и фона. По умолчанию `None`.
- `level` (int, optional): Уровень логирования. По умолчанию `None`.

**Возвращает**:
- `str`: Отформатированное сообщение.

**Как работает функция**:
1. Извлекает символ лога на основе уровня логирования из словаря `LOG_SYMBOLS`.
2. Если указан цвет, извлекает цвета текста и фона из словарей `TEXT_COLORS` и `BG_COLORS`.
3. Форматирует сообщение, добавляя символ лога, цвета (если указаны) и информацию об исключении (если есть).
4. Возвращает отформатированное сообщение.

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

**Как работает функция**:
1. Получает информацию о фрейме стека вызовов, откуда была вызвана функция.
2. Извлекает имя файла, имя функции и номер строки из информации о фрейме.
3. Форматирует строку, содержащую информацию об исключении, имени файла, имени функции и номере строки.
4. Возвращает отформатированную строку.

### `log`

```python
def log(self, level, message, ex=None, exc_info=False, color: Optional[Tuple[str, str]] = None):
    """General method to log messages at specified level with optional color."""
    ...
```

**Описание**: Общий метод для логирования сообщений на указанном уровне с возможностью добавления цвета.

**Параметры**:
- `level` (int): Уровень логирования (например, `logging.INFO`, `logging.ERROR`).
- `message` (str): Сообщение для логирования.
- `ex` (Exception, optional): Объект исключения. По умолчанию `None`.
- `exc_info` (bool, optional): Флаг, указывающий, нужно ли включать информацию об исключении в лог. По умолчанию `False`.
- `color` (Tuple[str, str], optional): Кортеж, содержащий цвет текста и фона. По умолчанию `None`.

**Как работает функция**:
1. Форматирует сообщение с использованием метода `_format_message`.
2. Если включена информация об исключении и есть объект исключения, использует `self.logger_console.exception` для логирования сообщения.
3. В противном случае использует `self.logger_console.log` для логирования сообщения на указанном уровне.

### `info`

```python
def info(self, message, ex=None, exc_info=False, text_color: str = "green", bg_color: str = ""):
    """Logs an info message with optional text and background colors."""
    ...
```

**Описание**: Логирует информационное сообщение с опциональными цветами текста и фона.

**Параметры**:
- `message` (str): Сообщение для логирования.
- `ex` (Exception, optional): Объект исключения. По умолчанию `None`.
- `exc_info` (bool, optional): Флаг, указывающий, нужно ли включать информацию об исключении в лог. По умолчанию `False`.
- `text_color` (str, optional): Цвет текста. По умолчанию `"green"`.
- `bg_color` (str, optional): Цвет фона. По умолчанию `""`.

**Как работает функция**:
1. Определяет кортеж `color` из `text_color` и `bg_color`.
2. Вызывает метод `self.log` с уровнем `logging.INFO` и указанным сообщением, исключением, информацией об исключении и цветом.

### `success`

```python
def success(self, message, ex=None, exc_info=False, text_color: str = "yellow", bg_color: str = ""):
    """Logs a success message with optional text and background colors."""
    ...
```

**Описание**: Логирует сообщение об успехе с опциональными цветами текста и фона.

**Параметры**:
- `message` (str): Сообщение для логирования.
- `ex` (Exception, optional): Объект исключения. По умолчанию `None`.
- `exc_info` (bool, optional): Флаг, указывающий, нужно ли включать информацию об исключении в лог. По умолчанию `False`.
- `text_color` (str, optional): Цвет текста. По умолчанию `"yellow"`.
- `bg_color` (str, optional): Цвет фона. По умолчанию `""`.

**Как работает функция**:
1. Определяет кортеж `color` из `text_color` и `bg_color`.
2. Вызывает метод `self.log` с уровнем `logging.INFO` и указанным сообщением, исключением, информацией об исключении и цветом.

### `warning`

```python
def warning(self, message, ex=None, exc_info=False, text_color: str = "light_red", bg_color: str = ""):
    """Logs a warning message with optional text and background colors."""
    ...
```

**Описание**: Логирует предупреждающее сообщение с опциональными цветами текста и фона.

**Параметры**:
- `message` (str): Сообщение для логирования.
- `ex` (Exception, optional): Объект исключения. По умолчанию `None`.
- `exc_info` (bool, optional): Флаг, указывающий, нужно ли включать информацию об исключении в лог. По умолчанию `False`.
- `text_color` (str, optional): Цвет текста. По умолчанию `"light_red"`.
- `bg_color` (str, optional): Цвет фона. По умолчанию `""`.

**Как работает функция**:
1. Определяет кортеж `color` из `text_color` и `bg_color`.
2. Вызывает метод `self.log` с уровнем `logging.WARNING` и указанным сообщением, исключением, информацией об исключении и цветом.

### `debug`

```python
def debug(self, message, ex=None, exc_info=True, text_color: str = "cyan", bg_color: str = ""):
    """Logs a debug message with optional text and background colors."""
    ...
```

**Описание**: Логирует отладочное сообщение с опциональными цветами текста и фона.

**Параметры**:
- `message` (str): Сообщение для логирования.
- `ex` (Exception, optional): Объект исключения. По умолчанию `None`.
- `exc_info` (bool, optional): Флаг, указывающий, нужно ли включать информацию об исключении в лог. По умолчанию `True`.
- `text_color` (str, optional): Цвет текста. По умолчанию `"cyan"`.
- `bg_color` (str, optional): Цвет фона. По умолчанию `""`.

**Как работает функция**:
1. Определяет кортеж `color` из `text_color` и `bg_color`.
2. Вызывает метод `self.log` с уровнем `logging.DEBUG` и указанным сообщением, исключением, информацией об исключении и цветом.

### `exception`

```python
def exception(self, message, ex=None, exc_info=True, text_color: str = "cyan", bg_color: str = "light_gray"):
    """Logs an exception message with optional text and background colors."""
    ...
```

**Описание**: Логирует сообщение об исключении с опциональными цветами текста и фона.

**Параметры**:
- `message` (str): Сообщение для логирования.
- `ex` (Exception, optional): Объект исключения. По умолчанию `None`.
- `exc_info` (bool, optional): Флаг, указывающий, нужно ли включать информацию об исключении в лог. По умолчанию `True`.
- `text_color` (str, optional): Цвет текста. По умолчанию `"cyan"`.
- `bg_color` (str, optional): Цвет фона. По умолчанию `"light_gray"`.

**Как работает функция**:
1. Определяет кортеж `color` из `text_color` и `bg_color`.
2. Вызывает метод `self.log` с уровнем `logging.ERROR` и указанным сообщением, исключением, информацией об исключении и цветом.

### `error`

```python
def error(self, message, ex=None, exc_info=True, text_color: str = "red", bg_color: str = ""):
    """Logs an error message with optional text and background colors."""
    ...
```

**Описание**: Логирует сообщение об ошибке с опциональными цветами текста и фона.

**Параметры**:
- `message` (str): Сообщение для логирования.
- `ex` (Exception, optional): Объект исключения. По умолчанию `None`.
- `exc_info` (bool, optional): Флаг, указывающий, нужно ли включать информацию об исключении в лог. По умолчанию `True`.
- `text_color` (str, optional): Цвет текста. По умолчанию `"red"`.
- `bg_color` (str, optional): Цвет фона. По умолчанию `""`.

**Как работает функция**:
1. Определяет кортеж `color` из `text_color` и `bg_color`.
2. Вызывает метод `self.log` с уровнем `logging.ERROR` и указанным сообщением, исключением, информацией об исключении и цветом.

### `critical`

```python
def critical(self, message, ex=None, exc_info=True, text_color: str = "red", bg_color: str = "white"):
    """Logs a critical message with optional text and background colors."""
    ...
```

**Описание**: Логирует критическое сообщение с опциональными цветами текста и фона.

**Параметры**:
- `message` (str): Сообщение для логирования.
- `ex` (Exception, optional): Объект исключения. По умолчанию `None`.
- `exc_info` (bool, optional): Флаг, указывающий, нужно ли включать информацию об исключении в лог. По умолчанию `True`.
- `text_color` (str, optional): Цвет текста. По умолчанию `"red"`.
- `bg_color` (str, optional): Цвет фона. По умолчанию `"white"`.

**Как работает функция**:
1. Определяет кортеж `color` из `text_color` и `bg_color`.
2. Вызывает метод `self.log` с уровнем `logging.CRITICAL` и указанным сообщением, исключением, информацией об исключении и цветом.