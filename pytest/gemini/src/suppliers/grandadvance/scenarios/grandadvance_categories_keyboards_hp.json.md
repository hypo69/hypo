```python
import pytest
import json

# Fixture to load the JSON data from the provided string
@pytest.fixture
def keyboard_data():
    data = """
    {
        "HP WIRELESS KEYBOARD": {
            "brand": "HP",
            "url": "https://www.grandadvance.co.il/default.aspx?g=products&a=list&tieId=585&manid=116",
            "checkbox": false,
            "active": true,
            "condition": "new",
            "presta_categories": "203,204,316"
        },
        "HP USB KEYBOARD": {
            "brand": "HP",
            "url": "https://www.grandadvance.co.il/default.aspx?g=products&a=list&tieId=587&manId=38",
            "checkbox": false,
            "active": true,
            "condition": "new",
            "presta_categories": "203,204,315"
        },
        "HP USB MOUSE": {
            "brand": "HP",
            "url": "https://www.grandadvance.co.il/default.aspx?g=products&a=list&tieId=587&manid=116",
            "checkbox": false,
            "active": true,
            "condition": "new",
            "presta_categories": "203,206,317"
        },
        "HP WIRELESS MOUSE": {
            "brand": "HP",
            "url": "https://www.grandadvance.co.il/default.aspx?g=products&a=list&tieId=586&manid=116",
            "checkbox": false,
            "active": true,
            "condition": "new",
            "presta_categories": "203,206,318"
        },
        "HP USB KEYBOARD-MOUSE SET": {
            "brand": "HP",
            "url": "https://www.grandadvance.co.il/default.aspx?g=products&a=list&tieId=582&manid=116",
            "checkbox": false,
            "active": true,
            "condition": "new",
            "presta_categories": "203,207,208"
        },
        "HP WIRELESS  KEYBOARD-MOUSE SET": {
            "brand": "HP",
            "url": "https://www.grandadvance.co.il/default.aspx?g=products&a=list&tieId=582&manid=116",
            "checkbox": false,
            "active": true,
            "condition": "new",
            "presta_categories": "203,207,334"
        }
    }
    """
    return json.loads(data)

# Test case to verify the structure and keys of the JSON
def test_keyboard_data_structure(keyboard_data):
    """Checks if the loaded data is a dictionary and contains specific keys."""
    assert isinstance(keyboard_data, dict), "The loaded data should be a dictionary."
    expected_keys = [
        "HP WIRELESS KEYBOARD",
        "HP USB KEYBOARD",
        "HP USB MOUSE",
        "HP WIRELESS MOUSE",
        "HP USB KEYBOARD-MOUSE SET",
        "HP WIRELESS  KEYBOARD-MOUSE SET",
    ]
    assert all(key in keyboard_data for key in expected_keys), f"Not all expected keys are present: {expected_keys}"


# Test case to verify the values of a specific entry
def test_keyboard_data_entry_values(keyboard_data):
    """Checks if the data entry values for 'HP WIRELESS KEYBOARD' are correct."""
    expected_entry = {
        "brand": "HP",
        "url": "https://www.grandadvance.co.il/default.aspx?g=products&a=list&tieId=585&manid=116",
        "checkbox": False,
        "active": True,
        "condition": "new",
        "presta_categories": "203,204,316",
    }
    actual_entry = keyboard_data.get("HP WIRELESS KEYBOARD")
    assert actual_entry == expected_entry, f"Data entry values do not match for 'HP WIRELESS KEYBOARD'. Expected: {expected_entry}, got: {actual_entry}"


# Test case to verify data types of values
def test_keyboard_data_value_types(keyboard_data):
    """Checks the data type of specific values in the 'HP USB KEYBOARD' entry."""
    keyboard_item = keyboard_data.get("HP USB KEYBOARD")
    assert isinstance(keyboard_item['brand'], str), "Brand should be a string"
    assert isinstance(keyboard_item['url'], str), "URL should be a string"
    assert isinstance(keyboard_item['checkbox'], bool), "Checkbox should be a boolean"
    assert isinstance(keyboard_item['active'], bool), "Active should be a boolean"
    assert isinstance(keyboard_item['condition'], str), "Condition should be a string"
    assert isinstance(keyboard_item['presta_categories'], str), "presta_categories should be a string"


#Test case to verify the 'presta_categories' key
def test_presta_categories_format(keyboard_data):
    """Verifies that 'presta_categories' values are strings and contain comma-separated numeric values."""
    for item in keyboard_data.values():
        assert isinstance(item["presta_categories"], str), "presta_categories should be a string"
        categories = item["presta_categories"].split(",")
        for cat in categories:
            assert cat.isdigit(), f"Category '{cat}' is not a number in {item}"

# Test case for an empty or missing key
def test_keyboard_data_missing_key(keyboard_data):
    """Checks for a missing key and expects that it is not present."""
    assert "NON_EXISTENT_KEY" not in keyboard_data, "The key should not exist"

# Test to see all values inside every item are strings or bool
def test_keyboard_data_values_are_strings_or_bool(keyboard_data):
    """Checks if values are strings or bool"""
    for item in keyboard_data.values():
        for value in item.values():
            assert isinstance(value, (str, bool)), f"Values must be a string or boolean, but got {type(value)} with value {value}"

# Test Case with empty json
def test_empty_json():
    empty_data = {}
    assert isinstance(empty_data, dict)
    assert not empty_data
    
    
def test_keyboard_data_urls_are_strings(keyboard_data):
    """Checks if the url is a string"""
    for item in keyboard_data.values():
       assert isinstance(item['url'], str), "Url should be a string"

def test_keyboard_data_brands_are_strings(keyboard_data):
     """Checks if the brand is a string"""
     for item in keyboard_data.values():
       assert isinstance(item['brand'], str), "brand should be a string"
```