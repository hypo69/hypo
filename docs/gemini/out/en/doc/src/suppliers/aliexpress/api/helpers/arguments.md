# hypotez/src/suppliers/aliexpress/api/helpers/arguments.py

## Overview

This module provides helper functions for handling arguments related to product IDs and lists.  It includes functions for converting lists to strings, handling different data types for product IDs, and extracting product IDs from various inputs.


## Functions

### `get_list_as_string`

**Description**: This function takes a value and returns a comma-separated string representation if it's a list or the value itself if it's a string.  If the input is neither a string nor a list, it raises an `InvalidArgumentException`.

**Parameters**:
- `value`: (Any): The value to process.

**Returns**:
- `str | None`: The comma-separated string representation of the input list or the input string itself. Returns `None` if the input is `None`.

**Raises**:
- `InvalidArgumentException`: Raised if the input `value` is neither a list nor a string.


### `get_product_ids`

**Description**: This function takes a string or a list of product identifiers and extracts the corresponding product IDs. It handles cases where the input is a string, converting it to a list of strings before processing. If the input is not a list or string, it raises an `InvalidArgumentException`.

**Parameters**:
- `values`: (str | list): A comma-separated string or a list of product identifiers to convert to product IDs.

**Returns**:
- `list`: A list of product IDs extracted from the input.

**Raises**:
- `InvalidArgumentException`: Raised if the input `values` is not a string or a list.


## Modules Used

- `hypotez.src.suppliers.aliexpress.api.tools.get_product_id`
- `hypotez.src.suppliers.aliexpress.api.errors.exceptions`