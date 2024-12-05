# affiliated_products_generator.py

## Overview

This module contains the `AliAffiliatedProducts` class, responsible for generating complete product data from the AliExpress Affiliate API.  It fetches product details, affiliate links, images, and videos, and saves them locally.  It builds upon the `AliApi` class and includes utilities for handling URLs, extracting product IDs, ensuring HTTPS, and saving various media types.


## Table of Contents

* [Imports and Dependencies](#imports-and-dependencies)
* [AliAffiliatedProducts Class](#aliaffiliatedproducts-class)
    * [Class Docstring](#class-docstring)
    * [Attributes](#attributes)
    * [Initialization](#initialization)
    * [Methods]
        * [`process_affiliate_products`](#process_affiliate_products)
        * [`delete_product`](#delete_product)


## Imports and Dependencies

```python
import asyncio
from itertools import count
from math import log
from pathlib import Path
from typing import List, Union, Optional
from types import SimpleNamespace
from urllib.parse import urlparse, parse_qs

from src import gs
from src.suppliers.aliexpress import AliApi
from src.suppliers.aliexpress import Aliexpress
from src.suppliers.aliexpress.affiliate_links_shortener_via_webdriver import AffiliateLinksShortener
from src.suppliers.aliexpress.utils.extract_product_id import extract_prod_ids
from src.suppliers.aliexpress.utils.set_full_https import ensure_https
from src.utils.convertor.csv2json import csv2dict
from src.utils.jjson import j_dumps
from src.utils import save_png_from_url, save_video_from_url
from src.utils.printer import pprint
from src.utils.file import read_text_file, save_text_file

from src.logger import logger
```

This section lists the external libraries and modules used in the file, including standard Python libraries and custom modules.


## AliAffiliatedProducts Class

### Class Docstring

```python
class AliAffiliatedProducts(AliApi):
    """ Class to collect full product data from URLs or product IDs
    locator_description For more details on how to create templates for ad campaigns, see the section `Managing Aliexpress Ad Campaigns`
    @code
    # Example usage:
    prod_urls = ['123','456',...]
    prod_urls = ['https://www.aliexpress.com/item/123.html','456',...]

    parser = AliAffiliatedProducts(
                                campaign_name,
                                campaign_category,
                                language,
                                currency)

    products = parser._affiliate_product(prod_urls)
    @endcode
    """
```

This class is designed to collect full product data from URLs or product IDs using the AliExpress Affiliate API.


### Attributes

```python
campaign_name: str
campaign_category: Optional[str]
campaign_path: Path
language: str
currency: str
```

These attributes store essential information about the campaign, such as its name, category, location, language, and currency.


### Initialization

```python
def __init__(self,
             campaign_name: str,
             campaign_category: Optional[str] = None,
             language: str = 'EN',
             currency: str = 'USD',
             *args, **kwargs):
    """
    @param campaign_name `str`: Name of the advertising campaign. The directory with the prepared material is taken by name.
    @param campaign_category `Optional[str]`: Category for the campaign (default None).
    @param language `str`: Language for the campaign (default 'EN').
    @param currency `str`: Currency for the campaign (default 'USD').
    @param tracking_id `str`: Tracking ID for Aliexpress API.
    """
    super().__init__(language, currency)

    self.campaign_name = campaign_name
    self.campaign_category = campaign_category
    self.language = language
    self.currency = currency
    self.locale = f"{self.language}_{self.currency}"
    self.campaign_path = gs.path.google_drive / 'aliexpress' / 'campaigns' / self.campaign_name / 'categories' / self.campaign_category
```

Initializes the `AliAffiliatedProducts` object with campaign-related parameters, calls the parent class constructor, and sets the campaign path.


### Methods

#### `process_affiliate_products`

```python
def process_affiliate_products(self, prod_urls: List[str]) -> List[SimpleNamespace]:
    """
    Processes a list of URLs and returns a list of products with affiliate links and saved images.

    :param prod_urls: List of product URLs or IDs.
    :return: List of processed products.
    """
    # ... (implementation details) ...
```

This method processes a list of product URLs to fetch affiliate links, download images and videos, and save product data locally.


#### `delete_product`

```python
def delete_product(self, product_id: str, exc_info: bool = False):
    """ Delete a product that does not have an affiliate link"""
    # ... (implementation details) ...
```

This method removes a product entry from the campaign data if no affiliate link is found.


**(Detailed documentation for `process_affiliate_products` and `delete_product`, including parameter descriptions, return values, and potential exceptions, should be included here.)**


```