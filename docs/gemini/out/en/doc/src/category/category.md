# hypotez/src/category/category.py

## Overview

This module provides classes for interacting with and processing product category data, particularly for PrestaShop. It includes functions for fetching parent categories, asynchronously crawling categories, and comparing data with a file.


## Classes

### `Category`

**Description**: A class that handles product categories, inheriting from `PrestaCategory`.  It provides methods for retrieving parent categories and asynchronously crawling category hierarchies.

**Methods**

#### `__init__`

**Description**: Initializes a `Category` object.

**Parameters**:

- `api_credentials` (Dict): API credentials for accessing category data.
- `args` (*args): Variable length argument list (not used).
- `kwargs` (**kwargs): Keyword arguments (not used).

#### `get_parents`

**Description**: Retrieves a list of parent categories for a given category ID.

**Parameters**:

- `id_category` (int): The ID of the category to retrieve parents for.
- `dept` (int): Depth level of the category.

**Returns**:

- list: A list of parent categories.


#### `crawl_categories_async`

**Description**: Asynchronously crawls categories, building a hierarchical dictionary.

**Parameters**:

- `url` (str): The URL of the category page.
- `depth` (int): The depth of the crawling recursion.
- `driver`: Selenium WebDriver instance (needs to be provided).
- `locator` (str): XPath locator for category links.
- `dump_file` (Path): Path to the JSON file for saving results.
- `default_category_id` (int): Default category ID.
- `category` (dict, optional): An existing category dictionary (default=None).

**Returns**:

- dict: The updated or new category dictionary.

**Raises**:

- `Exception`: Catches any errors during the crawling process.


#### `crawl_categories`

**Description**: Crawls categories recursively and builds a hierarchical dictionary.


**Parameters**:

- `url` (str): URL of the page to crawl.
- `depth` (int): Depth of recursion.
- `driver`: Selenium WebDriver instance.
- `locator` (str): XPath locator for finding category links.
- `dump_file` (Path): File for saving the hierarchical dictionary.
- `id_category_default` (int): Default category ID.
- `category` (dict, optional): Category dictionary (default is empty).

**Returns**:

- dict: Hierarchical dictionary of categories and their URLs.

**Raises**:

- `Exception`: Catches any errors during the crawling process.


#### `_is_duplicate_url`

**Description**: Checks if a URL already exists in the category dictionary.

**Parameters**:

- `category` (dict): Category dictionary.
- `url` (str): URL to check.

**Returns**:

- bool: True if the URL is a duplicate, False otherwise.



## Functions

### `compare_and_print_missing_keys`

**Description**: Compares a current dictionary with data in a file and prints missing keys.

**Parameters**:

- `current_dict` (dict): Current dictionary for comparison.
- `file_path` (str): Path to the file containing the data for comparison.


**Raises**:

- `Exception`: Handles potential errors during loading data from the file (e.g., file not found or invalid JSON format) and gracefully exits without raising an exception to the calling function.