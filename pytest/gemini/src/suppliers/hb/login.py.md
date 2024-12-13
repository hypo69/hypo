```python
import pytest

from src.suppliers.hb.login import login

def test_login_valid_supplier():
    """
    Test the login function with a valid supplier.
    It should return True as per the current implementation.
    """
    # Mock a supplier object (as it's not used) for test purposes
    class MockSupplier:
        pass
    mock_supplier = MockSupplier()
    assert login(mock_supplier) == True

def test_login_with_none():
    """
    Test the login function with None as input.
    It should not raise an exception due to the current implementation
    and return True.
    """
    assert login(None) == True

def test_login_with_integer():
    """
    Test the login function with an integer input.
    It should not raise an exception due to the current implementation
    and return True.
    """
    assert login(123) == True

def test_login_with_string():
    """
    Test the login function with a string input.
    It should not raise an exception due to the current implementation
     and return True.
    """
    assert login("test") == True

def test_login_with_list():
    """
    Test the login function with a list input.
     It should not raise an exception due to the current implementation
    and return True.
    """
    assert login([1, 2, 3]) == True
```