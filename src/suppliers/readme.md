 <b>Class</b> `Supplier` <b>Base class for all suppliers</b>
Provides methods and attributes for a specific
Thank you for sharing the entire `Supplier` class code. Based on the provided class and its description, here is an overview of its structure, attributes, methods, and their purposes:

### Overview of `Supplier` Class

#### **Attributes:**
- **`supplier_id`**: Identifier for the supplier.
- **`supplier_prefix`**: Prefix or identifier for the supplier, e.g., 'amazon', 'aliexpress'.
- **`supplier_settings`**: Configuration settings specific to the supplier, loaded from a JSON file.
- **`locale`**: Locale code for language, default is 'en'.
- **`price_rule`**: Rule for calculating prices, e.g., adding VAT.
- **`related_modules`**: Additional functions or modules related to the specific supplier.
- **`scenario_files`**: List of scenario files to execute.
- **`current_scenario`**: Currently executing scenario.
- **`login_data`**: Dictionary of login credentials and URLs.
- **`locators`**: Dictionary of locators for web elements on various pages.
- **`driver`**: Instance of `Driver` for interacting with web browsers.

#### **Methods:**

1. **`__init__`**:
   - Initializes the `Supplier` class.
   - Takes parameters to set up the supplier, locale, and WebDriver.
   - Loads supplier-specific settings and locators.

2. **`_payload`**:
   - Loads the supplier's settings and locators.
   - Configures the WebDriver if needed.

3. **`login`**:
   - Handles logging into the supplier's website if authentication is required.
   - Calls the `login` method from the related module.

4. **`run_scenario_files`**:
   - Executes one or more scenario files.
   - Uses the `run_scenario_files` function from `src.scenario`.

5. **`run_scenarios`**:
   - Executes a list or single scenario.
   - Uses the `run_scenarios` function from `src.scenario`.

#### **Dependencies:**
- **`importlib`**: For dynamic module imports.
- **`pathlib.Path`**: For path manipulations.
- **`typing.List`**: For type hinting.
- **`types.SimpleNamespace`**: For dynamic attributes.
- **`src.settings.gs`**: For accessing settings.
- **`src.utils.j_loads`**: For loading JSON data.
- **`src.webdriver.Driver`, `Firefox`, `Chrome`, `Edge`**: For browser automation.
- **`src.scenario.run_scenarios`, `run_scenario_files`**: For executing scenarios.
- **`src.logger.logger`**: For logging.
- **`src.exceptions.DefaultSettingsException`**: For custom exceptions.

### Explanation:

The `Supplier` class is designed to handle interactions with various suppliers by loading their specific settings and scenarios, handling authentication if needed, and executing predefined scenarios. It uses a combination of configuration files and dynamic module imports to support different suppliers, making it flexible and extensible. The class relies heavily on external modules and functions for its operations, ensuring that the core logic remains focused on supplier-specific details.
data supplier: e.g., amazon.com, walmart.com, mouser.com, digikey.com, or custom ones.
Several suppliers are already created in the program, others will be defined by the customer.
<pre>
+-----------------+          +-----------------+
|     Driver      |          |   Supplier      |
+-----------------+          +-----------------+
| - html_content  |          | - scenario_file |
| + execute_locator() |       | + load_scenario()|
+-----------------+          +-----------------+
          |                           |
          |                           |
          |                           |
          | uses                      | instructs
          |                           |
          v                           v
+-----------------+          +-----------------+
| ExecuteLocator  |          |     Page        |
+-----------------+          +-----------------+
| - driver        |          | - product_elements |
| - actions       |          +-----------------+
| - by_mapping    |          | + handle_elements() |
+-----------------+          +-----------------+
| + execute_locator(locator, message, typing_speed, continue_on_error) | 
+-----------------+          
          |
          | handles
          v
+-----------------+
|      Page       |
+-----------------+
| - product_elements  |
+-----------------+
| + handle_elements() |
+-----------------+
</pre>
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


<pre>
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
│
├── Methods
│   ├── __init__(self, supplier_prefix: str, locale: str = 'en', webdriver: str | Driver | bool = 'default', *attrs, **kwargs)
│   │   ├── importlib.import_module(f'src.suppliers.{self.supplier_prefix}')
│   │   ├── j_loads(Path(self.supplier_home_dir, f'{self.supplier_prefix}.json'))
│   │   ├── Path(gs.path.src, 'suppliers', self.supplier_prefix)
│   │   ├── self._payload(webdriver, *attrs, **kwargs)
│   │
│   ├── _payload(self, webdriver: str | Driver | bool, *attrs, **kwargs) -> bool
│   │   ├── logger.info(self.supplier_prefix)
│   │   ├── j_loads_ns(Path(locators_path, 'store.json'))
│   │   ├── j_loads_ns(Path(locators_path, 'login.json'))
│   │   ├── j_loads_ns(Path(locators_path, 'category.json'))
│   │   ├── j_loads_ns(Path(locators_path, 'product.json'))
│   │   ├── Path(self.supplier_home_dir, 'scenarios', scenario_filename)
│   │   ├── Driver(WebDriver)
│   │
│   ├── login(self) -> bool
│   │   ├── self.related_modules.login(self)
│   │
│   ├── run_scenario_files(self, scenario_files: str | List[str] = None) -> bool
│   │   ├── run_scenario_files(self, scenario_files)
│   │
│   ├── run_scenarios(self, scenarios: dict | list[dict]) -> bool
│       ├── run_scenarios(self, scenarios)
│
├── Dependencies
│   ├── importlib
│   ├── pathlib.Path
│   ├── typing.List
│   ├── types.SimpleNamespace
│   ├── src.settings.gs
│   ├── src.utils.j_loads
│   ├── src.utils.j_loads_ns
│   ├── src.webdriver.Driver
│   ├── src.webdriver.Firefox
│   ├── src.webdriver.Chrome
│   ├── src.webdriver.Edge
│   ├── src.scenario.run_scenarios
│   ├── src.scenario.run_scenario_files
│   ├── src.logger.logger
│   ├── src.exceptions.DefaultSettingsException
</pre>


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

