```python
import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from src.suppliers.amazon.graber import Graber, Context
from src.webdriver.driver import Driver
from src.logger.logger import logger
from src.webdriver.exceptions import ExecuteLocatorException
from typing import Callable

# Fixture for a mock driver
@pytest.fixture
def mock_driver():
    mock_driver = AsyncMock(spec=Driver)
    return mock_driver

# Fixture for a mock logger
@pytest.fixture
def mock_logger():
    mock_logger = MagicMock(spec=logger)
    return mock_logger

@pytest.mark.asyncio
async def test_graber_initialization(mock_driver):
    """
    Test the initialization of the Graber class.
    Verifies that the supplier prefix is set correctly and the parent class is initialized.
    Also checks if Context.locator_for_decorator is initialized to None.
    """
    graber = Graber(driver=mock_driver)
    assert graber.supplier_prefix == 'amazon'
    assert graber.driver == mock_driver
    assert Context.locator_for_decorator is None

@pytest.mark.asyncio
async def test_close_pop_up_decorator_no_exception(mock_logger,mock_driver):
    """
    Test the close_pop_up decorator with no exceptions raised during locator execution.
     Verifies that the wrapped function executes correctly.
    """
    # Mock the close_pop_up function
    @close_pop_up(value="test")
    async def mock_func(a, b):
        return a + b
    
    # Execute the decorated function
    result = await mock_func(1, 2)
    # Assert that the wrapped function was executed and returned the result
    assert result == 3

@pytest.mark.asyncio
async def test_close_pop_up_decorator_with_exception(mock_logger,mock_driver):
    """
    Test the close_pop_up decorator when an ExecuteLocatorException is raised.
    Verifies that the exception is caught and logged, and the wrapped function still executes.
    """
    # Mock driver to raise ExecuteLocatorException
    mock_driver.execute_locator = AsyncMock(side_effect=ExecuteLocatorException("Locator execution failed"))

    @close_pop_up()
    async def mock_func(a, b):
       return a + b

    result = await mock_func(1,2)
    assert result == 3
    # Assert that the debug message was logged
    mock_logger.debug.assert_called()

@pytest.mark.asyncio
async def test_close_pop_up_decorator_with_locator(mock_driver, mock_logger):
    """
    Test the close_pop_up decorator when a locator is set in Context.
    Checks if the locator is executed by the driver before calling the wrapped function.
    """

    # Set a mock locator in Context
    Context.locator = MagicMock()
    Context.locator.close_pop_up = MagicMock()
    Context.driver = mock_driver
    
    @close_pop_up()
    async def mock_func(a, b):
        return a + b
    
    result = await mock_func(1, 2)
    
    # Assert that driver execute_locator was called
    mock_driver.execute_locator.assert_called_once()
    assert result == 3

@pytest.mark.asyncio
async def test_close_pop_up_decorator_no_locator(mock_driver, mock_logger):
    """
    Test the close_pop_up decorator when no locator is set in Context.
    Verifies that the wrapped function still executes correctly without calling execute_locator.
    """
    # Ensure Context.locator is None
    Context.locator = None
    Context.driver = mock_driver

    @close_pop_up()
    async def mock_func(a, b):
        return a + b

    result = await mock_func(1,2)

    # Assert that driver.execute_locator was not called
    mock_driver.execute_locator.assert_not_called()
    assert result == 3
```