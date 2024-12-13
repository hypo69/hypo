```python
import pytest
import json

# Fixture for loading the locales data
@pytest.fixture
def locales_data():
    """Provides the locales data from the JSON file."""
    # simulate loading a json file
    return {
      "locales": [
        { "HE": "ILS" },
        { "EN": "USD" },
        { "RU": "ILS" }
      ],
      "disabled": [
        { "RU": "USD" },
        { "EN": "EUR" },
        { "EN": "GBR" },
        { "RU": "EUR" }
      ]
    }


def test_locales_data_structure(locales_data):
    """
    Test that the loaded JSON data contains the expected keys and is a dictionary.
    """
    assert isinstance(locales_data, dict), "Data should be loaded as a dictionary."
    assert "locales" in locales_data, "'locales' key is missing."
    assert "disabled" in locales_data, "'disabled' key is missing."

def test_locales_is_list(locales_data):
    """
    Test that the value of the 'locales' key is a list
    """
    assert isinstance(locales_data["locales"], list)


def test_disabled_is_list(locales_data):
    """
    Test that the value of the 'disabled' key is a list
    """
    assert isinstance(locales_data["disabled"], list)

def test_locales_content_structure(locales_data):
  """
  Test that the content of locales key is a list of dicts
  """
  for locale in locales_data["locales"]:
      assert isinstance(locale, dict), "Each item in 'locales' should be a dictionary."
      assert len(locale) == 1, "Each locale item should contain a single key-value pair."


def test_disabled_content_structure(locales_data):
    """
    Test that the content of disabled key is a list of dicts
    """
    for disabled in locales_data["disabled"]:
        assert isinstance(disabled, dict), "Each item in 'disabled' should be a dictionary."
        assert len(disabled) == 1, "Each disabled item should contain a single key-value pair."

def test_locales_valid_keys(locales_data):
    """
    Test that the locale keys are valid language codes
    """
    valid_keys = ["HE", "EN", "RU"]
    for locale in locales_data["locales"]:
        key = list(locale.keys())[0]
        assert key in valid_keys, f"'{key}' is not a valid locale code."


def test_disabled_valid_keys(locales_data):
    """
    Test that the disabled keys are valid language codes
    """
    valid_keys = ["HE", "EN", "RU"]
    for disabled in locales_data["disabled"]:
        key = list(disabled.keys())[0]
        assert key in valid_keys, f"'{key}' is not a valid locale code."

def test_locales_values_not_empty(locales_data):
    """
    Test that the locale values are not empty strings
    """
    for locale in locales_data["locales"]:
      value = list(locale.values())[0]
      assert value != "", f"'{value}' locale value is empty."

def test_disabled_values_not_empty(locales_data):
  """
    Test that the disabled values are not empty strings
    """
  for disabled in locales_data["disabled"]:
      value = list(disabled.values())[0]
      assert value != "", f"'{value}' disabled value is empty."
```