## \file /src/endpoints/prestashop/category.py
# -*- coding: utf-8 -*-
#! .pyenv/bin/python3

"""
.. module:: src.endpoints.prestashop.category 
	:platform: Windows, Unix
	:synopsis:

"""

from typing import List, Dict, Optional, Union
from types import SimpleNamespace
import asyncio
from src.logger.logger import logger
from src.utils.jjson import j_loads, j_dumps
from src.endpoints.prestashop.api import PrestaShop, PrestaShopAsync


class PrestaCategory(PrestaShop):
    """! Class for managing categories in PrestaShop."""

    def __init__(self, api_key:str, api_domain:str, *args, **kwargs):
        """
        Initializes a Product object.

        """
                                    
        super().__init__( api_key = api_key ,api_domain = api_domain, *args, **kwargs)

    def get_parent_categories_list(self, id_category: str | int, parent_categories_list: List[int|str] = []) -> List[int]:
        """! Retrieve parent categories from PrestaShop for a given category."""
        if not id_category:
            logger.error("Missing category ID.")
            return parent_categories_list

        category = super().get('categories', resource_id=id_category, display='full', io_format='JSON')
        if not category:
            logger.error("Issue with retrieving categories.")
            return

        _parent_category = int(category['id_parent'])
        parent_categories_list.append(_parent_category)

        if _parent_category <= 2:
            return parent_categories_list
        else:
            return self.get_parent_categories_list(_parent_category, parent_categories_list)

