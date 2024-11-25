# Module: hypotez/src/suppliers/ksp/graber.py

## Overview

This module defines the `Graber` class, responsible for grabbing product fields from a KSP (likely Morlevi) source. It utilizes a driver instance for interacting with the target website, and follows an asynchronous pattern.  The module incorporates data fetching logic for various product attributes, using optional parameters to enable selection of which fields to retrieve in a given call.  The module relies on classes and functions defined in other modules, such as `src.suppliers.Graber`, `src.product`, `src.webdriver`, `src.utils.jjson`, `src.logger` and manages global context for operations like closing pop-ups using a decorator (`close_pop_up`).


## Classes

### `Graber`

**Description**: This class encapsulates the logic for grabbing product fields from the KSP source.  It inherits from the `Grbr` class (likely a base graber class).

**Attributes**:

- `supplier_prefix` (str): A string prefix identifying the supplier.


**Methods**:

#### `__init__`

**Description**:  Initializes the `Graber` instance, setting the supplier prefix and potentially initializing global context elements such as `Context.locator`

**Parameters**:

- `driver` (Driver): The driver instance for web interactions.


#### `grab_page`

**Description**:  Grabs various product fields asynchronously.

**Parameters**:

- `driver` (Driver): The driver instance to use.

**Returns**:

- `ProductFields`: An object containing the grabbed product fields.

**Raises**:

- `ExecuteLocatorException`: Raised if there are issues executing locators during pop-up handling.


## Functions

(None explicitly defined in this module, but `fetch_all_data` and a number of `self.method_calls` are present in the code.)

### `fetch_all_data` (Internal)

**Description**: This is an internal asynchronous function that fetches various product data points.  It's called within `grab_page`. Note that, this is a generated function; the full list of parameters is not obvious from the code.

**Parameters**:

- Various keyword arguments (e.g., `id_product`, `additional_shipping_cost`).

**Returns**:

- (Implicit): The function does not explicitly return a value.  It updates the `self.fields` attribute.

**Raises**:

(Implicit): Any exceptions raised during the execution of inner functions like `self.id_product`.


## Global Variables

### `MODE`

**Description**: A global variable that likely determines the execution mode (e.g., 'dev', 'prod').  Its value is `'dev'` by default.


## Notes

The code includes a large number of `await self.method_call(kwards.get("method_call_name", ''))` calls. These are likely individual functions for fetching different product details.  A more comprehensive documentation for each of these individual methods, or their implementation within the `Graber` class, is missing and would improve the documentation significantly.