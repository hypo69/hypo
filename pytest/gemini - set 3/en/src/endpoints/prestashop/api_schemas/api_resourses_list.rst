```python
import pytest

from hypotez.src.endpoints.prestashop.api_schemas.api_resourses_list import resource, MODE

def test_resource_list_type():
    """Checks if resource is a list."""
    assert isinstance(resource, list), "resource should be a list"

def test_resource_list_non_empty():
    """Checks if resource list is not empty."""
    assert len(resource) > 0, "resource list should not be empty"


def test_resource_list_elements_are_strings():
    """Checks if all elements in the resource list are strings."""
    for element in resource:
        assert isinstance(element, str), f"Element '{element}' in resource list should be a string"


def test_resource_list_contains_unique_elements():
    """Checks if all elements in resource list are unique."""
    assert len(resource) == len(set(resource)), "resource list should contain unique elements"


def test_mode_is_string():
    """Checks if MODE is a string."""
    assert isinstance(MODE, str), "MODE should be a string"


def test_mode_value():
    """Checks if MODE has a valid value."""
    assert MODE in ['dev', 'prod', 'test'], "MODE should be either 'dev', 'prod', or 'test'"


# Edge case: testing with an empty list (should raise an exception)
def test_resource_list_empty():
    """Test handling of an empty resource list (should raise ValueError)."""
    with pytest.raises(ValueError):
        resource_empty = []
        # ... (rest of the function remains the same)
        pass

# Edge case: testing with a list containing non-strings
def test_resource_list_non_string_elements():
    """Test handling of a resource list containing non-string elements (should raise TypeError)."""
    with pytest.raises(TypeError):
        resource_invalid = ["products", 123, "categories"]
        # ... (rest of the function remains the same)
        pass



# Example testing with specific elements
def test_resource_list_contains_specific_element():
    """Checks if the resource list contains a specific element."""
    assert "products" in resource, "The list should contain 'products'"



```