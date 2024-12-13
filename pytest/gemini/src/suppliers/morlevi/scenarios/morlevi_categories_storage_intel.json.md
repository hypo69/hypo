```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def morlevi_categories_data():
    """Loads the morlevi_categories_storage_intel.json data."""
    file_path = 'hypotez/src/suppliers/morlevi/scenarios/morlevi_categories_storage_intel.json'
    with open(file_path, 'r') as f:
        return json.load(f)

# Test cases for data structure and validity
def test_scenarios_key_exists(morlevi_categories_data):
    """Verify that the 'scenarios' key exists in the data."""
    assert 'scenarios' in morlevi_categories_data, "The 'scenarios' key is missing in the JSON data."

def test_scenarios_is_dict(morlevi_categories_data):
    """Verify that 'scenarios' is a dictionary."""
    assert isinstance(morlevi_categories_data['scenarios'], dict), "The 'scenarios' value is not a dictionary."

def test_scenario_keys_exist(morlevi_categories_data):
    """Verify that each scenario has the required keys."""
    required_keys = ["brand", "name", "url", "checkbox", "active", "condition", "presta_categories"]
    for scenario_name, scenario_data in morlevi_categories_data['scenarios'].items():
        for key in required_keys:
            assert key in scenario_data, f"Scenario '{scenario_name}' is missing key '{key}'."

def test_scenario_values_type(morlevi_categories_data):
     """Verify the type of values in each scenario."""
     for scenario_name, scenario_data in morlevi_categories_data['scenarios'].items():
        assert isinstance(scenario_data["brand"], str), f"Scenario '{scenario_name}' 'brand' is not a string."
        assert isinstance(scenario_data["name"], str), f"Scenario '{scenario_name}' 'name' is not a string."
        assert isinstance(scenario_data["url"], str), f"Scenario '{scenario_name}' 'url' is not a string."
        assert isinstance(scenario_data["checkbox"], bool), f"Scenario '{scenario_name}' 'checkbox' is not a boolean."
        assert isinstance(scenario_data["active"], bool), f"Scenario '{scenario_name}' 'active' is not a boolean."
        assert isinstance(scenario_data["condition"], str), f"Scenario '{scenario_name}' 'condition' is not a string."
        assert isinstance(scenario_data["presta_categories"], str), f"Scenario '{scenario_name}' 'presta_categories' is not a string."

def test_presta_categories_are_comma_separated(morlevi_categories_data):
    """Verify that 'presta_categories' is a comma separated string of digits"""
    for scenario_name, scenario_data in morlevi_categories_data['scenarios'].items():
        presta_categories = scenario_data['presta_categories']
        categories = presta_categories.split(',')
        for category in categories:
            assert category.isdigit(), f"Scenario '{scenario_name}' 'presta_categories' contains non-digit value: '{category}'"

def test_active_values_are_boolean(morlevi_categories_data):
    """Verify that 'active' values are booleans."""
    for scenario_name, scenario_data in morlevi_categories_data['scenarios'].items():
        assert isinstance(scenario_data['active'], bool), f"Scenario '{scenario_name}' 'active' value is not a boolean."

def test_checkbox_values_are_boolean(morlevi_categories_data):
    """Verify that 'checkbox' values are booleans."""
    for scenario_name, scenario_data in morlevi_categories_data['scenarios'].items():
        assert isinstance(scenario_data['checkbox'], bool), f"Scenario '{scenario_name}' 'checkbox' value is not a boolean."

def test_brand_is_intel(morlevi_categories_data):
    """Verify that all the brands are INTEL"""
    for scenario_name, scenario_data in morlevi_categories_data['scenarios'].items():
        assert scenario_data['brand'] == "INTEL", f"Scenario '{scenario_name}' has a brand other than INTEL"
```