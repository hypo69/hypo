# Модуль logger

## Обзор

Модуль `logger` предоставляет утилиту для ведения журналов с использованием различных уровней и форматов логов, включая консоль, файлы и JSON. Модуль использует паттерн Singleton для обеспечения единственного экземпляра логгера в приложении. Поддерживает разные уровни логов и форматы вывода, включая цветную консольную информацию.

## Классы

### `SingletonMeta`

**Описание**: Метакласс для реализации паттерна Singleton.

**Методы**:

- `__call__`: Создает экземпляр класса только один раз.


### `JsonFormatter`

**Описание**: Пользовательский форматировщик для логов в формате JSON.

**Методы**:

- `format`: Форматирует запись лога в формате JSON.


### `Logger`

**Описание**: Класс-логгер, реализующий паттерн Singleton и поддерживающий логгирование в консоль, файлы и JSON.

**Атрибуты**:

- `logger_console`: Логгер для консоли.
- `logger_file_info`: Логгер для файла с информационными сообщениями.
- `logger_file_debug`: Логгер для файла с отладочными сообщениями.
- `logger_file_errors`: Логгер для файла с ошибками.
- `logger_file_json`: Логгер для файла с сообщениями в формате JSON.
- `_initialized`: Флаг, указывающий на инициализацию логгера.


**Методы**:

- `__init__`: Инициализирует экземпляр логгера.
- `_configure_logger`: Настраивает и возвращает логгер с заданными параметрами.
- `initialize_loggers`: Инициализирует логгеры для консоли, файлов и JSON.
- `_format_message`: Форматирует сообщение с необязательным цветом и информацией об исключении.
- `_ex_full_info`: Предоставляет подробную информацию об исключении, включая файл, функцию и номер строки, где был вызван лог.
- `log`: Записывает сообщения на указанном уровне с необязательными цветом и информацией об исключении.
- `info`: Записывает сообщение уровня `INFO`.
- `success`: Записывает сообщение уровня `INFO` с цветом `CYAN`.
- `warning`: Записывает сообщение уровня `WARNING` с цветом `YELLOW`.
- `debug`: Записывает сообщение уровня `DEBUG`.
- `error`: Записывает сообщение уровня `ERROR`.
- `critical`: Записывает сообщение уровня `CRITICAL`.
- `info_red`: Записывает сообщение уровня `INFO` красным цветом.
- `info_black`: Записывает сообщение уровня `INFO` черным с белым фоном.


## Функции

### `__init__`

**Описание**: Инициализация экземпляра класса `Logger`.

**Параметры**:
Нет.


### `_configure_logger`

**Описание**: Настраивает и возвращает логгер.

**Параметры**:
- `name` (str): Имя логгера.
- `log_path` (str): Путь к лог-файлу.
- `level` (Optional[int], опционально): Уровень логгирования. По умолчанию `logging.DEBUG`.
- `formatter` (Optional[logging.Formatter], опционально): Пользовательский форматировщик. По умолчанию `None`.
- `mode` (Optional[str], опционально): Режим открытия файла. По умолчанию `'a'`.

**Возвращает**:
- `logging.Logger`: Настроенный экземпляр логгера.


### `initialize_loggers`

**Описание**: Инициализирует логгеры для консоли, файлов (INFO, DEBUG, ERROR) и JSON.

**Параметры**:
- `info_log_path` (Optional[str], опционально): Путь к файлу для логов уровня INFO. По умолчанию `''`.
- `debug_log_path` (Optional[str], опционально): Путь к файлу для логов уровня DEBUG. По умолчанию `''`.
- `errors_log_path` (Optional[str], опционально): Путь к файлу для логов уровня ERROR/CRITICAL. По умолчанию `''`.
- `json_log_path` (Optional[str], опционально): Путь к файлу для логов в формате JSON. По умолчанию `''`.


### `_format_message`

**Описание**: Форматирует сообщение с необязательным цветом и информацией об исключении.

**Параметры**:
- `message` (str): Сообщение.
- `ex` (Optional[str], опционально): Информация об исключении.
- `color` (Optional[str], опционально): Цвет сообщения.

**Возвращает**:
- str: Форматированное сообщение.


### `_ex_full_info`

**Описание**: Возвращает полную информацию об исключении, включая файл, функцию и номер строки.

**Параметры**:
- `ex` (Optional[str], опционально): Информация об исключении.

**Возвращает**:
- str: Форматированная информация об исключении.


### `log`

**Описание**: Общий метод для записи сообщений на указанном уровне с необязательными цветом и информацией об исключении.

**Параметры**:
- `level`: Уровень лога.
- `message` (str): Сообщение.
- `ex` (Optional[Exception], опционально): Информация об исключении.
- `exc_info` (bool, опционально): Выводить информацию об исключении.
- `color` (Optional[str], опционально): Цвет сообщения.

**Возвращает**:
- None

**Вызывает исключения**:
Нет.


### Другие функции (`info`, `success`, `warning`, `debug`, `error`, `critical`)

Эти функции являются оберткаи над `log`, с установленными уровнями и цветами по умолчанию.  Их документация аналогична описанию `log`, но с указанием конкретных значений по умолчанию для параметров уровня (`level`) и цвета (`color`).