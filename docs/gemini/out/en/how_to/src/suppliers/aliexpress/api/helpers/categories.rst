rst
How to use the category filtering functions
========================================================================================

Description
-------------------------
This Python code defines two functions for filtering categories and child categories from a list of category objects.  `filter_parent_categories` identifies categories without parent relationships, and `filter_child_categories` finds child categories associated with a specific parent category ID.  It includes error handling to gracefully manage various input types, including a single value (rather than a list) being passed in.


Execution steps
-------------------------
1. **Import necessary modules:**  The code imports `List`, `Union`, and `models` from a module (likely referring to a category model). The crucial point is that these `models` (representing categories and child categories) are defined elsewhere.

2. **Define `filter_parent_categories`:** This function takes a list of `Category` or `ChildCategory` objects (`categories`) as input.
   - It initializes an empty list called `filtered_categories`.
   - It handles the case where the input `categories` is not a list, converting it into a list for processing.
   - It iterates through each `category` in the input list.
   - It checks if the current `category` object has a `parent_category_id` attribute. If not, it appends the `category` to the `filtered_categories` list.
   - Finally, it returns the `filtered_categories` list.


3. **Define `filter_child_categories`:** This function also takes a list of category or child category objects and a parent category ID.
   - It initializes an empty list called `filtered_categories`.
   - It handles the case where the input `categories` is not a list.
   - It iterates through each `category` in the input `categories`.
   - It checks if the current `category` object has a `parent_category_id`.
   - It checks if the `parent_category_id` of the current `category` matches the input `parent_category_id`.  If it does, the category is added to the `filtered_categories` list.
   - Finally, it returns the `filtered_categories` list.


Usage example
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.api.helpers import categories
    from hypotez.src.suppliers.aliexpress.api import models

    # Example usage (assuming you have defined models.Category and models.ChildCategory)
    # Create some example category objects
    cat1 = models.Category(id=1, name="Electronics")
    cat2 = models.Category(id=2, name="Clothing")
    child1 = models.ChildCategory(id=3, name="Phones", parent_category_id=1)
    child2 = models.ChildCategory(id=4, name="Shirts", parent_category_id=2)
    child3 = models.ChildCategory(id=5, name="Shoes", parent_category_id=2)
    
    all_categories = [cat1, cat2, child1, child2, child3]

    # Get parent categories
    parent_cats = categories.filter_parent_categories(all_categories)
    print("Parent Categories:")
    for cat in parent_cats:
        print(f"  {cat.name}")
    
    # Get child categories for a specific parent
    child_cats_of_electronics = categories.filter_child_categories(all_categories, 1)
    print("\nChild Categories for Electronics:")
    for child_cat in child_cats_of_electronics:
        print(f"  {child_cat.name}")

    #IlluStarting error handling (non-list input):
    single_category = models.Category(id=6, name="Books")
    filtered_single = categories.filter_parent_categories(single_category)
    print(f"\nFiltering a single category: {filtered_single}")