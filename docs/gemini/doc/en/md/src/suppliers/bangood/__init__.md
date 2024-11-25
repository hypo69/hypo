# Module: hypotez/src/suppliers/bangood/__init__.py

## Overview

This module provides functionalities for interacting with the Banggood supplier. It defines a `Graber` class for data extraction and functions to retrieve lists of categories and products within specific categories from the Banggood website.


## Table of Contents

* [MODE](#mode)
* [Classes](#classes)
    * [Graber](#graber)
* [Functions](#functions)
    * [get_list_categories_from_site](#get-list-categories-from-site)
    * [get_list_products_in_category](#get-list-products-in-category)


## Variables

### `MODE`

**Description**: Configuration variable controlling the operational mode of the module.  Currently set to 'dev'.

**Type**: `str`

## Classes

### `Graber`

**Description**:  A class for data extraction from Banggood.  This class likely contains methods to fetch data, process it, and handle potential errors.  The specific details of the class are not provided in the current snippet.

**Methods**:

(Methods for the Graber class are not defined in the provided snippet.)


## Functions

### `get_list_categories_from_site`

**Description**: Retrieves a list of categories from the Banggood website.  This function is likely to use web scraping techniques to gather this data.

**Returns**:
- `list`: A list of Banggood category data.


### `get_list_products_in_category`

**Description**: Retrieves a list of products within a specific category from Banggood.  This function likely takes the category ID or name as input.

**Parameters**:

- `category_id` (int): The ID of the category to get products from.


**Returns**:
- `list`: A list of products within the specified category.