```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def category_data():
    """Provides the loaded JSON data for testing."""
    file_path = 'hypotez/src/suppliers/ivory/scenarios/morlevi_categories_storage_wd.json'
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

# Test cases for structure and data integrity
def test_scenarios_key_exists(category_data):
    """Checks if the 'scenarios' key exists in the loaded data."""
    assert 'scenarios' in category_data, "The 'scenarios' key is missing."

def test_scenarios_is_dict(category_data):
    """Checks if 'scenarios' is a dictionary."""
    assert isinstance(category_data['scenarios'], dict), "'scenarios' is not a dictionary."

def test_scenario_keys_exist(category_data):
    """Checks if all scenarios have the required keys."""
    required_keys = ["brand", "name", "url", "checkbox", "active", "condition", "presta_categories"]
    for scenario_name, scenario_data in category_data['scenarios'].items():
      for key in required_keys:
        assert key in scenario_data, f"Scenario '{scenario_name}' is missing key: {key}"

def test_scenario_values_types(category_data):
    """Checks if scenario values are of the expected type."""
    for scenario_name, scenario_data in category_data['scenarios'].items():
        assert isinstance(scenario_data['brand'], str), f"Scenario '{scenario_name}' brand is not a string."
        assert isinstance(scenario_data['name'], str), f"Scenario '{scenario_name}' name is not a string."
        assert isinstance(scenario_data['url'], str), f"Scenario '{scenario_name}' url is not a string."
        assert isinstance(scenario_data['checkbox'], bool), f"Scenario '{scenario_name}' checkbox is not a boolean."
        assert isinstance(scenario_data['active'], bool), f"Scenario '{scenario_name}' active is not a boolean."
        assert isinstance(scenario_data['condition'], str), f"Scenario '{scenario_name}' condition is not a string."
        assert isinstance(scenario_data['presta_categories'], str), f"Scenario '{scenario_name}' presta_categories is not a string."

def test_scenario_active_value(category_data):
    """Checks if all scenarios active values are True"""
    for scenario_name, scenario_data in category_data['scenarios'].items():
        assert scenario_data['active'] == True ,f"Scenario '{scenario_name}' active is not True"

def test_scenario_condition_value(category_data):
    """Checks if all scenarios condition values are 'new'"""
    for scenario_name, scenario_data in category_data['scenarios'].items():
        assert scenario_data['condition'] == 'new' ,f"Scenario '{scenario_name}' condition is not 'new'"

def test_presta_categories_format(category_data):
    """Checks if presta_categories values are comma-separated strings of integers."""
    for scenario_name, scenario_data in category_data['scenarios'].items():
        categories = scenario_data['presta_categories'].split(',')
        for category in categories:
            assert category.isdigit(), f"Scenario '{scenario_name}' presta_categories '{category}' is not a digit."
        
def test_scenario_name_not_empty(category_data):
    """Checks if all scenario names are not empty"""
    for scenario_name, scenario_data in category_data['scenarios'].items():
        assert scenario_data['name'] != "", f"Scenario '{scenario_name}' name is empty."

def test_scenario_brand_not_empty(category_data):
    """Checks if all scenario brands are not empty"""
    for scenario_name, scenario_data in category_data['scenarios'].items():
        assert scenario_data['brand'] != "", f"Scenario '{scenario_name}' brand is empty."

def test_scenario_url_not_empty(category_data):
    """Checks if all scenario urls are not empty"""
    for scenario_name, scenario_data in category_data['scenarios'].items():
        assert scenario_data['url'] != "", f"Scenario '{scenario_name}' url is empty."
```