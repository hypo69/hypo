# Модуль logger

## Обзор

Модуль `logger` предоставляет класс `Logger` для централизованного ведения логов в консоли, файлах (информация, отладка, ошибки, JSON) с поддержкой Singleton паттерна.  Класс умеет форматировать сообщения логов в JSON, а также обрабатывать исключения, выводя их полную информацию в лог.


## Классы

### `SingletonMeta`

**Описание**: Метакласс, реализующий паттерн Singleton для класса `Logger`.  Гарантирует, что в системе существует только один экземпляр `Logger`.

**Атрибуты**:
- `_instances`: Словарь, хранящий экземпляры классов, использующих `SingletonMeta`.
- `_lock`: Объект блокировки `threading.Lock()` для предотвращения проблем с многопоточностью.

**Методы**:
- `__call__`: Переопределенный метод вызова класса, гарантирующий создание единственного экземпляра.


### `JsonFormatter`

**Описание**: Пользовательский форматировщик для записи логов в формате JSON.

**Методы**:
- `format`: Форматирует запись лога в JSON. Добавляет поля `exc_info` для информации об исключениях.


### `Logger`

**Описание**: Класс для ведения логов в консоли, файлах и формате JSON. Реализует Singleton паттерн.

**Атрибуты**:
- `logger_console`: Логгер для консоли.
- `logger_file_info`: Логгер для файла с информационными сообщениями.
- `logger_file_debug`: Логгер для файла с отладочными сообщениями.
- `logger_file_errors`: Логгер для файла с ошибками.
- `logger_file_json`: Логгер для файла с логами в формате JSON.
- `_initialized`: Флаг, указывающий, был ли инициализирован логгер.

**Методы**:
- `__init__`: Инициализирует логгеры (все атрибуты логгеров устанавливаются в `None`, `_initialized` в `False`).
- `_configure_logger`: Конфигурирует и возвращает логгер для файла.
- `initialize_loggers`: Инициализирует логгеры для консоли, файлов (информация, отладка, ошибки, JSON), основываясь на переданных путях к файлам. Добавляет форматирование времени и имени логгера в выходные данные.
- `_format_message`: Возвращает отформатированное сообщение с опциональной цветовой подсветкой и информацией об исключениях.
- `_ex_full_info`: Возвращает полную информацию об исключении, включая имя файла, имя функции и номер строки, где оно произошло.
- `log`: Общий метод для записи логов с указанным уровнем и опциональной цветовой подсветкой. Обрабатывает инициализацию логгеров, форматирование сообщений и запись в консоль и файл.
- `info`, `success`, `warning`, `debug`, `error`, `critical`: Методы для записи логов определенных уровней.  Используют `log` для записи, а также передают значения `colorama` по умолчанию (например, `colorama.Fore.GREEN` для `info`).


## Функции


Нет функций в этом модуле.