# HotProductsResponse

## Overview

This module defines the `HotProductsResponse` class, which represents a response containing information about hot products from AliExpress.  It includes pagination information and a list of `Product` objects.


## Classes

### `HotProductsResponse`

**Description**: This class represents the response from an API call to retrieve hot products. It holds pagination details and a list of `Product` objects.

**Attributes**:

- `current_page_no` (int): The current page number of the retrieved hot products.
- `current_record_count` (int): The number of records on the current page.
- `total_record_count` (int): The total number of records available across all pages.
- `products` (List[Product]): A list of `Product` objects, each representing a hot product.


## Functions

This module does not contain any functions.