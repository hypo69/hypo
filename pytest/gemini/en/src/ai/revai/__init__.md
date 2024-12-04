```python
import pytest

# Tests for the module
def test_mode_is_dev():
    """Checks if the MODE variable is set to 'dev'."""
    from hypotez.src.ai.revai import MODE
    assert MODE == 'dev', f"MODE variable should be 'dev', but it is {MODE}"
```