# Модуль `logger`

## Обзор

Модуль `logger` предназначен для реализации логирования в приложении. Он предоставляет функциональность для вывода сообщений в консоль, записи в файлы (информационные, отладочные, ошибки), а также записи логов в формате JSON. Модуль использует паттерн Singleton для обеспечения единственного экземпляра логгера.

## Содержание

1. [Классы](#классы)
    - [`SingletonMeta`](#singletonmeta)
    - [`JsonFormatter`](#jsonformatter)
    - [`Logger`](#logger)
2. [Функции](#функции)

## Классы

### `SingletonMeta`

**Описание**: Метакласс для реализации паттерна Singleton.

**Методы**:
- `__call__`: Метод, вызываемый при создании нового экземпляра класса. Гарантирует, что будет создан только один экземпляр класса.

### `JsonFormatter`

**Описание**: Кастомный форматтер для логирования в формате JSON.

**Методы**:
- `format`: Форматирует запись лога в виде JSON.

### `Logger`

**Описание**: Класс Logger, реализующий паттерн Singleton для ведения логов в консоль, файлы и в формате JSON.

**Параметры**:
- `info_log_path` (Optional[str], optional): Путь к файлу для информационных логов. По умолчанию `None`.
- `debug_log_path` (Optional[str], optional): Путь к файлу для отладочных логов. По умолчанию `None`.
- `errors_log_path` (Optional[str], optional): Путь к файлу для логов ошибок. По умолчанию `None`.
- `json_log_path` (Optional[str], optional): Путь к файлу для JSON логов. По умолчанию `None`.

**Методы**:
- `__init__`: Инициализирует экземпляр Logger, создаёт директории и файлы для логов, настраивает логгеры.
- `_format_message`: Форматирует сообщение, добавляя цвет и информацию об исключении.
- `_ex_full_info`: Возвращает полную информацию об исключении, включая имя файла, функции и номер строки, где возникло исключение.
- `log`: Общий метод для логирования сообщений на указанном уровне с опциональным цветом.
- `info`: Логирует информационное сообщение с опциональными цветами.
- `success`: Логирует сообщение об успехе с опциональными цветами.
- `warning`: Логирует предупреждение с опциональными цветами.
- `debug`: Логирует отладочное сообщение с опциональными цветами.
- `error`: Логирует сообщение об ошибке с опциональными цветами.
- `critical`: Логирует критическое сообщение с опциональными цветами.

## Функции

### `_format_message`

**Описание**: Форматирует сообщение для вывода в лог, добавляя цвета и информацию об исключении.

**Параметры**:
- `message` (str): Сообщение для логирования.
- `ex` (Optional, optional): Исключение, которое нужно добавить в сообщение. По умолчанию `None`.
- `color` (Optional[Tuple[str, str]], optional): Кортеж из двух строк, представляющих цвет текста и фона. По умолчанию `None`.

**Возвращает**:
- `str`: Отформатированное сообщение.

### `_ex_full_info`

**Описание**: Возвращает полную информацию об исключении, включая имя файла, функции и номер строки.

**Параметры**:
- `ex`: Исключение, информацию о котором нужно получить.

**Возвращает**:
- `str`: Строка с информацией об исключении.

### `log`

**Описание**: Общий метод для логирования сообщений на указанном уровне с опциональным цветом.

**Параметры**:
- `level`: Уровень логирования (например, `logging.INFO`, `logging.ERROR`).
- `message`: Сообщение для логирования.
- `ex` (Optional, optional): Исключение, которое нужно добавить в сообщение. По умолчанию `None`.
- `exc_info` (bool, optional): Если `True`, то добавляет информацию об исключении в сообщение. По умолчанию `False`.
- `color` (Optional[Tuple[str, str]], optional): Кортеж из двух строк, представляющих цвет текста и фона. По умолчанию `None`.

### `info`

**Описание**: Логирует информационное сообщение с опциональными цветами.

**Параметры**:
- `message` (str): Сообщение для логирования.
- `ex` (Optional, optional): Исключение, которое нужно добавить в сообщение. По умолчанию `None`.
- `exc_info` (bool, optional): Если `True`, то добавляет информацию об исключении в сообщение. По умолчанию `False`.
- `text_color` (str, optional): Цвет текста. По умолчанию `"green"`.
- `bg_color` (str, optional): Цвет фона. По умолчанию `""`.

### `success`

**Описание**: Логирует сообщение об успехе с опциональными цветами.

**Параметры**:
- `message` (str): Сообщение для логирования.
- `ex` (Optional, optional): Исключение, которое нужно добавить в сообщение. По умолчанию `None`.
- `exc_info` (bool, optional): Если `True`, то добавляет информацию об исключении в сообщение. По умолчанию `False`.
- `text_color` (str, optional): Цвет текста. По умолчанию `"yellow"`.
- `bg_color` (str, optional): Цвет фона. По умолчанию `""`.

### `warning`

**Описание**: Логирует предупреждение с опциональными цветами.

**Параметры**:
- `message` (str): Сообщение для логирования.
- `ex` (Optional, optional): Исключение, которое нужно добавить в сообщение. По умолчанию `None`.
- `exc_info` (bool, optional): Если `True`, то добавляет информацию об исключении в сообщение. По умолчанию `False`.
- `text_color` (str, optional): Цвет текста. По умолчанию `"black"`.
- `bg_color` (str, optional): Цвет фона. По умолчанию `"yellow"`.

### `debug`

**Описание**: Логирует отладочное сообщение с опциональными цветами.

**Параметры**:
- `message` (str): Сообщение для логирования.
- `ex` (Optional, optional): Исключение, которое нужно добавить в сообщение. По умолчанию `None`.
- `exc_info` (bool, optional): Если `True`, то добавляет информацию об исключении в сообщение. По умолчанию `True`.
- `text_color` (str, optional): Цвет текста. По умолчанию `"cyan"`.
- `bg_color` (str, optional): Цвет фона. По умолчанию `""`.

### `error`

**Описание**: Логирует сообщение об ошибке с опциональными цветами.

**Параметры**:
- `message` (str): Сообщение для логирования.
- `ex` (Optional, optional): Исключение, которое нужно добавить в сообщение. По умолчанию `None`.
- `exc_info` (bool, optional): Если `True`, то добавляет информацию об исключении в сообщение. По умолчанию `True`.
- `text_color` (str, optional): Цвет текста. По умолчанию `"red"`.
- `bg_color` (str, optional): Цвет фона. По умолчанию `""`.

### `critical`

**Описание**: Логирует критическое сообщение с опциональными цветами.

**Параметры**:
- `message` (str): Сообщение для логирования.
- `ex` (Optional, optional): Исключение, которое нужно добавить в сообщение. По умолчанию `None`.
- `exc_info` (bool, optional): Если `True`, то добавляет информацию об исключении в сообщение. По умолчанию `True`.
- `text_color` (str, optional): Цвет текста. По умолчанию `"red"`.
- `bg_color` (str, optional): Цвет фона. По умолчанию `"white"`.