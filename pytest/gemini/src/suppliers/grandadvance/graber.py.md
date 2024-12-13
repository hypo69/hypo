```python
import pytest
from typing import Any, Callable
from unittest.mock import MagicMock
from src.suppliers.grandadvance.graber import Graber, Context
from src.webdriver.driver import Driver
from src.webdriver.exceptions import ExecuteLocatorException
from src.logger.logger import logger  # Assume logger is correctly set up elsewhere


@pytest.fixture
def mock_driver():
    """Provides a mock Driver object for testing."""
    driver_mock = MagicMock(spec=Driver)
    return driver_mock


class TestGraber:
    """Tests for the Graber class."""

    def test_graber_initialization(self, mock_driver):
        """Checks correct initialization of Graber class."""
        graber = Graber(mock_driver)
        assert graber.supplier_prefix == 'grandadvance'
        assert graber.driver == mock_driver
        assert Context.locator_for_decorator is None

    def test_close_pop_up_decorator_no_exception(self, mock_driver):
        """
        Test if decorator works correctly without any exception from execute_locator.
        This test case is checking the decorator, even if it is commented in the original code.
        """
        
        def close_pop_up(value: Any = None) -> Callable:
            """Mock close_pop_up decorator."""
            def decorator(func: Callable) -> Callable:
                async def wrapper(*args, **kwargs):
                    try:
                        # Simulate successful locator execution
                        await Context.driver.execute_locator(Context.locator.close_pop_up)  
                    except ExecuteLocatorException as e:
                        logger.debug(f'Ошибка выполнения локатора: {e}')
                    return await func(*args, **kwargs)
                return wrapper
            return decorator

        @close_pop_up()
        async def test_func():
            return "Test function called"
        
        Context.driver = mock_driver
        Context.locator = MagicMock()
        Context.locator.close_pop_up = "some_locator"  
        mock_driver.execute_locator.return_value = None
        
        result =  test_func()
        
        assert result == "Test function called"
        mock_driver.execute_locator.assert_called_once_with("some_locator")


    def test_close_pop_up_decorator_with_exception(self, mock_driver, caplog):
       """
       Test if decorator correctly handles exceptions during execute_locator.
       This test case is checking the decorator, even if it is commented in the original code.
       """
       
       def close_pop_up(value: Any = None) -> Callable:
            """Mock close_pop_up decorator."""
            def decorator(func: Callable) -> Callable:
                async def wrapper(*args, **kwargs):
                    try:
                        # Simulate exception during locator execution
                        await Context.driver.execute_locator(Context.locator.close_pop_up)  
                    except ExecuteLocatorException as e:
                        logger.debug(f'Ошибка выполнения локатора: {e}')
                    return await func(*args, **kwargs)
                return wrapper
            return decorator

       @close_pop_up()
       async def test_func():
            return "Test function called"

       Context.driver = mock_driver
       Context.locator = MagicMock()
       Context.locator.close_pop_up = "some_locator"  
       mock_driver.execute_locator.side_effect = ExecuteLocatorException("Test Exception")
       
       result = test_func()
       
       assert result == "Test function called"
       mock_driver.execute_locator.assert_called_once_with("some_locator")
       assert "Ошибка выполнения локатора: Test Exception" in caplog.text  
```