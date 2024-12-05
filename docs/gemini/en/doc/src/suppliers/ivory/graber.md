# hypotez/src/suppliers/ivory/graber.py

## Overview

This module defines the `Graber` class, which is responsible for collecting product field data from the `ivory.co.il` website.  It extends the `Graber` base class and provides specialized functions for handling specific field extraction tasks.  The class uses a decorator to handle potential pop-up windows.  It also uses asynchronous operations for efficiency.


## Classes

### `Graber`

**Description**: This class extends the base `Graber` class to handle the specific data extraction logic for `ivory.co.il`.  It includes asynchronous methods for fetching product information, and supports custom field handling through overridden methods.

**Methods**

- `__init__(self, driver: Driver)`: Initializes the `Graber` instance.  Sets the `supplier_prefix` and initializes the base `Graber` class with the provided `driver` instance. This also sets up the global `Context` object with the appropriate locator for decorators.
- `grab_page(self, driver: Driver) -> ProductFields`: Fetches product data from the given `driver`.  The method calls various specific field extraction methods and combines the extracted values in the `ProductFields` object.

## Functions

### `close_pop_up`


**Description**:  This function (though commented out in the provided code) defines a decorator for handling pop-up windows.  It aims to ensure any pop-ups are closed before the main function logic executes.


**Parameters**:
- `value (Any, optional)`: An optional value for the decorator, potentially used for configuration or additional actions.


**Returns**:
- `Callable`: A decorator that can be used to wrap other functions and potentially handle pop-up windows before execution.

## Notes

* The code contains extensive commented-out logic for various product fields, implying further extraction methods are intended but not fully implemented within the current structure.
* The `close_pop_up` decorator functionality is currently commented out and needs to be uncommented and adjusted for use with the provided `Context` object.
* The `MODE` variable is defined, but its usage is unclear.
* Global variables `d` and `self.d` appear to be used to save the driver object. This should be avoided for clarity and maintainability.

## Implementation Notes

The provided code shows a structure for asynchronous data extraction from the `ivory.co.il` website, with an emphasis on handling potentially blocking operations like pop-up windows using the `@close_pop_up` decorator.  Further implementation of the various product field extraction functions (`id_product`, `description_short`, `name`, etc.) will be crucial for the complete functionality of the class.