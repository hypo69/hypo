# gearbest

## Overview

This module provides functionality for interacting with the GearBest supplier.


## Classes

### `Graber`

**Description**:  This class handles the process of gathering data from GearBest.


**Methods**:

- `get_product_details(product_url: str) -> dict | None`:
    **Description**: Retrieves detailed product information from a given URL.

    **Parameters**:
    - `product_url` (str): The URL of the product page on GearBest.

    **Returns**:
    - `dict | None`: A dictionary containing the product details, or `None` if there was an error.


## Variables

### `MODE`

**Description**:  A string variable representing the current mode (e.g., 'dev', 'prod').


This module imports the `Graber` class from the `graber` submodule.