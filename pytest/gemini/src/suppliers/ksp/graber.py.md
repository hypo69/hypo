```python
import pytest
from unittest.mock import MagicMock, AsyncMock
from src.suppliers.ksp.graber import Graber, Context
from src.webdriver.driver import Driver
from src.utils.jjson import j_loads_ns
from src import gs
from src.logger.logger import logger
from src.webdriver.exceptions import ExecuteLocatorException
import asyncio
from functools import wraps
from typing import Any, Callable

@pytest.fixture
def mock_driver():
    """Provides a mock driver object."""
    driver = MagicMock(spec=Driver)
    driver.current_url = "https://example.com/product"
    driver.execute_locator = AsyncMock()
    return driver


@pytest.fixture
def mock_mobile_driver():
    """Provides a mock driver object for mobile site."""
    driver = MagicMock(spec=Driver)
    driver.current_url = "https://example.com/mob/product"
    driver.execute_locator = AsyncMock()
    return driver


def test_graber_initialization_desktop(mock_driver):
    """Checks initialization for desktop site."""
    graber = Graber(mock_driver)
    assert graber.supplier_prefix == "ksp"
    assert hasattr(graber, 'locator')
    assert Context.locator_for_decorator is None
    mock_driver.assert_not_called()


def test_graber_initialization_mobile(mock_mobile_driver):
    """Checks initialization for mobile site."""
    graber = Graber(mock_mobile_driver)
    assert graber.supplier_prefix == "ksp"
    assert hasattr(graber, 'locator')
    assert Context.locator_for_decorator is None
    mock_mobile_driver.assert_not_called()


def test_graber_initialization_mobile_locator_loaded(mock_mobile_driver, monkeypatch):
    """Checks if mobile locators are loaded correctly when the mobile URL is detected"""
    mock_j_loads_ns = MagicMock(return_value={"some": "locator"})
    monkeypatch.setattr("src.suppliers.ksp.graber.j_loads_ns", mock_j_loads_ns)

    graber = Graber(mock_mobile_driver)
    
    mock_j_loads_ns.assert_called_once_with(gs.path.src / 'suppliers' / 'ksp' / 'locators' / 'product_mobile_site.json')
    assert graber.locator == {"some": "locator"}


def test_graber_initialization_desktop_locator_not_loaded(mock_driver, monkeypatch):
    """Checks that no mobile locators are loaded for the desktop site"""
    mock_j_loads_ns = MagicMock(return_value={"some": "locator"})
    monkeypatch.setattr("src.suppliers.ksp.graber.j_loads_ns", mock_j_loads_ns)

    graber = Graber(mock_driver)

    mock_j_loads_ns.assert_not_called()
    assert hasattr(graber, 'locator')


def test_close_pop_up_decorator_template_execute_locator_success(mock_driver, monkeypatch):
    """Checks that the decorator executes the locator and the wrapped function."""

    def close_pop_up(value: Any = None) -> Callable:
        """Создает декоратор для закрытия всплывающих окон перед выполнением основной логики функции."""
        def decorator(func: Callable) -> Callable:
            @wraps(func)
            async def wrapper(*args, **kwargs):
                try:
                    await Context.driver.execute_locator(Context.locator.close_pop_up)  # Await async pop-up close  
                except ExecuteLocatorException as e:
                    logger.debug(f'Ошибка выполнения локатора: {e}')
                return await func(*args, **kwargs)  # Await the main function
            return wrapper
        return decorator

    Context.driver = mock_driver
    Context.locator = MagicMock()
    Context.locator.close_pop_up = "some_locator"

    @close_pop_up()
    async def some_function(a, b):
        return a + b

    async def run_test():
        result = await some_function(3, 4)
        assert result == 7
        mock_driver.execute_locator.assert_called_once_with("some_locator")
    
    asyncio.run(run_test())


def test_close_pop_up_decorator_template_execute_locator_fail(mock_driver, monkeypatch):
    """Checks that the decorator handles locator exceptions."""

    def close_pop_up(value: Any = None) -> Callable:
        """Создает декоратор для закрытия всплывающих окон перед выполнением основной логики функции."""
        def decorator(func: Callable) -> Callable:
            @wraps(func)
            async def wrapper(*args, **kwargs):
                try:
                    await Context.driver.execute_locator(Context.locator.close_pop_up)  # Await async pop-up close  
                except ExecuteLocatorException as e:
                   logger.debug(f'Ошибка выполнения локатора: {e}')
                return await func(*args, **kwargs)  # Await the main function
            return wrapper
        return decorator

    Context.driver = mock_driver
    Context.locator = MagicMock()
    Context.locator.close_pop_up = "some_locator"
    mock_driver.execute_locator.side_effect = ExecuteLocatorException("Locator error")

    @close_pop_up()
    async def some_function(a, b):
        return a + b

    async def run_test():
        result = await some_function(3, 4)
        assert result == 7
        mock_driver.execute_locator.assert_called_once_with("some_locator")
    
    asyncio.run(run_test())
```