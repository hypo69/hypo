## \file hypotez/src/suppliers/aliexpress/aliapi.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe

""" module: src.suppliers.aliexpress """
MODE = 'debug'
""" module: src.suppliers.aliexpress """
MODE = 'debug'
""" AliExpress API Scenario
\rst
aliapi.py
│
├── re
│
├── json
│
├── asyncio
│
├── pathlib.Path
│
├── typing.Union, List, Dict
│
├── types.SimpleNamespace
│
├── requests.get
│
├── requests.post
│
├── src.settings.gs
│   ├── gs.aliexpress_credentials
│   │   ├── api_key
│   │   ├── secret
│   │   └── tracking_id
│
├── src.utils.jjson
│
├── src.utils.j_loads
│
├── src.utils.j_dumps
│
├── src.utils.pprint
│
├── src.utils.convertor.xls2dict.xls2dict
│
├── src.utils.convertor.json2csv.json2csv
│
├── src.logger.logger
│   ├── logger.success()
│   ├── logger.error()
│   ├── logger.warning()
│
├── src.db.manager_categories.AliexpressCategory
│
├── src.db.manager_categories.CategoryManager
│
├── src.db.manager_coupons_and_sales.ProductCampaignsManager
│
└── .api.AliexpressApi
    ├── AliexpressApi
    ├── AliexpressApi.__init__()
    ├── AliexpressApi.retrieve_product_details()
    ├── AliexpressApi.get_affiliate_links()
\endrst
The `start()` function begins the API scenario collection process, 
processing XLS files from the `scenarios\\api\\sources` directory. 
`start()` processes only one XLS file if specified, or all files in the directory if no specific file is provided.
"""
...

...
import re
import json
import asyncio
from pathlib import Path
from typing import List, Dict
from types import SimpleNamespace
from requests import get, post

from header import gs
from src.utils import jjson, j_loads, j_dumps, pprint
from src.utils.convertors import json2csv
from src.logger import logger
from .api import AliexpressApi

from src.db.manager_categories import AliexpressCategory, CategoryManager
from src.db.manager_coupons_and_sales import ProductCampaignsManager

class AliApi(AliexpressApi):
    """
    Custom API class for AliExpress operations.
    """
    
    # Database managers
    manager_categories: CategoryManager = None
    manager_campaigns: ProductCampaignsManager = None
       
    def __init__(self, language: str = 'en', currency: str = 'usd', *args, **kwargs):
        """ Initializes an instance of the AliApi class.
        @param language: The language to use for API requests. Defaults to 'en'.
        @param currency: The currency to use for API requests. Defaults to 'usd'.
        """
        credentials = gs.credentials.aliexpress
        api_key = credentials.api_key
        secret = credentials.secret
        tracking_id = credentials.tracking_id
        super().__init__(api_key, secret, language, currency, tracking_id)
        # Initialize database managers if needed
        # self.manager_categories = CategoryManager()
        # self.manager_campaigns = ProductCampaignsManager(gs.presta_credentials[0])
        ...

    # def collect_deals_from_url():
    #     """ Given a URL, I retrieve deals, coupons, and other offers received from AliExpress"""
    #     ...

    def retrieve_product_details_as_dict(self, product_ids: list) -> dict | dict | None:
        """ Sends a list of product IDs to AliExpress and receives a list of SimpleNamespace objects with product descriptions.
        @param product_ids: List of product IDs.
        @returns: List of product data as dictionaries.
        @code
        # Convert from SimpleNamespace format to dict
            namespace_list = [
            SimpleNamespace(a=1, b=2, c=3),
            SimpleNamespace(d=4, e=5, f=6),
            SimpleNamespace(g=7, h=8, i=9)
            ]

            # Convert each SimpleNamespace object to a dictionary
            dict_list = [vars(ns) for ns in namespace_list]
            
            # Alternatively, you can use the __dict__ method:
            dict_list = [ns.__dict__ for ns in namespace_list]
            
            # Print the list of dictionaries
            print(dict_list)
        @endcode
        """
        prod_details_ns = self.retrieve_product_details(product_ids)
        prod_details_dict = [vars(ns) for ns in prod_details_ns]
        return prod_details_dict
    
    def get_affiliate_links(self, links: str | list, link_type: int = 0, **kwargs) -> List[SimpleNamespace]:
        """ 
        Retrieves affiliate links for the specified products.
        @param links: The product links to be processed.
        @param link_type: The type of affiliate link to be generated.
        @returns: A list of SimpleNamespace objects containing affiliate links.
        """
        return super().get_affiliate_links(links, link_type, **kwargs)

