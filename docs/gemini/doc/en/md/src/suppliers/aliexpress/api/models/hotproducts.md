# hypotez/src/suppliers/aliexpress/api/models/hotproducts.py

## Overview

This module defines the `HotProductsResponse` class, used for representing the response from the AliExpress API related to hot products. It includes attributes for pagination information (current page number, record count, and total record count) and a list of `Product` objects.


## Table of Contents

- [Overview](#overview)
- [Classes](#classes)
    - [`HotProductsResponse`](#hotproductsresponse)


## Classes

### `HotProductsResponse`

**Description**: Represents the response from the AliExpress API for hot products.  It contains information about the current page, the number of records on that page, the total number of records, and a list of products.


**Attributes**:

- `current_page_no` (int): The current page number being returned.
- `current_record_count` (int): The number of records present in the current page.
- `total_record_count` (int): The total number of records across all pages.
- `products` (List[Product]): A list of `Product` objects representing the hot products.

**Note**: This class assumes the existence of a `Product` class, which is likely defined elsewhere (e.g., in the `product.py` file).  Documentation for the `Product` class is needed for a complete understanding of this module.