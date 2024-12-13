```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def morlevi_categories_data():
    """Provides the JSON data for testing."""
    file_path = 'hypotez/src/suppliers/morlevi/scenarios/morlevi_categories_minipc_intel.json'
    with open(file_path, 'r') as f:
        return json.load(f)

# Test cases for the structure and data of the loaded JSON

def test_json_structure(morlevi_categories_data):
    """
    Test that the loaded JSON data has the correct top-level structure,
    expecting a dictionary with a "scenarios" key
    """
    assert isinstance(morlevi_categories_data, dict), "The root should be a dictionary."
    assert "scenarios" in morlevi_categories_data, "The root dictionary should have a 'scenarios' key."
    assert isinstance(morlevi_categories_data["scenarios"], dict), "The 'scenarios' value should be a dictionary."

def test_scenarios_keys(morlevi_categories_data):
  """
  Test that the "scenarios" dictionary has the expected keys.
  """
  expected_keys = {
      "INTEL MINIPC I3 8-9th GEN",
      "INTEL MINIPC I3 10th GEN",
      "INTEL MINIPC I5 8-9th",
      "INTEL MINIPC I5 10th",
      "INTEL  MINIPC I7",
      "INTEL  MINIPC I9",
      "INTEL MINIPC AMD",
      "INTEL MINIPC Celeron"
  }
  actual_keys = set(morlevi_categories_data["scenarios"].keys())
  assert actual_keys == expected_keys, "The scenarios dictionary should have the expected keys"


def test_scenario_data_types(morlevi_categories_data):
    """
    Test that each scenario has the correct data types for each value.
    """
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert isinstance(scenario_data, dict), f"Scenario '{scenario_name}' should be a dictionary."
        assert isinstance(scenario_data.get("brand"), str), f"Scenario '{scenario_name}' brand should be a string."
        assert isinstance(scenario_data.get("url"), str), f"Scenario '{scenario_name}' url should be a string."
        assert isinstance(scenario_data.get("checkbox"), bool), f"Scenario '{scenario_name}' checkbox should be a boolean."
        assert isinstance(scenario_data.get("active"), bool), f"Scenario '{scenario_name}' active should be a boolean."
        assert isinstance(scenario_data.get("condition"),str), f"Scenario '{scenario_name}' condition should be a string"
        assert isinstance(scenario_data.get("presta_categories"), str), f"Scenario '{scenario_name}' presta_categories should be a string"

def test_scenario_valid_urls(morlevi_categories_data):
    """
        Test that most of the  scenario URLs are valid URLs or placeholders ,
        exclude the ones that we know are placeholders
    """
    excluded_scenarios = ["INTEL  MINIPC I9", "INTEL MINIPC AMD", "INTEL MINIPC Celeron"]

    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
      if scenario_name not in excluded_scenarios:
        url = scenario_data.get("url")
        assert url.startswith("https://www.morlevi.co.il/Cat/"), f"Scenario '{scenario_name}' URL should start with 'https://www.morlevi.co.il/Cat/'"


def test_scenario_brand_values(morlevi_categories_data):
    """
    Test that all brands are  "INTEL"
    """
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        brand = scenario_data.get("brand")
        assert brand == "INTEL", f"Scenario '{scenario_name}' brand should be 'INTEL'."

def test_scenario_checkbox_values(morlevi_categories_data):
    """
    Test that all checkbox values are false
    """
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        checkbox = scenario_data.get("checkbox")
        assert checkbox == False, f"Scenario '{scenario_name}' checkbox should be False."

def test_scenario_active_values(morlevi_categories_data):
    """
        Test that all active values are True
    """
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
      active = scenario_data.get("active")
      assert active == True, f"Scenario '{scenario_name}' active should be True"
def test_scenario_condition_values(morlevi_categories_data):
    """
       Test that all condition values are "new"
   """
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
      condition = scenario_data.get("condition")
      assert condition == "new", f"Scenario '{scenario_name}' condition should be new"

def test_scenario_presta_categories_not_empty(morlevi_categories_data):
    """
        Test that all 'presta_categories' values are not empty strings
    """
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
      presta_categories = scenario_data.get("presta_categories")
      assert presta_categories != "", f"Scenario '{scenario_name}' presta_categories should not be empty"
```