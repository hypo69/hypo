## ИНСТРУКЦИЯ:

Анализируй предоставленный код подробно и объясни его функциональность. Ответ должен включать три раздела:  

1. **<алгоритм>**: Опиши рабочий процесс в виде пошаговой блок-схемы, включая примеры для каждого логического блока, и проиллюстрируй поток данных между функциями, классами или методами.  
2. **<mermaid>**: Напиши код для диаграммы в формате `mermaid`, проанализируй и объясни все зависимости, 
    которые импортируются при создании диаграммы. 
    **ВАЖНО!** Убедитесь, что все имена переменных, используемые в диаграмме `mermaid`, 
    имеют осмысленные и описательные имена. Имена переменных вроде `A`, `B`, `C`, и т.д., не допускаются!  
    
    **Дополнительно**: Если в коде есть импорт `import header`, добавьте блок `mermaid` flowchart, объясняющий `header.py`:\
    ```mermaid\
    flowchart TD\
        Start --> Header[<code>header.py</code><br> Determine Project Root]\
    \
        Header --> import[Import Global Settings: <br><code>from src import gs</code>] \
    ```

3. **<объяснение>**: Предоставьте подробные объяснения:  
   - **Импорты**: Их назначение и взаимосвязь с другими пакетами `src.`.  
   - **Классы**: Их роль, атрибуты, методы и взаимодействие с другими компонентами проекта.  
   - **Функции**: Их аргументы, возвращаемые значения, назначение и примеры.  
   - **Переменные**: Их типы и использование.  
   - Выделите потенциальные ошибки или области для улучшения.  

Дополнительно, постройте цепочку взаимосвязей с другими частями проекта (если применимо).  

Это обеспечивает всесторонний и структурированный анализ кода.
## Формат ответа: `.md` (markdown)
**КОНЕЦ ИНСТРУКЦИИ**

## <алгоритм>

**1. Инициализация логгера:**

   - **Запуск**: При первом обращении к классу `Logger` (через `logger: Logger = Logger()`), метакласс `SingletonMeta` обеспечивает создание только одного экземпляра класса.
   - **Конфигурация**: 
      - Читается конфигурация из файла `config.json` (путь формируется на основе `__root__` из `header.py`).
      - Формируется путь для хранения логов на основе текущей даты и времени.
      - Создаются директории для хранения логов, если они не существуют.
      - Создаются файлы для логов (info, debug, errors, json), если они не существуют.
   - **Настройка логгеров**:
      - Создаются четыре логгера:
         - `logger_console` (вывод в консоль).
         - `logger_file_info` (запись INFO-сообщений в файл).
         - `logger_file_debug` (запись DEBUG-сообщений в файл).
         - `logger_file_errors` (запись ERROR/CRITICAL сообщений в файл).
         - `logger_file_json` (запись всех сообщений в формате JSON).
      - Настраиваются обработчики для каждого логгера, форматирование сообщений.
      - Для JSON-логгера используется кастомный форматтер `JsonFormatter`.
      - Удаляются все StreamHandler (чтобы избежать двойной записи в консоль).
   
**Пример:**
  ```python
  # Предположим, что config.json содержит: {"path": {"log": "logs"}}
  # И текущая дата и время 10:30 16.05.2024
  logger = Logger() # Создается экземпляр логгера
  # В результате:
  # Путь к файлам логов: /<project_root>/logs/1605241030
  # Файлы: info.log, debug.log, errors.log в папке /logs/1605241030 и 1605241030.json в папке /logs
  ```

**2. Форматирование сообщений:**

   - **Функция `_format_message`**:
      - Принимает сообщение, опциональные цвета текста и фона.
      - Если цвета указаны, форматирует сообщение с использованием кодов `colorama`.
      - Если цвета не указаны, возвращает сообщение без изменений.
   - **Функция `_ex_full_info`**:
      - Извлекает информацию о месте вызова функции (`файл`, `функция`, `номер строки`).
      - Формирует строку с деталями исключения.
**Пример:**
   ```python
   logger._format_message("Test message", color=("red", "white"))
    # => "\x1b[31m\x1b[47mTest message \x1b[0m"
   logger._ex_full_info(Exception("Some error")) 
  # => "\nFile: <filename>, \n |\n  -Function: <function_name>, \n   |\n    --Line: <line_number>\nSome error"
  ```
**3. Запись логов:**

   - **Функция `log`**:
      - Принимает уровень лога (`logging.INFO`, `logging.DEBUG`, `logging.ERROR` и др.), сообщение, опциональное исключение, флаг `exc_info` и опциональные цвета.
      - Форматирует сообщение с помощью `_format_message`.
      - Если `exc_info` истинно, добавляет полную информацию об исключении с помощью `_ex_full_info`.
      - Записывает сообщение в консольный логгер.
   - **Функции `info`, `success`, `warning`, `debug`, `error`, `critical`**:
      - Вызывают функцию `log` с соответствующим уровнем логирования и опциональными цветами по умолчанию.
**Пример:**
```python
logger.info("Information message", text_color="blue") 
# Выведет "Information message" синим цветом в консоль и запишет в info.log
logger.debug("Debug message", exc_info=True, ex=Exception("Debug error"))
# Выведет "Debug message" синим цветом в консоль с информацией об исключении и запишет в debug.log
```
**4. Взаимодействие**:
   - `header.py` -> `logger.py` : `header.py` определяет корень проекта, который используется для определения путей к файлам логов.
   - `config.json` -> `logger.py` : `logger.py` читает `config.json` для определения пути к логам.
   - `logger.py` -> `logging` : `logger.py` использует модуль `logging` для создания логгеров и записи логов.

## <mermaid>

```mermaid
flowchart TD
    Start[Start] --> LoggerInit[Logger Initialization]
    LoggerInit --> ReadConfig[Read config.json]
    ReadConfig --> CreateLogPaths[Create log file paths]
    CreateLogPaths --> EnsureDirsAndFiles[Ensure log directories and files exist]
    EnsureDirsAndFiles --> CreateLoggers[Create loggers (console, info, debug, errors, json)]
    CreateLoggers --> SetLoggerLevels[Set log levels for each logger]
    SetLoggerLevels --> CreateHandlers[Create handlers for each logger]
    CreateHandlers --> SetFormatters[Set formatters for each handler]
    SetFormatters --> RemoveConsoleHandlers[Remove console handlers from json logger]
    RemoveConsoleHandlers --> EndInit[End of Logger Initialization]
    
    LogMessage[Log Message] --> FormatMessage[Format Message with color (if provided)]
    FormatMessage --> FullExceptionInfo[Get full exception information (if needed)]
    FullExceptionInfo --> LogToConsole[Log to console]
    LogToConsole --> EndLog[End Log Message]
    
    subgraph SingletonMeta
    direction TB
        SingletonStart[Singleton Entry] --> CheckInstance[Check if instance exists]
        CheckInstance -- Yes --> ReturnInstance[Return existing instance]
        CheckInstance -- No --> AcquireLock[Acquire lock]
        AcquireLock --> CheckInstanceAgain[Check if instance exists again]
        CheckInstanceAgain -- Yes --> ReleaseLock[Release lock]
        ReleaseLock --> ReturnInstanceAgain[Return existing instance]
        CheckInstanceAgain -- No --> CreateInstance[Create new instance]
        CreateInstance --> StoreInstance[Store new instance]
        StoreInstance --> ReleaseLockAgain[Release lock]
        ReleaseLockAgain --> ReturnNewInstance[Return new instance]
        ReturnInstanceAgain --> SingletonEnd[Singleton End]
        ReturnNewInstance --> SingletonEnd
    end
    
    Start --> SingletonStart
    EndInit --> EndInit
    EndLog --> EndLog
    SingletonEnd --> LoggerInit
    
    subgraph header.py
    direction TB
        HeaderStart[Start] --> DetermineRoot[Determine Project Root]
        DetermineRoot --> ImportGS[Import Global Settings: <br><code>from src import gs</code>] 
        ImportGS --> HeaderEnd[End]
    end
```

### Анализ зависимостей `mermaid`:
-   `Start` - начало выполнения кода
-   `LoggerInit` - блок инициализации логгера.
-   `ReadConfig` - чтение файла конфигурации `config.json`.
-   `CreateLogPaths` - формирование путей к файлам логов на основе конфигурации.
-   `EnsureDirsAndFiles` - создание папок и файлов для логов.
-   `CreateLoggers` - создание объектов логгеров.
-   `SetLoggerLevels` - установка уровней логирования для логгеров.
-   `CreateHandlers` - создание обработчиков логгирования.
-   `SetFormatters` - установка форматтеров для сообщений логгирования.
-   `RemoveConsoleHandlers` - удаление обработчиков консоли для json-логгера.
-   `EndInit` - конец инициализации логгера.
-   `LogMessage` - начало записи сообщения лога.
-   `FormatMessage` - форматирование сообщения, включая цвета.
-   `FullExceptionInfo` - получение полной информации об исключении.
-   `LogToConsole` - запись сообщения в консоль.
-   `EndLog` - конец записи сообщения лога.
-   `SingletonMeta` -  метакласс для реализации паттерна `Singleton`, гарантирующий, что существует только один экземпляр класса `Logger`
-   `SingletonStart` - начало работы метакласса
-   `CheckInstance` - проверка, существует ли уже экземпляр класса
-   `ReturnInstance` - возврат существующего экземпляра
-   `AcquireLock` - получение блокировки для потокобезопасного создания экземпляра
-   `CheckInstanceAgain` - повторная проверка существования экземпляра внутри блокировки
-   `ReleaseLock` - освобождение блокировки
-   `ReturnInstanceAgain` - возврат существующего экземпляра после блокировки
-   `CreateInstance` - создание нового экземпляра
-   `StoreInstance` - сохранение экземпляра
-   `ReleaseLockAgain` - повторное освобождение блокировки после создания экземпляра
-   `ReturnNewInstance` - возврат нового экземпляра
-   `SingletonEnd` - конец работы метакласса
-  `header.py` - блок определяющий корень проекта

## <объяснение>

### Импорты:
-   `logging`: Стандартный модуль Python для ведения логов.
-   `colorama`: Библиотека для добавления цветов в вывод консоли.
-   `datetime`: Модуль для работы с датой и временем, используется для создания уникальных имен папок с логами.
-   `json`: Модуль для работы с данными в формате JSON, используется для логгирования в JSON-файл.
-   `inspect`: Модуль для интроспекции, используется для получения информации о месте вызова функции.
-   `threading`: Модуль для поддержки потоков, используется для реализации потокобезопасного синглтона.
-   `pathlib.Path`: Модуль для работы с путями к файлам и директориям.
-   `typing.Optional, Tuple`: Модуль для аннотации типов.
-   `types.SimpleNamespace`: Модуль для создания объекта с атрибутами из словаря, используется для хранения конфигурации.
-   `header`: Самописный модуль, определяющий корень проекта.

### Классы:
-   **`SingletonMeta` (метакласс):**
    -   Реализует паттерн Singleton, гарантирует, что у класса `Logger` будет только один экземпляр.
    -   `_instances`: Словарь для хранения созданных экземпляров класса.
    -   `_lock`: Объект блокировки для обеспечения потокобезопасности при создании экземпляра.
    -   Метод `__call__` перехватывает вызов класса и либо возвращает существующий экземпляр, либо создает новый (при первом вызове).

-   **`JsonFormatter` (наследуется от `logging.Formatter`):**
    -   Класс для форматирования логов в формате JSON.
    -   Метод `format` преобразует запись лога в JSON-формат с полями `asctime`, `levelname`, `message`, `exc_info`.

-   **`Logger` (с метаклассом `SingletonMeta`):**
    -   Основной класс логгера, реализует логику записи логов в консоль, файлы, и JSON.
    -   Атрибуты: `log_files_path`, `info_log_path`, `debug_log_path`, `errors_log_path`, `json_log_path` (пути к файлам логов).
    -   Метод `__init__`: Инициализирует логгер, создает пути для логов, создает логгеры, настраивает обработчики.
    -   Метод `_format_message`: Форматирует сообщение, добавляет цвета (если указаны).
    -   Метод `_ex_full_info`: Формирует строку с информацией об исключении, включая место вызова функции.
    -   Метод `log`: Записывает сообщение в логгер нужного уровня с форматированием и возможностью добавления исключения.
    -   Методы `info`, `success`, `warning`, `debug`, `error`, `critical`: Вызывают метод `log` с предопределенными уровнями логов и цветами.

### Функции:
-   `SingletonMeta.__call__(cls, *args, **kwargs)`:  Обеспечивает создание единственного экземпляра класса.
-   `JsonFormatter.format(self, record)`: Форматирует запись лога в JSON.
-   `Logger.__init__(self, info_log_path=None, debug_log_path=None, errors_log_path=None, json_log_path=None)`: Инициализирует экземпляр логгера, создает пути, папки и файлы. Настраивает логгеры, обработчики и форматтеры.
-  `Logger._format_message(self, message, ex=None, color=None)`:  Форматирует сообщение, добавляя цвета и информацию об исключении.
-   `Logger._ex_full_info(self, ex)`: Извлекает и форматирует информацию об исключении.
-   `Logger.log(self, level, message, ex=None, exc_info=False, color=None)`: Общая функция для записи лога.
-   `Logger.info(self, message, ex=None, exc_info=False, text_color="green", bg_color="")`, `Logger.success(self, message, ex=None, exc_info=False, text_color="yellow", bg_color="")`, `Logger.warning(self, message, ex=None, exc_info=False, text_color="black", bg_color="yellow")`, `Logger.debug(self, message, ex=None, exc_info=True, text_color="cyan", bg_color="")`, `Logger.error(self, message, ex=None, exc_info=True, text_color="red", bg_color="")`, `Logger.critical(self, message, ex=None, exc_info=True, text_color="red", bg_color="white")`:  Функции для записи логов с предопределенным уровнем и цветом.

### Переменные:
-   `TEXT_COLORS`, `BG_COLORS`:  Словари с кодами цветов для текста и фона.
-   `__root__`: Переменная, импортированная из `header.py`, содержащая корень проекта.
-  `config` :  Объект `SimpleNamespace`, содержащий конфигурацию проекта из `config.json`.
-   `timestamp`: Строка, содержащая текущую дату и время для создания уникальных путей к файлам.
-   `log_files_path`, `info_log_path`, `debug_log_path`, `errors_log_path`, `json_log_path`: Переменные типа `Path` для хранения путей к файлам логов.
-   `logger_console`, `logger_file_info`, `logger_file_debug`, `logger_file_errors`, `logger_file_json`: Экземпляры логгеров из модуля `logging`.

### Цепочка взаимосвязей:
1.  `header.py` определяет корень проекта (`__root__`).
2.  `logger.py` импортирует `__root__` из `header.py`.
3.  `logger.py` использует `__root__` для чтения файла `config.json`.
4.  `logger.py` создает пути к лог-файлам на основе данных из `config.json` и текущей даты и времени.
5.  `logger.py` использует модуль `logging` для создания логгеров, настройки обработчиков и форматирования сообщений.
6.  `logger.py` использует `colorama` для добавления цветов в консольный вывод.
7. `logger.py` использует метакласс `SingletonMeta` для обеспечения единственного экземпляра класса `Logger`.

### Потенциальные ошибки и улучшения:
-   **Двойной вывод в консоль (исправлено)**: Изначально логи могли дублироваться, выводясь и в консоль, и в файл.  Это было исправлено путем удаления всех StreamHandler из JSON логгера.
-   **Жестко закодированные пути к файлам**: Пути к лог-файлам относительно конфигурации.
-   **Отсутствие ротации логов**: Файлы логов не ротируются, что может привести к их разрастанию.
-   **Использование `inspect.stack()[3]`**: Зависимость от конкретного уровня стека вызова может привести к ошибке, если функция `log` будет вызываться с другого уровня.
-   **Недостаточная гибкость**: Логика форматирования сообщений может быть расширена для поддержки дополнительных параметров.
-  **Улучшение обработки исключений**: Можно добавить более подробное логирование исключений, включая трассировку стека.

### Дополнительно:
 -  Можно добавить автоматическую очистку старых логов, чтобы не переполнять дисковое пространство.
 - Рассмотреть возможность использования сторонней библиотеки для управления логами (например, `loguru`).
- Можно вынести все настройки форматера в config.json.
- Рассмотреть возможность использования сторонней библиотеки для  управления цветами и стилями (например, `rich`).