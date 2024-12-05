rst
How to use the bangood module
========================================================================================

Description
-------------------------
This Python module (`hypotez/src/suppliers/bangood/__init__.py`) initializes the Banggood supplier. It defines a `MODE` constant and imports necessary classes and functions from submodules within the `bangood` package. This setup enables access to functions for retrieving Banggood product data.

Execution steps
-------------------------
1. The module sets a `MODE` variable, likely for operational configuration (e.g., 'dev', 'prod').
2. It imports the `Graber` class and the functions `get_list_categories_from_site` and `get_list_products_in_category` from the submodules `.graber` and `.scenario`, respectively.  These likely contain the actual code for interacting with the Banggood API or website.

Usage example
-------------------------
.. code-block:: python

    from hypotez.src.suppliers.bangood import Graber, get_list_categories_from_site, get_list_products_in_category

    # Example usage to retrieve categories
    categories = get_list_categories_from_site()
    print(categories)  # Output will be a list of Banggood categories


    # Example usage to retrieve products within a specific category (assuming you have a category ID)
    category_id = 123  # Replace with a valid category ID
    products = get_list_products_in_category(category_id)
    print(products)  # Output will be a list of product details

    # Example of creating a Graber object (if needed)
    graber_instance = Graber()

    # Further actions using the 'graber_instance' depend on the implementation in the .graber module
    # Example (assuming a method exists to fetch a product):
    # product_details = graber_instance.fetch_product(product_id)