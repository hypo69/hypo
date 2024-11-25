# Module: src.suppliers.supplier

## Overview

This module defines the `Supplier` class, responsible for executing scenarios for various suppliers. It handles loading supplier configurations, executing login procedures, and running scenario files.

## Table of Contents

* [Classes](#classes)
    * [Supplier](#supplier)
* [Functions](#functions)


## Classes

### `Supplier`

**Description**: The `Supplier` class represents a specific supplier and manages its execution context. It loads supplier-specific configurations, handles login, and runs provided scenarios.

**Attributes**:

- `supplier_id` (Optional[int]): The ID of the supplier.
- `supplier_prefix` (str): A prefix identifying the supplier.
- `locale` (str): The locale code (e.g., 'en'). Defaults to 'en'.
- `price_rule` (Optional[str]): The price calculation rule.
- `related_modules` (Optional[ModuleType]): The Python module containing supplier-specific functions.
- `scenario_files` (List[str]): A list of scenario files to execute. Defaults to an empty list.
- `current_scenario` (Dict[str, Any]): The currently executing scenario. Defaults to an empty dictionary.
- `locators` (Dict[str, Any]): Locators for page elements. Defaults to an empty dictionary.
- `driver` (Optional[Driver]): The web driver instance.


**Methods**:

- [`__init__(self, **data)`](#__init__): Initializes the supplier and loads its configuration.
- [`_payload(self) -> bool`](#_payload): Loads the supplier's parameters from a JSON file.
- [`login(self) -> bool`](#login): Executes the login process for the supplier.
- [`run_scenario_files(self, scenario_files: Optional[str | List[str]] = None) -> bool`](#run_scenario_files): Runs one or more scenario files.
- [`run_scenarios(self, scenarios: dict | List[dict]) -> bool`](#run_scenarios): Runs a single or a list of scenarios.

### `Supplier.__init__`

**Description**: Initializes a `Supplier` object, loading its configuration.

**Parameters**:

- `**data` (dict): Keyword arguments to initialize the `Supplier` object.


**Raises**:
- `DefaultSettingsException`: If there's an error during the supplier initialization.


### `Supplier._payload`

**Description**: Loads the supplier's parameters from a JSON file using `j_loads_ns`.

**Parameters**:
  - None

**Returns**:
- `bool`: `True` if the loading is successful, `False` otherwise.


**Raises**:
- `ModuleNotFoundError`: if the supplier-specific module is not found.
- Various exceptions during `j_loads_ns` execution.



### `Supplier.login`

**Description**: Executes the login process for the supplier.

**Parameters**:
  - None

**Returns**:
- `bool`: `True` if the login was successful, `False` otherwise.


### `Supplier.run_scenario_files`

**Description**: Runs one or more scenario files.

**Parameters**:

- `scenario_files` (Optional[str | List[str]]): A list of scenario files to execute. If `None`, defaults to `self.scenario_files`.

**Returns**:
- `bool`: `True` if all scenarios are run successfully, `False` otherwise.


### `Supplier.run_scenarios`

**Description**: Runs a single or a list of scenarios.

**Parameters**:

- `scenarios` (dict | List[dict]): The scenario or list of scenarios to execute.

**Returns**:
- `bool`: `True` if the scenario is run successfully, `False` otherwise.


### `Supplier.check_supplier_prefix`

**Description**: Validator for the `supplier_prefix` attribute. Checks if it's empty.

**Parameters**:

- `value` (str): The value of `supplier_prefix`.

**Returns**:
- `str`: The validated `supplier_prefix`.

**Raises**:

- `ValueError`: If `supplier_prefix` is empty.


## Functions

(No functions defined in the file other than class methods)