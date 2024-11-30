```python
import pytest
import hypotez.src.ai.myai

# Tests for the myai module
def test_mode():
    """
    Checks that the MODE variable is correctly set.
    """
    assert hypotez.src.ai.myai.MODE == 'dev'

def test_mode_assignment():
    """
    Tests that the MODE variable cannot be directly modified
    (to be sure it is a constant).
    """
    with pytest.raises(AttributeError):
        hypotez.src.ai.myai.MODE = 'test'
```