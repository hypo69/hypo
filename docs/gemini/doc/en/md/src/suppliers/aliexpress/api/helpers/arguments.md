# hypotez/src/suppliers/aliexpress/api/helpers/arguments.py

## Overview

This module provides helper functions for handling arguments related to AliExpress API interactions, specifically for extracting and validating product IDs.


## Table of Contents

- [get_list_as_string](#get_list_as_string)
- [get_product_ids](#get_product_ids)


## Functions

### `get_list_as_string`

**Description**: Converts a list or string value to a comma-separated string. If the input is `None`, returns `None`. If the input is a string, returns the string as is. If the input is a list, returns the list elements joined by commas. Otherwise, raises an `InvalidArgumentException`.


**Parameters**:

- `value`: The input value (can be a list or a string).


**Returns**:

- `str | None`: Returns the comma-separated string representation of the input, or `None` if the input was `None`.


**Raises**:

- `InvalidArgumentException`: If the input is neither a list nor a string.


### `get_product_ids`

**Description**: Extracts product IDs from a string or list of values. If the input is a string, it's split into individual values. It then extracts product IDs from each value using `get_product_id` and returns them in a list. If the input is not a string or a list, raises an `InvalidArgumentException`.


**Parameters**:

- `values`: The input string or list of values containing product identifiers.


**Returns**:

- `list`: A list of extracted product IDs.


**Raises**:

- `InvalidArgumentException`: If the input is neither a list nor a string.