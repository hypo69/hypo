# hypotez/src/translators/product_translator.py

## Overview

This module handles translation management. It acts as a bridge between product field dictionaries, translation tables, and translators.  It provides functions for retrieving translations from the PrestaShop translation table, inserting new translations, and translating records.

## Functions

### `get_translations_from_presta_translations_table`

**Description**: This function retrieves translations from the PrestaShop translation table for a given product reference and locale.

**Parameters**:
- `product_reference` (str): The reference of the product for which to fetch translations.
- `i18n` (str, optional): The locale (e.g., `en_EN`, `he_HE`, `ru-RU`). Defaults to None.

**Returns**:
- `list`: A list containing translation records matching the specified `product_reference` and locale.  Returns an empty list if no records are found or if there's an issue with the database query.

**Raises**:
- `Exception`: Any database-related exceptions during the query.

### `insert_new_translation_to_presta_translations_table`

**Description**: This function inserts a new translation record into the PrestaShop translation table.

**Parameters**:
- `record` (dict): A dictionary containing the data to be inserted into the translation table.

**Returns**:
- None (void).

**Raises**:
- `Exception`: Any database-related exceptions during the insertion process.

### `translate_record`

**Description**: This function translates a record from one locale to another using the OpenAI translation API.

**Parameters**:
- `record` (dict): The record to be translated.
- `from_locale` (str): The original locale of the record.
- `to_locale` (str): The target locale for translation.


**Returns**:
- `dict`: The translated record.

**Raises**:
- `Exception`: Any exception arising during the translation process, including issues with the OpenAI API or data formatting.