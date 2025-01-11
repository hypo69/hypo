### Анализ кода модуля `src.logger`

**Качество кода**:
- **Соответствие стандартам**: 8
- **Плюсы**:
    - Хорошая структура документации, описывающая основные компоненты модуля.
    - Подробное описание классов, функций и параметров.
    - Наличие примеров использования.
    - Использование `rst` для форматирования.
- **Минусы**:
    - Отсутствуют явные RST-блоки кода для примеров.
    - Нет единого стиля в описании параметров (используются и `**Parameters:**` и `Parameters:`).
    - Некоторые параметры в описаниях дублируются, например, в функциях `info`, `success` и т.д.
    - Нет ссылок на код (например, как импортировать `logger` и использовать `config`).
    - Не указано использование `from src.logger import logger`.
    - Описания функций не соответствуют стилю RST.
    - Описание `config` не соответствует стандарту.

**Рекомендации по улучшению**:
- Устранить дублирование описаний параметров, используя общую формулировку для похожих функций.
- Добавить примеры кода с использованием блоков `code-block:: python`, чтобы показать, как правильно инициализировать и использовать logger.
- Использовать `from src.logger import logger` и показать пример в документации.
- Переписать описания функций в соответствии со стандартом RST.
- Описание `config` перенести в блок `code-block:: python`.
- Добавить в документацию пример с `JsonFormatter`.

**Оптимизированный код**:
```rst
.. module:: src.logger

==================================================
Документация для модуля `src.logger`
==================================================

Модуль `src.logger` предоставляет гибкую систему логирования, поддерживающую вывод в консоль, файл и JSON. 
Он использует шаблон Singleton, чтобы гарантировать наличие только одного экземпляра логгера в приложении. 
Логгер поддерживает различные уровни логирования (например, `INFO`, `ERROR`, `DEBUG`) и цветной вывод для консольных логов. 
Также можно настроить форматы вывода логов и управлять логированием в разные файлы.

.. note::
    В данном модуле используется ``from src.logger import logger``

---

Классы:
--------
- **SingletonMeta**: Метакласс, реализующий шаблон Singleton для логгера.
- **JsonFormatter**: Пользовательский форматер, выводящий логи в формате JSON.
- **Logger**: Основной класс логгера, поддерживающий вывод в консоль, файл и JSON.

---

Функции:
----------

.. code-block:: python

    def __init__(self):
        """
        Инициализирует экземпляр Logger с заполнителями для различных типов логгеров (консоль, файл и JSON).
        """
        ...

.. code-block:: python

    def _configure_logger(
        name: str,
        log_path: str,
        level: int = logging.DEBUG,
        formatter: logging.Formatter = None,
        mode: str = 'a'
    ) -> logging.Logger:
        """
        Настраивает и возвращает экземпляр логгера.

        :param name: Имя логгера.
        :type name: str
        :param log_path: Путь к файлу лога.
        :type log_path: str
        :param level: Уровень логирования, например, `logging.DEBUG`. По умолчанию `logging.DEBUG`.
        :type level: int, optional
        :param formatter: Пользовательский форматер (необязательно).
        :type formatter: logging.Formatter, optional
        :param mode: Режим файла, например, `'a'` для добавления (по умолчанию).
        :type mode: str, optional
        :return: Настроенный экземпляр `logging.Logger`.
        :rtype: logging.Logger

        Пример:
           >>> logger = _configure_logger('test', 'logs/test.log')
        """
        ...

.. code-block:: python

    def initialize_loggers(
        info_log_path: str = '',
        debug_log_path: str = '',
        errors_log_path: str = '',
        json_log_path: str = ''
    ):
        """
        Инициализирует логгеры для консоли и файлового логирования (info, debug, error и JSON).

        :param info_log_path: Путь к файлу info-логов (необязательно).
        :type info_log_path: str, optional
        :param debug_log_path: Путь к файлу debug-логов (необязательно).
        :type debug_log_path: str, optional
        :param errors_log_path: Путь к файлу error-логов (необязательно).
        :type errors_log_path: str, optional
        :param json_log_path: Путь к файлу JSON-логов (необязательно).
        :type json_log_path: str, optional

        Пример:
           >>> config = {
           ...    'info_log_path': 'logs/info.log',
           ...    'debug_log_path': 'logs/debug.log',
           ...    'errors_log_path': 'logs/errors.log',
           ...    'json_log_path': 'logs/log.json'
           ... }
           >>> logger = Logger()
           >>> logger.initialize_loggers(**config)
        """
        ...

.. code-block:: python

    def log(
        level: int,
        message: str,
        ex: Exception = None,
        exc_info: bool = False,
        color: tuple = None
    ):
        """
        Записывает сообщение в лог с указанным уровнем (например, `INFO`, `DEBUG`, `ERROR`) с необязательным исключением и цветным форматированием.

        :param level: Уровень логирования (например, `logging.INFO`, `logging.DEBUG`).
        :type level: int
        :param message: Сообщение лога.
        :type message: str
        :param ex: Необязательное исключение для записи в лог.
        :type ex: Exception, optional
        :param exc_info: Включать ли информацию об исключении (по умолчанию `False`).
        :type exc_info: bool, optional
        :param color: Кортеж с цветами текста и фона для вывода в консоль (необязательно).
        :type color: tuple, optional

        Пример:
           >>> logger.log(logging.INFO, 'This is an info message')
        """
        ...
   
.. code-block:: python

    def info(
        message: str,
        ex: Exception = None,
        exc_info: bool = False,
        colors: tuple = None
    ):
        """
        Записывает информационное сообщение в лог.

        :param message: Информационное сообщение для записи в лог.
        :type message: str
        :param ex: Необязательное исключение для записи в лог.
        :type ex: Exception, optional
        :param exc_info: Включать ли информацию об исключении (по умолчанию `False`).
        :type exc_info: bool, optional
        :param colors: Кортеж цветов для сообщения (необязательно).
        :type colors: tuple, optional

        Пример:
           >>> logger.info('This is an info message')
        """
        ...
    
.. code-block:: python

    def success(
        message: str,
        ex: Exception = None,
        exc_info: bool = False,
        colors: tuple = None
    ):
        """
        Записывает сообщение об успехе в лог.

        :param message: Сообщение об успехе для записи в лог.
        :type message: str
        :param ex: Необязательное исключение для записи в лог.
        :type ex: Exception, optional
        :param exc_info: Включать ли информацию об исключении (по умолчанию `False`).
        :type exc_info: bool, optional
        :param colors: Кортеж цветов для сообщения (необязательно).
        :type colors: tuple, optional

        Пример:
           >>> logger.success('This is a success message')
        """
        ...
    
.. code-block:: python

    def warning(
        message: str,
        ex: Exception = None,
        exc_info: bool = False,
        colors: tuple = None
    ):
        """
        Записывает предупреждающее сообщение в лог.

        :param message: Предупреждающее сообщение для записи в лог.
        :type message: str
        :param ex: Необязательное исключение для записи в лог.
        :type ex: Exception, optional
        :param exc_info: Включать ли информацию об исключении (по умолчанию `False`).
        :type exc_info: bool, optional
        :param colors: Кортеж цветов для сообщения (необязательно).
        :type colors: tuple, optional

        Пример:
           >>> logger.warning('This is a warning message')
        """
        ...

.. code-block:: python

    def debug(
        message: str,
        ex: Exception = None,
        exc_info: bool = True,
        colors: tuple = None
    ):
        """
        Записывает отладочное сообщение в лог.

        :param message: Отладочное сообщение для записи в лог.
        :type message: str
        :param ex: Необязательное исключение для записи в лог.
        :type ex: Exception, optional
        :param exc_info: Включать ли информацию об исключении (по умолчанию `True`).
        :type exc_info: bool, optional
        :param colors: Кортеж цветов для сообщения (необязательно).
        :type colors: tuple, optional

        Пример:
           >>> logger.debug('This is a debug message')
        """
        ...

.. code-block:: python

    def error(
        message: str,
        ex: Exception = None,
        exc_info: bool = True,
        colors: tuple = None
    ):
        """
        Записывает сообщение об ошибке в лог.

        :param message: Сообщение об ошибке для записи в лог.
        :type message: str
        :param ex: Необязательное исключение для записи в лог.
        :type ex: Exception, optional
        :param exc_info: Включать ли информацию об исключении (по умолчанию `True`).
        :type exc_info: bool, optional
        :param colors: Кортеж цветов для сообщения (необязательно).
        :type colors: tuple, optional

        Пример:
           >>> logger.error('This is an error message')
        """
        ...

.. code-block:: python

    def critical(
        message: str,
        ex: Exception = None,
        exc_info: bool = True,
        colors: tuple = None
    ):
        """
        Записывает критическое сообщение в лог.

        :param message: Критическое сообщение для записи в лог.
        :type message: str
        :param ex: Необязательное исключение для записи в лог.
        :type ex: Exception, optional
        :param exc_info: Включать ли информацию об исключении (по умолчанию `True`).
        :type exc_info: bool, optional
        :param colors: Кортеж цветов для сообщения (необязательно).
        :type colors: tuple, optional
        
        Пример:
           >>> logger.critical('This is a critical message')
        """
        ...


---

Параметры логгера:
---------------------

Класс `Logger` принимает несколько необязательных параметров для настройки поведения логирования.

- **Уровень**: Определяет уровень важности логов. Общие уровни включают:
    - `logging.DEBUG`: Подробная информация, полезная для диагностики проблем.
    - `logging.INFO`: Общая информация, например, об успешных операциях.
    - `logging.WARNING`: Предупреждения, которые не требуют немедленного действия.
    - `logging.ERROR`: Сообщения об ошибках.
    - `logging.CRITICAL`: Критические ошибки, требующие немедленного внимания.

- **Форматер**: Определяет формат сообщений лога. По умолчанию сообщения форматируются как `'%(asctime)s - %(levelname)s - %(message)s'`. Можно предоставить собственный форматер для различных форматов, например, JSON.

- **Цвет**: Цвета для сообщений лога в консоли. Цвета указываются в виде кортежа с двумя элементами:
    - **Цвет текста**: Указывает цвет текста (например, `colorama.Fore.RED`).
    - **Цвет фона**: Указывает цвет фона (например, `colorama.Back.WHITE`).

Цвет можно настроить для разных уровней логирования (например, зеленый для info, красный для ошибок и т.д.).

---

Конфигурация файлового логирования (`config`):
------------------------------------------

Для записи сообщений в файл можно указать пути к файлам в конфигурации.

.. code-block:: python

    config = {
        'info_log_path': 'logs/info.log',
        'debug_log_path': 'logs/debug.log',
        'errors_log_path': 'logs/errors.log',
        'json_log_path': 'logs/log.json'
    }

Пути к файлам, предоставленные в `config`, используются для записи логов в соответствующие файлы для каждого уровня логирования.

---

Примеры использования
----------------------

#### 1. Инициализация логгера:
.. code-block:: python

    from src.logger import logger
    config = {
        'info_log_path': 'logs/info.log',
        'debug_log_path': 'logs/debug.log',
        'errors_log_path': 'logs/errors.log',
        'json_log_path': 'logs/log.json'
    }
    logger.initialize_loggers(**config)

#### 2. Запись сообщений с разными уровнями:
.. code-block:: python

    logger.info('Это информационное сообщение')
    logger.success('Это сообщение об успехе')
    logger.warning('Это предупреждающее сообщение')
    logger.debug('Это отладочное сообщение')
    logger.error('Это сообщение об ошибке')
    logger.critical('Это критическое сообщение')

#### 3. Настройка цветов:
.. code-block:: python

    import colorama
    logger.info('Это сообщение будет зеленым', colors=(colorama.Fore.GREEN, colorama.Back.BLACK))
    logger.error('Это сообщение будет с красным фоном', colors=(colorama.Fore.WHITE, colorama.Back.RED))

#### 4. Использование `JsonFormatter`:
.. code-block:: python
    import logging
    from src.logger import JsonFormatter
    
    json_formatter = JsonFormatter()
    logger = Logger()
    logger.initialize_loggers(json_log_path='logs/json.log')
    
    logger.json_logger.setFormatter(json_formatter)
    logger.info('This message will be formatted as json')
   
---

Этот модуль предоставляет комплексную и гибкую систему логирования для Python-приложений. 
Вы можете настроить логирование в консоль и файлы с различными форматами и цветами, управлять уровнями логирования и обрабатывать исключения.
Конфигурация для файлового логирования хранится в словаре `config`, что позволяет легко настраивать его.