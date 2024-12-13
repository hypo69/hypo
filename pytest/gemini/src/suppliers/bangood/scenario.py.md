```python
import pytest
from unittest.mock import MagicMock
from src.suppliers.bangood.scenario import get_list_products_in_category, get_list_categories_from_site
from src.logger.logger import logger

# Mock the logger to prevent printing during tests
logger.info = MagicMock()
logger.warning = MagicMock()
logger.error = MagicMock()

@pytest.fixture
def mock_supplier():
    """Provides a mock Supplier object for testing."""
    supplier_mock = MagicMock()
    supplier_mock.driver = MagicMock()
    supplier_mock.locators = {
        'category': {
            'product_links': 'locator_for_product_links'
        },
        'product': {
            'close_banner': 'locator_for_close_banner'
        }
    }
    return supplier_mock


def test_get_list_products_in_category_valid_links(mock_supplier):
    """Checks correct behavior with valid product links."""
    mock_supplier.driver.execute_locator.return_value = ["url1", "url2"]
    result = get_list_products_in_category(mock_supplier)
    assert result == ["url1", "url2"]
    mock_supplier.driver.execute_locator.assert_called_with('locator_for_product_links')
    logger.info.assert_called()  # Ensure info log was called


def test_get_list_products_in_category_single_link(mock_supplier):
    """Checks correct behavior with a single product link returned as a string."""
    mock_supplier.driver.execute_locator.return_value = "url1"
    result = get_list_products_in_category(mock_supplier)
    assert result == ["url1"]
    mock_supplier.driver.execute_locator.assert_called_with('locator_for_product_links')
    logger.info.assert_called()


def test_get_list_products_in_category_no_links(mock_supplier):
    """Checks behavior when no product links are found."""
    mock_supplier.driver.execute_locator.return_value = None
    result = get_list_products_in_category(mock_supplier)
    assert result is None
    logger.warning.assert_called_with('Нет ссылок на товары. Так бывает')
    

def test_get_list_products_in_category_no_locators(mock_supplier):
     """Checks behavior when no category locators are provided."""
     mock_supplier.locators['category'] = None
     result = get_list_products_in_category(mock_supplier)
     assert result is None
     logger.error.assert_called()

def test_get_list_products_in_category_empty_locators(mock_supplier):
     """Checks behavior when empty category locators are provided."""
     mock_supplier.locators['category'] = {}
     result = get_list_products_in_category(mock_supplier)
     assert result is None
     logger.error.assert_called()
     
def test_get_list_products_in_category_close_banner_called(mock_supplier):
    """Checks if close banner is called correctly."""
    mock_supplier.driver.execute_locator.return_value = []
    get_list_products_in_category(mock_supplier)
    mock_supplier.driver.execute_locator.assert_any_call('locator_for_close_banner')
    
def test_get_list_products_in_category_scroll_called(mock_supplier):
    """Checks if scroll method is called."""
    mock_supplier.driver.execute_locator.return_value = []
    get_list_products_in_category(mock_supplier)
    mock_supplier.driver.scroll.assert_called()


def test_get_list_categories_from_site_not_implemented():
    """Checks that get_list_categories_from_site is not implemented."""
    with pytest.raises(NotImplementedError):
        get_list_categories_from_site(None)
```