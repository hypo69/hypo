# Module: hypotez/src/suppliers/aliexpress/api/models/category.py

## Overview

This module defines classes for representing categories on AliExpress.  It includes a base `Category` class and a `ChildCategory` class, inheriting from `Category`.


## Classes

### `Category`

**Description**: Represents a general category.

**Attributes**:

- `category_id` (int): The unique identifier for the category.
- `category_name` (str): The name of the category.


### `ChildCategory`

**Description**: Represents a child category, inheriting properties from `Category`.

**Attributes**:

- `parent_category_id` (int): The ID of the parent category.
- `category_id` (int): The unique identifier for the category.
- `category_name` (str): The name of the category.


## Functions

(No functions are defined in this file)