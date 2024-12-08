rst
How to use the `translate_product_fields.py` module
=========================================================================================

Description
-------------------------
This module provides functions for managing translations of product fields.  It connects to a PrestaShop translation database, retrieves translations for a given product, inserts new translations, and handles the translation process using an external AI translation service.  The module utilizes classes and functions to encapsulate database interactions, translation logic, and external API calls.

Execution steps
-------------------------
1. **Retrieve translations:** The `get_translations_from_presta_translations_table` function retrieves product translations from the PrestaShop database.
    - It takes the `product_reference` (a unique identifier for the product), `credentials` (database connection details), and an optional `i18n` parameter (language code) as input.
    - It constructs a search filter to query the database for translations matching the `product_reference`.
    - It uses `ProductTranslationsManager` (presumably a custom class) to perform the database query.
    - It returns a list of dictionaries containing the retrieved translations.

2. **Insert new translations:** The `insert_new_translation_to_presta_translations_table` function inserts a new translation record into the PrestaShop database.
    - It takes the translation record (`record`) and database credentials (`credentials`) as input.
    - It uses `ProductTranslationsManager` to execute the insertion.

3. **Translate a record:** The `translate_record` function translates the fields of a product record using the external AI translation service.
    - It takes the product record (`record`), the source language (`from_locale`), and the target language (`to_locale`) as input.
    - It calls the `translate` function (likely from the `src.ai` module) to perform the translation.
    - It returns the translated record.  Crucially, the code currently has an ellipsis (`...`) indicating missing post-translation processing.  This step needs to be handled in the implementation to update the translation records properly.


Usage example
-------------------------
.. code-block:: python

    from src.translators import translate_product_fields
    import json

    # Replace with your actual credentials and data.
    credentials = {
        'db_host': 'your_db_host',
        'db_user': 'your_db_user',
        'db_password': 'your_db_password',
        'db_name': 'your_db_name',
    }

    product_reference = 'your_product_reference'
    i18n = 'en_EN'

    try:
        translations = translate_product_fields.get_translations_from_presta_translations_table(
            product_reference, credentials, i18n
        )

        # Example usage: Print the translations
        print("Retrieved translations:")
        for translation in translations:
            print(json.dumps(translation, indent=4))


        # Example of inserting a new translation (replace with your record)
        new_record = {
            'product_reference': 'another_product',
            'field1': 'original_text',
            'i18n': 'ru_RU',
            'translation': 'перевод'  
        }
        translate_product_fields.insert_new_translation_to_presta_translations_table(new_record, credentials)


    except Exception as e:
        print(f"An error occurred: {e}")