```python
import pytest
from hypotez.src.product.product_fields.product_fields_translator import (
    rearrange_language_keys,
    translate_presta_fields_dict,
)


def test_rearrange_language_keys_valid_input():
    """Checks correct behavior with a valid input."""
    presta_fields_dict = {"field1": {"language": [{"attrs": {"id": "1"}, "value": "val1"}]}}
    client_langs_schema = [{"id": 2, "locale": "en-US", "iso_code": "en"}]
    page_lang = "en"
    expected_output = {"field1": {"language": [{"attrs": {"id": "2"}, "value": "val1"}]}}
    actual_output = rearrange_language_keys(
        presta_fields_dict, client_langs_schema, page_lang
    )
    assert actual_output == expected_output


def test_rearrange_language_keys_no_match():
    """Checks behavior when no matching language is found."""
    presta_fields_dict = {"field1": {"language": [{"attrs": {"id": "1"}, "value": "val1"}]}}
    client_langs_schema = [{"id": 2, "locale": "fr-FR", "iso_code": "fr"}]
    page_lang = "en"
    expected_output = {"field1": {"language": [{"attrs": {"id": "1"}, "value": "val1"}]}}
    actual_output = rearrange_language_keys(
        presta_fields_dict, client_langs_schema, page_lang
    )
    assert actual_output == expected_output



def test_rearrange_language_keys_empty_dict():
    """Checks behavior with an empty presta_fields_dict."""
    presta_fields_dict = {}
    client_langs_schema = [{"id": 2, "locale": "en-US", "iso_code": "en"}]
    page_lang = "en"
    expected_output = {}
    actual_output = rearrange_language_keys(
        presta_fields_dict, client_langs_schema, page_lang
    )
    assert actual_output == expected_output



def test_translate_presta_fields_dict_valid_input():
    """Checks correct behavior with a valid input and translation."""
    presta_fields_dict = {"reference": "123", "name": {"language": [{"attrs": {"id": "1"}, "value": "name"}]}}
    client_langs_schema = [{"id": 2, "locale": "en-US", "iso_code": "en"}]
    page_lang = "en"
    enabled_product_translations = [{"name": "translated_name"}]
    # Mock get_translations_from_presta_translations_table
    def mock_get_translations(ref):
        if ref == "123":
            return enabled_product_translations
        return None
    
    from unittest.mock import patch
    with patch('hypotez.src.product.product_fields.product_fields_translator.get_translations_from_presta_translations_table',side_effect=mock_get_translations):

        expected_output = {"reference": "123", "name": {"language": [{"attrs": {"id": "2"}, "value": "translated_name"}]}}
        actual_output = translate_presta_fields_dict(
            presta_fields_dict, client_langs_schema, page_lang
        )
        assert actual_output == expected_output



def test_translate_presta_fields_dict_no_translation():
    """Checks behavior when no translation is found."""
    presta_fields_dict = {"reference": "123", "name": {"language": [{"attrs": {"id": "1"}, "value": "name"}]}}
    client_langs_schema = [{"id": 2, "locale": "en-US", "iso_code": "en"}]
    page_lang = "en"
    enabled_product_translations = []
    # Mock get_translations_from_presta_translations_table
    def mock_get_translations(ref):
        if ref == "123":
            return enabled_product_translations
        return None
    from unittest.mock import patch

    with patch('hypotez.src.product.product_fields.product_fields_translator.get_translations_from_presta_translations_table',side_effect=mock_get_translations):
        
        expected_output = {"reference": "123", "name": {"language": [{"attrs": {"id": "1"}, "value": "name"}]}}
        actual_output = translate_presta_fields_dict(
            presta_fields_dict, client_langs_schema, page_lang
        )
        assert actual_output == expected_output
```

**Explanation and Improvements:**

1. **Mocking `get_translations_from_presta_translations_table`:**  The original code relies on external functions (`get_translations_from_presta_translations_table`, `insert_new_translation_to_presta_translations_table`) which are not defined in the provided snippet.  These were crucial to the original code.  I've added `patch` from `unittest.mock` to properly simulate how the function is called to retrieve translations.  This isolates the tests from these external dependencies, crucial for reliable testing.


2. **Clearer Test Cases:** The test cases now have more descriptive names (e.g., `test_rearrange_language_keys_no_match`) that clearly indicate the scenario being tested.


3. **Edge Cases and Error Handling:** Added a test (`test_rearrange_language_keys_no_match`) for cases where no matching language is found.  The test now includes an `expected_output` to ensure that the original dictionary remains unchanged. A test case `test_rearrange_language_keys_empty_dict` for empty input `presta_fields_dict` is also added.


4. **Complete Example:**  The `test_translate_presta_fields_dict_valid_input` case now includes an example `enabled_product_translations` list.


5. **Robustness:**  The `test_translate_presta_fields_dict_no_translation` tests the scenario where no translations are found in the database.


6. **Import Fixes:** I've fixed `import` statements to match my assumptions about the module structure (assuming the functions exist as specified).



**How to Run the Tests:**

1.  Save the test code as a `.py` file (e.g., `test_product_fields_translator.py`).
2.  Run `pytest test_product_fields_translator.py` from your terminal.


**Important Considerations (for real-world implementation):**

*   **Error Handling:**  The real `translate_presta_fields_dict` function should have more robust error handling. The `try...except` block in the original function is a good start, but consider more specific exception types and better error messages.  You need to decide what your app will do when the database operation fails, and your test code should reflect that.
*   **External Dependencies:**  Ideally, you should mock out any external calls (database connections, API calls) to prevent these dependencies from influencing your tests.


This revised solution provides a much more thorough and practical approach to testing the provided code. Remember to adapt the test cases to match the actual implementation details and expected behavior of your external functions (`get_translations_from_presta_translations_table`). Remember to replace the placeholder `record` and `get_translations_from_presta_translations_table` definitions.