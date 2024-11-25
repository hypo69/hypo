# Module: extract_product_id

## Overview

This module provides a function for extracting product IDs from AliExpress URLs or directly from a product ID string.  It uses regular expressions to locate the numerical product ID within the URLs.  The function handles both single URLs and lists of URLs, returning the extracted IDs or `None` if no valid IDs are found.


## Functions

### `extract_prod_ids`

**Description**: Extracts item IDs from a list of URLs or directly returns IDs if given.

**Parameters**:
- `urls` (str | list[str]): A URL, a list of URLs, or product IDs.

**Returns**:
- str | list[str] | None: A list of extracted item IDs, a single ID, or `None` if no valid ID is found.

**Examples**:
```python
>>> extract_prod_ids("https://www.aliexpress.com/item/123456.html")
'123456'

>>> extract_prod_ids(["https://www.aliexpress.com/item/123456.html", "7891011.html"])
['123456', '7891011']

>>> extract_prod_ids(["https://www.example.com/item/123456.html", "https://www.example.com/item/abcdef.html"])
['123456']

>>> extract_prod_ids("7891011")
'7891011'

>>> extract_prod_ids("https://www.example.com/item/abcdef.html")
None
```

### `extract_id`

**Description**: Extracts a product ID from a given URL or validates a product ID.

**Parameters**:
- `url` (str): The URL or product ID.

**Returns**:
- str | None: The extracted product ID or the input itself if it's a valid ID, or `None` if no valid ID is found.

**Examples**:
```python
>>> extract_id("https://www.aliexpress.com/item/123456.html")
'123456'

>>> extract_id("7891011")
'7891011'

>>> extract_id("https://www.example.com/item/abcdef.html")
None
```

**Note**: This function first checks if the input `url` is a valid product ID (i.e., a string of digits).  If so, it returns the `url` itself. Otherwise, it attempts to extract the ID from the URL using a regular expression.


```
```