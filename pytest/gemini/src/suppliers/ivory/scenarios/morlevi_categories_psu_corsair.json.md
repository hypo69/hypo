```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def load_data():
    """Loads the JSON data from the file."""
    file_path = "hypotez/src/suppliers/ivory/scenarios/morlevi_categories_psu_corsair.json"
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def test_scenarios_exist(load_data):
    """Checks if the 'scenarios' key exists in the loaded data."""
    assert 'scenarios' in load_data, "The 'scenarios' key is missing in the JSON data."

def test_scenario_keys_exist(load_data):
    """Checks if each scenario has the expected keys."""
    scenarios = load_data.get('scenarios', {})
    for scenario_name, scenario_data in scenarios.items():
        assert 'brand' in scenario_data, f"Scenario '{scenario_name}' is missing the 'brand' key."
        assert 'name' in scenario_data, f"Scenario '{scenario_name}' is missing the 'name' key."
        assert 'url' in scenario_data, f"Scenario '{scenario_name}' is missing the 'url' key."
        assert 'checkbox' in scenario_data, f"Scenario '{scenario_name}' is missing the 'checkbox' key."
        assert 'active' in scenario_data, f"Scenario '{scenario_name}' is missing the 'active' key."
        assert 'condition' in scenario_data, f"Scenario '{scenario_name}' is missing the 'condition' key."
        assert 'presta_categories' in scenario_data, f"Scenario '{scenario_name}' is missing the 'presta_categories' key."

def test_scenario_brand_value(load_data):
    """Checks if all scenario brands are 'CORSAIR'."""
    scenarios = load_data.get('scenarios', {})
    for scenario_name, scenario_data in scenarios.items():
      assert scenario_data['brand'] == "CORSAIR", f"Scenario '{scenario_name}' has an incorrect brand."

def test_scenario_name_value_is_string(load_data):
     """Checks if all scenario names are strings."""
     scenarios = load_data.get('scenarios', {})
     for scenario_name, scenario_data in scenarios.items():
         assert isinstance(scenario_data['name'], str), f"Scenario '{scenario_name}' has a name that is not a string."

def test_scenario_url_value_is_string(load_data):
    """Checks if all scenario urls are strings."""
    scenarios = load_data.get('scenarios', {})
    for scenario_name, scenario_data in scenarios.items():
        assert isinstance(scenario_data['url'], str), f"Scenario '{scenario_name}' has a url that is not a string."
        
def test_scenario_checkbox_value_is_boolean(load_data):
    """Checks if all scenario checkbox values are booleans."""
    scenarios = load_data.get('scenarios', {})
    for scenario_name, scenario_data in scenarios.items():
        assert isinstance(scenario_data['checkbox'], bool), f"Scenario '{scenario_name}' has a checkbox value that is not a boolean."

def test_scenario_active_value_is_boolean(load_data):
    """Checks if all scenario active values are booleans."""
    scenarios = load_data.get('scenarios', {})
    for scenario_name, scenario_data in scenarios.items():
        assert isinstance(scenario_data['active'], bool), f"Scenario '{scenario_name}' has an active value that is not a boolean."

def test_scenario_condition_value(load_data):
    """Checks if all scenario condition values are equal 'new'."""
    scenarios = load_data.get('scenarios', {})
    for scenario_name, scenario_data in scenarios.items():
      assert scenario_data['condition'] == "new", f"Scenario '{scenario_name}' has an incorrect condition."
      
def test_scenario_presta_categories_value_is_string(load_data):
    """Checks if all scenario presta_categories values are strings."""
    scenarios = load_data.get('scenarios', {})
    for scenario_name, scenario_data in scenarios.items():
         assert isinstance(scenario_data['presta_categories'], str), f"Scenario '{scenario_name}' has a presta_categories value that is not a string."
```