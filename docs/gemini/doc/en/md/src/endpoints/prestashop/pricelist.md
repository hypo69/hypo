# hypotez/src/endpoints/prestashop/pricelist.py

## Overview

This module provides functionality for requesting and updating price lists from a PrestaShop API. It defines a `PriceListRequester` class that inherits from the `PrestaShop` class, handling API interactions for price-related operations.

## Table of Contents

- [Classes](#classes)
    - [`PriceListRequester`](#class-pricelistrequester)
- [Functions](#functions)


## Classes

### `PriceListRequester`

**Description**: A class for requesting and updating price lists from a PrestaShop API. It inherits from the `PrestaShop` class.

**Methods**

#### `__init__`

**Description**: Initializes the `PriceListRequester` object.

**Parameters**:

- `api_credentials` (dict): A dictionary containing API credentials, including 'api_domain' and 'api_key'.

**Raises**:
  - `TypeError`: If `api_credentials` is not a dictionary, or if it does not contain the required keys.



#### `request_prices`

**Description**: Requests the price list for a given set of products.

**Parameters**:

- `products` (list): A list of product names.

**Returns**:

- dict | None: A dictionary where keys are product names and values are their prices. Returns `None` if there's an error.


#### `update_source`

**Description**: Updates the data source for price requests.

**Parameters**:

- `new_source`: The new data source.


#### `modify_product_price`

**Description**: Modifies the price of a specific product.

**Parameters**:

- `product` (str): The name of the product.
- `new_price` (float): The new price for the product.