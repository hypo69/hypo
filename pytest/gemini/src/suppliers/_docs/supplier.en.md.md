```python
import pytest
from typing import List, Dict
from unittest.mock import MagicMock

# Mock the Driver class for testing purposes
class MockDriver:
    def __init__(self):
        self.logged_in = False

    def login(self):
        self.logged_in = True

    def close(self):
        pass

    def get(self, url):
        pass
    
    def find_element(self, *args):
        return MagicMock()
    
    def find_elements(self, *args):
        return [MagicMock()]

# Mock the ConfigLoader class
class MockConfigLoader:
    def __init__(self, data=None):
      if data is None:
        self.data = {
                "settings": {"test": "value"},
                "locators": {"test_locator": "xpath://test"},
                "login_data": {"user": "test_user", "pass": "test_pass"}
            }
      else:
        self.data = data
    def load(self, key):
        if key in self.data:
            return self.data[key]
        return None


# Mock the specific module for supplier functions
class MockModule:
    def scenario_runner(self, scenario, **kwargs):
        return True
    def login_action(self, driver, login_data):
        driver.login()
        return True

# Assuming a simplified Supplier class for testing, replace with your actual class
class Supplier:
    def __init__(self, supplier_prefix: str, locale: str = 'en', webdriver: str | MockDriver | bool = 'default', *attrs, **kwargs):
        self.supplier_id = f"{supplier_prefix}_{locale}"
        self.supplier_prefix = supplier_prefix
        self.locale = locale
        self.supplier_settings = None
        self.price_rule = None
        self.related_modules = MockModule()
        self.scenario_files = []
        self.current_scenario = None
        self.login_data = None
        self.locators = None
        self.driver = None
        self.parsing_method = 'webdriver'
        self.config_loader = MockConfigLoader()
        self._payload(webdriver, *attrs, **kwargs)

    def _payload(self, webdriver: str | MockDriver | bool, *attrs, **kwargs) -> bool:
        self.supplier_settings = self.config_loader.load("settings")
        self.locators = self.config_loader.load("locators")
        self.login_data = self.config_loader.load("login_data")

        if webdriver == 'default':
            self.driver = MockDriver()
        elif isinstance(webdriver, str) and webdriver != 'default':
            # For cases where a specific driver type is passed as string
            self.driver = MockDriver() #Simplified for mock
        elif isinstance(webdriver, MockDriver):
            self.driver = webdriver
        elif webdriver is True:
            self.driver = MockDriver()
        else:
            self.driver = None

        return True

    def login(self) -> bool:
        if self.driver and self.login_data:
            return self.related_modules.login_action(self.driver, self.login_data)
        return False

    def run_scenario_files(self, scenario_files: str | List[str] = None) -> bool:
      if scenario_files is None:
        scenario_files = self.scenario_files
      if isinstance(scenario_files, str):
          scenario_files = [scenario_files]
      
      for file in scenario_files:
        if self.related_modules.scenario_runner(scenario = f"running {file}"):
          continue
        else:
          return False
      
      return True

    def run_scenarios(self, scenarios: dict | list[dict]) -> bool:
        if isinstance(scenarios, dict):
          scenarios = [scenarios]
        for scenario in scenarios:
          if self.related_modules.scenario_runner(scenario=scenario):
            continue
          else:
            return False
        return True


# Fixture definitions
@pytest.fixture
def mock_supplier():
    """Provides a Supplier object for testing."""
    return Supplier(supplier_prefix='test_supplier', locale='en')

@pytest.fixture
def mock_supplier_with_mockdriver():
    """Provides a Supplier object with a mock driver."""
    return Supplier(supplier_prefix='test_supplier', locale='en', webdriver=MockDriver())

@pytest.fixture
def mock_supplier_with_custom_data():
    """Provides a Supplier object with a mock driver."""
    data = {
                "settings": {"test": "custom"},
                "locators": {"test_locator": "xpath://custom"},
                "login_data": {"user": "custom_user", "pass": "custom_pass"}
            }
    return Supplier(supplier_prefix='test_supplier', locale='en', config_loader=MockConfigLoader(data))


# Tests for __init__ method
def test_supplier_init_default(mock_supplier):
    """Checks initialization with default values."""
    assert mock_supplier.supplier_prefix == 'test_supplier'
    assert mock_supplier.locale == 'en'
    assert mock_supplier.supplier_id == 'test_supplier_en'
    assert mock_supplier.driver is not None
    assert mock_supplier.supplier_settings is not None
    assert mock_supplier.locators is not None
    assert mock_supplier.login_data is not None
    assert isinstance(mock_supplier.driver, MockDriver)
    
def test_supplier_init_with_string_driver():
    """Checks initialization with string driver."""
    supplier = Supplier(supplier_prefix='test_supplier', locale='en', webdriver='chrome')
    assert isinstance(supplier.driver, MockDriver)

def test_supplier_init_with_custom_driver():
    """Checks initialization with a MockDriver instance."""
    mock_driver = MockDriver()
    supplier = Supplier(supplier_prefix='test_supplier', locale='en', webdriver=mock_driver)
    assert supplier.driver is mock_driver

def test_supplier_init_with_true_driver():
    """Checks initialization with a MockDriver instance."""
    supplier = Supplier(supplier_prefix='test_supplier', locale='en', webdriver=True)
    assert isinstance(supplier.driver, MockDriver)

def test_supplier_init_no_driver():
    """Checks initialization with a no driver."""
    supplier = Supplier(supplier_prefix='test_supplier', locale='en', webdriver=False)
    assert supplier.driver is None
    
def test_supplier_init_with_custom_data(mock_supplier_with_custom_data):
  """Checks the load of custom data during init"""
  assert mock_supplier_with_custom_data.supplier_settings["test"] == "custom"
  assert mock_supplier_with_custom_data.locators["test_locator"] == "xpath://custom"
  assert mock_supplier_with_custom_data.login_data["user"] == "custom_user"

# Tests for _payload method
def test_payload_loads_config(mock_supplier):
    """Checks if _payload correctly loads configurations."""
    assert mock_supplier.supplier_settings is not None
    assert mock_supplier.locators is not None
    assert mock_supplier.login_data is not None
    
# Tests for login method
def test_login_success(mock_supplier_with_mockdriver):
    """Checks successful login."""
    assert mock_supplier_with_mockdriver.login() is True
    assert mock_supplier_with_mockdriver.driver.logged_in is True

def test_login_no_driver(mock_supplier):
    """Checks login attempt when no driver is available."""
    mock_supplier.driver = None
    assert mock_supplier.login() is False

def test_login_no_login_data(mock_supplier_with_mockdriver):
    """Checks login attempt when no login data is available."""
    mock_supplier_with_mockdriver.login_data = None
    assert mock_supplier_with_mockdriver.login() is False

# Tests for run_scenario_files method
def test_run_scenario_files_single_file(mock_supplier):
    """Checks execution of a single scenario file."""
    assert mock_supplier.run_scenario_files('test_scenario.json') is True

def test_run_scenario_files_multiple_files(mock_supplier):
    """Checks execution of multiple scenario files."""
    assert mock_supplier.run_scenario_files(['test_scenario1.json', 'test_scenario2.json']) is True

def test_run_scenario_files_no_files(mock_supplier):
  """Checks execution of no files provided"""
  assert mock_supplier.run_scenario_files() is True

def test_run_scenario_files_failed_scenario(mock_supplier):
    """Checks the failed scenario case"""
    mock_supplier.related_modules.scenario_runner = lambda scenario, **kwargs: False
    assert mock_supplier.run_scenario_files('test_scenario.json') is False

# Tests for run_scenarios method
def test_run_scenarios_single_scenario(mock_supplier):
    """Checks execution of a single scenario."""
    assert mock_supplier.run_scenarios({'action': 'scrape', 'target': 'product_list'}) is True
    
def test_run_scenarios_multiple_scenarios(mock_supplier):
  """Checks execution of multiple scenarios"""
  scenarios = [{'action': 'scrape', 'target': 'product_list'}, {'action':'check', 'target': 'availability'}]
  assert mock_supplier.run_scenarios(scenarios) is True
  
def test_run_scenarios_failed_scenario(mock_supplier):
    """Checks the failed scenario case"""
    mock_supplier.related_modules.scenario_runner = lambda scenario, **kwargs: False
    assert mock_supplier.run_scenarios({'action': 'scrape', 'target': 'product_list'}) is False
    
def test_run_scenarios_empty_scenario(mock_supplier):
    """Checks running an empty scenario list"""
    assert mock_supplier.run_scenarios([]) is True

```