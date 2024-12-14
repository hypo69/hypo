# Анализ кода модуля `category.py`

**Качество кода**
8
-  Плюсы
    - Код имеет базовую структуру для работы с категориями PrestaShop.
    - Используется `logger` для логирования ошибок и отладки.
    - Присутствуют docstring для класса и методов.
    - Код соответствует PEP 8.
-  Минусы
    -  Отсутствуют docstring для параметров и возвращаемых значений в функциях.
    -  Использование `try-except` не стандартизировано и не соответствует заданию.
    -  Использование `j_loads` не наблюдается.
    -  Смешанный стиль комментариев (RST и `#`).
    -  Не все комментарии соответствуют стандарту RST.
    -  Не все переменные аннотированы.
    -  `MODE` не используется и является лишней переменной

**Рекомендации по улучшению**
1.  Добавить docstring для всех параметров и возвращаемых значений в функциях в формате RST.
2.  Убрать лишние `try-except` блоки и использовать `logger.error` для обработки ошибок.
3.  Использовать `j_loads` для чтения файлов, если это необходимо.
4.  Унифицировать стиль комментариев, привести все в RST.
5.  Удалить неиспользуемую переменную `MODE`.
6.  Добавить аннотации типов.

**Оптимизированный код**

```python
"""
Модуль для работы с категориями PrestaShop.
=========================================================================================

Этот модуль содержит класс :class:`PrestaCategory`, который используется для работы с категориями в PrestaShop,
включая добавление, удаление, обновление и получение списка родительских категорий.

Пример использования
--------------------

Пример использования класса `PrestaCategory`:

.. code-block:: python

    prestacategory = PrestaCategory(API_DOMAIN='your_api_domain', API_KEY='your_api_key')
    prestacategory.add_category_PrestaShop('New Category', 'Parent Category')
    prestacategory.delete_category_PrestaShop(3)
    prestacategory.update_category_PrestaShop(4, 'Updated Category Name')
    print(prestacategory.get_parent_categories_list_PrestaShop(5))
"""
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12
import requests
from attr import attr, attrs
from pathlib import Path
from typing import List, Dict, Optional, Union
from types import SimpleNamespace

# from src import gs # TODO: проверить необходимость
# from src.utils.jjson import j_loads # TODO: проверить необходимость
from src.logger.logger import logger

from .api import PrestaShop

class PrestaCategory(PrestaShop):
    """
    Класс для работы с категориями в PrestaShop.

    Предоставляет методы для добавления, удаления, обновления категорий, а также получения
    списка родительских категорий.

    :param credentials: Словарь или объект SimpleNamespace с параметрами `api_domain` и `api_key`.
    :type credentials: Optional[Union[dict, SimpleNamespace]]
    :param api_domain: Домен API.
    :type api_domain: Optional[str]
    :param api_key: Ключ API.
    :type api_key: Optional[str]

    :raises ValueError: Если не указаны `api_domain` и `api_key`.
    """
    def __init__(self,
                 credentials: Optional[Union[dict, SimpleNamespace]] = None,
                 api_domain: Optional[str] = None,
                 api_key: Optional[str] = None,
                 *args, **kwards):
        """
        Инициализация категории PrestaShop.

        :param credentials: Словарь или объект SimpleNamespace с параметрами `api_domain` и `api_key`.
        :type credentials: Optional[Union[dict, SimpleNamespace]]
        :param api_domain: Домен API.
        :type api_domain: Optional[str]
        :param api_key: Ключ API.
        :type api_key: Optional[str]

        :raises ValueError: Если не указаны `api_domain` и `api_key`.
        """
        # Инициализация класса PrestaCategory
        if credentials is not None:
            # Извлечение api_domain и api_key из словаря credentials
            api_domain = credentials.get('api_domain', api_domain)
            api_key = credentials.get('api_key', api_key)

        # Проверка наличия api_domain и api_key
        if not api_domain or not api_key:
            #  Вывод ошибки, если параметры не заданы
            raise ValueError('Необходимы оба параметра: api_domain и api_key.')
        # Вызов конструктора родительского класса PrestaShop
        super().__init__(api_domain, api_key, *args, **kwards)


    def get_parent_categories_list(self, id_category: Union[str, int],  parent_categories_list: Optional[List[int]] = None) -> list:
        """
        Извлекает из базы данных PrestaShop родительские категории заданной категории.

        :param id_category: ID категории, для которой нужно извлечь родительские категории.
        :type id_category: Union[str, int]
        :param parent_categories_list: Список родительских категорий (используется для рекурсии).
        :type parent_categories_list: Optional[List[int]]
        :return: Список родительских категорий.
        :rtype: list
        
        :raises ValueError: Если `id_category` не передан.

        :todo: Обработать ситуацию, когда у клиента нет такой категории. Например, в магазине мебели не должно быть категории `motherboards`.
        """
        # Инициализация parent_categories_list, если он None
        if parent_categories_list is None:
            parent_categories_list = []
        # проверка на наличие `id_category`
        if not id_category:
             # Логирование ошибки, если id_category не указан
            logger.error(f"""Нет id категории!!!\n                         {parent_categories_list}\n                    Если отправить запрос без id вернется словарь со всми категориями""")
            return parent_categories_list
        # Получение информации о категории из API
        category = super().get('categories', resource_id = id_category, display='full', io_format='JSON')
        """
        Возвращает словарь
        @code
        {'category':
                {'id': 11259,
                'id_parent': '11248',
                'level_depth': '5',
                'nb_products_recursive': -1,
                'active': '1',
                'id_shop_default': '1',
                'is_root_category': '0',
                'position': '0',
                'date_add': '2023-07-25 11:58:08', ...}
        }
        """
        ...
        # Проверка, что категория получена
        if not category:
             # Логирование ошибки, если категория не найдена
            logger.error(f'Что-то не так с категориями')
            return
        # Извлечение id родительской категории
        _parent_category: int = int(category['id_parent'])
         # Добавление id родительской категории в список
        parent_categories_list.append(_parent_category)

        # Проверка, достигнут ли корневой уровень
        if _parent_category <= 2: # `2` - корневая директория
            return parent_categories_list
            ...
        else:
             # Рекурсивный вызов функции для получения родительских категорий
            return self.get_parent_categories_list(_parent_category, parent_categories_list)
```