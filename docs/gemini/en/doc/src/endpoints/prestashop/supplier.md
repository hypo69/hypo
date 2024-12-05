# hypotez/src/endpoints/prestashop/supplier.py

## Overview

This module defines the `PrestaSupplier` class, which extends the `PrestaShop` class to handle interactions with PrestaShop suppliers. It provides methods for accessing and managing supplier data.


## Classes

### `PrestaSupplier`

**Description**: This class extends the `PrestaShop` class, providing specific methods for interacting with PrestaShop suppliers.

**Methods**:

- `__init__`


#### `__init__`

**Description**: Initializes a `PrestaSupplier` object.

**Parameters**:
- `credentials` (Optional[dict | SimpleNamespace], optional): A dictionary or a `SimpleNamespace` object containing the `api_domain` and `api_key`. Defaults to `None`.
- `api_domain` (Optional[str], optional): The API domain. Defaults to `None`.
- `api_key` (Optional[str], optional): The API key. Defaults to `None`.

**Raises**:
- `ValueError`: If both `api_domain` and `api_key` are not provided.

**Returns**:
- None (void)


## Functions

(No functions are defined in this file)


## Modules

This module uses the following modules:
- `types` (for `SimpleNamespace`)
- `typing` (for `Optional`)
- `header`
- `src.gs`
- `src.logger`
- `src.utils.jjson`
- `PrestaShop`


## Variables

(No variables are defined in this file that require documentation)


## Notes

- The code utilizes the `SimpleNamespace` type for flexibility in handling credentials.
- Error handling is included to ensure both `api_domain` and `api_key` are provided.
- The documentation format adheres to the specified Markdown guidelines.