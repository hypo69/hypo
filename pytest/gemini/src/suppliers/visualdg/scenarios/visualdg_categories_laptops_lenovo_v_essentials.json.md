```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def scenario_data():
    """Loads the JSON data from the file."""
    file_path = 'hypotez/src/suppliers/visualdg/scenarios/visualdg_categories_laptops_lenovo_v_essentials.json'
    with open(file_path, 'r') as file:
        return json.load(file)

def test_scenario_data_is_loaded(scenario_data):
    """Checks if the scenario data is loaded correctly."""
    assert isinstance(scenario_data, dict)
    assert "scenarios" in scenario_data
    assert isinstance(scenario_data["scenarios"], dict)
    assert len(scenario_data["scenarios"]) > 0

def test_scenario_structure(scenario_data):
    """Validates structure of each scenario entry."""
    for scenario_name, scenario_details in scenario_data["scenarios"].items():
      assert isinstance(scenario_name, str), f"Scenario name '{scenario_name}' is not a string"
      assert isinstance(scenario_details, dict), f"Details for '{scenario_name}' is not a dict"
      
      assert "brand" in scenario_details, f"'brand' key missing in '{scenario_name}'"
      assert isinstance(scenario_details["brand"], str), f"'brand' in '{scenario_name}' is not a string"

      assert "template" in scenario_details, f"'template' key missing in '{scenario_name}'"
      assert isinstance(scenario_details["template"], str), f"'template' in '{scenario_name}' is not a string"

      assert "url" in scenario_details, f"'url' key missing in '{scenario_name}'"
      assert isinstance(scenario_details["url"], str), f"'url' in '{scenario_name}' is not a string"
      
      assert "checkbox" in scenario_details, f"'checkbox' key missing in '{scenario_name}'"
      assert isinstance(scenario_details["checkbox"], bool), f"'checkbox' in '{scenario_name}' is not a boolean"

      assert "active" in scenario_details, f"'active' key missing in '{scenario_name}'"
      assert isinstance(scenario_details["active"], bool), f"'active' in '{scenario_name}' is not a boolean"
      
      assert "condition" in scenario_details, f"'condition' key missing in '{scenario_name}'"
      assert isinstance(scenario_details["condition"], str), f"'condition' in '{scenario_name}' is not a string"

      assert "presta_categories" in scenario_details, f"'presta_categories' key missing in '{scenario_name}'"
      assert isinstance(scenario_details["presta_categories"], str), f"'presta_categories' in '{scenario_name}' is not a string"

def test_scenario_brand_is_lenovo(scenario_data):
    """Checks if the 'brand' is always LENOVO"""
    for scenario_name, scenario_details in scenario_data["scenarios"].items():
        assert scenario_details["brand"] == "LENOVO", f"Brand is not 'LENOVO' in '{scenario_name}'"
    
def test_scenario_template_is_v_essentials(scenario_data):
    """Checks if the 'template' is always 'V ESSENTIALS'"""
    for scenario_name, scenario_details in scenario_data["scenarios"].items():
        assert scenario_details["template"] == "V ESSENTIALS", f"Template is not 'V ESSENTIALS' in '{scenario_name}'"

def test_scenario_checkbox_is_false(scenario_data):
    """Checks if 'checkbox' is always false"""
    for scenario_name, scenario_details in scenario_data["scenarios"].items():
        assert scenario_details["checkbox"] is False, f"'checkbox' is not False in '{scenario_name}'"

def test_scenario_active_is_true(scenario_data):
    """Checks if 'active' is always true"""
    for scenario_name, scenario_details in scenario_data["scenarios"].items():
         assert scenario_details["active"] is True, f"'active' is not True in '{scenario_name}'"

def test_scenario_condition_is_new(scenario_data):
    """Checks if 'condition' is always new"""
    for scenario_name, scenario_details in scenario_data["scenarios"].items():
        assert scenario_details["condition"] == "new", f"'condition' is not 'new' in '{scenario_name}'"

def test_scenario_url_not_empty(scenario_data):
  """Checks if URLs are strings and not empty."""
  for scenario_name, scenario_details in scenario_data["scenarios"].items():
      assert scenario_details["url"] != "", f"URL is empty in '{scenario_name}'"

def test_presta_categories_format(scenario_data):
    """
    Test that 'presta_categories' values are strings of comma-separated numbers.
    """
    for scenario_name, scenario_details in scenario_data["scenarios"].items():
        presta_categories = scenario_details["presta_categories"]
        assert isinstance(presta_categories, str), f"'presta_categories' in '{scenario_name}' is not a string"
        
        categories = presta_categories.split(',')
        for category in categories:
            assert category.isdigit(), f"'{category}' in 'presta_categories' of '{scenario_name}' is not a digit"
```