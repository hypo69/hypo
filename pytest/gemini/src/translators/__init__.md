```python
import pytest

# Tests for the __init__.py file (which currently only sets a constant)

def test_mode_is_dev():
    """Checks if the MODE constant is set to 'dev'."""
    from hypotez.src.translators import MODE
    assert MODE == 'dev', f"MODE should be 'dev', but is {MODE}"
```