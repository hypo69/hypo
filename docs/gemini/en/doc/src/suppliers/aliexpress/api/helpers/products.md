# hypotez/src/suppliers/aliexpress/api/helpers/products.py

## Overview

This module provides helper functions for parsing product data from AliExpress.  It contains functions for handling individual product data and lists of products.

## Table of Contents

* [Overview](#overview)
* [Functions](#functions)
    * [`parse_product`](#parse_product)
    * [`parse_products`](#parse_products)


## Functions

### `parse_product`

**Description**: This function takes a product object and parses the `product_small_image_urls` attribute, converting it to a string.

**Parameters**:

* `product`: The product object to be parsed.


**Returns**:

* `product`: The parsed product object.

**Raises**:

* `AttributeError`: If the `product_small_image_urls` attribute is not found or is not a string.


```python
def parse_product(product):
    product.product_small_image_urls = product.product_small_image_urls.string
    return product
```

### `parse_products`

**Description**: This function takes a list of product objects and parses each product using the `parse_product` function.

**Parameters**:

* `products`: A list of product objects.


**Returns**:

* `new_products`: A list of parsed product objects.


```python
def parse_products(products):
    new_products = []

    for product in products:
        new_products.append(parse_product(product))

    return new_products
```