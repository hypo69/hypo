rst
How to use the `product_fields_translator.py` code block
==========================================================================================

Description
-------------------------
This Python code defines functions for translating product fields from a PrestaShop format to a format compatible with a client database.  It handles cases where the product data needs translation based on the language of the client's database and the product page. It utilizes a schema of client languages to map PrestaShop language codes to client database language IDs. It also manages situations where translations are not found in the database, inserting new translations if necessary.


Execution steps
-------------------------
1. **Input Data Preparation:**
   The function `translate_presta_fields_dict` receives three primary inputs:
     - `presta_fields_dict`: A dictionary containing product fields, typically in a format from a PrestaShop API.  The key part is that it needs a nested structure with a `language` key containing arrays with a nested `attrs` key and `id`.
     - `client_langs_schema`: A list or dictionary defining the client's available language codes and corresponding IDs. This provides the mapping for translation.
     - `page_lang` (Optional): The language code of the product page. If not provided, the function attempts to determine it from the `presta_fields_dict`.

2. **Language ID Retrieval:**
   The `rearrange_language_keys` function searches the `client_langs_schema` for a language matching the `page_lang`. It checks for several possible language codes (locale, ISO code, language code) to ensure robustness.

3. **Updating Language IDs:**
   If a matching `client_lang_id` is found, `rearrange_language_keys` updates the `id` attributes within the `presta_fields_dict`'s `language` structure. Critically, it ensures the `id` is a string.


4. **Translation from Database:**
   The `translate_presta_fields_dict` function calls `get_translations_from_presta_translations_table` to retrieve existing translations from the database, using the product reference (`presta_fields_dict['reference']`).


5. **Handling Missing Translations:**
    If no translation is found in the database for the specified product reference, the code will insert a new translation record into the database using a record function.


6. **Applying Existing Translations:**
    If translations exist in the database, the code iterates through the `enabled_product_translations` and `client_langs_schema`. It checks for matching `iso_code` within `translated_record.locale`. If a match is found, it updates the `presta_fields_dict` with the translated values for the corresponding language using the `client_lang['id']` to maintain consistency with the client's language schema.


7. **Error Handling:**
    The code includes error handling (using `try...except`) to catch and log potential exceptions during the translation process.

8. **Return Value:**
   The function returns the updated `presta_fields_dict` with translated fields.


Usage example
-------------------------
.. code-block:: python

    import json

    # Sample input data (replace with your actual data)
    presta_fields_dict = {
        "reference": "12345",
        "name": {
            "language": [
                {"attrs": {"id": "1"}, "value": "Product Name (PrestaShop)"},
            ]
        },
        # ... other fields
    }

    client_langs_schema = [
        {"id": 1, "iso_code": "en"},
        {"id": 2, "iso_code": "fr"},
    ]


    page_lang = "en"

    # Mock functions for demonstration
    def get_translations_from_presta_translations_table(reference):
        return [{"locale": "en", "name": "Product Name (Translation)"}]

    from hypotez.src.product.product_fields.product_fields_translator import translate_presta_fields_dict
    translated_data = translate_presta_fields_dict(presta_fields_dict, client_langs_schema, page_lang)
    print(json.dumps(translated_data, indent=2))