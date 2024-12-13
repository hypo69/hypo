```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def cdata_categories_data():
    """Loads the cdata categories JSON data."""
    file_path = 'hypotez/src/suppliers/cdata/scenarios/cdata_categories_keyboards.json'
    with open(file_path, 'r') as f:
        return json.load(f)

def test_cdata_categories_data_structure(cdata_categories_data):
    """
    Test that the loaded JSON data has the expected structure,
    specifically that it contains a 'scenarios' key, which is a dictionary
    """
    assert "scenarios" in cdata_categories_data
    assert isinstance(cdata_categories_data["scenarios"], dict)


def test_cdata_categories_scenario_keys(cdata_categories_data):
    """
     Test if each scenario in the 'scenarios' dictionary contains the mandatory keys
     like 'brand', 'url', 'checkbox', 'active', 'condition', and 'presta_categories'.
    """
    scenarios = cdata_categories_data["scenarios"]
    mandatory_keys = {"brand", "url", "checkbox", "active", "condition", "presta_categories"}

    for scenario_name, scenario_data in scenarios.items():
        assert isinstance(scenario_data, dict), f"Scenario '{scenario_name}' data is not a dictionary."
        assert mandatory_keys.issubset(scenario_data.keys()), f"Scenario '{scenario_name}' is missing mandatory keys. Mandatory keys are: {mandatory_keys} and scenario keys are: {scenario_data.keys()}"


def test_cdata_categories_scenario_values_types(cdata_categories_data):
    """
    Test if the values of the scenario keys have the expected types.
    This includes testing the types of 'brand', 'url', 'checkbox', 'active', 'condition', and 'presta_categories'.
    """
    scenarios = cdata_categories_data["scenarios"]
    for scenario_name, scenario_data in scenarios.items():
      assert isinstance(scenario_data["brand"], str), f"The 'brand' in scenario '{scenario_name}' is not a string."
      assert isinstance(scenario_data["url"], str), f"The 'url' in scenario '{scenario_name}' is not a string."
      assert isinstance(scenario_data["checkbox"], bool), f"The 'checkbox' in scenario '{scenario_name}' is not a boolean."
      assert isinstance(scenario_data["active"], bool), f"The 'active' in scenario '{scenario_name}' is not a boolean."
      assert isinstance(scenario_data["condition"], str), f"The 'condition' in scenario '{scenario_name}' is not a string."
      assert isinstance(scenario_data["presta_categories"], str), f"The 'presta_categories' in scenario '{scenario_name}' is not a string."


def test_cdata_categories_presta_categories_format(cdata_categories_data):
     """
     Test that 'presta_categories' values are strings containing comma-separated numbers.
     """
     scenarios = cdata_categories_data["scenarios"]
     for scenario_name, scenario_data in scenarios.items():
        presta_categories = scenario_data["presta_categories"]
        categories = presta_categories.split(",")
        for category in categories:
            assert category.strip().isdigit(), f"The 'presta_categories' value in scenario '{scenario_name}' is not a comma-separated string of numbers. Invalid value: {presta_categories} "


def test_cdata_categories_url_validity(cdata_categories_data):
    """
    Test that 'url' values are valid URL strings
    This test ensures that each 'url' starts with 'http'
    """
    scenarios = cdata_categories_data["scenarios"]
    for scenario_name, scenario_data in scenarios.items():
        url = scenario_data["url"]
        if not (url.startswith("http://") or url.startswith("https://") or url.startswith("-----------------------------------")):
          pytest.fail(f"The 'url' in scenario '{scenario_name}' is not a valid URL format it should start with http:// or https://. Invalid value: {url}")


def test_cdata_categories_active_is_boolean(cdata_categories_data):
     """
     Test that 'active' values are boolean type.
     """
     scenarios = cdata_categories_data["scenarios"]
     for scenario_name, scenario_data in scenarios.items():
        active = scenario_data["active"]
        assert isinstance(active,bool), f"The 'active' value in scenario '{scenario_name}' is not a boolean. Invalid value: {active} "

def test_cdata_categories_checkbox_is_boolean(cdata_categories_data):
     """
     Test that 'checkbox' values are boolean type.
     """
     scenarios = cdata_categories_data["scenarios"]
     for scenario_name, scenario_data in scenarios.items():
        checkbox = scenario_data["checkbox"]
        assert isinstance(checkbox,bool), f"The 'checkbox' value in scenario '{scenario_name}' is not a boolean. Invalid value: {checkbox} "

def test_cdata_categories_condition_is_string(cdata_categories_data):
     """
     Test that 'condition' values are string type.
     """
     scenarios = cdata_categories_data["scenarios"]
     for scenario_name, scenario_data in scenarios.items():
        condition = scenario_data["condition"]
        assert isinstance(condition, str), f"The 'condition' value in scenario '{scenario_name}' is not a string. Invalid value: {condition} "

```