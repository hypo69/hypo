# Анализ кода модуля `category.py`

**Качество кода**
8
-  Плюсы
    - Код содержит docstring для модуля и класса `PrestaCategory`.
    - Используется `from src.logger.logger import logger` для логирования.
    - Есть базовая структура для работы с PrestaShop API.
    - Присутствует обработка параметров инициализации с использованием `Optional` типов.
    - Применение `j_loads` отсутствует, но это предусмотрено в требованиях.
-  Минусы
    - Не все функции и методы имеют docstring.
    - Не используется `j_loads` из `src.utils.jjson`.
    - Комментарии не соответствуют RST.
    - В функции `get_parent_categories_list` есть закомментированный код.
    - Обработка ошибок недостаточно структурирована.
    - Присутствует излишнее использование `...` в коде.
    -  В коде используется неявное приведение типов данных
    -  Присутствуют лишние комментарии в коде

**Рекомендации по улучшению**
1.  Добавить docstring для всех функций и методов в формате reStructuredText (RST).
2.  Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения файлов (если это требуется).
3.  Переписать комментарии в формате RST.
4.  Удалить закомментированный код.
5.  Улучшить обработку ошибок с использованием `logger.error`.
6.  Удалить излишние `...`.
7.  Привести типы данных явно.
8.  Удалить не нужные коментарии

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12
"""
Модуль для работы с категориями PrestaShop.
=========================================================================================

Этот модуль предоставляет класс :class:`PrestaCategory`, который используется для управления категориями в PrestaShop.
Он включает методы для добавления, удаления, обновления категорий, а также для получения списка родительских категорий.

Клиенты могут иметь свои собственные уникальные деревья категорий, которые понятны только им.
Связывание продукта с категорией описано в сценариях поставщиков.

.. image:: categories_tree.png
   :alt: Дерево категорий
"""


import requests
from attr import attr, attrs
from pathlib import Path
from typing import List, Dict
from types import SimpleNamespace
from typing import Optional

import header # TODO: Разобраться зачем этот импорт
from src import gs # TODO: Разобраться зачем этот импорт
from src.utils.jjson import j_loads # TODO: возможно нужен j_loads_ns
from .api import PrestaShop
from src.logger.logger import logger


class PrestaCategory(PrestaShop):
    """
    Класс для работы с категориями в PrestaShop.

    :param credentials: (Optional[dict | SimpleNamespace]): Словарь или объект SimpleNamespace с параметрами `api_domain` и `api_key`. Defaults to None.
    :param api_domain: (Optional[str]): Домен API. Defaults to None.
    :param api_key: (Optional[str]): Ключ API. Defaults to None.

    :raises ValueError: Если не указаны `api_domain` или `api_key`.

    Пример использования класса:

    .. code-block:: python

        prestacategory = PrestaCategory(API_DOMAIN='your_api_domain', API_KEY='your_api_key')
        prestacategory.add_category_PrestaShop('New Category', 'Parent Category')
        prestacategory.delete_category_PrestaShop(3)
        prestacategory.update_category_PrestaShop(4, 'Updated Category Name')
        print(prestacategory.get_parent_categories_list_PrestaShop(5))
    """
    
    def __init__(self, 
                 credentials: Optional[dict | SimpleNamespace] = None, 
                 api_domain: Optional[str] = None, 
                 api_key: Optional[str] = None, 
                 *args, **kwards):
        """
        Инициализация категории PrestaShop.

        :param credentials: (Optional[dict | SimpleNamespace]): Словарь или объект SimpleNamespace с параметрами `api_domain` и `api_key`. Defaults to None.
        :param api_domain: (Optional[str]): Домен API. Defaults to None.
        :param api_key: (Optional[str]): Ключ API. Defaults to None.

        :raises ValueError: Если не указаны `api_domain` или `api_key`.
        """
        if credentials is not None:
            api_domain = credentials.get('api_domain', api_domain)
            api_key = credentials.get('api_key', api_key)
        
        if not api_domain or not api_key:
            raise ValueError('Необходимы оба параметра: api_domain и api_key.')
        
        super().__init__(api_domain, api_key, *args, **kwards)

    
    def get_parent_categories_list(self, id_category: str | int,  parent_categories_list:List[int] = []) -> list:
        """
        Получает список родительских категорий для заданной категории.

        :param id_category: (str | int) ID категории, для которой нужно получить родительские категории.
        :param parent_categories_list: (List[int]) Список родительских категорий.
        :return: (list) Список родительских категорий.
        
        .. todo::
            - Обработать ситуацию, когда у клиента нет такой категории.
        """
        
        if not id_category:
            logger.error(f"""Нет id категории!!!
                         {parent_categories_list}
                    Если отправить запрос без id вернется словарь со всеми категориями""")
            return parent_categories_list
        
        #  Выполняет запрос для получения данных категории из PrestaShop
        category = super().get('categories', resource_id = id_category, display='full', io_format='JSON')
        """
         возвращает словарь
        
         @code
         {
             'category':
                 {
                     'id': 11259,
                     'id_parent': '11248',
                     'level_depth': '5',
                     'nb_products_recursive': -1,
                     'active': '1',
                     'id_shop_default': '1',
                     'is_root_category': '0',
                     'position': '0',
                     'date_add': '2023-07-25 11:58:08', ...
                 }
         }
        """
        
        if not category:
            logger.error(f'Что-то не так с категориями')
            return

        # Извлекает ID родительской категории и добавляет его в список
        try:
            _parent_category: int = int(category['category']['id_parent'])
            parent_categories_list.append (_parent_category)
        except (KeyError, ValueError) as e:
            logger.error(f'Ошибка при извлечении родительской категории {e}')
            return parent_categories_list
         
        # Проверяет, достигнута ли корневая директория
        if _parent_category <= 2:
            return parent_categories_list
        else:
            # Рекурсивно вызывает функцию для получения родительских категорий
            return self.get_parent_categories_list(_parent_category, parent_categories_list)
```