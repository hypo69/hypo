```python
import pytest
import json

# Assuming the JSON data is loaded into a dictionary, simulating the behavior
# when loaded from a file.

@pytest.fixture
def settings_data():
    """Provides the settings data as a dictionary."""
    return {
        "langs": {
            "en": 1,
            "he": 2,
            "ru": 3
        }
    }

def test_settings_data_loaded_correctly(settings_data):
    """
    Test that the settings data is loaded correctly.
    This test asserts that the returned data is a dictionary and contains the "langs" key.
    """
    assert isinstance(settings_data, dict), "The loaded settings should be a dictionary"
    assert "langs" in settings_data, "The 'langs' key should be present in the settings"

def test_langs_values_are_integers(settings_data):
    """
    Test that the values in the 'langs' dictionary are integers.
    Iterates over the dictionary and asserts the value type.
    """
    langs = settings_data.get("langs", {})
    for lang, value in langs.items():
        assert isinstance(value, int), f"The value for '{lang}' should be an integer"

def test_langs_keys_are_strings(settings_data):
    """
    Test that the keys in the 'langs' dictionary are strings.
    Iterates over the dictionary keys and asserts the key type.
    """
    langs = settings_data.get("langs", {})
    for lang in langs.keys():
        assert isinstance(lang, str), f"The key '{lang}' should be a string."


def test_langs_contains_expected_keys(settings_data):
    """
    Test that the 'langs' dictionary contains the expected keys ('en', 'he', 'ru').
    """
    langs = settings_data.get("langs", {})
    expected_keys = {"en", "he", "ru"}
    assert set(langs.keys()) == expected_keys, "The 'langs' dictionary does not contain the expected keys"

def test_langs_has_correct_en_value(settings_data):
    """
    Test that the 'en' key in 'langs' has the correct value (1).
    """
    langs = settings_data.get("langs", {})
    assert langs.get("en") == 1, "The 'en' key should have the value 1"

def test_langs_has_correct_he_value(settings_data):
    """
    Test that the 'he' key in 'langs' has the correct value (2).
    """
    langs = settings_data.get("langs", {})
    assert langs.get("he") == 2, "The 'he' key should have the value 2"

def test_langs_has_correct_ru_value(settings_data):
    """
    Test that the 'ru' key in 'langs' has the correct value (3).
    """
    langs = settings_data.get("langs", {})
    assert langs.get("ru") == 3, "The 'ru' key should have the value 3"

def test_empty_settings_data():
     """
    Test when the settings data is empty. Simulates a potential scenario
    where the JSON file is empty.
     """
     empty_data = {}
     assert isinstance(empty_data,dict) , "Empty settings should be a dict"
     assert "langs" not in empty_data, "Langs should not exist in the empty settings data"

def test_malformed_settings_data():
    """
    Test for handling malformed settings data (e.g., missing 'langs' key).
    This test is for demonstrating handling of unexpected settings structure.
    """
    malformed_data = {"other_key": "value"}
    assert isinstance(malformed_data, dict)
    assert "langs" not in malformed_data, "Malformed data should not have the 'langs' key"

```