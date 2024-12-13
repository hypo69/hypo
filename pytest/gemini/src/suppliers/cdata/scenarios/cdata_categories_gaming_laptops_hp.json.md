```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def cdata_categories_data():
    """Provides the JSON data for testing."""
    json_data = """
{
  "scenarios": {
    "HP GAMING 14 I5": {
      "brand": "HP",
      "url": "---------------------------HP GAMING 14 I5-----------------------------------",
      "checkbox": false,
      "active": true,
      "condition":"new","presta_categories": "3,49,50,52,101,10,5,462"
    },
    "HP GAMING 14 I7": {
      "brand": "HP",
      "url": "------------------------------HP GAMING 14 I7---------------------------------",
      "checkbox": false,
      "active": true,
      "condition":"new","presta_categories": "3,49,50,52,101,10,6,463"
    },
    "HP GAMING 14 I9": {
      "brand": "HP",
      "url": "--------------------------------HP GAMING 14 I9------------------------------",
      "checkbox": false,
      "active": true,
      "condition":"new","presta_categories": "3,49,50,52,101,10,7,464"
    },
    "HP GAMING 14 AMD": {
      "brand": "HP",
      "url": "---------------------------------HP GAMING 14 AMD-----------------------------",
      "checkbox": false,
      "active": true,
      "condition":"new","presta_categories": "3,49,50,52,101,10,234,465"
    },
    "HP GAMING 15 I5": {
      "brand": "HP",
      "url": "https://reseller.c-data.co.il/%D7%A0%D7%99%D7%99%D7%93%D7%99-gaming#/specFilters=227m!#-!4634!-#!225!#-!4663!##!6406&manFilters=2",
      "checkbox": false,
      "active": true,
      "condition":"new","presta_categories": "3,49,50,52,102,11,5,469"
    },
    "HP GAMING 15 I7": {
      "brand": "HP",
      "url": "https://reseller.c-data.co.il/%D7%A0%D7%99%D7%99%D7%93%D7%99-gaming#/specFilters=227m!#-!4635!-#!225!#-!4663!##!6406&manFilters=2",
      "checkbox": false,
      "active": true,
      "condition":"new","presta_categories": "3,49,50,52,102,11,6,470"
    },
    "HP GAMING 15 I9": {
      "brand": "HP",
      "url": "--------------------------------HP GAMING 15 I9------------------------------",
      "checkbox": false,
      "active": true,
      "condition":"new","presta_categories": "3,49,50,52,102,11,7,471"
    },
    "HP GAMING 15 AMD": {
      "brand": "HP",
      "url": "-------------------------HP GAMING 15 AMD-------------------------------------",
      "checkbox": false,
      "active": true,
      "condition":"new","presta_categories": "3,49,50,52,102,,11,234,472"
    },
    "HP GAMING 17 I5": {
      "brand": "HP",
      "url": "---------------------------------HP GAMING 17 I5-----------------------------",
      "checkbox": false,
      "active": true,
      "condition":"new","presta_categories": "3,49,50,52,103,12,5,476"
    },
    "HP GAMING 17 I7": {
      "brand": "HP",
      "url": "------------------------------------HP GAMING 17 I7---------------------------",
      "checkbox": false,
      "active": true,
      "condition":"new","presta_categories": "3,49,50,52,103,12,6,477"
    },
    "HP GAMING 17 I9": {
      "brand": "HP",
      "url": "-------------------------------------HP GAMING 17 I9-------------------------",
      "checkbox": false,
      "active": true,
      "condition":"new","presta_categories": "3,49,50,52,103,12,7,478"
    },
    "HP GAMING 17 AMD": {
      "brand": "HP",
      "url": "------------------------------------HP GAMING 17 AMD--------------------------",
      "checkbox": false,
      "active": true,
      "condition":"new","presta_categories": "3,49,50,52,103,12,234,479"
    }
  }
}
"""
    return json.loads(json_data)


def test_cdata_categories_data_structure(cdata_categories_data):
    """
    Test the basic structure of the loaded JSON data.
    Verifies that the 'scenarios' key exists and is a dictionary.
    """
    assert "scenarios" in cdata_categories_data
    assert isinstance(cdata_categories_data["scenarios"], dict)

def test_cdata_categories_scenario_keys(cdata_categories_data):
    """
    Test that each scenario has the expected keys.
    Checks for the presence of required keys: 'brand', 'url', 'checkbox', 'active', 'condition', and 'presta_categories'.
    """
    for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
        assert "brand" in scenario_data
        assert "url" in scenario_data
        assert "checkbox" in scenario_data
        assert "active" in scenario_data
        assert "condition" in scenario_data
        assert "presta_categories" in scenario_data

def test_cdata_categories_scenario_values_types(cdata_categories_data):
    """
    Test that the values of keys in each scenario have the correct data types.
    Checks if 'brand' and 'url' are strings, 'checkbox' and 'active' are booleans, and 'presta_categories' is a string.
    """
    for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
        assert isinstance(scenario_data["brand"], str)
        assert isinstance(scenario_data["url"], str)
        assert isinstance(scenario_data["checkbox"], bool)
        assert isinstance(scenario_data["active"], bool)
        assert isinstance(scenario_data["condition"],str)
        assert isinstance(scenario_data["presta_categories"], str)


def test_cdata_categories_presta_categories_format(cdata_categories_data):
    """
     Test the format of the presta_categories string.
    Verifies that 'presta_categories' is a comma-separated string.
     """
    for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
        categories = scenario_data["presta_categories"]
        assert isinstance(categories, str)
        # Split by commas and check each value is a digit 
        for cat_id in categories.split(","):
          assert cat_id.strip().isdigit() or cat_id.strip() == "" 

def test_cdata_categories_active_boolean(cdata_categories_data):
    """
    Test that the 'active' key in each scenario is indeed a boolean.
    Ensures that all values for 'active' are either True or False.
    """
    for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
      assert isinstance(scenario_data["active"],bool)


def test_cdata_categories_checkbox_boolean(cdata_categories_data):
     """
    Test that the 'checkbox' key in each scenario is indeed a boolean.
    Ensures that all values for 'checkbox' are either True or False.
    """
     for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
      assert isinstance(scenario_data["checkbox"],bool)

def test_cdata_categories_condition_string(cdata_categories_data):
    """
     Test that the 'condition' key in each scenario is a string.
     Ensures that all values for 'condition' are strings.
     """
    for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
      assert isinstance(scenario_data["condition"],str)


def test_cdata_categories_scenario_data_not_empty(cdata_categories_data):
    """
    Test that the data inside the scenarios is not empty.
    Verifies that no string values are empty after stripping whitespace.
    """
    for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
      assert scenario_data["brand"].strip() != ""
      assert scenario_data["url"].strip() != ""
      assert scenario_data["condition"].strip() != ""
      assert scenario_data["presta_categories"].strip() != ""
```