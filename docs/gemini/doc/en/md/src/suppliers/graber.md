# hypotez/src/suppliers/graber.py

## Overview

This module defines the `Graber` base class for collecting product data from web pages.  It handles common tasks like error handling and provides a framework for custom field processing.  The `close_pop_up` decorator is included to attempt to close pop-up windows before executing the main logic of a function.  The `Context` class provides a way to store global settings for easier access and modification by suppliers.  Each product field retrieval function is carefully wrapped in try/except blocks for robustness, logging errors, and gracefully handling unavailable data.


## Classes

### `Context`

**Description**: A class for holding global settings, primarily used to manage the driver and locators.

**Attributes**:

- `driver` (Driver): The driver object for controlling the browser.  Initialized by `Graber` instance.
- `locator` (SimpleNamespace): Holds locators.  Initialized by `Graber` instance.  Must be a `SimpleNamespace` to allow access through dot notation.  Initialized to `None` unless `close_pop_up` is used.
- `supplier_prefix` (str): Prefix identifying the specific supplier.

### `Graber`

**Description**: The base class for gathering product data from web pages.

**Methods**:

#### `__init__(self, supplier_prefix: str, driver: Driver)`

**Description**: Initializes a `Graber` instance.

**Parameters**:

- `supplier_prefix` (str): The supplier prefix string.
- `driver` (Driver): An instance of the `Driver` class to handle web interactions.

**Raises**:
- `Exception`: Any exception during locator loading or object initialization

#### `error(self, field: str)`

**Description**: Error handler for specific fields.  Logs a debug message about the error and the field name.

**Parameters**:
- `field` (str): Name of the field that raised an error.


#### `set_field_value(self, value: Any, locator_func: Callable[[], Any], field_name: str, default: Any = '') -> Any`

**Description**: A general function for setting field values, handling potential errors during locator execution.

**Parameters**:

- `value` (Any): The value to set. If provided, this value is used instead of fetching from the locator.
- `locator_func` (Callable[[], Any]): Function to fetch the value from the locator.
- `field_name` (str): Name of the field.
- `default` (Any, optional): Default value to use if the locator returns None or an error occurs. Defaults to an empty string.

**Returns**:
- `Any`: The value that was ultimately set for the field.

#### `grab_page(self) -> ProductFields`

**Description**: Asynchronous function to gather all product fields.

**Returns**:
  `ProductFields`: An object containing the gathered product data.


#### Other Methods (Numerous):

Each method (`id_product`, `name`, etc.) fetches a specific product field, handling potential errors and optional user-provided values.  Each method's exact purpose and parameters are documented inside the method's docstring.  The `close_pop_up` decorator is present on all the methods, adding a layer of error handling and pop-up window closure where needed.  The `try...except` blocks meticulously log detailed errors. The docstrings within these methods are comprehensive regarding the use of provided values versus locator calls and default values, error handling, and the expected return values.


## Functions

### `close_pop_up(value: Any = None) -> Callable`

**Description**: Creates a decorator to close pop-up windows.  Useful for ensuring pop-up windows are closed before other operations in functions.


**Parameters**:

- `value` (Any, optional): Additional data that can be passed to the decorator.  This is not used internally, but could be utilized in future implementations.


**Returns**:
- `Callable`: A decorator that will wrap the function it is applied to.


## Notes

- The `Graber` class is designed to be extended with specific supplier implementations.
- The `Context` class manages global settings for the driver and locators, making them accessible throughout the class hierarchy.
- Error handling is extensive, including logging and returning sensible defaults.