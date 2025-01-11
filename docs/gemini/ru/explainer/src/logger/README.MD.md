## <алгоритм>

1. **Инициализация логгера:**
   - Создается экземпляр класса `Logger`.
   - Вызывается метод `initialize_loggers` с путями к файлам логов (info, debug, error, json).
     - **Пример:** `logger = Logger(); logger.initialize_loggers(info_log_path='logs/info.log', debug_log_path='logs/debug.log', errors_log_path='logs/errors.log', json_log_path='logs/log.json')`

2. **Конфигурация логгеров:**
   - Метод `initialize_loggers` вызывает метод `_configure_logger` для каждого типа логгера (console, info, debug, error, json).
   - `_configure_logger` создает и настраивает `logging.Logger` с заданным именем, путем к файлу, уровнем логирования, форматом и режимом записи.
     - **Пример:**
       - `_configure_logger(name='console', log_path=None, level=logging.DEBUG)`
       - `_configure_logger(name='info', log_path='logs/info.log', level=logging.INFO)`

3. **Логгирование сообщений:**
   - Вызываются методы `info`, `success`, `warning`, `debug`, `error`, `critical` для записи сообщений в лог.
     - **Пример:** `logger.info('Сообщение', ex=Exception("Error"), exc_info=True, colors=(colorama.Fore.GREEN, colorama.Back.BLACK))`
   - Каждый метод вызывает метод `log` с соответствующим уровнем логирования.
   - `log` записывает сообщение в консоль и в файлы, если они были сконфигурированы, используя соответствующие логгеры.
   - Если указаны цвета, сообщение выводится в консоль с применением указанных цветов.

4. **Обработка исключений:**
   - Методы логирования могут принимать исключения `ex` и флаг `exc_info`, для вывода дополнительной информации об исключении в лог.

## <mermaid>

```mermaid
flowchart TD
    subgraph Logger
        Start[Start]
        InitLogger[Logger Initialization]
        InitLoggers[initialize_loggers]
        ConfigLogger[_configure_logger]
        LogMessage[log(level, message, ex, exc_info, color)]
        Info[info(message, ex, exc_info, colors)]
        Success[success(message, ex, exc_info, colors)]
        Warning[warning(message, ex, exc_info, colors)]
        Debug[debug(message, ex, exc_info, colors)]
        Error[error(message, ex, exc_info, colors)]
        Critical[critical(message, ex, exc_info, colors)]
        End[End]

        Start --> InitLogger
        InitLogger --> InitLoggers
        InitLoggers --> ConfigLogger
        ConfigLogger --> InitLoggers
        InitLoggers --> LogMessage
        LogMessage --> End

        Info --> LogMessage
        Success --> LogMessage
        Warning --> LogMessage
        Debug --> LogMessage
        Error --> LogMessage
        Critical --> LogMessage
    end
    
    subgraph SingletonMeta
        StartMeta[Start Meta]
        CheckInstance[Check if instance exists]
        CreateInstance[Create new Instance]
        ReturnInstance[Return Instance]
    
        StartMeta --> CheckInstance
        CheckInstance -- Yes --> ReturnInstance
        CheckInstance -- No --> CreateInstance
        CreateInstance --> ReturnInstance
    end    
    
    style CheckInstance fill:#f9f,stroke:#333,stroke-width:2px
    
    
    linkStyle 0,1,2,3,4,5,6,7,8,9,10,11 stroke:#333,stroke-width:2px
```

**Анализ зависимостей `mermaid`:**

- **`Logger`:** Основной класс логгера, который управляет логированием сообщений.
  -  **`Start`**: Начало работы класса `Logger`.
  - **`InitLogger`**:  Инициализация экземпляра класса `Logger`.
  - **`InitLoggers`**: Метод `initialize_loggers` настраивает различные логгеры (консольный, файловый, json).
  - **`ConfigLogger`**: Метод `_configure_logger` создает и настраивает конкретные экземпляры логгеров (`logging.Logger`).
  - **`LogMessage`**: Метод `log` записывает сообщения в соответствующие логгеры.
  - **`Info`**, **`Success`**, **`Warning`**, **`Debug`**, **`Error`**, **`Critical`**: Методы для логирования сообщений разных уровней.
  - **`End`**: Завершение работы класса `Logger`.
- **`SingletonMeta`:** Метакласс, реализующий паттерн Singleton.
  - **`StartMeta`**: Начало работы метакласса.
  - **`CheckInstance`**: Проверка, существует ли уже экземпляр класса.
  - **`CreateInstance`**: Создание нового экземпляра, если он не существует.
  - **`ReturnInstance`**: Возвращение существующего или вновь созданного экземпляра.
   
  
## <объяснение>

### Импорты:

- `logging`: Стандартный модуль Python для логирования. Используется для создания и настройки логгеров, определения уровней логирования и форматирования сообщений.
- `typing.Optional`: Используется для указания, что аргумент функции может быть `None`.
- `colorama`:  Сторонняя библиотека для добавления цветового оформления в консольный вывод.
- `json`: Стандартный модуль Python для работы с JSON-форматом.

### Классы:

- **`SingletonMeta(type)`**: Метакласс, реализующий паттерн Singleton.
  - **Роль:** Гарантирует, что будет создан только один экземпляр класса `Logger`.
  - **Методы:**
    - `__call__`: Переопределяет оператор вызова, возвращает существующий экземпляр класса, если он существует, иначе создает новый.
- **`JsonFormatter(logging.Formatter)`**: Класс для форматирования сообщений лога в JSON.
  - **Роль:** Обеспечивает вывод логов в JSON-формате.
  - **Методы:**
    - `format(record)`: Преобразует запись лога в JSON-строку.
- **`Logger(metaclass=SingletonMeta)`**: Основной класс логгера.
  - **Роль:** Предоставляет интерфейс для записи логов в консоль, файлы и JSON.
  - **Атрибуты:**
    - `console_logger`:  Экземпляр `logging.Logger` для вывода в консоль.
    - `info_logger`, `debug_logger`, `errors_logger`: Экземпляры `logging.Logger` для записи в файлы.
    - `json_logger`: Экземпляр `logging.Logger` для записи в JSON-файл.
  - **Методы:**
     -  `__init__(self)`: Инициализирует атрибуты логгера как пустые (None).
     - `_configure_logger(self, name: str, log_path: str, level: Optional[int] = logging.DEBUG, formatter: Optional[logging.Formatter] = None, mode: Optional[str] = 'a') -> logging.Logger`: Конфигурирует и возвращает экземпляр `logging.Logger`.
     - `initialize_loggers(self, info_log_path: Optional[str] = '', debug_log_path: Optional[str] = '', errors_log_path: Optional[str] = '', json_log_path: Optional[str] = '')`: Настраивает логгеры, вызывает метод `_configure_logger` для каждого из них.
     - `log(self, level, message, ex=None, exc_info=False, color=None)`: Основной метод для записи сообщений лога.
     -  `info(self, message, ex=None, exc_info=False, colors: Optional[tuple] = None)`,  `success(self, message, ex=None, exc_info=False, colors: Optional[tuple] = None)`,  `warning(self, message, ex=None, exc_info=False, colors: Optional[tuple] = None)`,   `debug(self, message, ex=None, exc_info=True, colors: Optional[tuple] = None)`, `error(self, message, ex=None, exc_info=True, colors: Optional[tuple] = None)`, `critical(self, message, ex=None, exc_info=True, colors: Optional[tuple] = None)`: Вспомогательные методы для записи сообщений с определенным уровнем.

### Функции:

- `_configure_logger(...)`:
  - **Аргументы**:
    - `name`: Имя логгера (строка).
    - `log_path`: Путь к файлу лога (строка).
    - `level`: Уровень логирования (целое, например, `logging.DEBUG`). По умолчанию `logging.DEBUG`.
    - `formatter`: Пользовательский форматтер (экземпляр `logging.Formatter`). По умолчанию `None`.
    - `mode`: Режим открытия файла (строка, например, 'a' для добавления). По умолчанию 'a'.
  - **Возвращает**: Экземпляр `logging.Logger`.
  - **Назначение**: Создает и настраивает логгер с заданными параметрами. Если `log_path` не задан, создаётся логгер только для консоли. Устанавливает уровень логирования, форматтер и добавляет обработчик вывода в файл, если `log_path` не пустой.

- `initialize_loggers(...)`:
    -   **Аргументы**:
         - `info_log_path`: Путь к файлу для `INFO` логов (строка).
         -  `debug_log_path`: Путь к файлу для `DEBUG` логов (строка).
         -   `errors_log_path`: Путь к файлу для `ERROR` логов (строка).
         -   `json_log_path`: Путь к файлу для `JSON` логов (строка).
    -   **Возвращает**: Ничего (None).
    -   **Назначение**: Настраивает логгеры для консоли и файлов. Для каждого пути к файлу создает логгер с соответствующим уровнем, вызывая  `_configure_logger`.

- `log(...)`:
    -   **Аргументы**:
         -   `level`: Уровень логирования (например, `logging.INFO`).
         -  `message`: Сообщение для логирования (строка).
         -   `ex`: Исключение для логирования (опционально, экземпляр Exception).
         -    `exc_info`: Флаг для включения информации об исключении (логическое значение).
         -   `color`: Кортеж с цветами текста и фона (опционально).
    -    **Возвращает**: Ничего (None).
    -   **Назначение**: Записывает сообщение в лог, используя соответствующий логгер. Выводит сообщение в консоль и/или в файл, если они настроены.
-`info(self, message, ex=None, exc_info=False, colors: Optional[tuple] = None)`,  `success(self, message, ex=None, exc_info=False, colors: Optional[tuple] = None)`,  `warning(self, message, ex=None, exc_info=False, colors: Optional[tuple] = None)`,   `debug(self, message, ex=None, exc_info=True, colors: Optional[tuple] = None)`, `error(self, message, ex=None, exc_info=True, colors: Optional[tuple] = None)`, `critical(self, message, ex=None, exc_info=True, colors: Optional[tuple] = None)`:
    -   **Аргументы**:
         -   `message`: Сообщение для логирования (строка).
         -    `ex`: Исключение для логирования (опционально, экземпляр Exception).
         -   `exc_info`: Флаг для включения информации об исключении (логическое значение).
         -   `color`: Кортеж с цветами текста и фона (опционально).
    -    **Возвращает**: Ничего (None).
    -   **Назначение**: Методы-обертки над методом `log`, задают уровень логирования и вызывают `log`.

### Переменные:

- `logger`: Экземпляр класса `Logger`, используется для логирования сообщений.
- `config`: Словарь, содержащий пути к файлам логов.

### Потенциальные ошибки и области для улучшения:

1.  **Отсутствие обработки исключений при записи в файл:** В методе `log` нет обработки возможных исключений при записи в файл (например, `IOError`). Желательно добавить блоки `try-except` для обработки подобных ошибок.
2.  **Ограниченная настройка форматов:** Форматирование логов ограничено стандартным форматом `logging.Formatter` и пользовательским JSON-форматтером. Можно расширить возможности, добавив поддержку пользовательских форматов.
3.  **Улучшение настроек:**
    - Переменная `mode = 'a'` для записи в файл по умолчанию. Предоставить пользователю возможность настраивать это значение.
    - Настройка `logging.StreamHandler` для вывода в консоль. По умолчанию `logging.StreamHandler` выводит всё на `sys.stderr`, желательно дать возможность настроить вывод в `sys.stdout`.
4. **Необходимость явного импорта `colorama`:** Пользователь должен импортировать `colorama` в свой код.
5. **Зависимости:** `colorama` является внешней зависимостью, необходимо убедиться что все пользователи устанавливают её.

### Цепочка взаимосвязей с другими частями проекта:

- Модуль `src.logger` может использоваться в любой части проекта для записи логов.
- Связан с `src.gs`, который хранит общие настройки, включая настройки логгера, как указано в инструкции.
- Класс `SingletonMeta` обеспечивает, что все части проекта будут использовать один и тот же экземпляр логгера.