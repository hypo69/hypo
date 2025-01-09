# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
.. module:: src.endpoints.prestashop 
    :platform: Windows, Unix
    :synopsis: `PrestaCategory` layer between client categories (PrestaShop, in my case) and suppliers
The class provides methods for adding, deleting, updating categories, 
as well as obtaining a list of parent categories from a given one.

locator_description Clients can each have their own unique category tree, which is only understandable to them. 
Product binding to category is described in supplier scenarios

"""

import requests
from attr import attr, attrs
from pathlib import Path
from typing import List, Dict, Optional
from types import SimpleNamespace

import header
from src import gs
from src.utils.jjson import j_loads
from .api import PrestaShop
from src.logger.logger import logger

class PrestaCategory(PrestaShop):
    """! Class for managing categories in PrestaShop.

    Example usage:

    .. code-block:: python

        prestacategory = PrestaCategory(API_DOMAIN=API_DOMAIN, API_KEY=API_KEY)
        prestacategory.add_category_PrestaShop('New Category', 'Parent Category')
        prestacategory.delete_category_PrestaShop(3)
        prestacategory.update_category_PrestaShop(4, 'Updated Category Name')
        print(prestacategory.get_parent_categories_list_PrestaShop(5))
    """

    def __init__(self, 
                 credentials: Optional[dict | SimpleNamespace] = None, 
                 api_domain: Optional[str] = None, 
                 api_key: Optional[str] = None, 
                 *args, **kwargs):
        """! Initialize PrestaShop category instance.

        Args:
            credentials (Optional[dict | SimpleNamespace], optional): Dictionary or SimpleNamespace object with `api_domain` and `api_key` parameters. Defaults to None.
            api_domain (Optional[str], optional): API domain. Defaults to None.
            api_key (Optional[str], optional): API key. Defaults to None.

        Raises:
            ValueError: Raised when both `api_domain` and `api_key` are not provided.
        """

        if credentials is not None:
            api_domain = credentials.get('api_domain', api_domain)
            api_key = credentials.get('api_key', api_key)

        if not api_domain or not api_key:
            raise ValueError('Both api_domain and api_key parameters are required.')

        super().__init__(api_domain, api_key, *args, **kwargs)

    def get_parent_categories_list(self, id_category: str | int, parent_categories_list: List[int] = []) -> list:
        """! Retrieve parent categories from PrestaShop for a given category.

        Args:
            id_category (str | int): Category ID for which parent categories need to be retrieved.
            parent_categories_list (List[int], optional): List of parent category IDs. Defaults to an empty list.

        Returns:
            list: List of parent category IDs.

        Raises:
            ValueError: Raised when the given category ID does not exist in PrestaShop.
        """

        if not id_category:
            logger.error(
                f"""Missing category ID!!!
                Current parent categories list: {parent_categories_list}
                If a request is sent without an ID, a dictionary with all categories will be returned."""
            )
            return parent_categories_list

        category = super().get('categories', resource_id=id_category, display='full', io_format='JSON')

        if not category:
            logger.error('There is an issue with the categories.')
            return

        _parent_category: int = int(category['id_parent'])
        parent_categories_list.append(_parent_category)

        if _parent_category <= 2:  # `2` is the root directory ID
            return parent_categories_list
        else:
            return self.get_parent_categories_list(_parent_category, parent_categories_list)



        # -*- coding: utf-8 -*-
#! venv/bin/python/python3.12
"""
.. module:: src.endpoints.prestashop
    :platform: Windows, Unix
    :synopsis: `PrestaCategoryAsync` layer between client categories (PrestaShop, in my case) and suppliers.
    The class provides methods for adding, deleting, updating categories,
    as well as obtaining a list of parent categories from a given one.

    locator_description Clients can each have their own unique category tree, which is only understandable to them.
    Product binding to category is described in supplier scenarios
"""
import asyncio
from typing import List, Dict, Optional, Union
from types import SimpleNamespace

import aiohttp
from src import gs
from src.logger.logger import logger
from src.utils.jjson import j_loads
from src.endpoints.prestashop import PrestaShopAsync

class PrestaCategoryAsync(PrestaShopAsync):
    """! Async Class for managing categories in PrestaShop.

    Example usage:

    .. code-block:: python

        async def main():
            prestacategory = PrestaCategoryAsync(API_DOMAIN=API_DOMAIN, API_KEY=API_KEY)
            await prestacategory.add_category('New Category', 'Parent Category')
            await prestacategory.delete_category(3)
            await prestacategory.update_category(4, 'Updated Category Name')
            print(await prestacategory.get_parent_categories_list(5))

        if __name__ == "__main__":
            asyncio.run(main())
    """

    def __init__(self,
                 credentials: Optional[Union[dict, SimpleNamespace]] = None,
                 api_domain: Optional[str] = None,
                 api_key: Optional[str] = None,
                 *args, **kwargs):
        """! Initialize PrestaShop category instance asynchronously.

        Args:
            credentials (Optional[dict | SimpleNamespace], optional): Dictionary or SimpleNamespace object with `api_domain` and `api_key` parameters. Defaults to None.
            api_domain (Optional[str], optional): API domain. Defaults to None.
            api_key (Optional[str], optional): API key. Defaults to None.

        Raises:
            ValueError: Raised when both `api_domain` and `api_key` are not provided.
        """

        if credentials is not None:
            api_domain = credentials.get('api_domain', api_domain)
            api_key = credentials.get('api_key', api_key)

        if not api_domain or not api_key:
            raise ValueError('Both api_domain and api_key parameters are required.')

        super().__init__(api_domain, api_key, *args, **kwargs)


    async def get_parent_categories_list(self, id_category: Union[str, int], parent_categories_list: List[int] = []) -> list:
        """! Retrieve parent categories from PrestaShop for a given category asynchronously.

        Args:
            id_category (str | int): Category ID for which parent categories need to be retrieved.
            parent_categories_list (List[int], optional): List of parent category IDs. Defaults to an empty list.

        Returns:
            list: List of parent category IDs.

        Raises:
            ValueError: Raised when the given category ID does not exist in PrestaShop.
        """

        if not id_category:
            logger.error(
                f"""Missing category ID!!!
                Current parent categories list: {parent_categories_list}
                If a request is sent without an ID, a dictionary with all categories will be returned."""
            )
            return parent_categories_list

        category = await super().read('categories', resource_id=id_category, display='full', io_format='JSON')

        if not category:
            logger.error('There is an issue with the categories.')
            return

        _parent_category: int = int(category['category']['id_parent'])
        parent_categories_list.append(_parent_category)

        if _parent_category <= 2:  # `2` is the root directory ID
            return parent_categories_list
        else:
            return await self.get_parent_categories_list(_parent_category, parent_categories_list)
