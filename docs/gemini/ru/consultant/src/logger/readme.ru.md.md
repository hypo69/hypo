# Анализ кода модуля `src.logger`

**Качество кода: 9**
-   **Плюсы**
    -   Документация в формате reStructuredText (RST) присутствует и является достаточно подробной, описывает структуру модуля, классы и функции.
    -   Примеры использования модуля хорошо иллюстрируют основные возможности.
    -   Присутствует описание уровней логирования и настройки цветов.
    -   Описан процесс конфигурации логирования в файлы.
-   **Минусы**
    -   В документации не хватает более подробных описаний параметров функций, особенно типов данных.
    -   Недостает примеров использования кастомных форматтеров и более сложных сценариев логирования.
    -   Не указано, как обрабатывать исключения внутри самого модуля logger.

**Рекомендации по улучшению**

1.  **Документация**:
    -   Добавить более подробное описание типов данных для параметров функций в формате RST.
    -   Привести примеры использования кастомных форматтеров.
    -   Улучшить описание обработки исключений в коде.
2.  **Примеры**:
    -   Добавить пример использования JSON-форматтера.
    -   Показать пример настройки нескольких файлов логирования.
    -   Добавить пример обработки исключений в примере использования.

**Оптимизированный код**

```markdown
.. module:: src.logger

<TABLE>
<TR>
<TD>
<A HREF = 'https://github.com/hypo69/hypo/blob/master/README.MD'>[Root ↑]</A>
</TD>
<TD>
<A HREF = 'https://github.com/hypo69/hypo/blob/master/src/README.MD'>src</A> /
</TD>
<TD>
<A HREF = 'https://github.com/hypo69/hypo/blob/master/src/logger/README.MD'>English</A>
</TD>
</TABLE>

Документация для модуля `src.logger`
=====================================================================================

Модуль `src.logger` предоставляет гибкую систему логирования, поддерживающую логирование в консоль, файлы и в формате JSON.
Он использует шаблон проектирования Singleton, чтобы обеспечить использование единственного экземпляра логгера во всем приложении.
Логгер поддерживает различные уровни логирования (например, `INFO`, `ERROR`, `DEBUG`) и включает цветное отображение для вывода в консоль.
Также доступны настройки форматов вывода и управление логированием в различные файлы.

---

### Классы:

- **SingletonMeta**: Метакласс, реализующий шаблон Singleton для логгера.
- **JsonFormatter**: Кастомный форматтер для вывода логов в формате JSON.
- **Logger**: Основной класс логгера, поддерживающий логирование в консоль, файлы и в формате JSON.

---

### Функции:

#### `__init__`
    Инициализирует экземпляр класса Logger с плейсхолдерами для различных типов логгеров (консоль, файлы и JSON).

#### `_configure_logger(name: str, log_path: str, level: Optional[int] = logging.DEBUG, formatter: Optional[logging.Formatter] = None, mode: Optional[str] = 'a') -> logging.Logger`
    Настраивает и возвращает экземпляр логгера.

    :param name: Имя логгера.
    :type name: str
    :param log_path: Путь к файлу логов.
    :type log_path: str
    :param level: Уровень логирования, например, `logging.DEBUG`. Значение по умолчанию — `logging.DEBUG`.
    :type level: Optional[int]
    :param formatter: Кастомный форматтер (опционально).
    :type formatter: Optional[logging.Formatter]
    :param mode: Режим работы с файлом, например, `'a'` для добавления (значение по умолчанию).
    :type mode: Optional[str]
    :return: Настроенный экземпляр `logging.Logger`.
    :rtype: logging.Logger

#### `initialize_loggers(info_log_path: Optional[str] = '', debug_log_path: Optional[str] = '', errors_log_path: Optional[str] = '', json_log_path: Optional[str] = '')`
    Инициализирует логгеры для логирования в консоль и файлы (информация, отладка, ошибки и JSON).

    :param info_log_path: Путь к файлу логов информации (опционально).
    :type info_log_path: Optional[str]
    :param debug_log_path: Путь к файлу логов отладки (опционально).
    :type debug_log_path: Optional[str]
    :param errors_log_path: Путь к файлу логов ошибок (опционально).
    :type errors_log_path: Optional[str]
    :param json_log_path: Путь к файлу логов в формате JSON (опционально).
    :type json_log_path: Optional[str]

#### `log(level: int, message: str, ex: Optional[Exception] = None, exc_info: bool = False, color: Optional[tuple] = None)`
    Логирует сообщение на указанном уровне (например, `INFO`, `DEBUG`, `ERROR`) с возможным исключением и цветовым форматированием.

    :param level: Уровень логирования (например, `logging.INFO`, `logging.DEBUG`).
    :type level: int
    :param message: Логируемое сообщение.
    :type message: str
    :param ex: Исключение для логирования (опционально).
    :type ex: Optional[Exception]
    :param exc_info: Включать информацию об исключении (значение по умолчанию — `False`).
    :type exc_info: bool
    :param color: Кортеж цветов текста и фона для консольного вывода (опционально).
    :type color: Optional[tuple]

#### Другие методы:

- `info`: Логирует информационное сообщение.
- `success`: Логирует сообщение об успешной операции.
- `warning`: Логирует предупреждение.
- `debug`: Логирует сообщение для отладки.
- `error`: Логирует сообщение об ошибке.
- `critical`: Логирует критическое сообщение.

---

### Параметры логгера

Класс `Logger` принимает несколько опциональных параметров для настройки поведения логирования.

- **Уровень**: Контролирует, какие сообщения будут записаны. Основные уровни:
  - `logging.DEBUG`: Подробная информация для диагностики.
  - `logging.INFO`: Общая информация, например, успешные операции.
  - `logging.WARNING`: Предупреждения, не требующие немедленного действия.
  - `logging.ERROR`: Сообщения об ошибках.
  - `logging.CRITICAL`: Критические ошибки, требующие немедленного внимания.

- **Форматтер**: Определяет формат сообщений. По умолчанию используется `'%(asctime)s - %(levelname)s - %(message)s'`. Можно задать кастомный форматтер, например для JSON.

- **Цвета**: Задают цвет текста и фона в консоли. Цвета указываются кортежем:
  - **Цвет текста**: Например, `colorama.Fore.RED`.
  - **Цвет фона**: Например, `colorama.Back.WHITE`.

---

### Конфигурация для логирования в файл (`config`)

Для записи сообщений в файл можно указать пути в конфигурации.

```python
config = {
    'info_log_path': 'logs/info.log',
    'debug_log_path': 'logs/debug.log',
    'errors_log_path': 'logs/errors.log',
    'json_log_path': 'logs/log.json'
}
```

---

### Примеры использования

#### 1. Инициализация логгера:

```python
from src.logger.logger import Logger
import logging

logger: Logger = Logger()
config = {
    'info_log_path': 'logs/info.log',
    'debug_log_path': 'logs/debug.log',
    'errors_log_path': 'logs/errors.log',
    'json_log_path': 'logs/log.json'
}
logger.initialize_loggers(**config)
```

#### 2. Логирование сообщений:

```python
logger.info('Это информационное сообщение')
logger.success('Это сообщение об успешной операции')
logger.warning('Это предупреждение')
logger.debug('Это сообщение для отладки')
logger.error('Это сообщение об ошибке')
logger.critical('Это критическое сообщение')
```

#### 3. Настройка цветов:

```python
import colorama
logger.info('Это сообщение будет зеленым', colors=(colorama.Fore.GREEN, colorama.Back.BLACK))
logger.error('Это сообщение с красным фоном', colors=(colorama.Fore.WHITE, colorama.Back.RED))
```

#### 4. Пример использования JSON-форматтера:

```python
import logging
from src.logger.logger import Logger, JsonFormatter


logger: Logger = Logger()
config = {
    'json_log_path': 'logs/json_log.json'
}
logger.initialize_loggers(**config)
json_formatter = JsonFormatter()
json_logger = logger._configure_logger(name='json_logger', log_path=config['json_log_path'], formatter=json_formatter)
json_logger.info({'event': 'start', 'message': 'Application started'})

```

#### 5. Пример логирования исключений:

```python
from src.logger.logger import Logger
import logging
logger: Logger = Logger()
config = {
    'errors_log_path': 'logs/errors.log'
}
logger.initialize_loggers(**config)

try:
    1 / 0
except Exception as ex:
    logger.error('Произошла ошибка деления на ноль', ex=ex, exc_info=True)
```

---

Модуль `src.logger` предоставляет полноценную систему логирования для Python-приложений. Вы можете настроить логирование в консоль и файлы с различными форматами и цветами, управлять уровнями логирования и обрабатывать исключения. Конфигурация логирования в файлы задается через словарь `config`, что позволяет легко изменять настройки.
```