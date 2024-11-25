# aliexpress/aliapi.py

## Overview

This module provides an API interface for interacting with the AliExpress platform. It includes methods for retrieving product details, generating affiliate links, and potentially managing product campaigns and categories.  It leverages the `AliexpressApi` class and integrates with database managers for data persistence.

## Table of Contents

* [AliApi](#aliapi)
    * [__init__](#init)
    * [retrieve_product_details_as_dict](#retrieve_product_details_as_dict)
    * [get_affiliate_links](#get_affiliate_links)

## Classes

### `AliApi`

**Description**: A custom API class extending `AliexpressApi` for enhanced AliExpress operations. This class is responsible for managing interactions with AliExpress, including retrieving product details and generating affiliate links. It also initializes database managers.

**Methods**

#### `__init__`

**Description**: Initializes an instance of the `AliApi` class.

**Parameters**

- `language` (str, optional): The language to use for API requests. Defaults to 'en'.
- `currency` (str, optional): The currency to use for API requests. Defaults to 'usd'.

**Raises**
- `Exception`:  Raises an exception if there's an issue with obtaining credentials or initializing the database managers.


#### `retrieve_product_details_as_dict`

**Description**: Retrieves product details for a list of product IDs.

**Parameters**

- `product_ids` (list): A list of product IDs.

**Returns**

- `dict | dict | None`: A list of dictionaries representing product details.  Returns `None` if there's an error in retrieving the product data.


#### `get_affiliate_links`

**Description**: Retrieves affiliate links for specified product links.

**Parameters**

- `links` (str | list): The product links to process.
- `link_type` (int, optional): The type of affiliate link to generate. Defaults to 0.

**Returns**

- `List[SimpleNamespace]`: A list of `SimpleNamespace` objects containing affiliate links.


## Functions

(None defined in this file)