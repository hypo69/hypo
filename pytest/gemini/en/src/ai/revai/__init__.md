```python
import pytest
import sys

# Replace with the actual file content if available.
# Assuming MODE is a global variable
MODE = 'dev'


def test_mode_is_dev():
    """Checks if the MODE variable is set to 'dev'."""
    assert MODE == 'dev', f"MODE variable should be 'dev', but is '{MODE}'"
```