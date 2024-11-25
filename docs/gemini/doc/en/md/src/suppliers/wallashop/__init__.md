# wallaShop Module

## Overview

This module provides access to WallaShop data. It currently defines a `Graber` class for retrieving data.  The `MODE` constant is set to 'dev' by default, potentially influencing the behaviour of data retrieval.

## Table of Contents

* [Graber Class](#graber-class)


## Classes

### `Graber`

**Description**: The `Graber` class is responsible for fetching data from WallaShop.

**Methods**:

- [`get_products`](#get_products)



## Functions

(No functions defined in this module)


### `get_products`

**Description**: Fetches product information from WallaShop.

**Parameters**:
- None

**Returns**:
- `list[dict] | None`: A list of product dictionaries or `None` if there is an error during the retrieval process.


**Raises**:
- `HTTPError`: If there is a problem with the HTTP request.
- `ConnectionError`: If there is a problem connecting to the server.
- `ValueError`: If the data received from the server is malformed.


```
```python
# Example usage (not part of the documentation, but helpful for understanding)
# from .graber import Graber
# graber = Graber()
# products = graber.get_products()
# if products:
#     for product in products:
#         print(product)
# else:
#     print("No products found or an error occurred.")