```python
import pytest

# Import the code you want to test
from hypotez.src.endpoints.prestashop.api_schemas.api_resourses_list import resource

# Test cases for the resource list
def test_resource_list_valid():
    """Checks if the resource list contains the expected values."""
    assert 'products' in resource
    assert 'categories' in resource
    assert 'addresses' in resource
    # Add more assertions for other expected resources


def test_resource_list_length():
    """Checks if the resource list has the expected length."""
    assert len(resource) == 70, f"Expected 70 resources, but got {len(resource)}"

def test_resource_list_duplicates():
    """Checks if the resource list contains any duplicates."""
    assert len(resource) == len(set(resource)), "The resource list contains duplicates."


def test_resource_list_case_sensitivity():
    """Checks if the resource names are case-sensitive."""
    assert 'products' in resource
    assert 'Products' not in resource
    #Similarly check for other resources.
```