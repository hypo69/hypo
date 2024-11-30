```python
import pytest
import hypotez.src.suppliers.ivory.login as login

# No fixtures needed for this simple code.


def test_mode_is_dev():
    """Checks if the MODE constant is 'dev'."""
    assert login.MODE == 'dev'

# Since there are no functions or methods,
# there are no more tests to write.  
# Further tests would depend on the actual functions 
# in the login.py file (which is empty).
```