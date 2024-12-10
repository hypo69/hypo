# Модуль `src.logger`

## Обзор

Модуль `src.logger` предоставляет гибкую систему логгирования, поддерживающую логгирование в консоль, файл и в формате JSON. Он использует паттерн Singleton для обеспечения того, что используется только одна инстанция логгера во всем приложении. Логгер поддерживает различные уровни логгирования (например, `INFO`, `ERROR`, `DEBUG`) и включает цветной вывод для логов в консоль. Также вы можете настраивать форматы вывода логов и управлять логгированием в различные файлы.

## Классы

### `SingletonMeta`

**Описание**: Метакласс, реализующий паттерн Singleton для логгера.

### `JsonFormatter`

**Описание**: Специальный форматер, выводящий логи в формате JSON.

### `Logger`

**Описание**: Основной класс логгера, поддерживающий логгирование в консоль, файл и в формате JSON.


## Функции

### `__init__`

**Описание**: Инициализирует экземпляр `Logger` с заполнителями для различных типов логгеров (консоль, файл и JSON).


### `_configure_logger(name: str, log_path: str, level: Optional[int] = logging.DEBUG, formatter: Optional[logging.Formatter] = None, mode: Optional[str] = 'a') -> logging.Logger`

**Описание**: Настраивает и возвращает экземпляр логгера.

**Параметры:**

- `name` (str): Имя логгера.
- `log_path` (str): Путь к файлу логов.
- `level` (Optional[int], optional): Уровень логгирования, например, `logging.DEBUG`. По умолчанию `logging.DEBUG`.
- `formatter` (Optional[logging.Formatter], optional): Настраиваемый форматер (необязательно).
- `mode` (Optional[str], optional): Режим файла, например, `'a'` для добавления (по умолчанию).

**Возвращает**: Настроенный экземпляр `logging.Logger`.


### `initialize_loggers(info_log_path: Optional[str] = '', debug_log_path: Optional[str] = '', errors_log_path: Optional[str] = '', json_log_path: Optional[str] = '')`

**Описание**: Инициализирует логгеры для консольного и файлового логгирования (информация, отладка, ошибка и JSON).

**Параметры:**

- `info_log_path` (Optional[str], optional): Путь для файла логов информации.
- `debug_log_path` (Optional[str], optional): Путь для файла логов отладки.
- `errors_log_path` (Optional[str], optional): Путь для файла логов ошибок.
- `json_log_path` (Optional[str], optional): Путь для файла логов в формате JSON.


### `log(level, message, ex=None, exc_info=False, color=None)`

**Описание**: Записывает сообщение на указанном уровне (например, `INFO`, `DEBUG`, `ERROR`) с необязательными данными об исключениях и форматированием цвета.

**Параметры:**

- `level`: Уровень логгирования (например, `logging.INFO`, `logging.DEBUG`).
- `message`: Сообщение для логгирования.
- `ex`: Необязательное исключение для логгирования.
- `exc_info`: Нужно ли включать информацию об исключении (по умолчанию `False`).
- `color`: Кортеж с текстовым и фоновым цветами для консольного вывода (необязательно).


### `info(message, ex=None, exc_info=False, colors: Optional[tuple] = None)`
### `success(message, ex=None, exc_info=False, colors: Optional[tuple] = None)`
### `warning(message, ex=None, exc_info=False, colors: Optional[tuple] = None)`
### `debug(message, ex=None, exc_info=True, colors: Optional[tuple] = None)`
### `error(message, ex=None, exc_info=True, colors: Optional[tuple] = None)`
### `critical(message, ex=None, exc_info=True, colors: Optional[tuple] = None)`

**Описание**: Функции для записи логов на соответствующем уровне (INFO, SUCCESS, WARNING, DEBUG, ERROR, CRITICAL).


## Параметры для логгера

Класс `Logger` принимает несколько необязательных параметров для настройки поведения логгирования.

- **Уровень** (Level): Контролирует уровень серьезности логов, которые фиксируются.
  - `logging.DEBUG`: Подробная информация, полезная для диагностики проблем.
  - `logging.INFO`: Общая информация, например, успешные операции.
  - `logging.WARNING`: Предупреждения, которые не обязательно требуют немедленных действий.
  - `logging.ERROR`: Сообщения об ошибках.
  - `logging.CRITICAL`: Критические ошибки, требующие немедленного внимания.

- **Форматер** (Formatter): Определяет, как форматируются сообщения логов. По умолчанию сообщения форматируются как `'%(asctime)s - %(levelname)s - %(message)s'`. Вы можете предоставить пользовательский форматер для различных форматов, например, JSON.

- **Цвет** (Color): Цвета сообщений логов в консоли. Цвета задаются как кортеж из двух элементов:
  - **Цвет текста** (например, `colorama.Fore.RED`).
  - **Цвет фона** (например, `colorama.Back.WHITE`).

Цвет можно настраивать для различных уровней логов (например, зелёный для `INFO`, красный для `ERROR` и т.д.).


## Настройка файлового логгирования (`config`)

Для записи сообщений в файл вы можете указать пути к файлам в конфигурации.

```python
config = {
    'info_log_path': 'logs/info.log',
    'debug_log_path': 'logs/debug.log',
    'errors_log_path': 'logs/errors.log',
    'json_log_path': 'logs/log.json'
}
```

Пути к файлам, указанные в `config`, используются для записи логов в соответствующие файлы для каждого уровня логов.


## Пример использования

... (Пример использования, как в исходном тексте)
```
```