## \file /src/endpoints/prestashop/category.py
# -*- coding: utf-8 -*-
#! .pyenv/bin/python3

"""
```rst
  .. module:: src.endpoints.prestashop.category
```
Модуль для управления категориями в PrestaShop.
================================================
Содержит класс PrestaCategory, который позволяет
получать информацию о родительских категориях.

Классы модуля:
-------------
- PrestaCategory - Класс для управления категориями в PrestaShop.
"""

from typing import List, Dict, Optional
from types import SimpleNamespace
import asyncio
from src.logger.logger import logger
from src.utils.jjson import j_loads, j_dumps
from src.endpoints.prestashop.api import PrestaShop, PrestaShopAsync


class PrestaCategory(PrestaShop):
    """Class for managing categories in PrestaShop."""

    def __init__(self, api_key: str, api_domain: str, *args, **kwargs) -> None:
        """Initializes a Product object.

        Args:
            api_key (str): Ключ API для доступа к PrestaShop.
            api_domain (str): Доменное имя PrestaShop.

        Returns:
            None

        Example:
            >>> category = PrestaCategory(api_key='your_api_key', api_domain='your_domain')
        """
        super().__init__(api_key=api_key, api_domain=api_domain, *args, **kwargs)

    def get_parent_categories_list(
        self, id_category: str | int, parent_categories_list: Optional[List[int | str]] = None
    ) -> List[int | str]:
        """Retrieve parent categories from PrestaShop for a given category.

        Args:
            id_category (str | int): ID категории, для которой нужно получить родительские категории.
            parent_categories_list (Optional[List[int | str]], optional): Список родительских категорий. Defaults to None.

        Returns:
            List[int | str]: Список ID родительских категорий.

        Raises:
            ValueError: Если отсутствует ID категории.
            Exception: Если возникает ошибка при получении данных о категории.

        Example:
            >>> category = PrestaCategory(api_key='your_api_key', api_domain='your_domain')
            >>> parent_categories = category.get_parent_categories_list(id_category='10')
            >>> print(parent_categories)
            [2, 10]
        """
        if not id_category:
            logger.error('Missing category ID.')
            return parent_categories_list or []

        category: Optional[Dict] = super().get(
            'categories', resource_id=id_category, display='full', io_format='JSON'
        )
        if not category:
            logger.error('Issue with retrieving categories.')
            return parent_categories_list or []

        _parent_category: int = int(category['id_parent'])
        parent_categories_list = parent_categories_list or []
        parent_categories_list.append(_parent_category)

        if _parent_category <= 2:
            return parent_categories_list
        else:
            return self.get_parent_categories_list(_parent_category, parent_categories_list)
