```python
import pytest
from hypotez.src import credentials


def test_mode_is_dev():
    """Tests that the MODE variable is set to 'dev'."""
    assert credentials.MODE == 'dev'


def test_gs_import():
    """Tests that the gs object from credentials is importable."""
    try:
        gs = credentials.gs
        assert gs is not None
    except Exception as e:
        pytest.fail(f"Failed to import gs from credentials: {e}")


# Test for potential errors if gs is not defined in credentials.py
def test_gs_import_error_handling():
    """Tests if appropriate error is raised if gs is not defined correctly."""
    with pytest.raises(AttributeError, match="module 'credentials' has no attribute 'gs'"):
        credentials.gs  # Should raise an AttributeError
```