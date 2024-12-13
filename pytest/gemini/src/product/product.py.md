```python
import pytest
from src.product.product import Product
from src.category import Category  # Assuming Category class is available for mocking

# Mock the Category.get_parents method for testing purposes
def mock_get_parents(id_category, dept):
    if id_category == 1:
        return [1, 2]
    elif id_category == 2:
        return [2,3,4]
    else:
         return []


# Set up fixtures if needed, in this case, we don't need specific fixtures
# Tests for Product.get_parent_categories method
def test_get_parent_categories_valid_input():
    """Checks the behavior of get_parent_categories with a valid integer input.
    
    Mocks the Category.get_parents method
    """
    Category.get_parents = mock_get_parents
    id_category = 1
    dept = 0
    expected_result = [1, 2]
    
    result = Product.get_parent_categories(id_category, dept)
    
    assert result == expected_result
    
def test_get_parent_categories_valid_input_depth():
    """Checks the behavior of get_parent_categories with a valid integer input and specific depth.
    
    Mocks the Category.get_parents method
    """
    Category.get_parents = mock_get_parents
    id_category = 2
    dept = 1
    expected_result = [2,3,4]
    
    result = Product.get_parent_categories(id_category, dept)
    
    assert result == expected_result

def test_get_parent_categories_invalid_input_type():
    """Checks the behavior of get_parent_categories when id_category is not an integer.
    
    Verifies that a TypeError is raised.
    """
    with pytest.raises(TypeError, match="id_category must be an integer"):
        Product.get_parent_categories("invalid", 0)

def test_get_parent_categories_edge_case_zero_dept():
    """Checks the behavior of get_parent_categories with a valid integer input and zero depth.
    
    Mocks the Category.get_parents method
    """
    Category.get_parents = mock_get_parents
    id_category = 1
    dept = 0
    expected_result = [1, 2]
    
    result = Product.get_parent_categories(id_category, dept)
    
    assert result == expected_result
    
def test_get_parent_categories_edge_case_no_parents():
    """Checks the behavior of get_parent_categories with an ID that has no parents
    
    Mocks the Category.get_parents method
    """
    Category.get_parents = mock_get_parents
    id_category = 3
    dept = 0
    expected_result = []
    
    result = Product.get_parent_categories(id_category, dept)
    
    assert result == expected_result
```