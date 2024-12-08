How to use the Aliexpress Category Management Module
=========================================================================================

Description
-------------------------
This module provides functionality for working with product categories on the Aliexpress platform. It includes functions for retrieving product links within a category, updating categories based on website data, and database operations.  It handles retrieving product lists, updating category information, and interacting with a database.


Execution steps
-------------------------
1. **Initialization:**  Import the necessary modules and create an instance of the `Supplier` object.  This object likely contains configuration details for interacting with Aliexpress.  Also, establish a database connection if needed.

2. **Data Retrieval (from Aliexpress):** Use the `get_list_categories_from_site` function to retrieve the list of categories from the Aliexpress website.  Optionally, filter by a specific brand using the `brand` parameter. This function likely leverages the `Supplier` object for authentication and data fetching.

3. **Category Update (optional):** If category updates are needed, use `update_categories_in_scenario_file` to compare the retrieved data with the information in your `scenario_file`.  This function updates the `scenario_file` with the latest information.

4. **Product List Retrieval (optional):** To get product links within a specific category, use `get_list_products_in_category`. Provide the `Supplier` object as input.


5. **Database Interactions:** Employ the `DBAdaptor` class for database operations (e.g., insertion, updates, deletions). The `select` method is used to query, `insert`, `update` and `delete` to modify database entries. Provide necessary identifiers like `cat_id` or `parent_id` to target specific categories or products.

6. **Data Storage (optional):** Store the retrieved product data, updated categories, or database modifications in relevant databases and files as needed.


7. **Completion:**  The process concludes with successful database updates and/or files.


Usage example
-------------------------
.. code-block:: python

    # Import necessary modules.
    from your_module import Supplier, DBAdaptor, get_list_products_in_category, update_categories_in_scenario_file, get_list_categories_from_site

    # Create a Supplier instance (replace with actual configuration)
    supplier = Supplier()

    # Get categories from the site, optionally filtering by brand
    categories = get_list_categories_from_site(supplier, "scenario_file.json", brand="Nike")

    # Update the scenario file if needed
    update_categories_in_scenario_file(supplier, "scenario_file.json")


    # Get product list for a specific category (using a category ID example).
    products = get_list_products_in_category(supplier, cat_id=123)



    # Database interaction example (replace with appropriate parameters)
    db = DBAdaptor()
    db.select(cat_id=123)
    db.insert(data_to_insert)  # Replace with your data structure.
    db.update(data_to_update)  # Replace with data to update
    db.delete(id_to_delete) # Replace with the data identifier


    # ... further processing and storing of results ...