```python
import pytest
from hypotez.src.product.product_fields.product_fields_translator import rearrange_language_keys, translate_presta_fields_dict
from pprint import pprint


def test_rearrange_language_keys_valid_input():
    """Tests rearrange_language_keys with valid input."""
    presta_fields_dict = {'product_name': {'language': [{'attrs': {'id': 'old_id'}, 'value': 'Product Name'}]}}
    client_langs_schema = [{'id': 1, 'locale': 'en-US', 'iso_code': 'en'}]
    page_lang = 'en'
    expected_output = {'product_name': {'language': [{'attrs': {'id': '1'}, 'value': 'Product Name'}]}}
    actual_output = rearrange_language_keys(presta_fields_dict, client_langs_schema, page_lang)
    assert actual_output == expected_output


def test_rearrange_language_keys_no_match():
    """Tests rearrange_language_keys when no matching language is found."""
    presta_fields_dict = {'product_name': {'language': [{'attrs': {'id': 'old_id'}, 'value': 'Product Name'}]}}
    client_langs_schema = [{'id': 1, 'locale': 'fr-FR', 'iso_code': 'fr'}]
    page_lang = 'en'
    expected_output = {'product_name': {'language': [{'attrs': {'id': 'old_id'}, 'value': 'Product Name'}]}}
    actual_output = rearrange_language_keys(presta_fields_dict, client_langs_schema, page_lang)
    assert actual_output == expected_output


def test_rearrange_language_keys_multiple_fields():
    """Tests rearrange_language_keys with multiple fields."""
    presta_fields_dict = {
        'product_name': {'language': [{'attrs': {'id': 'old_id'}, 'value': 'Product Name'}]},
        'description': {'language': [{'attrs': {'id': 'old_id'}, 'value': 'Description'}]},
    }
    client_langs_schema = [{'id': 1, 'locale': 'en-US', 'iso_code': 'en'}]
    page_lang = 'en'
    expected_output = {
        'product_name': {'language': [{'attrs': {'id': '1'}, 'value': 'Product Name'}]},
        'description': {'language': [{'attrs': {'id': '1'}, 'value': 'Description'}]},
    }
    actual_output = rearrange_language_keys(presta_fields_dict, client_langs_schema, page_lang)
    assert actual_output == expected_output


def test_translate_presta_fields_dict_valid_input():
    """Test for valid input with translations present."""
    presta_fields_dict = {'reference': '12345', 'name': {'language': [{'attrs': {'id': 'old_id'}, 'value': 'Product Name'}]}}
    client_langs_schema = [{'id': 1, 'locale': 'en-US', 'iso_code': 'en'}]
    page_lang = 'en'
    # Mock get_translations_from_presta_translations_table to avoid external dependencies
    def mock_get_translations(reference):
        return [{'reference': '12345', 'name': 'Translated Name'}]
    
    # Replace the function in the module with a mock
    translate_presta_fields_dict.get_translations_from_presta_translations_table = mock_get_translations

    expected_output = {'reference': '12345', 'name': {'language': [{'attrs': {'id': '1'}, 'value': 'Translated Name'}]}}
    actual_output = translate_presta_fields_dict(presta_fields_dict, client_langs_schema, page_lang)
    assert actual_output == expected_output

@pytest.mark.parametrize("page_lang", ["en", "en-US", "es"])
def test_translate_presta_fields_dict_valid_iso_codes(page_lang):
  """Test for valid input with different possible page_lang iso_codes """
  presta_fields_dict = {'reference': '12345', 'name': {'language': [{'attrs': {'id': 'old_id'}, 'value': 'Product Name'}]}}
  client_langs_schema = [{'id': 1, 'locale': 'en-US', 'iso_code': 'en'}, {'id': 2, 'locale': 'es-ES', 'iso_code': 'es'}]
  page_lang = page_lang

  # Mock get_translations_from_presta_translations_table to avoid external dependencies
  def mock_get_translations(reference):
      if page_lang == "en":
          return [{'reference': '12345', 'name': 'Translated Name'}]
      elif page_lang == "es":
          return [{'reference': '12345', 'name': 'Producto Traducido'}]
      else:
          return []

  translate_presta_fields_dict.get_translations_from_presta_translations_table = mock_get_translations
  expected_output = {'reference': '12345', 'name': {'language': [{'attrs': {'id': '1'}, 'value': 'Translated Name'}]}} if page_lang == "en" else {'reference': '12345', 'name': {'language': [{'attrs': {'id': '2'}, 'value': 'Producto Traducido'}]}}
  actual_output = translate_presta_fields_dict(presta_fields_dict, client_langs_schema, page_lang)
  assert actual_output == expected_output




```

**Explanation and Improvements:**

* **Clearer Test Names:** Test names now better reflect the scenario being tested.
* **Edge Cases and Invalid Input:** Tests now include cases where no matching language is found and cases with multiple fields.
* **Mocking:** The crucial `get_translations_from_presta_translations_table` function is now mocked in the tests. This is essential because the tests should not depend on external resources or databases (the original code was interacting with a database).  This dramatically improves testability.
* **Parametrization:** The `test_translate_presta_fields_dict_valid_iso_codes` test now uses `pytest.mark.parametrize` to run the same test multiple times with different values of `page_lang`. This is a better way to test various possible `page_lang` values.
* **Comprehensive Test Coverage:** The tests now cover valid input, no match, multiple fields, and different possible `page_lang` values.
* **Error Handling (partially):**  While the original code had `try...except` blocks, the tests do not currently fully verify the error handling as they are mocking the database interaction.  For a complete error handling test, you would need to mock a function that simulates a database error.

**How to use these tests:**

1. **Install pytest:** `pip install pytest`
2. **Save the tests:**  Save the provided test code in a file (e.g., `test_product_fields_translator.py`) in the same directory as `product_fields_translator.py`.
3. **Run the tests:** `pytest test_product_fields_translator.py`

**Important Considerations for Real-World Testing:**

* **Database Mocking:**  Replace the mock function with a more robust mechanism to simulate database interactions and error scenarios.   Use a testing library like `unittest.mock` or `pytest-mock`.
* **Exception Handling:** Add tests to verify that the `try...except` blocks in the original code properly handle potential exceptions (e.g., `ProductFieldException`).
* **Input Validation:** Test cases should include invalid or unexpected input types and values for the function parameters to ensure robustness.
* **External Dependencies:** Consider how external resources (like the translations database) are managed for better test coverage.
* **Completeness:** Add more test cases to cover a wider range of possible inputs and scenarios.


By adding these improvements, you'll be able to develop more confident and reliable tests. Remember to tailor these tests to the specific error handling and external interaction details of your production code.