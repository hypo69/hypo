# Модуль `src.logger`

## Обзор

Модуль `src.logger` предоставляет гибкую систему логирования, поддерживающую вывод в консоль, файлы и JSON. Он использует паттерн Singleton для гарантии единственного экземпляра логгера во всем приложении. Логгер поддерживает различные уровни логирования (например, `INFO`, `ERROR`, `DEBUG`) и включает цветной вывод для консольных логов. Также можно настроить форматы вывода логов и управлять записью в различные файлы.

## Подробней

Модуль `src.logger` предназначен для централизованного и удобного логирования событий в приложении. Он позволяет легко переключаться между различными уровнями логирования, настраивать формат вывода и направлять логи в различные места (консоль, файлы). Использование паттерна Singleton гарантирует, что все части приложения используют один и тот же экземпляр логгера, что упрощает управление и конфигурацию. Этот модуль важен для отладки, мониторинга и анализа работы приложения.

## Классы

### `SingletonMeta`

**Описание**: Метакласс, реализующий паттерн Singleton для логгера.

**Методы**:
- `__call__`: Обеспечивает создание только одного экземпляра класса.

**Примеры**

```python
class MyClass(metaclass=SingletonMeta):
    pass

instance1 = MyClass()
instance2 = MyClass()

print(instance1 is instance2)  # Вывод: True
```

### `JsonFormatter`

**Описание**: Пользовательский форматтер, выводящий логи в формате JSON.

**Методы**:
- `format`: Форматирует запись лога в JSON.

### `Logger`

**Описание**: Основной класс логгера, поддерживающий вывод в консоль, файлы и JSON.

**Методы**:
- `__init__`: Инициализирует экземпляр логгера с заполнителями для различных типов логгеров (консоль, файл и JSON).
- `_configure_logger`: Настраивает и возвращает экземпляр логгера.
- `initialize_loggers`: Инициализирует логгеры для консоли и файлового логирования (info, debug, error и JSON).
- `log`: Логирует сообщение на указанном уровне с опциональным исключением и цветовым форматированием.
- `info`: Логирует информационное сообщение.
- `success`: Логирует сообщение об успехе.
- `warning`: Логирует предупреждающее сообщение.
- `debug`: Логирует отладочное сообщение.
- `error`: Логирует сообщение об ошибке.
- `critical`: Логирует критическое сообщение.

**Параметры**:
- `info_log_path` (Optional[str]): Путь к файлу для информационных логов.
- `debug_log_path` (Optional[str]): Путь к файлу для отладочных логов.
- `errors_log_path` (Optional[str]): Путь к файлу для логов ошибок.
- `json_log_path` (Optional[str]): Путь к файлу для JSON логов.

## Функции

### `_configure_logger`

```python
def _configure_logger(name: str, log_path: str, level: Optional[int] = logging.DEBUG, formatter: Optional[logging.Formatter] = None, mode: Optional[str] = 'a') -> logging.Logger:
    """ This if example function
    Args:
        name (str): Имя логгера.
        log_path (str): Путь к файлу лога.
        level (Optional[int], optional): Уровень логирования. По умолчанию logging.DEBUG.
        formatter (Optional[logging.Formatter], optional): Пользовательский форматтер. По умолчанию None.
        mode (Optional[str], optional): Режим файла. По умолчанию 'a'.
    Returns:
        logging.Logger: Настроенный экземпляр logging.Logger.

     **Как работает функция**:
     Функция `_configure_logger` настраивает и возвращает экземпляр логгера. Она принимает имя логгера, путь к файлу лога, уровень логирования, форматтер и режим файла. Если форматтер не указан, используется стандартный форматтер. Функция создает обработчик файла и устанавливает уровень логирования и форматтер для обработчика. Затем она добавляет обработчик к логгеру и возвращает логгер.

    """
   # - Не выводи тело функции. только документацию и примеры вызова функции;
```

**Описание**: Настраивает и возвращает экземпляр логгера.

**Параметры**:
- `name` (str): Имя логгера.
- `log_path` (str): Путь к файлу лога.
- `level` (Optional[int], optional): Уровень логирования. По умолчанию `logging.DEBUG`.
- `formatter` (Optional[logging.Formatter], optional): Пользовательский форматтер. По умолчанию `None`.
- `mode` (Optional[str], optional): Режим файла. По умолчанию `'a'` (append).

**Возвращает**:
- `logging.Logger`: Настроенный экземпляр `logging.Logger`.

**Примеры**:

```python
import logging
from src.logger.logger import Logger  # Укажите правильный путь к вашему модулю

# Пример использования функции _configure_logger внутри класса Logger:
logger_instance = Logger()
configured_logger = logger_instance._configure_logger(
    name='my_logger',
    log_path='my_log_file.log',
    level=logging.INFO
)

configured_logger.info('This is a test message.')
```

### `initialize_loggers`

```python
def initialize_loggers(info_log_path: Optional[str] = '', debug_log_path: Optional[str] = '', errors_log_path: Optional[str] = '', json_log_path: Optional[str] = '') -> None:
    """ This if example function
    Args:
        info_log_path (Optional[str], optional): Путь к файлу для информационных логов. По умолчанию ''.
        debug_log_path (Optional[str], optional): Путь к файлу для отладочных логов. По умолчанию ''.
        errors_log_path (Optional[str], optional): Путь к файлу для логов ошибок. По умолчанию ''.
        json_log_path (Optional[str], optional): Путь к файлу для JSON логов. По умолчанию ''.
    Returns:
        None: 

     **Как работает функция**:
     Функция `initialize_loggers` инициализирует логгеры для различных уровней логирования (info, debug, error и JSON). Она принимает пути к файлам логов для каждого уровня логирования. Если путь не указан, логгер для этого уровня не создается. Функция вызывает метод `_configure_logger` для создания и настройки каждого логгера.

    """
   # - Не выводи тело функции. только документацию и примеры вызова функции;
```

**Описание**: Инициализирует логгеры для консоли и файлового логирования (info, debug, error и JSON).

**Параметры**:
- `info_log_path` (Optional[str], optional): Путь к файлу для информационных логов. По умолчанию `''`.
- `debug_log_path` (Optional[str], optional): Путь к файлу для отладочных логов. По умолчанию `''`.
- `errors_log_path` (Optional[str], optional): Путь к файлу для логов ошибок. По умолчанию `''`.
- `json_log_path` (Optional[str], optional): Путь к файлу для JSON логов. По умолчанию `''`.

**Примеры**:

```python
from src.logger.logger import Logger  # Укажите правильный путь к вашему модулю

# Пример использования функции initialize_loggers:
logger_instance = Logger()
config = {
    'info_log_path': 'logs/info.log',
    'debug_log_path': 'logs/debug.log',
    'errors_log_path': 'logs/errors.log',
    'json_log_path': 'logs/log.json'
}
logger_instance.initialize_loggers(**config)
```

### `log`

```python
def log(level, message, ex=None, exc_info=False, color=None) -> None:
    """ This if example function
    Args:
        level (int): Уровень логирования (например, logging.INFO, logging.DEBUG).
        message (str): Логируемое сообщение.
        ex (Exception, optional): Опциональное исключение для логирования. По умолчанию None.
        exc_info (bool, optional): Флаг, указывающий, нужно ли включать информацию об исключении. По умолчанию False.
        color (tuple, optional): Кортеж с цветами текста и фона для вывода в консоль. По умолчанию None.
    Returns:
        None:

     **Как работает функция**:
     Функция `log` является основной функцией для логирования сообщений. Она принимает уровень логирования, сообщение, исключение (если есть) и флаг для включения информации об исключении. Функция определяет, нужно ли выводить сообщение в консоль и/или в файл, и выполняет логирование соответствующим образом.

    """
   # - Не выводи тело функции. только документацию и примеры вызова функции;
```

**Описание**: Логирует сообщение на указанном уровне (например, `INFO`, `DEBUG`, `ERROR`) с опциональным исключением и цветовым форматированием.

**Параметры**:
- `level` (int): Уровень логирования (например, `logging.INFO`, `logging.DEBUG`).
- `message` (str): Логируемое сообщение.
- `ex` (Exception, optional): Опциональное исключение для логирования. По умолчанию `None`.
- `exc_info` (bool, optional): Флаг, указывающий, нужно ли включать информацию об исключении. По умолчанию `False`.
- `color` (tuple, optional): Кортеж с цветами текста и фона для вывода в консоль. По умолчанию `None`.

**Примеры**:

```python
import logging
import colorama
from src.logger.logger import Logger  # Укажите правильный путь к вашему модулю

# Пример использования функции log:
logger_instance = Logger()
config = {
    'info_log_path': 'logs/info.log',
    'debug_log_path': 'logs/debug.log',
    'errors_log_path': 'logs/errors.log',
    'json_log_path': 'logs/log.json'
}
logger_instance.initialize_loggers(**config)

logger_instance.log(logging.INFO, 'This is an info message.')
logger_instance.log(logging.ERROR, 'This is an error message.', exc_info=True)
logger_instance.log(logging.WARNING, 'This is a warning message with color.', color=(colorama.Fore.YELLOW, colorama.Back.BLACK))
```

### `info`

```python
def info(message, ex=None, exc_info=False, colors: Optional[tuple] = None) -> None:
    """ This if example function
    Args:
        message (str): Информационное сообщение для логирования.
        ex (Exception, optional): Опциональное исключение для логирования. По умолчанию None.
        exc_info (bool, optional): Флаг, указывающий, нужно ли включать информацию об исключении. По умолчанию False.
        colors (tuple, optional): Кортеж с цветами текста и фона для вывода в консоль. По умолчанию None.
    Returns:
        None:

     **Как работает функция**:
     Функция `info` логирует информационное сообщение. Она вызывает функцию `log` с уровнем логирования `logging.INFO`.

    """
   # - Не выводи тело функции. только документацию и примеры вызова функции;
```

**Описание**: Логирует информационное сообщение.

**Параметры**:
- `message` (str): Информационное сообщение для логирования.
- `ex` (Exception, optional): Опциональное исключение для логирования. По умолчанию `None`.
- `exc_info` (bool, optional): Флаг, указывающий, нужно ли включать информацию об исключении. По умолчанию `False`.
- `colors` (tuple, optional): Кортеж с цветами текста и фона для вывода в консоль. По умолчанию `None`.

### `success`

```python
def success(message, ex=None, exc_info=False, colors: Optional[tuple] = None) -> None:
    """ This if example function
    Args:
        message (str): Сообщение об успехе для логирования.
        ex (Exception, optional): Опциональное исключение для логирования. По умолчанию None.
        exc_info (bool, optional): Флаг, указывающий, нужно ли включать информацию об исключении. По умолчанию False.
        colors (tuple, optional): Кортеж с цветами текста и фона для вывода в консоль. По умолчанию None.
    Returns:
        None:

     **Как работает функция**:
     Функция `success` логирует сообщение об успехе. Она вызывает функцию `log` с уровнем логирования `logging.INFO`.

    """
   # - Не выводи тело функции. только документацию и примеры вызова функции;
```

**Описание**: Логирует сообщение об успехе.

**Параметры**:
- `message` (str): Сообщение об успехе для логирования.
- `ex` (Exception, optional): Опциональное исключение для логирования. По умолчанию `None`.
- `exc_info` (bool, optional): Флаг, указывающий, нужно ли включать информацию об исключении. По умолчанию `False`.
- `colors` (tuple, optional): Кортеж с цветами текста и фона для вывода в консоль. По умолчанию `None`.

### `warning`

```python
def warning(message, ex=None, exc_info=False, colors: Optional[tuple] = None) -> None:
    """ This if example function
    Args:
        message (str): Предупреждающее сообщение для логирования.
        ex (Exception, optional): Опциональное исключение для логирования. По умолчанию None.
        exc_info (bool, optional): Флаг, указывающий, нужно ли включать информацию об исключении. По умолчанию False.
        colors (tuple, optional): Кортеж с цветами текста и фона для вывода в консоль. По умолчанию None.
    Returns:
        None:

     **Как работает функция**:
     Функция `warning` логирует предупреждающее сообщение. Она вызывает функцию `log` с уровнем логирования `logging.WARNING`.

    """
   # - Не выводи тело функции. только документацию и примеры вызова функции;
```

**Описание**: Логирует предупреждающее сообщение.

**Параметры**:
- `message` (str): Предупреждающее сообщение для логирования.
- `ex` (Exception, optional): Опциональное исключение для логирования. По умолчанию `None`.
- `exc_info` (bool, optional): Флаг, указывающий, нужно ли включать информацию об исключении. По умолчанию `False`.
- `colors` (tuple, optional): Кортеж с цветами текста и фона для вывода в консоль. По умолчанию `None`.

### `debug`

```python
def debug(message, ex=None, exc_info=True, colors: Optional[tuple] = None) -> None:
    """ This if example function
    Args:
        message (str): Отладочное сообщение для логирования.
        ex (Exception, optional): Опциональное исключение для логирования. По умолчанию None.
        exc_info (bool, optional): Флаг, указывающий, нужно ли включать информацию об исключении. По умолчанию True.
        colors (tuple, optional): Кортеж с цветами текста и фона для вывода в консоль. По умолчанию None.
    Returns:
        None:

     **Как работает функция**:
     Функция `debug` логирует отладочное сообщение. Она вызывает функцию `log` с уровнем логирования `logging.DEBUG`.

    """
   # - Не выводи тело функции. только документацию и примеры вызова функции;
```

**Описание**: Логирует отладочное сообщение.

**Параметры**:
- `message` (str): Отладочное сообщение для логирования.
- `ex` (Exception, optional): Опциональное исключение для логирования. По умолчанию `None`.
- `exc_info` (bool, optional): Флаг, указывающий, нужно ли включать информацию об исключении. По умолчанию `True`.
- `colors` (tuple, optional): Кортеж с цветами текста и фона для вывода в консоль. По умолчанию `None`.

### `error`

```python
def error(message, ex=None, exc_info=True, colors: Optional[tuple] = None) -> None:
    """ This if example function
    Args:
        message (str): Сообщение об ошибке для логирования.
        ex (Exception, optional): Опциональное исключение для логирования. По умолчанию None.
        exc_info (bool, optional): Флаг, указывающий, нужно ли включать информацию об исключении. По умолчанию True.
        colors (tuple, optional): Кортеж с цветами текста и фона для вывода в консоль. По умолчанию None.
    Returns:
        None:

     **Как работает функция**:
     Функция `error` логирует сообщение об ошибке. Она вызывает функцию `log` с уровнем логирования `logging.ERROR`.

    """
   # - Не выводи тело функции. только документацию и примеры вызова функции;
```

**Описание**: Логирует сообщение об ошибке.

**Параметры**:
- `message` (str): Сообщение об ошибке для логирования.
- `ex` (Exception, optional): Опциональное исключение для логирования. По умолчанию `None`.
- `exc_info` (bool, optional): Флаг, указывающий, нужно ли включать информацию об исключении. По умолчанию `True`.
- `colors` (tuple, optional): Кортеж с цветами текста и фона для вывода в консоль. По умолчанию `None`.

### `critical`

```python
def critical(message, ex=None, exc_info=True, colors: Optional[tuple] = None) -> None:
    """ This if example function
    Args:
        message (str): Критическое сообщение для логирования.
        ex (Exception, optional): Опциональное исключение для логирования. По умолчанию None.
        exc_info (bool, optional): Флаг, указывающий, нужно ли включать информацию об исключении. По умолчанию True.
        colors (tuple, optional): Кортеж с цветами текста и фона для вывода в консоль. По умолчанию None.
    Returns:
        None:

     **Как работает функция**:
     Функция `critical` логирует критическое сообщение. Она вызывает функцию `log` с уровнем логирования `logging.CRITICAL`.

    """
   # - Не выводи тело функции. только документацию и примеры вызова функции;
```

**Описание**: Логирует критическое сообщение.

**Параметры**:
- `message` (str): Критическое сообщение для логирования.
- `ex` (Exception, optional): Опциональное исключение для логирования. По умолчанию `None`.
- `exc_info` (bool, optional): Флаг, указывающий, нужно ли включать информацию об исключении. По умолчанию `True`.
- `colors` (tuple, optional): Кортеж с цветами текста и фона для вывода в консоль. По умолчанию `None`.

## Параметры для `Logger`

Класс `Logger` принимает несколько опциональных параметров для настройки поведения логирования.

- **Level**: Управляет уровнем серьезности регистрируемых логов. Общие уровни включают:
  - `logging.DEBUG`: Подробная информация, полезная для диагностики проблем.
  - `logging.INFO`: Общая информация, например об успешных операциях.
  - `logging.WARNING`: Предупреждения, которые не обязательно требуют немедленных действий.
  - `logging.ERROR`: Сообщения об ошибках.
  - `logging.CRITICAL`: Критические ошибки, требующие немедленного внимания.

- **Formatter**: Определяет, как форматируются сообщения журнала. По умолчанию сообщения форматируются как `'%(asctime)s - %(levelname)s - %(message)s'`. Вы можете предоставить пользовательский форматтер для различных форматов, например JSON.

- **Color**: Цвета для сообщений журнала в консоли. Цвета указываются в виде кортежа с двумя элементами:
  - **Цвет текста**: Указывает цвет текста (например, `colorama.Fore.RED`).
  - **Цвет фона**: Указывает цвет фона (например, `colorama.Back.WHITE`).

Цвет можно настроить для различных уровней журнала (например, зеленый для информации, красный для ошибок и т. д.).

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

Пути к файлам, указанные в `config`, используются для записи логов в соответствующие файлы для каждого уровня логирования.

## Пример использования

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

#### 2. Логирование сообщений на разных уровнях:

```python
logger.info('Это информационное сообщение')
logger.success('Это сообщение об успехе')
logger.warning('Это предупреждающее сообщение')
logger.debug('Это отладочное сообщение')
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
logger.error('У этого сообщения будет красный фон', colors=(colorama.Fore.WHITE, colorama.Back.RED))
```

Этот модуль предоставляет комплексную и гибкую систему логирования для Python-приложений. Вы можете настроить консольное и файловое логирование с различными форматами и цветами, управлять уровнями логирования и корректно обрабатывать исключения. Конфигурация для файлового логирования хранится в словаре `config`, что обеспечивает простую настройку.