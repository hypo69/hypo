```python
import pytest
import json

# Assuming the JSON content is loaded as a dictionary in a real-world scenario,
# let's create a fixture for a simplified example of loading the JSON content.
# In actual code, this would be replaced with reading from the file.

@pytest.fixture
def settings_data():
    """Provides test data representing the settings.json content."""
    return {
        "langs": {
            "en": 1,
            "he": 2,
            "ru": 3
        }
    }

# Test cases for the 'langs' dictionary within the settings data

def test_settings_langs_exists(settings_data):
    """Checks if the 'langs' key exists in the settings data."""
    assert "langs" in settings_data, "The 'langs' key should exist in settings data."

def test_settings_langs_type_is_dict(settings_data):
    """Checks if the value of 'langs' is a dictionary."""
    assert isinstance(settings_data["langs"], dict), "The value of 'langs' should be a dictionary."

def test_settings_langs_valid_languages(settings_data):
  """Checks if languages 'en', 'he', 'ru' exist in the 'langs' dictionary with valid numerical values"""
  assert "en" in settings_data["langs"] and isinstance(settings_data["langs"]["en"], int), "English language should be present with a numerical value."
  assert "he" in settings_data["langs"] and isinstance(settings_data["langs"]["he"], int), "Hebrew language should be present with a numerical value."
  assert "ru" in settings_data["langs"] and isinstance(settings_data["langs"]["ru"], int), "Russian language should be present with a numerical value."

def test_settings_langs_valid_values(settings_data):
    """Checks if the language values are correct."""
    assert settings_data["langs"]["en"] == 1, "English language value should be 1."
    assert settings_data["langs"]["he"] == 2, "Hebrew language value should be 2."
    assert settings_data["langs"]["ru"] == 3, "Russian language value should be 3."


def test_settings_langs_no_extra_keys(settings_data):
    """Checks if there are no extra keys in the 'langs' dictionary."""
    expected_keys = {"en", "he", "ru"}
    assert set(settings_data["langs"].keys()) == expected_keys, "The 'langs' dictionary should only contain keys: 'en', 'he', 'ru'."


def test_settings_langs_empty_value():
    """Test case when the values are empty"""
    settings_data = {
        "langs": {
            "en": None,
            "he": None,
            "ru": None
        }
    }
    with pytest.raises(AssertionError):
        test_settings_langs_valid_languages(settings_data)

def test_settings_langs_wrong_type_values():
    """Test case when the values are of the wrong type"""
    settings_data = {
        "langs": {
            "en": "1",
            "he": "2",
            "ru": "3"
        }
    }
    with pytest.raises(AssertionError):
       test_settings_langs_valid_languages(settings_data)
```