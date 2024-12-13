```python
import pytest
from unittest.mock import patch, MagicMock
from pathlib import Path
from typing import List, Dict

from src.translators.translate_product_fields import (
    get_translations_from_presta_translations_table,
    insert_new_translation_to_presta_translations_table,
    translate_record,
)

# Mock necessary modules and classes
@pytest.fixture
def mock_product_translations_manager():
    with patch("src.translators.translate_product_fields.ProductTranslationsManager") as mock:
        yield mock


@pytest.fixture
def mock_translate():
    with patch("src.translators.translate_product_fields.translate") as mock:
        yield mock


def test_get_translations_from_presta_translations_table_valid_input(mock_product_translations_manager):
    """
    Tests that the function retrieves translations correctly for a valid product reference.
    """
    product_reference = "test_product"
    credentials = {"host": "test_host", "user": "test_user", "password": "test_password", "database": "test_db"}
    expected_translations = [{"field1": "translation1"}, {"field2": "translation2"}]

    mock_manager = MagicMock()
    mock_manager.select_record.return_value = expected_translations
    mock_product_translations_manager.return_value.__enter__.return_value = mock_manager

    translations = get_translations_from_presta_translations_table(product_reference, credentials)
    
    mock_product_translations_manager.assert_called_once_with(credentials)
    mock_manager.select_record.assert_called_once_with(product_reference=product_reference)
    assert translations == expected_translations


def test_get_translations_from_presta_translations_table_no_translations(mock_product_translations_manager):
    """
    Tests that the function returns an empty list when no translations are found.
    """
    product_reference = "nonexistent_product"
    credentials = {"host": "test_host", "user": "test_user", "password": "test_password", "database": "test_db"}
    mock_manager = MagicMock()
    mock_manager.select_record.return_value = []
    mock_product_translations_manager.return_value.__enter__.return_value = mock_manager

    translations = get_translations_from_presta_translations_table(product_reference, credentials)
    
    assert translations == []


def test_insert_new_translation_to_presta_translations_table_valid_record(mock_product_translations_manager):
    """
    Tests that the function inserts a new translation record correctly.
    """
    record = {"product_reference": "new_product", "field1": "translation1", "field2": "translation2"}
    credentials = {"host": "test_host", "user": "test_user", "password": "test_password", "database": "test_db"}

    mock_manager = MagicMock()
    mock_product_translations_manager.return_value.__enter__.return_value = mock_manager

    insert_new_translation_to_presta_translations_table(record, credentials)

    mock_product_translations_manager.assert_called_once_with(credentials)
    mock_manager.insert_record.assert_called_once_with(record)


def test_translate_record_valid_input(mock_translate):
    """
    Tests that the function calls the translation service correctly and returns the translated record.
    """
    record = {"field1": "text1", "field2": "text2"}
    from_locale = "en_US"
    to_locale = "fr_FR"
    expected_translated_record = {"field1": "traduction1", "field2": "traduction2"}

    mock_translate.return_value = expected_translated_record

    translated_record = translate_record(record, from_locale, to_locale)
    
    mock_translate.assert_called_once_with(record, from_locale, to_locale)
    assert translated_record == expected_translated_record


def test_translate_record_empty_record(mock_translate):
    """
    Tests that the function handles empty input record correctly.
    """
    record = {}
    from_locale = "en_US"
    to_locale = "fr_FR"
    expected_translated_record = {}

    mock_translate.return_value = expected_translated_record

    translated_record = translate_record(record, from_locale, to_locale)
    
    mock_translate.assert_called_once_with(record, from_locale, to_locale)
    assert translated_record == expected_translated_record

```