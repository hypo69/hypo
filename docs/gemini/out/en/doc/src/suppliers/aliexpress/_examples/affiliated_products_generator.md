# affiliated_products_generator.py

## Overview

This module contains the `AliAffiliatedProducts` class for generating affiliate product links from AliExpress product URLs or IDs.  It handles the retrieval, processing, and potentially saving of images and videos associated with the products.


## Classes

### `AliAffiliatedProducts`

**Description**: This class is responsible for fetching and processing affiliate product information from AliExpress. It extracts affiliate links and potentially saves associated media (images, videos).

**Methods**

#### `process_affiliate_products`

**Description**: This method takes a list of product URLs or IDs and processes them to generate affiliate product data.

**Parameters**:
- `prod_urls` (list): A list of product URLs or IDs (strings).

**Returns**:
- `list | None`: A list of `Product` objects containing affiliate product information, or `None` if there's an error during processing.


## Functions

### `main`

**Description**: This function demonstrates how to use the `AliAffiliatedProducts` class. It sets up parameters for a campaign and calls `process_affiliate_products` to get affiliate product information. It prints the results or a message if no products are found.

**Parameters**:
- None

**Returns**:
- None