# Module: src.category

## Overview

This module provides functionality for working with categories, primarily targeting PrestaShop.  It's designed for handling category data, including fetching parent categories, and recursively crawling category structures from URLs.  The module utilizes asynchronous operations for efficient handling of large category hierarchies.

## Classes

### `Category`

**Description**: This class extends `PrestaCategory` and provides methods for managing product categories. It encapsulates the logic for accessing and processing category data from a PrestaShop API.

**Attributes**:

- `credentials (dict)`: API credentials for accessing the PrestaShop API.  This attribute is set when the class instance is initialized.

**Methods**:

#### `__init__(self, api_credentials, *args, **kwards)`

**Description**: Initializes the `Category` object.  It calls the parent class's constructor (`__init__`) with provided API credentials.

**Parameters**:

- `api_credentials (dict)`: Dictionary containing API credentials for the PrestaShop API.


#### `get_parents(self, id_category, dept)`

**Description**: Retrieves the parent categories for a given category ID. This method utilizes the parent class method `get_list_parent_categories`.

**Parameters**:

- `id_category (int)`: The ID of the category for which to retrieve parent categories.
- `dept (int)`: The department number for category data.

**Returns**:
- `list`: A list of parent category IDs.

#### `crawl_categories_async(self, url, depth, driver, locator, dump_file, id_category_default, category=None)`

**Description**: Asynchronous recursive function to crawl categories, building a hierarchical dictionary of categories and their URLs.

**Parameters**:

- `url (str)`: The URL of the current category page.
- `depth (int)`: The recursion depth.
- `driver (object)`: An instance of a Selenium WebDriver.
- `locator (dict)`: An XPath locator for finding category links on the page.
- `dump_file (Path)`: The file path to save the hierarchical category dictionary.
- `id_category_default (int)`: Default category ID for assigning to the crawled categories.
- `category (dict, optional)`: An existing category dictionary (passed recursively). Defaults to None.

**Returns**:
- `dict`: A hierarchical dictionary representing the categories and their URLs.

**Raises**:
- `SomeError`:  (Placeholder) If there is an error during web scraping or processing.


#### `crawl_categories(self, url, depth: int, driver, locator: dict, dump_file: Path, id_category_default, category: dict = {})`

**Description**: Recursive function to crawl categories and build a hierarchical dictionary.

**Parameters**:

- `url (str)`: The URL of the current category page.
- `depth (int)`: The recursion depth.
- `driver (object)`: An instance of a Selenium WebDriver.
- `locator (dict)`: An XPath locator for finding category links on the page.
- `dump_file (Path)`: The file path to save the hierarchical category dictionary.
- `id_category_default (int)`: Default category ID for assigning to the crawled categories.
- `category (dict, optional)`: An existing category dictionary (passed recursively). Defaults to an empty dictionary.

**Returns**:
- `dict`: A hierarchical dictionary representing the categories and their URLs.


## Functions

### `check_duplicate_url(dictionary, url) -> bool`

**Description**: Checks if a given URL already exists within a hierarchical dictionary.

**Parameters**:

- `dictionary (dict)`: The hierarchical dictionary to check.
- `url (str)`: The URL to check for duplicates.

**Returns**:

- `bool`: `True` if the URL already exists, `False` otherwise.


### `compare_and_print_new_keys(current_dict, file_path)`

**Description**: Compares a dictionary with data from a file and prints keys that are not present in the current dictionary.

**Parameters**:

- `current_dict (dict)`: The dictionary to compare against.
- `file_path (str)`: Path to the file containing the data for comparison.

**Raises**:
- `Exception`: (Placeholder) If there is an error during file loading or processing.