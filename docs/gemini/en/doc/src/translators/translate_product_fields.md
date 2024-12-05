# translate_product_fields.py

## Overview

This module provides functions for managing translations of product fields. It acts as a bridge between a product field dictionary, a translation table (likely a database), and translation services. It handles fetching translations from a PrestaShop database, inserting new translations, and translating individual product field records.

## Functions

### `get_translations_from_presta_translations_table`

**Description**: This function retrieves translations from the PrestaShop translation table based on a product reference.

**Parameters**:

- `product_reference` (str): The unique identifier of the product.
- `credentials` (dict): Dictionary containing credentials for database connection (e.g., username, password, database name).
- `i18n` (Optional[str], optional): The target language code (e.g., "en_EN", "he_HE", "ru-RU"). Defaults to `None`.

**Returns**:

- `list`: A list of dictionaries containing the retrieved translations.  Returns an empty list if no matching translations are found.

**Raises**:

- `Exception`:  An exception is raised if there's an error connecting to or querying the database.


### `insert_new_translation_to_presta_translations_table`

**Description**: This function inserts a new translation record into the PrestaShop translation table.

**Parameters**:

- `record` (dict): The translation record to insert.
- `credentials` (dict): Dictionary containing credentials for database connection (e.g., username, password, database name).

**Returns**:

- `None`: This function does not return a value.

**Raises**:

- `Exception`: An exception is raised if there's an error inserting the record into the database.


### `translate_record`

**Description**: This function translates a product field record from one language to another using a translation service.

**Parameters**:

- `record` (dict): The product field record to translate.
- `from_locale` (str): The source language code.
- `to_locale` (str): The target language code.

**Returns**:

- `dict`: The translated product field record.

**Raises**:

- `Exception`: An exception is raised if there's an error during translation. Note the expected error handling now uses `Exception` (not unspecified, as in the original).


## Classes

(If any classes are present in the file, document them here)


## Modules Used

- `pathlib`
- `typing`
- `src.gs`
- `src.utils.printer`
- `src.product.product_fields.product_fields`
- `src.db` (likely a database interaction module)
- `src.ai` (likely a translation service module)
- `src.endpoints.PrestaShop`