```python
import pytest
from unittest.mock import MagicMock
from src.suppliers.wallashop.graber import Graber, Context
from src.webdriver.driver import Driver
from src.webdriver.exceptions import ExecuteLocatorException


@pytest.fixture
def mock_driver():
    """Provides a mock driver object."""
    driver = MagicMock(spec=Driver)
    driver.execute_locator = MagicMock()
    return driver


def test_graber_initialization(mock_driver):
    """Checks if Graber is initialized correctly."""
    graber = Graber(driver=mock_driver)
    assert graber.supplier_prefix == 'wallashop'
    assert graber.driver == mock_driver
    assert Context.locator_for_decorator is None


def test_graber_inheritance(mock_driver):
    """Checks if Graber inherits correctly from the parent class."""
    graber = Graber(driver=mock_driver)
    assert hasattr(graber, 'get_title')
    assert hasattr(graber, 'get_price')
    assert hasattr(graber, 'get_description')
    assert hasattr(graber, 'get_images')
    assert hasattr(graber, 'get_sku')
    assert hasattr(graber, 'get_attributes')
    assert hasattr(graber, 'get_availability')
    assert hasattr(graber, 'get_barcode')
    assert hasattr(graber, 'get_category')
    assert hasattr(graber, 'get_meta')


def test_graber_default_decorator_is_none(mock_driver):
    """Checks if the default decorator is None."""
    graber = Graber(driver=mock_driver)
    assert Context.locator_for_decorator is None


# def test_close_pop_up_decorator_no_exception(mock_driver):
#     """Test that the decorator does not raise an exception when no locator is set."""
#     # Create a Graber instance with a mocked driver
#     graber = Graber(driver=mock_driver)
#     # Define a dummy function that the decorator will wrap
#     async def dummy_function(value: int):
#         return value + 1
#
#     # Apply the close_pop_up decorator with no locator provided
#     decorated_function = close_pop_up()(dummy_function)
#
#     # Call the decorated function and check if it returns correctly
#     result =  decorated_function(5)
#     assert result == 6
#
#
# def test_close_pop_up_decorator_with_exception(mock_driver):
#     """Test that the decorator handles exceptions when the locator is set but fails."""
#     # Create a Graber instance with a mocked driver
#     graber = Graber(driver=mock_driver)
#
#     # Set a mock locator in Context, which should raise an exception when executed
#     Context.locator_for_decorator = MagicMock()
#     Context.driver.execute_locator.side_effect = ExecuteLocatorException("Test exception")
#
#     async def dummy_function_with_locator(value: int):
#          return value + 1
#     # Apply the close_pop_up decorator with a failing locator
#     decorated_function = close_pop_up()(dummy_function_with_locator)
#
#     # Call the decorated function and check if it returns correctly
#     result =  decorated_function(5)
#     assert result == 6
#
#     # Check if the execute_locator was called and the exception was handled
#     Context.driver.execute_locator.assert_called_once()
#     assert Context.locator_for_decorator is not None
#
#
# def test_close_pop_up_decorator_with_locator(mock_driver):
#     """Test that the decorator handles a locator execution if one is set"""
#     # Create a Graber instance with a mocked driver
#     graber = Graber(driver=mock_driver)
#
#     # Set a mock locator in Context
#     Context.locator_for_decorator = MagicMock()
#
#     async def dummy_function_with_locator(value: int):
#          return value + 1
#     # Apply the close_pop_up decorator with a passing locator
#     decorated_function = close_pop_up()(dummy_function_with_locator)
#
#     # Call the decorated function and check if it returns correctly
#     result = decorated_function(5)
#     assert result == 6
#
#     # Check if the execute_locator was called
#     Context.driver.execute_locator.assert_called_once()
#     assert Context.locator_for_decorator is not None

#TODO: add tests for decorated function of the main functions

```