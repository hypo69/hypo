# src.suppliers.amazon

## Overview

This module provides functionalities for interacting with Amazon's product data. It contains classes for data retrieval and functions for product listing.  Currently, it primarily focuses on getting lists of products in given categories.

## Table of Contents

* [Overview](#overview)
* [Classes](#classes)
    * [Graber](#graber)
* [Functions](#functions)
    * [get\_list\_products\_in\_category](#get_list_products_in_category)


## Classes

### Graber

**Description**: This class is responsible for retrieving data from Amazon.


**Methods**

(No methods are defined within the provided code snippet)


## Functions

### get\_list\_products\_in\_category

**Description**: Retrieves a list of products within a specific category.


**Parameters**:

* `category_name` (str): The name of the category to retrieve products from.


**Returns**:

* `list`: A list of product dictionaries. Returns an empty list if no products are found or if there's an error.


**Raises**:

* `requests.exceptions.RequestException`: If there is an error during the HTTP request.
* `ValueError`: If the `category_name` parameter is invalid.
* `TypeError`: If the input `category_name` is not a string.


```python
def get_list_products_in_category(category_name: str) -> list:
    """
    Args:
        category_name (str): The name of the category to retrieve products from.

    Returns:
        list: A list of product dictionaries. Returns an empty list if no products are found or if there's an error.

    Raises:
        requests.exceptions.RequestException: If there is an error during the HTTP request.
        ValueError: If the category_name parameter is invalid.
        TypeError: If the input category_name is not a string.
    """
    pass
```