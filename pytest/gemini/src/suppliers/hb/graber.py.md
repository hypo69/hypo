```python
import pytest
from unittest.mock import MagicMock
from src.suppliers.hb.graber import Graber, Context
from src.webdriver.driver import Driver
from src.webdriver.exceptions import ExecuteLocatorException


@pytest.fixture
def mock_driver():
    """Provides a mock Driver object."""
    driver_mock = MagicMock(spec=Driver)
    return driver_mock

@pytest.fixture
def graber_instance(mock_driver):
    """Provides a Graber instance with a mock driver."""
    return Graber(mock_driver)


def test_graber_initialization(graber_instance, mock_driver):
    """Checks that Graber is initialized correctly."""
    assert graber_instance.supplier_prefix == 'hb'
    assert graber_instance.driver == mock_driver
    assert Context.locator_for_decorator is None #default value in the constructor


def test_close_pop_up_decorator_no_exception(mocker, graber_instance):
    """Tests the close_pop_up decorator when no exception occurs during locator execution."""
    # Mock the async execute_locator to not raise an exception
    mock_execute_locator = mocker.patch.object(Context.driver, 'execute_locator', new_callable=mocker.AsyncMock)
    
    @graber_instance.close_pop_up()
    async def test_function():
        return "test_result"

    result = test_function()
    
    #Assert mock method call in decorator
    mock_execute_locator.assert_not_called()
    assert result == "test_result"



def test_close_pop_up_decorator_with_exception(mocker, graber_instance):
    """Tests the close_pop_up decorator when an ExecuteLocatorException occurs."""
    # Mock the async execute_locator to raise an ExecuteLocatorException
    mock_execute_locator = mocker.patch.object(Context.driver, 'execute_locator', side_effect=ExecuteLocatorException("Test Error"), new_callable=mocker.AsyncMock)
    
    @graber_instance.close_pop_up()
    async def test_function():
        return "test_result"

    result = test_function()
    
    #Assert mock method call in decorator
    mock_execute_locator.assert_not_called()
    assert result == "test_result"

def test_close_pop_up_decorator_with_locator(mocker, graber_instance):
    """Tests the close_pop_up decorator when an ExecuteLocatorException occurs."""
    # Mock the async execute_locator to raise an ExecuteLocatorException
    mock_execute_locator = mocker.patch.object(Context.driver, 'execute_locator', new_callable=mocker.AsyncMock)
    
    
    Context.locator_for_decorator  = 'close_pop_up'

    @graber_instance.close_pop_up()
    async def test_function():
        return "test_result"

    result = test_function()
    
    #Assert mock method call in decorator
    mock_execute_locator.assert_not_called()
    assert result == "test_result"
    Context.locator_for_decorator  = None
```