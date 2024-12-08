# Module: hypotez/src/suppliers/supplier.py

## Overview

This module defines the `Supplier` base class for executing scenarios for various suppliers.  It handles loading supplier configurations, executing login procedures, and running predefined scenarios.

## Table of Contents

- [Supplier Class](#supplier-class)
- [Functions](#functions)


## Supplier Class

### `Supplier`

**Description**: The base class for interacting with and executing scenarios for specific suppliers. It loads supplier-specific configurations, manages the driver, and handles scenario execution.

**Attributes**:

- `supplier_id` (Optional[int]): Identifier for the supplier.
- `supplier_prefix` (str): A prefix identifying the supplier.  Crucial for locating configuration files.
- `locale` (str): Locale code (e.g., 'en'). Defaults to 'en'.
- `price_rule` (Optional[str]): Price calculation rule.
- `related_modules` (Optional[ModuleType]):  A module containing supplier-specific functions (e.g., login).
- `scenario_files` (List[str]): List of scenario files to run.
- `current_scenario` (Dict[str, Any]): Current scenario being executed.
- `locators` (Dict[str, Any]):  Page element locators.
- `driver` (Optional[Driver]): WebDriver instance.


**Methods**:

- [`__init__(self, **data)`](#__init__-self-data)]
- [`_payload(self)`](#_payload-self)]
- [`login(self)`](#login-self)]
- [`run_scenario_files(self, scenario_files=None)`](#run-scenario-files-self-scenario-files-none)]
- [`run_scenarios(self, scenarios)`](#run-scenarios-self-scenarios)]


### `__init__(self, **data)`

**Description**: Initializes the `Supplier` object, loading supplier configuration.

**Raises**:

- `DefaultSettingsException`: If configuration loading fails.


### `_payload(self)`

**Description**: Loads supplier settings from a JSON file using `j_loads_ns`.  Imports the module associated with the `supplier_prefix` to get appropriate functions.

**Returns**:

- `bool`: `True` if loading was successful, `False` otherwise.

**Raises**:

- `ModuleNotFoundError`: If the supplier-specific module cannot be found.


### `login(self)`

**Description**: Executes the login process for the supplier.

**Returns**:

- `bool`: `True` if login is successful, `False` otherwise.


### `run_scenario_files(self, scenario_files=None)`

**Description**: Runs one or more scenario files.

**Args**:

- `scenario_files` (Optional[str | List[str]]): A list of scenario files to run.  If `None`, defaults to `self.scenario_files`.

**Returns**:

- `bool`: `True` if all scenarios are run successfully, `False` otherwise.


### `run_scenarios(self, scenarios)`

**Description**: Runs a single scenario or a list of scenarios.

**Args**:

- `scenarios` (dict | List[dict]): The scenario or list of scenarios to run.

**Returns**:

- `bool`: `True` if all scenarios are run successfully, `False` otherwise.


## Functions

No additional functions are defined outside of the `Supplier` class.