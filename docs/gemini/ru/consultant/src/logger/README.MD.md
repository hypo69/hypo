# Анализ кода модуля `src.logger`

## Качество кода:

- **Соответствие стандартам**: 7
- **Плюсы**:
    - Документ содержит подробное описание модуля `src.logger`.
    - Присутствуют описания классов, функций, параметров и примеры использования.
    - Логическая структура документа позволяет легко ориентироваться в материале.
    - Указаны основные концепции логирования и примеры конфигурации.
- **Минусы**:
    - Отсутствуют docstring в коде модуля.
    - Необходимо использовать `from src.logger.logger import logger` для импорта логгера.
    - В коде используется `logging` вместо `logger.error`.
    - Не приведены примеры использования RST для docstring в коде.
    - Необходимо более четко следовать стандартам PEP8 в примерах кода.

## Рекомендации по улучшению:

1. **Добавить docstring**:
   - В начале модуля, для классов и функций, необходимо добавить документацию в формате RST. Это улучшит читаемость и понимание кода.
2.  **Использовать `from src.logger.logger import logger`**:
    - При импорте логгера использовать `from src.logger.logger import logger`.
3. **Улучшить обработку ошибок**:
   - Заменить `logging.error` на `logger.error` для обработки ошибок.
4.  **Улучшить примеры кода**:
    - Следовать стандартам PEP8 и добавить пояснения в виде комментариев к примерам кода.
5. **Добавить примеры RST**:
   - Добавить примеры использования RST-форматирования в документации.
6. **Избегать неясных выражений**:
    -  Вместо "получаем" или "делаем" использовать более точные формулировки, такие как "проверяем", "отправляем", "выполняем".

## Оптимизированный код:

```rst
.. module:: src.logger

Модуль :mod:`src.logger`
========================

Этот модуль предоставляет гибкую систему логирования, поддерживающую вывод в консоль, файлы и JSON.
Он использует шаблон проектирования Singleton, чтобы гарантировать наличие только одного экземпляра логгера в приложении.
Логгер поддерживает различные уровни логирования (например, ``INFO``, ``ERROR``, ``DEBUG``) и включает
цветной вывод для логов в консоли. Вы можете также настроить форматы вывода логов и управлять записью в разные файлы.

Примеры использования:
----------------------

.. code-block:: python

    from src.logger.logger import logger
    import colorama # Добавлен импорт colorama для примера

    config = {
       'info_log_path': 'logs/info.log',
       'debug_log_path': 'logs/debug.log',
       'errors_log_path': 'logs/errors.log',
       'json_log_path': 'logs/log.json'
    }

    logger.initialize_loggers(**config)
    logger.info('This is an info message')
    logger.success('This is a success message')
    logger.warning('This is a warning message')
    logger.debug('This is a debug message')
    logger.error('This is an error message')
    logger.critical('This is a critical message')

    logger.info('This message will be green', colors=(colorama.Fore.GREEN, colorama.Back.BLACK))
    logger.error('This message will have a red background', colors=(colorama.Fore.WHITE, colorama.Back.RED))

---

**Классы:**

- :class:`SingletonMeta`: Метакласс, реализующий шаблон Singleton для логгера.
- :class:`JsonFormatter`: Пользовательский форматтер, выводящий логи в формате JSON.
- :class:`Logger`: Основной класс логгера, поддерживающий вывод в консоль, файлы и JSON.

---

**Функции:**

#### `__init__`

   Инициализирует экземпляр Logger с плейсхолдерами для разных типов логгеров (консольный, файловый и JSON).

#### `_configure_logger(name: str, log_path: str, level: Optional[int] = logging.DEBUG, formatter: Optional[logging.Formatter] = None, mode: Optional[str] = 'a') -> logging.Logger`
   
   Конфигурирует и возвращает экземпляр логгера.

   :param name: Имя логгера.
   :type name: str
   :param log_path: Путь к файлу лога.
   :type log_path: str
   :param level: Уровень логирования, например, ``logging.DEBUG``. По умолчанию ``logging.DEBUG``.
   :type level: Optional[int], optional
   :param formatter: Пользовательский форматтер (опционально).
   :type formatter: Optional[logging.Formatter], optional
   :param mode: Режим файла, например, ``'a'`` для добавления (по умолчанию).
   :type mode: Optional[str], optional
   :return: Конфигурированный экземпляр ``logging.Logger``.
   :rtype: logging.Logger

   Пример:

   .. code-block:: python
       
        _configure_logger(name='file', log_path='logs/file.log', level=logging.INFO)
   

#### `initialize_loggers(info_log_path: Optional[str] = '', debug_log_path: Optional[str] = '', errors_log_path: Optional[str] = '', json_log_path: Optional[str] = '')`

   Инициализирует логгеры для консоли и файлов (инфо, дебаг, ошибки и JSON).
   
   :param info_log_path: Путь к файлу для информационных логов (опционально).
   :type info_log_path: Optional[str], optional
   :param debug_log_path: Путь к файлу для отладочных логов (опционально).
   :type debug_log_path: Optional[str], optional
   :param errors_log_path: Путь к файлу для логов ошибок (опционально).
   :type errors_log_path: Optional[str], optional
   :param json_log_path: Путь к файлу для JSON логов (опционально).
   :type json_log_path: Optional[str], optional

   Пример:
   .. code-block:: python

       initialize_loggers(info_log_path='logs/info.log', debug_log_path='logs/debug.log', errors_log_path='logs/errors.log')


#### `log(level, message, ex=None, exc_info=False, color=None)`

   Записывает сообщение на указанном уровне (например, ``INFO``, ``DEBUG``, ``ERROR``) с опциональным исключением и цветовым форматированием.

   :param level: Уровень логирования (например, ``logging.INFO``, ``logging.DEBUG``).
   :type level: int
   :param message: Сообщение лога.
   :type message: str
   :param ex: Опциональное исключение для логирования.
   :type ex: Optional[Exception], optional
   :param exc_info: Включать ли информацию об исключении (по умолчанию ``False``).
   :type exc_info: bool, optional
   :param color: Кортеж с цветами текста и фона для вывода в консоль (опционально).
   :type color: Optional[tuple], optional

   Пример:
   .. code-block:: python

       log(level=logging.INFO, message='This is a test message')

#### `info(message, ex=None, exc_info=False, colors: Optional[tuple] = None)`

   Записывает информационное сообщение.

   :param message: Информационное сообщение для записи.
   :type message: str
   :param ex: Опциональное исключение для записи.
   :type ex: Optional[Exception], optional
   :param exc_info: Включать ли информацию об исключении (по умолчанию ``False``).
   :type exc_info: bool, optional
   :param colors: Кортеж значений цвета для сообщения (опционально).
   :type colors: Optional[tuple], optional

   Пример:
   .. code-block:: python

       info(message='This is an info message')


#### `success(message, ex=None, exc_info=False, colors: Optional[tuple] = None)`

    Записывает сообщение об успешном выполнении.

    :param message: Сообщение об успехе для записи.
    :type message: str
    :param ex: Опциональное исключение для записи.
    :type ex: Optional[Exception], optional
    :param exc_info: Включать ли информацию об исключении (по умолчанию ``False``).
    :type exc_info: bool, optional
    :param colors: Кортеж значений цвета для сообщения (опционально).
    :type colors: Optional[tuple], optional

   Пример:
   .. code-block:: python

       success(message='This is a success message')

#### `warning(message, ex=None, exc_info=False, colors: Optional[tuple] = None)`

   Записывает предупреждающее сообщение.

   :param message: Предупреждающее сообщение для записи.
   :type message: str
   :param ex: Опциональное исключение для записи.
   :type ex: Optional[Exception], optional
   :param exc_info: Включать ли информацию об исключении (по умолчанию ``False``).
   :type exc_info: bool, optional
   :param colors: Кортеж значений цвета для сообщения (опционально).
   :type colors: Optional[tuple], optional

   Пример:
   .. code-block:: python

       warning(message='This is a warning message')

#### `debug(message, ex=None, exc_info=True, colors: Optional[tuple] = None)`

    Записывает отладочное сообщение.

    :param message: Отладочное сообщение для записи.
    :type message: str
    :param ex: Опциональное исключение для записи.
    :type ex: Optional[Exception], optional
    :param exc_info: Включать ли информацию об исключении (по умолчанию ``True``).
    :type exc_info: bool, optional
    :param colors: Кортеж значений цвета для сообщения (опционально).
    :type colors: Optional[tuple], optional

   Пример:
   .. code-block:: python

       debug(message='This is a debug message')

#### `error(message, ex=None, exc_info=True, colors: Optional[tuple] = None)`

    Записывает сообщение об ошибке.

    :param message: Сообщение об ошибке для записи.
    :type message: str
    :param ex: Опциональное исключение для записи.
    :type ex: Optional[Exception], optional
    :param exc_info: Включать ли информацию об исключении (по умолчанию ``True``).
    :type exc_info: bool, optional
    :param colors: Кортеж значений цвета для сообщения (опционально).
    :type colors: Optional[tuple], optional
    
   Пример:
   .. code-block:: python

       error(message='This is an error message')

#### `critical(message, ex=None, exc_info=True, colors: Optional[tuple] = None)`

    Записывает критическое сообщение.

    :param message: Критическое сообщение для записи.
    :type message: str
    :param ex: Опциональное исключение для записи.
    :type ex: Optional[Exception], optional
    :param exc_info: Включать ли информацию об исключении (по умолчанию ``True``).
    :type exc_info: bool, optional
    :param colors: Кортеж значений цвета для сообщения (опционально).
    :type colors: Optional[tuple], optional

   Пример:
   .. code-block:: python

       critical(message='This is a critical message')

---

**Параметры для Logger**

Класс ``Logger`` принимает несколько опциональных параметров для настройки поведения логирования.

- **Level**: Управляет уровнем важности регистрируемых логов. Общие уровни включают:
  - ``logging.DEBUG``: Подробная информация, полезная для диагностики проблем.
  - ``logging.INFO``: Общая информация, например, об успешных операциях.
  - ``logging.WARNING``: Предупреждения, не требующие немедленных действий.
  - ``logging.ERROR``: Сообщения об ошибках.
  - ``logging.CRITICAL``: Критические ошибки, требующие немедленного внимания.

- **Formatter**: Определяет формат сообщений лога. По умолчанию, сообщения форматируются как ``'%(asctime)s - %(levelname)s - %(message)s'``. Вы можете предоставить пользовательский форматтер для разных форматов, например, JSON.

- **Color**: Цвета для сообщений лога в консоли. Цвета задаются в виде кортежа из двух элементов:
  - **Цвет текста**: Задает цвет текста (например, ``colorama.Fore.RED``).
  - **Цвет фона**: Задает цвет фона (например, ``colorama.Back.WHITE``).

Цвет можно настроить для разных уровней логирования (например, зеленый для информации, красный для ошибок и т.д.).

---

**Конфигурация файлового логирования (config)**

Чтобы записывать сообщения в файл, вы можете указать пути к файлам в конфигурации.

.. code-block:: python

    config = {
        'info_log_path': 'logs/info.log',
        'debug_log_path': 'logs/debug.log',
        'errors_log_path': 'logs/errors.log',
        'json_log_path': 'logs/log.json'
    }

Пути к файлам, указанные в ``config``, используются для записи логов в соответствующие файлы для каждого уровня логирования.

---

**Пример использования**

#### 1. Инициализация логгера:

.. code-block:: python

   from src.logger.logger import logger # Correct import
   config = {
       'info_log_path': 'logs/info.log',
       'debug_log_path': 'logs/debug.log',
       'errors_log_path': 'logs/errors.log',
       'json_log_path': 'logs/log.json'
   }
   logger.initialize_loggers(**config)

#### 2. Логирование сообщений на разных уровнях:

.. code-block:: python

    from src.logger.logger import logger

    logger.info('This is an info message')
    logger.success('This is a success message')
    logger.warning('This is a warning message')
    logger.debug('This is a debug message')
    logger.error('This is an error message')
    logger.critical('This is a critical message')

#### 3. Настройка цветов:

.. code-block:: python
    
    from src.logger.logger import logger
    import colorama # Import colorama for example

    logger.info('This message will be green', colors=(colorama.Fore.GREEN, colorama.Back.BLACK))
    logger.error('This message will have a red background', colors=(colorama.Fore.WHITE, colorama.Back.RED))

---

Этот модуль предоставляет комплексную и гибкую систему логирования для Python-приложений. Вы можете настраивать логирование в консоль и файлы с разными форматами и цветами, управлять уровнями логирования и обрабатывать исключения. Конфигурация для файлового логирования хранится в словаре ``config``, что позволяет легко настраивать его.
```