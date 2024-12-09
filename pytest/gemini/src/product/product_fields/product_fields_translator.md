```python
import pytest
from hypotez.src.product.product_fields.product_fields_translator import rearrange_language_keys, translate_presta_fields_dict
from unittest.mock import patch
from src.logger import logger
from src.logger.exceptions import ProductFieldException

# Mock functions for testing
@patch('hypotez.src.product.product_fields.product_fields_translator.get_translations_from_presta_translations_table', return_value=[])
@patch('hypotez.src.product.product_fields.product_fields_translator.insert_new_translation_to_presta_translations_table')
def test_translate_presta_fields_dict_empty_translations(mock_insert, mock_get_translations):
    """Tests translate_presta_fields_dict with empty translations."""
    presta_fields_dict = {'reference': '123'}
    client_langs_schema = [{'id': 1, 'iso_code': 'en', 'locale': 'en-US'}]
    page_lang = 'en-US'
    result = translate_presta_fields_dict(presta_fields_dict, client_langs_schema, page_lang)
    
    assert result == presta_fields_dict
    mock_insert.assert_called_once()  # Check if insert function is called

@patch('hypotez.src.product.product_fields.product_fields_translator.get_translations_from_presta_translations_table', return_value=[{'reference': '123', 'locale': 'en-US'}])
def test_translate_presta_fields_dict_valid_translations(mock_get_translations):
    """Tests translate_presta_fields_dict with valid translations."""
    presta_fields_dict = {'reference': '123', 'name': {'language': [{'attrs': {'id': '1'}, 'value': 'test'}]}}
    client_langs_schema = [{'id': 1, 'iso_code': 'en', 'locale': 'en-US'}]
    page_lang = 'en-US'
    result = translate_presta_fields_dict(presta_fields_dict, client_langs_schema, page_lang)
    
    assert result['reference'] == {'language': [{'attrs': {'id': '1'}, 'value': '123'}]}
    assert result['name'] == {'language': [{'attrs': {'id': '1'}, 'value': 'test'}]}
    # Check if the translation is updated
    
@patch('hypotez.src.product.product_fields.product_fields_translator.get_translations_from_presta_translations_table', side_effect=Exception)
def test_translate_presta_fields_dict_exception(mock_get_translations):
    """Tests translate_presta_fields_dict with exceptions."""
    presta_fields_dict = {'reference': '123'}
    client_langs_schema = [{'id': 1, 'iso_code': 'en', 'locale': 'en-US'}]
    page_lang = 'en-US'
    with pytest.raises(Exception):
      translate_presta_fields_dict(presta_fields_dict, client_langs_schema, page_lang)
    
    mock_get_translations.assert_called_once()  # Check that the function is called
    #Check for logger error


def test_rearrange_language_keys_valid_input():
    """Tests rearrange_language_keys with valid input."""
    presta_fields_dict = {'field1': {'language': [{'attrs': {'id': '1'}, 'value': 'val1'}]}}
    client_langs_schema = [{'id': 1, 'locale': 'en-US', 'iso_code':'en'}]
    page_lang = 'en-US'
    result = rearrange_language_keys(presta_fields_dict, client_langs_schema, page_lang)
    assert result['field1']['language'][0]['attrs']['id'] == '1'

def test_rearrange_language_keys_no_match():
    """Tests rearrange_language_keys when no matching language is found."""
    presta_fields_dict = {'field1': {'language': [{'attrs': {'id': '1'}, 'value': 'val1'}]}}
    client_langs_schema = [{'id': 2, 'locale': 'fr-FR', 'iso_code':'fr'}]
    page_lang = 'en-US'
    result = rearrange_language_keys(presta_fields_dict, client_langs_schema, page_lang)
    assert result == presta_fields_dict
    
def test_rearrange_language_keys_empty_input():
    """Tests rearrange_language_keys with empty input."""
    presta_fields_dict = {}
    client_langs_schema = []
    page_lang = 'en-US'
    result = rearrange_language_keys(presta_fields_dict, client_langs_schema, page_lang)
    assert result == {}


```

**Explanation and Improvements:**

1. **Mocking:**  Crucially, the tests now use `@patch` to mock the external functions (`get_translations_from_presta_translations_table`, `insert_new_translation_to_presta_translations_table`). This isolates the unit under test (the target functions) from the external dependencies, preventing issues if those functions fail or are not available during testing.  The mocking is set up so that various return scenarios are tested.

2. **Exception Handling:** The `test_translate_presta_fields_dict_exception` test now uses `pytest.raises` to verify that the function handles exceptions correctly.

3. **Clearer Test Names:** Test names are more descriptive, making it easier to understand the purpose of each test.

4. **Comprehensive Cases:** The tests cover scenarios with valid inputs, empty translations, no match, and empty input data.  This is critical for robust testing.

5. **Edge Cases (rearrange_language_keys):**  `test_rearrange_language_keys_no_match` explicitly tests the case where no matching language is found in the schema.  `test_rearrange_language_keys_empty_input` adds a test for an empty input dictionary.


**How to Run the Tests:**

1.  Make sure you have `pytest` installed. If not, run:
    ```bash
    pip install pytest
    ```

2.  Save the code as `test_product_fields_translator.py` (or a similar name) in the same directory as your `product_fields_translator.py` file.

3.  Run the tests from your terminal:
    ```bash
    pytest test_product_fields_translator.py
    ```


This improved test suite provides much better coverage and reliability for your code.  Remember to adapt the mocks and fixtures to match your actual implementation if there are more complex dependencies.  Consider adding more tests for various input scenarios and edge cases related to different types of data structures and possible errors.