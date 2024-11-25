# Module: hypotez/src/suppliers/gearbest/graber.py

## Overview

This module defines the `Graber` class for grabbing product fields from the GearBest supplier. It utilizes an asynchronous approach for efficient data extraction and incorporates error handling for better robustness. The `Graber` class inherits from the base `Graber` class and provides specific methods for extracting data from the GearBest platform.

## Table of Contents

* [Overview](#overview)
* [Classes](#classes)
    * [Graber](#graber)
        * [grab_page](#grab_page)


## Classes

### `Graber`

**Description**: This class extends the `Graber` base class and manages the data extraction process from GearBest. It initializes with a driver instance and contains methods to retrieve product information.

**Methods**

#### `__init__`

**Description**: Initializes the `Graber` object with a driver and sets the `supplier_prefix`.

**Parameters**:

- `driver` (Driver): The webdriver instance to interact with the GearBest website.


#### `grab_page`

**Description**: Asynchronous function to grab product fields.

**Parameters**:

- `driver` (Driver): The driver instance to use for grabbing.

**Returns**:

- `ProductFields`: The grabbed product fields.

**Raises**:

- `ExecuteLocatorException`: If an error occurs during locator execution.


## Functions


No functions are defined directly within this module.  All functions related to data extraction are methods of the `Graber` class.