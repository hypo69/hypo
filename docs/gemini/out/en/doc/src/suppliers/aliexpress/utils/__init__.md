# src.suppliers.aliexpress.utils

## Overview

This module provides utility functions for the AliExpress supplier. It includes functions for extracting product IDs, ensuring HTTPS connections, and handling locales.

## Table of Contents

* [extract_product_id](#extract-product-id)
* [ensure_https](#ensure-https)
* [locales](#locales)


## Functions

### `extract_prod_ids`

**Description**: Extracts product IDs from a given input.

**Parameters**:

-  No parameters


**Returns**:
 - `list`: A list of extracted product IDs. Returns an empty list if no IDs are found.


**Raises**:
 - `ValueError`: If input data is invalid or cannot be parsed.


### `ensure_https`

**Description**: Ensures a URL is using HTTPS.

**Parameters**:

- `url` (str): The URL to check and convert to HTTPS if needed.


**Returns**:
 - `str`: The URL converted to HTTPS if needed; otherwise, the original URL.


**Raises**:
 - `TypeError`: If input is not a string.
 - `ValueError`: If the provided URL is invalid.


### `locales`

**Description**: Provides a list of available locales.

**Parameters**:

-  No parameters


**Returns**:
 - `list`: A list of available locales.


**Raises**:
 - `ValueError`: If locale data is invalid or cannot be loaded.