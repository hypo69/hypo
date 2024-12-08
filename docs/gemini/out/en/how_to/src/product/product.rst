rst
How to use the Product class
========================================================================================

Description
-------------------------
This Python code defines a `Product` class for interacting with a website, a product, and the PrestaShop API. It handles product data manipulations and interacts with the PrestaShop API.  The `Product` class inherits from `ProductFields` and `PrestaShop`, combining functionalities for product data and PrestaShop API interaction.  It also includes a static method `get_parent_categories` to retrieve parent categories of a given product category.

Execution steps
-------------------------
1. **Import necessary modules:** The code imports modules like `header`, `gs`, `PrestaShop`, `Category`, `ProductFields`, and `logger` from different parts of the project. This ensures the necessary functionalities are available for use.

2. **Define the Product class:** The `Product` class inherits from `ProductFields` and `PrestaShop`.  This is a crucial step for combining functionality for product data access and PrestaShop API interactions.

3. **Initialize the Product object:** The `__init__` method initializes the `Product` object, inheriting the initialization logic from the parent classes.  The rest of the `__init__` method is not shown, but it would likely handle setting up the necessary attributes.


4. **Implement the static method `get_parent_categories`:** This method is designed to retrieve the parent categories of a given product category.

   a. **Input Validation:** It checks if the `id_category` parameter is an integer using `isinstance()`.  If not, it raises a `TypeError`, preventing unexpected behavior.

   b. **Data Retrieval:** It calls the `get_parents` method of the `Category` class, providing the `id_category` and `dept` as parameters to retrieve the parent category information.

5. **Error Handling:** The code includes a `TypeError` if the input `id_category` is not an integer. This is important for robustness in handling unexpected input.


Usage example
-------------------------
.. code-block:: python

    from hypotez.src.product.product import Product
    from hypotez.src.category import Category

    # Example usage to get parent categories for category ID 123.
    try:
        parent_categories = Product.get_parent_categories(123)
        print(f"Parent categories for category 123: {parent_categories}")
    except TypeError as e:
        print(f"Error: {e}")

    # Example of creating a Product object (assuming other necessary imports and setup)
    # my_product = Product(...)