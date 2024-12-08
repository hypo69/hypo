rst
How to use the AliCampaignEditor class
========================================================================================

Description
-------------------------
This code defines the `AliCampaignEditor` class, which is used to manage and edit advertising campaigns on AliExpress.  It provides methods for updating campaign properties, product details within categories, deleting products, retrieving categories, and listing all categories.  The class inherits from `AliPromoCampaign` and uses various helper functions for file manipulation, data loading, and JSON handling.


Execution steps
-------------------------
1. **Initialization (`__init__`)**: The `__init__` method initializes the `AliCampaignEditor` object. It takes the campaign name, language, and currency as input.  It also optionally loads existing campaign data from a JSON file.
2. **Product Deletion (`delete_product`)**: This method checks if a product with a given ID exists in a `sources.txt` file. If found, it removes the product from the list and saves the updated list.  If not found, it renames the product's corresponding file to add an underscore to avoid deleting the file.
3. **Product Update (`update_product`)**: This method updates product details within a specified category. It takes the category name, language, and product data (as a dictionary) as input.  It then calls the `dump_category_products_files` method to update the category with the new product details.
4. **Campaign Update (`update_campaign`)**: This method updates campaign properties like descriptions and tags.
5. **Category Update (`update_category`)**: This method updates the category data in a JSON file.  It reads the existing data, updates the specific category object, and then saves the updated JSON.
6. **Category Retrieval (`get_category`)**: This method retrieves a category by its name from the campaign's internal representation. It returns a `SimpleNamespace` object containing the category details, or `None` if the category is not found.
7. **Category Listing (`list_categories`)**: This method returns a list of all categories in the campaign.
8. **Product Retrieval (`get_category_products`)**: This method retrieves product data from JSON files associated with a given category. It constructs the file path, reads the JSON files, converts the data into `SimpleNamespace` objects, and returns the list of products. If no JSON files are found, it calls `process_category_products` to trigger the preparation of category products and then returns `None`.

Usage example
-------------------------
.. code-block:: python

    from pathlib import Path
    from hypotez.src.suppliers.aliexpress.campaign.ali_campaign_editor import AliCampaignEditor
    from types import SimpleNamespace


    # Example usage for deleting a product
    campaign_name = "Summer Sale"
    editor = AliCampaignEditor(campaign_name=campaign_name, language="EN", currency="USD")
    product_id_to_delete = "12345"
    editor.delete_product(product_id_to_delete)


    # Example usage for updating a category
    category_name_to_update = "Electronics"
    updated_category_data = SimpleNamespace(name=category_name_to_update, description="New description")
    json_path = Path("campaign_data.json")
    success = editor.update_category(json_path, updated_category_data)
    if success:
        print("Category updated successfully.")
    else:
        print("Failed to update category.")

    # Example usage for retrieving a list of categories
    categories = editor.list_categories
    if categories:
        print("Categories:", categories)
    else:
        print("No categories found.")