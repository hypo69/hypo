```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def morlevi_categories_data():
    """Loads the morlevi categories data from the JSON file."""
    file_location = 'hypotez/src/suppliers/morlevi/scenarios/morlevi_categories_monitors_coolermaster.json'
    with open(file_location, 'r') as f:
        return json.load(f)

# Test cases for the 'scenarios' data structure
def test_morlevi_categories_data_structure(morlevi_categories_data):
    """
    Checks that the loaded data has the expected structure
    with a 'scenarios' key which is a dictionary.
    """
    assert "scenarios" in morlevi_categories_data
    assert isinstance(morlevi_categories_data["scenarios"], dict)

# Test cases for individual scenario data
def test_morlevi_scenario_data_valid_keys(morlevi_categories_data):
    """
    Tests if each scenario within the 'scenarios' dictionary
    contains all the expected keys: 'brand', 'url', 'checkbox', 'active', 'condition', 'presta_categories'.
    """
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
         assert "brand" in scenario_data, f"Scenario {scenario_name} missing 'brand' key"
         assert "url" in scenario_data, f"Scenario {scenario_name} missing 'url' key"
         assert "checkbox" in scenario_data, f"Scenario {scenario_name} missing 'checkbox' key"
         assert "active" in scenario_data, f"Scenario {scenario_name} missing 'active' key"
         assert "condition" in scenario_data, f"Scenario {scenario_name} missing 'condition' key"
         assert "presta_categories" in scenario_data, f"Scenario {scenario_name} missing 'presta_categories' key"


def test_morlevi_scenario_data_valid_values(morlevi_categories_data):
    """
    Tests if the values of 'checkbox', 'active', 'condition', 'brand', and 'presta_categories'
    are of the expected types for each scenario.
    """
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
      assert isinstance(scenario_data["checkbox"], bool), f"Scenario {scenario_name} 'checkbox' should be boolean"
      assert isinstance(scenario_data["active"], bool), f"Scenario {scenario_name} 'active' should be boolean"
      assert isinstance(scenario_data["condition"], str), f"Scenario {scenario_name} 'condition' should be string"
      assert isinstance(scenario_data["brand"], str), f"Scenario {scenario_name} 'brand' should be string"
      assert isinstance(scenario_data["presta_categories"], str), f"Scenario {scenario_name} 'presta_categories' should be string"


def test_morlevi_scenario_data_url_is_string(morlevi_categories_data):
    """
    Tests if the url value in each scenario is a string
    """
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
      assert isinstance(scenario_data["url"],str), f"Scenario {scenario_name} 'url' should be a string"

def test_morlevi_scenario_data_url_not_empty(morlevi_categories_data):
  """
  Tests if the url value in each scenario is not empty
  """
  for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
    assert scenario_data["url"] != "", f"Scenario {scenario_name} 'url' should not be empty"

def test_morlevi_scenario_data_presta_categories_not_empty(morlevi_categories_data):
  """
    Tests if the 'presta_categories' value in each scenario is not empty
  """
  for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
    assert scenario_data["presta_categories"] != "", f"Scenario {scenario_name} 'presta_categories' should not be empty"

def test_morlevi_scenario_data_presta_categories_valid_format(morlevi_categories_data):
    """
    Tests if the 'presta_categories' value in each scenario is a string containing comma-separated numbers.
    """
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
      presta_categories = scenario_data["presta_categories"]
      categories = presta_categories.split(',')
      for cat in categories:
          assert cat.isdigit(), f"Scenario {scenario_name} 'presta_categories' should only contain comma-separated digits: {presta_categories}"

def test_morlevi_scenario_data_condition_new(morlevi_categories_data):
    """
    Tests if 'condition' field is always "new"
    """
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert scenario_data["condition"] == "new", f"Scenario {scenario_name} 'condition' should be 'new'"
```