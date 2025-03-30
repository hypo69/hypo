# Модуль `src.logger`

## Обзор

Модуль `src.logger` предоставляет гибкую систему логирования, поддерживающую логирование в консоль, файлы и в формате JSON. Он использует шаблон проектирования Singleton, чтобы обеспечить использование единственного экземпляра логгера во всем приложении. Логгер поддерживает различные уровни логирования (например, `INFO`, `ERROR`, `DEBUG`) и включает цветное отображение для вывода в консоль. Также доступны настройки форматов вывода и управление логированием в различные файлы.

## Подробнее

Модуль логирования в проекте `hypotez` предназначен для централизованного управления логированием событий, происходящих в различных частях приложения. Он позволяет разработчикам легко записывать информацию о работе программы, отлаживать код и отслеживать ошибки. Использование Singleton гарантирует, что все компоненты приложения используют один и тот же экземпляр логгера, что упрощает настройку и управление логированием. Модуль поддерживает различные уровни логирования, такие как `DEBUG`, `INFO`, `WARNING`, `ERROR` и `CRITICAL`, что позволяет фильтровать сообщения в зависимости от их важности. Кроме того, модуль позволяет логировать сообщения в консоль, файлы и в формате JSON, что обеспечивает гибкость в выборе способа хранения и анализа логов.

## Классы

### `SingletonMeta`

**Описание**: Метакласс, реализующий шаблон Singleton для логгера.

### `JsonFormatter`

**Описание**: Кастомный форматтер для вывода логов в формате JSON.

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
    """This if example function
    Args:
        name (str): Имя логгера.
        log_path (str): Путь к файлу логов.
        level (Optional[int], optional): Уровень логирования, например, logging.DEBUG. Значение по умолчанию — logging.DEBUG.
        formatter (Optional[logging.Formatter], optional): Кастомный форматтер (опционально).
        mode (Optional[str], optional): Режим работы с файлом, например, 'a' для добавления (значение по умолчанию).
    Returns:
        logging.Logger: Настроенный экземпляр logging.Logger.

     **Как работает функция**:
     Функция `_configure_logger` настраивает и возвращает экземпляр логгера. Она принимает имя логгера, путь к файлу логов, уровень логирования, форматтер и режим работы с файлом. Если форматтер не указан, используется формат по умолчанию. Функция создает обработчик файла и устанавливает для него уровень логирования и форматтер. Затем она добавляет обработчик к логгеру и возвращает настроенный экземпляр логгера.
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

**Примеры**:

```python
import logging
from src.logger.logger import Logger

logger: Logger = Logger()

log = logger._configure_logger(name='test_logger', log_path='test.log', level=logging.INFO)
logger.info('test')
```

### `initialize_loggers`

```python
def initialize_loggers(info_log_path: Optional[str] = '', debug_log_path: Optional[str] = '', errors_log_path: Optional[str] = '', json_log_path: Optional[str] = '') -> None:
    """This if example function
    Args:
        info_log_path (Optional[str], optional): Путь к файлу логов информации (опционально). По умолчанию ''.
        debug_log_path (Optional[str], optional): Путь к файлу логов отладки (опционально). По умолчанию ''.
        errors_log_path (Optional[str], optional): Путь к файлу логов ошибок (опционально). По умолчанию ''.
        json_log_path (Optional[str], optional): Путь к файлу логов в формате JSON (опционально). По умолчанию ''.
    Returns:
        None:

     **Как работает функция**:
     Функция `initialize_loggers` инициализирует логгеры для логирования в консоль и файлы. Она принимает пути к файлам логов для информации, отладки, ошибок и JSON. Если путь не указан, логирование в файл для данного типа сообщений не производится. Функция создает логгеры для каждого указанного пути и устанавливает для них уровень логирования и форматтер. Затем она добавляет обработчики к основному логгеру.
    """
    ...
```

**Описание**: Инициализирует логгеры для логирования в консоль и файлы (информация, отладка, ошибки и JSON).

**Параметры**:
- `info_log_path` (Optional[str], optional): Путь к файлу логов информации (опционально). По умолчанию `''`.
- `debug_log_path` (Optional[str], optional): Путь к файлу логов отладки (опционально). По умолчанию `''`.
- `errors_log_path` (Optional[str], optional): Путь к файлу логов ошибок (опционально). По умолчанию `''`.
- `json_log_path` (Optional[str], optional): Путь к файлу логов в формате JSON (опционально). По умолчанию `''`.

**Примеры**:

```python
from src.logger.logger import Logger

logger: Logger = Logger()
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
def log(level: int, message: str, ex: Optional[Exception] = None, exc_info: bool = False, colors: Optional[tuple[str, str]] = None) -> None:
    """This if example function
    Args:
        level (int): Уровень логирования (например, logging.INFO, logging.DEBUG).
        message (str): Логируемое сообщение.
        ex (Optional[Exception], optional): Исключение для логирования (опционально). По умолчанию None.
        exc_info (bool, optional): Включать информацию об исключении (значение по умолчанию — False).
        colors (Optional[tuple[str, str]], optional): Кортеж цветов текста и фона для консольного вывода (опционально). По умолчанию None.
    Returns:
        None:

     **Как работает функция**:
     Функция `log` логирует сообщение на указанном уровне. Она принимает уровень логирования, сообщение, исключение (если есть) и флаг, указывающий, нужно ли включать информацию об исключении. Функция также может принимать кортеж цветов для консольного вывода. Если указано исключение, оно добавляется к сообщению. Функция вызывает метод `log` у основного логгера для записи сообщения.
    """
    ...
```

**Описание**: Логирует сообщение на указанном уровне (например, `INFO`, `DEBUG`, `ERROR`) с возможным исключением и цветовым форматированием.

**Параметры**:
- `level` (int): Уровень логирования (например, `logging.INFO`, `logging.DEBUG`).
- `message` (str): Логируемое сообщение.
- `ex` (Optional[Exception], optional): Исключение для логирования (опционально). По умолчанию `None`.
- `exc_info` (bool, optional): Включать информацию об исключении (значение по умолчанию — `False`).
- `colors` (Optional[tuple[str, str]], optional): Кортеж цветов текста и фона для консольного вывода (опционально). По умолчанию `None`.

**Примеры**:

```python
import logging
import colorama
from src.logger.logger import Logger

logger: Logger = Logger()
config = {
    'info_log_path': 'logs/info.log',
    'debug_log_path': 'logs/debug.log',
    'errors_log_path': 'logs/errors.log',
    'json_log_path': 'logs/log.json'
}
logger.initialize_loggers(**config)

logger.info('Это информационное сообщение')
logger.error('Это сообщение об ошибке', colors=(colorama.Fore.WHITE, colorama.Back.RED))

try:
    1 / 0
except Exception as ex:
    logger.error('Произошла ошибка деления на ноль', ex, exc_info=True)
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
from src.logger.logger import Logger

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
from src.logger.logger import Logger

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
```

#### 3. Настройка цветов:

```python
import colorama
from src.logger.logger import Logger

logger: Logger = Logger()
config = {
    'info_log_path': 'logs/info.log',
    'debug_log_path': 'logs/debug.log',
    'errors_log_path': 'logs/errors.log',
    'json_log_path': 'logs/log.json'
}
logger.initialize_loggers(**config)

logger.info('Это сообщение будет зеленым', colors=(colorama.Fore.GREEN, colorama.Back.BLACK))
logger.error('Это сообщение с красным фоном', colors=(colorama.Fore.WHITE, colorama.Back.RED))
```