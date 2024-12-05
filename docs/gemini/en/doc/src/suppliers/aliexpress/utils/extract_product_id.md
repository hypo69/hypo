# Module: extract_product_id

## Overview

This module provides a function for extracting product IDs from URLs or a list of URLs. It also allows for direct input of product IDs.  The function handles both single URLs and lists of URLs robustly, returning `None` if no valid product ID is found.


## Table of Contents

* [extract_prod_ids](#extract_prod_ids)
* [extract_id](#extract_id)


## Functions

### `extract_prod_ids`

**Description**: Extracts item IDs from a list of URLs or directly returns IDs if given.


**Parameters**:

* `urls` (str | list[str]): A URL, a list of URLs, or product IDs.


**Returns**:

* str | list[str] | None: A list of extracted item IDs, a single ID, or `None` if no valid ID is found.


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

* `url` (str): The URL or product ID.


**Returns**:

* str | None: The extracted product ID or the input itself if it's a valid ID, or `None` if no valid ID is found.


**Examples**:

```python
>>> extract_id("https://www.aliexpress.com/item/123456.html")
'123456'

>>> extract_id("7891011")
'7891011'

>>> extract_id("https://www.example.com/item/abcdef.html")
None
```