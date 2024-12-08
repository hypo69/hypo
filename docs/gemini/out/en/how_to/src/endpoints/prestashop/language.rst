rst
How to use the PrestaLanguage class
========================================================================================

Description
-------------------------
This Python code defines a `PrestaLanguage` class, which extends the `PrestaShop` class.  It provides methods for managing languages within a PrestaShop store via its API.  The class handles initialization with API credentials, and offers methods to add, delete, update, and retrieve language details.  It also validates that both `api_domain` and `api_key` are provided during initialization.


Execution steps
-------------------------
1. **Import necessary modules:** The code imports `PrestaShop`, `gs`, `pprint`, `header`, `logger`, `PrestaShopException`, `SimpleNamespace`, and `Optional` from various modules within the project.

2. **Define the `PrestaLanguage` class:** This class inherits from `PrestaShop`, indicating it uses the underlying API functions for interaction with PrestaShop.

3. **`__init__` method (Initialization):**
    - Takes optional `credentials` (dict or SimpleNamespace), `api_domain`, and `api_key` as arguments.
    - Extracts `api_domain` and `api_key` from `credentials` if provided.
    - **Validation:** Checks if both `api_domain` and `api_key` are provided; raises a `ValueError` if either is missing.
    - Calls the `__init__` method of the parent `PrestaShop` class to set up the API connection.

4. **Methods for language management:** The class includes methods:
    - `add_language_PrestaShop()`: Adds a new language to PrestaShop.
    - `delete_language_PrestaShop()`: Deletes a language from PrestaShop.
    - `update_language_PrestaShop()`: Updates an existing language.
    - `get_language_details_PrestaShop()`: Retrieves details about a specific language.


Usage example
-------------------------
.. code-block:: python

    from hypotez.src.endpoints.prestashop.language import PrestaLanguage
    from types import SimpleNamespace


    # Example credentials (replace with your actual credentials)
    credentials = SimpleNamespace(api_domain="your-api-domain", api_key="your-api-key")


    try:
        prestalanguage = PrestaLanguage(credentials=credentials)
        # Add a language
        prestalanguage.add_language_PrestaShop('English', 'en')
        # Update a language
        prestalanguage.update_language_PrestaShop(4, 'Updated Language Name')
        # Delete a language
        prestalanguage.delete_language_PrestaShop(3)
        # Get language details (replace 5 with the appropriate language ID)
        language_details = prestalanguage.get_language_details_PrestaShop(5)
        print(language_details)  # Output the retrieved language details
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")