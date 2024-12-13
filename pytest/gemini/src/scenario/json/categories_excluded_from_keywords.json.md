```python
import pytest
import json

# Fixture to load the json data
@pytest.fixture
def categories_data():
    """Loads the json data from the specified file path."""
    file_path = 'hypotez/src/scenario/json/categories_excluded_from_keywords.json'
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        pytest.fail(f"File not found at: {file_path}")
    except json.JSONDecodeError:
        pytest.fail("Error decoding JSON file. Check the file for syntax errors.")



def test_categories_data_is_dict(categories_data):
    """Checks if the loaded data is a dictionary."""
    assert isinstance(categories_data, dict), "Loaded data should be a dictionary."

def test_categories_data_not_empty(categories_data):
    """Checks if the loaded data dictionary is not empty."""
    assert categories_data, "Loaded data should not be empty."

def test_categories_data_keys_are_strings(categories_data):
     """Checks if all keys in the dictionary are strings."""
     for key in categories_data.keys():
          assert isinstance(key, str), f"Key {key} is not a string, found {type(key)}"

def test_categories_data_values_are_strings(categories_data):
     """Checks if all values in the dictionary are strings."""
     for value in categories_data.values():
          assert isinstance(value, str), f"Value {value} is not a string, found {type(value)}"


def test_categories_data_specific_keys_exist(categories_data):
    """Checks if specific keys are present in the dictionary."""
    expected_keys = ["3198", "3202", "3229", "3371", "3228", "3436"]
    for key in expected_keys:
        assert key in categories_data, f"Expected key '{key}' not found in the dictionary."

def test_categories_data_specific_values_match(categories_data):
    """Checks if specific keys have the correct values."""
    assert categories_data.get("3198") == "CONSUMER ELECTRONICS", "Value for key '3198' does not match."
    assert categories_data.get("3202") == "computer,smartphone,gaming console,smart device", "Value for key '3202' does not match."
    assert categories_data.get("3436") == "Speakers & Audio", "Value for key '3436' does not match."


def test_categories_data_no_duplicate_keys(categories_data):
    """Checks that there are no duplicate keys in the dictionary."""
    keys = list(categories_data.keys())
    assert len(keys) == len(set(keys)), "Duplicate keys found in the dictionary."

def test_categories_data_empty_string_values_not_allowed(categories_data):
    """Checks that no values are empty strings."""
    for key, value in categories_data.items():
          assert value.strip() != "", f"Key '{key}' has an empty string value, which is not allowed."
    
def test_categories_data_whitespace_in_values(categories_data):
    """Checks that values do not contain unnecessary leading or trailing whitespaces."""
    for key, value in categories_data.items():
        assert value == value.strip(), f"Value for key '{key}' has leading or trailing whitespace: '{value}'"

def test_categories_data_null_values_not_allowed(categories_data):
     """Check if any of the values are None (null) values which is not allowed."""
     for key, value in categories_data.items():
          assert value is not None, f"Key '{key}' has a None value which is not allowed."

```