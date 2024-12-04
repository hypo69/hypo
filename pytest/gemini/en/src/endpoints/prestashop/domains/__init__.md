```python
import pytest

# Tests for the __init__.py file, which seems to only contain constants.
# Since there are no functions or methods to test, we'll just verify the constant value.

def test_mode_value():
    """Checks the value of the MODE constant."""
    from hypotez.src.endpoints.prestashop.domains import MODE
    assert MODE == 'dev'
```