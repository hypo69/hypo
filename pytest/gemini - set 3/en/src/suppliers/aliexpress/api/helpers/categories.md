```python
import pytest
from hypotez.src.suppliers.aliexpress.api.helpers.categories import filter_parent_categories, filter_child_categories
from hypotez.src.suppliers.aliexpress.api.helpers import models  # Assuming models are defined elsewhere

# Define example models (replace with actual models if available)
class Category:
    def __init__(self, id=None, parent_category_id=None):
        self.id = id
        self.parent_category_id = parent_category_id

class ChildCategory:
    def __init__(self, id=None, parent_category_id=None):
        self.id = id
        self.parent_category_id = parent_category_id

# Fixture for creating test data
@pytest.fixture
def categories():
    return [
        Category(1, None),
        ChildCategory(2, 1),
        Category(3, 4),  # Parent category with a parent
        ChildCategory(4, 5),
        Category(5, None),
        ChildCategory(6, 5),
    ]


# Tests for filter_parent_categories
def test_filter_parent_categories_valid_input(categories):
    """Tests with a list of valid categories."""
    expected_result = [categories[0], categories[4]]
    actual_result = filter_parent_categories(categories)
    assert actual_result == expected_result

def test_filter_parent_categories_empty_input():
    """Tests with an empty list."""
    assert filter_parent_categories([]) == []

def test_filter_parent_categories_single_category(categories):
  """Test with a single Category object."""
  assert filter_parent_categories(categories[0]) == [categories[0]]


def test_filter_parent_categories_non_category_input(categories):
  """Test with a non-list input."""
  assert filter_parent_categories(123) == []


def test_filter_parent_categories_with_child_category(categories):
    """Tests that child categories are filtered out."""
    expected_result = [categories[0], categories[4]]
    actual_result = filter_parent_categories(categories)
    assert actual_result == expected_result



# Tests for filter_child_categories
def test_filter_child_categories_valid_input(categories):
    """Tests with valid input and parent_category_id."""
    expected_result = [categories[1],categories[6]]
    actual_result = filter_child_categories(categories, 1)
    assert actual_result == expected_result
    
def test_filter_child_categories_invalid_parent_id(categories):
    """Tests with invalid parent_category_id."""
    assert filter_child_categories(categories, 10) == []


def test_filter_child_categories_empty_input(categories):
    """Tests with an empty list of categories."""
    assert filter_child_categories([], 1) == []

def test_filter_child_categories_no_children(categories):
    """Tests with no child categories for the specified parent."""
    assert filter_child_categories([categories[0],categories[2]],1) == []

def test_filter_child_categories_non_list_input(categories):
  """Test with a non-list input for categories."""
  assert filter_child_categories(123, 1) == []
```

**Explanation and Improvements:**

* **Model Definitions:** Added example `Category` and `ChildCategory` classes. Replace these with your actual model definitions if available.  This is crucial for testing methods that rely on attributes of the objects.
* **Clearer Test Names:** Improved test names for better readability.
* **Comprehensive Test Cases:** Added tests for empty lists, single category input, and non-list inputs.  Also included cases with a mix of categories and child categories to ensure filtering works correctly.
* **Edge Cases:** Added tests for `parent_category_id` values not in the input and edge cases that cover scenarios where no parent categories or child categories match the criteria.
* **pytest.raises (not used here):**  `pytest.raises` isn't needed in these tests, as the expected behavior is to return empty lists or correct lists for invalid inputs and boundary conditions.
* **Fixture for Categories:** Created a `categories` fixture for reusable test data. This makes the tests more concise and readable.


**To run these tests:**

1.  Make sure you have `pytest` installed: `pip install pytest`
2.  Save the test code in a file (e.g., `test_categories.py`).
3.  Run the tests from your terminal: `pytest test_categories.py`

Remember to replace the example `Category` and `ChildCategory` with your actual models.  If your `models` module has a complex structure, you might need additional fixtures or test data to ensure full coverage.  Crucially, make sure the example models have the `parent_category_id` attribute to match the method's requirements.