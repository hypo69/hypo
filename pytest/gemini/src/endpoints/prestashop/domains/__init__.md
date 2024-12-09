```python
import pytest

# Tests for the __init__.py file (which only defines a constant)
def test_mode_value():
    """Checks the value of the MODE constant."""
    from hypotez.src.endpoints.prestashop.domains import MODE
    assert MODE == 'dev'
```