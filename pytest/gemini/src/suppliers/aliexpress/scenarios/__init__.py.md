```python
import pytest

# No fixtures are needed for this module as it only contains imports and a constant.

def test_mode_is_dev():
    """
    Checks if the MODE constant is set to 'dev'.
    This test verifies the default development mode.
    """
    from hypotez.src.suppliers.aliexpress.scenarios import MODE
    assert MODE == 'dev', "MODE should be set to 'dev' by default."

def test_login_import():
    """
    Checks if the login module is imported successfully.
    This test ensures that the login module is available in the scenarios package.
    """
    try:
        from hypotez.src.suppliers.aliexpress.scenarios import login
    except ImportError:
        pytest.fail("Failed to import the login module. Ensure login.py exists in the same directory.")
```