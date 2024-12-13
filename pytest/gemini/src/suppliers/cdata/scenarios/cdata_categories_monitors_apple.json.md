```python
import pytest
import json

# Fixture to load the json data
@pytest.fixture
def cdata_categories_data():
    """Loads the JSON data for testing."""
    json_data = """
{
  "scenarios": {
    "APPLE 18": {
      "brand": "APPLE",
      "url": "---------------------APPLE 18----------------------",
      "checkbox": false,
      "active": true,
      "condition":"new",
      "presta_categories": "127,241"
    },
    "APPLE 21.5": {
      "brand": "APPLE",
      "url": "---------------------APPLE 22----------------------",
      "checkbox": false,
      "active": true,
      "condition":"new",
      "presta_categories": "127,128"
    },
    "APPLE 23.5": {
      "brand": "APPLE",
      "url": "---------------------APPLE 24----------------------",
      "checkbox": false,
      "active": true,
      "condition":"new",
      "presta_categories": "127,129"
    },
    "APPLE 27": {
      "brand": "APPLE",
      "url": "---------------------APPLE 27----------------------",
      "checkbox": false,
      "active": true,
      "condition":"new",
      "presta_categories": "127,130"
    },
    "APPLE 31": {
      "brand": "APPLE",
      "url": "https://reseller.c-data.co.il/%D7%9E%D7%A1%D7%9B%D7%99%D7%9D#/specFilters=215m!#-!6360&manFilters=3",
      "checkbox": false,
      "active": true,
      "condition":"new",
      "presta_categories": "127,131"
    },
    "APPLE 34": {
      "brand": "APPLE",
      "url": "---------------------APPLE 34----------------------",
      "checkbox": false,
      "active": true,
      "condition":"new",
      "presta_categories": "127,132"
    },
    "APPLE 49": {
      "brand": "APPLE",
      "url": "---------------------APPLE 49----------------------",
      "checkbox": false,
      "active": true,
      "condition":"new",
      "presta_categories": "127,133"
    }
  }
}
"""
    return json.loads(json_data)

def test_cdata_categories_data_structure(cdata_categories_data):
    """Checks if the loaded data has the correct structure."""
    assert "scenarios" in cdata_categories_data, "The JSON should have a 'scenarios' key"
    assert isinstance(cdata_categories_data["scenarios"], dict), "'scenarios' should be a dictionary"

def test_cdata_categories_scenario_keys(cdata_categories_data):
    """Checks if each scenario has the expected keys."""
    for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
        assert "brand" in scenario_data, f"Scenario {scenario_name} missing 'brand'"
        assert "url" in scenario_data, f"Scenario {scenario_name} missing 'url'"
        assert "checkbox" in scenario_data, f"Scenario {scenario_name} missing 'checkbox'"
        assert "active" in scenario_data, f"Scenario {scenario_name} missing 'active'"
        assert "condition" in scenario_data, f"Scenario {scenario_name} missing 'condition'"
        assert "presta_categories" in scenario_data, f"Scenario {scenario_name} missing 'presta_categories'"

def test_cdata_categories_scenario_values_types(cdata_categories_data):
    """Checks the types of values in each scenario."""
    for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
        assert isinstance(scenario_data["brand"], str), f"'brand' in {scenario_name} should be a string"
        assert isinstance(scenario_data["url"], str), f"'url' in {scenario_name} should be a string"
        assert isinstance(scenario_data["checkbox"], bool), f"'checkbox' in {scenario_name} should be a boolean"
        assert isinstance(scenario_data["active"], bool), f"'active' in {scenario_name} should be a boolean"
        assert isinstance(scenario_data["condition"], str), f"'condition' in {scenario_name} should be a string"
        assert isinstance(scenario_data["presta_categories"], str), f"'presta_categories' in {scenario_name} should be a string"

def test_cdata_categories_scenario_brand_value(cdata_categories_data):
    """Checks if 'brand' is always 'APPLE'."""
    for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
        assert scenario_data["brand"] == "APPLE", f"'brand' in {scenario_name} should be 'APPLE'"

def test_cdata_categories_scenario_active_value(cdata_categories_data):
    """Checks if 'active' is always True."""
    for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
        assert scenario_data["active"] == True, f"'active' in {scenario_name} should be True"
        
def test_cdata_categories_scenario_condition_value(cdata_categories_data):
    """Checks if 'condition' is always 'new'."""
    for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
        assert scenario_data["condition"] == "new", f"'condition' in {scenario_name} should be 'new'"

def test_cdata_categories_scenario_checkbox_value(cdata_categories_data):
     """Checks if 'checkbox' is always False."""
     for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
          assert scenario_data["checkbox"] == False, f"'checkbox' in {scenario_name} should be False"

def test_cdata_categories_scenario_url_not_empty(cdata_categories_data):
    """Checks if the URL is not an empty string."""
    for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
        assert scenario_data["url"] != "", f"'url' in {scenario_name} should not be empty"

def test_cdata_categories_presta_categories_not_empty(cdata_categories_data):
     """Checks if 'presta_categories' is not an empty string."""
     for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
          assert scenario_data["presta_categories"] != "", f"'presta_categories' in {scenario_name} should not be empty"
```