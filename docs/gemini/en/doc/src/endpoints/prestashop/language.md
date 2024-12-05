# hypotez/src/endpoints/prestashop/language.py

## Overview

This module defines the `PrestaLanguage` class for managing language settings within a PrestaShop store. It inherits from the `PrestaShop` class, providing methods for adding, deleting, updating, and retrieving language details.  It utilizes the `PrestaShop` API for communication with the store.

## Classes

### `PrestaLanguage`

**Description**: This class is responsible for managing languages within a PrestaShop store. It offers methods for interacting with the PrestaShop API to perform various operations related to language settings.

**Methods**:

#### `__init__`

**Description**: Initializes the `PrestaLanguage` object.

**Parameters**:

- `credentials` (Optional[dict | SimpleNamespace], optional): A dictionary or SimpleNamespace object containing the API domain and key. Defaults to `None`.
- `api_domain` (Optional[str], optional): The API domain. Defaults to `None`.
- `api_key` (Optional[str], optional): The API key. Defaults to `None`.

**Raises**:

- `ValueError`: If both `api_domain` and `api_key` are not provided.

**Returns**:
-  None. (Implicitly returns an instance of `PrestaLanguage`)



## Functions

(No functions are defined in this file.)