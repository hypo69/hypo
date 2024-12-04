```python
import pytest

from hypotez.src.suppliers.aliexpress.api.models.category import Category, ChildCategory


# Test cases for the Category class
def test_category_valid_creation():
    """Test creation of Category object with valid data."""
    category = Category(category_id=1, category_name="Electronics")
    assert category.category_id == 1
    assert category.category_name == "Electronics"


def test_category_invalid_category_id():
    """Test creation of Category object with invalid category_id (not an integer)."""
    with pytest.raises(TypeError):
        Category(category_id="invalid", category_name="Electronics")


def test_category_invalid_category_name():
    """Test creation of Category object with invalid category_name (empty string)."""
    with pytest.raises(ValueError):
        Category(category_id=1, category_name="")


# Test cases for the ChildCategory class
def test_child_category_valid_creation():
    """Test creation of ChildCategory object with valid data."""
    child_category = ChildCategory(category_id=2, category_name="Laptops", parent_category_id=1)
    assert child_category.category_id == 2
    assert child_category.category_name == "Laptops"
    assert child_category.parent_category_id == 1


def test_child_category_missing_parent_category_id():
    """Test creation of ChildCategory object without parent_category_id."""
    with pytest.raises(TypeError):
        ChildCategory(category_id=2, category_name="Laptops")


def test_child_category_invalid_parent_category_id():
    """Test creation of ChildCategory object with invalid parent_category_id (not an integer)."""
    with pytest.raises(TypeError):
        ChildCategory(category_id=2, category_name="Laptops", parent_category_id="invalid")


def test_child_category_invalid_category_name():
    """Test creation of ChildCategory object with invalid category_name (empty string)."""
    with pytest.raises(ValueError):
        ChildCategory(category_id=1, category_name="", parent_category_id=1)

# Additional tests for edge cases (e.g., boundary values) or complex scenarios


def test_child_category_zero_parent_id():
    """Test creation of ChildCategory with parent_category_id as zero."""
    child_category = ChildCategory(category_id=2, category_name="Laptops", parent_category_id=0)
    assert child_category.parent_category_id == 0


def test_child_category_negative_parent_id():
    """Test creation of ChildCategory with negative parent_category_id."""
    child_category = ChildCategory(category_id=2, category_name="Laptops", parent_category_id=-1)
    assert child_category.parent_category_id == -1

```