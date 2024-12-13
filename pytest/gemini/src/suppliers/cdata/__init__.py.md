```python
import pytest

from hypotez.src.suppliers.cdata import MODE, Graber  # Import from your module


def test_mode_is_dev():
    """
    Test that the MODE variable is set to 'dev'.
    """
    assert MODE == 'dev'


def test_graber_importable():
    """
    Test that the Graber class can be imported.
    """
    assert Graber is not None
    # You might add more checks, like if you can create an instance of Graber
    # For example: 
    # graber = Graber()
    # assert isinstance(graber, Graber)

```