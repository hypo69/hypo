```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def morlevi_categories_data():
    """Loads the morlevi categories data from the JSON file."""
    with open('hypotez/src/suppliers/ivory/scenarios/morlevi_categories_storage_crucial.json', 'r') as f:
        data = json.load(f)
    return data


def test_scenarios_exist(morlevi_categories_data):
    """Checks if the 'scenarios' key exists in the loaded data."""
    assert "scenarios" in morlevi_categories_data, "The 'scenarios' key is missing in the JSON data."


def test_scenarios_not_empty(morlevi_categories_data):
    """Checks if the 'scenarios' dictionary is not empty."""
    assert morlevi_categories_data["scenarios"], "The 'scenarios' dictionary is empty."


def test_scenario_keys_exist(morlevi_categories_data):
    """Checks if each scenario has required keys."""
    required_keys = ["brand", "name", "url", "checkbox", "active", "condition", "presta_categories"]
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        for key in required_keys:
            assert key in scenario_data, f"Scenario '{scenario_name}' is missing the key: '{key}'."


def test_scenario_brand_value(morlevi_categories_data):
    """Checks if the brand value is always 'CRUCIAL'."""
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
         assert scenario_data["brand"] == "CRUCIAL", f"Scenario '{scenario_name}' has an invalid brand: '{scenario_data['brand']}'."


def test_scenario_active_is_boolean(morlevi_categories_data):
    """Checks if the active key value is boolean"""
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert isinstance(scenario_data["active"], bool), f"Scenario '{scenario_name}' has an invalid 'active' value, it's not boolean: '{scenario_data['active']}'."


def test_scenario_checkbox_is_boolean(morlevi_categories_data):
    """Checks if the checkbox key value is boolean"""
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert isinstance(scenario_data["checkbox"], bool), f"Scenario '{scenario_name}' has an invalid 'checkbox' value, it's not boolean: '{scenario_data['checkbox']}'."


def test_scenario_condition_is_new(morlevi_categories_data):
    """Checks if the condition key value is new"""
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert scenario_data["condition"] == "new", f"Scenario '{scenario_name}' has an invalid 'condition' value, it's not 'new': '{scenario_data['condition']}'."

def test_scenario_presta_categories_is_string(morlevi_categories_data):
    """Checks if presta_categories is string """
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
         assert isinstance(scenario_data["presta_categories"], str), f"Scenario '{scenario_name}' has an invalid 'presta_categories' value, it's not string: '{scenario_data['presta_categories']}'."

def test_scenario_url_is_string(morlevi_categories_data):
    """Checks if url is string """
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
         assert isinstance(scenario_data["url"], str), f"Scenario '{scenario_name}' has an invalid 'url' value, it's not string: '{scenario_data['url']}'."
```