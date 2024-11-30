# Документация модуля `src.logger`

## <input code>

```
### Documentation for the `src.logger` Module

The `src.logger` module provides a flexible logging system that supports console, file, and JSON logging. It utilizes the Singleton design pattern to ensure only a single instance of the logger is used across the application. The logger supports various log levels (e.g., `INFO`, `ERROR`, `DEBUG`) and includes colorized output for console logs. You can also customize the log output formats and control logging to different files.

---

### Classes:
- **SingletonMeta**: Metaclass that implements the Singleton design pattern for the logger.
- **JsonFormatter**: A custom formatter that outputs logs in JSON format.
- **Logger**: The main logger class that supports console, file, and JSON logging.

---

### Functions:

#### `__init__`
Initializes the Logger instance with placeholders for different logger types (console, file, and JSON).

#### `_configure_logger(name: str, log_path: str, level: Optional[int] = logging.DEBUG, formatter: Optional[logging.Formatter] = None, mode: Optional[str] = 'a') -> logging.Logger`
Configures and returns a logger instance.

**Parameters:**
- `name`: Name of the logger.
- `log_path`: Path to the log file.
- `level`: Logging level, e.g., `logging.DEBUG`. Default is `logging.DEBUG`.
- `formatter`: Custom formatter (optional).
- `mode`: File mode, e.g., `'a'` for append (default).

**Returns**: Configured `logging.Logger` instance.

#### `initialize_loggers(info_log_path: Optional[str] = '', debug_log_path: Optional[str] = '', errors_log_path: Optional[str] = '', json_log_path: Optional[str] = '')`
Initializes the loggers for console and file logging (info, debug, error, and JSON).

**Parameters:**
- `info_log_path`: Path for info log file (optional).
- `debug_log_path`: Path for debug log file (optional).
- `errors_log_path`: Path for error log file (optional).
- `json_log_path`: Path for JSON log file (optional).

#### `log(level, message, ex=None, exc_info=False, color=None)`
Logs a message at the specified level (e.g., `INFO`, `DEBUG`, `ERROR`) with optional exception and color formatting.

**Parameters:**
- `level`: Logging level (e.g., `logging.INFO`, `logging.DEBUG`).
- `message`: The log message.
- `ex`: Optional exception to log.
- `exc_info`: Whether to include exception information (default is `False`).
- `color`: Tuple with text and background colors for console output (optional).

#### `info(message, ex=None, exc_info=False, colors: Optional[tuple] = None)`
Logs an info message.

... (other functions)

---

### Parameters for the Logger
The `Logger` class accepts several optional parameters for customizing the logging behavior.

---

### File Logging Configuration (`config`)

```python
config = {
    'info_log_path': 'logs/info.log',
    'debug_log_path': 'logs/debug.log',
    'errors_log_path': 'logs/errors.log',
    'json_log_path': 'logs/log.json'
}
```

---

### Example Usage
... (example code)
```

```

## <algorithm>

(Блок-схема отсутствует, так как это описание кода, а не алгоритм с конкретными данными.)


## <mermaid>

```mermaid
graph LR
    subgraph "src.logger"
        Logger --> SingletonMeta
        Logger --> JsonFormatter
        Logger --> _configure_logger
        Logger --> initialize_loggers
        Logger --> log
        Logger --> info
        Logger --> success
        Logger --> warning
        Logger --> debug
        Logger --> error
        Logger --> critical
    end
    subgraph "Python's logging module"
        _configure_logger --> logging.Logger
        log --> logging.Logger
    end
    subgraph "colorama"
        Logger --> colorama
    end

```

## <explanation>

**Импорты:**

Модуль `src.logger` скорее всего использует стандартный модуль `logging` для основной функциональности ведения журнала. `colorama` — это внешняя библиотека, используемая для цветного вывода в консоль.  Отсутствуют явные импорты других частей проекта (`src.`), но присутствует неявно использование (`logging`).


**Классы:**

* **`SingletonMeta`**:  Реализует паттерн Singleton, гарантируя, что класс `Logger` будет иметь только один экземпляр.
* **`JsonFormatter`**:  Настраивает форматирование журнальных сообщений в формате JSON.
* **`Logger`**:  Основной класс для ведения журнала. Он содержит методы для записи сообщений в консоль, файлы и JSON.  Взаимодействует с внешними модулями, такими как `logging`, и `colorama`, для достижения своих функций.


**Функции:**

* **`__init__`**: Инициализирует экземпляр класса `Logger`.  Принимает аргументы (пути к файлам логов) и сохраняет их для дальнейшего использования.
* **`_configure_logger`**: Настраивает экземпляр логгера `logging.Logger` с указанным именем, путём к файлу, уровнем логгирования, форматированием и режимом записи. Это важная функция, которая конфигурирует логгер.
* **`initialize_loggers`**:  Инициализирует логгеры для различных уровней логов (INFO, DEBUG, ERROR, JSON) используя пути из словаря `config`. Настраивает логгер для записи в файлы и в консоль.
* **`log` (и другие методы info, success, warning, etc.)**: Записывают сообщения в журнал на соответствующих уровнях.  Используют аргументы для настройки уровня важности, сообщения, исключений (если есть) и форматирования. Присутствует параметр `color` для настройки цвета вывода в консоли.


**Переменные:**

Переменные типа `str` хранят пути к файлам для логов.  Переменные `config` — это словарь, который хранит пути к файлам.  Переменные уровня логгирования ( `logging.INFO`, `logging.DEBUG` и т.д.) используются для выбора уровня записываемых сообщений.


**Возможные ошибки и улучшения:**

* **Неявная зависимость от `logging`:** Не указан явный импорт модуля `logging`, но код предполагает его использование. Должен быть явный импорт для лучшей читаемости и поддержки.
* **Обработка ошибок:**  Отсутствует явная обработка ошибок при работе с файлами.  В реальных приложениях нужно добавлять обработку исключений (например, `try...except` блоков), чтобы приложение не аварийно завершалось при проблемах с файлами.
* **Достаточно общая документация.**  Документация содержит много деталей, но можно добавить примеров с реальными данными.
* **Должен быть явный импорт `colorama`:** Это гарантирует, что код будет работать в других средах, а не только там, где colorama установлена по умолчанию.
* **Управление ресурсами:** Если в логге будет производиться очень много операций ввода-вывода, нужно следить за утечками ресурсов.

**Взаимосвязи с другими частями проекта:**

Модуль `src.logger` используется другими частями приложения для записи сообщений о происходящих событиях. Это указывает на связь с другими модулями приложения.  Очевидно, что этот модуль должен использоваться другими частями приложения, которые нуждаются в возможности логгирования.