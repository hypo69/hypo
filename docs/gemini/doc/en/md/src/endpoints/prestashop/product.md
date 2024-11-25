# PrestaShop Product Endpoint

## Overview

This module provides functionalities for interacting with PrestaShop products through its API. It defines a class `PrestaProduct` that inherits from the base `PrestaShop` class, offering methods for checking product availability, searching for products, and retrieving product details.

## Table of Contents

- [PrestaProduct](#prestaproduct)
    - [__init__](#init)
    - [check](#check)
    - [search](#search)
    - [get](#get)


## Classes

### `PrestaProduct`

**Description**: This class extends the `PrestaShop` class to specifically handle product-related operations.

**Methods**:

- [`__init__`](#init)
- [`check`](#check)
- [`search`](#search)
- [`get`](#get)

### `__init__`

**Description**: Initializes the `PrestaProduct` object.

**Parameters**:

- `credentials` (Optional[dict | SimpleNamespace], optional): Dictionary or `SimpleNamespace` object containing API domain and key. Defaults to `None`.
- `api_domain` (Optional[str], optional): API domain. Defaults to `None`.
- `api_key` (Optional[str], optional): API key. Defaults to `None`.

**Raises**:

- `ValueError`: If both `api_domain` and `api_key` are not provided.


## Functions


### `check`

**Description**: Checks for a product's existence in the database by its product reference (SKU, MKT).

**Parameters**:

- `product_reference` (str): The product reference (SKU, MKT).

**Returns**:

- dict | False: A dictionary containing product details if found, otherwise `False`.

### `search`

**Description**: Performs an advanced search in the database based on specified filters.

**Parameters**:

- `filter` (str): The filter criteria.
- `value` (str): The filter value.

**Returns**:

- dict | None:  A dictionary containing the search results, or `None` if no results are found.

### `get`

**Description**: Retrieves product information based on its ID.

**Parameters**:

- `id_product` (int): The ID of the product.

**Returns**:

- dict | None: A dictionary containing the product details, or `None` if no product is found.