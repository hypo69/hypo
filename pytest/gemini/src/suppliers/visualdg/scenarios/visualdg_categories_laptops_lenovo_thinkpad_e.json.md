```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def scenario_data():
    """Provides the scenario data from the JSON file."""
    # Use a relative path to the file within the tests directory
    file_path = 'hypotez/src/suppliers/visualdg/scenarios/visualdg_categories_laptops_lenovo_thinkpad_e.json'
    with open(file_path, 'r') as f:
        return json.load(f)

def test_scenario_data_is_loaded(scenario_data):
    """Checks that the scenario data is loaded correctly."""
    assert isinstance(scenario_data, dict), "The loaded data should be a dictionary."
    assert "scenarios" in scenario_data, "The 'scenarios' key should exist in the loaded data."
    assert isinstance(scenario_data["scenarios"], dict), "The 'scenarios' value should be a dictionary."
    assert len(scenario_data["scenarios"]) > 0, "There should be at least one scenario in the data."


def test_scenario_has_required_keys(scenario_data):
    """Checks if each scenario has all the required keys."""
    for scenario_name, scenario_details in scenario_data["scenarios"].items():
         assert "brand" in scenario_details, f"Scenario '{scenario_name}' is missing 'brand' key."
         assert "template" in scenario_details, f"Scenario '{scenario_name}' is missing 'template' key."
         assert "url" in scenario_details, f"Scenario '{scenario_name}' is missing 'url' key."
         assert "checkbox" in scenario_details, f"Scenario '{scenario_name}' is missing 'checkbox' key."
         assert "active" in scenario_details, f"Scenario '{scenario_name}' is missing 'active' key."
         assert "condition" in scenario_details, f"Scenario '{scenario_name}' is missing 'condition' key."
         assert "presta_categories" in scenario_details, f"Scenario '{scenario_name}' is missing 'presta_categories' key."

def test_scenario_values_are_correct_type(scenario_data):
    """Checks if the values of the scenario keys are of the correct type."""
    for scenario_name, scenario_details in scenario_data["scenarios"].items():
        assert isinstance(scenario_details["brand"], str), f"Scenario '{scenario_name}': 'brand' should be a string."
        assert isinstance(scenario_details["template"], str), f"Scenario '{scenario_name}': 'template' should be a string."
        assert isinstance(scenario_details["url"], str), f"Scenario '{scenario_name}': 'url' should be a string."
        assert isinstance(scenario_details["checkbox"], bool), f"Scenario '{scenario_name}': 'checkbox' should be a boolean."
        assert isinstance(scenario_details["active"], bool), f"Scenario '{scenario_name}': 'active' should be a boolean."
        assert isinstance(scenario_details["condition"], str), f"Scenario '{scenario_name}': 'condition' should be a string."
        assert isinstance(scenario_details["presta_categories"], str), f"Scenario '{scenario_name}': 'presta_categories' should be a string."


def test_scenario_brand_value(scenario_data):
    """Checks that the brand value is 'LENOVO' for each scenario."""
    for scenario_name, scenario_details in scenario_data["scenarios"].items():
        assert scenario_details["brand"] == "LENOVO", f"Scenario '{scenario_name}': brand should be 'LENOVO'."

def test_scenario_template_value(scenario_data):
    """Checks that the template value is 'THINKPAD E' for each scenario."""
    for scenario_name, scenario_details in scenario_data["scenarios"].items():
        assert scenario_details["template"] == "THINKPAD E", f"Scenario '{scenario_name}': template should be 'THINKPAD E'."

def test_scenario_url_not_empty(scenario_data):
     """Checks that the url value is not empty for each scenario."""
     for scenario_name, scenario_details in scenario_data["scenarios"].items():
        assert len(scenario_details["url"]) > 0, f"Scenario '{scenario_name}': url should not be empty."

def test_scenario_checkbox_is_false(scenario_data):
    """Checks that the checkbox value is false for each scenario."""
    for scenario_name, scenario_details in scenario_data["scenarios"].items():
        assert scenario_details["checkbox"] == False, f"Scenario '{scenario_name}': checkbox should be False."

def test_scenario_active_is_true(scenario_data):
    """Checks that the active value is true for each scenario."""
    for scenario_name, scenario_details in scenario_data["scenarios"].items():
        assert scenario_details["active"] == True, f"Scenario '{scenario_name}': active should be True."

def test_scenario_condition_is_new(scenario_data):
    """Checks that the condition value is 'new' for each scenario."""
    for scenario_name, scenario_details in scenario_data["scenarios"].items():
        assert scenario_details["condition"] == "new", f"Scenario '{scenario_name}': condition should be 'new'."

def test_scenario_presta_categories_not_empty(scenario_data):
     """Checks that the presta_categories value is not empty for each scenario."""
     for scenario_name, scenario_details in scenario_data["scenarios"].items():
        assert len(scenario_details["presta_categories"]) > 0, f"Scenario '{scenario_name}': presta_categories should not be empty."

def test_scenario_presta_categories_is_comma_separated_numbers(scenario_data):
    """Checks that presta_categories is a string of comma separated numbers."""
    for scenario_name, scenario_details in scenario_data["scenarios"].items():
      categories = scenario_details["presta_categories"].split(',')
      for category in categories:
        assert category.isdigit(), f"Scenario '{scenario_name}': presta_categories should be comma separated numbers only. Invalid category: {category} "
```