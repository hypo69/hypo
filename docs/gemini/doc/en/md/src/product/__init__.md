# hypotez/src/product/__init__.py

## Overview

This module provides access to classes and functions related to product data. It defines external classes, attributes, and a function for working with product information.

## Table of Contents

* [Product](#product)
* [ProductFields](#productfields)
* [record](#record)
* [translate_presta_fields_dict](#translate_presta_fields_dict)


## Classes

### `Product`

**Description**:  Methods and attributes of the product.  Detailed description in `product.py`.


### `ProductFields`

**Description**: Product fields. Detailed description in `product_fields.py`.


## Attributes

### `record`

**Description**: A dictionary of product fields in flat format (without nesting).


## Functions

### `translate_presta_fields_dict`

**Description**: Function that translates multilingual fields of `ProductFields`.


**Parameters**:  (None)


**Returns**:  (dict): Returns a dictionary with translated fields.

**Raises**:  (None)


## Module Constants

### `MODE`

**Description**:  A string constant indicating the current mode (e.g., 'dev').