## АНАЛИЗ КОДА: `src.logger`

### 1. <алгоритм>

1.  **Инициализация Logger:**
    *   Создается экземпляр класса `Logger`.
    *   Используется паттерн Singleton, гарантирующий единственный экземпляр логгера.
    *   При инициализации устанавливаются плейсхолдеры для различных типов логгеров (консольный, файловый, JSON).

2.  **Конфигурация логгеров:**
    *   Вызывается метод `initialize_loggers`, который принимает пути к файлам логов (информация, отладка, ошибки, JSON) в качестве параметров.
    *   Для каждого типа логгера (`info`, `debug`, `error`, `json`) вызывается метод `_configure_logger`.
        *   Метод `_configure_logger` создает и настраивает экземпляр `logging.Logger` с указанным именем, путем к файлу, уровнем логирования, форматтером и режимом работы с файлом.
        *   Если форматтер не указан, используется формат по умолчанию. Для JSON используется кастомный форматтер `JsonFormatter`.
        *   Каждый созданный логгер сохраняется в атрибутах экземпляра `Logger` (например, `self.info_logger`, `self.debug_logger`).

3.  **Логирование сообщений:**
    *   Вызывается метод `log`, который принимает уровень логирования, сообщение, исключение (опционально), флаг для включения информации об исключении и цвет (опционально).
    *   В методе `log` сообщение передаётся в соответствующий логгер в зависимости от уровня логирования:
        *  `DEBUG` - `self.debug_logger`
        *   `INFO` - `self.info_logger`
        *   `WARNING` - `self.info_logger`
        *   `ERROR` - `self.error_logger`
        *   `CRITICAL` - `self.error_logger`
    *   Сообщения могут быть отформатированы с использованием цветов для консольного вывода.
    *   Есть сокращенные методы `info`, `success`, `warning`, `debug`, `error`, `critical`, которые просто вызывают метод `log` с соответствующим уровнем.

**Примеры:**

*   **Инициализация:**
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

    Здесь создается экземпляр `Logger` и настраиваются логгеры для файлов `info.log`, `debug.log`, `errors.log` и `log.json`.
*   **Логирование сообщения:**
    ```python
    logger.info("This is an info message")
    ```

    В данном случае сообщение "This is an info message" будет записано в файл `info.log` с уровнем логирования `INFO`.

### 2. <mermaid>

```mermaid
flowchart TD
    classDef default fill:#f9f,stroke:#333,stroke-width:2px
    classDef class fill:#ccf,stroke:#333,stroke-width:2px
    classDef function fill:#aaf,stroke:#333,stroke-width:2px
    
    Start[Start] --> Logger_Instance[<code>Logger</code><br>Instance Creation]
    class Logger_Instance class;

    Logger_Instance --> initialize_loggers_call[Call <code>initialize_loggers</code><br>with log paths]
    class initialize_loggers_call function;

    initialize_loggers_call --> configure_info_logger[Call <code>_configure_logger</code><br>for INFO logs]
    class configure_info_logger function;

    configure_info_logger --> create_info_logger[Create <code>logging.Logger</code><br>for INFO]
    class create_info_logger function;

    create_info_logger --> configure_debug_logger[Call <code>_configure_logger</code><br>for DEBUG logs]
    
    configure_debug_logger --> create_debug_logger[Create <code>logging.Logger</code><br>for DEBUG]

    create_debug_logger --> configure_error_logger[Call <code>_configure_logger</code><br>for ERROR logs]
    
    configure_error_logger --> create_error_logger[Create <code>logging.Logger</code><br>for ERROR]

   create_error_logger --> configure_json_logger[Call <code>_configure_logger</code><br>for JSON logs]
    
    configure_json_logger --> create_json_logger[Create <code>logging.Logger</code><br>for JSON]
    
    create_json_logger --> log_call[Call <code>log</code> method<br>to log a message]
    class log_call function;

    log_call --> log_level_check[Check Log Level]
    class log_level_check;

    log_level_check -- "DEBUG" --> debug_logger[<code>self.debug_logger</code><br>Log with DEBUG Level]
    class debug_logger;

    log_level_check -- "INFO or WARNING" --> info_logger[<code>self.info_logger</code><br>Log with INFO/WARNING Level]
    class info_logger;

    log_level_check -- "ERROR or CRITICAL" --> error_logger[<code>self.error_logger</code><br>Log with ERROR/CRITICAL Level]
    class error_logger;
    
    debug_logger --> End[End]
    info_logger --> End
    error_logger --> End
    
    linkStyle default stroke:#000,stroke-width:1px;
```

**Объяснение `mermaid` диаграммы:**

*   **`Start`**: Начало процесса, когда создается экземпляр класса `Logger`.
*   **`Logger_Instance`**: Экземпляр класса `Logger`. Используется Singleton для гарантии единого экземпляра.
*   **`initialize_loggers_call`**: Вызов метода `initialize_loggers` для настройки логгеров с передачей путей к файлам логов.
*   **`configure_info_logger`**, **`configure_debug_logger`**, **`configure_error_logger`**, **`configure_json_logger`**: Последовательные вызовы метода `_configure_logger` для настройки каждого типа логгера.
*   **`create_info_logger`**, **`create_debug_logger`**, **`create_error_logger`**, **`create_json_logger`**: Создание экземпляров `logging.Logger` с соответствующими параметрами (имя, путь к файлу, уровень, форматтер).
*   **`log_call`**: Вызов метода `log` для записи сообщения в лог.
*   **`log_level_check`**: Проверка уровня логирования для выбора соответствующего логгера.
*   **`debug_logger`**, **`info_logger`**, **`error_logger`**: Выбор нужного логгера, на основе уровня логирования, `info_logger` используется и для `warning` сообщений.
*   **`End`**: Завершение процесса логирования.

**Зависимости:**
*  Импортируются модули из стандартной библиотеки `logging` для создания и настройки логгеров.
*  Используются модули `colorama` для добавления цветов в консольный вывод.

### 3. <объяснение>

**Импорты:**

*   `logging`: Стандартный модуль Python для логирования. Предоставляет классы и функции для создания и настройки логгеров, обработчиков и форматтеров. Он используется для создания логгеров для различных типов (консоль, файлы).
*   `typing.Optional`: Используется для аннотации типов, указывая, что переменная может быть либо определенного типа, либо `None`.
*   `colorama`: Библиотека для добавления цветового форматирования в консольный вывод. Она используется для цветного вывода сообщений в консоль.

**Классы:**

*   **`SingletonMeta`**:
    *   **Роль**: Метакласс, который обеспечивает создание единственного экземпляра класса (Singleton).
    *   **Атрибуты**: `_instances` – словарь для хранения экземпляров классов.
    *   **Методы**: `__call__` – переопределяет вызов класса, возвращая существующий экземпляр или создавая новый, если его нет.
    *   **Взаимодействие**: Используется для класса `Logger`, гарантируя, что существует только один экземпляр логгера.

*   **`JsonFormatter`**:
    *   **Роль**: Кастомный форматтер, который преобразует логи в формат JSON.
    *   **Атрибуты**: Нет.
    *   **Методы**: `format` – форматирует запись лога в JSON, добавляя время, уровень логирования и сообщение.
    *   **Взаимодействие**: Используется при настройке логгера для JSON-файла, задавая формат записи лога.

*   **`Logger`**:
    *   **Роль**: Основной класс, предоставляющий интерфейс для логирования.
    *   **Атрибуты**: `info_logger`, `debug_logger`, `error_logger`, `json_logger` – хранят экземпляры логгеров.
    *   **Методы**:
        *   `__init__`: Инициализирует атрибуты логгеров как `None`.
        *   `_configure_logger`: Создает и настраивает экземпляр `logging.Logger`.
        *   `initialize_loggers`: Настраивает логгеры для файлов и консоли.
        *   `log`: Логирует сообщения с указанным уровнем, цветом и исключением.
        *   `info`, `success`, `warning`, `debug`, `error`, `critical`: Сокращенные методы для логирования сообщений с разными уровнями.
    *   **Взаимодействие**: Использует классы `JsonFormatter` и `logging` для реализации логирования.

**Функции:**

*   `_configure_logger(name: str, log_path: str, level: Optional[int] = logging.DEBUG, formatter: Optional[logging.Formatter] = None, mode: Optional[str] = 'a') -> logging.Logger`:
    *   **Аргументы**:
        *   `name`: Имя логгера.
        *   `log_path`: Путь к файлу логов.
        *   `level`: Уровень логирования (по умолчанию `logging.DEBUG`).
        *   `formatter`: Кастомный форматтер (по умолчанию `None`).
        *   `mode`: Режим открытия файла (по умолчанию `'a'` - append).
    *   **Возвращает**: Экземпляр `logging.Logger`.
    *   **Назначение**: Создает и настраивает логгер, подключает обработчик (handler) для записи в файл, задает формат сообщений.
    *   **Пример**:
    ```python
        logger = logging.getLogger("my_logger")
        file_handler = logging.FileHandler("my_log.log")
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.setLevel(logging.DEBUG)
    ```
    *   **Цепочка**: Вызывается из `initialize_loggers` для создания и настройки логгеров.

*   `initialize_loggers(info_log_path: Optional[str] = '', debug_log_path: Optional[str] = '', errors_log_path: Optional[str] = '', json_log_path: Optional[str] = '')`:
    *   **Аргументы**: Пути к файлам логов для информации, отладки, ошибок и JSON (все опционально).
    *   **Возвращает**: Ничего.
    *   **Назначение**: Инициализирует логгеры для разных типов сообщений, вызывая `_configure_logger` для каждого типа.
    *   **Пример**:
    ```python
    config = {
        'info_log_path': 'logs/info.log',
        'debug_log_path': 'logs/debug.log',
        'errors_log_path': 'logs/errors.log',
        'json_log_path': 'logs/log.json'
    }
    logger.initialize_loggers(**config)
    ```
    *   **Цепочка**: Вызывается после создания экземпляра `Logger` для настройки всех логгеров.

*   `log(level, message, ex=None, exc_info=False, color=None)`:
    *   **Аргументы**:
        *   `level`: Уровень логирования.
        *   `message`: Сообщение для записи.
        *   `ex`: Исключение для логирования (опционально).
        *   `exc_info`: Включать ли информацию об исключении (по умолчанию `False`).
        *   `color`: Кортеж с цветами текста и фона (опционально).
    *   **Возвращает**: Ничего.
    *   **Назначение**: Логирует сообщение с указанным уровнем, добавляя цветное форматирование (если задано) и обрабатывая исключения.
    *   **Пример**:
    ```python
        logger.log(logging.INFO, "This is a log message")
    ```
    *   **Цепочка**: Вызывается методами `info`, `success`, `warning`, `debug`, `error`, `critical` для записи логов.

**Переменные:**

*   `_instances` в `SingletonMeta`: Словарь для хранения экземпляров классов (часть реализации Singleton).
*   `info_logger`, `debug_logger`, `error_logger`, `json_logger` в `Logger`: Атрибуты, хранящие настроенные экземпляры `logging.Logger`.

**Потенциальные ошибки и улучшения:**

*   **Обработка исключений**: В методе `log` можно добавить более детальную обработку исключений, чтобы логировать трассировку стека в правильном формате.
*   **Форматирование консольного вывода**: При использовании цветов можно добавить проверку на поддержку цветного вывода терминалом.
*   **Расширение функциональности**: Можно добавить поддержку других типов обработчиков (например, отправка логов по сети).
*   **Конфигурация из файла**: Загрузка конфигурации логгеров (пути, уровни) из конфигурационного файла.

**Взаимосвязь с другими частями проекта:**

*   Модуль `src.logger` может использоваться любым модулем в проекте `hypotez` для логирования событий.
*   Используется конфигурация, хранящая пути к файлам логов.
*   Зависит от `colorama` для цветного вывода в консоль.