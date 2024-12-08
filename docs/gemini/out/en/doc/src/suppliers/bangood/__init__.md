# src.suppliers.bangood

## Overview

This module provides functions and classes for interacting with the Banggood supplier API.  It currently includes functionality for retrieving product listings and categories.


## Table of Contents

* [Graber](#graber)
* [get\_list\_categories\_from\_site](#get_list_categories_from_site)
* [get\_list\_products\_in\_category](#get_list_products_in_category)


## Classes

### `Graber`

**Description**: This class handles the process of fetching data from the Banggood API.


**Methods**:


*  `fetch_data()`: Fetches data from the Banggood API.  Specific details on parameters, return values, and potential exceptions are not provided in the source code snippet.  Please refer to the implementation details of the `Graber` class within the `graber.py` file for further information.


## Functions

### `get_list_categories_from_site`

**Description**: Retrieves a list of categories from the Banggood website.


**Parameters**:
None


**Returns**:
- `list`: A list of category data.  Specific format is not detailed; refer to the function's implementation.

**Raises**:
- `APIError`: If there's an error communicating with the Banggood API.
- `DataError`: If the received data from the API is malformed or invalid.


### `get_list_products_in_category`

**Description**: Retrieves a list of products within a specific category from the Banggood website.


**Parameters**:
- `category_id` (str): The ID of the category to retrieve products for.


**Returns**:
- `list`: A list of product data. Specific format is not detailed; refer to the function's implementation.

**Raises**:
- `APIError`: If there's an error communicating with the Banggood API.
- `DataError`: If the received data from the API is malformed or invalid.
- `ValueError`: If `category_id` is not a valid string.


```python
# Example usage (assuming Graber and necessary exceptions are defined elsewhere)
# ...
# result = get_list_products_in_category(category_id='12345')

# ...
```