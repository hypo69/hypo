```python
import pytest
from typing import Dict, List
from hypotez.src.translators.translate_product_fields import (
    get_translations_from_presta_translations_table,
    insert_new_translation_to_presta_translations_table,
    translate_record,
)
from unittest.mock import patch
from src.db import ProductTranslationsManager


# Fixture for ProductTranslationsManager
@pytest.fixture
def mock_translations_manager(monkeypatch):
    class MockTranslationsManager:
        def __init__(self, credentials):
            self.credentials = credentials

        def select_record(self, **kwargs):
            product_reference = kwargs.get('product_reference')
            if product_reference == 'test_product':
                return [{'field1': 'value1', 'field2': 'value2'}]
            else:
                return []

        def insert_record(self, record):
            pass  # Mock the insertion

    monkeypatch.setattr(
        'hypotez.src.translators.translate_product_fields.ProductTranslationsManager',
        MockTranslationsManager,
    )
    return MockTranslationsManager


# Fixture for test data
@pytest.fixture
def credentials():
    return {'user': 'testuser', 'password': 'testpassword'}


@pytest.fixture
def product_reference():
    return 'test_product'


# Test cases for get_translations_from_presta_translations_table
def test_get_translations_from_presta_translations_table_valid_input(
    mock_translations_manager, credentials, product_reference
):
    """Tests the function with valid input and expected output."""
    translations = get_translations_from_presta_translations_table(
        product_reference, credentials
    )
    assert translations == [{'field1': 'value1', 'field2': 'value2'}]


def test_get_translations_from_presta_translations_table_product_not_found(
    mock_translations_manager, credentials, product_reference
):
    """Tests the function with a product reference not found."""
    translations = get_translations_from_presta_translations_table(
        'nonexistent_product', credentials
    )
    assert translations == []

def test_get_translations_from_presta_translations_table_empty_credentials(mock_translations_manager):
    """Tests the function with an empty credential dict"""
    with pytest.raises(TypeError):
        get_translations_from_presta_translations_table('test_product', {})


# Test cases for insert_new_translation_to_presta_translations_table (using a mock)
def test_insert_new_translation_to_presta_translations_table(mock_translations_manager, credentials):
    """Tests the function with valid input (mock)."""
    record = {'field1': 'value1', 'field2': 'value2'}
    insert_new_translation_to_presta_translations_table(record, credentials)
    #  No assertion needed as the function doesn't return anything.
    # The mock insert_record is expected to do nothing.

#Test translate_record (mock)
@patch('hypotez.src.translators.translate_product_fields.translate')
def test_translate_record(mock_translate, credentials):
    """Tests translate_record with a mocked translate function."""
    record = {'field1': 'value1', 'field2': 'value2'}
    from_locale = 'en_US'
    to_locale = 'fr_FR'
    translated_record = translate_record(record, from_locale, to_locale)
    # Assert that the translate function was called with the correct arguments.
    mock_translate.assert_called_once_with(record, from_locale, to_locale)
    # The actual translated record should be tested; example assertion:
    assert isinstance(translated_record, dict)


```

**Explanation and Improvements:**

* **Mocking `ProductTranslationsManager`:**  Critically, the tests now mock the `ProductTranslationsManager`. This isolates the `translate_product_fields` functions from the database interaction.  This is *essential* for unit testing; otherwise, you're testing database connectivity, not the logic of the functions themselves.
* **Fixtures:**  `mock_translations_manager` and `credentials` are now fixtures, which is much better practice for code reusability and organization.
* **Comprehensive Test Cases:** The tests now include a case where the product is not found in the database. This is important for robustness.
* **Clearer Assertions:** Assertions are now more directly related to the expected behavior (e.g., `assert translations == []` for the not-found case).
* **Edge Case for Empty Credentials:** Added a test to check for an exception when the credentials are empty, as this would be critical in a real-world scenario.
* **`translate_record` Test (with Mock):** Added a test for `translate_record` that uses `@patch` to mock the `translate` function call, this is a crucial part of testing, as it isolates the function under test and ensures that the correct call to `translate` is made.  Also includes an assertion to verify that the translated record is of the correct type.

**How to Run:**

1.  Install pytest: `pip install pytest`
2.  Save the test code above in a file named `test_translate_product_fields.py` (or similar).
3.  Run the tests from your terminal: `pytest test_translate_product_fields.py`

Remember to replace the placeholder `# ...` in the original code with actual implementation to fully run the tests.  The mocking in this solution allows you to test the core logic without needing a running database. This is essential for well-structured, maintainable unit tests.