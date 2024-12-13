```python
import pytest
from unittest.mock import MagicMock
from src.suppliers.visualdg.graber import Graber
from src.webdriver.driver import Driver
from src.suppliers.graber import Context, ExecuteLocatorException
from typing import Callable
from functools import wraps

# Fixture for creating a mock Driver object
@pytest.fixture
def mock_driver():
    """Provides a mock Driver object for testing."""
    return MagicMock(spec=Driver)

# Fixture for a basic Graber instance
@pytest.fixture
def basic_graber_instance(mock_driver):
    """Provides a basic Graber instance for testing."""
    return Graber(driver=mock_driver)

# Mock for the close_pop_up decorator
def close_pop_up(value: any = None) -> Callable:
    """Mock decorator for testing purposes."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        async def wrapper(*args, **kwargs):
            try:
                if Context.locator_for_decorator:
                    await Context.driver.execute_locator(Context.locator_for_decorator)
            except ExecuteLocatorException as e:
                print(f'Ошибка выполнения локатора: {e}')
            return await func(*args, **kwargs)
        return wrapper
    return decorator

# Tests for Graber class initialization
def test_graber_initialization(mock_driver):
    """Tests the correct initialization of the Graber class."""
    graber = Graber(driver=mock_driver)
    assert graber.supplier_prefix == 'visualdg'
    assert graber.driver == mock_driver
    assert Context.locator_for_decorator is None

# Test case for decorator execution
@pytest.mark.asyncio
async def test_graber_decorator_execution(mock_driver, basic_graber_instance):
    """Tests that decorator executes if `Context.locator_for_decorator` is set."""
    
    mock_locator = MagicMock()
    Context.locator_for_decorator = mock_locator
    Context.driver = mock_driver

    @close_pop_up()
    async def test_function():
         return 'test_function_result'

    result = await test_function()

    mock_driver.execute_locator.assert_called_once_with(mock_locator)
    assert result == 'test_function_result'
    Context.locator_for_decorator = None

# Test case for decorator not executing when no locator provided
@pytest.mark.asyncio
async def test_graber_no_decorator_execution(mock_driver, basic_graber_instance):
    """Tests that the decorator does not execute if no locator is provided."""
    
    Context.driver = mock_driver
    
    @close_pop_up()
    async def test_function():
         return 'test_function_result'

    result = await test_function()
    mock_driver.execute_locator.assert_not_called()
    assert result == 'test_function_result'

# Test case for decorator catching the exception
@pytest.mark.asyncio
async def test_graber_decorator_exception(mock_driver, basic_graber_instance, capsys):
    """Tests that the decorator catches the ExecuteLocatorException."""
    
    mock_locator = MagicMock(side_effect=ExecuteLocatorException("Test exception"))
    Context.locator_for_decorator = mock_locator
    Context.driver = mock_driver

    @close_pop_up()
    async def test_function():
         return 'test_function_result'

    result = await test_function()
    captured = capsys.readouterr()
    assert "Ошибка выполнения локатора: Test exception" in captured.out
    assert result == 'test_function_result'
    Context.locator_for_decorator = None

# Test case if Context.locator_for_decorator is None
@pytest.mark.asyncio
async def test_graber_locator_none_no_exception(mock_driver, basic_graber_instance):
    """Tests behavior when Context.locator_for_decorator is None."""
    
    Context.driver = mock_driver
    Context.locator_for_decorator = None
    @close_pop_up()
    async def test_function():
        return 'test_function_result'
    
    result = await test_function()
    mock_driver.execute_locator.assert_not_called()
    assert result == 'test_function_result'
    Context.locator_for_decorator = None
```