# Supplier Module

## Overview

This module defines the `Supplier` class, a base class for managing data suppliers.  It provides a framework for interacting with various data sources (e.g., Amazon, AliExpress, Walmart) by handling initialization, data collection, login, and scenario execution.

## Table of Contents

* [Supplier Class](#supplier-class)
    * [Overview](#overview-of-the-supplier-class)
    * [Components](#components-of-the-supplier-class)
        * [Class Attributes](#class-attributes)
        * [Methods](#methods)
    * [How It Works](#how-it-works)
    * [Example Usage](#example-usage)
    * [Summary](#summary)


## Supplier Class

### Overview of the Supplier Class

The `Supplier` class serves as a base class for managing data suppliers. It provides a framework for interacting with various data sources, handling supplier-specific settings, data collection, login, and scenario execution.

### Components of the Supplier Class

#### Class Attributes

| Attribute        | Type                                    | Description                                                                                               |
|-----------------|-------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| `supplier_id`   | Unique Identifier                       | Unique identifier for the supplier.                                                                       |
| `supplier_prefix`| str                                   | Prefix for the supplier (e.g., `aliexpress` or `amazon`).                                                  |
| `supplier_settings`| dict                                | Settings for the supplier, loaded from a configuration file.                                              |
| `locale`        | str                                   | Localization code (e.g., `en` for English, `ru` for Russian).                                       |
| `price_rule`    | Callable                              | Rule for calculating prices (e.g., adding VAT or applying discounts).                                    |
| `related_modules`| str or Module                           | Module containing supplier-specific functions.                                                             |
| `scenario_files`| List[str]                              | List of scenario files to be executed.                                                                      |
| `current_scenario`| str or None                           | The currently executing scenario.                                                                       |
| `login_data`    | dict or None                           | Login credentials for accessing the supplier’s website (if required).                               |
| `locators`      | dict                                 | Locators for web elements on the supplier’s site.                                                            |
| `driver`        | `Driver` or str or bool or None             | Web driver for interacting with the supplier’s site (e.g., 'chrome', 'firefox'). If str, assumes the browser name. |
| `parsing_method`| str                                   | Method for data parsing (e.g., `webdriver`, `api`, `xls`, `csv`).                                    |


#### Methods

##### `__init__`

```python
def __init__(self, supplier_prefix: str, locale: str = 'en', webdriver: str | Driver | bool = 'default', *attrs, **kwargs) -> None:
    """
    Constructor that initializes attributes based on the supplier prefix and other parameters.

    Args:
        supplier_prefix (str): The prefix for the supplier.
        locale (str, optional): The localization code. Defaults to 'en'.
        webdriver (str | Driver | bool, optional): The webdriver to use. Defaults to 'default'.
    """
    # Initializes supplier prefix, locale, and web driver
```

##### `_payload`

```python
def _payload(self, webdriver: str | Driver | bool, *attrs, **kwargs) -> bool:
    """
    Loads supplier-specific configurations, locators, and initializes the web driver.

    Args:
        webdriver (str | Driver | bool): The webdriver to use.

    Returns:
        bool: True if the payload was loaded successfully.

    """
    # Loads configuration files and initializes the web driver
```

##### `login`

```python
def login(self) -> bool:
    """
    Handles the login process for the supplier’s site if authentication is required.

    Returns:
        bool: True if login was successful.
    """
    # Performs login to the supplier's site
```

##### `run_scenario_files`

```python
def run_scenario_files(self, scenario_files: str | List[str] = None) -> bool:
    """
    Executes one or more scenario files.

    Args:
        scenario_files (str | List[str], optional): The scenario file(s) to execute. Defaults to None.

    Returns:
        bool: True if all scenarios are successfully completed.
    """
    # Executes scenario files and returns True if all scenarios are successfully completed
```

##### `run_scenarios`

```python
def run_scenarios(self, scenarios: dict | list[dict]) -> bool:
    """
    Executes one or more scenarios.

    Args:
        scenarios (dict | list[dict]): The scenarios to execute.

    Returns:
        bool: True if all scenarios are successfully completed.
    """
    # Executes given scenarios and returns True if all scenarios are successfully completed
```


### How It Works

1. Initialization: The `__init__` method initializes the supplier's attributes.
2. Configuration Loading: The `_payload` method loads supplier-specific configurations and initializes the web driver.
3. Login: The `login` method handles the authentication process.
4. Scenario Execution: `run_scenario_files` and `run_scenarios` methods execute the defined scenarios.

### Example Usage

```python
# Create a Supplier object for 'aliexpress'
supplier = Supplier(supplier_prefix='aliexpress', locale='en', webdriver='chrome')

# Perform login to the supplier’s site
supplier.login()

# Execute scenario files
supplier.run_scenario_files(['example_scenario.json'])

# Or execute specific scenarios
supplier.run_scenarios([{'action': 'scrape', 'target': 'product_list'}])
```

### Summary

The `Supplier` class provides a structured approach to managing data suppliers, handling configurations, logins, and scenario execution.  This serves as a base class, allowing for the creation of specific supplier implementations.