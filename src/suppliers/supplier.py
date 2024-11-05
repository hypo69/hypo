## \file ./src/suppliers/supplier.py
# -*- coding: utf-8 -*-
#! /venv/Scripts/python.exe
#! /usr/bin/python
# /path/to/interpreter/python
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


@dotfile suppliers//supplier.dot
"""
import importlib
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional
from types import SimpleNamespace

from src import gs
from src.utils import j_loads, j_loads_ns
from src.webdriver import Driver
from src.scenario import (
    run_scenarios,
    run_scenario_files,
)
from src.logger import logger
from src.logger.exceptions import DefaultSettingsException

from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional
from types import ModuleType
import importlib

from src import gs
from src.utils import j_loads
from src.webdriver import Driver
from src.logger import logger
from src.logger.exceptions import DefaultSettingsException

@dataclass(frozen=True)
class Supplier:
    """Supplier class. Executes scenarios for various suppliers.
    
    This class takes the prefix of a specific supplier (e.g., amazon, aliexpress)
    and connects its functions via the related_modules interface.
    
    Attributes:
        supplier_id (int): Identifier for the supplier.
        supplier_prefix (str): Supplier prefix.
        locale (str): Locale code in ISO 639-1.
        price_rule (str): Rule for calculating prices.
        related_modules (ModuleType): Functions relevant to each supplier.
        scenario_files (List[str]): List of scenario files to execute.
        current_scenario (dict): Currently executing scenario.
        locators (dict): Locators for page elements.
        driver (Driver): Web driver.
    """
    
    supplier_id: int = field(default=None)
    supplier_prefix: str = field(default=None)
    locale: str = field(default='en')
    price_rule: str = field(default=None)
    related_modules: Optional[ModuleType] = field(default=None)  
    scenario_files: List[str] = field(default_factory=list)
    current_scenario: dict = field(default_factory=dict)
    locators: dict = field(default_factory=dict)
    driver: Driver = field(default=None)
    
    def __post_init__(self):
        """Initializes the supplier by loading its configuration."""
        if not self._payload():
            raise DefaultSettingsException(f'Error starting supplier: {self.supplier_prefix}')

    def _payload(self) -> bool:
        """Load supplier parameters.

        Returns:
            bool: True if loading was successful, otherwise False.
        """
        logger.info(f'Loading settings for supplier: {self.supplier_prefix}')
        
        # Import the related module for the specific supplier
        try:
            related_module = importlib.import_module(f'src.suppliers.{self.supplier_prefix}')
            object.__setattr__(self, 'related_modules', related_module)
        except ModuleNotFoundError as e:
            logger.error(f'Related module not found for supplier {self.supplier_prefix}: {e}')
            return False
        
        # Construct the path for supplier settings based on the supplier prefix
        settings_path = gs.path.src / 'suppliers' / f'{self.supplier_prefix}_settings.json'
        
        # Load settings and locators here
        try:
            # Assuming j_loads function reads JSON files and returns a dictionary
            settings = j_loads(settings_path)
            if not settings:
                logger.error(f'No settings found for supplier: {self.supplier_prefix}')
                return False
            
            # Load individual settings into the class attributes
            object.__setattr__(self, 'price_rule', settings.get('price_rule', 'default_rule'))
            object.__setattr__(self, 'locale', settings.get('locale', 'en'))
            object.__setattr__(self, 'scenario_files', settings.get('scenario_files', []))
            object.__setattr__(self, 'locators', settings.get('locators', {}))
            
            logger.info(f'Successfully loaded settings for supplier: {self.supplier_prefix}')
            return True
        
        except Exception as e:
            logger.error(f'Error loading settings for supplier {self.supplier_prefix}: {e}')
            return False

 

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

