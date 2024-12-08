# Module: src.suppliers.aliexpress.api.helpers.categories

## Overview

This module provides functions for filtering categories and subcategories from the AliExpress API. It includes functions to extract parent categories and child categories based on specified criteria.

## Table of Contents

* [filter_parent_categories](#filter_parent_categories)
* [filter_child_categories](#filter_child_categories)


## Functions

### `filter_parent_categories`

**Description**: Filters and returns a list of categories that do not have a parent category.

**Parameters**:

* `categories` (List[models.Category | models.ChildCategory]): List of category or child category objects.

**Returns**:

* List[models.Category]: List of category objects without a parent category.

**Raises**:
* `TypeError`: if the input `categories` is not a list or if the elements in the list are not `models.Category` or `models.ChildCategory` objects.



### `filter_child_categories`

**Description**: Filters and returns a list of child categories that belong to the specified parent category.

**Parameters**:

* `categories` (List[models.Category | models.ChildCategory]): List of category or child category objects.
* `parent_category_id` (int): The ID of the parent category to filter child categories by.


**Returns**:

* List[models.ChildCategory]: List of child category objects with the specified parent category ID.

**Raises**:
* `TypeError`: if the input `categories` is not a list or if the elements in the list are not `models.Category` or `models.ChildCategory` objects.
* `ValueError`: if `parent_category_id` is not an integer.