```python
import pytest

# Tests for the __init__.py file (which currently only defines a constant)
def test_mode_is_dev():
    """Checks if the MODE constant is set to 'dev'."""
    from hypotez.src.translators import MODE
    assert MODE == 'dev', f"Expected MODE to be 'dev', but got '{MODE}'"
```