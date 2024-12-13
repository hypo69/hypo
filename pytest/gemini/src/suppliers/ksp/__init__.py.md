```python
import pytest

from hypotez.src.suppliers.ksp import Graber, MODE


def test_module_mode_variable():
    """Checks if the MODE variable is defined correctly"""
    assert MODE in ['dev', 'prod'], "MODE variable must be 'dev' or 'prod'"


def test_graber_class_exists():
    """Checks if the Graber class exists."""
    assert Graber, "Graber class should be defined"
    
def test_graber_class_is_callable():
    """Checks if Graber is a class (callable)"""
    assert callable(Graber), "Graber should be a class and callable"
```