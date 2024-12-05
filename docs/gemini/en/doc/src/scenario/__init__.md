# Module: hypotez/src/scenario/__init__.py

## Overview

This module provides functions for executing scenarios for suppliers.  It handles both single scenario files and lists of scenarios, allowing for flexible execution.  It interacts with the `Supplier` object for managing scenario execution.


## Functions

### `run_scenario_files`

**Description**: Executes multiple scenario files.

**Parameters**:
- `supplier` (Supplier): The supplier object to run scenarios against.
- `scenario_files` (list[str]): A list of file paths containing scenario data.

**Returns**:
- `None`: This function doesn't return a value directly; it executes the scenarios.

**Raises**:
- `ValueError`: If `scenario_files` is not a list of strings, or if any file in the list is not found.
- `Exception`: Any other exception raised during scenario execution within `run_scenario_file`.


### `run_scenarios`

**Description**: Executes multiple scenarios.

**Parameters**:
- `supplier` (Supplier): The supplier object to run scenarios against.
- `scenarios` (list[dict] | dict): A list of scenario dictionaries or a single scenario dictionary.

**Returns**:
- `None`: This function doesn't return a value directly; it executes the scenarios.

**Raises**:
- `TypeError`: If `scenarios` is not a list of dictionaries or a single dictionary.
- `Exception`: Any other exception raised during scenario execution within `run_scenario`.


### `run_scenario_file`

**Description**: Executes a single scenario file.

**(Note: This function is *not* directly exported from the init file, but inferred from the code. It is assumed to exist in the underlying module.)**

**Parameters**:  (Assuming parameters based on common practice)
- `supplier` (Supplier): The supplier object to run scenarios against.
- `scenario_file` (str): The path to the scenario file.

**Returns**:
- `None`: This function does not return a value directly.

**Raises**:
- `FileNotFoundError`: If the `scenario_file` does not exist.
- `Exception`: Any other exception that might occur during file reading, parsing, or execution.


### `run_scenario`

**Description**: Executes a single scenario.

**(Note: This function is *not* directly exported from the init file, but inferred from the code. It is assumed to exist in the underlying module.)**

**Parameters**:  (Assuming parameters based on common practice)
- `supplier` (Supplier): The supplier object to run scenarios against.
- `scenario` (dict): A scenario dictionary.

**Returns**:
- `None`: This function does not return a value directly.

**Raises**:
- `Exception`: Any other exception that might occur during scenario execution.


### `execute_PrestaShop_insert`

**(Note: This function is *not* directly documented in the input, but appears in the imported functions.)**


### `execute_PrestaShop_insert_async`

**(Note: This function is *not* directly documented in the input, but appears in the imported functions.)**


## Module Level Variables

### `MODE`

**Description**: Holds the current execution mode (e.g., 'dev', 'prod').


## Module Usage Examples

The provided docstring includes examples of how to use the `run_scenario_files` and `run_scenarios` functions with various input types.  Refer to the docstring for complete usage examples.

```
```