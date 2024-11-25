# hypotez/src/scenario/executor.py

## Overview

This module provides functions for executing scenarios, loading them from files,
extracting product information, and inserting it into PrestaShop.  It handles
loading scenario files, running individual scenarios, and managing the insertion
of product data into the PrestaShop platform.


## Classes

### `Product`

**Description**: Represents a product with details for insertion into PrestaShop.


**Methods**:

- `__init__`: Initializes the Product object with data.



## Functions

### `dump_journal`

**Description**: Saves the journal data to a JSON file.

**Parameters**:

- `s` (Supplier): The supplier instance.
- `journal` (dict): The journal data to save.

**Returns**:
  None


### `run_scenario_files`

**Description**: Executes a list of scenario files.

**Parameters**:

- `s` (Supplier): The supplier instance.
- `scenario_files_list` (List[Path] | Path): List of file paths to scenario files, or a single file path.

**Returns**:
  bool: True if all scenarios were executed successfully, False otherwise.

**Raises**:

- `TypeError`: If `scenario_files_list` is not a list or a Path object.


### `run_scenario_file`

**Description**: Loads and executes scenarios from a file.

**Parameters**:

- `s` (Supplier): The supplier instance.
- `scenario_file` (Path): Path to the scenario file.

**Returns**:
  bool: True if the scenario was executed successfully, False otherwise.

**Raises**:

- `FileNotFoundError`: If the scenario file does not exist.
- `json.JSONDecodeError`: If the scenario file has an invalid JSON format.


### `run_scenarios`

**Description**: Executes a list of scenarios (NOT FILES).

**Parameters**:

- `s` (Supplier): The supplier instance.
- `scenarios` (List[dict] | dict, optional): A list of scenario dictionaries or a single scenario dictionary. Defaults to None.
    - `scenarios` can be a list of dictionaries, a single dictionary or `None`, in which case it defaults to the `s.current_scenario`.

**Returns**:

- List | dict | False: The result of executing the scenarios (list or dictionary) or False for errors.


**Raises**:
- `TypeError`: If `scenarios` is not a list or a dictionary.


### `run_scenario`

**Description**: Executes a single scenario.

**Parameters**:

- `supplier` (Supplier): The supplier instance.
- `scenario` (dict): Dictionary containing scenario details.
- `scenario_name` (str): Name of the scenario.

**Returns**:

- List | dict | False: The result of executing the scenario or False if there's an error.


### `insert_grabbed_data`

**Description**: Inserts grabbed product data into PrestaShop.

**Parameters**:

- `product_fields` (ProductFields): Instance containing product information.

**Returns**:
  None

**Raises**:
  - Exception: Any exception during insertion.

### `execute_PrestaShop_insert_async`

**Description**: Asynchronously executes PrestaShop insertion.

**Parameters**:
- `f` (ProductFields): Product information.
- `coupon_code` (str, optional): Coupon code. Defaults to None.
- `start_date` (str, optional): Start date. Defaults to None.
- `end_date` (str, optional): End date. Defaults to None.


**Returns**:
  bool: True if successful, False otherwise.

**Raises**:
  - Exception: Any exception during insertion.



### `execute_PrestaShop_insert`

**Description**: Inserts the product into PrestaShop.

**Parameters**:

- `f` (ProductFields): Product information.
- `coupon_code` (str, optional): Coupon code. Defaults to None.
- `start_date` (str, optional): Start date. Defaults to None.
- `end_date` (str, optional): End date. Defaults to None.


**Returns**:
  bool: True if the insertion was successful, False otherwise.


**Raises**:

- Exception: Any exception during insertion.