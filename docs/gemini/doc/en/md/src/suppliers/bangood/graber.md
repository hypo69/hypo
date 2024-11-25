# hypotez/src/suppliers/bangood/graber.py

## Overview

This module defines the `Graber` class for scraping product data from Banggood.  It utilizes the `Graber` base class from the `src.suppliers` module and interacts with the `Driver` class for web interaction. It incorporates asynchronous operations and data extraction functions for various product attributes.


## Classes

### `Graber`

**Description**: This class extends the `Grbr` class (presumably a base class for grabbers) and handles specific scraping operations for Banggood.  It initializes the `supplier_prefix` and contains the `grab_page` method.


**Attributes**:

- `supplier_prefix` (str):  Prefix for the supplier's data.


**Methods**:

#### `__init__(self, driver: Driver)`

**Description**: Initializes the `Graber` instance with a `Driver` object.


**Parameters**:

- `driver` (Driver): The web driver instance used for interaction with the Banggood website.


#### `grab_page(self, driver: Driver) -> ProductFields`

**Description**: Asynchronous function to fetch product data.


**Parameters**:

- `driver` (Driver): The driver instance to interact with the website.


**Returns**:

- `ProductFields`: A `ProductFields` object containing the scraped product data.


## Functions


(Note: The provided code defines no functions outside of methods, so this section remains empty in this documentation).

## Global Variables

(Note: The provided code defines no functions outside of methods, so this section remains empty in this documentation).