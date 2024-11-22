```python
import pytest
from typing import List
from hypotez.src.suppliers.aliexpress.api.helpers.categories import filter_parent_categories, filter_child_categories
from hypotez.src.suppliers.aliexpress.api import models  # Adjust import path as needed


class TestCategoriesHelpers:

    def test_filter_parent_categories_valid_input(self):
        # Valid input: list of categories without parents
        category1 = models.Category(id=1)
        category2 = models.Category(id=2)
        categories = [category1, category2]
        expected_result = [category1, category2]
        actual_result = filter_parent_categories(categories)
        assert actual_result == expected_result

    def test_filter_parent_categories_with_child_category(self):
        # Valid input: list containing a category and a child category
        category = models.Category(id=1)
        child_category = models.ChildCategory(id=2, parent_category_id=3)
        categories = [category, child_category]
        expected_result = [category]
        actual_result = filter_parent_categories(categories)
        assert actual_result == expected_result


    def test_filter_parent_categories_empty_list(self):
        # Edge case: empty list
        categories = []
        expected_result = []
        actual_result = filter_parent_categories(categories)
        assert actual_result == expected_result


    def test_filter_parent_categories_single_category(self):
        # Valid input: single category object
        category = models.Category(id=1)
        expected_result = [category]
        actual_result = filter_parent_categories(category)
        assert actual_result == expected_result

    def test_filter_parent_categories_non_category_input(self):
        # Invalid input: non-list input
        result = filter_parent_categories(123)
        assert result == []
        result = filter_parent_categories("string")
        assert result == []

    def test_filter_child_categories_valid_input(self):
        # Valid input: list of child categories with matching parent ID
        category1 = models.ChildCategory(id=1, parent_category_id=10)
        category2 = models.ChildCategory(id=2, parent_category_id=10)
        categories = [category1, category2]
        parent_category_id = 10
        expected_result = [category1, category2]
        actual_result = filter_child_categories(categories, parent_category_id)
        assert actual_result == expected_result

    def test_filter_child_categories_no_match(self):
        # Edge case: no matching child categories
        category1 = models.ChildCategory(id=1, parent_category_id=10)
        categories = [category1]
        parent_category_id = 20
        expected_result = []
        actual_result = filter_child_categories(categories, parent_category_id)
        assert actual_result == expected_result

    def test_filter_child_categories_with_parent_category(self):
        # Valid input: list containing a parent and child category.
        category = models.Category(id=10)
        child_category = models.ChildCategory(id=1, parent_category_id=10)
        categories = [category, child_category]
        parent_category_id = 10
        expected_result = [child_category]
        actual_result = filter_child_categories(categories, parent_category_id)
        assert actual_result == expected_result


    def test_filter_child_categories_empty_list(self):
        # Edge case: empty list
        categories = []
        parent_category_id = 10
        expected_result = []
        actual_result = filter_child_categories(categories, parent_category_id)
        assert actual_result == expected_result

    def test_filter_child_categories_non_category_input(self):
      # Invalid input: non-list input
      result = filter_child_categories(123, 10)
      assert result == []
      result = filter_child_categories("string", 10)
      assert result == []
```


**Explanation and Improvements:**

* **Clearer Test Names:** Test names now explicitly describe the input and expected outcome.
* **Comprehensive Scenarios:** Tests cover various scenarios, including empty lists, single elements, non-list input, and scenarios with both parent and child categories.
* **Edge Cases:**  Thorough testing of edge cases like empty lists and non-matching parent IDs.
* **`pytest.raises` not needed:** The original code's error handling wasn't being tested for, so `pytest.raises` wasn't required.  This test suite now covers the handling of incorrect data types (e.g., passing an integer instead of a list) and covers the basic expected input types and their behavior.
* **Import Fix:**  Import `models` from the correct location.  This example assumes the correct path has been provided. 
* **Class Structure:** Tests are grouped into a `TestCategoriesHelpers` class for better organization.  This is a good practice for larger test suites.

**How to run:**

1.  Make sure you have `pytest` installed (`pip install pytest`).
2.  Save the code as a Python file (e.g., `test_categories.py`).
3.  Run `pytest test_categories.py` from your terminal.


This improved test suite provides more robust and comprehensive coverage of the `filter_parent_categories` and `filter_child_categories` functions. Remember to adapt the import paths (`hypotez.src...`) to match your actual project structure. Remember to replace `hypotez.src...` with the correct path to your models module.