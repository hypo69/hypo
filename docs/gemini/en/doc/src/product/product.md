# Product Module Documentation

## Overview

This module defines the behavior of a product, handling interactions between the website, product data, and the PrestaShop API. It utilizes data fetched from product pages and interacts with the PrestaShop API for various operations.

## Table of Contents

* [Overview](#overview)
* [Classes](#classes)
    * [Product](#product)
* [Functions](#functions)
    * [get_parent_categories](#get_parent_categories)


## Classes

### `Product`

**Description**: This class handles product manipulations, fetching data from product pages and interacting with the PrestaShop API. It extends both `ProductFields` and `PrestaShop`.

**Methods**:

- `__init__`: Initializes a `Product` object.

    **Parameters**:
    - `*args`: Variable length argument list.
    - `**kwargs`: Arbitrary keyword arguments.

    **Description**: Initializes the Product object, likely by calling the parent classes' constructors.


## Functions

### `get_parent_categories`

**Description**: Collects parent categories from a specified category ID. Duplicates the `get_parents` function from the `Category` class.

**Parameters**:
- `id_category` (int): The ID of the category to retrieve parent categories for.
- `dept` (int, optional): The depth level of the categories to retrieve (default is 0).

**Returns**:
- list: A list of parent categories.

**Raises**:
- `TypeError`: If `id_category` is not an integer.