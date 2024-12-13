```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def load_scenario_data():
    file_path = "hypotez/src/suppliers/ivory/scenarios/morlevi_categories_sound.json"
    with open(file_path, 'r') as file:
        return json.load(file)

# Test to check if the JSON file loads without errors
def test_load_json_file(load_scenario_data):
    """Checks if the JSON file can be loaded without errors."""
    assert isinstance(load_scenario_data, dict), "The loaded data should be a dictionary."
    assert "scenarios" in load_scenario_data, "The dictionary should contain 'scenarios' key."

# Test to check the structure of the loaded scenarios data
def test_scenario_structure(load_scenario_data):
    """Verifies that each scenario has the correct keys."""
    scenarios = load_scenario_data.get("scenarios", {})
    assert isinstance(scenarios, dict), "The scenarios should be a dictionary."
    for scenario_name, scenario_data in scenarios.items():
      assert isinstance(scenario_data, dict), f"Scenario data for '{scenario_name}' should be a dictionary."
      required_keys = ["brand", "url", "checkbox", "active", "condition", "presta_categories"]
      for key in required_keys:
        assert key in scenario_data, f"'{key}' key is missing in scenario '{scenario_name}'"
      assert isinstance(scenario_data["brand"], str), f"Brand in scenario '{scenario_name}' should be a string"
      assert isinstance(scenario_data["url"], str), f"URL in scenario '{scenario_name}' should be a string"
      assert isinstance(scenario_data["checkbox"], bool), f"Checkbox in scenario '{scenario_name}' should be a boolean"
      assert isinstance(scenario_data["active"], bool), f"Active in scenario '{scenario_name}' should be a boolean"
      assert isinstance(scenario_data["condition"], str), f"Condition in scenario '{scenario_name}' should be a string"
      assert isinstance(scenario_data["presta_categories"], str), f"Presta categories in scenario '{scenario_name}' should be a string"


# Test to verify that all URLs in the scenarios are valid
def test_scenario_urls(load_scenario_data):
    """Verifies that all the URLs in the scenarios are strings and not empty."""
    scenarios = load_scenario_data.get("scenarios", {})
    for scenario_name, scenario_data in scenarios.items():
        url = scenario_data.get("url")
        assert isinstance(url, str), f"URL in scenario '{scenario_name}' is not a string."
        assert url, f"URL in scenario '{scenario_name}' is empty."
        assert url.startswith("https://"), f"URL in scenario '{scenario_name}' does not start with https://."


# Test to verify that all brands in the scenarios are strings and not empty
def test_scenario_brands(load_scenario_data):
  """Verifies that all the brands in the scenarios are strings and not empty."""
  scenarios = load_scenario_data.get("scenarios", {})
  for scenario_name, scenario_data in scenarios.items():
    brand = scenario_data.get("brand")
    assert isinstance(brand, str), f"Brand in scenario '{scenario_name}' is not a string."
    assert brand, f"Brand in scenario '{scenario_name}' is empty."

# Test to verify that all conditions in the scenarios are strings and not empty
def test_scenario_conditions(load_scenario_data):
  """Verifies that all the conditions in the scenarios are strings and not empty."""
  scenarios = load_scenario_data.get("scenarios", {})
  for scenario_name, scenario_data in scenarios.items():
    condition = scenario_data.get("condition")
    assert isinstance(condition, str), f"Condition in scenario '{scenario_name}' is not a string."
    assert condition, f"Condition in scenario '{scenario_name}' is empty."


# Test to verify that all presta_categories in the scenarios are strings and not empty
def test_scenario_presta_categories(load_scenario_data):
  """Verifies that all the presta_categories in the scenarios are strings and not empty."""
  scenarios = load_scenario_data.get("scenarios", {})
  for scenario_name, scenario_data in scenarios.items():
    presta_categories = scenario_data.get("presta_categories")
    assert isinstance(presta_categories, str), f"Presta_categories in scenario '{scenario_name}' is not a string."
    assert presta_categories, f"Presta_categories in scenario '{scenario_name}' is empty."
```