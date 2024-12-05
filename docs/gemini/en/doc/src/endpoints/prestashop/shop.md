# hypotez/src/endpoints/prestashop/shop.py

## Overview

This module provides a class `PrestaShopShop` for interacting with PrestaShop stores. It inherits from the `PrestaShop` class and handles authentication and basic operations.

## Table of Contents

- [PrestaShopShop](#prestashopshop)
    - [__init__](#init)


## Classes

### `PrestaShopShop`

**Description**: This class extends the `PrestaShop` class, providing specific methods for interacting with PrestaShop shops.

**Methods**

#### `__init__`

**Description**: Initializes a `PrestaShopShop` object.

**Parameters**

- `credentials` (Optional[dict | SimpleNamespace], optional): A dictionary or `SimpleNamespace` object containing `api_domain` and `api_key`. Defaults to `None`.
- `api_domain` (Optional[str], optional): The API domain. Defaults to `None`.
- `api_key` (Optional[str], optional): The API key. Defaults to `None`.

**Raises**

- `ValueError`: Raised if both `api_domain` and `api_key` are not provided, either directly or through the `credentials` parameter.

**Returns**

- None