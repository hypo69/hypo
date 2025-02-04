## \file /src/endpoints/prestashop/category_async.py
# -*- coding: utf-8 -*-
#! .pyenv/bin/python3

"""
.. module:: src.endpoints.prestashop.category_async 
	:platform: Windows, Unix
	:synopsis:

"""

from typing import List, Dict, Optional, Union
from types import SimpleNamespace
import asyncio
from src.logger.logger import logger
from src.utils.jjson import j_loads, j_dumps
from src.endpoints.prestashop.api import PrestaShop, PrestaShopAsync




class PrestaCategoryAsync(PrestaShopAsync):
    """! Async class for managing categories in PrestaShop."""

    def __init__(self, credentials: Optional[Union[dict, SimpleNamespace]] = None, api_domain: Optional[str] = None, api_key: Optional[str] = None):
        if credentials:
            api_domain = credentials.get('api_domain', api_domain)
            api_key = credentials.get('api_key', api_key)

        if not api_domain or not api_key:
            raise ValueError('Both api_domain and api_key parameters are required.')

        super().__init__(api_domain, api_key)

    async def get_parent_categories_list_async(self, id_category: int|str , additional_categories_list: Optional[List[int] | int] = []) -> List[int]:
        """! Asynchronously retrieve parent categories for a given category."""
        try:
            id_category:int = id_category if isinstance(id_category, int) else int(id_category)
        except Exception as ex:
            logger.error(f"Недопустимый формат категории{id_category}", ex)

        additional_categories_list:list = additional_categories_list if isinstance(additional_categories_list, list) else [additional_categories_list]
        additional_categories_list.append(id_category)

        out_categories_list:list = []

        for c in additional_categories_list:

            try:
                parent:int = await super().read('categories', resource_id=c, display='full', io_format='JSON')
            except Exception as ex:
                logger.error(f"Недопустимый формат категории", ex)
                continue            
                
            if parent <=2:
                return out_categories_list # Дошли до верха. Дерево категорий начинается с 2

            out_categories_list.append(parent)



async def main():
    """"""
    ...

if __name__ == '__main__':
    main()


