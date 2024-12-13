```python
import pytest

from hypotez.src.suppliers.aliexpress.api.models.category import Category, ChildCategory


def test_category_creation():
    """Test the creation of a Category object with valid data."""
    category = Category()
    category.category_id = 123
    category.category_name = "Electronics"
    assert category.category_id == 123
    assert category.category_name == "Electronics"


def test_child_category_creation():
    """Test the creation of a ChildCategory object with valid data."""
    child_category = ChildCategory()
    child_category.category_id = 456
    child_category.category_name = "Mobile Phones"
    child_category.parent_category_id = 123
    assert child_category.category_id == 456
    assert child_category.category_name == "Mobile Phones"
    assert child_category.parent_category_id == 123


def test_category_attributes_are_correct_types():
    """Test that the attributes of a Category object are of the correct types."""
    category = Category()
    category.category_id = 123
    category.category_name = "Electronics"
    assert isinstance(category.category_id, int)
    assert isinstance(category.category_name, str)


def test_child_category_attributes_are_correct_types():
    """Test that the attributes of a ChildCategory object are of the correct types."""
    child_category = ChildCategory()
    child_category.category_id = 456
    child_category.category_name = "Mobile Phones"
    child_category.parent_category_id = 123
    assert isinstance(child_category.category_id, int)
    assert isinstance(child_category.category_name, str)
    assert isinstance(child_category.parent_category_id, int)


def test_category_empty_init():
    """Test the creation of a Category object without initial data"""
    category = Category()
    assert hasattr(category, "category_id")
    assert hasattr(category, "category_name")
    

def test_child_category_empty_init():
    """Test the creation of a ChildCategory object without initial data"""
    child_category = ChildCategory()
    assert hasattr(child_category, "category_id")
    assert hasattr(child_category, "category_name")
    assert hasattr(child_category, "parent_category_id")
```