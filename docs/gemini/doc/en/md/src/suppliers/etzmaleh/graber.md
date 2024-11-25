# Module: hypotez/src/suppliers/etzmaleh/graber.py

## Overview

This module defines the `Graber` class for extracting product data from the Etzmaleh supplier. It utilizes asynchronous operations and interacts with a `Driver` object for web scraping. The class inherits from the base `Grbr` class and contains methods to fetch various product attributes.

## Table of Contents

- [Overview](#overview)
- [Classes](#classes)
    - [Graber](#graber)
        - [`__init__`](#init)
        - [`grab_page`](#grab-page)


## Classes

### `Graber`

**Description**: This class handles the process of grabbing product information from the Morlevi supplier. It extends the base `Grbr` class and stores the supplier prefix.

**Methods**

#### `__init__`

**Description**: The constructor initializes the `Graber` object.

**Parameters**:

- `driver` (Driver): The webdriver instance for interacting with the webpage.


#### `grab_page`

**Description**: Asynchronous function to fetch product fields from the page.

**Parameters**:

- `driver` (Driver): The webdriver instance.

**Returns**:

- `ProductFields`: The gathered product data.

**Raises**:

- `ExecuteLocatorException`: If there's an error executing locators.

## Functions

(No functions are defined in this module)