# hypotez/src/utils/string/validator.py

## Overview

This module provides functions for validating strings based on various criteria and formats.  It includes checks for price, weight, SKU, and URLs, and also has a helper function for checking if a string is an integer.


## Classes

### `ProductFieldsValidator`

**Description**: This class encapsulates functions for validating various string fields relevant to product data.

**Static Methods**:

#### `validate_price(price: str) -> bool`

**Description**: Validates a price string.

**Parameters**:

- `price` (str): The price string to validate.

**Returns**:

- `bool`: `True` if the price is valid (i.e., can be converted to a float), `None` otherwise.

#### `validate_weight(weight: str) -> bool`

**Description**: Validates a weight string.

**Parameters**:

- `weight` (str): The weight string to validate.

**Returns**:

- `bool`: `True` if the weight is valid (i.e., can be converted to a float), `None` otherwise.


#### `validate_sku(sku: str) -> bool`

**Description**: Validates a product SKU string.

**Parameters**:

- `sku` (str): The SKU string to validate.

**Returns**:

- `bool`: `True` if the SKU is valid (at least 3 characters after cleaning), `None` otherwise.

#### `validate_url(url: str) -> bool`

**Description**: Validates a URL string.

**Parameters**:

- `url` (str): The URL string to validate.

**Returns**:

- `bool`: `True` if the URL is valid (has a scheme and netloc after basic preprocessing), `None` otherwise.



#### `isint(s: str) -> bool`

**Description**: Checks if a string can be converted to an integer.

**Parameters**:

- `s` (str): The string to check.

**Returns**:

- `bool`: `True` if the string can be converted to an integer, `None` otherwise.  Raises no exceptions.


## Functions

(No functions defined outside the class)