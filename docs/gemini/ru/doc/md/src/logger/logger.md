# Модуль logger

## Обзор

Модуль `logger` предоставляет утилиту для ведения логов с различными уровнями и форматами, включая вывод в консоль, файлы и JSON.  Он использует паттерн "Одиночка" (Singleton), гарантируя, что в приложении используется только один экземпляр логгера. Модуль поддерживает различные уровни логов, форматы вывода и возможность цветного вывода сообщений в консоли, в зависимости от уровня важности.

## Классы

### `SingletonMeta`

**Описание**: Метакласс для реализации паттерна "Одиночка".  Гарантирует, что создается только один экземпляр класса, к которому он применяется.

### `JsonFormatter`

**Описание**:  Пользовательский форматтер для логов в формате JSON.

**Методы**

- `format(record: logging.LogRecord) -> str`: Форматирует запись лога в JSON.

**Параметры**

- `record (logging.LogRecord)`: Запись лога.

**Возвращает**

- `str`: Форматированная запись лога в JSON формате.


### `Logger`

**Описание**:  Класс логгера, реализующий паттерн "Одиночка". Поддерживает вывод логов в консоль, файлы и в формате JSON.

**Методы**

- `__init__(self)`: Инициализирует экземпляр класса `Logger`.
- `_configure_logger(self, name: str, log_path: str, level: Optional[int] = logging.DEBUG, formatter: Optional[logging.Formatter] = None, mode: Optional[str] = 'a') -> logging.Logger`: Конфигурирует и возвращает логгер с заданными параметрами.
- `initialize_loggers(self, info_log_path: Optional[str] = '', debug_log_path: Optional[str] = '', errors_log_path: Optional[str] = '', json_log_path: Optional[str] = '')`: Инициализирует логгеры для консоли, файлов (info, debug, errors) и JSON.
- `_format_message(self, message, ex=None, color=None)`: Форматирует сообщение с опциональными цветом и информацией об исключении.
- `_ex_full_info(self, ex)`: Возвращает полную информацию об исключении, включая файл, функцию и строку, где был вызван лог.
- `log(self, level, message, ex=None, exc_info=False, color=None)`:  Общий метод для записи логов на определённом уровне с опциональным цветом и информацией об исключении.
- `info(self, message, ex=None, exc_info=False, colors: Optional[tuple] = None)`: Записывает сообщение уровня `INFO`.
- `success(self, message, ex=None, exc_info=False, colors: Optional[tuple] = None)`: Записывает сообщение уровня `INFO` (успех).
- `warning(self, message, ex=None, exc_info=False, colors: Optional[tuple] = None)`: Записывает сообщение уровня `WARNING`.
- `debug(self, message, ex=None, exc_info=True, colors: Optional[tuple] = None)`: Записывает сообщение уровня `DEBUG`.
- `error(self, message, ex=None, exc_info=True, colors: Optional[tuple] = None)`: Записывает сообщение уровня `ERROR`.
- `critical(self, message, ex=None, exc_info=True, colors: Optional[tuple] = None)`: Записывает сообщение уровня `CRITICAL`.


## Функции

###  `__init__(self)`

**Описание**: Инициализирует переменные экземпляра класса `Logger`.


##  Дополнительная информация

Обратите внимание на  внутримодульные комментарии, которые  разъясняют назначение различных элементов кода.

```
```