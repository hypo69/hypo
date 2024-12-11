```python
import pytest

# Tests for the __init__.py file, which appears to only contain constants.
# Since there are no functions or classes to test, there are no tests.


def test_mode_is_dev():
    """Checks if the MODE constant is 'dev'."""
    from hypotez.src.endpoints.prestashop.domains import MODE
    assert MODE == 'dev'
```