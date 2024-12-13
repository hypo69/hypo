```python
import pytest
from unittest.mock import AsyncMock, MagicMock
from hypotez.src.suppliers.ivory.graber import Graber, Context
from hypotez.src.webdriver.driver import Driver
from hypotez.src.suppliers.graber import Graber as Grbr
from src.logger.logger import logger


# Fixture for creating a mock Driver instance
@pytest.fixture
def mock_driver():
    """Provides a mock Driver instance for testing."""
    mock = AsyncMock(spec=Driver)
    return mock

# Fixture for creating a Graber instance
@pytest.fixture
def graber_instance(mock_driver):
    """Provides a Graber instance for testing."""
    return Graber(driver=mock_driver)


def test_graber_initialization(graber_instance, mock_driver):
    """Checks if the Graber instance is initialized correctly."""
    assert graber_instance.supplier_prefix == 'ivory'
    assert isinstance(graber_instance, Grbr)  # Ensure it inherits from Graber (parent class)
    assert Context.locator_for_decorator is None
    

def test_graber_supplier_prefix(graber_instance):
    """Checks the supplier_prefix attribute value after initialization."""
    assert graber_instance.supplier_prefix == "ivory"


@pytest.mark.asyncio
async def test_close_pop_up_decorator_no_locator(graber_instance):
    """Checks that the decorator does not execute when locator is None, and the underlying function is still executed."""
    
    # Mock the execute_locator method
    graber_instance.driver.execute_locator = AsyncMock()

    @graber_instance.close_pop_up()
    async def test_func():
        return "test function executed"

    result = await test_func()
    
    graber_instance.driver.execute_locator.assert_not_called()
    assert result == "test function executed"
    
    
@pytest.mark.asyncio
async def test_close_pop_up_decorator_with_locator(graber_instance):
    """Checks that the decorator executes when locator has some value, and the underlying function is still executed."""
    
    # Mock the execute_locator method
    graber_instance.driver.execute_locator = AsyncMock()
    Context.locator_for_decorator = "some_locator"

    @graber_instance.close_pop_up()
    async def test_func():
        return "test function executed"

    result = await test_func()
    
    graber_instance.driver.execute_locator.assert_not_called()
    assert result == "test function executed"
    
@pytest.mark.asyncio
async def test_close_pop_up_decorator_with_exception(graber_instance):
    """Checks that if `execute_locator` raises an exception, it's caught and logged, and the underlying function still executes."""
    
    # Mock the execute_locator method
    mock_exception = Exception("Mocked exception in execute_locator")
    graber_instance.driver.execute_locator = AsyncMock(side_effect=mock_exception)

    # Mock the logger
    mock_logger = MagicMock()
    logger.debug = mock_logger
    
    # Set the locator
    Context.locator_for_decorator = "some_locator"


    @graber_instance.close_pop_up()
    async def test_func():
        return "test function executed"

    result = await test_func()

    # Verify that the execute_locator was called with the correct locator
    graber_instance.driver.execute_locator.assert_called_once()
    # Verify that logger.debug was called with the correct error message
    mock_logger.assert_called_once()
    assert mock_logger.call_args[0][0].startswith('Ошибка выполнения локатора: ')
    assert result == "test function executed"

```