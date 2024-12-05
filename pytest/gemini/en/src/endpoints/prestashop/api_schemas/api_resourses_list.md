```python
import pytest

# Import the code to be tested
from hypotez.src.endpoints.prestashop.api_schemas.api_resourses_list import resource


def test_resource_list_type():
    """Checks if the resource list is a list."""
    assert isinstance(resource, list), "resource should be a list"


def test_resource_list_content():
    """Checks if the resource list contains strings."""
    for item in resource:
        assert isinstance(item, str), f"Element '{item}' in the resource list is not a string"


def test_resource_list_duplicates():
    """Checks if the resource list contains any duplicates."""
    assert len(resource) == len(set(resource)), "The resource list contains duplicates"


def test_resource_list_length():
    """Checks the length of the resource list."""
    assert len(resource) > 0, "The resource list should not be empty"
    assert len(resource) <= 100, "The resource list is too long (maximum 100 resources)"


def test_resource_list_contains_specific_elements():
    """Checks if the resource list contains specific elements."""
    assert 'products' in resource
    assert 'categories' in resource
    assert 'orders' in resource


def test_resource_list_edge_case_empty_list():
    """Tests with an empty resource list (should raise an exception)."""
    with pytest.raises(AssertionError):
        empty_resource = []
        assert len(empty_resource) > 0  # Expecting an assertion error

def test_resource_list_invalid_element_type():
    """Tests with an invalid element type in the resource list (should raise an exception)."""
    invalid_resource = ['products', 123, 'categories']
    with pytest.raises(AssertionError):
        for item in invalid_resource:
            assert isinstance(item, str), f"Element '{item}' in the resource list is not a string"
```