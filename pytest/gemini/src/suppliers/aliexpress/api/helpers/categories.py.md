```python
import pytest
from typing import List
from hypotez.src.suppliers.aliexpress.api import models
from hypotez.src.suppliers.aliexpress.api.helpers.categories import filter_parent_categories, filter_child_categories

# Fixture for creating sample category and child category objects
@pytest.fixture
def sample_categories():
    """Provides a list of sample categories and child categories for testing."""
    class Category:
        def __init__(self, category_id: int, category_name: str):
            self.category_id = category_id
            self.category_name = category_name

    class ChildCategory:
        def __init__(self, category_id: int, category_name: str, parent_category_id: int):
            self.category_id = category_id
            self.category_name = category_name
            self.parent_category_id = parent_category_id


    return [
        Category(1, "Category 1"),
        ChildCategory(2, "Child Category 1", 1),
        Category(3, "Category 2"),
        ChildCategory(4, "Child Category 2", 3),
        ChildCategory(5, "Child Category 3", 1),
        Category(6, "Category 3")
    ]

@pytest.fixture
def sample_categories_with_different_types():
    """Provides a list of sample categories and other types for testing."""
    class Category:
        def __init__(self, category_id: int, category_name: str):
            self.category_id = category_id
            self.category_name = category_name

    class ChildCategory:
        def __init__(self, category_id: int, category_name: str, parent_category_id: int):
            self.category_id = category_id
            self.category_name = category_name
            self.parent_category_id = parent_category_id


    return [
        Category(1, "Category 1"),
        ChildCategory(2, "Child Category 1", 1),
        1,
        "string",
        2.2,
        Category(3, "Category 2"),
        ChildCategory(4, "Child Category 2", 3),
        ChildCategory(5, "Child Category 3", 1),
        Category(6, "Category 3")
    ]
@pytest.fixture
def empty_categories():
     return []


# Tests for filter_parent_categories
def test_filter_parent_categories_valid_input(sample_categories):
    """Checks correct filtering of parent categories with valid input."""
    parent_categories = filter_parent_categories(sample_categories)
    assert len(parent_categories) == 3
    assert all(not hasattr(cat, 'parent_category_id') for cat in parent_categories)
    assert [cat.category_id for cat in parent_categories] == [1, 3, 6]

def test_filter_parent_categories_empty_list(empty_categories):
    """Checks behavior with an empty list."""
    parent_categories = filter_parent_categories(empty_categories)
    assert parent_categories == []

def test_filter_parent_categories_with_different_types(sample_categories_with_different_types):
    """Checks correct filtering of parent categories when invalid types are passed."""
    parent_categories = filter_parent_categories(sample_categories_with_different_types)
    assert len(parent_categories) == 3
    assert all(not hasattr(cat, 'parent_category_id') for cat in parent_categories)
    assert [cat.category_id for cat in parent_categories] == [1, 3, 6]

def test_filter_parent_categories_single_category(sample_categories):
    """Checks behavior when only one parent category is passed."""
    single_category = sample_categories[0]
    parent_categories = filter_parent_categories([single_category])
    assert len(parent_categories) == 1
    assert parent_categories[0].category_id == 1

def test_filter_parent_categories_single_child_category(sample_categories):
    """Checks behavior when only one child category is passed."""
    single_child_category = sample_categories[1]
    parent_categories = filter_parent_categories([single_child_category])
    assert len(parent_categories) == 0

def test_filter_parent_categories_single_invalid_type():
    """Checks behavior when single invalid type is passed."""
    parent_categories = filter_parent_categories(1)
    assert len(parent_categories) == 0


# Tests for filter_child_categories
def test_filter_child_categories_valid_input(sample_categories):
    """Checks correct filtering of child categories with valid input."""
    child_categories = filter_child_categories(sample_categories, 1)
    assert len(child_categories) == 2
    assert all(hasattr(cat, 'parent_category_id') and cat.parent_category_id == 1 for cat in child_categories)
    assert [cat.category_id for cat in child_categories] == [2, 5]

def test_filter_child_categories_no_match(sample_categories):
    """Checks behavior when no child categories match the given parent ID."""
    child_categories = filter_child_categories(sample_categories, 999)
    assert len(child_categories) == 0

def test_filter_child_categories_empty_list(empty_categories):
    """Checks behavior with an empty list."""
    child_categories = filter_child_categories(empty_categories, 1)
    assert child_categories == []

def test_filter_child_categories_with_different_types(sample_categories_with_different_types):
    """Checks correct filtering of child categories when invalid types are passed."""
    child_categories = filter_child_categories(sample_categories_with_different_types, 1)
    assert len(child_categories) == 2
    assert all(hasattr(cat, 'parent_category_id') and cat.parent_category_id == 1 for cat in child_categories)
    assert [cat.category_id for cat in child_categories] == [2, 5]


def test_filter_child_categories_single_category(sample_categories):
    """Checks behavior when only one parent category is passed."""
    single_category = sample_categories[0]
    child_categories = filter_child_categories([single_category], 1)
    assert len(child_categories) == 0

def test_filter_child_categories_single_child_category(sample_categories):
    """Checks behavior when only one child category is passed."""
    single_child_category = sample_categories[1]
    child_categories = filter_child_categories([single_child_category], 1)
    assert len(child_categories) == 1
    assert child_categories[0].category_id == 2

def test_filter_child_categories_single_invalid_type():
    """Checks behavior when single invalid type is passed."""
    child_categories = filter_child_categories(1, 1)
    assert len(child_categories) == 0
```