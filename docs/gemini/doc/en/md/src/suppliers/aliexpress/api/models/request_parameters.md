# hypotez/src/suppliers/aliexpress/api/models/request_parameters.py

## Overview

This module defines constants for various parameters used in AliExpress API requests.  It contains enums for product types, sorting options, and link types.


## Table of Contents

* [ProductType](#producttype)
* [SortBy](#sortby)
* [LinkType](#linktype)


## ProductType

### `ProductType`

**Description**: Represents different product types.

**Constants**:
- `ALL`: Represents all product types.
- `PLAZA`: Represents PLAZA products.
- `TMALL`: Represents TMALL products.


## SortBy

### `SortBy`

**Description**: Represents different sorting criteria for products.

**Constants**:
- `SALE_PRICE_ASC`: Sorts by sale price in ascending order.
- `SALE_PRICE_DESC`: Sorts by sale price in descending order.
- `LAST_VOLUME_ASC`: Sorts by last volume in ascending order.
- `LAST_VOLUME_DESC`: Sorts by last volume in descending order.


## LinkType

### `LinkType`

**Description**: Represents different types of links.

**Constants**:
- `NORMAL`: Represents a normal link.
- `HOTLINK`: Represents a hotlink.