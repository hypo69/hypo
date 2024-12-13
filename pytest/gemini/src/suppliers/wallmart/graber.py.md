```python
import pytest
from unittest.mock import MagicMock
from src.suppliers.wallmart.graber import Graber
from src.webdriver.driver import Driver
from src.suppliers.graber import Context, ExecuteLocatorException


@pytest.fixture
def mock_driver():
    """Provides a mock Driver instance."""
    driver_mock = MagicMock(spec=Driver)
    return driver_mock

def test_graber_init(mock_driver):
    """Checks if Graber initializes correctly."""
    graber = Graber(driver=mock_driver)
    assert graber.supplier_prefix == "wallmart"
    assert graber.driver == mock_driver
    assert Context.locator_for_decorator is None

def test_graber_init_parent_attributes(mock_driver):
    """Checks if the parent class attributes are initialized correctly."""
    graber = Graber(driver=mock_driver)
    assert graber.supplier_prefix == 'wallmart'
    assert graber.driver == mock_driver

def test_graber_supplier_prefix_exists():
    """Checks if the supplier_prefix attribute exists and is accessible."""
    mock_driver = MagicMock(spec=Driver)
    graber = Graber(driver=mock_driver)
    assert hasattr(graber, "supplier_prefix"), "supplier_prefix attribute does not exist"
    assert isinstance(graber.supplier_prefix, str), "supplier_prefix is not a string"


def test_graber_context_locator_for_decorator_is_none(mock_driver):
    """Check if Context.locator_for_decorator is set to None."""
    graber = Graber(driver=mock_driver)
    assert Context.locator_for_decorator is None, "Context.locator_for_decorator should be None after initialization"
```