```python
import pytest
import hypotez.src.ai.myai as myai

# Tests for the myai module

def test_mode_is_dev():
    """Checks if the MODE variable is set to 'dev'."""
    assert myai.MODE == 'dev'
```