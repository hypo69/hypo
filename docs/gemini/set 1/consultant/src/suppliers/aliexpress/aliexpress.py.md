# Улучшенный код
```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
Модуль для работы с AliExpress.
=========================================================================================

Этот модуль предоставляет класс :class:`Aliexpress`, который объединяет функциональность
из классов :class:`Supplier`, :class:`AliRequests` и :class:`AliApi` для взаимодействия с AliExpress.

Пример использования
--------------------

Пример использования класса `Aliexpress`:

.. code-block:: python

    # Запуск без веб-драйвера
    a = Aliexpress()

    # Запуск с веб-драйвером Chrome
    a = Aliexpress('chrome')

    # Запуск в режиме запросов
    a = Aliexpress(requests=True)
"""


import pickle
import threading
from requests.sessions import Session
from fake_useragent import UserAgent
from pathlib import Path
from typing import Union, Any
from requests.cookies import RequestsCookieJar
from urllib.parse import urlparse

from src import gs
from src.suppliers.supplier import Supplier
from .alirequests import AliRequests
from .aliapi import AliApi
from src.logger.logger import logger


class Aliexpress(Supplier, AliRequests, AliApi):
    """
    Базовый класс для работы с AliExpress.

    Этот класс объединяет функциональность классов :class:`Supplier`, :class:`AliRequests` и :class:`AliApi`
    для упрощения взаимодействия с AliExpress.

    **Примеры использования**:

    .. code-block:: python

        # Запуск без веб-драйвера
        a = Aliexpress()

        # Запуск с веб-драйвером Chrome
        a = Aliexpress('chrome')

        # Запуск в режиме запросов
        a = Aliexpress(requests=True)
    """
    ...

    def __init__(self,
                 webdriver: bool | str = False,
                 locale: str | dict = {'EN': 'USD'},
                 *args: Any, **kwargs: Any) -> None:
        """
        Инициализация класса Aliexpress.

        :param webdriver: Режим веб-драйвера. Поддерживаемые значения:
            - `False` (по умолчанию): Без веб-драйвера.
            - `'chrome'`: Использовать веб-драйвер Chrome.
            - `'mozilla'`: Использовать веб-драйвер Mozilla.
            - `'edge'`: Использовать веб-драйвер Edge.
            - `'default'`: Использовать системный веб-драйвер по умолчанию.
        :type webdriver: bool | str

        :param locale: Настройки языка и валюты для скрипта.
        :type locale: str | dict

        :param args: Дополнительные позиционные аргументы.
        :param kwargs: Дополнительные именованные аргументы.

        **Примеры**:

        .. code-block:: python

            # Запуск без веб-драйвера
            a = Aliexpress()

            # Запуск с веб-драйвером Chrome
            a = Aliexpress('chrome')

        """
        ...
        super().__init__(supplier_prefix='aliexpress',
                         locale=locale,
                         webdriver=webdriver,
                         *args, **kwargs)
```
# Внесённые изменения
- Добавлены docstring в формате reStructuredText (RST) для модуля и класса.
- Добавлены типы для параметров `__init__` и возвращаемого значения.
- Добавлены комментарии RST для параметров `__init__`.
- Добавлены примеры использования в docstring класса и функции `__init__`.
- Добавлен импорт `Any` из `typing`.
- Убраны лишние комментарии с `#` после docstring.
- Заменено `json.load` на `j_loads` или `j_loads_ns` если это необходимо (в данном файле не требуется).
- Все комментарии после `#` описывают следующий блок кода.

# Оптимизированный код
```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
Модуль для работы с AliExpress.
=========================================================================================

Этот модуль предоставляет класс :class:`Aliexpress`, который объединяет функциональность
из классов :class:`Supplier`, :class:`AliRequests` и :class:`AliApi` для взаимодействия с AliExpress.

Пример использования
--------------------

Пример использования класса `Aliexpress`:

.. code-block:: python

    # Запуск без веб-драйвера
    a = Aliexpress()

    # Запуск с веб-драйвером Chrome
    a = Aliexpress('chrome')

    # Запуск в режиме запросов
    a = Aliexpress(requests=True)
"""


import pickle
import threading
from requests.sessions import Session
from fake_useragent import UserAgent
from pathlib import Path
from typing import Union, Any
from requests.cookies import RequestsCookieJar
from urllib.parse import urlparse

from src import gs
from src.suppliers.supplier import Supplier
from .alirequests import AliRequests
from .aliapi import AliApi
from src.logger.logger import logger


class Aliexpress(Supplier, AliRequests, AliApi):
    """
    Базовый класс для работы с AliExpress.

    Этот класс объединяет функциональность классов :class:`Supplier`, :class:`AliRequests` и :class:`AliApi`
    для упрощения взаимодействия с AliExpress.

    **Примеры использования**:

    .. code-block:: python

        # Запуск без веб-драйвера
        a = Aliexpress()

        # Запуск с веб-драйвером Chrome
        a = Aliexpress('chrome')

        # Запуск в режиме запросов
        a = Aliexpress(requests=True)
    """
    ...

    def __init__(self,
                 webdriver: bool | str = False,
                 locale: str | dict = {'EN': 'USD'},
                 *args: Any, **kwargs: Any) -> None:
        """
        Инициализация класса Aliexpress.

        :param webdriver: Режим веб-драйвера. Поддерживаемые значения:
            - `False` (по умолчанию): Без веб-драйвера.
            - `'chrome'`: Использовать веб-драйвер Chrome.
            - `'mozilla'`: Использовать веб-драйвер Mozilla.
            - `'edge'`: Использовать веб-драйвер Edge.
            - `'default'`: Использовать системный веб-драйвер по умолчанию.
        :type webdriver: bool | str

        :param locale: Настройки языка и валюты для скрипта.
        :type locale: str | dict

        :param args: Дополнительные позиционные аргументы.
        :param kwargs: Дополнительные именованные аргументы.

        **Примеры**:

        .. code-block:: python

            # Запуск без веб-драйвера
            a = Aliexpress()

            # Запуск с веб-драйвером Chrome
            a = Aliexpress('chrome')

        """
        # Код инициализирует родительский класс Supplier с заданными параметрами
        super().__init__(supplier_prefix='aliexpress',
                         locale=locale,
                         webdriver=webdriver,
                         *args, **kwargs)