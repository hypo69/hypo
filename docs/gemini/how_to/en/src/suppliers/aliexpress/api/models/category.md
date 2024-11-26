## How to use the `Category` and `ChildCategory` classes in `aliexpress/api/models/category.py`

This guide describes how to use the `Category` and `ChildCategory` classes defined in the `aliexpress/api/models/category.py` file.

**`Category` Class**

This class represents a general category.  It has two attributes:

*   `category_id`: An integer representing the unique identifier of the category.
*   `category_name`: A string containing the name of the category.

**Example Usage (Category):**

```python
from hypotez.src.suppliers.aliexpress.api.models.category import Category

# Create a Category object
electronics_category = Category(category_id=123, category_name="Electronics")

# Access attributes
print(electronics_category.category_id)  # Output: 123
print(electronics_category.category_name)  # Output: Electronics
```

**`ChildCategory` Class**

This class represents a child category, inheriting from the `Category` class.  It adds an additional attribute:

*   `parent_category_id`: An integer representing the unique identifier of the parent category.

**Example Usage (ChildCategory):**

```python
from hypotez.src.suppliers.aliexpress.api.models.category import ChildCategory

# Create a ChildCategory object
smartphone_category = ChildCategory(
    category_id=456,
    category_name="Smartphones",
    parent_category_id=123
)

# Access attributes
print(smartphone_category.category_id)  # Output: 456
print(smartphone_category.category_name)  # Output: Smartphones
print(smartphone_category.parent_category_id)  # Output: 123
```

**Important Considerations:**

*   **Initialization:**  The examples show how to create instances of these classes.  Remember to pass the correct data types (integers for IDs, strings for names).
*   **Error Handling:**  The code does not include error handling.  In a real application, you might want to add checks to ensure the data being passed is valid (e.g., checking for `None` or invalid data types).
*   **Data Source:**  This code assumes you're getting the data from somewhere else (e.g., an API call, database query).  You'll need to implement that logic to populate the `category_id`, `category_name`, and `parent_category_id` attributes.
*   **`__init__` Method (Implied):**  The code defines the attributes as class variables.  However, a proper `__init__` method should be used in practice to initialize these attributes when an object is created:
```python
class Category:
    def __init__(self, category_id, category_name):
        self.category_id = category_id
        self.category_name = category_name
```
Add the appropriate `__init__` method to the `ChildCategory` class as well.

This updated guide now clarifies the implied initialization methods and emphasizes the need for data validation and error handling in real-world applications.