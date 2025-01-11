# Модуль `src.logger.logger`

## Обзор

Модуль `src.logger.logger` предназначен для реализации системы логирования в приложении. Он поддерживает вывод логов в консоль, файлы и JSON-формате. Модуль использует паттерн Singleton для обеспечения единственного экземпляра логгера. Все импорты строятся относительно корневого пути проекта.

## Содержание

- [Классы](#классы)
  - [`SingletonMeta`](#singletonmeta)
  - [`JsonFormatter`](#jsonformatter)
  - [`Logger`](#logger)
- [Переменные](#переменные)
- [Глобальные переменные](#глобальные-переменные)

## Классы

### `SingletonMeta`

**Описание**: Метакласс для реализации паттерна Singleton.

**Методы**:

- `__call__(cls, *args, **kwargs)`: Создает или возвращает существующий экземпляр класса.

### `JsonFormatter`

**Описание**: Пользовательский форматтер для логирования в JSON-формате.

**Методы**:

- `format(self, record)`: Форматирует запись лога в JSON.

### `Logger`

**Описание**: Класс логгера, реализующий паттерн Singleton с поддержкой логирования в консоль, файлы и JSON.

**Параметры:**
-   `log_files_path` (`Path`): Путь к папке с лог файлами.
-   `info_log_path` (`Path`): Путь к файлу с информационными логами.
-   `debug_log_path` (`Path`): Путь к файлу с отладочными логами.
-  `errors_log_path` (`Path`): Путь к файлу с логами ошибок.
-   `json_log_path` (`Path`): Путь к файлу с JSON логами.

**Методы**:

- `__init__(self, info_log_path: Optional[str] = None, debug_log_path: Optional[str] = None, errors_log_path: Optional[str] = None, json_log_path: Optional[str] = None)`
    
    **Описание**: Инициализирует экземпляр логгера.

    **Параметры**:
    - `info_log_path` (Optional[str], optional): Путь к файлу для информационных логов. По умолчанию `None`.
    - `debug_log_path` (Optional[str], optional): Путь к файлу для отладочных логов. По умолчанию `None`.
    - `errors_log_path` (Optional[str], optional): Путь к файлу для логов ошибок. По умолчанию `None`.
    - `json_log_path` (Optional[str], optional): Путь к файлу для JSON логов. По умолчанию `None`.

-   `_format_message(self, message, ex=None, color: Optional[Tuple[str, str]] = None) -> str`:

    **Описание**: Форматирует сообщение с опциональным цветом и информацией об исключении.

    **Параметры**:
    - `message` (str): Сообщение для логирования.
    - `ex` (Optional[str], optional): Текст исключения. По умолчанию `None`.
    - `color` (Optional[Tuple[str, str]], optional): Кортеж из двух строк, представляющий цвет текста и фона. По умолчанию `None`.

    **Возвращает**:
    - `str`: Отформатированное сообщение.

-   `_ex_full_info(self, ex)`:

    **Описание**: Возвращает полную информацию об исключении, включая предыдущую функцию, файл и номер строки.

    **Параметры**:
    - `ex`: Информация об исключении.

    **Возвращает**:
    - `str`: Полная информация об исключении.
-   `log(self, level, message, ex=None, exc_info=False, color: Optional[Tuple[str, str]] = None)`:
    
    **Описание**: Общий метод для записи сообщений лога на указанном уровне с опциональным цветом.

    **Параметры**:
    - `level`: Уровень логирования (например, `logging.INFO`, `logging.DEBUG`).
    - `message`: Сообщение для логирования.
    - `ex` (Optional[str], optional): Исключение. По умолчанию `None`.
    - `exc_info` (bool, optional): Флаг для включения информации об исключении. По умолчанию `False`.
    - `color` (Optional[Tuple[str, str]], optional): Кортеж с цветом текста и фона. По умолчанию `None`.
    
- `info(self, message, ex=None, exc_info=False, text_color: str = "green", bg_color: str = "")`:

    **Описание**: Записывает информационное сообщение с опциональным цветом текста и фона.

    **Параметры**:
    - `message` (str): Сообщение для логирования.
    - `ex` (Optional[str], optional): Исключение. По умолчанию `None`.
    - `exc_info` (bool, optional): Флаг для включения информации об исключении. По умолчанию `False`.
    - `text_color` (str, optional): Цвет текста. По умолчанию `"green"`.
    - `bg_color` (str, optional): Цвет фона. По умолчанию `""`.

-   `success(self, message, ex=None, exc_info=False, text_color: str = "yellow", bg_color: str = "")`:
  
    **Описание**: Записывает сообщение об успехе с опциональным цветом текста и фона.

    **Параметры**:
    - `message` (str): Сообщение для логирования.
    - `ex` (Optional[str], optional): Исключение. По умолчанию `None`.
    - `exc_info` (bool, optional): Флаг для включения информации об исключении. По умолчанию `False`.
    - `text_color` (str, optional): Цвет текста. По умолчанию `"yellow"`.
    - `bg_color` (str, optional): Цвет фона. По умолчанию `""`.

-   `warning(self, message, ex=None, exc_info=False, text_color: str = "black", bg_color: str = "yellow")`:

    **Описание**: Записывает сообщение предупреждения с опциональным цветом текста и фона.

    **Параметры**:
    - `message` (str): Сообщение для логирования.
    - `ex` (Optional[str], optional): Исключение. По умолчанию `None`.
    - `exc_info` (bool, optional): Флаг для включения информации об исключении. По умолчанию `False`.
    - `text_color` (str, optional): Цвет текста. По умолчанию `"black"`.
    - `bg_color` (str, optional): Цвет фона. По умолчанию `"yellow"`.

-   `debug(self, message, ex=None, exc_info=True, text_color: str = "cyan", bg_color: str = "")`:

    **Описание**: Записывает отладочное сообщение с опциональным цветом текста и фона.

    **Параметры**:
    - `message` (str): Сообщение для логирования.
    - `ex` (Optional[str], optional): Исключение. По умолчанию `None`.
    - `exc_info` (bool, optional): Флаг для включения информации об исключении. По умолчанию `True`.
    - `text_color` (str, optional): Цвет текста. По умолчанию `"cyan"`.
    - `bg_color` (str, optional): Цвет фона. По умолчанию `""`.

-   `error(self, message, ex=None, exc_info=True, text_color: str = "red", bg_color: str = "")`:

    **Описание**: Записывает сообщение об ошибке с опциональным цветом текста и фона.

    **Параметры**:
    - `message` (str): Сообщение для логирования.
    - `ex` (Optional[str], optional): Исключение. По умолчанию `None`.
    - `exc_info` (bool, optional): Флаг для включения информации об исключении. По умолчанию `True`.
    - `text_color` (str, optional): Цвет текста. По умолчанию `"red"`.
    - `bg_color` (str, optional): Цвет фона. По умолчанию `""`.

-   `critical(self, message, ex=None, exc_info=True, text_color: str = "red", bg_color: str = "white")`:
   
    **Описание**: Записывает критическое сообщение с опциональным цветом текста и фона.

    **Параметры**:
    - `message` (str): Сообщение для логирования.
    - `ex` (Optional[str], optional): Исключение. По умолчанию `None`.
    - `exc_info` (bool, optional): Флаг для включения информации об исключении. По умолчанию `True`.
    - `text_color` (str, optional): Цвет текста. По умолчанию `"red"`.
    - `bg_color` (str, optional): Цвет фона. По умолчанию `"white"`.

## Переменные
- `TEXT_COLORS`: Словарь для текстовых цветов.
- `BG_COLORS`: Словарь для цветов фона.

## Глобальные переменные
- `logger`: Экземпляр класса `Logger`, инициализированный по умолчанию.