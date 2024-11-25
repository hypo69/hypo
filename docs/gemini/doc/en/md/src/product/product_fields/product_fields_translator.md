# hypotez/src/product/product_fields/product_fields_translator.py

## Overview

This module provides functions for translating product fields to the languages of the client database. It handles the conversion of product field data from the provider's system (likely PrestaShop) to the client's database format, ensuring accurate language mappings.  The module leverages a schema of client languages to determine the correct language identifiers.

## Table of Contents

* [rearrange_language_keys](#rearrange-language-keys)
* [translate_presta_fields_dict](#translate-presta-fields-dict)


## Functions

### `rearrange_language_keys`

**Description**: This function updates language identifiers in the `presta_fields_dict` based on the provided `page_lang` and `client_langs_schema`.  It searches for a matching language ID in the schema based on different locale formats (locale, iso_code, language_code).

**Parameters**:

- `presta_fields_dict` (dict): A dictionary containing product fields, potentially with nested language information.
- `client_langs_schema` (list | dict): A list or dictionary representing the client's language schema.  This provides the mapping from language codes to IDs.
- `page_lang` (str): The language code of the current page.

**Returns**:

- dict: The updated `presta_fields_dict` with potentially updated language IDs.


### `translate_presta_fields_dict`

**Description**: Translates multilingual product fields to the client's database format.  It takes the product fields, the client's language schema, and the page language as input.  It fetches pre-existing translations from the database and updates the fields to use the correct client language IDs.  It handles cases where the translation isn't found in the database and adds it as a new record.

**Parameters**:

- `presta_fields_dict` (dict): A dictionary containing product fields, potentially with nested language information (as expected from PrestaShop).
- `client_langs_schema` (list | dict): A list or dictionary representing the client's language schema.
- `page_lang` (str, optional): The language code of the current page. Defaults to `None` (attempts to infer from the data).

**Returns**:

- dict: The updated `presta_fields_dict` with translated fields.

**Raises**:

- `ProductFieldException`: Potentially raised during database interactions or translation process.


**Important Notes**:

- The code relies on external modules (`gs`, `pprint`, `logger`, and others) that are not included in this snippet.  These dependencies need to be considered for actual implementation.
- The `get_translations_from_presta_translations_table` and `insert_new_translation_to_presta_translations_table` functions are assumed to exist elsewhere and perform database interactions.
- The code assumes a specific structure for `presta_fields_dict` and `client_langs_schema`.
- Error handling (`try...except`) is used, but it should be extended to capture and log more specific errors and handle edge cases, including data validation.
- The handling of `page_lang` is potentially flawed.  It should have a more robust way of checking for language (e.g., using an ISO-standard language list instead of relying on different language codes.
- The use of `client_lang['iso_code'] in translated_record.locale` for translation matching is not ideal. It's better to have a more controlled mapping, especially if the `locale` attribute is not properly structured.