# Module: hypotez/src/suppliers/aliexpress/affiliated_products_generator.py

## Overview

This module provides functionality for generating affiliated product data from AliExpress. It fetches product details, including affiliate links, images, and videos, and saves them in a specified directory structure. The module utilizes the `AliApi` class and integrates with other modules for logging, file handling, image/video saving, and JSON serialization.

## Table of Contents

* [Classes](#classes)
    * [AliAffiliatedProducts](#aliaffiliatedproducts)
* [Functions](#functions)
    * [process_affiliate_products](#process_affiliate_products)


## Classes

### `AliAffiliatedProducts`

**Description**: This class inherits from `AliApi` and extends its functionality to collect full product data, including affiliate links and saved images. It manages language and currency settings for the campaign.

**Attributes**:

- `language: str`: Language for the campaign.
- `currency: str`: Currency for the campaign.


**Methods**:

- `__init__`:
    **Description**: Initializes the `AliAffiliatedProducts` object with language and currency settings.
    **Parameters**:
        - `language (str | dict, optional):` Language for the campaign (default 'EN').
        - `currency (str, optional):` Currency for the campaign (default 'USD').
    **Raises**:
        - `Exception`: If language or currency are invalid or missing.


- `process_affiliate_products`:
    **Description**: Processes a list of product IDs or URLs, retrieves affiliate links, fetches product details, saves images/videos, and generates output data.
    **Parameters**:
        - `prod_ids (list[str]):` List of product URLs or IDs.
        - `category_root (Path | str):` Path to the directory where the output data will be stored.
    **Returns**:
        - `list[SimpleNamespace]`: A list of processed products with affiliate links and saved images.
    **Raises**:
        - `Exception`: If there are no affiliate products returned for the given `prod_ids`.



## Functions

(No functions other than the methods of the class are defined in this file)

```