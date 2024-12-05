# aliexpress/api/models/category.py

## Overview

This module defines classes for representing categories from the AliExpress API.  It includes a base `Category` class and a derived `ChildCategory` class for handling parent-child relationships within the category hierarchy.


## Table of Contents

* [Category](#category)
* [ChildCategory](#childcategory)


## Classes

### `Category`

**Description**: Represents a general category.

**Attributes**:

- `category_id` (int): The unique identifier for the category.
- `category_name` (str): The name of the category.


### `ChildCategory`

**Description**: Represents a child category, inheriting from the `Category` class.

**Attributes**:

- `parent_category_id` (int): The ID of the parent category.
- `category_id` (int): The unique identifier for the category.  Inherited from `Category`.
- `category_name` (str): The name of the category. Inherited from `Category`.