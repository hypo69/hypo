# Документация для модуля `src.logger`

## Обзор

Модуль `src.logger` предоставляет гибкую систему логирования, поддерживающую логирование в консоль, файлы и в формате JSON. Он использует шаблон проектирования Singleton, чтобы обеспечить использование единственного экземпляра логгера во всем приложении. Логгер поддерживает различные уровни логирования (например, `INFO`, `ERROR`, `DEBUG`) и включает цветное отображение для вывода в консоль. Также доступны настройки форматов вывода и управление логированием в различные файлы.

## Подробней

Модуль `src.logger` предназначен для централизованного управления логированием в проекте `hypotez`. Он обеспечивает единообразный интерфейс для записи логов в различные источники, такие как консоль, файлы разных уровней (информация, отладка, ошибки) и JSON-файлы. Использование шаблона Singleton гарантирует, что во всем приложении будет использоваться один и тот же экземпляр логгера, что упрощает управление и конфигурацию логирования.

## Классы

### `SingletonMeta`

**Описание**: Метакласс, реализующий шаблон Singleton для логгера.

**Принцип работы**:
Метакласс `SingletonMeta` обеспечивает создание только одного экземпляра класса `Logger`. При первом вызове класса создается экземпляр, который затем возвращается при последующих вызовах. Это гарантирует, что во всем приложении используется один и тот же объект логгера.

### `JsonFormatter`

**Описание**: Кастомный форматтер для вывода логов в формате JSON.

**Принцип работы**:
Класс `JsonFormatter` используется для форматирования логов в формате JSON. Он наследуется от стандартного форматтера `logging.Formatter` и переопределяет метод `format` для преобразования записей лога в JSON-строки.

### `Logger`

**Описание**: Основной класс логгера, поддерживающий логирование в консоль, файлы и в формате JSON.

**Принцип работы**:
Класс `Logger` является центральным компонентом модуля `src.logger`. Он предоставляет методы для инициализации логгеров, настройки обработчиков (handlers) и логирования сообщений на различных уровнях (INFO, DEBUG, ERROR и т.д.). Класс использует метакласс `SingletonMeta` для обеспечения единственного экземпляра логгера.

**Методы**:
- `__init__`: Инициализирует экземпляр класса Logger с плейсхолдерами для различных типов логгеров (консоль, файлы и JSON).
- `_configure_logger(name: str, log_path: str, level: Optional[int] = logging.DEBUG, formatter: Optional[logging.Formatter] = None, mode: Optional[str] = 'a') -> logging.Logger`: Настраивает и возвращает экземпляр логгера.
- `initialize_loggers(info_log_path: Optional[str] = '', debug_log_path: Optional[str] = '', errors_log_path: Optional[str] = '', json_log_path: Optional[str] = '')`: Инициализирует логгеры для логирования в консоль и файлы (информация, отладка, ошибки и JSON).
- `log(level, message, ex=None, exc_info=False, color=None)`: Логирует сообщение на указанном уровне (например, `INFO`, `DEBUG`, `ERROR`) с возможным исключением и цветовым форматированием.
- `info(message: str, colors: Optional[Tuple[Any, Any]] = None)`: Логирует информационное сообщение.
- `success(message: str, colors: Optional[Tuple[Any, Any]] = None)`: Логирует сообщение об успешной операции.
- `warning(message: str, colors: Optional[Tuple[Any, Any]] = None)`: Логирует предупреждение.
- `debug(message: str, colors: Optional[Tuple[Any, Any]] = None)`: Логирует сообщение для отладки.
- `error(message: str, ex: Optional[Exception] = None, exc_info: bool = True, colors: Optional[Tuple[Any, Any]] = None)`: Логирует сообщение об ошибке.
- `critical(message: str, colors: Optional[Tuple[Any, Any]] = None)`: Логирует критическое сообщение.

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
        mode (Optional[str], optional): Режим работы с файлом, например, `'a'` для добавления (значение по умолчанию). По умолчанию `'a'`.

    Returns:
        logging.Logger: Настроенный экземпляр `logging.Logger`.
    """
```

**Назначение**:
Функция `_configure_logger` настраивает и возвращает экземпляр логгера. Она создает обработчик (handler) для записи логов в файл, устанавливает уровень логирования и форматтер для сообщений.

**Параметры**:
- `name` (str): Имя логгера.
- `log_path` (str): Путь к файлу логов.
- `level` (Optional[int], optional): Уровень логирования, например, `logging.DEBUG`. По умолчанию `logging.DEBUG`.
- `formatter` (Optional[logging.Formatter], optional): Кастомный форматтер (опционально). По умолчанию `None`.
- `mode` (Optional[str], optional): Режим работы с файлом, например, `'a'` для добавления (значение по умолчанию). По умолчанию `'a'`.

**Возвращает**:
- `logging.Logger`: Настроенный экземпляр `logging.Logger`.

**Как работает функция**:
1. Создается объект логгера с заданным именем.
2. Устанавливается уровень логирования.
3. Создается обработчик `logging.FileHandler` для записи логов в файл.
4. Устанавливается форматтер для обработчика.
5. Добавляется обработчик к логгеру.
6. Возвращается настроенный объект логгера.

**ASCII flowchart**:
```
Начало --> Создание логгера
|
Установка уровня логирования
|
Создание обработчика FileHandler
|
Установка форматтера для обработчика
|
Добавление обработчика к логгеру
|
Возврат настроенного логгера --> Конец
```

**Примеры**:
```python
import logging
from src.logger.logger import Logger

logger_instance = Logger()
log = logger_instance._configure_logger(name='my_logger', log_path='my_log.log', level=logging.INFO)
log.info('Сообщение в лог')
```

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
    """
```

**Назначение**:
Функция `initialize_loggers` инициализирует логгеры для логирования в консоль и файлы. Она создает и настраивает различные логгеры для информации, отладки, ошибок и JSON-формата.

**Параметры**:
- `info_log_path` (Optional[str], optional): Путь к файлу логов информации (опционально). По умолчанию ''.
- `debug_log_path` (Optional[str], optional): Путь к файлу логов отладки (опционально). По умолчанию ''.
- `errors_log_path` (Optional[str], optional): Путь к файлу логов ошибок (опционально). По умолчанию ''.
- `json_log_path` (Optional[str], optional): Путь к файлу логов в формате JSON (опционально). По умолчанию ''.

**Как работает функция**:
1. Настраивается основной логгер для консоли с цветовым форматированием.
2. Если указаны пути к файлам, создаются и настраиваются логгеры для информации, отладки, ошибок и JSON-формата.

**ASCII flowchart**:
```
Начало --> Настройка логгера для консоли
|
Проверка наличия info_log_path --> Если есть, настройка логгера для info
|
Проверка наличия debug_log_path --> Если есть, настройка логгера для debug
|
Проверка наличия errors_log_path --> Если есть, настройка логгера для errors
|
Проверка наличия json_log_path --> Если есть, настройка логгера для json
|
Конец
```

**Примеры**:
```python
from src.logger.logger import Logger

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
def log(level: int, message: str, ex: Optional[Exception] = None, exc_info: bool = False, colors: Optional[Tuple[Any, Any]] = None) -> None:
    """
    Логирует сообщение на указанном уровне (например, `INFO`, `DEBUG`, `ERROR`) с возможным исключением и цветовым форматированием.

    Args:
        level (int): Уровень логирования (например, `logging.INFO`, `logging.DEBUG`).
        message (str): Логируемое сообщение.
        ex (Optional[Exception], optional): Исключение для логирования (опционально). По умолчанию `None`.
        exc_info (bool, optional): Включать информацию об исключении (значение по умолчанию — `False`).
        colors (Optional[Tuple[Any, Any]], optional): Кортеж цветов текста и фона для консольного вывода (опционально). По умолчанию `None`.
    """
```

**Назначение**:
Функция `log` логирует сообщение на указанном уровне с возможностью добавления информации об исключении и цветового форматирования.

**Параметры**:
- `level` (int): Уровень логирования (например, `logging.INFO`, `logging.DEBUG`).
- `message` (str): Логируемое сообщение.
- `ex` (Optional[Exception], optional): Исключение для логирования (опционально). По умолчанию `None`.
- `exc_info` (bool, optional): Включать информацию об исключении (значение по умолчанию — `False`).
- `colors` (Optional[Tuple[Any, Any]], optional): Кортеж цветов текста и фона для консольного вывода (опционально). По умолчанию `None`.

**Как работает функция**:
1. Форматирует сообщение. Если передано исключение, добавляет его в сообщение.
2. Логирует сообщение на указанном уровне.
3. Если указаны цвета, устанавливает их для консольного вывода.

**ASCII flowchart**:
```
Начало --> Форматирование сообщения
|
Логирование сообщения на указанном уровне
|
Установка цветов для консольного вывода (если указаны)
|
Конец
```

**Примеры**:
```python
import logging
from src.logger.logger import Logger
import colorama

logger_instance = Logger()
logger_instance.initialize_loggers()
logger_instance.log(level=logging.INFO, message='Это информационное сообщение')
logger_instance.log(level=logging.ERROR, message='Произошла ошибка', ex=Exception('Test error'), exc_info=True)
logger_instance.log(level=logging.INFO, message='Зеленый текст', colors=(colorama.Fore.GREEN, colorama.Back.BLACK))
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

### 1. Инициализация логгера:

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

### 2. Логирование сообщений:

```python
from src.logger.logger import logger

logger.info('Это информационное сообщение')
logger.success('Это сообщение об успешной операции')
logger.warning('Это предупреждение')
logger.debug('Это сообщение для отладки')
logger.error('Это сообщение об ошибке')
logger.critical('Это критическое сообщение')
```

### 3. Настройка цветов:

```python
import colorama
from src.logger.logger import logger

logger.info('Это сообщение будет зеленым', colors=(colorama.Fore.GREEN, colorama.Back.BLACK))
logger.error('Это сообщение с красным фоном', colors=(colorama.Fore.WHITE, colorama.Back.RED))
```