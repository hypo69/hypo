```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def morlevi_categories_data():
    """Loads the morlevi_categories_storage_intel.json data."""
    with open("hypotez/src/suppliers/ivory/scenarios/morlevi_categories_storage_intel.json", "r") as f:
        return json.load(f)

def test_morlevi_categories_data_is_dict(morlevi_categories_data):
    """Verify that the loaded data is a dictionary."""
    assert isinstance(morlevi_categories_data, dict), "The loaded data should be a dictionary."

def test_morlevi_categories_has_scenarios_key(morlevi_categories_data):
    """Verify the 'scenarios' key exists."""
    assert "scenarios" in morlevi_categories_data, "The 'scenarios' key should exist in the data."

def test_morlevi_scenarios_is_dict(morlevi_categories_data):
      """Verify that the loaded scenarios data is a dictionary."""
      assert isinstance(morlevi_categories_data["scenarios"], dict), "The 'scenarios' data should be a dictionary."

def test_morlevi_scenario_keys_are_strings(morlevi_categories_data):
    """Verify that all keys in the scenarios are strings."""
    for key in morlevi_categories_data["scenarios"].keys():
        assert isinstance(key, str), f"The scenario key '{key}' should be a string."

def test_morlevi_scenario_values_are_dicts(morlevi_categories_data):
    """Verify that all values in the scenarios are dictionaries."""
    for value in morlevi_categories_data["scenarios"].values():
      assert isinstance(value, dict), f"The scenario value '{value}' should be a dictionary."


def test_morlevi_scenario_contains_required_keys(morlevi_categories_data):
    """Verify that each scenario has the required keys."""
    required_keys = ["brand", "name", "url", "checkbox", "active", "condition", "presta_categories"]
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        for key in required_keys:
            assert key in scenario_data, f"Scenario '{scenario_name}' is missing key '{key}'"

def test_morlevi_scenario_brand_is_string(morlevi_categories_data):
     """Verify that the 'brand' value is a string for all scenarios."""
     for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
          assert isinstance(scenario_data["brand"], str), f"Brand in scenario '{scenario_name}' should be a string"

def test_morlevi_scenario_name_is_string(morlevi_categories_data):
     """Verify that the 'name' value is a string for all scenarios."""
     for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
          assert isinstance(scenario_data["name"], str), f"Name in scenario '{scenario_name}' should be a string"

def test_morlevi_scenario_url_is_string(morlevi_categories_data):
     """Verify that the 'url' value is a string for all scenarios."""
     for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
          assert isinstance(scenario_data["url"], str), f"URL in scenario '{scenario_name}' should be a string"

def test_morlevi_scenario_checkbox_is_bool(morlevi_categories_data):
    """Verify that the 'checkbox' value is a boolean for all scenarios."""
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert isinstance(scenario_data["checkbox"], bool), f"Checkbox in scenario '{scenario_name}' should be a boolean"

def test_morlevi_scenario_active_is_bool(morlevi_categories_data):
    """Verify that the 'active' value is a boolean for all scenarios."""
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert isinstance(scenario_data["active"], bool), f"Active in scenario '{scenario_name}' should be a boolean"

def test_morlevi_scenario_condition_is_string(morlevi_categories_data):
     """Verify that the 'condition' value is a string for all scenarios."""
     for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
          assert isinstance(scenario_data["condition"], str), f"condition in scenario '{scenario_name}' should be a string"


def test_morlevi_scenario_presta_categories_is_string(morlevi_categories_data):
    """Verify that the 'presta_categories' value is a string for all scenarios."""
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert isinstance(scenario_data["presta_categories"], str), f"'presta_categories' in scenario '{scenario_name}' should be a string"

def test_morlevi_scenario_presta_categories_valid_format(morlevi_categories_data):
    """Verify that 'presta_categories' contains only comma-separated numbers."""
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        categories_str = scenario_data["presta_categories"]
        categories = categories_str.split(',')
        for cat in categories:
             assert cat.isdigit(), f"'presta_categories' in scenario '{scenario_name}' contains non-numeric characters"

def test_morlevi_scenario_brand_is_intel(morlevi_categories_data):
     """Verify that the 'brand' value is 'INTEL' for all scenarios."""
     for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
          assert scenario_data["brand"] == "INTEL", f"Brand in scenario '{scenario_name}' should be INTEL"


def test_morlevi_scenario_has_at_least_one_scenario(morlevi_categories_data):
    """Verify that there is at least one scenario in the data."""
    assert len(morlevi_categories_data["scenarios"]) > 0, "There should be at least one scenario in the data."


def test_morlevi_scenario_no_empty_strings(morlevi_categories_data):
    """Verify that no string values are empty."""
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
         for key, value in scenario_data.items():
             if isinstance(value, str):
                 assert value != "", f"String value for key '{key}' in scenario '{scenario_name}' should not be empty."
```