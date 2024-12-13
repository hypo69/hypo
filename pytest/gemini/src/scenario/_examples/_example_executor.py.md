```python
import pytest
from pathlib import Path
from unittest.mock import MagicMock, patch
from hypotez.src.scenario._examples._example_executor import (
    run_scenario_files,
    run_scenario_file,
    run_scenario,
    insert_grabbed_data,
    add_coupon,
    execute_PrestaShop_insert_async,
    execute_PrestaShop_insert,
    MockSupplier,
    MockRelatedModules,
    MockDriver
)
from hypotez.src.product.product_fields import ProductFields
from hypotez.src.endpoints.PrestaShop import PrestaShop  # Assuming this import is correct for your environment
import asyncio

# Fixtures
@pytest.fixture
def mock_supplier():
    """Provides a mock Supplier object for testing."""
    return MockSupplier()

@pytest.fixture
def mock_related_modules():
    """Provides a mock RelatedModules object for testing."""
    return MockRelatedModules()

@pytest.fixture
def mock_driver():
    """Provides a mock Driver object for testing."""
    return MockDriver()

@pytest.fixture
def example_product_fields():
    """Provides example ProductFields object for testing."""
    return ProductFields(
        presta_fields_dict={'reference': 'REF123', 'name': [{'id': 1, 'value': 'Sample Product'}], 'price': 100},
        assist_fields_dict={'images_urls': ['http://example.com/image1.jpg'], 'default_image_url': 'http://example.com/default_image.jpg', 'locale': 'en'}
    )

# Tests for run_scenario_files
def test_run_scenario_files_valid_input(mock_supplier):
    """Checks correct behavior when running multiple scenario files."""
    scenario_files = [Path('scenarios/scenario1.json'), Path('scenarios/scenario2.json')]
    with patch('hypotez.src.scenario._examples._example_executor.run_scenario_file', return_value=True) as mock_run_scenario_file:
        result = run_scenario_files(mock_supplier, scenario_files)
        assert result is True
        assert mock_run_scenario_file.call_count == len(scenario_files)
    
def test_run_scenario_files_empty_list(mock_supplier):
    """Checks behavior when an empty list of scenario files is provided."""
    scenario_files = []
    result = run_scenario_files(mock_supplier, scenario_files)
    assert result is True
    
def test_run_scenario_files_one_file_fails(mock_supplier):
    """Checks correct behavior when one of the scenario files fails to execute."""
    scenario_files = [Path('scenarios/scenario1.json'), Path('scenarios/scenario2.json')]
    with patch('hypotez.src.scenario._examples._example_executor.run_scenario_file', side_effect=[True, False]) as mock_run_scenario_file:
        result = run_scenario_files(mock_supplier, scenario_files)
        assert result is False
        assert mock_run_scenario_file.call_count == len(scenario_files)

# Tests for run_scenario_file
def test_run_scenario_file_valid_input(mock_supplier, mock_related_modules):
    """Checks correct behavior when a valid scenario file is provided."""
    scenario_file = Path('scenarios/scenario1.json')
    mock_supplier.related_modules = mock_related_modules
    with patch('hypotez.src.scenario._examples._example_executor.run_scenario', return_value=True) as mock_run_scenario:
       
        result = run_scenario_file(mock_supplier, scenario_file)
        assert result is True
        mock_run_scenario.assert_called_once()

def test_run_scenario_file_invalid_input(mock_supplier):
    """Checks correct behavior when an invalid scenario file is provided."""
    scenario_file = "invalid_path"
    with pytest.raises(AttributeError):
         run_scenario_file(mock_supplier, scenario_file)

def test_run_scenario_file_scenario_fails(mock_supplier, mock_related_modules):
    """Checks behavior when scenario execution fails."""
    scenario_file = Path('scenarios/scenario1.json')
    mock_supplier.related_modules = mock_related_modules
    with patch('hypotez.src.scenario._examples._example_executor.run_scenario', return_value=False) as mock_run_scenario:
        result = run_scenario_file(mock_supplier, scenario_file)
        assert result is False
        mock_run_scenario.assert_called_once()

# Tests for run_scenario
def test_run_scenario_valid_input(mock_supplier, mock_related_modules):
    """Checks correct execution of a scenario with valid input."""
    mock_supplier.related_modules = mock_related_modules
    scenario = {
        'url': 'http://example.com/category',
        'products': [{'url': 'http://example.com/product1'}, {'url': 'http://example.com/product2'}]
    }
    with patch('hypotez.src.scenario._examples._example_executor.insert_grabbed_data', return_value=True) as mock_insert_grabbed_data, \
            patch('hypotez.src.scenario._examples._example_executor.asyncio.run', return_value=True) as mock_async_run:
        result = run_scenario(mock_supplier, scenario)
        assert result is True
        assert mock_insert_grabbed_data.call_count == len(scenario['products'])
        mock_async_run.assert_called_once()

def test_run_scenario_no_products(mock_supplier):
    """Checks correct execution of a scenario with no products."""
    scenario = {'url': 'http://example.com/category', 'products': []}
    with patch('hypotez.src.scenario._examples._example_executor.insert_grabbed_data', return_value=True) as mock_insert_grabbed_data:
        result = run_scenario(mock_supplier, scenario)
        assert result is True
        mock_insert_grabbed_data.assert_not_called()


def test_run_scenario_insertion_fails(mock_supplier, mock_related_modules):
    """Checks behavior when product insertion fails."""
    mock_supplier.related_modules = mock_related_modules
    scenario = {
        'url': 'http://example.com/category',
        'products': [{'url': 'http://example.com/product1'}, {'url': 'http://example.com/product2'}]
    }
    with patch('hypotez.src.scenario._examples._example_executor.insert_grabbed_data', side_effect=[True,False]) as mock_insert_grabbed_data:
        result = run_scenario(mock_supplier, scenario)
        assert result is False
        assert mock_insert_grabbed_data.call_count == len(scenario['products'])


# Tests for insert_grabbed_data
@patch('hypotez.src.scenario._examples._example_executor.execute_PrestaShop_insert')
def test_insert_grabbed_data_valid_input(mock_execute_PrestaShop_insert, example_product_fields):
    """Checks correct behavior when inserting grabbed data."""
    insert_grabbed_data(example_product_fields)
    mock_execute_PrestaShop_insert.assert_called_once_with(example_product_fields)

def test_insert_grabbed_data_none_input():
    """Checks behavior when None input is provided."""
    with pytest.raises(AttributeError):
        insert_grabbed_data(None)

# Tests for add_coupon
@patch('hypotez.src.scenario._examples._example_executor.PrestaShop')
def test_add_coupon_valid_input(mock_prestashop):
    """Checks correct behavior when adding a coupon."""
    credentials = {'api_domain': 'https://example.com/api', 'api_key': 'YOUR_API_KEY'}
    reference = 'REF123'
    coupon_code = 'SUMMER2024'
    start_date = '2024-07-01'
    end_date = '2024-07-31'
    add_coupon(credentials, reference, coupon_code, start_date, end_date)
    mock_prestashop.assert_called_once()
    mock_prestashop.return_value.add_coupon.assert_called_once_with(reference, coupon_code, start_date, end_date)

def test_add_coupon_missing_credentials():
     """Checks behavior when credentials are missing."""
     with pytest.raises(TypeError):
        add_coupon(None, 'REF123', 'SUMMER2024', '2024-07-01', '2024-07-31')


# Tests for execute_PrestaShop_insert_async
@pytest.mark.asyncio
@patch('hypotez.src.scenario._examples._example_executor.execute_PrestaShop_insert')
async def test_execute_PrestaShop_insert_async_valid_input(mock_execute_PrestaShop_insert, example_product_fields):
    """Checks correct async behavior when inserting into PrestaShop."""
    await execute_PrestaShop_insert_async(example_product_fields)
    mock_execute_PrestaShop_insert.assert_called_once_with(example_product_fields)

@pytest.mark.asyncio
async def test_execute_PrestaShop_insert_async_none_input():
     """Checks behavior when None input is provided."""
     with pytest.raises(AttributeError):
        await execute_PrestaShop_insert_async(None)

# Tests for execute_PrestaShop_insert
@patch('hypotez.src.scenario._examples._example_executor.PrestaShop')
def test_execute_PrestaShop_insert_valid_input(mock_prestashop, example_product_fields):
    """Checks correct synchronous behavior when inserting into PrestaShop."""
    mock_prestashop.return_value.insert.return_value = True
    result = execute_PrestaShop_insert(example_product_fields)
    assert result is True
    mock_prestashop.assert_called_once()
    mock_prestashop.return_value.insert.assert_called_once_with(example_product_fields)

@patch('hypotez.src.scenario._examples._example_executor.PrestaShop')
def test_execute_PrestaShop_insert_insert_fails(mock_prestashop, example_product_fields):
    """Checks behavior when PrestaShop insert fails."""
    mock_prestashop.return_value.insert.return_value = False
    result = execute_PrestaShop_insert(example_product_fields)
    assert result is False
    mock_prestashop.assert_called_once()
    mock_prestashop.return_value.insert.assert_called_once_with(example_product_fields)

def test_execute_PrestaShop_insert_none_input():
    """Checks behavior when None input is provided."""
    with pytest.raises(AttributeError):
        execute_PrestaShop_insert(None)

# Tests for Mock Classes
def test_mock_supplier_creation():
    """Checks if mock supplier object is created successfully with all attributes."""
    supplier = MockSupplier()
    assert supplier.supplier_abs_path == Path('/path/to/scenarios')
    assert supplier.scenario_files == [Path('scenarios/scenario1.json'), Path('scenarios/scenario2.json')]
    assert supplier.current_scenario is None
    assert supplier.supplier_settings == {'runned_scenario': []}
    assert isinstance(supplier.related_modules, MockRelatedModules)
    assert isinstance(supplier.driver, MockDriver)

def test_mock_related_modules_get_list_products_in_category():
    """Checks the output of the get_list_products_in_category function in mock class."""
    modules = MockRelatedModules()
    result = modules.get_list_products_in_category("test")
    assert result == ['http://example.com/product1', 'http://example.com/product2']

def test_mock_related_modules_grab_product_page():
    """Checks the output of grab_product_page in mock class."""
    modules = MockRelatedModules()
    result = modules.grab_product_page("test")
    assert isinstance(result, ProductFields)
    assert result.presta_fields_dict == {'reference': 'REF123', 'name': [{ 'id': 1, 'value': 'Sample Product' }], 'price': 100}
    assert result.assist_fields_dict == {'images_urls': ['http://example.com/image1.jpg'], 'default_image_url': 'http://example.com/default_image.jpg', 'locale': 'en'}


@pytest.mark.asyncio
async def test_mock_related_modules_grab_page():
    """Checks the output of async grab_page in mock class."""
    modules = MockRelatedModules()
    result = await modules.grab_page("test")
    assert isinstance(result, ProductFields)
    assert result.presta_fields_dict == {'reference': 'REF123', 'name': [{ 'id': 1, 'value': 'Sample Product' }], 'price': 100}
    assert result.assist_fields_dict == {'images_urls': ['http://example.com/image1.jpg'], 'default_image_url': 'http://example.com/default_image.jpg', 'locale': 'en'}


def test_mock_driver_get_url():
     """Checks if the get_url in mock class returns True."""
     driver = MockDriver()
     result = driver.get_url('http://example.com')
     assert result == True
```