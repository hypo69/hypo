```python
import pytest

from hypotez.src.suppliers.gearbest import Graber, MODE


def test_module_mode_is_dev():
    """Checks if the module's MODE variable is set to 'dev'."""
    assert MODE == "dev"


def test_graber_class_exists():
    """Checks if the Graber class is defined in the module."""
    assert Graber is not None, "Graber class is not defined"

```