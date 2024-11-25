# Module: hypotez/src/suppliers/ivory/graber.py

## Overview

This module contains the `Graber` class for grabbing product fields from the Ivory supplier. It leverages asynchronous operations and integrates with the `Graber` base class, `Driver`, and other modules for data extraction.  The module defines a function for closing pop-up windows and handling potential errors during execution.


## Classes

### `Graber`

**Description**: This class handles the specific data extraction logic for the Ivory supplier.

**Methods**

#### `__init__`

**Description**: Initializes the `Graber` object, setting the `supplier_prefix` and initializing the base class (`Grbr`).  It also handles setting `Context.locator` for potential use within close_pop_up decorator.

#### `grab_page`

**Description**: Asynchronous function responsible for fetching product fields from the page.

**Parameters**

- `driver` (Driver): The WebDriver instance used for interacting with the web page.

**Returns**

- `ProductFields`: A `ProductFields` object containing the extracted product information.

**Raises**

- `ExecuteLocatorException`: Thrown if there is an error in executing a locator (likely related to pop-up closure logic).



## Functions

(None defined in the provided code, though `close_pop_up` is commented out)