# hypotez/src/suppliers/aliexpress/affiliated_products_generator.py

## Overview

This module provides functionality for generating affiliated product data from AliExpress. It fetches product details, affiliate links, and saves associated images and videos.  The module utilizes the `AliApi` class to interact with the AliExpress API, and includes utilities for handling URLs, saving files, and logging.  It also utilizes various helper functions and classes for working with data structures and output generation.  The output includes product details, affiliate links, and image/video file paths saved in JSON format.


## Classes

### `AliAffiliatedProducts`

**Description**: This class extends the `AliApi` class to handle the collection of full product data for affiliated products on AliExpress.  It focuses on retrieving and storing affiliate links, images, and videos alongside product details. It also supports specifying language and currency for the campaign.

**Methods**:

- `__init__(language: str | dict = 'EN', currency: str = 'USD', *args, **kwargs)`
    **Description**: Initializes the `AliAffiliatedProducts` object, handling settings for language and currency, and using the parent `AliApi` constructor for API interaction initialization.
    **Parameters**:
        - `language` (str | dict, optional): Language for the campaign. Defaults to 'EN'.
        - `currency` (str, optional): Currency for the campaign. Defaults to 'USD'.
    **Raises**:
        - `Exception`: If an error occurs during the initialization.

- `process_affiliate_products(prod_ids: list[str], category_root: Path | str) -> list[SimpleNamespace]`
    **Description**: Processes a list of product IDs or URLs, retrieves affiliate links, downloads images/videos, and saves the resulting product data in JSON format.
    **Parameters**:
        - `prod_ids` (list[str]): A list of product URLs or IDs.
        - `category_root` (Path | str): The directory to save the output files (images, videos, JSON).
    **Returns**:
        - `list[SimpleNamespace]`: A list of processed products with affiliate links and saved images.
    **Raises**:
        - `Exception`: If there's an issue processing products or saving files.
    **Notes**: The method includes a detailed flowchart illustrating the processing steps, from fetching product data to saving the output.


## Functions

(No functions are present outside of class methods in the provided code.)


## Modules Used

- `asyncio`
- `datetime`
- `html`
- `pathlib`
- `urllib.parse`
- `types`
- `typing`
- `src.logger`
- `src.suppliers.aliexpress.AliApi`
- `src.suppliers.aliexpress.campaign.html_generators`
- `src.suppliers.aliexpress.utils.ensure_https`
- `src.product.product_fields`
- `src.utils.image`
- `src.utils.video`
- `src.utils.file`
- `src.utils.jjson`
- `src.utils`