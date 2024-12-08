```python
import pytest
from typing import List, Union

# Assuming models are defined elsewhere. For testing purposes, create mock models.
class Category:
    def __init__(self, parent_category_id=None, id=None):
        self.parent_category_id = parent_category_id
        self.id = id

class ChildCategory(Category):
    pass

from hypotez.src.suppliers.aliexpress.api.helpers.categories import filter_parent_categories, filter_child_categories


def test_filter_parent_categories_valid_input():
    """Tests filter_parent_categories with a list of valid categories."""
    categories = [
        Category(id=1),
        ChildCategory(parent_category_id=1, id=2),
        Category(id=3, parent_category_id=None),
    ]
    expected_output = [Category(id=1), Category(id=3, parent_category_id=None)]
    actual_output = filter_parent_categories(categories)
    assert actual_output == expected_output


def test_filter_parent_categories_empty_input():
    """Tests filter_parent_categories with an empty list."""
    categories = []
    expected_output = []
    actual_output = filter_parent_categories(categories)
    assert actual_output == expected_output


def test_filter_parent_categories_single_non_category_input():
    """Tests filter_parent_categories with a single non-category value."""
    categories = 123
    expected_output = [123]
    actual_output = filter_parent_categories(categories)
    assert actual_output == expected_output


def test_filter_parent_categories_mixed_input():
    """Tests filter_parent_categories with a mixed input type."""
    categories = [1, 2, Category(id=3, parent_category_id=None), "abc"]
    expected_output = [1, 2, "abc", Category(id=3, parent_category_id=None)]
    actual_output = filter_parent_categories(categories)
    assert actual_output == expected_output


def test_filter_child_categories_valid_input():
    """Tests filter_child_categories with valid input."""
    categories = [
        ChildCategory(parent_category_id=1, id=2),
        ChildCategory(parent_category_id=2, id=3),
        Category(id=4),
    ]
    parent_category_id = 1
    expected_output = [ChildCategory(parent_category_id=1, id=2)]
    actual_output = filter_child_categories(categories, parent_category_id)
    assert actual_output == expected_output


def test_filter_child_categories_invalid_parent_id():
    """Tests filter_child_categories with an invalid parent ID."""
    categories = [
        ChildCategory(parent_category_id=1, id=2),
    ]
    parent_category_id = 3
    expected_output = []
    actual_output = filter_child_categories(categories, parent_category_id)
    assert actual_output == expected_output


def test_filter_child_categories_empty_input():
    """Tests filter_child_categories with an empty list."""
    categories = []
    parent_category_id = 1
    expected_output = []
    actual_output = filter_child_categories(categories, parent_category_id)
    assert actual_output == expected_output


def test_filter_child_categories_single_non_category_input():
    """Tests filter_child_categories with a single non-category value."""
    categories = 123
    parent_category_id = 1
    expected_output = []
    actual_output = filter_child_categories(categories, parent_category_id)
    assert actual_output == []
```