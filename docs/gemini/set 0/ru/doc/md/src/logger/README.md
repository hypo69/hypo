# Модуль `src.logger`

## Обзор

Модуль `src.logger` предоставляет гибкую систему логирования, поддерживающую вывод в консоль, файлы и в формате JSON. Он использует паттерн проектирования Singleton, чтобы гарантировать, что в приложении используется только один экземпляр логгера. Логгер поддерживает различные уровни логирования (например, `INFO`, `ERROR`, `DEBUG`) и включает цветной вывод для логирования в консоль. Вы также можете настраивать форматы вывода логов и управлять логированием в разные файлы.

## Классы

### `SingletonMeta`

**Описание**: Метакласс, реализующий паттерн проектирования Singleton для логгера.

### `JsonFormatter`

**Описание**: Пользовательский форматировщик, выводящий логи в формате JSON.

### `Logger`

**Описание**: Основной класс логгера, поддерживающий логирование в консоль, файлы и в формате JSON.


## Функции

### `__init__`

**Описание**: Инициализирует экземпляр `Logger` с плацехолдерами для различных типов логгеров (консоль, файл, JSON).


### `_configure_logger(name: str, log_path: str, level: Optional[int] = logging.DEBUG, formatter: Optional[logging.Formatter] = None, mode: Optional[str] = 'a') -> logging.Logger`

**Описание**: Настраивает и возвращает экземпляр логгера.

**Параметры**:
- `name` (str): Имя логгера.
- `log_path` (str): Путь к файлу лога.
- `level` (Optional[int], опционально): Уровень логирования, например, `logging.DEBUG`. По умолчанию `logging.DEBUG`.
- `formatter` (Optional[logging.Formatter], опционально): Пользовательский форматировщик (необязательно).
- `mode` (Optional[str], опционально): Режим файла, например, `'a'` для добавления (по умолчанию).

**Возвращает**: Настроенный экземпляр `logging.Logger`.


### `initialize_loggers(info_log_path: Optional[str] = '', debug_log_path: Optional[str] = '', errors_log_path: Optional[str] = '', json_log_path: Optional[str] = '')`

**Описание**: Инициализирует логгеры для консольного и файлового логирования (информация, отладка, ошибки и JSON).

**Параметры**:
- `info_log_path` (Optional[str], опционально): Путь к файлу лога для информации.
- `debug_log_path` (Optional[str], опционально): Путь к файлу лога для отладки.
- `errors_log_path` (Optional[str], опционально): Путь к файлу лога для ошибок.
- `json_log_path` (Optional[str], опционально): Путь к файлу лога для JSON.


### `log(level, message, ex=None, exc_info=False, color=None)`

**Описание**: Записывает сообщение на указанном уровне (например, `INFO`, `DEBUG`, `ERROR`) с необязательным указанием исключения и форматированием цвета.

**Параметры**:
- `level`: Уровень логирования (например, `logging.INFO`, `logging.DEBUG`).
- `message`: Сообщение лога.
- `ex`: Необязательное исключение для записи.
- `exc_info`: Флаг, включающий ли информацию об исключении (по умолчанию `False`).
- `color`: Кортеж с цветами текста и фона для консольного вывода (опционально).


### `info`, `success`, `warning`, `debug`, `error`, `critical`

**Описание**: Функции для логирования сообщений на соответствующих уровнях, аналогичные `log`, но с предопределёнными уровнями.

**Параметры**: Аналогичные `log`, но с фиксированным `level` (logging.INFO, logging.DEBUG и т.д.)


## Параметры логгера

Класс `Logger` принимает несколько необязательных параметров для настройки поведения логирования.

- **Level**: Управляет уровнем серьезности логов, которые будут записаны. Распространенные уровни:
  - `logging.DEBUG`: Детальная информация, полезная для диагностики проблем.
  - `logging.INFO`: Общая информация, такая как успешные операции.
  - `logging.WARNING`: Предупреждения, которые не обязательно требуют немедленного действия.
  - `logging.ERROR`: Сообщения об ошибках.
  - `logging.CRITICAL`: Критические ошибки, требующие немедленного вмешательства.

- **Formatter**: Определяет, как форматируются сообщения логов. По умолчанию сообщения форматируются как `'%(asctime)s - %(levelname)s - %(message)s'`. Вы можете указать пользовательский форматировщик для разных форматов, таких как JSON.

- **Color**: Цвета для сообщений логов в консоли. Цвета задаются как кортеж из двух элементов:
  - Цвет текста (например, `colorama.Fore.RED`).
  - Цвет фона (например, `colorama.Back.WHITE`).

Цвет можно настроить для разных уровней логирования (например, зеленый для информации, красный для ошибок и т.д.).


## Настройка файлового логирования (`config`)

Для записи сообщений в файл вы можете указать пути к файлам в конфигурации.

```python
config = {
    'info_log_path': 'logs/info.log',
    'debug_log_path': 'logs/debug.log',
    'errors_log_path': 'logs/errors.log',
    'json_log_path': 'logs/log.json'
}
```

Пути к файлам, указанные в `config`, используются для записи логов в соответствующие файлы для каждого уровня логирования.

## Пример использования

#### 1. Инициализация логгера

#### 2. Логирование сообщений на разных уровнях

#### 3. Настройка цветов

## Заключение

Этот модуль предоставляет комплексную и гибкую систему логирования для приложений Python. Вы можете настроить консольное и файловое логирование с разными форматами и цветами, управлять уровнями логирования и обрабатывать исключения. Конфигурация файлового логирования хранится в словаре `config`, что позволяет легко настроить ее.