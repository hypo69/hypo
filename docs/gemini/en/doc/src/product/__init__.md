# src.product

## Overview

This module provides functionalities related to product information. It exposes classes for representing products, their fields, and a utility function for translating multilingual product fields.  The detailed descriptions for each class and function are included within the module files.

## Table of Contents

* [Product](#product)
* [ProductFields](#productfields)
* [record](#record)
* [translate_presta_fields_dict](#translate-presta-fields-dict)
* [MODE](#mode)


## Product

### `Product`

**Description**:  Represents a product.  Detailed information about the `Product` class, including its methods and attributes, is available in `product.py`.


## ProductFields

### `ProductFields`

**Description**: Represents the fields of a product. Detailed information about the `ProductFields` class is available in `product_fields.py`.


## record

**Description**: A dictionary holding product fields in a flat format.  This structure removes any nested field structures.


## translate_presta_fields_dict

### `translate_presta_fields_dict`

**Description**: Translates multilingual fields of `ProductFields`.  This function takes a `ProductFields` object and performs necessary translations.

**Parameters**:
-  None specified.

**Returns**:
-  `dict`:  A dictionary containing translated fields


## MODE

**Description**:  A string representing the current mode (e.g., "dev"). This value is set to 'dev' in the module.