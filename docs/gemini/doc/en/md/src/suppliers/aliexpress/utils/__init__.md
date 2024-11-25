# Module: hypotez/src/suppliers/aliexpress/utils

## Overview

This module provides utility functions for interacting with AliExpress data.  It contains functions for extracting product IDs, ensuring HTTPS connections, and handling locales.

## Table of Contents

- [extract_product_id](#extract-product-id)
- [ensure_https](#ensure-https)
- [locales](#locales)


## Functions

### `extract_prod_ids`

**Description**: Extracts product IDs from a given input.

**Parameters**:
-  No parameters are defined, but this method is likely to accept a string or a list, to extract product IDs from different sources.


**Returns**:
-  `list`: Returns a list of product IDs.


**Raises**:
- `TypeError`: If input is not of expected type.
- `ValueError`: If input contains invalid data.



### `ensure_https`

**Description**: Ensures a given URL is using HTTPS.

**Parameters**:
- `url` (str): The URL to check and potentially modify.

**Returns**:
- `str`: The URL with HTTPS protocol if needed, otherwise the original URL.

**Raises**:
- `TypeError`: If the input is not a string.



### `locales`

**Description**: Provides locale data (likely a dictionary or list of locale codes).


**Parameters**:
- None

**Returns**:
- `dict | list`:  Returns a dictionary or a list of locale codes.

**Raises**:
- `TypeError`: If returned data is not in expected format.