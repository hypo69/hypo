# hypotez/src/suppliers/graber.py

## Overview

This module defines the `Graber` base class for fetching product data from HTML pages of various suppliers.  It utilizes a web driver (`Driver` class) to extract target fields (name, description, specification, article, price, etc.) based on locators stored in JSON files within the `locators` directory for each supplier.  Custom field handling can be achieved by overriding specific methods in derived classes.  The `@close_pop_up` decorator is included to handle potential pop-up windows before accessing main content.  Global settings are managed through the `Context` class.

## Classes

### `Context`

**Description**:  A class for managing global settings, primarily the web driver (`driver`), locators (`locator`), and supplier prefix (`supplier_prefix`).

**Attributes**:
- `driver` (Driver): The web driver instance for interacting with the browser.
- `locator` (SimpleNamespace): A namespace holding locators from the JSON file.
- `supplier_prefix` (str): A prefix identifying the supplier.


### `Graber`

**Description**: The base class for gathering product data from a page for all suppliers.

**Methods**:

#### `__init__(self, supplier_prefix: str, driver: Driver)`

**Description**: Initializes the `Graber` instance.

**Parameters**:
- `supplier_prefix` (str): The prefix identifying the supplier.
- `driver` (Driver): The web driver instance.

#### `error(self, field: str)`

**Description**: Error handler for fields.

**Parameters**:
- `field` (str): The name of the field that encountered an error.

#### `set_field_value(self, value: Any, locator_func: Callable[[], Any], field_name: str, default: Any = '') -> Any`

**Description**: A universal function for setting field values, handling potential errors.

**Parameters**:
- `value` (Any): The value to set.
- `locator_func` (Callable[[], Any]): The function to retrieve a value from a locator.
- `field_name` (str): The name of the field to set.
- `default` (Any): The default value (empty string by default).

**Returns**:
- `Any`: The set value.


#### `grab_page(self) -> ProductFields`

**Description**: Asynchronous function to fetch all product fields.

**Returns**:
- `ProductFields`: An object containing the fetched product fields.


#### `(All other methods, e.g., id_product, name, price, etc.)`

These methods are designed to fetch values for specific product attributes using locators and store them in the `ProductFields` object.  They include comprehensive error handling (`try...except`) and validation to prevent crashes. Each method accepts an optional `value` parameter. If `value` is provided, it is used directly; otherwise, the `driver` is used to execute a locator to obtain the value.  Various validation steps and normalization functions are implemented.

**Note**: The full method documentation is not displayed due to its length. Each method contains specific arguments and return values as documented in the code.  The `@close_pop_up` decorator is applied to handle pop-up windows in a consistent manner across these methods.


## Functions

### `close_pop_up(value: Any = None) -> Callable`

**Description**: Creates a decorator to close pop-up windows before executing the wrapped function.

**Parameters**:
- `value` (Any, optional): Additional value for the decorator.

**Returns**:
- `Callable`: A decorator that wraps the function.