# Module: hypotez/src/suppliers/aliexpress/api/tools/get_product_id.py

## Overview

This module provides a function for extracting product IDs from raw text, primarily focusing on AliExpress product information.  It leverages the `extract_prod_ids` function from a utility module.


## Table of Contents

* [Functions](#functions)


## Functions

### `get_product_id`

**Description**: This function extracts the product ID from a given string. It relies on the `extract_prod_ids` function for the core extraction logic.

**Parameters**:
- `raw_product_id` (str): The input string potentially containing a product ID.


**Returns**:
- `str`: The extracted product ID as a string. Returns the result of the `extract_prod_ids` function.

**Raises**:
- `ProductIdNotFoundException`: Raised if the product ID cannot be found in the input string.  (This exception is defined in the `..errors` module, implied by the import statement.)