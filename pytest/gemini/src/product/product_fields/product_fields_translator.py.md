```python
import pytest
from unittest.mock import MagicMock, patch

from src.product.product_fields.product_fields_translator import rearrange_language_keys, translate_presta_fields_dict
from src.logger.exceptions import ProductFieldException

# Fixture definitions
@pytest.fixture
def sample_presta_fields_dict():
    """Provides a sample presta_fields_dict for testing."""
    return {
        'name': {'language': [{'attrs': {'id': '1'}, 'value': 'Product Name'}]},
        'description': {'language': [{'attrs': {'id': '1'}, 'value': 'Product Description'}]}
    }


@pytest.fixture
def sample_client_langs_schema():
    """Provides a sample client_langs_schema for testing."""
    return [
        {'id': 1, 'locale': 'en-US', 'iso_code': 'en', 'language_code': 'en-us'},
        {'id': 2, 'locale': 'fr-FR', 'iso_code': 'fr', 'language_code': 'fr-fr'},
        {'id': 3, 'locale': 'ru-RU', 'iso_code': 'ru', 'language_code': 'ru-ru'},
    ]

@pytest.fixture
def mock_record():
    class MockRecord:
        def __init__(self, data):
            self.data = data
            self.locale = 'en'
            self.reference = "test_reference"
        def __getattr__(self, name):
            if name in self.data:
                return self.data[name]
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")
    return MockRecord


# Tests for rearrange_language_keys
def test_rearrange_language_keys_valid_locale(sample_presta_fields_dict, sample_client_langs_schema):
    """Checks correct behavior with a valid locale match."""
    updated_dict = rearrange_language_keys(sample_presta_fields_dict, sample_client_langs_schema, 'en-US')
    for field in updated_dict.values():
        if isinstance(field, dict) and 'language' in field:
            for lang_data in field['language']:
                assert lang_data['attrs']['id'] == '1'


def test_rearrange_language_keys_valid_iso_code(sample_presta_fields_dict, sample_client_langs_schema):
    """Checks correct behavior with a valid iso_code match."""
    updated_dict = rearrange_language_keys(sample_presta_fields_dict, sample_client_langs_schema, 'en')
    for field in updated_dict.values():
        if isinstance(field, dict) and 'language' in field:
            for lang_data in field['language']:
                assert lang_data['attrs']['id'] == '1'

def test_rearrange_language_keys_valid_language_code(sample_presta_fields_dict, sample_client_langs_schema):
    """Checks correct behavior with a valid language_code match."""
    updated_dict = rearrange_language_keys(sample_presta_fields_dict, sample_client_langs_schema, 'en-us')
    for field in updated_dict.values():
        if isinstance(field, dict) and 'language' in field:
            for lang_data in field['language']:
                assert lang_data['attrs']['id'] == '1'


def test_rearrange_language_keys_no_match(sample_presta_fields_dict, sample_client_langs_schema):
    """Checks behavior when no language matches are found."""
    updated_dict = rearrange_language_keys(sample_presta_fields_dict, sample_client_langs_schema, 'de-DE')
    for field in updated_dict.values():
        if isinstance(field, dict) and 'language' in field:
            for lang_data in field['language']:
                assert lang_data['attrs']['id'] == '1' # should not be changed


def test_rearrange_language_keys_empty_presta_fields_dict(sample_client_langs_schema):
    """Checks behavior with an empty presta_fields_dict."""
    empty_dict = {}
    updated_dict = rearrange_language_keys(empty_dict, sample_client_langs_schema, 'en-US')
    assert updated_dict == {}

def test_rearrange_language_keys_empty_client_langs_schema(sample_presta_fields_dict):
    """Checks behavior with an empty client_langs_schema."""
    updated_dict = rearrange_language_keys(sample_presta_fields_dict, [], 'en-US')
    for field in updated_dict.values():
            if isinstance(field, dict) and 'language' in field:
                for lang_data in field['language']:
                    assert lang_data['attrs']['id'] == '1'  # should not be changed

def test_rearrange_language_keys_non_dict_field(sample_client_langs_schema):
    """Checks behavior when the field in the dict is not a dict."""
    presta_fields_dict = {'name': "Product Name"}
    updated_dict = rearrange_language_keys(presta_fields_dict, sample_client_langs_schema, 'en-US')
    assert updated_dict == presta_fields_dict # should not be changed


def test_rearrange_language_keys_field_without_language(sample_client_langs_schema):
    """Checks behavior when the field in the dict doesn't have a language key."""
    presta_fields_dict = {'name': {'value': 'Product Name'}}
    updated_dict = rearrange_language_keys(presta_fields_dict, sample_client_langs_schema, 'en-US')
    assert updated_dict == presta_fields_dict # should not be changed


# Tests for translate_presta_fields_dict
@patch('src.product.product_fields.product_fields_translator.get_translations_from_presta_translations_table')
@patch('src.product.product_fields.product_fields_translator.insert_new_translation_to_presta_translations_table')
def test_translate_presta_fields_dict_no_translations(mock_insert_translation, mock_get_translations, sample_presta_fields_dict, sample_client_langs_schema, mock_record):
    """Checks behavior when no translations are found in the table."""
    mock_get_translations.return_value = []
    
    global record
    record = mock_record
    
    translated_dict = translate_presta_fields_dict(sample_presta_fields_dict, sample_client_langs_schema, 'en-US')
    mock_insert_translation.assert_called_once()
    assert translated_dict == sample_presta_fields_dict #Should return the same dict with rearranged language keys


@patch('src.product.product_fields.product_fields_translator.get_translations_from_presta_translations_table')
def test_translate_presta_fields_dict_with_translations(mock_get_translations, sample_presta_fields_dict, sample_client_langs_schema, mock_record):
    """Checks behavior when translations are found in the table."""
    mock_translations = [
        mock_record(
            {"name": "Translated Product Name", "description": "Translated Product Description", "locale": "en"}
        ),
        mock_record(
           {"name": "Translated Product Name FR", "description": "Translated Product Description FR", "locale": "fr"}
        )
    ]
    mock_get_translations.return_value = mock_translations

    global record
    record = mock_record
    
    translated_dict = translate_presta_fields_dict(sample_presta_fields_dict, sample_client_langs_schema, 'en-US')

    assert translated_dict['name']['language'][0]['value'] == "Translated Product Name"
    assert translated_dict['description']['language'][0]['value'] == "Translated Product Description"
    assert translated_dict['name']['language'][0]['attrs']['id'] == '1'
    assert translated_dict['description']['language'][0]['attrs']['id'] == '1'

@patch('src.product.product_fields.product_fields_translator.get_translations_from_presta_translations_table')
def test_translate_presta_fields_dict_with_translations_no_match(mock_get_translations, sample_presta_fields_dict, sample_client_langs_schema, mock_record):
    """Checks behavior when translations are found in the table but there is no match."""
    mock_translations = [
        mock_record(
            {"name": "Translated Product Name", "description": "Translated Product Description", "locale": "de"}
        ),
        mock_record(
           {"name": "Translated Product Name FR", "description": "Translated Product Description FR", "locale": "fr"}
        )
    ]
    mock_get_translations.return_value = mock_translations
    
    global record
    record = mock_record
    
    translated_dict = translate_presta_fields_dict(sample_presta_fields_dict, sample_client_langs_schema, 'en-US')

    assert translated_dict['name']['language'][0]['value'] == "Product Name" #Should not be changed, cause no translation was found for this language
    assert translated_dict['description']['language'][0]['value'] == "Product Description"
    assert translated_dict['name']['language'][0]['attrs']['id'] == '1'
    assert translated_dict['description']['language'][0]['attrs']['id'] == '1'


@patch('src.product.product_fields.product_fields_translator.get_translations_from_presta_translations_table')
def test_translate_presta_fields_dict_with_translations_exception(mock_get_translations, sample_presta_fields_dict, sample_client_langs_schema, mock_record):
    """Checks exception handling during translation."""
    mock_translations = [
          mock_record(
            {"name": "Translated Product Name", "description": "Translated Product Description", "locale": "en"}
        ),
        mock_record(
           {"name": "Translated Product Name FR", "description": "Translated Product Description FR", "locale": "fr"}
        )
    ]
    mock_get_translations.return_value = mock_translations
    
    global record
    record = mock_record
    
    # Mock the hasattr to raise an exception
    with patch('src.product.product_fields.product_fields_translator.hasattr', side_effect=Exception("Test Exception")):
         translated_dict = translate_presta_fields_dict(sample_presta_fields_dict, sample_client_langs_schema, 'en-US')

    assert translated_dict == sample_presta_fields_dict  #Should return original dict, even after exception


def test_translate_presta_fields_dict_empty_presta_fields_dict(sample_client_langs_schema, mock_record):
    """Checks behavior with an empty presta_fields_dict."""
    empty_dict = {}
    global record
    record = mock_record
    translated_dict = translate_presta_fields_dict(empty_dict, sample_client_langs_schema, 'en-US')
    assert translated_dict == {}


def test_translate_presta_fields_dict_empty_client_langs_schema(sample_presta_fields_dict, mock_record):
    """Checks behavior with an empty client_langs_schema."""
    global record
    record = mock_record
    translated_dict = translate_presta_fields_dict(sample_presta_fields_dict, [], 'en-US')
    assert translated_dict == sample_presta_fields_dict  #Should not change original dict

def test_translate_presta_fields_dict_none_page_lang(sample_presta_fields_dict, sample_client_langs_schema, mock_record):
     """Checks behavior with None page_lang. should not raise exception"""
     global record
     record = mock_record
     translate_presta_fields_dict(sample_presta_fields_dict, sample_client_langs_schema, None)
```