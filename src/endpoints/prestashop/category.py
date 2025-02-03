
# -*- coding: utf-8 -*-

from typing import List, Dict, Optional, Union
from types import SimpleNamespace
import asyncio
from src.logger.logger import logger
from src.utils.jjson import j_loads, j_dumps
from src.endpoints.prestashop.api import PrestaShop, PrestaShopAsync


class PrestaCategory(PrestaShop):
    """! Class for managing categories in PrestaShop."""

    def __init__(self, credentials: Optional[Union[dict, SimpleNamespace]] = None, api_domain: Optional[str] = None, api_key: Optional[str] = None):
        if credentials:
            api_domain = credentials.get('api_domain', api_domain)
            api_key = credentials.get('api_key', api_key)

        if not api_domain or not api_key:
            raise ValueError('Both api_domain and api_key parameters are required.')

        super().__init__(api_domain, api_key)

    def get_parent_categories_list(self, id_category: Union[str, int], parent_categories_list: List[int] = []) -> List[int]:
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

