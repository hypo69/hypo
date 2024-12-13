```python
import pytest
from unittest.mock import patch, MagicMock
from src.translators.product_translator import (
    get_translations_from_presta_translations_table,
    insert_new_translation_to_presta_translations_table,
    translate_record
)
from src.db import ProductTranslationsManager


@pytest.fixture
def mock_translations_manager():
    """Mocks the ProductTranslationsManager for testing."""
    with patch("src.translators.product_translator.ProductTranslationsManager") as mock:
        yield mock


@pytest.fixture
def mock_translate():
    """Mocks the translate function from src.ai.openai."""
    with patch("src.translators.product_translator.translate") as mock:
        yield mock


def test_get_translations_from_presta_translations_table_valid_reference(mock_translations_manager):
    """Checks if the function correctly fetches translations with a valid product reference."""
    mock_manager_instance = mock_translations_manager.return_value.__enter__.return_value
    mock_manager_instance.select_record.return_value = [{'id': 1, 'product_reference': 'REF123', 'name': 'Test Product'}]
    product_reference = 'REF123'
    result = get_translations_from_presta_translations_table(product_reference)
    assert isinstance(result, list)
    assert len(result) > 0
    assert result[0]['product_reference'] == 'REF123'
    mock_manager_instance.select_record.assert_called_once_with(product_reference='REF123')


def test_get_translations_from_presta_translations_table_no_reference(mock_translations_manager):
    """Checks if the function returns an empty list when product reference doesn't exist."""
    mock_manager_instance = mock_translations_manager.return_value.__enter__.return_value
    mock_manager_instance.select_record.return_value = []
    product_reference = 'NON_EXISTENT_REF'
    result = get_translations_from_presta_translations_table(product_reference)
    assert isinstance(result, list)
    assert len(result) == 0
    mock_manager_instance.select_record.assert_called_once_with(product_reference='NON_EXISTENT_REF')


def test_get_translations_from_presta_translations_table_with_i18n(mock_translations_manager):
    """Checks if the i18n parameter is ignored in select_record method."""
    mock_manager_instance = mock_translations_manager.return_value.__enter__.return_value
    mock_manager_instance.select_record.return_value = [{'id': 1, 'product_reference': 'REF123', 'name': 'Test Product'}]
    product_reference = 'REF123'
    i18n = 'en_EN'
    result = get_translations_from_presta_translations_table(product_reference, i18n=i18n)
    assert isinstance(result, list)
    assert len(result) > 0
    assert result[0]['product_reference'] == 'REF123'
    mock_manager_instance.select_record.assert_called_once_with(product_reference='REF123')

def test_insert_new_translation_to_presta_translations_table_valid_record(mock_translations_manager):
    """Checks if the function correctly inserts a new record into the translations table."""
    mock_manager_instance = mock_translations_manager.return_value.__enter__.return_value
    test_record = {'product_reference': 'REF456', 'name': 'New Product'}
    insert_new_translation_to_presta_translations_table(test_record)
    mock_manager_instance.insert_record.assert_called_once_with(test_record)


def test_insert_new_translation_to_presta_translations_table_empty_record(mock_translations_manager):
    """Checks if the function correctly inserts empty record."""
    mock_manager_instance = mock_translations_manager.return_value.__enter__.return_value
    test_record = {}
    insert_new_translation_to_presta_translations_table(test_record)
    mock_manager_instance.insert_record.assert_called_once_with(test_record)

def test_translate_record_valid_input(mock_translate):
    """Checks if the translate function is called correctly and returns translated record."""
    mock_translate.return_value = {'name': 'Translated Product'}
    record = {'name': 'Test Product'}
    from_locale = 'en'
    to_locale = 'es'
    result = translate_record(record, from_locale, to_locale)
    assert isinstance(result, dict)
    assert result['name'] == 'Translated Product'
    mock_translate.assert_called_once_with(record, from_locale, to_locale)


def test_translate_record_empty_record(mock_translate):
    """Checks if the function handles an empty record."""
    mock_translate.return_value = {}
    record = {}
    from_locale = 'en'
    to_locale = 'fr'
    result = translate_record(record, from_locale, to_locale)
    assert isinstance(result, dict)
    assert result == {}
    mock_translate.assert_called_once_with(record, from_locale, to_locale)
```