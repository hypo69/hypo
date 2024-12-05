```python
import pytest

# Tests for the iso/__init__.py file
def test_mode_is_dev():
    """Checks that the MODE variable is set to 'dev'."""
    from hypotez.src.utils.iso import MODE
    assert MODE == 'dev', f"MODE should be 'dev', but is {MODE}"
```