```python
"""
Module: src.translators.product_translator.py

Provides functions for translating product data.
"""
import json
from typing import List, Dict
from pathlib import Path
from src import gs
from src.logger import logger
from src.utils import j_loads, j_dumps, pprint
from src.db import ProductTranslationsManager
from src.ai.openai import translate
from src.endpoints.PrestaShop import PrestaShop
from pydantic import BaseModel


class ProductTranslationRecord(BaseModel):
    """
    Pydantic model for product translation records.
    """
    product_reference: str
    locale: str
    name: str
    description: str
    description_short: str
    link_rewrite: str
    meta_description: str
    meta_keywords: str
    meta_title: str
    available_now: str
    available_later: str
    delivery_in_stock: str
    delivery_out_stock: str
    delivery_additional_message: str
    affiliate_short_link: str
    affiliate_text: str
    affiliate_summary: str
    affiliate_summary_2: str
    affiliate_image_small: str
    affiliate_image_medium: str
    affiliate_image_large: str
    ingredients: str
    how_to_use: str
    specification: str


def get_translations_from_presta_translations_table(
    product_reference: str, i18n: str = None
) -> List[ProductTranslationRecord]:
    """
    Fetches product translations from the database.

    :param product_reference: Product reference.
    :type product_reference: str
    :param i18n: Target locale (e.g., 'en_EN', 'ru_RU'). Optional.
    :type i18n: str
    :raises ValueError: If the database query fails.
    :returns: A list of ProductTranslationRecord objects.
    """
    try:
        with ProductTranslationsManager() as translations_manager:
            search_filter = {"product_reference": product_reference}
            product_translations = translations_manager.select_record(
                **search_filter
            )
            return [ProductTranslationRecord(**translation) for translation in product_translations]
    except Exception as e:
        logger.exception(f"Error fetching translations: {e}")
        raise ValueError(f"Error fetching translations: {e}")

def insert_new_translation_to_presta_translations_table(record: ProductTranslationRecord):
    """Inserts a new translation record into the database."""
    try:
        with ProductTranslationsManager() as translations_manager:
            translations_manager.insert_record(record.dict())  # Use dict()
    except Exception as e:
        logger.exception(f"Error inserting translation: {e}")
        raise ValueError(f"Error inserting translation: {e}")


def translate_record(
    record: ProductTranslationRecord, from_locale: str, to_locale: str
) -> ProductTranslationRecord:
    """
    Translates a product record.

    :param record: The record to translate.
    :type record: ProductTranslationRecord
    :param from_locale: The source locale.
    :type from_locale: str
    :param to_locale: The target locale.
    :type to_locale: str
    :raises ValueError: If translation fails.
    :returns: The translated record.
    """
    try:
        translated_record = translate(record.dict(), from_locale, to_locale)
        return ProductTranslationRecord(**translated_record)  # Convert back to model
    except Exception as e:
        logger.exception(f"Error translating record: {e}")
        raise ValueError(f"Error translating record: {e}")

```

**Changes Made:**

* **Pydantic Model:** Created `ProductTranslationRecord` to validate and structure product translation data.  This improves data integrity and readability.
* **Type Hinting:** Added type hints (`typing`) for better code clarity and maintainability.
* **Error Handling:** Implemented `try-except` blocks to catch and log exceptions during database interactions and translation. This prevents the application from crashing and provides more informative error messages.
* **Improved `get_translations_from_presta_translations_table`:**
    * Returns a list of `ProductTranslationRecord` objects.
    * Raises `ValueError` for database errors.
* **Improved `insert_new_translation_to_presta_translations_table`:**
    * Takes a `ProductTranslationRecord` as input.
    * Handles exceptions and raises `ValueError`.
    * Uses `record.dict()` to convert the model to a dictionary for database insertion.
* **Improved `translate_record`:**
    * Takes a `ProductTranslationRecord` as input.
    * Raises `ValueError` for translation errors.
    * Converts the translated dictionary back to a `ProductTranslationRecord` for consistent data type.
* **Docstrings:** Updated docstrings with more complete descriptions, including parameters, return types, and possible exceptions.  Used proper RST formatting.
* **Removed Redundant Code:** Removed the `record` function as it was not necessary with the Pydantic model.


This revised code is more robust, maintainable, and adheres to best practices for data validation, error handling, and code clarity.  It's much easier to work with and to extend.  Crucially, it now validates the input data at the application level, ensuring correct data structure and content before interaction with the database and translation services. Remember to install the `pydantic` library if you haven't already.


```bash
pip install pydantic
```