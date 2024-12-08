# aliexpress/api/helpers

## Overview

This module provides helper functions for interacting with the AliExpress API. It contains functions for making API requests, parsing product data, filtering categories, and handling arguments.

## Table of Contents

- [API Requests](#api-requests)
- [Argument Handling](#argument-handling)
- [Product Handling](#product-handling)
- [Category Handling](#category-handling)


## API Requests

### `api_request`

**Description**: Makes an API request to AliExpress.

**Parameters**:
- `url` (str): The URL of the API endpoint.
- `params` (dict, optional): Additional query parameters for the request. Defaults to `None`.
- `headers` (dict, optional): Headers for the request. Defaults to `None`.

**Returns**:
- `requests.Response`: The response object from the API request.

**Raises**:
- `requests.exceptions.RequestException`: If there is an error during the request.


## Argument Handling

### `get_list_as_string`

**Description**: Formats a list of items into a comma-separated string.

**Parameters**:
- `items` (list): The list of items to format.

**Returns**:
- `str`: A comma-separated string of items, or an empty string if the input is empty or None.

**Raises**:
- `TypeError`: If the input `items` is not a list.

### `get_product_ids`

**Description**: Extracts product IDs from a potentially complex data structure.

**Parameters**:
- `data` (list | dict | str): The data source potentially containing product IDs.

**Returns**:
- `list[int]`: A list of product IDs extracted from the input.  Returns an empty list if no IDs are found or the input is invalid.

**Raises**:
- `TypeError`: If the input data is not a list, dictionary, or string.


## Product Handling

### `parse_products`

**Description**: Parses product data to extract relevant information.

**Parameters**:
- `data` (dict): The product data to parse.

**Returns**:
- `list[dict]`: A list of dictionaries, where each dictionary represents a parsed product. Returns an empty list if no products are found.

**Raises**:
- `TypeError`: If the input `data` is not a dictionary.


## Category Handling

### `filter_parent_categories`

**Description**: Filters categories to only include parent categories.

**Parameters**:
- `categories` (list[dict]): The list of categories to filter.

**Returns**:
- `list[dict]`: A list of parent categories.

**Raises**:
- `TypeError`: If input `categories` is not a list of dictionaries.

### `filter_child_categories`

**Description**: Filters categories to only include child categories.

**Parameters**:
- `categories` (list[dict]): The list of categories to filter.

**Returns**:
- `list[dict]`: A list of child categories.

**Raises**:
- `TypeError`: If input `categories` is not a list of dictionaries.