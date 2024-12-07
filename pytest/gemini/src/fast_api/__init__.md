```python
import pytest

# Tests for the __init__.py file
def test_mode_is_dev():
    """Checks if the MODE variable is set to 'dev'."""
    from hypotez.src.fast_api import MODE
    assert MODE == 'dev', f"Expected MODE to be 'dev', but got {MODE}"
```