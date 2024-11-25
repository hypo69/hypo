# helpers

## Overview

This module provides helper functions for interacting with the AliExpress API. It contains functions for handling requests, extracting product data, and filtering product categories.

## Table of Contents

- [api_request](#api-request)
- [get_list_as_string](#get-list-as-string)
- [get_product_ids](#get-product-ids)
- [parse_products](#parse-products)
- [filter_parent_categories](#filter-parent-categories)
- [filter_child_categories](#filter-child-categories)


## Functions

### `api_request`

**Description**: This function handles the API request to the AliExpress API.

**Parameters**:
- `url` (str): The URL of the API endpoint.
- `data` (Optional[dict], optional): Data to be sent with the request. Defaults to `None`.
- `params` (Optional[dict], optional): Query parameters for the request. Defaults to `None`.

**Returns**:
- `requests.Response | None`: The response from the API call, or `None` if there was an error.

**Raises**:
- `requests.exceptions.RequestException`: An exception raised for any issues during the HTTP request.


### `get_list_as_string`

**Description**: This function converts a list of items into a comma-separated string.

**Parameters**:
- `items` (list): The list of items to convert.

**Returns**:
- str: The comma-separated string representation of the list.

**Raises**:
- `TypeError`: Raised if the input is not a list.


### `get_product_ids`

**Description**: This function extracts product IDs from a list of product dictionaries.

**Parameters**:
- `products` (list): A list of product dictionaries.

**Returns**:
- list: A list of product IDs.

**Raises**:
- `TypeError`: Raised if the input is not a list of dictionaries.
- `KeyError`: Raised if a necessary key ('id') is missing from a product dictionary.


### `parse_products`

**Description**: This function parses the product data returned from the API call to extract relevant information.

**Parameters**:
- `products_data` (dict): The product data from the API response.

**Returns**:
- list: A list of product dictionaries, each containing parsed product information.

**Raises**:
- `TypeError`: Raised if the input is not a dictionary.
- `ValueError`: Raised if the structure of the input data doesn't match the expected format.


### `filter_parent_categories`

**Description**: This function filters a list of categories to retrieve only parent categories.

**Parameters**:
- `categories` (list): A list of category dictionaries.
- `parent_category_id` (int): The ID of the parent category to filter by.

**Returns**:
- list: A list of parent category dictionaries matching the given ID.


### `filter_child_categories`

**Description**: This function filters a list of categories to retrieve only child categories.

**Parameters**:
- `categories` (list): A list of category dictionaries.
- `parent_category_id` (int): The ID of the parent category to filter by.

**Returns**:
- list: A list of child category dictionaries matching the given ID.