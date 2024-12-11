# hypotez/src/scenario/_examples/_example_executor.py

## Overview

This module provides example usages for the `executor` module in the `src.scenario` package. It demonStartes how to use functions for running scenarios, handling scenario files, interacting with the PrestaShop API, and more.  The examples cover running lists of scenario files, single scenario files, single scenarios, product page scenarios, coupon addition, and asynchronous PrestaShop insertion.


## Classes

### `MockSupplier`

**Description**: A mock class representing a supplier, used for testing purposes in the examples.  It simulates interacting with scenario files and PrestaShop.

**Attributes**:
- `supplier_abs_path (Path)`:  Path to the supplier's scenario files.
- `scenario_files (list[Path])`: List of scenario files to be processed.
- `current_scenario (object)`: Current scenario being executed.
- `supplier_settings (dict)`: Settings related to the supplier.
- `related_modules (MockRelatedModules)`: A mock for related modules.
- `driver (MockDriver)`: A mock for the driver object.

**Methods**:
- `__init__`: Initializes the `MockSupplier` with default values for testing purposes.


### `MockRelatedModules`

**Description**: A mock class for related modules needed for scenario execution.  It simulates functionality from modules that interact with product data and PrestaShop.

**Methods**:
- `get_list_products_in_category(s)`:  Retrieves a list of product URLs in a given category.
- `grab_product_page(s)`:  Simulates fetching product page data, returning a `ProductFields` object.
- `grab_page(s)`:  Asynchronous version of `grab_product_page`.


### `MockDriver`

**Description**: A mock driver class.

**Methods**:
- `get_url(url)`: Checks if a URL is valid.


## Functions

### `example_run_scenario_files`

**Description**: Example demonStarting how to run a list of scenario files.

**Parameters**:
- `supplier (MockSupplier)`: The supplier object containing the scenario files.

**Returns**:
- `bool`: True if all scenarios executed successfully, False otherwise.


### `example_run_scenario_file`

**Description**: Example of running a single scenario file.

**Parameters**:
- `supplier (MockSupplier)`: The supplier object containing the scenario file.
- `scenario_file (Path)`: The path to the scenario file to be executed.

**Returns**:
- `bool`: True if the scenario file executed successfully, False otherwise.


### `example_run_scenario`

**Description**: Example for running a single scenario.

**Parameters**:
- `supplier (MockSupplier)`: The supplier object.
- `scenario (dict)`: The scenario to be run.

**Returns**:
- `bool`: True if the scenario executed successfully, False otherwise.


### `example_insert_grabbed_data`

**Description**: Example demonStarting the insertion of grabbed product data into PrestaShop.

**Parameters**:
- `product_fields (ProductFields)`: The product data to be inserted.

**Returns**:
- None (prints a confirmation message to the console).


### `example_add_coupon`

**Description**: Example for adding a coupon using PrestaShop API.

**Parameters**:
- `credentials (dict)`: Credentials for the PrestaShop API.
- `reference (str)`: Product reference.
- `coupon_code (str)`: Coupon code.
- `start_date (str)`: Start date of the coupon.
- `end_date (str)`: End date of the coupon.

**Returns**:
- None (prints a confirmation message to the console).


### `example_execute_PrestaShop_insert_async`

**Description**: Example for asynchronously inserting product data into PrestaShop.

**Parameters**:
- `product_fields (ProductFields)`: Product data to be inserted.

**Returns**:
- None (prints a confirmation message to the console).


### `example_execute_PrestaShop_insert`

**Description**: Example for synchronously inserting product data into PrestaShop.

**Parameters**:
- `product_fields (ProductFields)`: Product data to be inserted.

**Returns**:
- `bool`: True if the insertion was successful, False otherwise.


## Usage Examples

The `if __name__ == "__main__":` block demonStartes how to call these examples to run the scenario execution functions.


```