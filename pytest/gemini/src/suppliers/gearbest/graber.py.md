```python
import pytest
from unittest.mock import MagicMock
from src.suppliers.gearbest.graber import Graber, Context
from src.webdriver.driver import Driver

# Fixture for creating a mock Driver object
@pytest.fixture
def mock_driver():
    """Provides a mock Driver object."""
    return MagicMock(spec=Driver)

def test_graber_initialization(mock_driver):
    """
    Test the initialization of the Graber class.
    Checks if the supplier_prefix is set correctly and if the parent class is initialized.
    """
    graber = Graber(driver=mock_driver)
    assert graber.supplier_prefix == 'etzmaleh'
    assert graber.driver == mock_driver
    assert Context.locator_for_decorator is None

def test_graber_inherits_from_parent():
    """
    Test that the Graber class inherits from the parent class.
    Checks if the Graber class is a subclass of the parent class.
    """
    assert issubclass(Graber, Grbr)

def test_graber_prefix_is_correct(mock_driver):
      """
    Test if the supplier_prefix is set correctly.
    Check if the prefix is the expected string
      """
      graber = Graber(driver=mock_driver)
      assert graber.supplier_prefix == 'etzmaleh'
```