```python
import pytest
from typing import List
from hypotez.src.suppliers.aliexpress.api.helpers.categories import filter_parent_categories, filter_child_categories
from hypotez.src.suppliers.aliexpress.api.helpers import models  # Assuming models are defined elsewhere

# Dummy models for testing (replace with actual models if available)
class Category:
    parent_category_id = None

class ChildCategory:
    parent_category_id = None


# Test data
category_data = [
    Category(),
    ChildCategory(),
    Category(),
    ChildCategory(parent_category_id=1),
    Category(parent_category_id=2),  # Example with parent_category_id
]


@pytest.fixture
def valid_categories():
    return [Category(), ChildCategory(parent_category_id=1), Category(parent_category_id=2)]

@pytest.fixture
def child_categories_with_parent():
    return [ChildCategory(parent_category_id=1), ChildCategory(parent_category_id=1), ChildCategory(parent_category_id=2)]



# Tests for filter_parent_categories
def test_filter_parent_categories_valid_input(valid_categories):
    """Checks correct behavior with valid input."""
    result = filter_parent_categories(valid_categories)
    assert len(result) == 2 # Expecting 2 parent categories without parent id
    assert isinstance(result[0], Category)
    assert isinstance(result[1], Category)

def test_filter_parent_categories_empty_input():
    """Checks behavior with an empty input list."""
    result = filter_parent_categories([])
    assert result == []

def test_filter_parent_categories_single_category():
    """Checks with a single category input."""
    result = filter_parent_categories(Category())
    assert result == [Category()]


def test_filter_parent_categories_invalid_input_not_list():
  """Checks with invalid input (not a list)."""
  with pytest.raises(TypeError):
    filter_parent_categories(123)


def test_filter_parent_categories_invalid_input_mixed_types():
  """Checks handling of mixed types in input list."""
  mixed_input = [Category(), 123, "abc", ChildCategory()]
  result = filter_parent_categories(mixed_input)
  assert len(result) == 2 #filtering out the non-Category type
  assert isinstance(result[0], Category)




# Tests for filter_child_categories
def test_filter_child_categories_valid_input(child_categories_with_parent):
    """Tests with valid input and parent_category_id."""
    result = filter_child_categories(child_categories_with_parent, 1)
    assert len(result) == 2
    assert all(isinstance(cat, ChildCategory) for cat in result)

def test_filter_child_categories_no_match():
    """Tests with no matching child categories."""
    result = filter_child_categories(child_categories_with_parent, 2)
    assert result == []

def test_filter_child_categories_invalid_parent_id():
    """Tests with invalid parent_category_id."""
    result = filter_child_categories(child_categories_with_parent, 3)
    assert result == []

def test_filter_child_categories_invalid_input_not_list():
  """Tests invalid input (not a list) for filter_child_categories."""
  with pytest.raises(TypeError):
    filter_child_categories(123, 1)


def test_filter_child_categories_mixed_types():
  """Tests handling of mixed types in input list for filter_child_categories."""
  mixed_input = [ChildCategory(parent_category_id=1), 123, "abc", ChildCategory(parent_category_id=1)]
  result = filter_child_categories(mixed_input, 1)
  assert len(result) == 2
  assert all(isinstance(cat, ChildCategory) for cat in result)


```