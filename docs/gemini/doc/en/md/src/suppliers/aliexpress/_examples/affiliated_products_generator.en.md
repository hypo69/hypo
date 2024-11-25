# affiliated_products_generator.en

## Overview

This module provides functionality for generating affiliate product information from AliExpress. It allows users to specify campaign details and a list of product IDs or URLs to retrieve affiliate links, images, and videos.  The module handles the necessary API calls and data processing to return a list of `Product` objects, each containing the affiliate product information.

## Table of Contents

* [Overview](#overview)
* [Classes](#classes)
    * [AliAffiliatedProducts](#aliaffiliatedproducts)
* [Functions](#functions)
    * [main](#main)


## Classes

### `AliAffiliatedProducts`

**Description**: This class is responsible for fetching affiliate product information from AliExpress. It takes campaign parameters and a list of product IDs or URLs as input and returns a list of `Product` objects containing the affiliate product details.

**Methods**:

- `process_affiliate_products`: Fetches affiliate links, images, and videos for specified products.

#### `process_affiliate_products`

**Description**:  Retrieves affiliate links, images, and videos for the provided product identifiers.

**Parameters**:
- `prod_urls` (list[str]): A list of product IDs or URLs.  If a URL is provided, it must be a valid AliExpress product URL. If an ID is provided, it will be treated as a product ID and an API call made to fetch the URL


**Returns**:
- `list[Product] | None`: A list of `Product` objects containing affiliate product data, or `None` if there are any errors.

**Raises**:
- `APIError`: If there's an error with the API call.
- `ValueError`: If any of the product IDs or URLs are invalid or could not be processed.
- `Exception`: For unexpected errors.


## Functions

### `main`

**Description**: The main function demonstrates the usage of the `AliAffiliatedProducts` class. It sets up campaign parameters, provides a list of product URLs, retrieves affiliate product information, and prints the results to the console.

**Parameters**:
  (none)


**Returns**:
(none)


**Raises**:
(none)