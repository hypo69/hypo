```python
import pytest
import json

# Fixture for loading the JSON data
@pytest.fixture
def ksp_data():
    """Loads the ksp_categories_watches_honor.json data."""
    file_path = "hypotez/src/suppliers/ksp/scenarios/ksp_categories_watches_honor.json"
    with open(file_path, 'r') as f:
        return json.load(f)

# Test for the presence of "scenarios" key
def test_scenarios_key_exists(ksp_data):
    """Checks that the 'scenarios' key exists in the loaded data."""
    assert "scenarios" in ksp_data, "The 'scenarios' key is missing."

# Test for presence of specific scenario keys
def test_scenario_keys_exist(ksp_data):
    """Checks that specific scenario keys are present in the 'scenarios' dictionary."""
    scenarios = ksp_data.get("scenarios")
    assert scenarios, "No scenarios found."
    assert "Honor Magic Watch 2" in scenarios, "The 'Honor Magic Watch 2' key is missing."
    assert "Honor Band 6" in scenarios, "The 'Honor Band 6' key is missing."

# Test for correct scenario structure
def test_scenario_structure(ksp_data):
    """Checks if each scenario has the correct structure (brand, url, checkbox, active, condition, presta_categories)."""
    scenarios = ksp_data.get("scenarios")
    assert scenarios, "No scenarios found."
    for scenario_name, scenario_data in scenarios.items():
      assert "brand" in scenario_data, f"'brand' key missing in scenario: {scenario_name}."
      assert "url" in scenario_data, f"'url' key missing in scenario: {scenario_name}."
      assert "checkbox" in scenario_data, f"'checkbox' key missing in scenario: {scenario_name}."
      assert "active" in scenario_data, f"'active' key missing in scenario: {scenario_name}."
      assert "condition" in scenario_data, f"'condition' key missing in scenario: {scenario_name}."
      assert "presta_categories" in scenario_data, f"'presta_categories' key missing in scenario: {scenario_name}."
    

# Test for valid URL format (basic check)
def test_valid_url_format(ksp_data):
    """Checks if 'url' values are strings starting with 'https://'."""
    scenarios = ksp_data.get("scenarios")
    assert scenarios, "No scenarios found."
    for scenario_name, scenario_data in scenarios.items():
      url = scenario_data.get("url")
      assert isinstance(url, str), f"URL is not a string in scenario: {scenario_name}"
      assert url.startswith("https://"), f"URL does not start with 'https://' in scenario: {scenario_name}"


# Test for boolean value of 'checkbox' and 'active' keys
def test_checkbox_and_active_are_booleans(ksp_data):
  """Checks if 'checkbox' and 'active' values are booleans."""
  scenarios = ksp_data.get("scenarios")
  assert scenarios, "No scenarios found."
  for scenario_name, scenario_data in scenarios.items():
      assert isinstance(scenario_data.get("checkbox"), bool), f"checkbox is not a boolean in scenario: {scenario_name}"
      assert isinstance(scenario_data.get("active"), bool), f"active is not a boolean in scenario: {scenario_name}"
      
# Test if "condition" is a string
def test_condition_is_string(ksp_data):
    """Checks if the 'condition' values are strings."""
    scenarios = ksp_data.get("scenarios")
    assert scenarios, "No scenarios found."
    for scenario_name, scenario_data in scenarios.items():
        condition = scenario_data.get("condition")
        assert isinstance(condition, str), f"Condition is not a string in scenario: {scenario_name}"


# Test for non-empty 'presta_categories' dictionary
def test_presta_categories_is_not_empty(ksp_data):
    """Checks that the 'presta_categories' dictionary is not empty for all scenarios."""
    scenarios = ksp_data.get("scenarios")
    assert scenarios, "No scenarios found."
    for scenario_name, scenario_data in scenarios.items():
        presta_categories = scenario_data.get("presta_categories")
        assert presta_categories, f"'presta_categories' dictionary is empty in scenario: {scenario_name}"
        assert isinstance(presta_categories, dict), f"'presta_categories' is not a dictionary in scenario: {scenario_name}"

# Test 'presta_categories' keys and values are strings
def test_presta_categories_keys_and_values_are_strings(ksp_data):
    """Checks that the keys and values in 'presta_categories' are strings."""
    scenarios = ksp_data.get("scenarios")
    assert scenarios, "No scenarios found."
    for scenario_name, scenario_data in scenarios.items():
      presta_categories = scenario_data.get("presta_categories")
      for key, value in presta_categories.items():
        assert isinstance(key, str), f"Key in presta_categories is not a string in scenario: {scenario_name}"
        assert isinstance(value, str), f"Value in presta_categories is not a string in scenario: {scenario_name}"
```