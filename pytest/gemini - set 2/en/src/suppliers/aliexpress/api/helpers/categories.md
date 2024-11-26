```python
import pytest
from hypotez.src.suppliers.aliexpress.api.helpers.categories import filter_parent_categories, filter_child_categories
from hypotez.src.suppliers.aliexpress.api.helpers import models  # Assuming models are defined elsewhere

# Sample models for testing (replace with actual models if available)
class Category:
    def __init__(self, parent_category_id=None):
        self.parent_category_id = parent_category_id

class ChildCategory:
    def __init__(self, parent_category_id):
        self.parent_category_id = parent_category_id


@pytest.fixture
def categories_data():
    return [
        Category(),
        ChildCategory(1),
        Category(1),
        ChildCategory(2)
    ]


@pytest.fixture
def single_category():
    return Category(1)


@pytest.fixture
def invalid_input():
    return "invalid"

def test_filter_parent_categories_valid_input(categories_data):
    """Checks filtering of parent categories with valid input."""
    expected_result = [categories_data[0], categories_data[2]]
    actual_result = filter_parent_categories(categories_data)
    assert actual_result == expected_result


def test_filter_parent_categories_empty_input():
    """Checks handling of empty input."""
    assert filter_parent_categories([]) == []


def test_filter_parent_categories_single_category(single_category):
    """Check filtering of a single category."""
    assert filter_parent_categories(single_category) == [single_category]



def test_filter_parent_categories_invalid_input(invalid_input):
    """Checks handling of non-list/non-category input."""
    expected_result = [invalid_input]
    actual_result = filter_parent_categories(invalid_input)
    assert actual_result == expected_result


def test_filter_child_categories_valid_input(categories_data):
    """Checks filtering of child categories with valid input."""
    parent_id = 2
    expected_result = [categories_data[3]]
    actual_result = filter_child_categories(categories_data, parent_id)
    assert actual_result == expected_result

def test_filter_child_categories_no_match(categories_data):
    """Test with no matching child category."""
    parent_id = 5
    assert filter_child_categories(categories_data, parent_id) == []

def test_filter_child_categories_invalid_input(invalid_input):
    """Test with non-list/non-category input."""
    parent_id = 1
    expected_result = [invalid_input]
    actual_result = filter_child_categories(invalid_input, parent_id)
    assert actual_result == expected_result

def test_filter_child_categories_empty_input(categories_data):
    """Test with empty input list."""
    parent_id = 1
    assert filter_child_categories([], parent_id) == []


```

**Explanation and Improvements:**

* **Models:**  The code now includes sample `Category` and `ChildCategory` classes.  Crucially, in a real test, you'd replace these with the actual `models` classes from your project.
* **Clearer Test Names:**  Test names are more descriptive, indicating the input type and expected outcome.
* **Edge Cases:** Tests now cover empty input lists, single-element inputs, and invalid input types (not just lists).
* **`pytest.raises` (not needed here):**  The original code didn't need `pytest.raises` for exception handling because the functions are designed to gracefully handle non-list inputs.
* **Fixtures:** Fixtures are used to provide test data in a structured way, making the tests more organized.
* **Comprehensive Coverage:** The tests now cover various scenarios, including valid input, empty input, single elements, and invalid data types, all using the `categories_data` fixture.
* **`invalid_input` Fixture:** This allows for concise, reusable tests with a single invalid input.
* **Docstrings:**  Thorough docstrings explain the purpose and logic of each test.

**How to use:**

1.  **Replace Placeholders:** Replace the sample `Category` and `ChildCategory` classes with your actual model classes.
2.  **Run Tests:**  Save the test code (e.g., `test_categories.py`) in the same directory as your `categories.py` file.  Then run `pytest test_categories.py` from your terminal.


This revised solution is significantly more robust and comprehensive, ensuring thorough testing of your `filter_parent_categories` and `filter_child_categories` functions. Remember to adjust the tests to match your exact `models` definitions. Remember to install the `pytest` library if you haven't already (`pip install pytest`). Remember that correct class inheritance (and `hasattr()`) is very important to your `Category` and `ChildCategory` objects.