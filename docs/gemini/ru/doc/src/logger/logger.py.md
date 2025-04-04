# Модуль логирования `src.logger.logger`

## Обзор

Модуль `src.logger.logger` предназначен для реализации гибкой системы логирования в проекте `hypotez`. Он предоставляет класс `Logger`, который использует паттерн Singleton для обеспечения единственного экземпляра логгера в приложении. Логгер поддерживает запись сообщений в консоль, файлы (info, debug, errors) и в JSON-формате. Модуль также включает настройки цветового оформления для консольного вывода и позволяет форматировать сообщения с информацией об исключениях.

## Подробней

Этот модуль предоставляет централизованный механизм для регистрации событий, ошибок и отладочной информации, что упрощает мониторинг и отладку приложения. Класс `Logger` конфигурируется через файл `config.json`, где определяются пути к файлам логов. Использование Singleton гарантирует, что все компоненты приложения используют один и тот же экземпляр логгера, что упрощает управление и конфигурирование логирования.

## Классы

### `SingletonMeta`

**Описание**: Метакласс, реализующий паттерн Singleton.

**Принцип работы**:
Метакласс `SingletonMeta` гарантирует, что класс, для которого он используется, будет иметь только один экземпляр. Это достигается за счет хранения экземпляра класса в словаре `_instances` и использования блокировки `_lock` для обеспечения потокобезопасности при создании экземпляра.

**Методы**:

- `__call__(cls, *args, **kwargs)`: Метод вызывается при создании экземпляра класса. Он проверяет, существует ли уже экземпляр класса в `_instances`. Если нет, то создается новый экземпляр, сохраняется в `_instances` и возвращается. Если экземпляр уже существует, то возвращается существующий экземпляр.

### `JsonFormatter`

**Описание**: Класс, реализующий пользовательский форматтер для логирования в JSON-формате.

**Принцип работы**:
Класс `JsonFormatter` наследуется от `logging.Formatter` и переопределяет метод `format`, чтобы форматировать записи лога в виде JSON-строки. Это позволяет легко записывать структурированные данные логов в файл для последующего анализа.

**Методы**:

- `format(self, record)`: Форматирует запись лога в JSON-формат. Извлекает атрибуты записи лога, такие как время, уровень, сообщение и информацию об исключении (если есть), и формирует из них словарь, который затем преобразуется в JSON-строку.

### `Logger`

**Описание**: Класс логгера, реализующий паттерн Singleton и поддерживающий логирование в консоль, файлы и JSON-формате.

**Принцип работы**:
Класс `Logger` использует метакласс `SingletonMeta` для реализации паттерна Singleton. При инициализации он настраивает несколько логгеров: для консоли, для записи информации в файл, для отладочной информации в файл, для ошибок в файл и для записи в JSON-файл. Пути к файлам логов настраиваются через файл `config.json`.

**Методы**:

- `__init__`
   ```python
   def __init__(
       self,
       info_log_path: Optional[str] = None,
       debug_log_path: Optional[str] = None,
       errors_log_path: Optional[str] = None,
       json_log_path: Optional[str] = None,
   ):
       """Инициализирует экземпляр Logger."""
   ```

   **Назначение**: Инициализация экземпляра класса `Logger`.

   **Параметры**:
   - `info_log_path` (Optional[str], optional): Путь к файлу для записи информационных логов. По умолчанию `None`.
   - `debug_log_path` (Optional[str], optional): Путь к файлу для записи отладочных логов. По умолчанию `None`.
   - `errors_log_path` (Optional[str], optional): Путь к файлу для записи логов ошибок. По умолчанию `None`.
   - `json_log_path` (Optional[str], optional): Путь к файлу для записи логов в формате JSON. По умолчанию `None`.

   **Возвращает**: Ничего.

   **Вызывает исключения**: Отсутствуют.

   **Как работает функция**:
    1.  Чтение конфигурации из файла `config.json` и получение путей для логов.
    2.  Формирование путей для файлов логирования на основе текущей даты и времени.
    3.  Создание директорий для хранения логов, если они не существуют.
    4.  Создание файлов логов, если они не существуют.
    5.  Инициализация логгеров для консоли и файлов, установка уровней логирования и форматтеров.
    6.  Удаление обработчиков, выводящих логи в консоль, для JSON-логгера, чтобы избежать дублирования.

    **ASCII flowchart**:

    ```
    A [Чтение конфигурации из config.json]
    ↓
    B [Формирование путей для файлов логирования]
    ↓
    C [Создание директорий для хранения логов]
    ↓
    D [Создание файлов логов]
    ↓
    E [Инициализация логгеров для консоли и файлов]
    ↓
    F [Удаление обработчиков консоли для JSON-логгера]
    ```

   **Примеры**:

   ```python
   from src.logger.logger import Logger
   logger = Logger(info_log_path='info.log', debug_log_path='debug.log', errors_log_path='errors.log', json_log_path='log.json')
   ```

- `_format_message`
   ```python
   def _format_message(self, message, ex=None, color: Optional[Tuple[str, str]] = None, level=None):
       """Возвращает отформатированное сообщение с опциональным цветом и информацией об исключении."""
   ```

   **Назначение**: Форматирование сообщения лога с добавлением символа, цвета и информации об исключении.

   **Параметры**:
   - `message` (str): Сообщение для логирования.
   - `ex` (Optional[Exception], optional): Объект исключения. По умолчанию `None`.
   - `color` (Optional[Tuple[str, str]], optional): Кортеж, содержащий цвет текста и фона. По умолчанию `None`.
   - `level` (int, optional): Уровень логирования. По умолчанию `None`.

   **Возвращает**:
   - `str`: Отформатированное сообщение.

   **Вызывает исключения**: Отсутствуют.

   **Как работает функция**:
    1.  Определение символа лога на основе уровня логирования.
    2.  Применение цветового оформления, если оно задано.
    3.  Формирование итогового сообщения с символом, цветом и информацией об исключении.

    **ASCII flowchart**:

    ```
    A [Определение символа лога]
    ↓
    B [Применение цветового оформления (если задано)]
    ↓
    C [Формирование итогового сообщения]
    ```

   **Примеры**:

   ```python
   formatted_message = logger._format_message("Some message", ex=ValueError("Invalid value"), color=("red", "white"), level=logging.ERROR)
   ```

- `_ex_full_info`
   ```python
   def _ex_full_info(self, ex):
       """Возвращает полную информацию об исключении вместе с деталями о предыдущей функции, файле и строке."""
   ```

   **Назначение**: Получение полной информации об исключении, включая имя файла, имя функции и номер строки, где произошло исключение.

   **Параметры**:
   - `ex` (Exception): Объект исключения.

   **Возвращает**:
   - `str`: Полная информация об исключении.

   **Вызывает исключения**: Отсутствуют.

   **Как работает функция**:
    1.  Получение информации о фрейме стека вызовов.
    2.  Извлечение имени файла, имени функции и номера строки из фрейма.
    3.  Формирование строки с полной информацией об исключении.

    **ASCII flowchart**:

    ```
    A [Получение информации о фрейме стека вызовов]
    ↓
    B [Извлечение имени файла, имени функции и номера строки]
    ↓
    C [Формирование строки с информацией об исключении]
    ```

   **Примеры**:

   ```python
   try:
       raise ValueError("Some error")
   except ValueError as ex:
       full_info = logger._ex_full_info(ex)
       print(full_info)
   ```

- `log`
   ```python
   def log(self, level, message, ex=None, exc_info=False, color: Optional[Tuple[str, str]] = None):
       """Общий метод для логирования сообщений на указанном уровне с опциональным цветом."""
   ```

   **Назначение**: Общий метод для логирования сообщений на указанном уровне с возможностью добавления цвета и информации об исключении.

   **Параметры**:
   - `level` (int): Уровень логирования (например, `logging.INFO`, `logging.ERROR`).
   - `message` (str): Сообщение для логирования.
   - `ex` (Exception, optional): Объект исключения. По умолчанию `None`.
   - `exc_info` (bool, optional): Флаг, указывающий, нужно ли добавлять информацию об исключении в лог. По умолчанию `False`.
   - `color` (Tuple[str, str], optional): Кортеж, содержащий цвет текста и фона. По умолчанию `None`.

   **Возвращает**: Ничего.

   **Вызывает исключения**: Отсутствуют.

   **Как работает функция**:
    1.  Форматирование сообщения с использованием метода `_format_message`.
    2.  Логирование сообщения в консоль и файлы в зависимости от уровня логирования и настроек.

    **ASCII flowchart**:

    ```
    A [Форматирование сообщения]
    ↓
    B [Логирование сообщения в консоль (если включено)]
    ↓
    C [Логирование сообщения в файлы (info, debug, errors, json)]
    ```

   **Примеры**:

   ```python
   logger.log(logging.INFO, "Some information message", color=("green", ""))
   logger.log(logging.ERROR, "Some error message", ex=ValueError("Invalid value"), exc_info=True)
   ```

- `info`
   ```python
   def info(self, message, ex=None, exc_info=False, text_color: str = "green", bg_color: str = ""):
       """Логирует информационное сообщение с опциональным цветом текста и фона."""
   ```

   **Назначение**: Логирование информационного сообщения с возможностью указания цвета текста и фона.

   **Параметры**:
   - `message` (str): Сообщение для логирования.
   - `ex` (Exception, optional): Объект исключения. По умолчанию `None`.
   - `exc_info` (bool, optional): Флаг, указывающий, нужно ли добавлять информацию об исключении в лог. По умолчанию `False`.
   - `text_color` (str, optional): Цвет текста. По умолчанию "green".
   - `bg_color` (str, optional): Цвет фона. По умолчанию "".

   **Возвращает**: Ничего.

   **Вызывает исключения**: Отсутствуют.

   **Как работает функция**:
    1.  Вызов метода `log` с уровнем логирования `logging.INFO` и указанными параметрами.

   **Примеры**:

   ```python
   logger.info("Some information message")
   logger.info("Some information message", ex=ValueError("Invalid value"), exc_info=True)
   ```

- `success`
   ```python
   def success(self, message, ex=None, exc_info=False, text_color: str = "yellow", bg_color: str = ""):
       """Логирует сообщение об успехе с опциональным цветом текста и фона."""
   ```

   **Назначение**: Логирование сообщения об успехе с возможностью указания цвета текста и фона.

   **Параметры**:
   - `message` (str): Сообщение для логирования.
   - `ex` (Exception, optional): Объект исключения. По умолчанию `None`.
   - `exc_info` (bool, optional): Флаг, указывающий, нужно ли добавлять информацию об исключении в лог. По умолчанию `False`.
   - `text_color` (str, optional): Цвет текста. По умолчанию "yellow".
   - `bg_color` (str, optional): Цвет фона. По умолчанию "".

   **Возвращает**: Ничего.

   **Вызывает исключения**: Отсутствуют.

   **Как работает функция**:
    1.  Вызов метода `log` с уровнем логирования `logging.INFO` и указанными параметрами.

   **Примеры**:

   ```python
   logger.success("Operation completed successfully")
   ```

- `warning`
   ```python
   def warning(self, message, ex=None, exc_info=False, text_color: str = "light_red", bg_color: str = ""):
       """Логирует предупреждающее сообщение с опциональным цветом текста и фона."""
   ```

   **Назначение**: Логирование предупреждающего сообщения с возможностью указания цвета текста и фона.

   **Параметры**:
   - `message` (str): Сообщение для логирования.
   - `ex` (Exception, optional): Объект исключения. По умолчанию `None`.
   - `exc_info` (bool, optional): Флаг, указывающий, нужно ли добавлять информацию об исключении в лог. По умолчанию `False`.
   - `text_color` (str, optional): Цвет текста. По умолчанию "light_red".
   - `bg_color` (str, optional): Цвет фона. По умолчанию "".

   **Возвращает**: Ничего.

   **Вызывает исключения**: Отсутствуют.

   **Как работает функция**:
    1.  Вызов метода `log` с уровнем логирования `logging.WARNING` и указанными параметрами.

   **Примеры**:

   ```python
   logger.warning("Some potential issue detected")
   ```

- `debug`
   ```python
   def debug(self, message, ex=None, exc_info=True, text_color: str = "cyan", bg_color: str = ""):
       """Логирует отладочное сообщение с опциональным цветом текста и фона."""
   ```

   **Назначение**: Логирование отладочного сообщения с возможностью указания цвета текста и фона.

   **Параметры**:
   - `message` (str): Сообщение для логирования.
   - `ex` (Exception, optional): Объект исключения. По умолчанию `None`.
   - `exc_info` (bool, optional): Флаг, указывающий, нужно ли добавлять информацию об исключении в лог. По умолчанию `True`.
   - `text_color` (str, optional): Цвет текста. По умолчанию "cyan".
   - `bg_color` (str, optional): Цвет фона. По умолчанию "".

   **Возвращает**: Ничего.

   **Вызывает исключения**: Отсутствуют.

   **Как работает функция**:
    1.  Вызов метода `log` с уровнем логирования `logging.DEBUG` и указанными параметрами.

   **Примеры**:

   ```python
   logger.debug("Some debug information")
   ```

- `exception`
   ```python
   def exception(self, message, ex=None, exc_info=True, text_color: str = "cyan", bg_color: str = "light_gray"):
       """Логирует сообщение об исключении с опциональным цветом текста и фона."""
   ```

   **Назначение**: Логирование сообщения об исключении с возможностью указания цвета текста и фона.

   **Параметры**:
   - `message` (str): Сообщение для логирования.
   - `ex` (Exception, optional): Объект исключения. По умолчанию `None`.
   - `exc_info` (bool, optional): Флаг, указывающий, нужно ли добавлять информацию об исключении в лог. По умолчанию `True`.
   - `text_color` (str, optional): Цвет текста. По умолчанию "cyan".
   - `bg_color` (str, optional): Цвет фона. По умолчанию "light_gray".

   **Возвращает**: Ничего.

   **Вызывает исключения**: Отсутствуют.

   **Как работает функция**:
    1.  Вызов метода `log` с уровнем логирования `logging.ERROR` и указанными параметрами.

   **Примеры**:

   ```python
   try:
       raise ValueError("Some error")
   except ValueError as ex:
       logger.exception("An exception occurred", ex=ex, exc_info=True)
   ```

- `error`
   ```python
   def error(self, message, ex=None, exc_info=True, text_color: str = "red", bg_color: str = ""):
       """Логирует сообщение об ошибке с опциональным цветом текста и фона."""
   ```

   **Назначение**: Логирование сообщения об ошибке с возможностью указания цвета текста и фона.

   **Параметры**:
   - `message` (str): Сообщение для логирования.
   - `ex` (Exception, optional): Объект исключения. По умолчанию `None`.
   - `exc_info` (bool, optional): Флаг, указывающий, нужно ли добавлять информацию об исключении в лог. По умолчанию `True`.
   - `text_color` (str, optional): Цвет текста. По умолчанию "red".
   - `bg_color` (str, optional): Цвет фона. По умолчанию "".

   **Возвращает**: Ничего.

   **Вызывает исключения**: Отсутствуют.

   **Как работает функция**:
    1.  Вызов метода `log` с уровнем логирования `logging.ERROR` и указанными параметрами.

   **Примеры**:

   ```python
   logger.error("Some error occurred")
   ```

- `critical`
   ```python
   def critical(self, message, ex=None, exc_info=True, text_color: str = "red", bg_color: str = "white"):
       """Логирует критическое сообщение с опциональным цветом текста и фона."""
   ```

   **Назначение**: Логирование критического сообщения с возможностью указания цвета текста и фона.

   **Параметры**:
   - `message` (str): Сообщение для логирования.
   - `ex` (Exception, optional): Объект исключения. По умолчанию `None`.
   - `exc_info` (bool, optional): Флаг, указывающий, нужно ли добавлять информацию об исключении в лог. По умолчанию `True`.
   - `text_color` (str, optional): Цвет текста. По умолчанию "red".
   - `bg_color` (str, optional): Цвет фона. По умолчанию "white".

   **Возвращает**: Ничего.

   **Вызывает исключения**: Отсутствуют.

   **Как работает функция**:
    1.  Вызов метода `log` с уровнем логирования `logging.CRITICAL` и указанными параметрами.

   **Примеры**:

   ```python
   logger.critical("A critical error occurred")
   ```

## Функции

В данном модуле функции отсутствуют.

## Переменные

- `TEXT_COLORS`
   - Словарь, содержащий ANSI-коды для задания цветов текста в консоли.

- `BG_COLORS`
   - Словарь, содержащий ANSI-коды для задания цветов фона в консоли.

- `LOG_SYMBOLS`
   - Словарь, содержащий символы, соответствующие уровням логирования.

- `logger`
   - Экземпляр класса `Logger`, используемый для логирования сообщений.