# executor Module Documentation

## Overview

This module provides functions for executing scenarios, handling scenario files, and interacting with the PrestaShop API. It offers a way to run scenarios individually or in batches, and examples demonstrate the interaction with product data and API calls.

## Table of Contents

* [Overview](#overview)
* [Classes](#classes)
* [Functions](#functions)
    * [`run_scenario_files`](#run_scenario_files)
    * [`run_scenario_file`](#run_scenario_file)
    * [`run_scenario`](#run_scenario)
    * [`insert_grabbed_data`](#insert_grabbed_data)
    * [`execute_PrestaShop_insert`](#execute_prestashop_insert)
    * [`execute_PrestaShop_insert_async`](#execute_prestashop_insert_async)
    * [`add_coupon`](#add_coupon)
* [Examples](#examples)


## Classes

### `MockSupplier`

**Description**: A mock class representing a supplier for scenarios.  It simulates fetching scenario files, managing execution states, and interacting with related modules.

**Attributes**:

- `supplier_abs_path`: Path to the scenarios directory.
- `scenario_files`: List of scenario file paths.
- `current_scenario`: Current scenario being executed (for internal use).
- `supplier_settings`: Dictionary to store supplier settings (in this case runned_scenario).
- `related_modules`: Instance of `MockRelatedModules` class.
- `driver`: Instance of `MockDriver` class.


### `MockRelatedModules`

**Description**: A mock class simulating interactions with related modules.

**Methods**:

- `get_list_products_in_category(s)`: Returns a list of product URLs in a specified category.
- `grab_product_page(s)`: Retrieves product page details.
- `grab_page(s)`: Retrieves data from a given page (async).


### `MockDriver`

**Description**: A mock driver class simulating URL fetching.

**Methods**:

- `get_url(url)`: Simulates getting a URL.


## Functions

### `run_scenario_files`

**Description**: Runs a list of scenario files.

**Parameters**:
- `supplier`: An instance of a `Supplier` class containing scenario data and execution context.
- `scenario_files` (list of `Path`): A list of scenario files to execute.

**Returns**:
- `bool`: True if all scenarios executed successfully, False otherwise.

**Raises**:
- `ValueError`: If `scenario_files` is empty.
- `IOError`: If scenario files cannot be found or processed.


### `run_scenario_file`

**Description**: Runs a single scenario file.

**Parameters**:
- `supplier`: An instance of a `Supplier` class containing scenario data and execution context.
- `scenario_file` (`Path`): The scenario file path to execute.

**Returns**:
- `bool`: True if the scenario file executed successfully, False otherwise.

**Raises**:
- `IOError`: If scenario file cannot be found or processed.


### `run_scenario`

**Description**: Runs a single scenario.

**Parameters**:
- `supplier`: An instance of a `Supplier` class containing scenario data and execution context.
- `scenario` (dict): The scenario data to execute.

**Returns**:
- `bool`: True if the scenario executed successfully, False otherwise.

**Raises**:
- `TypeError`: If `scenario` is not a dictionary or if keys are incorrect.
- `ValueError`: If required data is missing in `scenario`.


### `insert_grabbed_data`

**Description**: Inserts grabbed product data into PrestaShop.

**Parameters**:
- `product_fields` (`ProductFields`): An object containing product data to be inserted.

**Returns**:
- None

**Raises**:
- `PrestaShopAPIError`: If there is an issue with the PrestaShop API call.
- `ValueError`: If `product_fields` is invalid or missing required data.


### `execute_PrestaShop_insert`

**Description**: Synchronously executes a PrestaShop insert operation.

**Parameters**:
- `product_fields` (`ProductFields`): Object containing product data to insert.

**Returns**:
- `bool`: True if the insertion was successful, False otherwise.

**Raises**:
- `PrestaShopAPIError`: If the PrestaShop API call fails.


### `execute_PrestaShop_insert_async`

**Description**: Asynchronously executes a PrestaShop insert operation.

**Parameters**:
- `product_fields` (`ProductFields`): Object containing product data to insert.

**Returns**:
- None

**Raises**:
- `PrestaShopAPIError`: If the PrestaShop API call fails.


### `add_coupon`

**Description**: Adds a coupon to the PrestaShop system.

**Parameters**:
- `credentials` (dict): PrestaShop API credentials (api_domain, api_key).
- `reference` (str): Product reference.
- `coupon_code` (str): Coupon code.
- `start_date` (str): Coupon start date.
- `end_date` (str): Coupon end date.

**Returns**:
- None

**Raises**:
- `PrestaShopAPIError`: If there is an error with the PrestaShop API.
- `ValueError`: If any of the required parameters are missing or invalid.


## Examples

The provided examples demonstrate various usages of the module functions.  Refer to the code comments for detailed explanations and examples.


```
```