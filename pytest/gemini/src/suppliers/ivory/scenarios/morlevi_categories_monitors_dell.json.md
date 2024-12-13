```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def load_test_data():
    """Loads the JSON data from the specified file."""
    file_path = "hypotez/src/suppliers/ivory/scenarios/morlevi_categories_monitors_dell.json"
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

# Test cases for the structure of the loaded JSON
def test_json_structure(load_test_data):
    """Checks if the loaded JSON has the expected structure with a 'scenarios' key."""
    data = load_test_data
    assert "scenarios" in data, "The JSON should have a 'scenarios' key."
    assert isinstance(data["scenarios"], dict), "'scenarios' should be a dictionary."

# Test cases for individual scenarios within the JSON data
def test_scenario_structure(load_test_data):
    """Checks if each scenario in 'scenarios' has the correct keys and value types."""
    data = load_test_data
    scenarios = data["scenarios"]
    
    for scenario_name, scenario_data in scenarios.items():
        assert isinstance(scenario_data, dict), f"Scenario '{scenario_name}' should be a dictionary."
        assert "brand" in scenario_data, f"Scenario '{scenario_name}' is missing 'brand' key."
        assert "url" in scenario_data, f"Scenario '{scenario_name}' is missing 'url' key."
        assert "checkbox" in scenario_data, f"Scenario '{scenario_name}' is missing 'checkbox' key."
        assert "active" in scenario_data, f"Scenario '{scenario_name}' is missing 'active' key."
        assert "condition" in scenario_data, f"Scenario '{scenario_name}' is missing 'condition' key."
        assert "presta_categories" in scenario_data, f"Scenario '{scenario_name}' is missing 'presta_categories' key."

        assert isinstance(scenario_data["brand"], str), f"Scenario '{scenario_name}' 'brand' should be a string."
        assert isinstance(scenario_data["url"], str), f"Scenario '{scenario_name}' 'url' should be a string."
        assert isinstance(scenario_data["checkbox"], bool), f"Scenario '{scenario_name}' 'checkbox' should be a boolean."
        assert isinstance(scenario_data["active"], bool), f"Scenario '{scenario_name}' 'active' should be a boolean."
        assert isinstance(scenario_data["condition"], str), f"Scenario '{scenario_name}' 'condition' should be a string."
        assert isinstance(scenario_data["presta_categories"], str), f"Scenario '{scenario_name}' 'presta_categories' should be a string."

def test_scenario_values(load_test_data):
    """
    Checks specific values within the loaded data to make sure they are correct
    """
    data = load_test_data
    scenarios = data["scenarios"]
    
    #check brand and category
    for scenario_name, scenario_data in scenarios.items():
        assert scenario_data["brand"] == "DELL", f"Scenario '{scenario_name}' has wrong brand value"
        assert "127" in scenario_data["presta_categories"], f"Scenario '{scenario_name}' has wrong categories value"
        assert "528" in scenario_data["presta_categories"], f"Scenario '{scenario_name}' has wrong categories value"
    
    # check active and checkbox
    for scenario_name, scenario_data in scenarios.items():
        assert scenario_data["active"] == True, f"Scenario '{scenario_name}' should be active"
        assert scenario_data["checkbox"] == False, f"Scenario '{scenario_name}' should be unchecked"

    # check urls
    assert "https://www.morlevi.co.il/Cat/8?p_315=7&p_350=1807&p_75=483&p_75=292&p_75=293&sort=datafloat2%2Cprice&keyword=" in scenarios["DELL 24-25"]["url"]
    assert "https://www.morlevi.co.il/Cat/8?p_315=7&p_350=1808&p_75=297&sort=datafloat2%2Cprice&keyword=" in scenarios["DELL 27-29"]["url"]
    assert "https://www.morlevi.co.il/Cat/8?p_315=7&p_350=1809&p_75=298&sort=datafloat2%2Cprice&keyword=" in scenarios["DELL 32"]["url"]


def test_condition_values(load_test_data):
    """
    Checks if the 'condition' is always 'new' in all scenarios
    """
    data = load_test_data
    scenarios = data["scenarios"]
    for scenario_name, scenario_data in scenarios.items():
         assert scenario_data["condition"] == "new", f"Scenario '{scenario_name}' condition should be equal to 'new'"


def test_presta_categories_format(load_test_data):
    """
    Checks if 'presta_categories' contains only digits and commas.
    """
    data = load_test_data
    scenarios = data["scenarios"]
    for scenario_name, scenario_data in scenarios.items():
        categories = scenario_data["presta_categories"]
        assert all(c.isdigit() or c == ',' for c in categories), f"Scenario '{scenario_name}' has invalid characters in 'presta_categories'."

```