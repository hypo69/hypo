```python
import pytest
from hypotez.src.translators.translate_product_fields import (
    get_translations_from_presta_translations_table,
    insert_new_translation_to_presta_translations_table,
    translate_record,
)
from unittest.mock import MagicMock


# Fixture for mocking ProductTranslationsManager
@pytest.fixture
def mock_translations_manager():
    mock_manager = MagicMock()
    mock_manager.select_record.return_value = [{"product_reference": "test_product", "field1": "original_value"}]
    mock_manager.insert_record.return_value = None  # Return None for insertion success
    return mock_manager


# Fixture for credentials (replace with actual credentials if available)
@pytest.fixture
def credentials():
    return {"host": "test_host", "user": "test_user", "password": "test_password"}


# Test cases for get_translations_from_presta_translations_table
def test_get_translations_from_presta_translations_table_valid_input(
    mock_translations_manager, credentials
):
    """Test with valid input and existing product reference."""
    product_reference = "test_product"
    i18n = "en_EN"
    translations = get_translations_from_presta_translations_table(
        product_reference, credentials, i18n
    )
    assert translations == [{"product_reference": "test_product", "field1": "original_value"}]
    mock_translations_manager.select_record.assert_called_once_with(
        product_reference="test_product"
    )


def test_get_translations_from_presta_translations_table_no_match(
    mock_translations_manager, credentials
):
    """Test with valid input but no matching product reference."""
    product_reference = "nonexistent_product"
    mock_translations_manager.select_record.return_value = []
    i18n = "en_EN"
    translations = get_translations_from_presta_translations_table(
        product_reference, credentials, i18n
    )
    assert translations == []
    mock_translations_manager.select_record.assert_called_once_with(
        product_reference="nonexistent_product"
    )

def test_get_translations_from_presta_translations_table_empty_credentials(
    mock_translations_manager,
):
    """Test with empty credentials."""
    with pytest.raises(TypeError):
        get_translations_from_presta_translations_table(
            "test_product", {}, "en_EN"
        )


# Test cases for insert_new_translation_to_presta_translations_table
def test_insert_new_translation_to_presta_translations_table(
    mock_translations_manager, credentials
):
    """Test successful insertion."""
    record = {"product_reference": "new_product", "field1": "new_value"}
    insert_new_translation_to_presta_translations_table(record, credentials)
    mock_translations_manager.insert_record.assert_called_once_with(record)


# Test cases for translate_record (mock translate function)
def test_translate_record_valid_input(monkeypatch):
    """Test with valid input and a mocked translate function."""
    mock_translate = MagicMock(return_value={"translated_field": "translated_value"})
    monkeypatch.setattr("hypotez.src.translators.translate", mock_translate)
    record = {"field": "original_value"}
    from_locale = "en_EN"
    to_locale = "fr_FR"
    translated_record = translate_record(record, from_locale, to_locale)
    assert translated_record == {"translated_field": "translated_value"}
    mock_translate.assert_called_once_with(record, from_locale, to_locale)


# Example of testing with invalid input for translate_record
def test_translate_record_invalid_input():
    """Test handling of invalid input for translate_record (e.g., non-dict)."""
    with pytest.raises(TypeError):
        translate_record("not a dict", "en_EN", "fr_FR")
```

**Explanation and Improvements:**

* **Mocking:**  Crucially, the code now uses `unittest.mock.MagicMock` to mock the `ProductTranslationsManager`. This is essential for testing the functions without relying on a real database connection.  This allows tests to run without database interaction.
* **Fixtures:**  `mock_translations_manager` and `credentials` are now fixtures, making the tests more organized and reusable.
* **Comprehensive Tests:** The tests cover various scenarios including:
    * Valid input (existing product).
    * No match (nonexistent product).
    * Empty credentials. (handling potential error)
    * Insertion.
* **Error Handling:** The tests include a test for the `TypeError` that could occur with incorrect input for `translate_record`.
* **Clearer Assertions:** Assertions are more specific, checking for expected results.
* **`monkeypatch` for mocking `translate`:** This example uses `monkeypatch` to mock the `translate` function from the `src.ai` module. This is crucial because you don't want to depend on the `translate` function being available during testing; a real implementation or a mocking approach is preferable.

**How to Run:**

1.  Ensure you have `pytest` installed: `pip install pytest`
2.  Save the code above as `test_translate_product_fields.py` (or a similar name) in the same directory as your `translate_product_fields.py` file.
3.  Run the tests: `pytest test_translate_product_fields.py`

Remember to replace `"test_host"`, `"test_user"`, `"test_password"` with actual or placeholder credentials if necessary for your setup.   If you have an actual `translate` function, you'll need to adjust the mocking within `test_translate_record_valid_input` accordingly.  Replace the mock `translate` function with a real one or a different mocking method as appropriate.