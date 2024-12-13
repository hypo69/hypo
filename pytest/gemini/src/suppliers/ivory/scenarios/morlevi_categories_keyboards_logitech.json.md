```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def morlevi_categories_data():
    """Loads the JSON data from the file."""
    file_path = "hypotez/src/suppliers/ivory/scenarios/morlevi_categories_keyboards_logitech.json"
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

# Test cases for the data structure
def test_scenarios_exists(morlevi_categories_data):
    """Checks if the 'scenarios' key exists in the loaded data."""
    assert "scenarios" in morlevi_categories_data, "The 'scenarios' key should be present in the JSON data."

def test_scenarios_not_empty(morlevi_categories_data):
    """Checks if the 'scenarios' dictionary is not empty."""
    assert morlevi_categories_data["scenarios"], "The 'scenarios' dictionary should not be empty."

def test_scenario_structure(morlevi_categories_data):
    """Checks the structure of a single scenario item."""
    scenarios = morlevi_categories_data["scenarios"]
    for scenario_name, scenario_data in scenarios.items():
         assert "brand" in scenario_data, f"Scenario '{scenario_name}' missing 'brand' key."
         assert "url" in scenario_data, f"Scenario '{scenario_name}' missing 'url' key."
         assert "checkbox" in scenario_data, f"Scenario '{scenario_name}' missing 'checkbox' key."
         assert "active" in scenario_data, f"Scenario '{scenario_name}' missing 'active' key."
         assert "condition" in scenario_data, f"Scenario '{scenario_name}' missing 'condition' key."
         assert "presta_categories" in scenario_data, f"Scenario '{scenario_name}' missing 'presta_categories' key."

def test_scenario_brand_type(morlevi_categories_data):
    """Checks that the brand is a string."""
    scenarios = morlevi_categories_data["scenarios"]
    for scenario_name, scenario_data in scenarios.items():
        assert isinstance(scenario_data["brand"], str), f"Scenario '{scenario_name}' 'brand' should be a string."

def test_scenario_url_type(morlevi_categories_data):
    """Checks that the URL is a string."""
    scenarios = morlevi_categories_data["scenarios"]
    for scenario_name, scenario_data in scenarios.items():
         assert isinstance(scenario_data["url"], str), f"Scenario '{scenario_name}' 'url' should be a string."

def test_scenario_checkbox_type(morlevi_categories_data):
    """Checks that the checkbox is a boolean."""
    scenarios = morlevi_categories_data["scenarios"]
    for scenario_name, scenario_data in scenarios.items():
         assert isinstance(scenario_data["checkbox"], bool), f"Scenario '{scenario_name}' 'checkbox' should be a boolean."

def test_scenario_active_type(morlevi_categories_data):
    """Checks that the active is a boolean."""
    scenarios = morlevi_categories_data["scenarios"]
    for scenario_name, scenario_data in scenarios.items():
         assert isinstance(scenario_data["active"], bool), f"Scenario '{scenario_name}' 'active' should be a boolean."

def test_scenario_condition_type(morlevi_categories_data):
    """Checks that the condition is a string."""
    scenarios = morlevi_categories_data["scenarios"]
    for scenario_name, scenario_data in scenarios.items():
        assert isinstance(scenario_data["condition"], str), f"Scenario '{scenario_name}' 'condition' should be a string."

def test_scenario_presta_categories_type(morlevi_categories_data):
    """Checks that the presta_categories is a string."""
    scenarios = morlevi_categories_data["scenarios"]
    for scenario_name, scenario_data in scenarios.items():
         assert isinstance(scenario_data["presta_categories"], str), f"Scenario '{scenario_name}' 'presta_categories' should be a string."

def test_presta_categories_valid_format(morlevi_categories_data):
     """Checks that the presta_categories are comma-separated strings."""
     scenarios = morlevi_categories_data["scenarios"]
     for scenario_name, scenario_data in scenarios.items():
        categories = scenario_data["presta_categories"]
        assert all(cat.strip().isdigit() for cat in categories.split(',')), f"Scenario '{scenario_name}': 'presta_categories' should be comma-separated numbers"
        

def test_scenario_data_values(morlevi_categories_data):
    """Checks specific values within the scenario data."""
    scenarios = morlevi_categories_data["scenarios"]
    
    # Example 1: Check brand for 'LOGITECH WIRELESS KEYBOARD'
    assert scenarios["LOGITECH WIRELESS KEYBOARD"]["brand"] == "LOGITECH"
    
    # Example 2: Check url for 'LOGITECH USB MOUSE'
    assert scenarios["LOGITECH USB MOUSE"]["url"] == "https://www.morlevi.co.il/Cat/108?p_315=29&sort=datafloat2%2Cprice&keyword="
    
    # Example 3: Check checkbox for 'LOGITECH GAMING  KEYBOARD'
    assert scenarios["LOGITECH GAMING  KEYBOARD"]["checkbox"] == False

    # Example 4: Check active for 'LOGITECH USB KEYBOARD'
    assert scenarios["LOGITECH USB KEYBOARD"]["active"] == True
    
    # Example 5: Check condition for 'LOGITECH WIRELESS MOUSE'
    assert scenarios["LOGITECH WIRELESS MOUSE"]["condition"] == "new"
    
    # Example 6: Check presta_categories for 'LOGITECH WIRELESS  KEYBOARD-MOUSE SET'
    assert scenarios["LOGITECH WIRELESS  KEYBOARD-MOUSE SET"]["presta_categories"] == "203,207,334"
```