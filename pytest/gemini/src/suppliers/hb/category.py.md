```python
import pytest
from unittest.mock import MagicMock
from src.suppliers.hb.category import get_list_products_in_category, paginator
from src.webdriver.driver import Driver
from src.suppliers import Supplier


# Fixture for creating a mock Supplier object
@pytest.fixture
def mock_supplier():
    """Provides a mock Supplier object for testing."""
    supplier = MagicMock(spec=Supplier)
    supplier.driver = MagicMock(spec=Driver)
    supplier.locators = {
        'category': {
            'product_links': 'product_links_locator',
            'pagination': {
                '<-': 'pagination_locator'
            }
        },
        'product': {
            'close_banner': 'close_banner_locator'
        }
    }
    supplier.current_scenario = {'name': 'test_category'}
    return supplier


# Tests for get_list_products_in_category
def test_get_list_products_in_category_no_products(mock_supplier):
    """Checks behavior when no product links are found."""
    mock_supplier.driver.execute_locator.return_value = None
    result = get_list_products_in_category(mock_supplier)
    assert result is None
    mock_supplier.driver.execute_locator.assert_called_with('product_links_locator')


def test_get_list_products_in_category_single_page(mock_supplier):
    """Checks behavior when product links are found on a single page."""
    mock_supplier.driver.execute_locator.return_value = ['product1', 'product2']
    result = get_list_products_in_category(mock_supplier)
    assert result == ['product1', 'product2']
    mock_supplier.driver.execute_locator.assert_called_with('product_links_locator')


def test_get_list_products_in_category_multiple_pages(mock_supplier):
    """Checks behavior when products span multiple pages."""
    mock_supplier.driver.execute_locator.side_effect = [
        ['product1', 'product2'],  # Initial product links
        True,  # First pagination response
        ['product3', 'product4'],
        False # Second pagination response
    ]
    mock_supplier.driver.current_url = "url2"
    mock_supplier.driver.previous_url = "url1"
    
    result = get_list_products_in_category(mock_supplier)
    assert len(result) == 2
    assert result[0] == ['product1', 'product2']
    assert result[1] == ['product3', 'product4']
    
    mock_supplier.driver.execute_locator.assert_any_call('product_links_locator')


def test_get_list_products_in_category_string_product_links(mock_supplier):
    """Checks behavior when product links are returned as a single string."""
    mock_supplier.driver.execute_locator.return_value = 'product1'
    result = get_list_products_in_category(mock_supplier)
    assert isinstance(result, list)
    assert result == ['product1']
    mock_supplier.driver.execute_locator.assert_called_with('product_links_locator')



# Tests for paginator
def test_paginator_next_page_exists(mock_supplier):
    """Checks paginator returns True if next page button exists."""
    mock_supplier.driver.execute_locator.return_value = 'button_element'
    locator = mock_supplier.locators['category']['pagination']
    result = paginator(mock_supplier.driver, locator, [])
    assert result is True
    mock_supplier.driver.execute_locator.assert_called_with('pagination_locator')


def test_paginator_next_page_not_exists(mock_supplier):
    """Checks paginator returns None if next page button doesn't exist."""
    mock_supplier.driver.execute_locator.return_value = None
    locator = mock_supplier.locators['category']['pagination']
    result = paginator(mock_supplier.driver, locator, [])
    assert result is None
    mock_supplier.driver.execute_locator.assert_called_with('pagination_locator')


def test_paginator_next_page_empty_list(mock_supplier):
    """Checks paginator returns None if next page button returns empty list."""
    mock_supplier.driver.execute_locator.return_value = []
    locator = mock_supplier.locators['category']['pagination']
    result = paginator(mock_supplier.driver, locator, [])
    assert result is None
    mock_supplier.driver.execute_locator.assert_called_with('pagination_locator')
```