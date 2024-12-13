```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def laptop_data():
    """Loads the laptop data from the JSON file."""
    file_path = 'hypotez/src/suppliers/visualdg/scenarios/visualdg_categories_laptops_asus.json'
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data


def test_laptop_data_structure(laptop_data):
    """
    Test that the loaded data has the expected structure.
    Checks for the existence of the 'scenarios' key and that it's a dictionary.
    """
    assert 'scenarios' in laptop_data
    assert isinstance(laptop_data['scenarios'], dict)


def test_laptop_scenario_keys(laptop_data):
    """
    Test that each scenario in the laptop data has the expected keys.
    Checks for required keys 'brand', 'url', 'checkbox', 'active', 'condition', and 'presta_categories'.
    """
    for scenario_name, scenario_data in laptop_data['scenarios'].items():
        assert 'brand' in scenario_data
        assert 'url' in scenario_data
        assert 'checkbox' in scenario_data
        assert 'active' in scenario_data
        assert 'condition' in scenario_data
        assert 'presta_categories' in scenario_data


def test_laptop_scenario_values_type(laptop_data):
    """
     Test that the values within each scenario have the correct type
    """
    for scenario_name, scenario_data in laptop_data['scenarios'].items():
         assert isinstance(scenario_data['brand'], str)
         assert isinstance(scenario_data['url'], str)
         assert isinstance(scenario_data['checkbox'], bool)
         assert isinstance(scenario_data['active'], bool)
         assert isinstance(scenario_data['condition'], str)
         assert isinstance(scenario_data['presta_categories'], str)


def test_laptop_brand_values(laptop_data):
    """
     Test that all brand values are ASUS
    """
    for scenario_name, scenario_data in laptop_data['scenarios'].items():
        assert scenario_data['brand'] == "ASUS"

def test_laptop_checkbox_values(laptop_data):
    """
    Test that all checkbox values are false
    """
    for scenario_name, scenario_data in laptop_data['scenarios'].items():
        assert scenario_data['checkbox'] == False

def test_laptop_active_values(laptop_data):
    """
    Test that all active values are true
    """
    for scenario_name, scenario_data in laptop_data['scenarios'].items():
        assert scenario_data['active'] == True


def test_laptop_condition_values(laptop_data):
    """
     Test that all condition values are new
    """
    for scenario_name, scenario_data in laptop_data['scenarios'].items():
        assert scenario_data['condition'] == "new"

def test_laptop_url_not_empty(laptop_data):
     """
    Test that the URL is not empty for any of the scenarios
    """
     for scenario_name, scenario_data in laptop_data['scenarios'].items():
          assert len(scenario_data['url']) > 0


def test_laptop_presta_categories_not_empty(laptop_data):
     """
    Test that the presta categories are not empty for any of the scenarios
    """
     for scenario_name, scenario_data in laptop_data['scenarios'].items():
          assert len(scenario_data['presta_categories']) > 0

def test_laptop_presta_categories_are_numbers(laptop_data):
    """
    Test that all presta categories are numbers separated by commas
    """
    for scenario_name, scenario_data in laptop_data['scenarios'].items():
        categories_str = scenario_data['presta_categories']
        categories_list = categories_str.split(',')
        for category in categories_list:
            assert category.isdigit(), f"Category '{category}' in scenario '{scenario_name}' is not a valid number."

def test_laptop_data_not_empty(laptop_data):
    """
    Test that the loaded JSON data is not empty.
    """
    assert laptop_data


def test_laptop_scenarios_not_empty(laptop_data):
    """
    Test that the scenarios within the JSON data are not empty.
    """
    assert laptop_data['scenarios']
```