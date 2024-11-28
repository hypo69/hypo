```python
import pytest
from hypotez.src.suppliers.aliexpress.api.helpers.categories import filter_parent_categories, filter_child_categories
from hypotez.src.suppliers.aliexpress.api.helpers import models  # Assuming models are defined elsewhere

# Dummy models for testing (replace with actual models if available)
class Category:
    def __init__(self, parent_category_id=None, id=None):
        self.parent_category_id = parent_category_id
        self.id = id
    
class ChildCategory(Category):
    pass


@pytest.fixture
def categories_data():
    """Provides test data for the category functions."""
    return [
        Category(parent_category_id=1, id=1),
        Category(parent_category_id=None, id=2),
        ChildCategory(parent_category_id=1, id=3),
        ChildCategory(parent_category_id=2, id=4),
        Category(id=5) # category without parent_category_id
    ]


def test_filter_parent_categories_valid_input(categories_data):
    """Tests filter_parent_categories with valid input."""
    expected_output = [categories_data[1], categories_data[4]]
    actual_output = filter_parent_categories(categories_data)
    assert actual_output == expected_output


def test_filter_parent_categories_empty_input():
    """Tests filter_parent_categories with an empty list."""
    assert filter_parent_categories([]) == []


def test_filter_parent_categories_single_non_category_input():
    """Tests filter_parent_categories with a single non-category input."""
    assert filter_parent_categories(123) == [] #should return empty list for non-list input


def test_filter_child_categories_valid_input(categories_data):
    """Tests filter_child_categories with valid input."""
    parent_id = 1
    expected_output = [categories_data[2]]
    actual_output = filter_child_categories(categories_data, parent_id)
    assert actual_output == expected_output


def test_filter_child_categories_invalid_parent_id(categories_data):
    """Tests filter_child_categories with an invalid parent ID."""
    parent_id = 5
    expected_output = []
    actual_output = filter_child_categories(categories_data, parent_id)
    assert actual_output == expected_output

def test_filter_child_categories_empty_input(categories_data):
    """Tests filter_child_categories with an empty list."""
    parent_id = 1
    assert filter_child_categories([], parent_id) == []

def test_filter_child_categories_single_non_category_input(categories_data):
    """Tests filter_child_categories with a single non-category input."""
    parent_id = 1
    assert filter_child_categories(123, parent_id) == []


def test_filter_parent_categories_non_list_input():
    """Tests filter_parent_categories with non-list input."""
    assert filter_parent_categories("not a list") == []


def test_filter_child_categories_non_list_input(categories_data):
    """Tests filter_child_categories with non-list input."""
    parent_id = 1
    assert filter_child_categories("not a list", parent_id) == []



# Example demonstrating how to test with specific error types (replace with your actual exceptions if needed)
# def test_filter_categories_invalid_input_type():
#     with pytest.raises(TypeError):
#         filter_parent_categories(123)


```

**Explanation and Improvements:**

1. **Dummy Models:**  The code now includes `Category` and `ChildCategory` classes.  Replace these with your actual models if they are defined elsewhere.  This is crucial for testing because you need objects to instantiate.

2. **`pytest.raises` (Removed):** The code now demonstrates how to handle potential errors, but removed the example of `pytest.raises` because it didn't have a suitable error in the original function. There's no explicit need for `pytest.raises` in this particular case, as the functions handle input types correctly, converting single values to a list.  

3. **Comprehensive Test Cases:**  The test cases now cover:
   - Valid inputs (various scenarios).
   - Empty input lists.
   - Edge cases with single non-list inputs.
   - Handling of a non-list input (e.g., string).


4. **Clear Test Names:** The test function names are descriptive and indicate the input and expected outcome.

5. **Fixtures:** The `categories_data` fixture provides test data that's used by multiple tests, making the tests more efficient.

6. **Docstrings:**  Docstrings are added to all tests for better clarity and understandability.


**How to Run the Tests:**

1. Make sure you have `pytest` installed:
   ```bash
   pip install pytest
   ```

2. Save the test code (e.g., `test_categories.py`) in the same directory as the `categories.py` file.

3. Run the tests from your terminal:
   ```bash
   pytest test_categories.py
   ```


This revised solution is much more robust and covers a wider range of potential input scenarios, especially important for production-quality code. Remember to replace the dummy model classes with your actual models if applicable. Also, consider adding more sophisticated test cases based on the actual expected behaviors of your functions.