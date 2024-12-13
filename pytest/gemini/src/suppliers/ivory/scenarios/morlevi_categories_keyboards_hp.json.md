```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def keyboard_data():
    """Loads the keyboard data from the JSON file."""
    file_location = 'hypotez/src/suppliers/ivory/scenarios/morlevi_categories_keyboards_hp.json'
    with open(file_location, 'r') as f:
        data = json.load(f)
    return data

# Test cases for the JSON structure and content

def test_scenarios_exists(keyboard_data):
    """Tests if the 'scenarios' key exists in the JSON data."""
    assert "scenarios" in keyboard_data, "The 'scenarios' key is missing from the JSON data."

def test_scenarios_not_empty(keyboard_data):
    """Tests if the 'scenarios' dictionary is not empty."""
    assert keyboard_data["scenarios"], "The 'scenarios' dictionary is empty."

def test_scenario_keys_present(keyboard_data):
    """Tests if each scenario has the required keys."""
    required_keys = ["brand", "url", "checkbox", "active", "condition", "presta_categories"]
    for scenario_name, scenario_data in keyboard_data["scenarios"].items():
        for key in required_keys:
          assert key in scenario_data, f"The key '{key}' is missing in scenario '{scenario_name}'."

def test_scenario_brand_correct(keyboard_data):
    """Tests if the 'brand' value in each scenario is 'HP'."""
    for scenario_name, scenario_data in keyboard_data["scenarios"].items():
        assert scenario_data["brand"] == "HP", f"The brand is not 'HP' in scenario '{scenario_name}'."

def test_scenario_checkbox_is_boolean(keyboard_data):
    """Tests if the 'checkbox' value in each scenario is a boolean."""
    for scenario_name, scenario_data in keyboard_data["scenarios"].items():
        assert isinstance(scenario_data["checkbox"], bool), f"The 'checkbox' value is not a boolean in scenario '{scenario_name}'."
    
def test_scenario_active_is_boolean(keyboard_data):
    """Tests if the 'active' value in each scenario is a boolean."""
    for scenario_name, scenario_data in keyboard_data["scenarios"].items():
        assert isinstance(scenario_data["active"], bool), f"The 'active' value is not a boolean in scenario '{scenario_name}'."

def test_scenario_condition_is_new(keyboard_data):
  """Tests if the 'condition' value is 'new'."""
  for scenario_name, scenario_data in keyboard_data["scenarios"].items():
    assert scenario_data["condition"] == "new", f"The condition is not 'new' in scenario '{scenario_name}'."


def test_scenario_presta_categories_is_string(keyboard_data):
    """Tests if the 'presta_categories' value is a string."""
    for scenario_name, scenario_data in keyboard_data["scenarios"].items():
        assert isinstance(scenario_data["presta_categories"], str), f"The 'presta_categories' value is not a string in scenario '{scenario_name}'."

def test_scenario_presta_categories_not_empty(keyboard_data):
    """Tests if 'presta_categories' string is not empty."""
    for scenario_name, scenario_data in keyboard_data["scenarios"].items():
      assert scenario_data["presta_categories"] != "", f"The 'presta_categories' value is empty in scenario '{scenario_name}'."

def test_scenario_presta_categories_valid_format(keyboard_data):
    """Tests if 'presta_categories' string contains only comma separated numbers."""
    for scenario_name, scenario_data in keyboard_data["scenarios"].items():
      categories = scenario_data["presta_categories"].split(',')
      for cat in categories:
        assert cat.isdigit(), f"The 'presta_categories' value '{scenario_data['presta_categories']}' in scenario '{scenario_name}' contains non-digit value."
```