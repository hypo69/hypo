# product Module: Product Management

## Overview

The `product` module is responsible for managing all aspects of product data, including processing, validation, and field management. It consists of the following components:

*   **product.py**: Manages the core logic for handling products, including operations such as creating, updating, and deleting product records. It provides functions to process product data and ensures compliance with business rules for managing products within the application.
*   **product_fields**: Controls the logic related to product fields, handling field validation, formatting, and management. This module ensures that product fields meet the necessary criteria for consistent data entry, enabling accurate and efficient processing of product information.

## Table of Contents

* [product.py](#product-py)
* [product_fields.py](#product-fields-py)


## product.py

### Overview

This file contains the core functions for managing product data.

### Functions

#### `create_product`

**Description**: Creates a new product record.

**Parameters**:
- `product_data` (dict): A dictionary containing the product data to be created.

**Returns**:
- `dict | None`: Returns a dictionary containing the created product record or `None` if an error occurs.

**Raises**:
- `ValidationError`: If the input `product_data` does not meet validation requirements.
- `DuplicateProductError`: If a product with the same ID already exists.



#### `update_product`

**Description**: Updates an existing product record.

**Parameters**:
- `product_id` (int): The ID of the product to update.
- `updated_data` (dict): A dictionary containing the updated product data.

**Returns**:
- `dict | None`: Returns a dictionary containing the updated product record or `None` if an error occurs.


**Raises**:
- `ValidationError`: If the input `updated_data` does not meet validation requirements.
- `ProductNotFoundError`: If the product with the given `product_id` is not found.


#### `delete_product`

**Description**: Deletes a product record.

**Parameters**:
- `product_id` (int): The ID of the product to delete.

**Returns**:
- `bool`: Returns `True` if the product was deleted successfully, `False` otherwise.

**Raises**:
- `ProductNotFoundError`: If the product with the given `product_id` is not found.


## product_fields.py

### Overview

This file contains functions for validating and managing product fields.

### Functions

#### `validate_field`

**Description**: Validates a product field.

**Parameters**:
- `field_name` (str): The name of the field to validate.
- `field_value` (any): The value of the field to validate.

**Returns**:
- `bool`: Returns `True` if the field is valid, `False` otherwise.

**Raises**:
- `ValidationError`: If the field value does not meet validation requirements.


#### `format_field`

**Description**: Formats a product field to a specific standard.

**Parameters**:
- `field_name` (str): The name of the field to format.
- `field_value` (any): The value of the field to format.

**Returns**:
- `any`: Returns the formatted field value.



#### `manage_field_types`

**Description**: Manages different types of product fields.

**Parameters**:
- `field_type` (str): The type of the field to manage (e.g., 'text', 'number').
- `field_value` (any): The value of the field.


**Returns**:
- `any`: The processed field value based on field_type


**Raises**:
- `InvalidFieldTypeEx` : If the provided field_type is not supported.