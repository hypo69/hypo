```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def morlevi_data():
    """Loads the morlevi_categories_monitors_gigabyte.json data."""
    
    file_path = 'hypotez/src/suppliers/morlevi/scenarios/morlevi_categories_monitors_gigabyte.json'
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

# Test case for valid 'brand' values
def test_brand_values(morlevi_data):
    """
    Checks if all 'brand' values in the scenarios are 'GIGABYTE'.
    """
    for scenario_name, scenario_data in morlevi_data["scenarios"].items():
      assert scenario_data["brand"] == "GIGABYTE", f"Scenario '{scenario_name}' has incorrect brand: {scenario_data['brand']}"

# Test case for valid 'url' values
def test_url_values(morlevi_data):
    """
    Checks if 'url' values are strings, and not empty strings (except specific cases).
    """
    for scenario_name, scenario_data in morlevi_data["scenarios"].items():
      if not (scenario_data["url"].startswith("---")):
         assert isinstance(scenario_data["url"], str), f"Scenario '{scenario_name}' url is not a string: {scenario_data['url']}"
         assert scenario_data["url"], f"Scenario '{scenario_name}' url is empty"


# Test case for 'checkbox' values
def test_checkbox_values(morlevi_data):
    """
    Checks if 'checkbox' values are boolean and false.
    """
    for scenario_name, scenario_data in morlevi_data["scenarios"].items():
        assert isinstance(scenario_data["checkbox"], bool), f"Scenario '{scenario_name}' has invalid checkbox type: {type(scenario_data['checkbox'])}"
        assert scenario_data["checkbox"] is False, f"Scenario '{scenario_name}' has invalid checkbox value: {scenario_data['checkbox']}"

# Test case for 'active' values
def test_active_values(morlevi_data):
    """
    Checks if 'active' values are boolean and true.
    """
    for scenario_name, scenario_data in morlevi_data["scenarios"].items():
      assert isinstance(scenario_data["active"], bool), f"Scenario '{scenario_name}' has invalid active type: {type(scenario_data['active'])}"
      assert scenario_data["active"] is True, f"Scenario '{scenario_name}' has invalid active value: {scenario_data['active']}"

# Test case for 'condition' values
def test_condition_values(morlevi_data):
    """
    Checks if all 'condition' values in the scenarios are 'new'.
    """
    for scenario_name, scenario_data in morlevi_data["scenarios"].items():
      assert scenario_data["condition"] == "new", f"Scenario '{scenario_name}' has incorrect condition: {scenario_data['condition']}"


# Test case for valid 'presta_categories' values
def test_presta_categories_values(morlevi_data):
    """
    Checks if 'presta_categories' values are strings and contain at least one comma
    """
    for scenario_name, scenario_data in morlevi_data["scenarios"].items():
      assert isinstance(scenario_data["presta_categories"], str), f"Scenario '{scenario_name}' presta_categories is not a string: {scenario_data['presta_categories']}"
      assert "," in scenario_data["presta_categories"], f"Scenario '{scenario_name}' presta_categories does not contain a comma: {scenario_data['presta_categories']}"
      

# Test case to ensure each scenario has all expected keys
def test_scenario_keys(morlevi_data):
   """
   Checks that each scenario has all expected keys
   """
   expected_keys = ["brand", "url", "checkbox", "active", "condition", "presta_categories"]
   for scenario_name, scenario_data in morlevi_data["scenarios"].items():
      assert all(key in scenario_data for key in expected_keys), f"Scenario '{scenario_name}' is missing one or more expected keys"
```