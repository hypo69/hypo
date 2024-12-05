# hypotez/src/suppliers/visualdg/graber.py

## Overview

This module defines the `Graber` class, a subclass of the `Grbr` class, responsible for collecting product data from the `visualdg.co.il` website.  It handles the specific data extraction logic for this particular supplier.  The class overloads functions from the parent class to provide custom handling for specific fields if needed.  A decorator is available for performing actions before web driver requests, allowing for actions such as closing pop-up windows.


## Classes

### `Graber`

**Description**: This class is designed to gather product information from the `visualdg.co.il` website. It extends the `Grbr` class and provides custom implementations for data extraction.

**Methods**

#### `__init__`

**Description**: Initializes the `Graber` class instance.

**Parameters**

- `driver (Driver)`: The web driver instance used for interacting with the website.

#### `grab_page`

**Description**: Asynchronous function to extract product data from the page.

**Parameters**

- `driver (Driver)`: The web driver instance to use.

**Returns**

- `ProductFields`: A `ProductFields` object containing the collected product data.

**Raises**

- `ExecuteLocatorException`: An error occurred while executing a locator operation.


## Functions

(No functions are defined outside of the class methods)