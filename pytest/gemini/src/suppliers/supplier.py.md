```python
import pytest
from typing import List, Dict, Any, Optional
from unittest.mock import patch, mock_open, MagicMock
from pydantic import ValidationError
from src.suppliers.supplier import Supplier
from src.logger.exceptions import DefaultSettingsException
import src.gs as gs
from src.webdriver.driver import Driver
import importlib

# Fixture for a valid Supplier instance
@pytest.fixture
def valid_supplier_data():
    return {
        "supplier_prefix": "test_supplier",
        "locale": "en",
        "scenario_files": ["scenario1.json", "scenario2.json"],
        "locators": {"button1": "locator1", "button2": "locator2"},
    }


@pytest.fixture
def mock_j_loads_ns():
    """Mocks j_loads_ns function and returns a SimpleNamespace object."""
    with patch('src.suppliers.supplier.j_loads_ns') as mock:
        mock.return_value = MagicMock(
            price_rule='custom_rule',
            locale='fr',
            scenario_files=['scenario3.json'],
            locators={'input1': 'locator3'}
            )
        yield mock
        

@pytest.fixture
def mock_module_not_found_j_loads_ns():
    """Mocks j_loads_ns function and returns None."""
    with patch('src.suppliers.supplier.j_loads_ns') as mock:
        mock.return_value = None
        yield mock
    
@pytest.fixture
def mock_import_module_success():
    """Mocks importlib.import_module to return a mock module"""
    with patch('src.suppliers.supplier.importlib.import_module') as mock:
        mock.return_value = MagicMock(login=lambda x: True)
        yield mock
        
@pytest.fixture
def mock_import_module_fail():
    """Mocks importlib.import_module to raise ModuleNotFoundError"""
    with patch('src.suppliers.supplier.importlib.import_module') as mock:
        mock.side_effect = ModuleNotFoundError
        yield mock

@pytest.fixture
def mock_run_scenario_files_success():
    with patch('src.suppliers.supplier.run_scenario_files') as mock:
        mock.return_value = True
        yield mock
        
@pytest.fixture
def mock_run_scenario_files_fail():
    with patch('src.suppliers.supplier.run_scenario_files') as mock:
        mock.return_value = False
        yield mock

@pytest.fixture
def mock_run_scenarios_success():
    with patch('src.suppliers.supplier.run_scenarios') as mock:
        mock.return_value = True
        yield mock

@pytest.fixture
def mock_run_scenarios_fail():
    with patch('src.suppliers.supplier.run_scenarios') as mock:
        mock.return_value = False
        yield mock


class TestSupplier:
    def test_supplier_creation_valid_data(self, valid_supplier_data, mock_j_loads_ns, mock_import_module_success):
        """Checks that a Supplier instance can be created with valid data."""
        supplier = Supplier(**valid_supplier_data)
        assert supplier.supplier_prefix == "test_supplier"
        assert supplier.locale == "fr"
        assert supplier.scenario_files == ['scenario3.json']
        assert supplier.locators == {'input1': 'locator3'}
        assert supplier.price_rule == 'custom_rule'

    def test_supplier_creation_empty_prefix(self):
         """Checks that a ValueError is raised if the supplier_prefix is empty."""
         with pytest.raises(ValueError, match="supplier_prefix не может быть пустым"):
             Supplier(supplier_prefix="")
             
    def test_supplier_creation_payload_fail(self, valid_supplier_data, mock_module_not_found_j_loads_ns, mock_import_module_fail):
        """Checks that a DefaultSettingsException is raised if the _payload method returns False."""
        with pytest.raises(DefaultSettingsException, match=r"Ошибка запуска поставщика: test_supplier"):
                Supplier(**valid_supplier_data)

    def test_check_supplier_prefix_valid(self):
        """Checks that the check_supplier_prefix validator returns the value when it's not empty."""
        assert Supplier.check_supplier_prefix("test_prefix") == "test_prefix"

    def test_check_supplier_prefix_invalid(self):
        """Checks that the check_supplier_prefix validator raises an error when the value is empty."""
        with pytest.raises(ValueError, match="supplier_prefix не может быть пустым"):
            Supplier.check_supplier_prefix("")
            
    def test_payload_success(self, valid_supplier_data, mock_j_loads_ns, mock_import_module_success):
        """Checks that _payload method returns True when settings are loaded successfully."""
        supplier = Supplier(**valid_supplier_data)
        assert supplier.price_rule == "custom_rule"
        assert supplier.locale == "fr"
        assert supplier.scenario_files == ["scenario3.json"]
        assert supplier.locators == {"input1": "locator3"}
    
    def test_payload_module_not_found(self, valid_supplier_data, mock_j_loads_ns, mock_import_module_fail):
        """Checks that _payload method returns False when import module not found."""
        supplier = Supplier(**valid_supplier_data)
        assert supplier.related_modules is None

    def test_payload_settings_not_found(self, valid_supplier_data, mock_module_not_found_j_loads_ns, mock_import_module_success):
        """Checks that _payload method returns False when settings are not found."""
        supplier = Supplier(**valid_supplier_data)
        assert supplier.price_rule == None
        assert supplier.locale == 'en'
        assert supplier.scenario_files == []
        assert supplier.locators == {}
    
    def test_login_success(self, valid_supplier_data, mock_j_loads_ns, mock_import_module_success):
         """Checks that the login method returns True when login is successful."""
         supplier = Supplier(**valid_supplier_data)
         assert supplier.login() == True

    def test_run_scenario_files_success(self, valid_supplier_data, mock_j_loads_ns, mock_import_module_success, mock_run_scenario_files_success):
        """Checks that run_scenario_files method returns True when scenario files are executed successfully."""
        supplier = Supplier(**valid_supplier_data)
        assert supplier.run_scenario_files() == True
        mock_run_scenario_files_success.assert_called_once()

    def test_run_scenario_files_custom_list_success(self, valid_supplier_data, mock_j_loads_ns, mock_import_module_success, mock_run_scenario_files_success):
        """Checks that run_scenario_files method returns True when scenario files are executed successfully."""
        supplier = Supplier(**valid_supplier_data)
        assert supplier.run_scenario_files(['new_scenario1.json']) == True
        mock_run_scenario_files_success.assert_called_once()
    
    def test_run_scenario_files_fail(self, valid_supplier_data, mock_j_loads_ns, mock_import_module_success, mock_run_scenario_files_fail):
        """Checks that run_scenario_files method returns False when scenario files fail."""
        supplier = Supplier(**valid_supplier_data)
        assert supplier.run_scenario_files() == False
        mock_run_scenario_files_fail.assert_called_once()

    def test_run_scenarios_success(self, valid_supplier_data, mock_j_loads_ns, mock_import_module_success, mock_run_scenarios_success):
        """Checks that run_scenarios method returns True when scenarios are executed successfully."""
        supplier = Supplier(**valid_supplier_data)
        scenarios = [{"name": "scenario1"}, {"name": "scenario2"}]
        assert supplier.run_scenarios(scenarios) == True
        mock_run_scenarios_success.assert_called_once()
        
    def test_run_scenarios_single_success(self, valid_supplier_data, mock_j_loads_ns, mock_import_module_success, mock_run_scenarios_success):
        """Checks that run_scenarios method returns True when scenarios are executed successfully."""
        supplier = Supplier(**valid_supplier_data)
        scenario = {"name": "scenario1"}
        assert supplier.run_scenarios(scenario) == True
        mock_run_scenarios_success.assert_called_once()

    def test_run_scenarios_fail(self, valid_supplier_data, mock_j_loads_ns, mock_import_module_success, mock_run_scenarios_fail):
        """Checks that run_scenarios method returns False when scenario execution fails."""
        supplier = Supplier(**valid_supplier_data)
        scenarios = [{"name": "scenario1"}, {"name": "scenario2"}]
        assert supplier.run_scenarios(scenarios) == False
        mock_run_scenarios_fail.assert_called_once()
```