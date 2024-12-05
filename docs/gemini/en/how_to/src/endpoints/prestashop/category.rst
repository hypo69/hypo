rst
How to use the `get_parent_categories_list` function
=========================================================================================

Description
-------------------------
This function retrieves a list of parent categories for a given category ID from a PrestaShop API. It recursively calls itself to traverse the category tree until it reaches the root category (id <= 2).  The function utilizes the PrestaShop API to fetch category data. It handles potential errors related to missing categories or invalid input.

Execution steps
-------------------------
1. **Input Validation:** Checks if the `id_category` is provided. If not, logs an error and returns the provided `parent_categories_list` (likely an empty list).

2. **API Call:** Fetches category data for the given `id_category` from the PrestaShop API using the `super().get('categories', ...)` method.  The `display='full'` parameter ensures that the necessary data (including `id_parent`) is retrieved.

3. **Error Handling:** Checks if the API call returned a valid category (`category`). If not, logs an error and returns `None` (or similar).

4. **Parent Category Retrieval:** Extracts the `id_parent` from the retrieved category data.

5. **Append to List:** Appends the extracted `id_parent` to the `parent_categories_list`.

6. **Recursive Call (if needed):** If the `id_parent` is greater than 2 (meaning it's not a root category), recursively calls `get_parent_categories_list` with the `id_parent` and the updated `parent_categories_list`.

7. **Root Category Check:** If the `id_parent` is less than or equal to 2 (root category), the function returns the `parent_categories_list` containing all the parent categories from the `id_category`.

8. **Return Value:** Returns the `parent_categories_list` containing all the parent category IDs from the given category ID.


Usage example
-------------------------
.. code-block:: python

    from hypotez.src.endpoints.prestashop.category import PrestaCategory

    # Replace with your actual API credentials
    API_DOMAIN = "your_api_domain"
    API_KEY = "your_api_key"

    prestacategory = PrestaCategory(API_DOMAIN=API_DOMAIN, API_KEY=API_KEY)

    try:
        category_id = 5
        parent_categories = prestacategory.get_parent_categories_list(category_id)
        if parent_categories:
            print(f"Parent categories for category {category_id}: {parent_categories}")
        else:
            print(f"No parent categories found for category {category_id}.")

    except ValueError as e:
        print(f"Error: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")