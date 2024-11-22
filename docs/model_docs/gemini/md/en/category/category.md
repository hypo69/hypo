```markdown
# Module: hypotez/src/category/category.py

## Overview

This module (`hypotez/src/category/category.py`) provides functions and classes for working with product categories, primarily targeting PrestaShop. It facilitates fetching category information, crawling category hierarchies, and managing data structures.

## Table of Contents

- [Classes](#classes)
    - [`Category`](#category)
- [Functions](#functions)
    - [`check_duplicate_url`](#check_duplicate_url)
    - [`compare_and_print_new_keys`](#compare_and_print_new_keys)
    - [`crawl_categories`](#crawl_categories)
    - [`crawl_categories_async`](#crawl_categories_async)


## Classes

### `Category`

**Description**: This class represents product categories. It inherits from `PrestaCategory` and provides methods for retrieving parent categories and crawling category hierarchies.

**Methods**:

#### `__init__`

**Description**: Initializes the `Category` object.

**Parameters**:
- `api_credentials` (dict): API credentials for authentication.
- `*args` (optional): Additional positional arguments.
- `**kwards` (optional): Additional keyword arguments.


#### `get_parents`

**Description**: Retrieves the parent categories of a given category ID.

**Parameters**:
- `id_category` (int): The ID of the category.
- `dept` (int):  The department level.

**Returns**:
- `list`: A list of parent category IDs.

#### `crawl_categories_async`

**Description**: An asynchronous recursive function to crawl categories and build a hierarchical dictionary.

**Parameters**:
- `url` (str): URL of the category page.
- `depth` (int): Depth of recursion.
- `driver` (object): Selenium webdriver instance.
- `locator` (dict): XPath locator for finding category links.
- `dump_file` (Path): File to save the hierarchical dictionary.
- `id_category_default` (int): Default category ID.
- `category` (dict, optional): Existing category dictionary (default: `None`).

**Returns**:
- `dict`: A hierarchical dictionary representing categories and their URLs.

#### `crawl_categories`

**Description**: A recursive function to crawl categories from a website and build a hierarchical dictionary.

**Parameters**:
- `url` (str): URL of the category page.
- `depth` (int): Depth of recursion.
- `driver` (object): Selenium webdriver instance.
- `locator` (dict): XPath locator for finding category links.
- `dump_file` (Path): File to save the hierarchical dictionary.
- `id_category_default` (int): Default category ID.
- `category` (dict, optional): Existing category dictionary (default: empty dictionary).

**Returns**:
- `dict`: A hierarchical dictionary representing categories and their URLs.


## Functions

### `check_duplicate_url`

**Description**: Checks if a given URL already exists in a hierarchical dictionary.

**Parameters**:
- `dictionary` (dict): The hierarchical dictionary to check.
- `url` (str): The URL to check for duplicates.

**Returns**:
- `bool`: `True` if the URL exists, `False` otherwise.


### `compare_and_print_new_keys`

**Description**: Compares current dictionary values with those in a file and prints keys not found in the current dictionary.

**Parameters**:
- `current_dict` (dict): The current dictionary for comparison.
- `file_path` (str): Path to the file containing data for comparison.

**Side Effects**: Prints keys that are present in the file but not in the `current_dict`.
```