### Анализ кода модуля `src.logger`

**Качество кода**:
- **Соответствие стандартам**: 7/10
- **Плюсы**:
    - Хорошая общая структура документации, описывающая основные классы и функции.
    - Наличие примеров использования, что облегчает понимание модуля.
    - Подробное описание параметров функций и их возвращаемых значений.
    - Описание уровней логирования и их применения.
- **Минусы**:
    - Используются двойные кавычки для строк, где должны быть одинарные в примерах кода.
    - Не везде соблюдается единообразие в оформлении документации (использование жирного шрифта для параметров функций).
    - Некоторые формулировки ("получаем", "делаем") в описаниях могут быть более точными.
    - Нет чёткого указания на использование `from src.logger.logger import logger` для логирования ошибок.
    - Описания некоторых методов недостаточно информативны ("Другие методы:").

**Рекомендации по улучшению**:

- Исправить все двойные кавычки в примерах кода на одинарные.
- Перефразировать неточные формулировки в описаниях, например, "получаем" на "возвращает" или "извлекает".
- В разделе "Другие методы" дать более конкретное описание каждого метода.
- Добавить больше деталей о том, как использовать кастомные форматтеры.
- Явно указать необходимость использовать `from src.logger import logger` для логирования ошибок.
- Добавить в документацию пример использования кастомного форматтера (JsonFormatter).
- Привести пример использования try-except, а также указать, что logger.error используется вместо обычного try-except.
- Оформить весь код в стиле reStructuredText (RST) с использованием правильных директив.

**Оптимизированный код**:

```rst
.. module:: src.logger
   :synopsis: Модуль для гибкого логирования в консоль, файлы и JSON.

.. Содержит классы Logger, JsonFormatter и SingletonMeta для управления логированием.

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

#### `_configure_logger(name: str, log_path: str, level: int = logging.DEBUG, formatter: logging.Formatter = None, mode: str = 'a') -> logging.Logger`
    
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

#### `initialize_loggers(info_log_path: str = '', debug_log_path: str = '', errors_log_path: str = '', json_log_path: str = '')`

    Инициализирует логгеры для логирования в консоль и файлы (информация, отладка, ошибки и JSON).
    
    :param info_log_path: Путь к файлу логов информации (опционально).
    :type info_log_path: str, optional
    :param debug_log_path: Путь к файлу логов отладки (опционально).
    :type debug_log_path: str, optional
    :param errors_log_path: Путь к файлу логов ошибок (опционально).
    :type errors_log_path: str, optional
    :param json_log_path: Путь к файлу логов в формате JSON (опционально).
    :type json_log_path: str, optional

#### `log(level: int, message: str, ex: Exception = None, exc_info: bool = False, color: tuple = None)`

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

- `info(message: str, color: tuple = None)`: Логирует информационное сообщение.
- `success(message: str, color: tuple = None)`: Логирует сообщение об успешной операции.
- `warning(message: str, color: tuple = None)`: Логирует предупреждение.
- `debug(message: str, color: tuple = None)`: Логирует сообщение для отладки.
- `error(message: str, ex: Exception = None, exc_info: bool = False, color: tuple = None)`: Логирует сообщение об ошибке.
- `critical(message: str, ex: Exception = None, exc_info: bool = False, color: tuple = None)`: Логирует критическое сообщение.

---

### Параметры логгера

Класс `Logger` принимает несколько опциональных параметров для настройки поведения логирования.

- **Уровень**: Контролирует, какие сообщения будут записаны. Основные уровни:
  - `logging.DEBUG`: Подробная информация для диагностики.
  - `logging.INFO`: Общая информация, например, успешные операции.
  - `logging.WARNING`: Предупреждения, не требующие немедленного действия.
  - `logging.ERROR`: Сообщения об ошибках.
  - `logging.CRITICAL`: Критические ошибки, требующие немедленного внимания.

- **Форматтер**: Определяет формат сообщений. По умолчанию используется `'%(asctime)s - %(levelname)s - %(message)s'`. Можно задать кастомный форматтер, например, для JSON.

- **Цвета**: Задают цвет текста и фона в консоли. Цвета указываются кортежем:
  - **Цвет текста**: Например, `colorama.Fore.RED`.
  - **Цвет фона**: Например, `colorama.Back.WHITE`.

---

### Конфигурация для логирования в файл (`config`)

Для записи сообщений в файл можно указать пути в конфигурации.

.. code-block:: python

    config = {
        'info_log_path': 'logs/info.log',
        'debug_log_path': 'logs/debug.log',
        'errors_log_path': 'logs/errors.log',
        'json_log_path': 'logs/log.json'
    }

---

### Примеры использования

#### 1. Инициализация логгера:

.. code-block:: python

    from src.logger import logger # Используйте этот импорт для логирования
    config = {
        'info_log_path': 'logs/info.log',
        'debug_log_path': 'logs/debug.log',
        'errors_log_path': 'logs/errors.log',
        'json_log_path': 'logs/log.json'
    }
    logger.initialize_loggers(**config)

#### 2. Логирование сообщений:

.. code-block:: python

    logger.info('Это информационное сообщение')
    logger.success('Это сообщение об успешной операции')
    logger.warning('Это предупреждение')
    logger.debug('Это сообщение для отладки')
    logger.error('Это сообщение об ошибке')
    logger.critical('Это критическое сообщение')

#### 3. Настройка цветов:

.. code-block:: python

    import colorama
    logger.info('Это сообщение будет зеленым', color=(colorama.Fore.GREEN, colorama.Back.BLACK))
    logger.error('Это сообщение с красным фоном', color=(colorama.Fore.WHITE, colorama.Back.RED))

#### 4. Использование `JsonFormatter`:

.. code-block:: python

    import logging
    from src.logger.logger import Logger, JsonFormatter
    
    logger = Logger()
    config = {
        'json_log_path': 'logs/log.json'
    }
    formatter = JsonFormatter()
    json_logger = logger._configure_logger('json_logger', config['json_log_path'], formatter=formatter)

    json_logger.info({'event': 'start', 'status': 'ok'})
    json_logger.error({'event': 'error', 'message': 'something went wrong'})

#### 5. Обработка ошибок с помощью `logger.error`:

.. code-block:: python

    try:
        1 / 0 # Вызываем ошибку деления на ноль.
    except Exception as ex:
        logger.error("Произошла ошибка", ex=ex, exc_info=True) # Логируем ошибку с использованием logger.error.

---

Модуль `src.logger` предоставляет полноценную систему логирования для Python-приложений.
Вы можете настроить логирование в консоль и файлы с различными форматами и цветами, управлять уровнями логирования и обрабатывать исключения.
Конфигурация логирования в файлы задается через словарь `config`, что позволяет легко изменять настройки.
Для логирования ошибок используйте `from src.logger import logger`, вместо обычного `try-except`, это позволит вам более детально обрабатывать ошибки.