```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def morlevi_categories_data():
    """Loads the morlevi categories data from the JSON file."""
    file_path = "hypotez/src/suppliers/morlevi/scenarios/morlevi_categories_storage_wd.json"
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

# Test cases for the structure of the loaded data
def test_data_is_loaded(morlevi_categories_data):
    """Test that the data is loaded correctly and is a dictionary."""
    assert isinstance(morlevi_categories_data, dict), "Data loaded should be a dictionary"

def test_data_has_scenarios_key(morlevi_categories_data):
    """Test that the loaded dictionary has the 'scenarios' key."""
    assert 'scenarios' in morlevi_categories_data, "The 'scenarios' key should be present in the data"

def test_scenarios_is_dict(morlevi_categories_data):
      """Test that the 'scenarios' key contains a dictionary."""
      assert isinstance(morlevi_categories_data['scenarios'], dict), "The 'scenarios' value should be a dictionary"


def test_scenarios_not_empty(morlevi_categories_data):
    """Test that the 'scenarios' dictionary is not empty."""
    assert morlevi_categories_data['scenarios'], "The 'scenarios' dictionary should not be empty"

# Test cases for individual scenario structure and data types
def test_scenario_keys(morlevi_categories_data):
    """Test that each scenario has the expected keys and their values are of the correct types."""
    for scenario_name, scenario_data in morlevi_categories_data['scenarios'].items():
        assert isinstance(scenario_data, dict), f"Scenario '{scenario_name}' should be a dictionary"
        assert 'brand' in scenario_data, f"Scenario '{scenario_name}' should have a 'brand' key"
        assert isinstance(scenario_data['brand'], str), f"Scenario '{scenario_name}' brand should be a string"
        assert 'name' in scenario_data, f"Scenario '{scenario_name}' should have a 'name' key"
        assert isinstance(scenario_data['name'], str), f"Scenario '{scenario_name}' name should be a string"
        assert 'url' in scenario_data, f"Scenario '{scenario_name}' should have a 'url' key"
        assert isinstance(scenario_data['url'], str), f"Scenario '{scenario_name}' url should be a string"
        assert 'checkbox' in scenario_data, f"Scenario '{scenario_name}' should have a 'checkbox' key"
        assert isinstance(scenario_data['checkbox'], bool), f"Scenario '{scenario_name}' checkbox should be a boolean"
        assert 'active' in scenario_data, f"Scenario '{scenario_name}' should have an 'active' key"
        assert isinstance(scenario_data['active'], bool), f"Scenario '{scenario_name}' active should be a boolean"
        assert 'condition' in scenario_data, f"Scenario '{scenario_name}' should have a 'condition' key"
        assert isinstance(scenario_data['condition'], str), f"Scenario '{scenario_name}' condition should be a string"
        assert 'presta_categories' in scenario_data, f"Scenario '{scenario_name}' should have a 'presta_categories' key"
        assert isinstance(scenario_data['presta_categories'], str), f"Scenario '{scenario_name}' presta_categories should be a string"

# Test cases for checking specific data values, edge cases and format

def test_presta_categories_format(morlevi_categories_data):
    """ Test that 'presta_categories' is a comma-separated string of digits"""
    for scenario_name, scenario_data in morlevi_categories_data['scenarios'].items():
        categories = scenario_data['presta_categories']
        assert all(cat.isdigit() for cat in categories.split(',')), f"'{scenario_name} presta_categories' should be comma separated digits"

def test_brand_is_western_digital(morlevi_categories_data):
    """ Test that the 'brand' is always "WESTERN DIGITAL" """
    for scenario_name, scenario_data in morlevi_categories_data['scenarios'].items():
        assert scenario_data['brand'] == "WESTERN DIGITAL", f"Scenario '{scenario_name}' brand should be WESTERN DIGITAL"

def test_url_is_string(morlevi_categories_data):
     """Test that the url is string."""
     for scenario_name, scenario_data in morlevi_categories_data['scenarios'].items():
        assert isinstance(scenario_data['url'],str), f"Scenario '{scenario_name}' url should be a string"
```