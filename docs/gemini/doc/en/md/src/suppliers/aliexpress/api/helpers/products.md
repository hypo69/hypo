# Module: hypotez/src/suppliers/aliexpress/api/helpers/products.py

## Overview

This module provides helper functions for parsing product data from AliExpress API responses.  It contains functions for processing individual products and lists of products.


## Table of Contents

* [parse_product](#parse-product)
* [parse_products](#parse-products)


## Functions

### `parse_product`

**Description**: This function processes a single product object, extracting and formatting the small image URLs.

**Parameters**:
- `product`: The product object to be processed.  Expected to have a `product_small_image_urls` attribute (likely a `BeautifulSoup` `Tag`) containing the URLs.

**Returns**:
- `product`: The modified product object with the `product_small_image_urls` attribute updated to a string.

**Raises**:
- `AttributeError`: If the input `product` object does not have the expected `product_small_image_urls` attribute.


### `parse_products`

**Description**: This function processes a list of product objects, applying the `parse_product` function to each item.

**Parameters**:
- `products`: A list of product objects to be processed.

**Returns**:
- `new_products`: A new list containing the processed product objects.

**Raises**:
- `TypeError`: If the input `products` is not a list.
- `TypeError`: If any element within the `products` list is not a valid product object.