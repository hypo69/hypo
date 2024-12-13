```python
import pytest
from unittest.mock import MagicMock
from src.suppliers.etzmaleh.graber import Graber
from src.webdriver.driver import Driver
from src.suppliers.graber import Context, Graber as Grbr
from src.webdriver.exceptions import ExecuteLocatorException
from typing import Any, Callable
from functools import wraps

# Mock the logger
class MockLogger:
    def debug(self, message):
        pass  # Do nothing for debug messages

# Replace the original logger with the mock logger
import src.logger.logger
src.logger.logger.logger = MockLogger()



@pytest.fixture
def mock_driver():
    """Provides a mock Driver object."""
    driver_mock = MagicMock(spec=Driver)
    driver_mock.execute_locator = MagicMock()
    return driver_mock

@pytest.fixture
def graber_instance(mock_driver):
    """Provides a Graber instance with a mock Driver."""
    return Graber(driver=mock_driver)

# Mock the base class's __init__
def mock_grbr_init(self, supplier_prefix, driver):
    self.supplier_prefix = supplier_prefix
    self.driver = driver
    self.log = MockLogger()
    self.is_test = False
    self.response_queue = []
    self.current_page_url = ""


Grbr.__init__ = mock_grbr_init # Apply the mock to the Graber base class


def test_graber_initialization(mock_driver):
    """Checks if the Graber class initializes correctly."""
    graber = Graber(driver=mock_driver)
    assert graber.supplier_prefix == 'etzmaleh'
    assert graber.driver == mock_driver
    assert Context.locator_for_decorator is None

# Test that the decorator doesn't cause exceptions
def test_close_pop_up_no_exception(mock_driver, graber_instance):
    """Check that the decorator does not raise exceptions if ExecuteLocatorException is catched."""
    @close_pop_up()
    async def mock_function():
        return "Function result"
    
    mock_driver.execute_locator.side_effect = ExecuteLocatorException("Test Exception")
    result =  mock_function()
    assert result == "Function result"

def test_close_pop_up_no_locator(mock_driver, graber_instance):
      """Check that decorator does not execute locator if not provided."""
      @close_pop_up()
      async def mock_function():
            return "Function result"
      
      result =  mock_function()
      mock_driver.execute_locator.assert_not_called()
      assert result == "Function result"



def test_graber_supplier_prefix(graber_instance):
    """Checks if the supplier prefix is set correctly."""
    assert graber_instance.supplier_prefix == 'etzmaleh'

def test_context_locator_for_decorator_is_none(graber_instance):
    """Checks if the locator for the decorator is None after initialization."""
    assert Context.locator_for_decorator is None

# Mock the close_pop_up decorator function to be able to test decorator functionality

def close_pop_up(value: Any = None) -> Callable:
    """Creates a decorator to simulate closing pop-ups."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        async def wrapper(*args, **kwargs):
            try:
                 if Context.locator_for_decorator:
                      await Context.driver.execute_locator(Context.locator_for_decorator)
            except ExecuteLocatorException as e:
                src.logger.logger.logger.debug(f'Ошибка выполнения локатора: {e}')
            return await func(*args, **kwargs)
        return wrapper
    return decorator
```