# PrestaCategory Module

## Overview

This module provides a `PrestaCategory` class for interacting with PrestaShop categories. It facilitates adding, deleting, updating categories, and retrieving parent categories.  It acts as a layer between client-specific category structures (PrestaShop) and supplier-related product mappings.  The class utilizes the PrestaShop API for communication.


## Table of Contents

* [PrestaCategory](#presta-category)
    * [__init__](#init)
    * [get_parent_categories_list](#get-parent-categories-list)

## Classes

### `PrestaCategory`

**Description**: This class manages interactions with PrestaShop categories, including adding, deleting, updating, and retrieving parent categories.  It inherits from the `PrestaShop` class.


**Methods**

#### `__init__`

**Description**: Initializes the `PrestaCategory` object.

**Parameters**

* `credentials` (Optional[dict | SimpleNamespace], optional): A dictionary or SimpleNamespace object containing API domain and key. Defaults to None.
* `api_domain` (Optional[str], optional): The PrestaShop API domain. Defaults to None.
* `api_key` (Optional[str], optional): The PrestaShop API key. Defaults to None.

**Raises**

* `ValueError`: Raised if `api_domain` or `api_key` are not provided.

#### `get_parent_categories_list`

**Description**: Retrieves the list of parent categories for a given category ID from the PrestaShop API.

**Parameters**

* `id_category` (str | int): The ID of the category for which to retrieve parent categories.
* `parent_categories_list` (List[int], optional): An initialized list to store parent category IDs. Defaults to an empty list.

**Returns**

* `list`: A list of parent category IDs.


**Raises**


* `ValueError`: If `id_category` is not provided.
*  Unhandled exceptions potentially raised by the underlying `requests` library during API calls.  (Crucially, you should explicitly document any exceptions that might be raised by the PrestaShop API itself)


**Notes**
* The function recursively calls itself to traverse the parent category hierarchy.
* The function has a termination condition (`_parent_category <= 2`) to avoid infinite recursion.
* Error handling and logging are implemented to deal with potential issues such as missing categories or API failures.
* There is a need for better error handling around potential `TypeError` if invalid input is received.  For instance, if `id_category` is not an integer or string that can be parsed as an integer.

```
```
```python