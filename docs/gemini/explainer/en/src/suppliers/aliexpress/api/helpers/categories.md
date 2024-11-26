```
## <input code>
```python
## \file hypotez/src/suppliers/aliexpress/api/helpers/categories.py
# -*- coding: utf-8 -*-\
#! venv/Scripts/python.exe # <- venv win
## ~~~~~~~~~~~~~
""" module: src.suppliers.aliexpress.api.helpers """

"""  функции для фильтрации категорий и подкатегорий API Aliexpress"""
from typing import List, Union
from .. import models
#from src.suppliers.aliexpress.api.api import models

def filter_parent_categories(categories: List[models.Category | models.ChildCategory]) -> List[models.Category]:
    """
    Filters and returns a list of categories that do not have a parent category.

    @param categories: List of category or child category objects.
    @return: List of category objects without a parent category.
    """
    filtered_categories = []
    
    if isinstance(categories, (str, int, float)):
        categories = [categories]  # Convert to list if a single non-category value is passed.

    for category in categories:
        if not hasattr(category, 'parent_category_id'):
            filtered_categories.append(category)

    return filtered_categories

def filter_child_categories(categories: List[models.Category | models.ChildCategory],
                            parent_category_id: int) -> List[models.ChildCategory]:
    """
    Filters and returns a list of child categories that belong to the specified parent category.

    @param categories: List of category or child category objects.
    @param parent_category_id: The ID of the parent category to filter child categories by.
    @return: List of child category objects with the specified parent category ID.
    """
    filtered_categories = []
    
    if isinstance(categories, (str, int, float)):
        categories = [categories]  # Convert to list if a single non-category value is passed.

    for category in categories:
        if hasattr(category, 'parent_category_id') and category.parent_category_id == parent_category_id:
            filtered_categories.append(category)

    return filtered_categories
```

```
## <algorithm>

**filter_parent_categories**

1. **Input:** `categories` (list of `models.Category` or `models.ChildCategory` objects)
   * Example: `[category1, category2, childCategory1]`


2. **Check for invalid input:** If `categories` is not a list, convert it to a list. 
   * Example: `categories = [123]`

3. **Iterate:** Loop through each `category` in the input list.
   * Example: Iterates through `category1`, `category2`, `childCategory1`
4. **Check for parent_category_id:** Check if the `category` object has a `parent_category_id` attribute.
   * Example: `category1` might not have `parent_category_id`, `childCategory1` has `parent_category_id`.

5. **Append to filtered list:** If `parent_category_id` is absent, append the `category` to `filtered_categories`.
   * Example: `category1` is appended.

6. **Return:** Return the `filtered_categories` list.
   * Example: `[category1]`


**filter_child_categories**

1. **Input:** `categories` (list of `models.Category` or `models.ChildCategory` objects), `parent_category_id` (integer).
   * Example: `[childCategory1, childCategory2, category1]`, `123`

2. **Check for invalid input:** If `categories` is not a list, convert it to a list.
   * Example: `categories = 456` => `categories = [456]`

3. **Iterate:** Loop through each `category` in the input list.
   * Example: Iterates through `childCategory1`, `childCategory2`, `category1`.

4. **Check for parent_category_id:** Check if the `category` object has a `parent_category_id` attribute.
   * Example: `category1` does, `childCategory2` has.

5. **Compare ID:**  Check if the `category`'s `parent_category_id` matches the provided `parent_category_id`.
   * Example: `childCategory1` might have a `parent_category_id` of `123`, while `parent_category_id` in input is `123`. `childCategory2` has different id, so skipped.


6. **Append to filtered list:** If the `parent_category_id` matches, append the `category` to `filtered_categories`.
   * Example: `childCategory1` is appended.

7. **Return:** Return the `filtered_categories` list.
   * Example: `[childCategory1]`


```

```
## <explanation>

**Imports:**

- `from typing import List, Union`: Imports necessary typing information for type hinting, specifically for defining lists (`List`) and union types (`Union`).  This improves code readability and maintainability by explicitly specifying the expected types of variables.
- `from .. import models`: Imports the `models` module from a parent directory. This implies that there's a `models.py` file (or similar) in the `hypotez/src/suppliers/aliexpress/api` directory containing definitions for category and child category models. The `..` notation indicates going up two directories. This is standard Python import practice and is important for maintaining a structured project.


**Classes (implied):**

- `models.Category`: A class representing a category. We can infer this exists based on the `models.Category` usage in the code.  The code relies on this class having the `parent_category_id` attribute.
- `models.ChildCategory`: A class representing a child category. We can infer this exists based on the `models.ChildCategory` usage in the code. The code relies on this class having the `parent_category_id` attribute.


**Functions:**

- `filter_parent_categories(categories: List[models.Category | models.ChildCategory]) -> List[models.Category]`:
    - Takes a list of category or child category objects as input.
    - Filters the input list to return only the categories without a parent category.
    - Includes input validation to handle cases where input is not a list, converting it to a list of one element if needed.
    - **Example:** If `categories = [category1, childCategory1]`, where `category1` does not have a `parent_category_id` and `childCategory1` does, it would return `[category1]`.
- `filter_child_categories(categories: List[models.Category | models.ChildCategory], parent_category_id: int) -> List[models.ChildCategory]`:
    - Takes a list of category or child category objects and a `parent_category_id` as input.
    - Filters the input list to return only the child categories that belong to the specified `parent_category_id`.
    - Includes input validation to handle cases where input is not a list, converting it to a list of one element if needed.
    - **Example:** If `categories = [childCategory1, childCategory2, category1]` and `parent_category_id = 123`, and only `childCategory1` has `parent_category_id=123`, it would return `[childCategory1]`.


**Variables:**

- `filtered_categories`:  A list used to accumulate the results of the filtering operations.


**Potential Errors/Improvements:**

- **Type Safety:**  While the code uses type hinting, the import of `models` isn't fully explicit. It depends on the `models` module having the expected classes and attributes.
- **Robustness:**  There's no error handling for cases where a `category` object might not have the expected attributes. For example,  if a list contains something other than a Category or ChildCategory object. The code would crash with an AttributeError.


**Relationships with other project parts:**

This code relies on the `models` module to provide the correct type definition and the existence of `Category` and `ChildCategory` classes. This suggests a close relationship with other parts of the project that work with category data, most likely the API client (`src.suppliers.aliexpress.api.api`).  The code is part of a larger system responsible for working with `aliexpress` supplier data.