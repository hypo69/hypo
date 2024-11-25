# hypotez/src/product/product.py

## Overview

This module defines the behavior of a product within the project, interacting with the website, product data, and the PrestaShop API.  It leverages data fetching from product pages and PrestaShop API calls.

## Classes

### `Product`

**Description**: This class handles product manipulations, initially fetching data from the product page and then using the PrestaShop API. It inherits from `ProductFields` and `PrestaShop`.

**Methods**:

- `__init__`:
    **Description**: Initializes a `Product` object.
    **Parameters**:
        - `*args`: Variable length argument list.
        - `**kwargs`: Arbitrary keyword arguments.
    **Returns**: None (implicitly).

- `get_parent_categories`:
    **Description**: Retrieves parent categories from a given category ID.  This method duplicates the functionality of `Category.get_parents()`.
    **Parameters**:
        - `id_category` (int): The ID of the category to retrieve parent categories from.
        - `dept` (int, optional): The depth of the category. Defaults to 0.
    **Raises**:
        - `TypeError`: If `id_category` is not an integer.
    **Returns**:
        - `list`: A list of parent category IDs.


## Functions

(No functions defined in the provided code snippet)