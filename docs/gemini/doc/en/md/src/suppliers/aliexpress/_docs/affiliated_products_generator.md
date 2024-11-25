# aliexpress/affiliated_products_generator.md

## Overview

This module contains the `AliAffiliatedProducts` class, responsible for generating complete product data from the AliExpress Affiliate API.  It builds upon the `AliApi` class to process product URLs or IDs, retrieving affiliate product details, saving images, videos, and JSON data.

## Table of Contents

- [Overview](#overview)
- [Imports and Dependencies](#imports-and-dependencies)
- [AliAffiliatedProducts Class](#aliaffiliatedproducts-class)
  - [Class Docstring](#class-docstring)
  - [Attributes](#attributes)
  - [Initialization](#initialization)
  - [Methods]
    - [process_affiliate_products](#process_affiliate_products)
    - [delete_product](#delete_product)

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
from src.utils import j_dumps
from src.utils import save_png_from_url, save_video_from_url
from src.utils import pprint
from src.utils.file import read_text_file, save_text_file

from src.logger import logger
```

- **Standard Libraries:** `asyncio`, `itertools`, `math`, `pathlib`, `typing`, `types`, `urllib.parse`
- **External Libraries:** `src`, `gs`, `AliApi`, `Aliexpress`, `AffiliateLinksShortener`, `extract_prod_ids`, `ensure_https`, `csv2dict`, `j_dumps`, `save_png_from_url`, `save_video_from_url`, `pprint`, `read_text_file`, `save_text_file`, `logger`


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

### Attributes

```python
campaign_name: str
campaign_category: Optional[str]
campaign_path: Path
language: str
currency: str
```

- `campaign_name`: Name of the advertising campaign.
- `campaign_category`: Category for the campaign (defaults to `None`).
- `campaign_path`: Path to the directory where campaign materials are stored.
- `language`: Language for the campaign (defaults to 'EN').
- `currency`: Currency for the campaign (defaults to 'USD').


### Initialization

```python
def __init__(self,
             campaign_name: str,
             campaign_category: Optional[str] = None,
             language: str = 'EN',
             currency: str = 'USD',
             *args, **kwargs):
    """
    Initializes the AliAffiliatedProducts object.

    Args:
        campaign_name (str): Name of the advertising campaign.
        campaign_category (Optional[str], optional): Category for the campaign. Defaults to None.
        language (str, optional): Language for the campaign. Defaults to 'EN'.
        currency (str, optional): Currency for the campaign. Defaults to 'USD'.
    """
    super().__init__(language, currency)

    self.campaign_name = campaign_name
    self.campaign_category = campaign_category
    self.language = language
    self.currency = currency
    self.locale = f"{self.language}_{self.currency}"
    self.campaign_path = gs.path.google_drive / 'aliexpress' / 'campaigns' / self.campaign_name / 'categories' / self.campaign_category
```

### Methods

#### `process_affiliate_products`

```python
def process_affiliate_products(self, prod_urls: List[str]) -> List[SimpleNamespace]:
    """Processes a list of URLs and returns a list of products with affiliate links and saved images.

    Args:
        prod_urls (List[str]): List of product URLs or IDs.

    Returns:
        List[SimpleNamespace]: List of processed products.
    """
    # ... (implementation details)
```

#### `delete_product`

```python
def delete_product(self, product_id: str, exc_info: bool = False):
    """Deletes a product that does not have an affiliate link.

    Args:
        product_id (str): The ID of the product to delete.
        exc_info (bool, optional): Whether to include exception information in the log. Defaults to False.
    """
    # ... (implementation details)
```

(Further details, including docstrings for the `delete_product` method,  and the omitted implementation details from `process_affiliate_products` should be populated from the original code.)


```