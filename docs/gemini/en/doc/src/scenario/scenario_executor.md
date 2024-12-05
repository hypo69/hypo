# Scenario Executor Module

## Overview

This module provides functionality for executing scenarios defined in various input files.  It handles loading, parsing, and running scenario files, iterating over scenarios within each file, and finally, handling errors and returning success/failure status.

## Table of Contents

* [Scenario Executor Module](#scenario-executor-module)
* [Overview](#overview)
* [Classes](#classes)
* [Functions](#functions)


## Classes

### `ScenarioExecutor`

**Description**:  The `ScenarioExecutor` class encapsulates the logic for executing a series of scenarios defined in a list of input files.

**Methods**:

* `execute(scenario_files: list) -> bool`: Executes a list of scenario files.
    * **Description**: This method takes a list of scenario file paths as input and runs all scenarios contained within them.
    * **Parameters**:
        * `scenario_files` (list): A list of file paths to scenario files.
    * **Returns**:
        * `bool`: `True` if all scenarios were executed successfully, `False` otherwise.


## Functions

### `load_scenarios(file_path: str) -> list | None`

**Description**: Loads and parses scenarios from a specified file.

**Parameters**:
* `file_path` (str): The path to the scenario file.

**Returns**:
* `list | None`: A list of scenario objects if successful, or `None` if the file cannot be loaded or parsed, or if the file content is invalid.

**Raises**:
* `FileNotFoundError`: If the specified file does not exist.
* `ValueError`: If the file format is invalid or if there is an issue parsing the scenarios within the file.


### `run_scenario(scenario: Scenario) -> bool`

**Description**: Executes a single scenario.

**Parameters**:
* `scenario` (Scenario): The scenario object to execute.

**Returns**:
* `bool`: `True` if the scenario was executed successfully, `False` otherwise.

**Raises**:
* `Exception`: For any other unexpected errors encountered during scenario execution.



### `navigate_to_url(url: str) -> bool`:

**Description**: Navigates to a given URL.

**Parameters**:
* `url` (str): The URL to navigate to.

**Returns**:
* `bool`: `True` if the URL was successfully navigated to, `False` otherwise.


### `get_list_of_products(url: str) -> list | None`:

**Description**: Retrieves a list of products from a given URL.

**Parameters**:
* `url` (str): The URL to retrieve products from.

**Returns**:
* `list | None`: A list of product information if successful, `None` otherwise.


### `navigate_to_product_page(product_url: str) -> bool`:

**Description**: Navigates to a product page.

**Parameters**:
* `product_url` (str): The URL of the product page.

**Returns**:
* `bool`: `True` if the product page was successfully navigated to, `False` otherwise.

### `grab_product_fields(product_page: str) -> dict | None`:

**Description**: Extracts product information from a product page.

**Parameters**:
* `product_page` (str): The HTML content of the product page.

**Returns**:
* `dict | None`: A dictionary containing the extracted product fields if successful, `None` otherwise.

### `create_product_object(product_data: dict) -> Product | None`:

**Description**: Creates a product object from extracted data.

**Parameters**:
* `product_data` (dict): A dictionary containing product information.

**Returns**:
* `Product | None`: A Product object if successful, `None` otherwise.

### `insert_product_into_prestashop(product_object: Product) -> bool`:

**Description**: Inserts the product into PrestaShop.

**Parameters**:
* `product_object` (Product): The product object to insert.

**Returns**:
* `bool`: `True` if the product was successfully inserted, `False` otherwise.


### `update_journal(success: bool) -> None`

**Description**: Updates a journal entry based on the result of the scenario execution.


**Parameters**:

*   `success` (bool): A boolean indicating whether the scenario execution was successful.


**Returns**:

*   `None`