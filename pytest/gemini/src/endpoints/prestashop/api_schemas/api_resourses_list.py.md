```python
import pytest
from hypotez.src.endpoints.prestashop.api_schemas.api_resourses_list import resource, MODE


def test_resource_is_a_list():
    """Checks if the 'resource' variable is a list."""
    assert isinstance(resource, list)

def test_resource_is_not_empty():
    """Checks if the 'resource' list is not empty."""
    assert len(resource) > 0

def test_resource_contains_expected_elements():
    """Checks if the 'resource' list contains some specific expected elements."""
    expected_elements = ['products', 'categories', 'customers', 'orders', 'suppliers']
    for element in expected_elements:
        assert element in resource

def test_resource_elements_are_strings():
    """Checks if all elements within the 'resource' list are strings."""
    for element in resource:
        assert isinstance(element, str)

def test_resource_elements_are_not_empty_strings():
    """Checks if all elements within the 'resource' list are not empty strings."""
    for element in resource:
        assert len(element) > 0

def test_resource_no_duplicate_elements():
    """Checks if there are no duplicate elements within the 'resource' list."""
    assert len(resource) == len(set(resource))

def test_mode_is_string():
    """Checks if the 'MODE' variable is a string."""
    assert isinstance(MODE, str)

def test_mode_is_dev():
     """Checks if the 'MODE' variable is equal to `dev` string."""
     assert MODE == 'dev'
```