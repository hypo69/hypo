```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def cdata_categories_desktops_data():
    """Loads the cdata_categories_desktops.json data."""
    file_path = 'hypotez/src/suppliers/cdata/scenarios/cdata_categories_desktops.json'
    with open(file_path, 'r') as f:
        return json.load(f)


def test_cdata_categories_desktops_data_structure(cdata_categories_desktops_data):
    """
    Test that the loaded data is a dictionary and contains the 'scenarios' key.
    """
    assert isinstance(cdata_categories_desktops_data, dict), "The loaded data should be a dictionary."
    assert "scenarios" in cdata_categories_desktops_data, "The dictionary should contain the 'scenarios' key."


def test_cdata_categories_desktops_scenarios_type(cdata_categories_desktops_data):
    """
    Test that the 'scenarios' value is a dictionary.
    """
    assert isinstance(cdata_categories_desktops_data["scenarios"], dict), "The 'scenarios' value should be a dictionary."

def test_cdata_categories_desktops_scenarios_not_empty(cdata_categories_desktops_data):
    """
    Test that the 'scenarios' dictionary is not empty.
    """
    assert cdata_categories_desktops_data["scenarios"], "The 'scenarios' dictionary should not be empty."

def test_cdata_categories_desktops_scenario_keys(cdata_categories_desktops_data):
    """
    Test that each scenario has the expected keys: 'brand', 'url', 'checkbox', 'active', 'condition', 'presta_categories'.
    """
    for scenario_name, scenario_data in cdata_categories_desktops_data["scenarios"].items():
      assert isinstance(scenario_data, dict), f"Scenario {scenario_name} should be a dictionary."
      assert "brand" in scenario_data, f"Scenario {scenario_name} should have the 'brand' key."
      assert "url" in scenario_data, f"Scenario {scenario_name} should have the 'url' key."
      assert "checkbox" in scenario_data, f"Scenario {scenario_name} should have the 'checkbox' key."
      assert "active" in scenario_data, f"Scenario {scenario_name} should have the 'active' key."
      assert "condition" in scenario_data, f"Scenario {scenario_name} should have the 'condition' key."
      assert "presta_categories" in scenario_data, f"Scenario {scenario_name} should have the 'presta_categories' key."


def test_cdata_categories_desktops_scenario_values_types(cdata_categories_desktops_data):
    """
    Test the data types of each value in scenarios.
    """
    for scenario_name, scenario_data in cdata_categories_desktops_data["scenarios"].items():
      assert isinstance(scenario_data["brand"], str), f"Brand in {scenario_name} should be a string."
      assert isinstance(scenario_data["url"], str), f"URL in {scenario_name} should be a string."
      assert isinstance(scenario_data["checkbox"], bool), f"Checkbox in {scenario_name} should be a boolean."
      assert isinstance(scenario_data["active"], bool), f"Active in {scenario_name} should be a boolean."
      assert isinstance(scenario_data["condition"], str), f"Condition in {scenario_name} should be a string."
      assert isinstance(scenario_data["presta_categories"], str), f"presta_categories in {scenario_name} should be a string."

def test_cdata_categories_desktops_scenario_active_values(cdata_categories_desktops_data):
    """
    Test that the 'active' values are always True.
    """
    for scenario_name, scenario_data in cdata_categories_desktops_data["scenarios"].items():
        assert scenario_data["active"] is True, f"Active in {scenario_name} should be True."

def test_cdata_categories_desktops_scenario_checkbox_values(cdata_categories_desktops_data):
    """
    Test that the 'checkbox' values are always False.
    """
    for scenario_name, scenario_data in cdata_categories_desktops_data["scenarios"].items():
        assert scenario_data["checkbox"] is False, f"Checkbox in {scenario_name} should be False."


def test_cdata_categories_desktops_scenario_condition_values(cdata_categories_desktops_data):
    """
    Test that the 'condition' values are always 'new'.
    """
    for scenario_name, scenario_data in cdata_categories_desktops_data["scenarios"].items():
        assert scenario_data["condition"] == "new", f"Condition in {scenario_name} should be 'new'."

def test_cdata_categories_desktops_scenario_url_not_empty(cdata_categories_desktops_data):
    """
    Test that the 'url' values are not empty strings or placeholder strings.
    """
    placeholder_strings = ["-------------------------------------DESKTOP DESKTOP HP AMD-----------------------------------",
                           "-------------------------------------DESKTOP HP pentium-----------------------------------",
                           "-------------------------------------DESKTOP DELL AMD-----------------------------------",
                           "-------------------------------------DESKTOP DELL pentium-----------------------------------"
                           ]
    for scenario_name, scenario_data in cdata_categories_desktops_data["scenarios"].items():
      url = scenario_data["url"]
      assert url, f"URL in {scenario_name} should not be empty."
      assert url not in placeholder_strings, f"URL in {scenario_name} should not be a placeholder string."

def test_cdata_categories_desktops_scenario_presta_categories_not_empty(cdata_categories_desktops_data):
  """
  Test that the 'presta_categories' values are not empty strings
  and contains only numbers and commas
  """
  for scenario_name, scenario_data in cdata_categories_desktops_data["scenarios"].items():
    presta_categories = scenario_data["presta_categories"]
    assert presta_categories, f"presta_categories in {scenario_name} should not be empty."
    assert all(char.isdigit() or char == ',' for char in presta_categories), f"presta_categories in {scenario_name} should only contain digits and commas."

def test_cdata_categories_desktops_scenario_presta_categories_format(cdata_categories_desktops_data):
    """
    Test that 'presta_categories' values are strings with comma-separated numbers.
    """
    for scenario_name, scenario_data in cdata_categories_desktops_data["scenarios"].items():
        presta_categories = scenario_data["presta_categories"]
        categories = presta_categories.split(',')
        for category in categories:
          assert category.isdigit(), f"Category '{category}' in 'presta_categories' of {scenario_name} should be a digit."
```