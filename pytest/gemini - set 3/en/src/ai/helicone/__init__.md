```python
import pytest

# Tests for the helicone module
def test_mode_default_value():
    """Checks that the MODE variable is initialized correctly."""
    from hypotez.src.ai.helicone import MODE
    assert MODE == 'dev'
```