```python
import pytest
from pathlib import Path
from unittest.mock import MagicMock, patch
import json
from src.scenario.executor import (
    dump_journal,
    run_scenario_files,
    run_scenario_file,
    run_scenarios,
    run_scenario,
    insert_grabbed_data,
    execute_PrestaShop_insert,
    ProductFields,
    _journal,
)

from src.product import Product
from src.logger.exceptions import ProductFieldException
from src.logger.logger import logger


# Fixtures
@pytest.fixture
def mock_supplier():
    """Provides a mock supplier object."""
    supplier_mock = MagicMock()
    supplier_mock.supplier_abs_path = Path('/tmp/test_supplier')
    supplier_mock.scenario_files = [Path('/tmp/test_scenario1.json'), Path('/tmp/test_scenario2.json')]
    supplier_mock.supplier_prefix = "TEST"
    supplier_mock.driver = MagicMock()
    supplier_mock.related_modules = MagicMock()
    return supplier_mock


@pytest.fixture
def mock_product_fields():
    """Provides a mock product_fields object."""
    product_fields_mock = MagicMock(spec=ProductFields)
    product_fields_mock.presta_fields_dict = {"name": "Test Product", "price": 100}
    product_fields_mock.assist_fields_dict = {"brand": "Test Brand"}
    product_fields_mock.product_id = 123
    product_fields_mock.product_name = "Test Product Name"
    product_fields_mock.product_category = "Test Category"
    product_fields_mock.product_price = 99.99
    product_fields_mock.description = "Test Description"
    return product_fields_mock


@pytest.fixture
def mock_journal():
    """Provides a mock journal dict"""
    return {'scenario_files': {}, 'name': 'test'}

# Tests for dump_journal
def test_dump_journal(mock_supplier):
    """Checks if dump_journal correctly creates a json file."""
    test_journal = {'test_key': 'test_value'}
    
    with patch("src.scenario.executor.j_dumps") as mock_j_dumps:
         dump_journal(mock_supplier, test_journal)
         mock_j_dumps.assert_called_once()
         assert mock_j_dumps.call_args[0][0] == test_journal
         assert mock_j_dumps.call_args[0][1] == Path(mock_supplier.supplier_abs_path, '_journal', f"{test_journal['name']}.json")
         
# Tests for run_scenario_files
def test_run_scenario_files_valid_list(mock_supplier):
    """Checks correct behavior with a valid list of scenario files."""
    scenario_files = [Path('/tmp/test_scenario1.json'), Path('/tmp/test_scenario2.json')]
    with patch("src.scenario.executor.run_scenario_file", return_value=True) as mock_run_scenario_file:
        assert run_scenario_files(mock_supplier, scenario_files) == True
        assert mock_run_scenario_file.call_count == 2
        mock_run_scenario_file.assert_called_with(mock_supplier, scenario_files[1])
    assert _journal['scenario_files'][scenario_files[0].name]['message'] == f"{scenario_files[0]} completed successfully!"
    assert _journal['scenario_files'][scenario_files[1].name]['message'] == f"{scenario_files[1]} completed successfully!"

def test_run_scenario_files_valid_path(mock_supplier):
    """Checks correct behavior with a valid single path of scenario files."""
    scenario_file = Path('/tmp/test_scenario1.json')
    with patch("src.scenario.executor.run_scenario_file", return_value=True) as mock_run_scenario_file:
        assert run_scenario_files(mock_supplier, scenario_file) == True
        mock_run_scenario_file.assert_called_once_with(mock_supplier, scenario_file)
    assert _journal['scenario_files'][scenario_file.name]['message'] == f"{scenario_file} completed successfully!"

def test_run_scenario_files_empty_list(mock_supplier):
    """Checks correct behavior when an empty list is provided, uses supplier default."""
    with patch("src.scenario.executor.run_scenario_file", return_value=True) as mock_run_scenario_file:
        assert run_scenario_files(mock_supplier, []) == True
        assert mock_run_scenario_file.call_count == 2
        mock_run_scenario_file.assert_called_with(mock_supplier, mock_supplier.scenario_files[1])
    assert _journal['scenario_files'][mock_supplier.scenario_files[0].name]['message'] == f"{mock_supplier.scenario_files[0]} completed successfully!"
    assert _journal['scenario_files'][mock_supplier.scenario_files[1].name]['message'] == f"{mock_supplier.scenario_files[1]} completed successfully!"

def test_run_scenario_files_invalid_input(mock_supplier):
    """Checks correct exception raising for invalid input."""
    with pytest.raises(TypeError, match="scenario_files_list must be a list or a Path object."):
        run_scenario_files(mock_supplier, "invalid_input")


def test_run_scenario_files_scenario_failed(mock_supplier):
    """Checks correct behavior when scenario file execution fails."""
    scenario_files = [Path('/tmp/test_scenario1.json')]
    with patch("src.scenario.executor.run_scenario_file", return_value=False) as mock_run_scenario_file:
        assert run_scenario_files(mock_supplier, scenario_files) == True
    assert _journal['scenario_files'][scenario_files[0].name]['message'] == f"{scenario_files[0]} FAILED!"

def test_run_scenario_files_exception_in_scenario(mock_supplier):
    """Checks correct exception handling during scenario execution."""
    scenario_files = [Path('/tmp/test_scenario1.json')]
    with patch("src.scenario.executor.run_scenario_file", side_effect=Exception("Test Exception")):
        run_scenario_files(mock_supplier, scenario_files)
    assert _journal['scenario_files'][scenario_files[0].name]['message'] == f"Error: Test Exception"


# Tests for run_scenario_file
def test_run_scenario_file_success(mock_supplier):
    """Checks correct execution of scenarios from a file."""
    mock_file_path = Path('/tmp/test_scenario.json')
    mock_scenario_content = {'scenarios': {'scenario1': {'url': 'test_url1'}, 'scenario2': {'url': 'test_url2'}}}
    
    with patch("src.scenario.executor.j_loads", return_value=mock_scenario_content):
        with patch("src.scenario.executor.run_scenario", return_value=True) as mock_run_scenario:
            assert run_scenario_file(mock_supplier, mock_file_path) == True
            assert mock_run_scenario.call_count == 2
            mock_run_scenario.assert_called_with(mock_supplier, {'url': 'test_url2'}, 'scenario2')

def test_run_scenario_file_file_not_found(mock_supplier):
    """Checks behavior when scenario file is not found."""
    mock_file_path = Path('/tmp/nonexistent_scenario.json')
    with patch("src.scenario.executor.j_loads", side_effect=FileNotFoundError("File not found")):
        assert run_scenario_file(mock_supplier, mock_file_path) == False


def test_run_scenario_file_json_decode_error(mock_supplier):
    """Checks behavior when there's an error decoding the JSON file."""
    mock_file_path = Path('/tmp/invalid_json.json')
    with patch("src.scenario.executor.j_loads", side_effect=json.JSONDecodeError("Error", "doc", 0)):
        assert run_scenario_file(mock_supplier, mock_file_path) == False

def test_run_scenario_file_empty_scenarios(mock_supplier):
    """Checks behavior when scenarios is empty in the file."""
    mock_file_path = Path('/tmp/test_scenario.json')
    mock_scenario_content = {'scenarios': {}}

    with patch("src.scenario.executor.j_loads", return_value=mock_scenario_content):
        with patch("src.scenario.executor.run_scenario", return_value=True) as mock_run_scenario:
            assert run_scenario_file(mock_supplier, mock_file_path) == True
            assert mock_run_scenario.call_count == 0


# Tests for run_scenarios
def test_run_scenarios_list_input(mock_supplier, mock_journal):
    """Checks correct execution of multiple scenarios."""
    scenarios = [{'url': 'test_url1'}, {'url': 'test_url2'}]
    with patch("src.scenario.executor.run_scenario", return_value="test_result") as mock_run_scenario:
        result = run_scenarios(mock_supplier, scenarios, mock_journal)
        assert result == "test_result"
        assert mock_run_scenario.call_count == 2
        mock_run_scenario.assert_called_with(mock_supplier, {'url': 'test_url2'})
        assert mock_journal['scenario_files'][-1][{'url': 'test_url1'}] == "test_result"
        assert mock_journal['scenario_files'][-1][{'url': 'test_url2'}] == "test_result"

def test_run_scenarios_dict_input(mock_supplier, mock_journal):
    """Checks correct execution of a single scenario passed as a dict."""
    scenario = {'url': 'test_url1'}
    with patch("src.scenario.executor.run_scenario", return_value="test_result") as mock_run_scenario:
       result = run_scenarios(mock_supplier, scenario, mock_journal)
       assert result == "test_result"
       mock_run_scenario.assert_called_once_with(mock_supplier, scenario)
       assert mock_journal['scenario_files'][-1][{'url': 'test_url1'}] == "test_result"

def test_run_scenarios_no_input_from_supplier(mock_supplier, mock_journal):
    """Checks execution when no scenarios are passed, uses current_scenario from the supplier."""
    mock_supplier.current_scenario = {'url': 'test_url1'}
    with patch("src.scenario.executor.run_scenario", return_value="test_result") as mock_run_scenario:
        result = run_scenarios(mock_supplier, None, mock_journal)
        assert result == "test_result"
        mock_run_scenario.assert_called_once_with(mock_supplier, {'url': 'test_url1'})
        assert mock_journal['scenario_files'][-1][{'url': 'test_url1'}] == "test_result"

def test_run_scenarios_no_input_none_current_scenario(mock_supplier, mock_journal):
     """Checks the behavior when no scenarios are specified and current_scenario is not specified"""
     mock_supplier.current_scenario = None
     with patch("src.scenario.executor.run_scenario", return_value="test_result") as mock_run_scenario:
         result = run_scenarios(mock_supplier, None, mock_journal)
         assert result == "test_result"
         mock_run_scenario.assert_called_once()

# Tests for run_scenario
def test_run_scenario_success(mock_supplier, mock_product_fields):
    """Checks correct execution of a single scenario."""
    scenario = {'url': 'test_url', 'product_fields': {}}
    mock_supplier.related_modules.get_list_products_in_category.return_value = ['url1', 'url2']
    mock_supplier.related_modules.grab_product_page.return_value = "grabbed_fields"
    mock_supplier.related_modules.grab_page.return_value = mock_product_fields

    with patch("src.scenario.executor.insert_grabbed_data") as mock_insert_grabbed_data:
        assert run_scenario(mock_supplier, scenario, "test_scenario") == ['url1', 'url2']
        mock_supplier.driver.get_url.assert_called()
        mock_insert_grabbed_data.assert_called()
        assert mock_supplier.current_scenario == scenario


def test_run_scenario_no_products_in_category(mock_supplier):
    """Checks behavior when no products are found in the category."""
    scenario = {'url': 'test_url', 'product_fields': {}}
    mock_supplier.related_modules.get_list_products_in_category.return_value = []
    assert run_scenario(mock_supplier, scenario, "test_scenario") == None
    mock_supplier.driver.get_url.assert_called_once_with('test_url')


def test_run_scenario_navigation_error(mock_supplier, mock_product_fields):
    """Checks behavior when navigation to a product page fails."""
    scenario = {'url': 'test_url', 'product_fields': {}}
    mock_supplier.related_modules.get_list_products_in_category.return_value = ['url1', 'url2']
    mock_supplier.driver.get_url.side_effect = [True, False, True]
    mock_supplier.related_modules.grab_page.return_value = mock_product_fields

    with patch("src.scenario.executor.insert_grabbed_data") as mock_insert_grabbed_data:
        assert run_scenario(mock_supplier, scenario, "test_scenario") == ['url1', 'url2']
        assert mock_supplier.driver.get_url.call_count == 3
        mock_insert_grabbed_data.assert_called_once()

def test_run_scenario_grab_page_error(mock_supplier):
    """Checks behavior when grab_page return None."""
    scenario = {'url': 'test_url', 'product_fields': {}}
    mock_supplier.related_modules.get_list_products_in_category.return_value = ['url1']
    mock_supplier.related_modules.grab_page.return_value = None

    with patch("src.scenario.executor.insert_grabbed_data") as mock_insert_grabbed_data:
        assert run_scenario(mock_supplier, scenario, "test_scenario") == ['url1']
        mock_insert_grabbed_data.assert_not_called()


def test_run_scenario_product_save_error(mock_supplier, mock_product_fields):
    """Checks behavior when Product initialization or saving fails."""
    scenario = {'url': 'test_url', 'product_fields': {}}
    mock_supplier.related_modules.get_list_products_in_category.return_value = ['url1']
    mock_supplier.related_modules.grab_page.return_value = mock_product_fields
    
    with patch("src.scenario.executor.Product", side_effect=Exception("Product init error")) as mock_product:
      assert run_scenario(mock_supplier, scenario, "test_scenario") == ['url1']
      mock_product.assert_called()

# Tests for insert_grabbed_data
def test_insert_grabbed_data_success(mock_product_fields):
    """Checks if insert_grabbed_data calls execute_PrestaShop_insert with correct data."""
    with patch("src.scenario.executor.execute_PrestaShop_insert") as mock_execute_presta:
        insert_grabbed_data(mock_product_fields)
        mock_execute_presta.assert_called_once_with(mock_product_fields)

# Tests for execute_PrestaShop_insert
def test_execute_PrestaShop_insert_success(mock_product_fields):
    """Checks correct behavior when PrestaShop insertion is successful."""
    with patch("src.scenario.executor.PrestaShop") as mock_presta_class:
         mock_presta = MagicMock()
         mock_presta_class.return_value = mock_presta
         mock_presta.post_product_data.return_value = True

         assert execute_PrestaShop_insert(mock_product_fields, "TEST_COUPON", "2024-01-01", "2024-01-31") == True
         mock_presta.post_product_data.assert_called_once_with(
          product_id=mock_product_fields.product_id,
          product_name=mock_product_fields.product_name,
          product_category=mock_product_fields.product_category,
          product_price=mock_product_fields.product_price,
          description=mock_product_fields.description,
          coupon_code="TEST_COUPON",
          start_date="2024-01-01",
          end_date="2024-01-31"
          )

def test_execute_PrestaShop_insert_failure(mock_product_fields):
    """Checks behavior when PrestaShop insertion fails."""
    with patch("src.scenario.executor.PrestaShop") as mock_presta_class:
         mock_presta = MagicMock()
         mock_presta_class.return_value = mock_presta
         mock_presta.post_product_data.side_effect = Exception("Prestashop Error")

         assert execute_PrestaShop_insert(mock_product_fields) == False
         mock_presta.post_product_data.assert_called_once()
```