# Анализ кода модуля `customer.py`

**Качество кода**

8/10
-   Плюсы
    -   Код структурирован и разбит на классы и методы, что облегчает его понимание и поддержку.
    -   Используется класс `SimpleNamespace` для гибкой передачи параметров конфигурации.
    -   Используется `logger` для логирования ошибок.
    -   Присутствует базовая документация в формате docstring.
    -   Используется `j_loads` для загрузки json
-   Минусы
    -   Не все комментарии соответствуют reStructuredText.
    -   Не хватает обработки ошибок в методах класса.
    -   Необходимо добавить подробную документацию к методам класса.
    -   Импорты не отсортированы и не сгруппированы.
    -   Не все методы класса имеют описание.

**Рекомендации по улучшению**

1.  **Документация:** Переписать docstring и комментарии в reStructuredText (RST) формате.
2.  **Импорты:** Отсортировать и сгруппировать импорты по категориям (стандартные, сторонние, локальные).
3.  **Обработка ошибок:** Улучшить обработку ошибок, используя `try-except` блоки и логирование.
4.  **Логирование:**  Убедиться, что все ошибки логируются с помощью `logger.error`.
5.  **Комментарии:** Добавить детальные комментарии к коду, объясняющие его логику.
6.  **Проверки:** Добавить проверки валидности данных.
7.  **Названия:** Привести в соответствие имена переменных и функций с общим стилем проекта.
8.  **Объект `credentials`:** Уточнить использование `credentials` и добавить документацию для него.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для работы с клиентами PrestaShop
========================================

Этот модуль предоставляет класс :class:`PrestaCustomer` для управления клиентами через API PrestaShop.

.. code-block:: python

    from src.endpoints.prestashop.customer import PrestaCustomer

    # Пример использования
    prestacustomer = PrestaCustomer(api_domain="your_domain", api_key="your_api_key")
    customer_id = prestacustomer.add_customer_PrestaShop("John Doe", "johndoe@example.com")
    prestacustomer.delete_customer_PrestaShop(customer_id)
    prestacustomer.update_customer_PrestaShop(customer_id, "Updated Name")
    customer_data = prestacustomer.get_customer_details_PrestaShop(customer_id)

"""
import os
import sys
from pathlib import Path
from typing import Optional, Union
from types import SimpleNamespace

from attr import attrs, attrib

# from src import gs # TODO проверить необходимость
# from src.utils.jjson import j_loads # TODO проверить необходимость
from src.logger.logger import logger  # TODO добавить обработку всех ошибок через logger
from src.logger.exceptions import PrestaShopException
from .api import PrestaShop


MODE = 'dev'  # TODO: проверить необходимость переменной и ее использование.


@attrs
class PrestaCustomer(PrestaShop):
    """
    Класс для работы с клиентами в PrestaShop.

    Предоставляет методы для добавления, удаления, обновления и получения информации о клиентах.

    :param credentials: (Optional[dict | SimpleNamespace]) Словарь или SimpleNamespace с параметрами 'api_domain' и 'api_key'.
    :param api_domain: (Optional[str]) Домен API PrestaShop.
    :param api_key: (Optional[str]) Ключ API PrestaShop.

    Пример использования:

    .. code-block:: python

        prestacustomer = PrestaCustomer(api_domain='your_api_domain', api_key='your_api_key')
        customer_id = prestacustomer.add_customer_PrestaShop('John Doe', 'johndoe@example.com')
        prestacustomer.delete_customer_PrestaShop(customer_id)
        prestacustomer.update_customer_PrestaShop(customer_id, 'Updated Customer Name')
        customer_details = prestacustomer.get_customer_details_PrestaShop(customer_id)
        print(customer_details)
    """
    
    def __init__(self, 
                 credentials: Optional[dict | SimpleNamespace] = None, 
                 api_domain: Optional[str] = None, 
                 api_key: Optional[str] = None, 
                 *args, **kwards):
        """
        Инициализация клиента PrestaShop.

        Инициализирует класс PrestaCustomer с данными для подключения к API PrestaShop.

        :param credentials: (Optional[dict | SimpleNamespace]) Словарь или SimpleNamespace с параметрами 'api_domain' и 'api_key'.
        :param api_domain: (Optional[str]) Домен API.
        :param api_key: (Optional[str]) Ключ API.
        :raises ValueError: Если api_domain или api_key не предоставлены.
        """
        #  Проверка наличия учетных данных
        if credentials:
            api_domain = getattr(credentials, 'api_domain', None) or credentials.get('api_domain', api_domain)
            api_key = getattr(credentials, 'api_key', None) or credentials.get('api_key', api_key)

        #  Проверка наличия обязательных параметров
        if not api_domain or not api_key:
             # Логирование ошибки
            logger.error("Необходимо передать оба параметра: api_domain и api_key.")
            raise ValueError('Необходимы оба параметра: api_domain и api_key.')

        # Вызов конструктора родительского класса
        super().__init__(api_domain, api_key, *args, **kwards)

    def add_customer_PrestaShop(self, customer_name: str, email: str) -> Optional[int]:
        """
        Добавляет нового клиента в PrestaShop.

        :param customer_name: Имя клиента.
        :param email: Email клиента.
        :return: ID добавленного клиента или None в случае ошибки.
        """
        # Данные клиента для добавления
        customer_data = {
             'customer': {
                 'firstname': customer_name.split(' ')[0], # TODO доработать логику разбиения имени
                 'lastname': customer_name.split(' ')[-1] , # TODO доработать логику разбиения имени
                'email': email,
                'passwd': 'password1234',  # TODO: Генерация пароля
                'id_gender': 1, # TODO: Конфигурация пола
                'active': 1, # TODO: Конфигурация активности
            }
        }
        
        try:
             # Выполнение запроса к API
            response = self.add('customers', customer_data)
            if response and 'customer' in response:
                # Возврат ID нового клиента
                return response['customer']['id']
            else:
                logger.error(f'Ошибка при добавлении клиента: {response=}')
                return None
        except Exception as e:
             # Логирование ошибки
            logger.error(f'Ошибка при добавлении клиента: {e}')
            return None

    def delete_customer_PrestaShop(self, customer_id: int) -> bool:
        """
        Удаляет клиента из PrestaShop по ID.
        
        :param customer_id: ID клиента для удаления.
        :return: True если удаление успешно, False в случае ошибки.
        """
        #  Выполнение запроса к API
        try:
            response = self.delete('customers', customer_id)
            if response is True:
                return True
            else:
               logger.error(f'Ошибка при удалении клиента с id: {customer_id=}. {response=}')
               return False
        except Exception as e:
             # Логирование ошибки
            logger.error(f'Ошибка при удалении клиента с id: {customer_id=}. {e=}')
            return False
    
    def update_customer_PrestaShop(self, customer_id: int, customer_name: str) -> bool:
        """
        Обновляет данные клиента в PrestaShop.

        :param customer_id: ID клиента для обновления.
        :param customer_name: Новое имя клиента.
        :return: True если обновление прошло успешно, False если возникла ошибка.
        """
        #  Подготовка данных для обновления
        customer_data = {
             'customer': {
                 'id': customer_id,
                 'firstname': customer_name.split(' ')[0], # TODO доработать логику разбиения имени
                 'lastname': customer_name.split(' ')[-1] # TODO доработать логику разбиения имени
            }
        }
        try:
             # Выполнение запроса к API
            response = self.update('customers', customer_id, customer_data)
            if response and 'customer' in response:
                 # Проверка успешности обновления
                return True
            else:
                 # Логирование ошибки
                logger.error(f'Ошибка при обновлении клиента c id: {customer_id=}. {response=}')
                return False
        except Exception as e:
             # Логирование ошибки
            logger.error(f'Ошибка при обновлении клиента c id: {customer_id=}. {e=}')
            return False

    def get_customer_details_PrestaShop(self, customer_id: int) -> Optional[dict]:
        """
        Получает детали клиента из PrestaShop по ID.

        :param customer_id: ID клиента.
        :return: Словарь с деталями клиента или None в случае ошибки.
        """
        try:
             # Выполнение запроса к API
            response = self.get('customers', customer_id)
            if response and 'customer' in response:
                #  Возврат данных клиента
                return response['customer']
            else:
                logger.error(f'Ошибка получения данных о клиенте с id: {customer_id=}. {response=}')
                return None
        except Exception as e:
             # Логирование ошибки
            logger.error(f'Ошибка при получении данных о клиенте с id: {customer_id=}. {e=}')
            return None

```