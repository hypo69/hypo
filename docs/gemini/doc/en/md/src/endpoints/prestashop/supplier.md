# hypotez/src/endpoints/prestashop/supplier.py

## Overview

This module defines the `PrestaSupplier` class for interacting with PrestaShop suppliers.  It inherits from the `PrestaShop` class, providing methods for accessing and managing supplier data.


## Classes

### `PrestaSupplier`

**Description**: This class handles interactions with PrestaShop suppliers.  It extends the functionality of the `PrestaShop` class.

**Methods**:

#### `__init__`

**Description**: Initializes a `PrestaSupplier` object.

**Parameters**:

- `credentials` (Optional[dict | SimpleNamespace], optional): A dictionary or a SimpleNamespace object containing `api_domain` and `api_key`. Defaults to `None`.
- `api_domain` (Optional[str], optional): The API domain. Defaults to `None`.
- `api_key` (Optional[str], optional): The API key. Defaults to `None`.

**Returns**:
- None

**Raises**:
- `ValueError`: If both `api_domain` and `api_key` are not provided.


## Functions

(No functions are defined in the provided code)