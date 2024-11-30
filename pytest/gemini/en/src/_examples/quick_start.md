```python
import pytest
import hypotez.src._examples.quick_start as quick_start

# No fixtures needed for the provided code

def test_mode_is_dev():
    """Checks if the MODE variable is set to 'dev'."""
    assert quick_start.MODE == 'dev'

# No other functions or classes to test, as the provided code is minimal
```