```rst
.. module: src.category
```
# Module: Category

## Overview

The `Category` module provides functionality for working with product categories, primarily for PrestaShop. It offers tools to interact with category data, including crawling category pages and managing hierarchical structures of categories.

## Class: `Category`

The `Category` class inherits from `PrestaCategory` and is responsible for handling product categories, fetching parent categories, and recursively crawling category pages.

### Constructor: `__init__(self, api_credentials, *args, **kwargs)`

Initializes a `Category` object.

#### Args:
- `api_credentials`: API credentials for accessing the category data.
- `args`: Variable length argument list (unused).
- `kwargs`: Keyword arguments (unused).

### Method: `get_parents(self, id_category, dept)`

Retrieves a list of parent categories.

#### Args:
- `id_category`: The ID of the category to retrieve parents for.
- `dept`: Depth level of the category.

#### Returns:
- A list of parent categories.

### Method: `crawl_categories_async(self, url, depth, driver, locator, dump_file, default_category_id, category=None)`

Asynchronously crawls categories, building a hierarchical dictionary.

#### Args:
- `url`: The URL of the category page.
- `depth`: The depth of the crawling recursion.
- `driver`: The Selenium WebDriver instance.
- `locator`: The XPath locator for category links.
- `dump_file`: The path to the JSON file for saving results.
- `default_category_id`: The default category ID.
- `category`: (Optional) An existing category dictionary (default=None).

#### Returns:
- The updated or new category dictionary.

### Method: `crawl_categories(self, url, depth, driver, locator, dump_file, id_category_default, category={})`

Crawls categories recursively and builds a hierarchical dictionary.

#### Args:
- `url`: URL of the page to crawl.
- `depth`: Depth of recursion.
- `driver`: Selenium WebDriver instance.
- `locator`: XPath locator for finding category links.
- `dump_file`: File for saving the hierarchical dictionary.
- `id_category_default`: Default category ID.
- `category`: Category dictionary (default is empty).

#### Returns:
- Hierarchical dictionary of categories and their URLs.

### Method: `_is_duplicate_url(self, category, url)`

Checks if a URL already exists in the category dictionary.

#### Args:
- `category`: Category dictionary.
- `url`: URL to check.

#### Returns:
- `True` if the URL is a duplicate, `False` otherwise.

## Function: `compare_and_print_missing_keys(current_dict, file_path)`

Compares the current dictionary with data from a file and prints any missing keys.

### Args:
- `current_dict`: The dictionary to compare against.
- `file_path`: The path to the file containing the comparison data.

## Usage Example

```python
from src.category import Category

# Initialize Category with API credentials
category = Category(api_credentials={'api_key': 'your_api_key'})

# Get parents of a category
parents = category.get_parents(id_category=123, dept=2)

# Crawl categories asynchronously
category_data = await category.crawl_categories_async(
    url='https://example.com/categories', 
    depth=3, 
    driver=driver_instance, 
    locator='//a[@class="category-link"]', 
    dump_file='categories.json', 
    default_category_id=123
)

# Compare current category data with a file and print missing keys
compare_and_print_missing_keys(current_dict=category_data, file_path='saved_categories.json')
```

## Dependencies

- `requests`
- `lxml`
- `asyncio`
- `selenium`
- `src.endpoints.prestashop.PrestaShop`
- `src.endpoints.prestashop.PrestaCategory`
- `src.utils.jjson.j_loads`
- `src.utils.jjson.j_dumps`
- `src.logger.logger`
```