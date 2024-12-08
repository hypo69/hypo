# Supplier Module

## Overview

This module defines the `Supplier` class, a base class for managing data suppliers. It provides a framework for interacting with various data sources (e.g., Amazon, AliExpress, Walmart) to collect data based on specified scenarios.  The class handles initialization, login, and scenario execution.

## Table of Contents

* [Supplier Class](#supplier-class)
    * [Initialization (`__init__`) Method](#initialization-init-method)
    * [_Payload Method](#_payload-method)
    * [Login Method (`login`) ](#login-method-login)
    * [Run Scenario Files Method (`run_scenario_files`) ](#run-scenario-files-method-run-scenario-files)
    * [Run Scenarios Method (`run_scenarios`) ](#run-scenarios-method-run-scenarios)


## Supplier Class

### Description

The `Supplier` class serves as a base class for managing data suppliers. It provides a framework for interacting with data sources, handling supplier-specific configurations, and executing data collection scenarios.

### Class Attributes

* `supplier_id`: Unique identifier for the supplier.
* `supplier_prefix`: Prefix for the supplier (e.g., `aliexpress`, `amazon`).
* `supplier_settings`: Settings for the supplier, loaded from a configuration file.
* `locale`: Localization code (e.g., `en`, `ru`).
* `price_rule`: Rule for calculating prices (e.g., adding VAT).
* `related_modules`: Module containing supplier-specific functions.
* `scenario_files`: List of scenario files to be executed.
* `current_scenario`: The currently executing scenario.
* `login_data`: Login credentials (if required).
* `locators`: Locators for web elements on the supplier's site.
* `driver`: Web driver for interacting with the supplier's site.
* `parsing_method`: Method for data parsing (e.g., `webdriver`, `api`, `xls`, `csv`).


### Methods

#### Initialization (`__init__`) Method

```python
def __init__(self, supplier_prefix: str, locale: str = 'en', webdriver: str | 'Driver' | bool = 'default', *attrs, **kwargs):
    """
    Args:
        supplier_prefix (str): Prefix for the supplier.
        locale (str, optional): Localization code. Defaults to 'en'.
        webdriver (str | 'Driver' | bool, optional): Webdriver type or instance. Defaults to 'default'.

    Raises:
        ValueError: If input parameters are invalid.
    """
    # Initializes supplier prefix, locale, and web driver
```

#### _Payload Method

```python
def _payload(self, webdriver: str | 'Driver' | bool, *attrs, **kwargs) -> bool:
    """
    Loads supplier-specific configurations, locators, and initializes the web driver.

    Args:
        webdriver (str | 'Driver' | bool): Webdriver type or instance.

    Returns:
        bool: True if configuration loading and driver initialization were successful, False otherwise.
    
    Raises:
        FileNotFoundError: If a configuration file is not found.
        Exception: For any other exceptions during configuration loading or driver initialization.
    """
    # Loads configuration files and initializes the web driver
```

#### Login Method (`login`)

```python
def login(self) -> bool:
    """
    Handles the login process for the supplier's site.

    Returns:
        bool: True if login was successful, False otherwise.

    Raises:
        Exception: For any exceptions during the login process.
    """
    # Performs login to the supplier's site
```

#### Run Scenario Files Method (`run_scenario_files`)

```python
def run_scenario_files(self, scenario_files: str | list[str] = None) -> bool:
    """
    Executes one or more scenario files.

    Args:
        scenario_files (str | list[str], optional): Scenario file(s) to execute. Defaults to None.

    Returns:
        bool: True if all scenarios are successfully completed, False otherwise.

    Raises:
        FileNotFoundError: If a scenario file is not found.
        Exception: For any exceptions during scenario execution.
    """
    # Executes scenario files and returns True if all scenarios are successfully completed
```

#### Run Scenarios Method (`run_scenarios`)

```python
def run_scenarios(self, scenarios: dict | list[dict]) -> bool:
    """
    Executes one or more scenarios.

    Args:
        scenarios (dict | list[dict]): Scenarios to execute.

    Returns:
        bool: True if all scenarios are successfully completed, False otherwise.

    Raises:
        Exception: For any exceptions during scenario execution.
    """
    # Executes given scenarios and returns True if all scenarios are successfully completed
```


```