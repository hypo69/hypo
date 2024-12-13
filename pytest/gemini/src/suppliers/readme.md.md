```python
import pytest
from unittest.mock import MagicMock, patch
from typing import List, Dict
from hypotez.src.suppliers.webdriver import Driver
from hypotez.src.suppliers import Supplier
from hypotez.src.exceptions import DefaultSettingsException

# Mock the necessary modules and classes to isolate tests
@pytest.fixture
def mock_driver():
    """Provides a mock Driver object."""
    mock = MagicMock(spec=Driver)
    return mock

@pytest.fixture
def mock_supplier_settings():
    """Provides mock supplier settings data."""
    return {
        "locators": {"search_input": "input#search"},
        "login_data": {"username": "testuser", "password": "testpassword"},
        "scenario_files": ["test_scenario1.json", "test_scenario2.json"],
        "related_modules": None,  # Simulate related modules as None
        "price_rule": "default_rule"
    }

@pytest.fixture
def mock_supplier(mock_driver, mock_supplier_settings):
    """Provides a mock Supplier object."""
    supplier = Supplier(supplier_prefix='test_supplier', webdriver=mock_driver)
    supplier.supplier_settings = mock_supplier_settings
    supplier.driver = mock_driver
    supplier.locators = mock_supplier_settings.get('locators', {})
    supplier.login_data = mock_supplier_settings.get('login_data', {})
    supplier.scenario_files = mock_supplier_settings.get('scenario_files', [])
    supplier.related_modules = mock_supplier_settings.get('related_modules', None)
    supplier.price_rule = mock_supplier_settings.get('price_rule', 'default_rule')

    return supplier


class TestSupplier:
    """Tests for the Supplier class."""

    def test_supplier_init_valid_prefix(self):
        """Checks successful initialization with valid prefix and default values."""
        supplier = Supplier(supplier_prefix='test_prefix')
        assert supplier.supplier_prefix == 'test_prefix'
        assert supplier.locale == 'en'
        assert supplier.driver is None  # No webdriver initialized initially

    def test_supplier_init_custom_locale(self):
        """Checks successful initialization with a custom locale."""
        supplier = Supplier(supplier_prefix='test_prefix', locale='ru')
        assert supplier.locale == 'ru'

    def test_supplier_init_custom_webdriver_str(self):
        """Checks successful initialization with custom webdriver type as string."""
        supplier = Supplier(supplier_prefix='test_prefix', webdriver='chrome')
        assert supplier.driver is None  # Still no driver instance.

    def test_supplier_init_custom_webdriver_bool(self):
        """Checks successful initialization with custom webdriver type as bool."""
        supplier = Supplier(supplier_prefix='test_prefix', webdriver=True)
        assert supplier.driver is None  # Still no driver instance.

    def test_supplier_init_default_settings_exception(self):
        """Checks the exception when there are default settings are misconfigured."""
        with pytest.raises(DefaultSettingsException):
            Supplier(supplier_prefix='invalid_prefix')

    def test_supplier_payload_success(self, mock_supplier, mock_driver, mock_supplier_settings):
        """Checks that _payload method loads settings and initializes webdriver correctly."""
        result = mock_supplier._payload(webdriver=mock_driver)
        assert result is True
        # Here, verify that the mock_driver has been set and other relevant attributes.
        assert mock_supplier.driver == mock_driver
        assert mock_supplier.locators == mock_supplier_settings.get("locators")
        assert mock_supplier.login_data == mock_supplier_settings.get("login_data")
        assert mock_supplier.scenario_files == mock_supplier_settings.get("scenario_files")
        assert mock_supplier.related_modules == mock_supplier_settings.get("related_modules")
        assert mock_supplier.price_rule == mock_supplier_settings.get("price_rule")

    def test_supplier_payload_invalid_webdriver(self, mock_supplier):
         """Checks the correct behavior if a wrong webdriver passed to `payload`."""
         # For the test, just check that no error raised with this setup.
         assert mock_supplier._payload(webdriver = 'not_valid') == True

    def test_supplier_login_success(self, mock_supplier, mock_driver):
        """Checks that login method calls the driver login method."""
        mock_driver.login.return_value = True
        assert mock_supplier.login() is True
        mock_driver.login.assert_called_once()

    def test_supplier_login_failure(self, mock_supplier, mock_driver):
        """Checks that login method returns False if login fails."""
        mock_driver.login.return_value = False
        assert mock_supplier.login() is False
        mock_driver.login.assert_called_once()

    def test_run_scenario_files_success(self, mock_supplier, mock_driver):
        """Checks successful execution of scenario files."""
        mock_driver.run_scenario.return_value = True
        scenario_files = ['test_scenario1.json', 'test_scenario2.json']
        assert mock_supplier.run_scenario_files(scenario_files=scenario_files) is True
        assert mock_driver.run_scenario.call_count == len(scenario_files)

    def test_run_scenario_files_single_file_success(self, mock_supplier, mock_driver):
        """Checks successful execution of a single scenario file."""
        mock_driver.run_scenario.return_value = True
        assert mock_supplier.run_scenario_files(scenario_files='test_scenario.json') is True
        mock_driver.run_scenario.assert_called_once()

    def test_run_scenario_files_no_files(self, mock_supplier):
        """Checks that execution is skipped if no scenario files are provided."""
        assert mock_supplier.run_scenario_files() is True

    def test_run_scenario_files_failure(self, mock_supplier, mock_driver):
        """Checks failure if any scenario file execution fails."""
        mock_driver.run_scenario.side_effect = [True, False]
        scenario_files = ['test_scenario1.json', 'test_scenario2.json']
        assert mock_supplier.run_scenario_files(scenario_files=scenario_files) is False
        assert mock_driver.run_scenario.call_count == len(scenario_files)


    def test_run_scenarios_success(self, mock_supplier, mock_driver):
        """Checks successful execution of multiple scenarios."""
        mock_driver.run_scenario.return_value = True
        scenarios = [{'action': 'scrape', 'target': 'product_list'}, {'action': 'search', 'keyword': 'test'}]
        assert mock_supplier.run_scenarios(scenarios=scenarios) is True
        assert mock_driver.run_scenario.call_count == len(scenarios)

    def test_run_scenarios_empty_list(self, mock_supplier):
        """Checks execution is skipped if the list of scenarios is empty."""
        assert mock_supplier.run_scenarios(scenarios=[]) is True

    def test_run_scenarios_empty_dict(self, mock_supplier):
        """Checks execution is skipped if the list of scenarios is empty."""
        assert mock_supplier.run_scenarios(scenarios={}) is True

    def test_run_scenarios_failure(self, mock_supplier, mock_driver):
        """Checks failure if any scenario execution fails."""
        mock_driver.run_scenario.side_effect = [True, False]
        scenarios = [{'action': 'scrape', 'target': 'product_list'}, {'action': 'search', 'keyword': 'test'}]
        assert mock_supplier.run_scenarios(scenarios=scenarios) is False
        assert mock_driver.run_scenario.call_count == len(scenarios)
```