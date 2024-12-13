```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def morlevi_categories_data():
    """Provides the loaded JSON data for testing."""
    file_path = 'hypotez/src/suppliers/morlevi/scenarios/morlevi_categories_psu_gigabyte.json'
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

def test_morlevi_categories_data_structure(morlevi_categories_data):
    """Checks if the loaded data has the correct top-level structure (a dictionary with a 'scenarios' key)."""
    assert isinstance(morlevi_categories_data, dict), "Data should be a dictionary."
    assert 'scenarios' in morlevi_categories_data, "Data should contain a 'scenarios' key."

def test_morlevi_categories_scenarios_is_dict(morlevi_categories_data):
     """Checks if the 'scenarios' value is a dictionary."""
     assert isinstance(morlevi_categories_data['scenarios'], dict), "The 'scenarios' value should be a dictionary."

def test_morlevi_categories_scenarios_not_empty(morlevi_categories_data):
    """Checks if the 'scenarios' dictionary is not empty."""
    assert morlevi_categories_data['scenarios'], "The 'scenarios' dictionary should not be empty."

def test_morlevi_category_valid_keys(morlevi_categories_data):
    """Checks if each scenario in the 'scenarios' dictionary has the expected keys."""
    expected_keys = ["brand", "name", "url", "checkbox", "active", "condition", "presta_categories"]
    for scenario_name, scenario_data in morlevi_categories_data['scenarios'].items():
        assert all(key in scenario_data for key in expected_keys), f"Scenario '{scenario_name}' is missing one or more expected keys: {expected_keys}"

def test_morlevi_category_data_types(morlevi_categories_data):
    """Checks if the values of each scenario have the expected data types."""
    for scenario_name, scenario_data in morlevi_categories_data['scenarios'].items():
        assert isinstance(scenario_data['brand'], str), f"Brand should be a string for scenario '{scenario_name}'."
        assert isinstance(scenario_data['name'], str), f"Name should be a string for scenario '{scenario_name}'."
        assert isinstance(scenario_data['url'], str), f"URL should be a string for scenario '{scenario_name}'."
        assert isinstance(scenario_data['checkbox'], bool), f"Checkbox should be a boolean for scenario '{scenario_name}'."
        assert isinstance(scenario_data['active'], bool), f"Active should be a boolean for scenario '{scenario_name}'."
        assert isinstance(scenario_data['condition'], str), f"Condition should be a string for scenario '{scenario_name}'."
        assert isinstance(scenario_data['presta_categories'], str), f"presta_categories should be a string for scenario '{scenario_name}'."

def test_morlevi_category_active_values(morlevi_categories_data):
     """Checks if all 'active' values are True."""
     for scenario_name, scenario_data in morlevi_categories_data['scenarios'].items():
        assert scenario_data['active'] == True, f"Active value should be True for scenario '{scenario_name}'."

def test_morlevi_category_condition_values(morlevi_categories_data):
     """Checks if all 'condition' values are 'new'."""
     for scenario_name, scenario_data in morlevi_categories_data['scenarios'].items():
         assert scenario_data['condition'] == 'new', f"Condition should be 'new' for scenario '{scenario_name}'."


def test_morlevi_category_checkbox_values(morlevi_categories_data):
    """Checks if all 'checkbox' values are False."""
    for scenario_name, scenario_data in morlevi_categories_data['scenarios'].items():
         assert scenario_data['checkbox'] == False, f"Checkbox value should be False for scenario '{scenario_name}'."

def test_morlevi_category_url_not_empty(morlevi_categories_data):
    """Checks that the url field for every scenario is not empty"""
    for scenario_name, scenario_data in morlevi_categories_data['scenarios'].items():
        assert scenario_data['url'] , f"URL field should not be empty for '{scenario_name}'"


def test_morlevi_category_name_not_empty(morlevi_categories_data):
     """Checks that the name field for every scenario is not empty"""
     for scenario_name, scenario_data in morlevi_categories_data['scenarios'].items():
          assert scenario_data['name'] , f"Name field should not be empty for '{scenario_name}'"

def test_morlevi_category_brand_not_empty(morlevi_categories_data):
     """Checks that the brand field for every scenario is not empty"""
     for scenario_name, scenario_data in morlevi_categories_data['scenarios'].items():
         assert scenario_data['brand'] , f"brand field should not be empty for '{scenario_name}'"


def test_morlevi_category_presta_categories_not_empty(morlevi_categories_data):
     """Checks that the presta_categories field for every scenario is not empty"""
     for scenario_name, scenario_data in morlevi_categories_data['scenarios'].items():
          assert scenario_data['presta_categories'] , f"presta_categories field should not be empty for '{scenario_name}'"


def test_morlevi_category_presta_categories_is_string_of_numbers_and_commas(morlevi_categories_data):
    """Checks if the presta_categories field is a string containing only digits and commas."""
    for scenario_name, scenario_data in morlevi_categories_data['scenarios'].items():
        presta_categories = scenario_data['presta_categories']
        assert isinstance(presta_categories, str), f"presta_categories should be a string for '{scenario_name}'"
        assert all(char.isdigit() or char == ',' for char in presta_categories), f"presta_categories should contain only digits and commas for '{scenario_name}'"
```