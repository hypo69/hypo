rst
How to use the `get_translations_from_presta_translations_table` function
===========================================================================

Description
-------------------------
This function retrieves translations for product fields from a PrestaShop translations table.  It takes a product reference and an i18n code (e.g., 'en_EN', 'ru-RU') as input and returns a list of translation records.  If no translations are found for the given product and i18n code, an empty list will be returned.

Execution steps
-------------------------
1. **Import necessary modules**: The code imports necessary modules for database interaction, logging, and handling JSON data.

2. **Define the function `get_translations_from_presta_translations_table`**: This function accepts a `product_reference` (string) and an optional `i18n` string (e.g., 'en_EN', 'he_HE', 'ru-RU') as input.

3. **Establish database connection**: The function uses a `ProductTranslationsManager` context manager to create a connection to the database. This ensures the connection is properly closed after use.

4. **Construct query filter**: It creates a dictionary (`search_filter`) to specify the criteria for selecting translations from the database. This filter looks for a record matching the given `product_reference`.

5. **Execute query**: The `translations_manager.select_record` method executes the query, retrieving matching translations from the database.

6. **Return translations**: The function returns the retrieved `product_translations` as a list.


Usage example
-------------------------
.. code-block:: python

    from hypotez.src.translators.product_translator import get_translations_from_presta_translations_table

    # Replace with your actual product reference and i18n code
    product_reference = "12345"
    i18n_code = "en_EN"

    try:
        translations = get_translations_from_presta_translations_table(product_reference, i18n_code)
        if translations:
            print("Translations found:")
            for translation in translations:
                print(translation)
        else:
            print("No translations found for this product and locale.")
    except Exception as e:
        print(f"An error occurred: {e}")