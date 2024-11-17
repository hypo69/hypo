
Here's a detailed explanation of what the `Supplier` class does, in English:

### Overview of the `Supplier` Class

The `Supplier` class serves as a base class for managing data suppliers in your application. It provides a framework for interacting with various data sources, such as Amazon, AliExpress, Walmart, and others. This class handles the initialization of supplier-specific settings, manages scenarios for data collection, and provides methods for logging in and executing scenarios.

### Components of the `Supplier` Class

#### 1. **Class Attributes**
   - `supplier_id`: Unique identifier for the supplier.
   - `supplier_prefix`: Prefix for the supplier, e.g., `aliexpress` or `amazon`.
   - `supplier_settings`: Settings for the supplier, loaded from a configuration file.
   - `locale`: Localization code (e.g., `en` for English, `ru` for Russian).
   - `price_rule`: Rule for calculating prices (e.g., adding VAT or applying discounts).
   - `related_modules`: Module containing supplier-specific functions.
   - `scenario_files`: List of scenario files to be executed.
   - `current_scenario`: The currently executing scenario.
   - `login_data`: Login credentials for accessing the supplier’s website (if required).
   - `locators`: Locators for web elements on the supplier’s site.
   - `driver`: Web driver for interacting with the supplier’s site.
   - `parsing_method`: Method for data parsing (e.g., `webdriver`, `api`, `xls`, `csv`).

#### 2. **Methods**
   - `__init__`: Constructor that initializes attributes based on the supplier prefix and other parameters.
     ```python
     def __init__(self, supplier_prefix: str, locale: str = 'en', webdriver: str | Driver | bool = 'default', *attrs, **kwargs):
         # Initializes supplier prefix, locale, and web driver
     ```

   - `_payload`: Loads supplier-specific configurations, locators, and initializes the web driver.
     ```python
     def _payload(self, webdriver: str | Driver | bool, *attrs, **kwargs) -> bool:
         # Loads configuration files and initializes the web driver
     ```

   - `login`: Handles the login process for the supplier’s site if authentication is required.
     ```python
     def login(self) -> bool:
         # Performs login to the supplier's site
     ```

   - `run_scenario_files`: Executes one or more scenario files.
     ```python
     def run_scenario_files(self, scenario_files: str | List[str] = None) -> bool:
         # Executes scenario files and returns True if all scenarios are successfully completed
     ```

   - `run_scenarios`: Executes one or more scenarios.
     ```python
     def run_scenarios(self, scenarios: dict | list[dict]) -> bool:
         # Executes given scenarios and returns True if all scenarios are successfully completed
     ```

### How It Works

1. **Initialization**:
   When an object of the `Supplier` class is created, the `__init__` method initializes the supplier prefix, locale, and web driver.
   ```python
   supplier = Supplier(supplier_prefix='aliexpress', locale='en', webdriver='chrome')
   ```

2. **Configuration Loading**:
   The `_payload` method loads configuration files for the supplier, including settings, locators, and initializes the web driver.
   ```python
   def _payload(self, webdriver: str | Driver | bool, *attrs, **kwargs) -> bool:
       # Loads configuration files and sets up the web driver
   ```

3. **Login**:
   The `login` method handles the authentication process for the supplier’s website.
   ```python
   supplier.login()
   ```

4. **Executing Scenarios**:
   - `run_scenario_files` method runs scenarios from a list of files.
     ```python
     supplier.run_scenario_files(['example_scenario.json'])
     ```
   - `run_scenarios` method runs scenarios based on specific conditions or tasks.
     ```python
     supplier.run_scenarios([{'action': 'scrape', 'target': 'product_list'}])
     ```

### Visual Representation

The `Supplier` class acts as a blueprint for managing data collection from various suppliers. It defines common methods and attributes that can be used or extended by specific implementations for different suppliers. The class centralizes supplier management, including configuration, login, and scenario execution.

### Example Usage

Here is an example of how you might use the `Supplier` class:

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

In summary, the `Supplier` class provides a structured way to interact with data suppliers by managing configurations, performing logins, and executing data collection scenarios. It serves as a foundational component that can be extended for specific suppliers by inheriting from this base class and adding or overriding functionality as needed.

