```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def morlevi_categories_data():
    """Loads the morlevi categories data from the JSON file."""
    file_path = 'hypotez/src/suppliers/morlevi/scenarios/morlevi_categories_psu_cooler_maser.json'
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

# Test case for checking the presence of scenarios key
def test_scenarios_key_exists(morlevi_categories_data):
    """Checks if the 'scenarios' key exists in the loaded data."""
    assert 'scenarios' in morlevi_categories_data, "The 'scenarios' key is missing."

# Test case for checking if scenarios is not empty
def test_scenarios_not_empty(morlevi_categories_data):
    """Checks if the 'scenarios' dictionary is not empty."""
    assert morlevi_categories_data['scenarios'], "The 'scenarios' dictionary is empty."


# Test case for checking if each scenario has all required keys
def test_scenario_keys_presence(morlevi_categories_data):
    """Checks if each scenario has all the required keys ('brand', 'name', 'url', 'checkbox', 'active', 'condition','presta_categories')."""
    required_keys = ['brand', 'name', 'url', 'checkbox', 'active', 'condition','presta_categories']
    for scenario_name, scenario_data in morlevi_categories_data['scenarios'].items():
        for key in required_keys:
            assert key in scenario_data, f"Scenario '{scenario_name}' is missing the key '{key}'."

# Test case for checking if brand is a string and not empty
def test_scenario_brand_is_valid_string(morlevi_categories_data):
     """Checks if the 'brand' value in each scenario is a non-empty string."""
     for scenario_name, scenario_data in morlevi_categories_data['scenarios'].items():
         assert isinstance(scenario_data['brand'], str), f"Scenario '{scenario_name}' brand is not a string"
         assert scenario_data['brand'], f"Scenario '{scenario_name}' brand is empty"

# Test case for checking if name is a string and not empty
def test_scenario_name_is_valid_string(morlevi_categories_data):
    """Checks if the 'name' value in each scenario is a non-empty string."""
    for scenario_name, scenario_data in morlevi_categories_data['scenarios'].items():
        assert isinstance(scenario_data['name'], str), f"Scenario '{scenario_name}' name is not a string"
        assert scenario_data['name'], f"Scenario '{scenario_name}' name is empty"


# Test case for checking if url is a string
def test_scenario_url_is_string(morlevi_categories_data):
    """Checks if the 'url' value in each scenario is a string."""
    for scenario_name, scenario_data in morlevi_categories_data['scenarios'].items():
        assert isinstance(scenario_data['url'], str), f"Scenario '{scenario_name}' url is not a string"

# Test case for checking if checkbox is a boolean
def test_scenario_checkbox_is_bool(morlevi_categories_data):
    """Checks if the 'checkbox' value in each scenario is a boolean."""
    for scenario_name, scenario_data in morlevi_categories_data['scenarios'].items():
        assert isinstance(scenario_data['checkbox'], bool), f"Scenario '{scenario_name}' checkbox is not a boolean"


# Test case for checking if active is a boolean
def test_scenario_active_is_bool(morlevi_categories_data):
     """Checks if the 'active' value in each scenario is a boolean."""
     for scenario_name, scenario_data in morlevi_categories_data['scenarios'].items():
        assert isinstance(scenario_data['active'], bool), f"Scenario '{scenario_name}' active is not a boolean"

# Test case for checking if condition is a string and not empty
def test_scenario_condition_is_valid_string(morlevi_categories_data):
     """Checks if the 'condition' value in each scenario is a non-empty string."""
     for scenario_name, scenario_data in morlevi_categories_data['scenarios'].items():
         assert isinstance(scenario_data['condition'], str), f"Scenario '{scenario_name}' condition is not a string"
         assert scenario_data['condition'], f"Scenario '{scenario_name}' condition is empty"


# Test case for checking if presta_categories is a string and not empty
def test_scenario_presta_categories_is_valid_string(morlevi_categories_data):
     """Checks if the 'presta_categories' value in each scenario is a non-empty string."""
     for scenario_name, scenario_data in morlevi_categories_data['scenarios'].items():
         assert isinstance(scenario_data['presta_categories'], str), f"Scenario '{scenario_name}' presta_categories is not a string"
         assert scenario_data['presta_categories'], f"Scenario '{scenario_name}' presta_categories is empty"


def test_url_format_valid(morlevi_categories_data):
    """check if the url is valid or not"""
    for scenario_name, scenario_data in morlevi_categories_data['scenarios'].items():
       if not scenario_data['url'].startswith("http"):
         assert True
       else:
          assert scenario_data['url'].startswith("https://www.morlevi.co.il/Cat/"), f"Scenario '{scenario_name}' url is not in the correct format"

```