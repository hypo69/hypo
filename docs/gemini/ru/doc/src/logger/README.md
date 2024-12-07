# Модуль `src.logger`

## Обзор

Модуль `src.logger` предоставляет гибкую систему логирования, поддерживающую вывод в консоль, файлы и JSON-формат. Он использует паттерн Singleton для обеспечения того, что в приложении используется только один экземпляр логгера. Логгер поддерживает различные уровни логов (например, `INFO`, `ERROR`, `DEBUG`) и включает цветной вывод для логов в консоли. Вы также можете настроить форматы вывода логов и управлять логированием в различные файлы.

## Классы

### `SingletonMeta`

**Описание**: Метакласс, реализующий паттерн Singleton для логгера.

### `JsonFormatter`

**Описание**: Специализированный форматировщик, выводит логи в формате JSON.


### `Logger`

**Описание**: Основной класс логгера, поддерживающий логирование в консоль, файлы и JSON.

## Функции

### `__init__`

**Описание**: Инициализирует экземпляр `Logger` с заполненными плацехолдерами для разных типов логгеров (консоль, файл, JSON).


### `_configure_logger(name: str, log_path: str, level: Optional[int] = logging.DEBUG, formatter: Optional[logging.Formatter] = None, mode: Optional[str] = 'a') -> logging.Logger`

**Описание**: Конфигурирует и возвращает экземпляр логгера.

**Параметры:**

- `name` (str): Имя логгера.
- `log_path` (str): Путь к файлу лога.
- `level` (Optional[int], опционально): Уровень логирования, например, `logging.DEBUG`. По умолчанию `logging.DEBUG`.
- `formatter` (Optional[logging.Formatter], опционально): Пользовательский форматировщик.
- `mode` (Optional[str], опционально): Режим файла, например, `'a'` для добавления (по умолчанию).

**Возвращает:**

- `logging.Logger`: Конфигурированный экземпляр `logging.Logger`.

### `initialize_loggers(info_log_path: Optional[str] = '', debug_log_path: Optional[str] = '', errors_log_path: Optional[str] = '', json_log_path: Optional[str] = '')`

**Описание**: Инициализирует логгеры для консольного и файлового логирования (информация, отладка, ошибки и JSON).

**Параметры:**

- `info_log_path` (Optional[str], опционально): Путь к файлу для логов уровня `INFO`.
- `debug_log_path` (Optional[str], опционально): Путь к файлу для логов уровня `DEBUG`.
- `errors_log_path` (Optional[str], опционально): Путь к файлу для логов уровня `ERROR`.
- `json_log_path` (Optional[str], опционально): Путь к файлу для JSON-логов.


### `log(level, message, ex=None, exc_info=False, color=None)`

**Описание**: Записывает сообщение на указанном уровне (например, `INFO`, `DEBUG`, `ERROR`) с опциональным исключением и форматированием цвета.

**Параметры:**

- `level`: Уровень логирования (например, `logging.INFO`, `logging.DEBUG`).
- `message`: Сообщение для логирования.
- `ex`: Опциональное исключение для логирования.
- `exc_info`: Флаг, включающий информацию об исключении (по умолчанию `False`).
- `color`: Кортеж с текстовыми и фоновыми цветами для консольного вывода (опционально).


### `info(message, ex=None, exc_info=False, colors: Optional[tuple] = None)`

**Описание**: Записывает сообщение уровня `INFO`.

**Параметры:**

-  (см. `log`)

### `success(message, ex=None, exc_info=False, colors: Optional[tuple] = None)`

**Описание**: Записывает сообщение уровня `Успех`.

**Параметры:**

- (см. `log`)


### `warning(message, ex=None, exc_info=False, colors: Optional[tuple] = None)`

**Описание**: Записывает сообщение уровня `Предупреждение`.

**Параметры:**

- (см. `log`)


### `debug(message, ex=None, exc_info=True, colors: Optional[tuple] = None)`

**Описание**: Записывает сообщение уровня `DEBUG`.

**Параметры:**

- (см. `log`)


### `error(message, ex=None, exc_info=True, colors: Optional[tuple] = None)`

**Описание**: Записывает сообщение уровня `ERROR`.

**Параметры:**

- (см. `log`)


### `critical(message, ex=None, exc_info=True, colors: Optional[tuple] = None)`

**Описание**: Записывает сообщение уровня `CRITICAL`.

**Параметры:**

- (см. `log`)


## Параметры логгера

## Настройка файлового логирования (`config`)

Для записи логов в файл можно указать пути в конфигурации.

```python
config = {
    'info_log_path': 'logs/info.log',
    'debug_log_path': 'logs/debug.log',
    'errors_log_path': 'logs/errors.log',
    'json_log_path': 'logs/log.json'
}
```

Пути, указанные в `config`, используются для записи логов в соответствующие файлы для каждого уровня.

## Пример использования

### 1. Инициализация логгера:

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

### 2. Логирование сообщений на различных уровнях:

```python
logger.info('Это информационное сообщение')
logger.success('Это сообщение успеха')
logger.warning('Это предупреждение')
logger.debug('Это отладочное сообщение')
logger.error('Это ошибка')
logger.critical('Это критическое сообщение')
```

### 3. Настройка цветов:

```python
logger.info('Это сообщение будет зелёным', colors=(colorama.Fore.GREEN, colorama.Back.BLACK))
logger.error('Это сообщение будет с красным фоном', colors=(colorama.Fore.WHITE, colorama.Back.RED))
```

## Заключение

Этот модуль предоставляет полную и гибкую систему логирования для приложений Python. Вы можете настроить консольное и файловое логирование с различными форматами и цветами, управлять уровнями логирования и обрабатывать исключения. Настройка файлового логирования хранится в словаре `config`, что позволяет легко настраивать ее.