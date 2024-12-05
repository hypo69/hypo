rst
How to use the `Category` and `ChildCategory` classes
========================================================================================

Description
-------------------------
This code defines two classes, `Category` and `ChildCategory`, likely representing categories and subcategories on AliExpress.  The `Category` class stores basic category information (ID and name). The `ChildCategory` class inherits from `Category`, adding a `parent_category_id` field to link subcategories to their parent categories.

Execution steps
-------------------------
1. The `Category` class is defined with attributes `category_id` (an integer) and `category_name` (a string).  These attributes represent fundamental information about a category.

2. The `ChildCategory` class inherits from `Category`, meaning it automatically gets the `category_id` and `category_name` attributes.

3. The `ChildCategory` class extends the base `Category` class by adding a new attribute `parent_category_id` which specifies the ID of the parent category for a subcategory.

Usage example
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.aliexpress.api.models.category import Category, ChildCategory

    # Example creating a main category
    main_category = Category(category_id=1, category_name="Electronics")

    # Example creating a subcategory
    sub_category = ChildCategory(
        category_id=2,
        category_name="Smartphones",
        parent_category_id=1
    )

    print(main_category.category_name)  # Output: Electronics
    print(sub_category.category_name)   # Output: Smartphones
    print(sub_category.parent_category_id)  # Output: 1