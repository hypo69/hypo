```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def categories_data():
    """Loads the JSON data from the specified file."""
    file_path = "hypotez/src/suppliers/morlevi/scenarios/morlevi_categories_keyboards.json"
    with open(file_path, 'r') as f:
        return json.load(f)

# Test cases for the structure and content of the loaded JSON data
def test_categories_data_structure(categories_data):
    """Checks if the loaded data has the expected top-level structure."""
    assert "scenarios" in categories_data
    assert isinstance(categories_data["scenarios"], dict)

def test_categories_data_not_empty(categories_data):
     """Checks if the scenarios data is not empty."""
     assert categories_data["scenarios"]

def test_each_scenario_has_required_keys(categories_data):
     """Checks that each scenario in scenarios has the required keys"""
     for scenario_name, scenario_data in categories_data["scenarios"].items():
          assert "brand" in scenario_data
          assert "template" in scenario_data
          assert "url" in scenario_data
          assert "checkbox" in scenario_data
          assert "active" in scenario_data
          assert "condition" in scenario_data
          assert "presta_categories" in scenario_data


def test_scenario_values_types(categories_data):
     """Checks that the types of values of the keys are correct"""
     for scenario_name, scenario_data in categories_data["scenarios"].items():
          assert isinstance(scenario_data["brand"], str)
          assert isinstance(scenario_data["template"], str)
          assert isinstance(scenario_data["url"], str)
          assert isinstance(scenario_data["checkbox"], bool)
          assert isinstance(scenario_data["active"], bool)
          assert isinstance(scenario_data["condition"], str)
          assert isinstance(scenario_data["presta_categories"],(str, dict))

def test_valid_url_format_for_some_scenarios(categories_data):
     """Checks that url is in valid format for some scenarios """
     for scenario_name, scenario_data in categories_data["scenarios"].items():
        if "--------------------------------------" not in scenario_data["url"]:
            assert scenario_data["url"].startswith("https://www.morlevi.co.il/Cat/")
        

def test_presta_categories_template_type(categories_data):
    """Check if when presta_categories is dict, it contains "template" key"""
    for scenario_name, scenario_data in categories_data["scenarios"].items():
        if isinstance(scenario_data["presta_categories"], dict):
             assert "template" in scenario_data["presta_categories"]

def test_presta_categories_template_values(categories_data):
    """Check the value type inside the template dict"""
    for scenario_name, scenario_data in categories_data["scenarios"].items():
        if isinstance(scenario_data["presta_categories"], dict) and "template" in scenario_data["presta_categories"]:
            for _,value in scenario_data["presta_categories"]["template"].items():
                 assert isinstance(value,str)


def test_condition_value_is_new(categories_data):
     """Checks if all the conditions values are set to new"""
     for scenario_name, scenario_data in categories_data["scenarios"].items():
          assert scenario_data["condition"] == "new"
```