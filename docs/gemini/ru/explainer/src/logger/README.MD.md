## <алгоритм>

**1. Инициализация логгера:**

   - Создается экземпляр класса `Logger`.
   - Вызывается метод `initialize_loggers` с параметрами путей к файлам логов (`info_log_path`, `debug_log_path`, `errors_log_path`, `json_log_path`).
   - Внутри `initialize_loggers` вызывается `_configure_logger` для каждого типа логгера (консоль, info, debug, error, json), создавая отдельные логгеры `logging.Logger`.

   *Пример:*
   ```python
   logger: Logger = Logger()
   config = {
       'info_log_path': 'logs/info.log',
       'debug_log_path': 'logs/debug.log',
       'errors_log_path': 'logs/errors.log',
       'json_log_path': 'logs/log.json'
   }
   logger.initialize_loggers(**config)
   ```
   *Данные*: Передаются пути к файлам логов.
   *Результат*: Создаются и настраиваются отдельные логгеры.

**2. Конфигурация логгера:**

   - Функция `_configure_logger` получает имя логгера, путь к файлу лога, уровень логгирования, форматтер и режим открытия файла.
   - Создается объект `logging.Logger` с указанным именем.
   - Создается обработчик (handler) в зависимости от типа логгера (консоль, файл).
   - К обработчику добавляется форматер (по умолчанию или JSON).
   - Устанавливается уровень логгирования.
   - Обработчик добавляется к логгеру.
   - Возвращается настроенный логгер.

   *Пример:*
   ```python
   def _configure_logger(name, log_path, level=logging.DEBUG, formatter=None, mode='a'):
        logger = logging.getLogger(name)
        handler = logging.FileHandler(log_path, mode=mode) if log_path else logging.StreamHandler()
        formatter = formatter or logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.setLevel(level)
        logger.addHandler(handler)
        return logger
   ```
   *Данные*: Имя логгера, путь к файлу, уровень логирования, форматер.
   *Результат*: Возвращает настроенный объект `logging.Logger`.

**3. Логгирование сообщений:**

   - Вызывается метод `log` с уровнем, сообщением, опциональным исключением, флагом `exc_info` и цветом.
   - В зависимости от уровня сообщения вызывается метод соответствующего уровня (`info`, `debug`, `error`, `critical` и т.д.).
   - Метод вызывает `log`, который добавляет цветное форматирование (если указано) и передает сообщение в соответствующие логгеры.
   - Каждый логгер (консоль, файл) обрабатывает сообщение в соответствии со своей конфигурацией (уровень, формат).

   *Пример:*
   ```python
    def log(self, level, message, ex=None, exc_info=False, color=None):
        if color:
            message = f"{color[0]}{color[1]}{message}{colorama.Style.RESET_ALL}"
        for logger in self._loggers.values():
            logger.log(level, message, exc_info=exc_info)
        if ex:
            for logger in self._loggers.values():
               logger.exception(ex)
   ```
   *Данные*: Уровень логирования, сообщение, опциональное исключение, информация об исключении, цвета.
   *Результат*: Сообщение записывается в лог в соответствии с уровнем и настройками.

**4. Цветное форматирование:**

   - Если при вызове `log` указан параметр `color`, сообщение оборачивается в escape-последовательности `colorama` для добавления цветов.
   - Это работает только для консольного вывода.

   *Пример:*
   ```python
   logger.info('This message will be green', colors=(colorama.Fore.GREEN, colorama.Back.BLACK))
   ```
   *Данные*: Цвета текста и фона (`colorama.Fore.GREEN`, `colorama.Back.BLACK`).
   *Результат*: Сообщение выводится в консоль с указанными цветами.

**Блок-схема (псевдокод):**

```
Start
  |
  v
Создать экземпляр Logger
  |
  v
Вызвать initialize_loggers(info_log_path, debug_log_path, errors_log_path, json_log_path)
  |
  v
  Для каждого типа логгера (info, debug, error, json)
  |  |
  |  v
  |  Вызвать _configure_logger(name, log_path, level, formatter, mode)
  |  |
  |  v
  |  Создать объект logging.Logger с именем
  |  |
  |  v
  |  Создать обработчик (FileHandler или StreamHandler)
  |  |
  |  v
  |  Установить форматер для обработчика
  |  |
  |  v
  |  Установить уровень логгирования
  |  |
  |  v
  |  Добавить обработчик к логгеру
  |  |
  |  v
  |  Сохранить настроенный логгер
  |
  v
Вызвать log(level, message, ex, exc_info, color)
  |
  v
  Если color указан, добавить к сообщению цвета
  |
  v
  Для каждого активного логгера
  |  |
  |  v
  |  Записать сообщение в лог
  |
  v
  Если ex указано, записать исключение
End
```

## <mermaid>

```mermaid
flowchart TD
    Start --> CreateLogger[Create Logger Instance]
    CreateLogger --> InitializeLoggers[Call initialize_loggers with log paths]
    InitializeLoggers --> ForEachLoggerType[For each logger type: info, debug, error, json]
    ForEachLoggerType --> ConfigureLogger[_configure_logger(name, log_path, level, formatter, mode)]
    ConfigureLogger --> CreateLoggerInstance[Create logging.Logger instance]
    ConfigureLogger --> CreateHandler[Create FileHandler or StreamHandler]
    CreateHandler --> SetFormatter[Set Formatter]
    SetFormatter --> SetLogLevel[Set Log Level]
    SetLogLevel --> AddHandlerToLogger[Add Handler to Logger]
    AddHandlerToLogger --> StoreLogger[Store Configured Logger]
    StoreLogger --> ForEachLoggerType
    ForEachLoggerType -- All loggers configured --> CallLog[Call log(level, message, ex, exc_info, color)]
    CallLog --> CheckColor[Check if color is specified]
    CheckColor -- Yes --> ApplyColorFormatting[Apply Color Formatting]
    CheckColor -- No --> SkipColorFormatting[Skip Color Formatting]
    ApplyColorFormatting --> LogMessageToAllLoggers[Log Message to All Loggers]
    SkipColorFormatting --> LogMessageToAllLoggers
    LogMessageToAllLoggers --> CheckException[Check if exception (ex) is specified]
    CheckException -- Yes --> LogExceptionToAllLoggers[Log Exception to All Loggers]
    CheckException -- No --> End
    LogExceptionToAllLoggers --> End
    
    
    classDef important fill:#f9f,stroke:#333,stroke-width:2px;
    class CreateLogger, InitializeLoggers, CallLog, ConfigureLogger important
```

```mermaid
flowchart TD
    Start --> Header[<code>header.py</code><br> Determine Project Root]

    Header --> ImportGlobalSettings[Import Global Settings: <br><code>from src import gs</code>]
     
    ImportGlobalSettings --> SetProjectSettings[Set Project Settings using <br> <code>gs</code>]

    SetProjectSettings --> Finish[Finish]
    
    classDef important fill:#f9f,stroke:#333,stroke-width:2px;
    class Header, ImportGlobalSettings, SetProjectSettings important
```

**Объяснение:**

1. **`Start`**: Начало процесса.
2.  **`CreateLogger`**: Создается экземпляр класса `Logger`, который является точкой входа в систему логирования.
3.  **`InitializeLoggers`**: Вызывается метод `initialize_loggers`, который принимает пути к файлам логов. Он инициирует настройку каждого отдельного логгера (console, info, debug, error, json).
4.  **`ForEachLoggerType`**: Цикл, который проходит по каждому типу логгера.
5.  **`ConfigureLogger`**: Вызывается функция `_configure_logger`, которая выполняет настройку конкретного логгера. Она принимает имя логгера, путь к файлу, уровень логирования, форматер и режим открытия файла.
6. **`CreateLoggerInstance`**: Внутри `_configure_logger` создается объект `logging.Logger` с указанным именем.
7. **`CreateHandler`**: Создается обработчик, который отвечает за запись логов (в файл или в консоль).
8. **`SetFormatter`**: К обработчику добавляется форматер, который определяет формат сообщения лога.
9. **`SetLogLevel`**: Устанавливается уровень логирования для данного логгера.
10. **`AddHandlerToLogger`**: Обработчик добавляется к логгеру.
11. **`StoreLogger`**: Настроенный логгер сохраняется для дальнейшего использования.
12.  **`CallLog`**: Вызывается метод `log` для записи сообщения. Метод принимает уровень логирования, сообщение, опциональное исключение, флаг `exc_info`, а также цвет для вывода в консоль.
13.  **`CheckColor`**: Проверяется, указан ли цвет для форматирования вывода в консоль.
14. **`ApplyColorFormatting`**: Если цвет указан, то добавляется цветное форматирование к сообщению.
15. **`SkipColorFormatting`**: Если цвет не указан, то сообщение не форматируется.
16.  **`LogMessageToAllLoggers`**: Сообщение отправляется во все настроенные логгеры для записи.
17. **`CheckException`**: Проверяется, было ли передано исключение.
18. **`LogExceptionToAllLoggers`**: Если исключение было передано, то информация о нём записывается в лог.
19. **`End`**: Конец процесса логирования.

**Зависимости:**

-   `logging`: Встроенный модуль Python для логирования.
-   `colorama`: Модуль для работы с цветом в консоли.

## <объяснение>

### Импорты:

-   **`logging`**:
    -   Это встроенный модуль Python, предоставляющий гибкую структуру для логирования событий, происходящих в приложении.
    -   `logging` позволяет записывать информацию в разные места (консоль, файлы) с разными уровнями детализации (DEBUG, INFO, WARNING, ERROR, CRITICAL).
    -   Этот модуль используется для создания объектов логгеров, установки уровней логирования, добавления обработчиков и форматирования сообщений.
-   **`colorama`**:
    -   Это сторонний модуль, который используется для добавления цветов в консольный вывод.
    -   `colorama` предоставляет константы для задания цветов текста (`Fore`) и фона (`Back`), а также для сброса стилей (`Style.RESET_ALL`).
    -   В `src.logger` модуль используется для раскрашивания сообщений в консоли в зависимости от уровня логирования или пользовательских настроек.

### Классы:

-   **`SingletonMeta`**:
    -   Это метакласс, реализующий шаблон проектирования Singleton.
    -   Он гарантирует, что класс `Logger` будет иметь только один экземпляр.
    -   Метод `__call__` переопределяется, чтобы при каждом вызове возвращать один и тот же экземпляр класса.
-   **`JsonFormatter`**:
    -   Это класс, наследуемый от `logging.Formatter`, который переопределяет метод `format` для формирования сообщений лога в формате JSON.
    -   Он преобразует сообщение лога в словарь и преобразует его в строку JSON.
    -   Используется для записи логов в файл в формате JSON.
-   **`Logger`**:
    -   Это основной класс логгера. Он использует метакласс `SingletonMeta`, чтобы обеспечить создание только одного экземпляра.
    -   Он содержит методы для инициализации логгеров (`initialize_loggers`), настройки (`_configure_logger`), и записи сообщений (`log`, `info`, `debug`, `error` и т.д.).
    -   Он хранит все созданные логгеры в словаре `_loggers`, где ключом является имя логгера.

### Функции:

-   **`__init__`**:
    -   Конструктор класса `Logger`. Он инициализирует словарь `_loggers`, в котором будут храниться все созданные логгеры.
-   **`_configure_logger(name, log_path, level=logging.DEBUG, formatter=None, mode='a')`**:
    -   Создает и настраивает объект `logging.Logger`.
    -   Принимает имя логгера, путь к файлу, уровень логирования, форматтер и режим открытия файла в качестве аргументов.
    -   Создает обработчик (`FileHandler` или `StreamHandler`) для записи логов в файл или консоль.
    -   Устанавливает форматтер для обработчика.
    -   Устанавливает уровень логирования.
    -   Возвращает сконфигурированный объект `logging.Logger`.
-   **`initialize_loggers(info_log_path='', debug_log_path='', errors_log_path='', json_log_path='')`**:
    -   Инициализирует все логгеры, вызывая `_configure_logger` для каждого из них (консоль, info, debug, error, json).
    -   Принимает пути к файлам логов для каждого типа.
    -   Создает и сохраняет логгеры в словаре `_loggers`.
-   **`log(level, message, ex=None, exc_info=False, color=None)`**:
    -   Записывает сообщение лога на указанном уровне.
    -   Принимает уровень логирования, сообщение, опциональное исключение, флаг `exc_info`, а также цвет для вывода в консоль.
    -   Добавляет цветное форматирование, если указано, и передает сообщение в соответствующие логгеры.
-   **`info(message, ex=None, exc_info=False, colors=None)`**, **`success(message, ex=None, exc_info=False, colors=None)`**, **`warning(message, ex=None, exc_info=False, colors=None)`**, **`debug(message, ex=None, exc_info=True, colors=None)`**, **`error(message, ex=None, exc_info=True, colors=None)`**, **`critical(message, ex=None, exc_info=True, colors=None)`**:
    -   Это вспомогательные методы для вызова `log` с разными уровнями логирования.
    -   Они предоставляют более удобный интерфейс для записи сообщений разных типов.

### Переменные:

-   **`_loggers`**:
    -   Словарь, в котором хранятся все созданные объекты `logging.Logger`.
    -   Ключами словаря являются имена логгеров (`console`, `info`, `debug`, `error`, `json`).

### Потенциальные ошибки и улучшения:

1.  **Отсутствие обработки исключений:** При создании `FileHandler` в `_configure_logger` не обрабатываются возможные исключения (`FileNotFoundError`, `PermissionError`).
2.  **Жестко заданные имена логгеров:** Имена логгеров (`console`, `info`, `debug`, `error`, `json`) жестко заданы в `initialize_loggers`.
3.  **Отсутствие проверки путей:** Пути к файлам не проверяются на существование.
4.  **Возможная потеря сообщений:** Если при создании FileHandler возникнет исключение, то сообщение не запишется.

**Взаимосвязь с другими частями проекта:**

-   Модуль `src.logger` является частью пакета `src` и может использоваться другими модулями проекта для логирования различных событий.
-   Конфигурация путей к файлам логов может храниться в файле конфигурации проекта, а не задаваться жестко в коде.
-   `src.logger` может зависеть от `src.header`, чтобы определить корневую директорию проекта, где будут храниться логи.

**Дополнительно:**

-   Можно добавить возможность настраивать форматы логов (например, добавлять время, имя файла, номер строки).
-   Можно добавить возможность настраивать уровни логирования через конфигурационный файл.
-   Вместо использования `colorama` можно использовать более продвинутые библиотеки для работы с терминалом.
-   Можно добавить поддержку ротации лог-файлов (для предотвращения их чрезмерного роста).