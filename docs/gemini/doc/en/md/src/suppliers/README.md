# Supplier Class Documentation

## Overview

This module provides the `Supplier` class, a base class for managing interactions with various suppliers (e.g., Amazon, Walmart, Mouser, Digi-Key).  It handles initialization, configuration, authentication, and scenario execution for different data sources.  Custom suppliers can be easily integrated by extending this class.

## Table of Contents

* [Supplier Class](#supplier-class)
* [Attributes](#attributes)
* [Methods](#methods)
* [How It Works](#how-it-works)
* [Class Diagram](#class-diagram)

## Supplier Class

### `Supplier`

**Description**: The `Supplier` class is the foundation for handling supplier interactions. It manages initialization, configuration, authentication, and scenario execution.


## Attributes

* **`supplier_id`** *(int)*: A unique identifier for the supplier.
* **`supplier_prefix`** *(str)*: A prefix identifying the supplier (e.g., 'amazon', 'aliexpress').
* **`supplier_settings`** *(dict)*: Settings specific to the supplier, loaded from a JSON file.
* **`locale`** *(str)*: Localization code (default: 'en').
* **`price_rule`** *(str)*: Rules for price calculation (e.g., VAT rules).
* **`related_modules`** *(module)*: Supplier-specific helper modules.
* **`scenario_files`** *(list)*: List of scenario files to execute.
* **`current_scenario`** *(dict)*: The currently executing scenario.
* **`login_data`** *(dict)*: Login credentials and related data.
* **`locators`** *(dict)*: Locator dictionary for web elements.
* **`driver`** *(Driver)*: WebDriver instance for supplier website interaction.
* **`parsing_method`** *(str)*: Data parsing method (e.g., 'webdriver', 'api', 'xls', 'csv').


## Methods

### `__init__`

**Description**: Constructor for the `Supplier` class.

**Parameters**:
* `supplier_prefix` (str): Prefix for the supplier.
* `locale` (str, optional): Localization code. Defaults to 'en'.
* `webdriver` (str | Driver | bool, optional): WebDriver type. Defaults to 'default'.

**Raises**:
* `DefaultSettingsException`: If default settings are not configured correctly.


### `_payload`

**Description**: Loads supplier configurations and initializes the WebDriver.

**Parameters**:
* `webdriver` (str | Driver | bool): WebDriver type.

**Returns**:
* bool: `True` if payload loaded successfully, `False` otherwise.


### `login`

**Description**: Handles authentication for the supplier's website.

**Returns**:
* bool: `True` if login was successful, `False` otherwise.


### `run_scenario_files`

**Description**: Executes one or more scenario files.

**Parameters**:
* `scenario_files` (str | List[str], optional): List or single path to scenario files.  Defaults to `None`.

**Returns**:
* bool: `True` if all scenarios executed successfully, `False` otherwise.


### `run_scenarios`

**Description**: Executes provided scenarios.

**Parameters**:
* `scenarios` (dict | list[dict]): Scenarios to execute.

**Returns**:
* bool: `True` if all scenarios executed successfully, `False` otherwise.


## How It Works

1. **Initialization**: The `__init__` method sets up the supplier prefix, locale, and WebDriver.
2. **Configuration Loading**: `_payload` loads the configuration and initializes locators and WebDriver.
3. **Authentication**: `login` handles user login.
4. **Scenario Execution**: `run_scenario_files` and `run_scenarios` execute the defined scenarios.


## Class Diagram

```plaintext
Supplier
├── Attributes
│   ├── supplier_id: int
│   ├── supplier_prefix: str
│   ├── supplier_settings: dict
│   ├── locale: str
│   ├── price_rule: str
│   ├── related_modules: module
│   ├── scenario_files: list
│   ├── current_scenario: dict
│   ├── login_data: dict
│   ├── locators: dict
│   ├── driver: Driver
│   ├── parsing_method: str
│
├── Methods
│   ├── __init__(self, supplier_prefix: str, locale: str = 'en', webdriver: str | Driver | bool = 'default', *attrs, **kwargs)
│   ├── _payload(self, webdriver: str | Driver | bool, *attrs, **kwargs) -> bool
│   ├── login(self) -> bool
│   ├── run_scenario_files(self, scenario_files: str | List[str] = None) -> bool
│   ├── run_scenarios(self, scenarios: dict | list[dict]) -> bool
```