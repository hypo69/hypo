# executor Module Documentation

## Overview

This module provides functions for running scenarios, handling scenario files, and interacting with the PrestaShop API.  It includes examples demonStarting how to use these functions to execute scenarios, process files, and work with products.  The module utilizes asynchronous operations (`async` functions) where applicable for improved performance.

## Table of Contents

* [Overview](#overview)
* [Functions](#functions)
    * [`run_scenario_files`](#run_scenario_files)
    * [`run_scenario_file`](#run_scenario_file)
    * [`run_scenarios`](#run_scenarios)
    * [`run_scenario`](#run_scenario)
    * [`insert_grabbed_data`](#insert_grabbed_data)
    * [`execute_PrestaShop_insert`](#execute_prestashop_insert)
    * [`execute_PrestaShop_insert_async`](#execute_prestashop_insert_async)
    * [`add_coupon`](#add_coupon)


## Functions

### `run_scenario_files`

**Description**: Executes a list of scenario files sequentially.

**Parameters**:
- `supplier` (object): An instance of a class (e.g., `MockSupplier`) containing information about the scenario files and related modules.  This object likely holds paths to files and necessary attributes for processing.
- `scenario_files` (list of Path): A list of file paths to scenario files.

**Returns**:
- `bool`: `True` if all scenarios executed successfully, `False` otherwise.

**Raises**:
- `FileNotFoundError`: If a scenario file in the list does not exist.
- `SomeError`: If there's an error during scenario execution (details not provided in the example code).


### `run_scenario_file`

**Description**: Executes a single scenario file.

**Parameters**:
- `supplier` (object): An instance of a class containing relevant scenario information.
- `scenario_file` (Path): The file path to the scenario file.

**Returns**:
- `bool`: `True` if the scenario file executed successfully, `False` otherwise.

**Raises**:
- `FileNotFoundError`: If the scenario file is not found.
- `SomeError`:  If errors occur during scenario execution.


### `run_scenarios`

**Description**: (Functionality not detailed in the provided code.  Assume it's a higher-level function to manage multiple scenarios.)

**Parameters**:  (Need detailed parameters from the actual function definition)

**Returns**: (Need detailed return type from the actual function definition)

**Raises**: (Need detailed exceptions from the actual function definition)


### `run_scenario`

**Description**: Executes a single scenario.

**Parameters**:
- `supplier` (object): An instance of a class with scenario management capabilities.
- `scenario` (dict): A dictionary containing the scenario data (e.g., URL, product details).

**Returns**:
- `bool`: `True` if the scenario executed successfully, `False` otherwise.

**Raises**:
- `SomeError`: If errors occur during scenario execution.


### `insert_grabbed_data`

**Description**: Inserts grabbed product data into PrestaShop.

**Parameters**:
- `product_fields` (object): An object (e.g., `ProductFields`) containing the product data to be inserted.

**Returns**:
- `None` (Implied from the example)

**Raises**:
- `PrestaShopAPIError`: If there's a problem communicating with the PrestaShop API.
- `SomeError`: For other potential insertion issues.


### `execute_PrestaShop_insert`

**Description**: Synchronously executes the insertion of product data into PrestaShop.

**Parameters**:
- `product_fields` (object): The product data to be inserted.

**Returns**:
- `bool`: `True` if the insertion was successful, `False` otherwise.

**Raises**:
- `PrestaShopAPIError`: If there's an issue with the PrestaShop API.
- `SomeError`: For other potential execution issues.


### `execute_PrestaShop_insert_async`

**Description**: Asynchronously executes the insertion of product data into PrestaShop.

**Parameters**:
- `product_fields` (object): The product data to be inserted.

**Returns**:
- `None` (Implied from the example)

**Raises**:
- `PrestaShopAPIError`: If there's an issue with the PrestaShop API.
- `SomeError`: For other potential execution issues.



### `add_coupon`

**Description**: Adds a coupon to the PrestaShop system.

**Parameters**:
- `credentials` (dict): Credentials for accessing the PrestaShop API.
- `reference` (str): The reference ID for the product associated with the coupon.
- `coupon_code` (str): The coupon code to be added.
- `start_date` (str): The start date of the coupon validity (YYYY-MM-DD format).
- `end_date` (str): The end date of the coupon validity (YYYY-MM-DD format).


**Returns**:
- `None` (Implied from the example)

**Raises**:
- `PrestaShopAPIError`: If there's a problem with the PrestaShop API.
- `ValueError`: If invalid date formats are provided.
- `SomeError`: For other potential issues.