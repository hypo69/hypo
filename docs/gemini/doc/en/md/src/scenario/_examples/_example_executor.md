# hypotez/src/scenario/_examples/_example_executor.py

## Overview

This module provides example functions for using the `executor` module in `src.scenario.executor`. It demonstrates how to run scenarios, manage scenario files, and interact with the PrestaShop API.  Includes examples for running lists of scenarios, single files, individual scenarios, product page handling, coupon addition, and asynchronous PrestaShop data insertion.

## Table of Contents

- [Examples](#examples)
    - [Example 1: Run a list of scenario files](#example-1-run-a-list-of-scenario-files)
    - [Example 2: Run a single scenario file](#example-2-run-a-single-scenario-file)
    - [Example 3: Run a single scenario](#example-3-run-a-single-scenario)
    - [Example 4: Insert grabbed product data into PrestaShop](#example-4-insert-grabbed-product-data-into-prestashop)
    - [Example 5: Add a coupon using PrestaShop API](#example-5-add-a-coupon-using-prestashop-api)
    - [Example 6: Execute PrestaShop insert asynchronously](#example-6-execute-prestashop-insert-asynchronously)
    - [Example 7: Execute PrestaShop insert synchronously](#example-7-execute-prestashop-insert-synchronously)
- [Classes](#classes)
    - [`MockSupplier`](#mocksupplier)
    - [`MockRelatedModules`](#mockrelatedmodules)
    - [`MockDriver`](#mockdriver)
- [Module Level Details](#module-level-details)


## Examples

### Example 1: Run a list of scenario files

**Description**: This example demonstrates running a list of scenario files using `run_scenario_files`.

**Parameters**:
- `supplier` (`MockSupplier`): An instance of the `MockSupplier` class, likely containing scenario file paths and related data.
- `scenario_files` (list of `Path`): A list of `Path` objects representing the scenario files to run.

**Returns**:
- `bool`: `True` if all scenarios execute successfully, `False` otherwise.

**Raises**:
- `Exception`: Any exceptions raised during scenario execution.


### Example 2: Run a single scenario file

**Description**: This example shows how to execute a single scenario file using `run_scenario_file`.

**Parameters**:
- `supplier` (`MockSupplier`): An instance of `MockSupplier`  containing file paths and scenario details.
- `scenario_file` (`Path`): A `Path` object representing the scenario file to run.

**Returns**:
- `bool`: `True` if the scenario file executes successfully, `False` otherwise.

**Raises**:
- `Exception`: Any exceptions raised during scenario file execution.


### Example 3: Run a single scenario

**Description**: This example shows how to execute a single scenario definition using `run_scenario`.

**Parameters**:
- `supplier` (`MockSupplier`): An instance of `MockSupplier`  containing relevant data and methods.
- `scenario` (dict): A dictionary representing the scenario to run. Must contain an `url` and a `products` array.

**Returns**:
- `bool`: `True` if the scenario executes successfully, `False` otherwise.

**Raises**:
- `Exception`: Any exceptions during scenario execution.


### Example 4: Insert grabbed product data into PrestaShop

**Description**: This example demonstrates inserting grabbed product data using `insert_grabbed_data`.

**Parameters**:
- `product_fields` (`ProductFields`): An instance of `ProductFields` containing data to insert into PrestaShop.

**Returns**:
- `None`: This function doesn't return a value, but may print messages.

**Raises**:
- `Exception`: Any exceptions during data insertion.

### Example 5: Add a coupon using PrestaShop API

**Description**: This example shows how to add a coupon using `add_coupon`.

**Parameters**:
- `credentials` (dict): PrestaShop API credentials (api_domain, api_key).
- `reference` (str): Product reference.
- `coupon_code` (str): Coupon code.
- `start_date` (str): Start date of coupon validity.
- `end_date` (str): End date of coupon validity.

**Returns**:
- `None`: This function doesn't return a value.

**Raises**:
- `Exception`: Any exceptions during coupon addition.


### Example 6: Execute PrestaShop insert asynchronously

**Description**: This example demonstrates asynchronous PrestaShop data insertion using `execute_PrestaShop_insert_async`.

**Parameters**:
- `product_fields` (`ProductFields`): An instance of `ProductFields` containing product data.

**Returns**:
- `None`: This function doesn't return a value, but may print messages.

**Raises**:
- `Exception`: Any exceptions during asynchronous data insertion.

### Example 7: Execute PrestaShop insert synchronously

**Description**: This example demonstrates synchronous PrestaShop data insertion using `execute_PrestaShop_insert`.

**Parameters**:
- `product_fields` (`ProductFields`): An instance of `ProductFields` containing product data to insert.


**Returns**:
- `bool`: `True` if the insertion was successful, `False` otherwise.

**Raises**:
- `Exception`: Any exceptions during data insertion.



## Classes

### `MockSupplier`

**Description**: A mock class simulating a supplier object for scenario execution. It holds paths to scenario files, current scenario, settings, and related modules.

### `MockRelatedModules`

**Description**: A mock class for testing dependencies, specifically providing methods for product listing retrieval and product page fetching, and includes asynchronous methods.

### `MockDriver`

**Description**: A mock class for testing the driver, demonstrating URL handling.


## Module Level Details

- The module's purpose is to provide examples for using the `executor` module's functions.
- It demonstrates handling scenario files, running scenarios, and interacting with PrestaShop API endpoints.
- Imports necessary classes and functions from related modules.
- Includes mock classes for testing purposes (e.g., `MockSupplier`, `MockRelatedModules`, `MockDriver`)