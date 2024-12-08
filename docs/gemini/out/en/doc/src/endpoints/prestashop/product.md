# hypotez/src/endpoints/prestashop/product.py

## Overview

This module defines the `PrestaProduct` class for interacting with a PrestaShop API to retrieve and manage product information. It utilizes the `PrestaShop` class from the `api.py` module and provides methods for checking product existence, performing advanced searches, and retrieving product details.

## Table of Contents

* [Overview](#overview)
* [Classes](#classes)
    * [PrestaProduct](#prestaproduct)
        * [__init__](#init)
        * [check](#check)
        * [search](#search)
        * [get](#get)

## Classes

### `PrestaProduct`

**Description**: This class extends the `PrestaShop` class to provide specific product-related functionalities. It directly interacts with the PrestaShop API.

**Methods**

#### `__init__`

**Description**: Initializes a `PrestaProduct` object.

**Parameters**

* `credentials` (Optional[dict | SimpleNamespace], optional): A dictionary or SimpleNamespace object containing API credentials (`api_domain`, `api_key`). Defaults to `None`.
* `api_domain` (Optional[str], optional): The PrestaShop API domain. Defaults to `None`.
* `api_key` (Optional[str], optional): The PrestaShop API key. Defaults to `None`.

**Raises**

* `ValueError`: If both `api_domain` and `api_key` are not provided.

#### `check`

**Description**: Checks if a product exists in the database by its reference (SKU or MKT).

**Parameters**

* `product_reference` (str): The product's reference (SKU or MKT).


**Returns**

* dict | False: Returns a dictionary containing product information if the product exists; otherwise, returns `False`.

#### `search`

**Description**: Performs an advanced search for products in the database based on specific filters.


**Parameters**

* `filter` (str): The filter criteria (e.g., `name`, `description`).
* `value` (str): The value to search for.


**Returns**

* list: Returns a list of product dictionaries matching the filter criteria.


#### `get`

**Description**: Retrieves detailed information about a product by its ID.

**Parameters**

* `id_product` (int): The ID of the product to retrieve.

**Returns**

* dict | None: Returns a dictionary containing product information if the product exists; otherwise, returns `None`.