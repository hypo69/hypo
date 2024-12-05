# Module: hypotez/src/suppliers/aliexpress/api/tools/get_product_id.py

## Overview

This module provides a function to extract product IDs from various input strings, primarily focusing on AliExpress product listings.

## Table of Contents

* [Functions](#functions)


## Functions

### `get_product_id`

**Description**: Extracts the product ID from a given string. This function leverages the `extract_prod_ids` function to perform the actual extraction.  It now directly returns the extracted product IDs, instead of attempting a regex-based search.

**Parameters**:

- `raw_product_id` (str): The input string potentially containing the product ID.


**Returns**:

- `str`: The extracted product ID as a string.  Returns an empty string if no product ID is found.


**Raises**:

- `ProductIdNotFoundException`: If no valid product ID is found in the input string.


```python
def get_product_id(raw_product_id: str) -> str:
    """Returns the product ID from a given text. Raises ProductIdNotFoundException on fail."""
    return extract_prod_ids(raw_product_id)
    # if re.search(r'^[0-9]*$', text):
    #     return text
    # # Extract product ID from URL
    # asin = re.search(r'(/)([0-9]*)(.)', text)
    # if asin:
    #     return asin.group(2)
    # else:
    #     raise ProductIdNotFoundException('Product id not found: ' + text)
```