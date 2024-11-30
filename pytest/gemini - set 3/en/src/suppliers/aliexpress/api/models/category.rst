```python
import pytest

from hypotez.src.suppliers.aliexpress.api.models.category import Category, ChildCategory


def test_category_creation_valid():
    """Tests creation of Category object with valid data."""
    category = Category(category_id=1, category_name="Electronics")
    assert category.category_id == 1
    assert category.category_name == "Electronics"


def test_category_creation_invalid_category_id():
    """Tests creation of Category object with invalid category_id (not an integer)."""
    with pytest.raises(TypeError):
        Category(category_id="invalid", category_name="Electronics")


def test_category_creation_invalid_category_name():
    """Tests creation of Category object with invalid category_name (not a string)."""
    with pytest.raises(TypeError):
        Category(category_id=1, category_name=123)


def test_child_category_creation_valid():
    """Tests creation of ChildCategory object with valid data."""
    child_category = ChildCategory(category_id=2, category_name="Phones", parent_category_id=1)
    assert child_category.category_id == 2
    assert child_category.category_name == "Phones"
    assert child_category.parent_category_id == 1


def test_child_category_creation_invalid_parent_category_id():
    """Tests creation of ChildCategory object with invalid parent_category_id (not an integer)."""
    with pytest.raises(TypeError):
        ChildCategory(category_id=2, category_name="Phones", parent_category_id="invalid")


def test_child_category_creation_missing_parent_category_id():
    """Tests creation of ChildCategory object with missing parent_category_id."""
    with pytest.raises(TypeError) as excinfo:
        ChildCategory(category_id=2, category_name="Phones")
    assert "missing" in str(excinfo.value)


def test_child_category_inherits_category_attributes():
    """Tests if ChildCategory correctly inherits attributes from Category."""
    child_category = ChildCategory(category_id=3, category_name="Laptops", parent_category_id=2)
    assert isinstance(child_category, Category)
    
    
def test_child_category_incorrect_type_parent_id():
    """Tests creation with incorrect type for parent_category_id, like a string instead of int."""
    with pytest.raises(TypeError):
        ChildCategory(category_id=2, category_name="Phones", parent_category_id="1")
    

def test_child_category_creation_invalid_category_id():
    """Tests creation of ChildCategory object with invalid category_id (not an integer)."""
    with pytest.raises(TypeError):
        ChildCategory(category_id="invalid", category_name="Phones", parent_category_id=1)

# Test cases for other potential methods (e.g., if there were methods to update or access attributes)
# ... (Add more test cases as needed based on other methods or complex logic)

```