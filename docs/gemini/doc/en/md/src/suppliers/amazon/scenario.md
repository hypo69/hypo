# amazon/scenario.py

## Overview

This module defines the scenario for scraping product data from Amazon. It handles fetching category lists, product lists within categories, and ultimately processing individual product pages.

## Table of Contents

* [get_list_products_in_category](#get-list-products-in-category)

## Functions

### `get_list_products_in_category`

**Description**: This function retrieves a list of product URLs from a given category page. It handles potential scrolling to load all products and checks for errors in the product list.


**Parameters**:

* `s` (Supplier): The Supplier object, containing driver and locator information for the target platform.


**Returns**:

* `list[str,str,None]`: A list of product URLs or `None` if no URLs are found or there are errors.


**Raises**:

* `TypeError`: If `list_products_in_category` is not a list or a string.
* `Exception`: For any other exceptions that might arise during the process.