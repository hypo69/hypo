```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def morlevi_categories_data():
    """Loads the morlevi categories JSON data from the file."""
    file_path = 'hypotez/src/suppliers/ivory/scenarios/morlevi_categories_cases_generic.json'
    try:
      with open(file_path, 'r') as f:
          return json.load(f)
    except FileNotFoundError:
        pytest.fail(f"Test file not found at: {file_path}")
    except json.JSONDecodeError:
        pytest.fail(f"Error decoding json file: {file_path}")

# Tests for the 'scenarios' structure

def test_scenarios_exists(morlevi_categories_data):
    """Checks if the 'scenarios' key exists in the loaded data."""
    assert "scenarios" in morlevi_categories_data, "The 'scenarios' key is missing in the JSON data."

def test_scenarios_not_empty(morlevi_categories_data):
  """Checks if the 'scenarios' is not empty."""
  assert morlevi_categories_data["scenarios"], "The 'scenarios' is empty"

def test_scenario_keys_exist(morlevi_categories_data):
    """Checks if each scenario has the required keys."""
    required_keys = ["brand", "template", "url", "checkbox", "active", "condition", "presta_categories"]
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        for key in required_keys:
            assert key in scenario_data, f"Scenario '{scenario_name}' is missing the key: {key}"

def test_scenario_brand_is_generic(morlevi_categories_data):
    """Checks if the 'brand' is 'GENERIC' for all scenarios."""
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert scenario_data["brand"] == "GENERIC", f"Scenario '{scenario_name}' does not have 'GENERIC' brand."

def test_scenario_template_is_empty_string(morlevi_categories_data):
    """Checks if the 'template' is an empty string for all scenarios."""
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
       assert scenario_data["template"] == "", f"Scenario '{scenario_name}' does not have an empty template string."

def test_scenario_checkbox_is_false(morlevi_categories_data):
   """Checks if the 'checkbox' is false for all scenarios."""
   for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
       assert scenario_data["checkbox"] is False, f"Scenario '{scenario_name}' does not have 'checkbox' as False."

def test_scenario_active_is_true(morlevi_categories_data):
    """Checks if the 'active' is true for all scenarios."""
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert scenario_data["active"] is True, f"Scenario '{scenario_name}' does not have 'active' as True."

def test_scenario_condition_is_new(morlevi_categories_data):
    """Checks if the 'condition' is 'new' for all scenarios."""
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert scenario_data["condition"] == "new", f"Scenario '{scenario_name}' does not have condition set as 'new'."

def test_scenario_presta_categories_exists(morlevi_categories_data):
    """Checks if the 'presta_categories' key exists for all scenarios and is not empty."""
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert "presta_categories" in scenario_data, f"Scenario '{scenario_name}' does not have 'presta_categories' key."
        assert scenario_data["presta_categories"] , f"Scenario '{scenario_name}' has an empty 'presta_categories' value."

def test_scenario_presta_categories_template_exists(morlevi_categories_data):
    """Checks if 'template' key exists in 'presta_categories' for all scenarios."""
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert "template" in scenario_data["presta_categories"], f"Scenario '{scenario_name}' is missing 'template' in 'presta_categories'."
        assert scenario_data["presta_categories"]["template"], f"Scenario '{scenario_name}' has an empty template in presta_categories"


def test_scenario_presta_categories_template_computer_cases(morlevi_categories_data):
    """Checks if 'computer cases' key exists in 'template' of 'presta_categories' and is not empty for all scenarios."""
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert "computer cases" in scenario_data["presta_categories"]["template"], f"Scenario '{scenario_name}' is missing 'computer cases' in template of 'presta_categories'."
        assert scenario_data["presta_categories"]["template"]["computer cases"], f"Scenario '{scenario_name}' has an empty computer cases in presta_categories"


def test_scenario_url_not_empty(morlevi_categories_data):
    """Checks if the url is not an empty string."""
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
         assert scenario_data["url"] != "", f"Scenario '{scenario_name}' has an empty url."
```