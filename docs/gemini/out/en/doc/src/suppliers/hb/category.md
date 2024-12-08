# Module: hypotez/src/suppliers/hb/category.py

## Overview

This module handles the collection of product data from the HB category pages. It uses a webdriver for interaction and implements logic for handling different scenarios, such as pagination and banner handling. It utilizes various functions to retrieve lists of product URLs, process category data, and ultimately generate a list of product data.  It interacts with the `Supplier` class for contextual data.

## Table of Contents

* [get_list_products_in_category](#get_list_products_in_category)
* [paginator](#paginator)
* [get_list_categories_from_site](#get_list_categories_from_site)

## Functions

### `get_list_products_in_category`

**Description**: Retrieves a list of product URLs from a given category page. It handles pagination and banner elements dynamically.

**Parameters**:

- `s` (Supplier): An instance of the Supplier class containing driver and locator data.

**Returns**:

- `list[str, str, None]`: A list of product URLs or `None` if no product links are found.

**Raises**:
- `Exception`:  For unexpected errors during the process.



### `paginator`

**Description**: This function handles pagination within a category page. It checks for the presence of next-page navigation elements.

**Parameters**:

- `d` (Driver): WebDriver instance.
- `locator` (dict): Locator data for pagination elements.
- `list_products_in_category` (list): Existing list of product URLs.

**Returns**:

- `bool`: `True` if there are more pages to retrieve products from.  `False` otherwise, or if there are no more pagination elements.

**Raises**:
- `Exception`: For unexpected errors related to pagination interaction.



### `get_list_categories_from_site`

**Description**:  This function gathers the latest available categories from the website.

**Parameters**:

- `s` (Supplier): An instance of the Supplier class.

**Returns**:

- `list or None`: A list of categories or `None` if the retrieval fails.

**Raises**:
- `Exception`: For any errors during the category retrieval process.