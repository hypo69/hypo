### Анализ кода модуля `src.logger`

**Качество кода**:
- **Соответствие стандартам**: 7/10
- **Плюсы**:
    - Хорошее описание модуля и его классов.
    - Четкое описание параметров и возвращаемых значений функций.
    - Примеры использования, демонстрирующие основные возможности модуля.
    - Подробное описание уровней логирования.
- **Минусы**:
    - Отсутствует полное соответствие PEP8.
    - Нет RST-документации для функций и методов.
    - Использование двойных кавычек в примерах кода.
    - Не используется `from src.logger import logger` в примерах.
    - Нет явных указаний на то, что `Logger` является Singleton.

**Рекомендации по улучшению**:
- Добавить RST-документацию для всех функций и методов, включая примеры.
- Использовать одинарные кавычки в коде, кроме операций вывода.
- Уточнить, что `Logger` реализован как Singleton с помощью метакласса `SingletonMeta`.
- Добавить явное описание для метакласса `SingletonMeta`.
- Использовать `from src.logger.logger import logger` для импорта логгера.
- Выравнить структуру разделов документации.
- Заменить неточные формулировки (например, "делаем") на более точные.

**Оптимизированный код**:
```rst
.. module:: src.logger

```
<TABLE >
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

Модуль `src.logger` предоставляет гибкую систему логирования, поддерживающую логирование в консоль, файлы и в формате JSON. Он использует шаблон проектирования Singleton, чтобы обеспечить использование единственного экземпляра логгера во всем приложении. Логгер поддерживает различные уровни логирования (например, `INFO`, `ERROR`, `DEBUG`) и включает цветное отображение для вывода в консоль. Также доступны настройки форматов вывода и управление логированием в различные файлы.

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
    :type level: int, optional
    :param formatter: Кастомный форматтер (опционально).
    :type formatter: logging.Formatter, optional
    :param mode: Режим работы с файлом, например, `'a'` для добавления (значение по умолчанию).
    :type mode: str, optional
    :return: Настроенный экземпляр `logging.Logger`.
    :rtype: logging.Logger
    
    
#### `initialize_loggers(info_log_path: Optional[str] = '', debug_log_path: Optional[str] = '', errors_log_path: Optional[str] = '', json_log_path: Optional[str] = '')`
    Инициализирует логгеры для логирования в консоль и файлы (информация, отладка, ошибки и JSON).
    
    :param info_log_path: Путь к файлу логов информации (опционально).
    :type info_log_path: str, optional
    :param debug_log_path: Путь к файлу логов отладки (опционально).
    :type debug_log_path: str, optional
    :param errors_log_path: Путь к файлу логов ошибок (опционально).
    :type errors_log_path: str, optional
    :param json_log_path: Путь к файлу логов в формате JSON (опционально).
    :type json_log_path: str, optional

#### `log(level, message, ex=None, exc_info=False, color=None)`
    Логирует сообщение на указанном уровне (например, `INFO`, `DEBUG`, `ERROR`) с возможным исключением и цветовым форматированием.
    
    :param level: Уровень логирования (например, `logging.INFO`, `logging.DEBUG`).
    :type level: int
    :param message: Логируемое сообщение.
    :type message: str
    :param ex: Исключение для логирования (опционально).
    :type ex: Exception, optional
    :param exc_info: Включать информацию об исключении (значение по умолчанию — `False`).
    :type exc_info: bool, optional
    :param color: Кортеж цветов текста и фона для консольного вывода (опционально).
    :type color: tuple, optional

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
from src.logger.logger import logger  # Используем явный импорт логгера

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
from src.logger.logger import logger  # Используем явный импорт логгера

logger.info('Это информационное сообщение')
logger.success('Это сообщение об успешной операции')
logger.warning('Это предупреждение')
logger.debug('Это сообщение для отладки')
logger.error('Это сообщение об ошибке')
logger.critical('Это критическое сообщение')
```

#### 3. Настройка цветов:
```python
from src.logger.logger import logger  # Используем явный импорт логгера
import colorama

logger.info('Это сообщение будет зеленым', color=(colorama.Fore.GREEN, colorama.Back.BLACK))
logger.error('Это сообщение с красным фоном', color=(colorama.Fore.WHITE, colorama.Back.RED))
```

---

Модуль `src.logger` предоставляет полноценную систему логирования для Python-приложений. Вы можете настроить логирование в консоль и файлы с различными форматами и цветами, управлять уровнями логирования и обрабатывать исключения. Конфигурация логирования в файлы задается через словарь `config`, что позволяет легко изменять настройки.