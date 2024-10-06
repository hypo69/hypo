""" <b>Class</b> `Supplier` <b>Base class for all suppliers</b>
Provides methods and attributes for a specific
data supplier: e.g., amazon.com, walmart.com, mouser.com, digikey.com, or custom ones.
Several suppliers are already created in the program, others will be defined by the customer.
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
@dotfile suppliers//supplier.dot
"""
...
## \file ../src/suppliers/supplier.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
...
import importlib
from pathlib import Path
from typing import List
from types import SimpleNamespace

from src import gs
from src.utils import j_loads, j_loads_ns
from src.webdriver import Driver, Firefox, Chrome, Edge
from src.scenario import (
    run_scenarios,
    run_scenario_files,
)
from src.logger import logger
from src.logger.exceptions import DefaultSettingsException

class Supplier:
    """ Supplier class. Executes scenarios: `scenario->executer` -> `executor->grabber` -> `grabber->prestashop`
    @image html supplier.png
    @details Essentially, this is the central class around which the program revolves. `Supplier` takes the prefix of 
    a specific supplier (amazon, aliexpress, ...) and connects its functions via the `related_modules` interface. 
    Everything related to a specific supplier is located in a directory named after the supplier.
    @param supplier_prefix `str`  : Supplier prefix. Prefixes can be found in the Google spreadsheet:
        Table of suppliers: https://docs.google.com/spreadsheets/d/14f0PyQa32pur-sW2MBvA5faIVghnsA0hWClYoKpkFBQ/edit?usp=sharing
    @param locale `str`  : Locale code in ISO 639-1  
            `en`, `he`, `ru`   
            Language for scenario execution  
            Two-letter ISO 639-1 code
    @param supplier_settings `dict`  : Each supplier has unique settings defined in the `src/suppliers/<supplier_prefix>/settings.json` file in the specific supplier's directory.
    @param price_rule `str`  : Determines the price calculation.  
        For example, to add VAT, use `*1.17`, to decrease the price by 100, use `-100`.
    @param login_data `dict`  : Dictionary of login data for accessing the website (if required).
    @param related_modules   : Functions relevant to each supplier.
    @param current_scenario `dict`  : Currently executing scenario.
    @param locators `dict`  : Locators for page elements.
    @param driver `Driver`  : Web driver.
    @param parsing_method `str`  : Parsing method:   
        - `webdriver` : WebDriver
        - `api` : API 
        - `xls` : Excel
        - `csv` : CSV
    """
    # Class attributes declaration
    supplier_id: int = None
    supplier_prefix: str = None
    supplier_settings: dict = None
    locale: str = None
    price_rule: str = None
    related_modules = None
    scenario_files: list = None
    current_scenario: dict = None

    login_data: dict = {
        'if_login': None,
        'login_url': None,
        'user': None,
        'password': None,
    }
    
    locators: dict = {
        'store': None,
        'login': None,
        'category': None,
        'product': None,
    }
    """  _var locators  Dictionary of web element locators on pages `product`, `category`, `login`, `store`.
    Each key will be populated with a dictionary of web elements from files `product.json`, `category.json`, `login.json`, `store.json`
    located in the directory `<supplier_prefix>/locators`. """

    def __init__(self, supplier_prefix: str, locale: str = 'en', webdriver: str | Driver | bool = 'default', *attrs, **kwargs):
        """ 
        @param supplier_prefix `str` supplier_prefix e.g., 'aliexpress'
                        Table of suppliers: https://docs.google.com/spreadsheets/d/14f0PyQa32pur-sW2MBvA5faIVghnsA0hWClYoKpkFBQ/edit?usp=sharing
        @param webdriver - WebDriver mode (default False)
        WebDriver modes: False, 'chrome', 'firefox', 'edge', 'default'
        """
        self.supplier_prefix = supplier_prefix
        self.locale = locale 

        if not self._payload(webdriver, *attrs, **kwargs): 
            raise DefaultSettingsException(f'Error starting supplier ', supplier_prefix )

    def _payload(self, webdriver: str | Driver | bool, *attrs, **kwargs) -> bool:
        """ Load supplier parameters
        @param webdriver - WebDriver mode (default False)
        WebDriver modes: False, 'chrome', 'firefox', 'edge', 'default'
        """
        logger.info(self.supplier_prefix)        

        self.supplier_home_dir = Path(gs.path.src, 'suppliers', self.supplier_prefix)
        
        self.related_modules = importlib.import_module(f'src.suppliers.{self.supplier_prefix}')
        """ `self.related_modules`  Additional functions from the module `<supplier_prefix>` """
        
        self.supplier_settings = j_loads(
            Path(self.supplier_home_dir, f'{self.supplier_prefix}.json'))
        """ supplier_settings: `self.supplier_settings` Default settings for this supplier, read from file <supplier_prefix>.json """

        # Execute scenario via grabber
        self.price_rule = self.supplier_settings.get('price_rule', 0)
        self.supplier_id = self.supplier_settings['supplier_id']
        """ Supplier ID
        Google spreadsheet of suppliers can be found here:  
        https://docs.google.com/spreadsheets/d/14f0PyQa32pur-sW2MBvA5faIVghnsA0hWClYoKpkFBQ/edit?usp=sharing
       """

        """  If scenario list is NOT defined during class initialization - take all from supplier's scenarios folder.  
        I still left the option to change the list before starting the collection of scenarios.  
        All scenario files paths are converted to absolute paths.
        """
        self.scenario_files = [ Path(self.supplier_home_dir, 'scenarios', scenario_filename) for scenario_filename 
                               in self.supplier_settings.get('scenario_files', 
                                [ Path(self.supplier_home_dir, 'scenarios', scenario_filename) for scenario_filename 
                                 in Path(self.supplier_home_dir, 'scenarios').iterdir() 
                                 if scenario_filename.suffix == '.json' ] ) ]
        

        locators_path =  Path(self.supplier_home_dir, 'locators')
        self.locator: SimpleNamespace = SimpleNamespace(**{
            'store': j_loads_ns(Path(locators_path, 'store.json')),
            'login': j_loads_ns(Path(locators_path, 'login.json')),
            'category': j_loads_ns(Path(locators_path, 'category.json')),
            'product': j_loads_ns(Path(locators_path, 'product.json')),
        })
       
        """  locators `dict` - Dictionary of web element locators on pages `product`, `category`, `login`, `store`.
        Each page type corresponds to its own JSON file: `product.json`, `category.json`, `login.json`, `store.json`
        Files for each supplier are located in corresponding directories `<supplier_prefix>/locators` """     

        # ~~~~~~~~~~~~~~~~~ debug ~~~~~~~
        # _start_time = int(time.time())
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        if not webdriver: ...
        else:
            if webdriver == 'chrome':
                WebDriver = Chrome
            elif webdriver == 'firefox':
                WebDriver = Firefox
            elif webdriver == 'edge':
                WebDriver = Edge

            self.driver = Driver(WebDriver)
            
            # ~~~~~~~~~~~~~~~~~ debug ~~~~~~~~~~~~
            # logger.success(f""" ... driver connected in {int(time.time()) - _start_time} seconds """)
            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
           
        return True

    def login(self) -> bool:
        """  Log in to the supplier website.  
         Handling the situation where logging into the supplier's site requires authentication.
        @returns: `True` if login success, else `False`
        """
        ...
        return self.related_modules.login(self)

    def run_scenario_files(self, scenario_files: str | List[str] = None) -> bool:
        """  Execute one or more scenario files.
          The function starts the executor `run_scenarios()` and passes it a list of scenario files in the variable `scenario_files`.
        @details (`src.scenarios.executor.run_scenarios()`).
        @param scenario_files `list[str] | str`: List of scenario file names
        @returns bool `True` if all scenarios in the list are successfully completed by the executor, otherwise: `False`
        @todo What if one scenario returns `False`, but others return `True`? Still get an overall `False`?
        Need to test this situation.
        """
        ...
        scenario_files = self.scenario_files if not scenario_files else scenario_files
        return run_scenario_files(self, scenario_files)

    def run_scenarios(self, scenarios: dict | list[dict]) -> bool:
        """  Function to execute a list or single scenario.
        @param scenarios `dict | list[dict]` : Scenario / list of scenarios to execute.
        @returns bool `True` if the scenario is successfully completed by the executor, otherwise: `False`
        """
        ...
        return run_scenarios(self, scenarios)
    
    ...
    # Other methods and class members continue here...

