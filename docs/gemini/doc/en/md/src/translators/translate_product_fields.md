# Module: hypotez/src/translators/translate_product_fields.py

## Overview

This module provides functions for translating product fields. It interacts with a database (PrestaShop translations table) to retrieve existing translations, insert new ones, and utilizes an AI translation service (`translate`).

## Functions

### `get_translations_from_presta_translations_table`

**Description**: Retrieves translations for a specific product from the PrestaShop translations table.

**Parameters**:
- `product_reference` (str): The reference ID of the product to retrieve translations for.
- `credentials` (dict): Dictionary containing credentials for database connection.
- `i18n` (Optional[str], optional): The target locale (e.g., "en_EN", "he_HE"). Defaults to `None`.


**Returns**:
- `list`: A list of dictionaries, each representing a translation record for a specific field of the product. Returns an empty list if no translations are found.

**Raises**:
- `Exception`: Any exception related to database interaction or other issues.


### `insert_new_translation_to_presta_translations_table`

**Description**: Inserts a new translation record into the PrestaShop translations table.

**Parameters**:
- `record` (dict): The dictionary containing the translation data to be inserted.
- `credentials` (dict): Dictionary containing credentials for database connection.


**Returns**:
- `None`: This function does not return a value.

**Raises**:
- `Exception`: Any exception related to database interaction or other issues.


### `translate_record`

**Description**: Translates the fields of a product record from one locale to another.

**Parameters**:
- `record` (dict): The dictionary containing the product record to be translated.
- `from_locale` (str): The source locale for translation.
- `to_locale` (str): The target locale for translation.


**Returns**:
- `dict`: The translated record.

**Raises**:
- `Exception`: Any exception related to the AI translation service (`translate`) or other issues.


## Classes

(No classes are defined in the provided code snippet.)