# Module: hypotez/src/suppliers/aliexpress/api/helpers/categories.py

## Overview

This module contains functions for filtering categories and subcategories from the AliExpress API.  It provides tools to extract parent and child categories based on specific criteria.


## Table of Contents

* [filter_parent_categories](#filter_parent_categories)
* [filter_child_categories](#filter_child_categories)


## Functions

### `filter_parent_categories`

**Description**: Filters a list of categories and child categories to return only those without a parent category.  Handles cases where input is not a list.

**Parameters**:
- `categories` (List[models.Category | models.ChildCategory]): A list of category or child category objects.  May include instances of `models.Category` and/or `models.ChildCategory`.

**Returns**:
- List[models.Category]: A list of category objects that do not have a parent category ID. Returns an empty list if no such categories are found or if the input is not a valid list.


**Raises**:
- `TypeError`: Raised if the input `categories` is not a list, or if elements within the list are not `models.Category` or `models.ChildCategory` objects.  Note: This exception is not formally present in the input code, but it's a logical consequence to ensure type safety in a real-world implementation.


### `filter_child_categories`

**Description**: Filters a list of categories and child categories to return only those that belong to a specified parent category.

**Parameters**:
- `categories` (List[models.Category | models.ChildCategory]): A list of category or child category objects.  May include instances of `models.Category` and/or `models.ChildCategory`.
- `parent_category_id` (int): The ID of the parent category to filter by.

**Returns**:
- List[models.ChildCategory]: A list of child category objects that have the specified `parent_category_id`. Returns an empty list if no matching child categories are found or if the input is not a valid list.

**Raises**:
- `TypeError`: Raised if the input `categories` is not a list, or if elements within the list are not `models.Category` or `models.ChildCategory` objects, or if `parent_category_id` is not an integer.


```