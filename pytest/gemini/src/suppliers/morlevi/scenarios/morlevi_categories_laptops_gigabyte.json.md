```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def morlevi_categories_data():
    """Loads the morlevi categories data from the JSON file."""
    file_path = 'hypotez/src/suppliers/morlevi/scenarios/morlevi_categories_laptops_gigabyte.json'
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

# Test cases for the JSON structure and data

def test_scenarios_key_exists(morlevi_categories_data):
    """Checks if the 'scenarios' key exists in the JSON data."""
    assert "scenarios" in morlevi_categories_data, "The 'scenarios' key is missing from the JSON data."

def test_scenarios_is_dict(morlevi_categories_data):
    """Checks if 'scenarios' value is a dictionary."""
    assert isinstance(morlevi_categories_data["scenarios"], dict), "The 'scenarios' value is not a dictionary."

def test_scenario_keys(morlevi_categories_data):
    """Checks if all scenarios have the expected keys."""
    expected_keys = {"brand", "url", "checkbox", "active", "condition", "presta_categories"}
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert set(scenario_data.keys()) == expected_keys, f"Scenario '{scenario_name}' has missing or extra keys."

def test_scenario_brand_values(morlevi_categories_data):
    """Checks if all brand values are 'GIGABYTE'."""
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert scenario_data["brand"] == "GIGABYTE", f"Scenario '{scenario_name}' has incorrect brand value."

def test_scenario_checkbox_values(morlevi_categories_data):
    """Checks if all checkbox values are False."""
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
         assert scenario_data["checkbox"] == False, f"Scenario '{scenario_name}' has incorrect checkbox value."

def test_scenario_active_values(morlevi_categories_data):
    """Checks if all active values are True."""
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert scenario_data["active"] == True, f"Scenario '{scenario_name}' has incorrect active value."

def test_scenario_condition_values(morlevi_categories_data):
    """Checks if all condition values are 'new'."""
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert scenario_data["condition"] == "new", f"Scenario '{scenario_name}' has incorrect condition value."
        
def test_presta_categories_exists(morlevi_categories_data):
    """Checks if 'presta_categories' key exists and is a dictionary for each scenario"""
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert "presta_categories" in scenario_data, f"'presta_categories' key is missing in '{scenario_name}'"
        assert isinstance(scenario_data["presta_categories"], dict), f"'presta_categories' is not a dict in '{scenario_name}'"

def test_presta_categories_template_exists(morlevi_categories_data):
    """Checks if 'template' key exists and is a dictionary inside 'presta_categories' for each scenario"""
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert "template" in scenario_data["presta_categories"], f"'template' key is missing in 'presta_categories' of '{scenario_name}'"
        assert isinstance(scenario_data["presta_categories"]["template"], dict), f"'template' is not a dict in 'presta_categories' of '{scenario_name}'"

def test_presta_categories_gigabyte_exists(morlevi_categories_data):
      """Checks if 'gigabyte' key exists and is a list inside 'template' for each scenario"""
      for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
            assert "gigabyte" in scenario_data["presta_categories"]["template"], f"'gigabyte' key is missing in 'template' of '{scenario_name}'"
            assert isinstance(scenario_data["presta_categories"]["template"]["gigabyte"], list), f"'gigabyte' is not a list in 'template' of '{scenario_name}'"

def test_presta_categories_gigabyte_not_empty(morlevi_categories_data):
    """Checks if 'gigabyte' list is not empty for each scenario"""
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert len(scenario_data["presta_categories"]["template"]["gigabyte"]) > 0 , f"'gigabyte' list is empty in 'template' of '{scenario_name}'"

def test_presta_categories_gigabyte_length(morlevi_categories_data):
    """Checks if 'gigabyte' list contains 2 elements for each scenario"""
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
         assert len(scenario_data["presta_categories"]["template"]["gigabyte"]) == 2 , f"'gigabyte' list does not contain 2 elements in 'template' of '{scenario_name}'"
```