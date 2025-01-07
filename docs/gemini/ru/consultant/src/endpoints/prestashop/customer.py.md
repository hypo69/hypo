# Анализ кода модуля `customer.py`

**Качество кода**
7
-  Плюсы
    - Код имеет базовую структуру, включающую класс `PrestaCustomer` для работы с клиентами PrestaShop.
    - Используется `logger` для логирования ошибок.
    - Есть docstring для класса и метода `__init__`, что облегчает понимание их назначения.
-  Минусы
    - Отсутствуют docstring для остальных методов класса, что затрудняет понимание их работы.
    - Используется `j_loads` из `src.utils.jjson`, но не используется `j_loads_ns`, что было бы более согласованно.
    - Отсутствует обработка исключений при обращении к API PrestaShop, что может привести к необработанным ошибкам.
    - Присутствует дублирование импорта `from src.logger.logger import logger`.
    - Использована конструкция `if credentials is not None:`, которая может быть упрощена.
    - Не использованы f-строки для форматирования строк.

**Рекомендации по улучшению**

1.  **Добавить docstring для всех методов**: Документировать каждый метод класса, включая параметры, возвращаемые значения и описание работы.
2.  **Использовать `j_loads_ns`**: Для консистентности и для будущих улучшений в рамках проекта.
3.  **Обработка исключений**: Добавить `try-except` блоки для обработки возможных ошибок API PrestaShop с использованием `logger.error` для логирования.
4.  **Устранить дублирование импорта**: Удалить повторяющийся импорт `from src.logger.logger import logger`.
5.  **Упростить инициализацию**: Упростить код инициализации, чтобы сделать его более читаемым.
6.  **Использовать f-строки**: Использовать f-строки для форматирования строк.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
Модуль для работы с клиентами PrestaShop.
=========================================================================================

Этот модуль содержит класс :class:`PrestaCustomer`, который используется для выполнения операций с клиентами в PrestaShop,
включая добавление, удаление, обновление и получение информации о клиентах.

Пример использования
--------------------

Пример использования класса `PrestaCustomer`:

.. code-block:: python

    prestacustomer = PrestaCustomer(api_domain='your_api_domain', api_key='your_api_key')
    prestacustomer.add_customer_PrestaShop('John Doe', 'johndoe@example.com')
    prestacustomer.delete_customer_PrestaShop(3)
    prestacustomer.update_customer_PrestaShop(4, 'Updated Customer Name')
    print(prestacustomer.get_customer_details_PrestaShop(5))
"""


import sys
import os
from attr import attr, attrs
from pathlib import Path
from typing import Union
from types import SimpleNamespace
from typing import Optional

import header
from src import gs
from src.logger.logger import logger
from src.utils.jjson import j_loads, j_loads_ns  # Используем j_loads_ns
from .api import PrestaShop
from src.logger.exceptions import PrestaShopException


class PrestaCustomer(PrestaShop):
    """
    Класс для работы с клиентами в PrestaShop.

    :param credentials: Словарь или объект SimpleNamespace с параметрами `api_domain` и `api_key`.
    :type credentials: Optional[dict | SimpleNamespace]
    :param api_domain: Домен API.
    :type api_domain: Optional[str]
    :param api_key: Ключ API.
    :type api_key: Optional[str]

    Пример использования класса:

    .. code-block:: python

        prestacustomer = PrestaCustomer(API_DOMAIN=API_DOMAIN, API_KEY=API_KEY)
        prestacustomer.add_customer_PrestaShop('John Doe', 'johndoe@example.com')
        prestacustomer.delete_customer_PrestaShop(3)
        prestacustomer.update_customer_PrestaShop(4, 'Updated Customer Name')
        print(prestacustomer.get_customer_details_PrestaShop(5))
    """
    
    def __init__(self, 
                 credentials: Optional[dict | SimpleNamespace] = None, 
                 api_domain: Optional[str] = None, 
                 api_key: Optional[str] = None, 
                 *args, **kwards):
        """
        Инициализация клиента PrestaShop.

        :param credentials: Словарь или объект SimpleNamespace с параметрами `api_domain` и `api_key`.
        :type credentials: Optional[dict | SimpleNamespace]
        :param api_domain: Домен API.
        :type api_domain: Optional[str]
        :param api_key: Ключ API.
        :type api_key: Optional[str]
        """
        # код исполняет присваивание api_domain и api_key из credentials, если они предоставлены.
        if credentials:
            api_domain = credentials.get('api_domain', api_domain)
            api_key = credentials.get('api_key', api_key)
        
        # код исполняет проверку наличия api_domain и api_key и выбрасывает исключение, если они не предоставлены.
        if not (api_domain and api_key):
            raise ValueError('Необходимы оба параметра: api_domain и api_key.')
        
        # код исполняет инициализацию родительского класса PrestaShop.
        super().__init__(api_domain, api_key, *args, **kwards)

    def add_customer_PrestaShop(self, name: str, email: str) -> Union[dict, None]:
        """
        Добавляет нового клиента в PrestaShop.

        :param name: Имя клиента.
        :type name: str
        :param email: Email клиента.
        :type email: str
        :return: Ответ API или None в случае ошибки.
        :rtype: Union[dict, None]
        """
        try:
            # код исполняет отправку запроса на добавление клиента в PrestaShop API.
            response = self.add(resource='customers', data={'firstname': name, 'email': email})
            return response
        except PrestaShopException as e:
            logger.error(f'Ошибка при добавлении клиента {name}: {e}')
            return None
    
    def delete_customer_PrestaShop(self, customer_id: int) -> bool:
        """
        Удаляет клиента из PrestaShop по ID.
    
        :param customer_id: ID клиента для удаления.
        :type customer_id: int
        :return: True в случае успеха, False в случае ошибки.
        :rtype: bool
        """
        try:
            # код исполняет отправку запроса на удаление клиента по ID.
            self.delete(resource='customers', id=customer_id)
            return True
        except PrestaShopException as e:
            logger.error(f'Ошибка при удалении клиента с ID {customer_id}: {e}')
            return False
    
    def update_customer_PrestaShop(self, customer_id: int, name: str) -> Union[dict, None]:
        """
        Обновляет данные клиента в PrestaShop по ID.
        
        :param customer_id: ID клиента для обновления.
        :type customer_id: int
        :param name: Новое имя клиента.
        :type name: str
        :return: Ответ API или None в случае ошибки.
        :rtype: Union[dict, None]
        """
        try:
           # код исполняет отправку запроса на обновление клиента по ID.
           response = self.update(resource='customers', id=customer_id, data={'firstname': name})
           return response
        except PrestaShopException as e:
            logger.error(f'Ошибка при обновлении клиента с ID {customer_id}: {e}')
            return None
    
    def get_customer_details_PrestaShop(self, customer_id: int) -> Union[dict, None]:
        """
        Получает данные клиента из PrestaShop по ID.
        
        :param customer_id: ID клиента для получения данных.
        :type customer_id: int
        :return: Ответ API или None в случае ошибки.
        :rtype: Union[dict, None]
        """
        try:
            # код исполняет отправку запроса на получение данных клиента по ID.
            response = self.get(resource='customers', id=customer_id)
            return response
        except PrestaShopException as e:
            logger.error(f'Ошибка при получении данных клиента с ID {customer_id}: {e}')
            return None
```