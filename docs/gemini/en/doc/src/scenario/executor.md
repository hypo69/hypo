# hypotez/src/scenario/executor.py

## Overview

This module provides functions for executing scenarios, loading them from files, and handling the process of extracting product information and inserting it into PrestaShop. It utilizes various libraries like `requests`, `asyncio`, and `json` for data manipulation and communication.


## Functions

### `dump_journal`

**Description**: Saves the journal data to a JSON file.

**Parameters**:

- `s` (Supplier instance): The supplier instance.
- `journal` (dict): The dictionary containing the journal data.

**Raises**:
- No exceptions explicitly raised in the function.


### `run_scenario_files`

**Description**: Executes a list of scenario files.

**Parameters**:

- `s` (Supplier instance): The supplier instance.
- `scenario_files_list` (List[Path] | Path): A list of file paths or a single file path for scenario files.

**Returns**:

- `bool`: True if all scenarios were executed successfully, False otherwise.

**Raises**:

- `TypeError`: If `scenario_files_list` is not a list or a Path object.


### `run_scenario_file`

**Description**: Loads and executes scenarios from a file.

**Parameters**:

- `s` (Supplier instance): The supplier instance.
- `scenario_file` (Path): Path to the scenario file.

**Returns**:

- `bool`: True if the scenario was executed successfully, False otherwise.

**Raises**:

- `FileNotFoundError`: If the scenario file is not found.
- `json.JSONDecodeError`: If the scenario file is not valid JSON.
- `Exception`: For other potential errors during scenario execution.


### `run_scenarios`

**Description**: Executes a list of scenarios.

**Parameters**:

- `s` (Supplier instance): The supplier instance.
- `scenarios` (List[dict] | dict, optional): A list of scenarios or a single scenario as a dictionary. Defaults to `s.current_scenario`.
- `_journal` (dict, optional): The journal. Defaults to `_journal` (global variable).

**Returns**:

- `List | dict | False`: The result of executing the scenarios. Returns a list or dictionary, depending on the input data type. Returns `False` for errors.

**Raises**:

- No exceptions explicitly raised in the function


### `run_scenario`

**Description**: Executes a single scenario.

**Parameters**:

- `supplier` (Supplier instance): Supplier instance.
- `scenario` (dict): Dictionary containing scenario details.
- `scenario_name` (str): Name of the scenario.
- `_journal` (dict, optional): The journal. Defaults to None.

**Returns**:

- `List | dict | False`: The result of executing the scenario.

**Raises**:

- `Exception`: If any error happens during scenario execution.

### `insert_grabbed_data`

**Description**: Inserts grabbed product data into PrestaShop.

**Parameters**:

- `product_fields` (ProductFields): ProductFields instance containing the product information.

**Raises**:
- No exceptions explicitly raised in the function.


### `execute_PrestaShop_insert`

**Description**: Inserts the product into PrestaShop.

**Parameters**:

- `f` (ProductFields): ProductFields instance containing the product information.
- `coupon_code` (str, optional): Optional coupon code. Defaults to `None`.
- `start_date` (str, optional): Optional start date for the promotion. Defaults to `None`.
- `end_date` (str, optional): Optional end date for the promotion. Defaults to `None`.

**Returns**:

- `bool`: True if the insertion was successful, False otherwise.

**Raises**:

- `Exception`: If any error occurs during the insertion process.