```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def morlevi_aoc_data():
    """Loads the morlevi_categories_monitors_aoc.json data."""
    file_location = 'hypotez/src/suppliers/ivory/scenarios/morlevi_categories_monitors_aoc.json'
    with open(file_location, 'r') as f:
        data = json.load(f)
    return data

# Test to check if the JSON file is loaded correctly
def test_morlevi_aoc_data_loaded(morlevi_aoc_data):
    """Checks if the JSON data is loaded correctly."""
    assert morlevi_aoc_data is not None
    assert isinstance(morlevi_aoc_data, dict)
    assert "scenarios" in morlevi_aoc_data

# Test to check the existence of scenarios
def test_morlevi_aoc_scenarios_exist(morlevi_aoc_data):
    """Checks if the scenarios key exists and is not empty."""
    assert "scenarios" in morlevi_aoc_data
    assert isinstance(morlevi_aoc_data["scenarios"], dict)
    assert len(morlevi_aoc_data["scenarios"]) > 0

# Test to check that each scenario has the correct structure and values
def test_morlevi_aoc_scenario_structure(morlevi_aoc_data):
    """Checks each scenario has the correct structure and types."""
    scenarios = morlevi_aoc_data["scenarios"]
    for scenario_name, scenario_data in scenarios.items():
      assert isinstance(scenario_name, str), f"Scenario name '{scenario_name}' is not a string"
      assert isinstance(scenario_data, dict), f"Scenario data for '{scenario_name}' is not a dictionary"
      assert "brand" in scenario_data, f"Scenario '{scenario_name}' missing 'brand' key"
      assert isinstance(scenario_data["brand"], str), f"Brand in scenario '{scenario_name}' is not a string"
      assert "url" in scenario_data, f"Scenario '{scenario_name}' missing 'url' key"
      assert isinstance(scenario_data["url"], str), f"URL in scenario '{scenario_name}' is not a string"
      assert "checkbox" in scenario_data, f"Scenario '{scenario_name}' missing 'checkbox' key"
      assert isinstance(scenario_data["checkbox"], bool), f"Checkbox in scenario '{scenario_name}' is not a boolean"
      assert "active" in scenario_data, f"Scenario '{scenario_name}' missing 'active' key"
      assert isinstance(scenario_data["active"], bool), f"Active in scenario '{scenario_name}' is not a boolean"
      assert "condition" in scenario_data, f"Scenario '{scenario_name}' missing 'condition' key"
      assert isinstance(scenario_data["condition"], str), f"Condition in scenario '{scenario_name}' is not a string"
      assert "presta_categories" in scenario_data, f"Scenario '{scenario_name}' missing 'presta_categories' key"
      assert isinstance(scenario_data["presta_categories"], str), f"presta_categories in scenario '{scenario_name}' is not a string"

# Test to check for a specific scenario's brand
def test_morlevi_aoc_specific_scenario_brand(morlevi_aoc_data):
  """Checks if the brand for a specific scenario is correct"""
  assert morlevi_aoc_data["scenarios"]["AOC 22"]["brand"] == "AOC"
  assert morlevi_aoc_data["scenarios"]["AOC 34"]["brand"] == "AOC"


# Test to check the content of URL values
def test_morlevi_aoc_url_content(morlevi_aoc_data):
    """Checks URL values for specific scenarios."""
    assert "AOC 22" in morlevi_aoc_data["scenarios"]
    assert "AOC 34" in morlevi_aoc_data["scenarios"]
    assert "AOC 49" in morlevi_aoc_data["scenarios"]
    assert "---------------------------------------AOC 22-------------------------------" == morlevi_aoc_data["scenarios"]["AOC 22"]["url"]
    assert "--------------------------  AOC 34 -----------------------------------" == morlevi_aoc_data["scenarios"]["AOC 34"]["url"].strip()
    assert "-----------------------------  AOC 49 ---------------------------------" == morlevi_aoc_data["scenarios"]["AOC 49"]["url"].strip()
    assert "https://www.morlevi.co.il/Cat/8?p_315=25&p_350=1806&sort=datafloat2%2Cprice&keyword=" == morlevi_aoc_data["scenarios"]["AOC 23"]["url"]

# Test for boolean values
def test_morlevi_aoc_boolean_values(morlevi_aoc_data):
    """Checks boolean values for specific scenarios."""
    for scenario_name, scenario_data in morlevi_aoc_data["scenarios"].items():
        assert isinstance(scenario_data["checkbox"], bool)
        assert scenario_data["checkbox"] == False
        assert isinstance(scenario_data["active"], bool)
        assert scenario_data["active"] == True

# Test to check the condition values
def test_morlevi_aoc_condition_values(morlevi_aoc_data):
    """Checks condition values for all scenarios."""
    for scenario_name, scenario_data in morlevi_aoc_data["scenarios"].items():
        assert scenario_data["condition"] == "new"

# Test to check the presta_categories values
def test_morlevi_aoc_presta_categories_values(morlevi_aoc_data):
    """Checks presta_categories values for all scenarios."""
    assert morlevi_aoc_data["scenarios"]["AOC 22"]["presta_categories"] == "127,128,529"
    assert morlevi_aoc_data["scenarios"]["AOC 23"]["presta_categories"] == "127,128,529"
    assert morlevi_aoc_data["scenarios"]["AOC 24-25"]["presta_categories"] == "127,129,529"
    assert morlevi_aoc_data["scenarios"]["AOC 27-29"]["presta_categories"] == "127,130,529"
    assert morlevi_aoc_data["scenarios"]["AOC 32"]["presta_categories"] == "127,131,529"
    assert morlevi_aoc_data["scenarios"]["AOC 34"]["presta_categories"] == "127,132,529"
    assert morlevi_aoc_data["scenarios"]["AOC 49"]["presta_categories"] == "127,133,529"
```