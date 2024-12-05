# aliexpress/aliapi.py

## Overview

This module provides an API wrapper for interacting with the AliExpress API. It defines a custom class `AliApi` extending the `AliexpressApi` class to handle specific AliExpress operations.  It includes functionality for retrieving product details, generating affiliate links, and potentially interacting with database managers for categories and campaigns.

## Table of Contents

- [Classes](#classes)
    - [`AliApi`](#aliapi)
- [Functions](#functions)
    - [`retrieve_product_details_as_dict`](#retrieve-product-details-as-dict)
    - [`get_affiliate_links`](#get-affiliate-links)


## Classes

### `AliApi`

**Description**: This class provides a custom wrapper for interacting with the AliExpress API.  It inherits from `AliexpressApi` and extends its functionality.  Crucially, it initializes database managers for product categories and campaigns.

**Methods**

- `__init__(self, language: str = 'en', currency: str = 'usd', *args, **kwargs)`
    **Description**: Initializes an instance of the `AliApi` class.
    **Parameters**
        - `language` (str): The language to use for API requests. Defaults to 'en'.
        - `currency` (str): The currency to use for API requests. Defaults to 'usd'.
    **Returns**:  None (implicit).
- `retrieve_product_details_as_dict(self, product_ids: list) -> dict | dict | None`
    **Description**: Retrieves product details for a given list of product IDs. Converts the result from a list of SimpleNamespace objects to a list of dictionaries.
    **Parameters**
        - `product_ids` (list): List of product IDs.
    **Returns**
        - `dict | dict | None`: A list of dictionaries representing product data. Returns `None` if there's an error.
    **Example Usage**:
    ```python
    # Example usage (assuming you have a list of product IDs)
    product_ids_list = [123, 456, 789]
    api_instance = AliApi()  # Replace with your AliApi instance
    product_details = api_instance.retrieve_product_details_as_dict(product_ids_list)
    if product_details:
        print(product_details)
    ```
- `get_affiliate_links(self, links: str | list, link_type: int = 0, **kwargs) -> List[SimpleNamespace]`
    **Description**: Retrieves affiliate links for specified products.
    **Parameters**
        - `links` (str | list): Product links.
        - `link_type` (int, optional): Link type. Defaults to 0.
    **Returns**
        - `List[SimpleNamespace]`: A list of SimpleNamespace objects containing affiliate links.



## Functions

(None found in the provided code block, but the comment block does contain references to possible functions)