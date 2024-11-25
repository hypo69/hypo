# Module: hypotez/src/translators/product_translator.py

## Overview

This module provides functions for managing product translations. It acts as an intermediary between product field dictionaries, translation tables, and translation tools.  It facilitates retrieving, inserting, and translating product information.

## Table of Contents

- [Functions](#functions)
    - [`get_translations_from_presta_translations_table`](#get_translations_from_presta_translations_table)
    - [`insert_new_translation_to_presta_translations_table`](#insert_new_translation_to_presta_translations_table)
    - [`translate_record`](#translate_record)


## Functions

### `get_translations_from_presta_translations_table`

**Description**: Retrieves product translations from the PrestaShop translation table.

**Parameters**:
- `product_reference` (str): The reference of the product for which to retrieve translations.
- `i18n` (str, optional): The target language (e.g., "en_EN", "he_HE"). Defaults to `None`.


**Returns**:
- list: A list of dictionaries representing the retrieved translations. Returns an empty list if no translations are found or if an error occurs.


**Raises**:
- `Exception`: Any exception raised during database interaction.


### `insert_new_translation_to_presta_translations_table`

**Description**: Inserts a new product translation record into the PrestaShop translation table.


**Parameters**:
- `record` (dict): A dictionary containing the translation data to be inserted.


**Returns**:
- None


**Raises**:
- `Exception`: Any exception raised during database interaction.


### `translate_record`

**Description**: Translates a product record from one language to another.

**Parameters**:
- `record` (dict): The product record to be translated.  Must be a dictionary.
- `from_locale` (str): The source language code (e.g., "en_US").
- `to_locale` (str): The target language code (e.g., "fr_FR").


**Returns**:
- dict: The translated product record as a dictionary.  Returns `None` if the translation fails.


**Raises**:
- `Exception`: Any exception raised during the translation process, including issues with the chosen translation service.