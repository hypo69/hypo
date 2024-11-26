How to use the `categories.py` module for filtering AliExpress API categories

This module, `categories.py`, provides functions for filtering categories and subcategories retrieved from the AliExpress API.  It's designed to work with `models.Category` and `models.ChildCategory` objects, which are likely defined elsewhere (e.g., in a `models.py` file).

**Essential Concepts:**

* **`models.Category`:** Represents a top-level category.
* **`models.ChildCategory`:** Represents a subcategory within a parent category.  Crucially, it has a `parent_category_id` attribute.

**Functions:**

1. **`filter_parent_categories(categories: List[models.Category | models.ChildCategory]) -> List[models.Category]`**

   This function filters a list of categories (or child categories) to return only the top-level categories (i.e., those without a parent).

   ```python
   from your_module import categories  # Import the categories module
   from your_module import models  # Assuming models are in the same directory

   # Example Usage (assuming you have a list of categories/child categories named 'all_categories'):
   parent_categories = categories.filter_parent_categories(all_categories)

   for category in parent_categories:
       print(category.name)  # Access the name attribute of the category object
   ```

   * **Input:** A list of `models.Category` or `models.ChildCategory` objects.  **Important:**  This function accepts a single category/child category as input, too. It will convert this to a list, preventing errors when a single item is provided instead of a list.
   * **Output:** A list containing only the `models.Category` objects that have no parent.
   * **Error Handling:** Handles cases where the input is not a list by converting it to a list.

2. **`filter_child_categories(categories: List[models.Category | models.ChildCategory], parent_category_id: int) -> List[models.ChildCategory]`**

   This function filters a list of categories/child categories to return only the child categories belonging to a specific parent category.

   ```python
   from your_module import categories  # Import the categories module
   from your_module import models  # Assuming models are in the same directory

   # Example Usage:
   parent_id = 123  # The ID of the parent category
   child_categories = categories.filter_child_categories(all_categories, parent_id)

   for category in child_categories:
       print(category.name)  # Access the name of the child category
       print(category.parent_category_id)  # Verify the parent ID matches
   ```

   * **Input:**
      * A list of `models.Category` or `models.ChildCategory` objects.
      * `parent_category_id`: An integer representing the ID of the parent category to filter by.
   * **Output:** A list of `models.ChildCategory` objects whose `parent_category_id` matches the input.
   * **Error Handling:** Handles cases where the input is not a list by converting it to a list.

**Crucial Considerations (for completeness):**

* **Import Statements:**  Ensure you have the correct import statements to access the `models` objects (`from .. import models`).  Adjust the import path (`from .. import models`) if necessary based on your project structure.
* **`models` Definition:** The provided code assumes you have `models.Category` and `models.ChildCategory` classes defined. Verify that these classes exist and have the required attributes (like `name` and `parent_category_id`).
* **Data Structure:** The code assumes that the data provided to these functions comes from the AliExpress API in a structured way.  It's good practice to use type hints (`List[models.Category | models.ChildCategory]`) to explicitly define the expected input data.
* **Error Handling:** The code handles cases where the input is not a list, but adding more robust error handling (e.g., checking for `None` or empty lists) would make it more resilient.


By following these guidelines, you can effectively use the `categories.py` module to extract specific categories from your AliExpress API data. Remember to replace placeholders like `your_module` with your actual module names.