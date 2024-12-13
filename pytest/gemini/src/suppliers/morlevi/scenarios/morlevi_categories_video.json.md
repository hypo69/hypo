```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def morlevi_categories_data():
    """Loads the JSON data for testing."""
    file_path = "hypotez/src/suppliers/morlevi/scenarios/morlevi_categories_video.json"
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

# Test to ensure the structure of the JSON file is correct
def test_json_structure(morlevi_categories_data):
    """Checks if the JSON has the expected structure."""
    assert "scenarios" in morlevi_categories_data
    assert isinstance(morlevi_categories_data["scenarios"], dict)

# Test for the presence of required keys in each scenario
def test_scenario_keys_presence(morlevi_categories_data):
    """Checks if all required keys are present in each scenario."""
    required_keys = ["brand", "url", "checkbox", "active", "condition", "presta_categories"]
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
         for key in required_keys:
            assert key in scenario_data, f"Key '{key}' missing in scenario '{scenario_name}'"

# Test to check the data types of each value in scenario
def test_scenario_data_types(morlevi_categories_data):
    """Checks the data types of values within each scenario."""
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert isinstance(scenario_data["brand"], str), f"brand in scenario '{scenario_name}' should be a string"
        assert isinstance(scenario_data["url"], str), f"url in scenario '{scenario_name}' should be a string"
        assert isinstance(scenario_data["checkbox"], bool), f"checkbox in scenario '{scenario_name}' should be a boolean"
        assert isinstance(scenario_data["active"], bool), f"active in scenario '{scenario_name}' should be a boolean"
        assert isinstance(scenario_data["condition"], str), f"condition in scenario '{scenario_name}' should be a string"
        assert isinstance(scenario_data["presta_categories"], dict), f"presta_categories in scenario '{scenario_name}' should be a dict"
        assert "template" in scenario_data["presta_categories"], f"template key missing in 'presta_categories' in scenario '{scenario_name}'"
        assert isinstance(scenario_data["presta_categories"]["template"], dict), f"template in 'presta_categories' in scenario '{scenario_name}' should be a dict"

# Test to check if 'brand' values are not empty strings
def test_scenario_brand_not_empty(morlevi_categories_data):
    """Checks that the 'brand' value in each scenario is not an empty string."""
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert scenario_data["brand"] != "", f"Brand in scenario '{scenario_name}' should not be an empty string."

# Test to check if url values are valid URLs
def test_scenario_url_valid(morlevi_categories_data):
    """Checks if the 'url' values in each scenario are valid URLs."""
    import re
    url_pattern = re.compile(r'^(https?://)[\w.-]+(/[\w.-]*)*/?$')
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert url_pattern.match(scenario_data["url"]), f"URL in scenario '{scenario_name}' is not a valid URL."

# Test to check if "template" values are not empty
def test_presta_template_not_empty(morlevi_categories_data):
    """Checks that the 'template' dict in 'presta_categories' is not empty."""
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
         assert scenario_data["presta_categories"]["template"] , f"template in presta_categories  in scenario '{scenario_name}' should not be an empty dict"
         assert len(scenario_data["presta_categories"]["template"]) > 0, f"template in presta_categories in scenario '{scenario_name}' should not be an empty dict"

# Test to ensure keys in "template" is a string
def test_presta_template_keys_string(morlevi_categories_data):
    """Checks that the keys in the 'template' dict in 'presta_categories' are strings."""
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
         for key in scenario_data["presta_categories"]["template"].keys():
            assert isinstance(key, str) , f"Keys in the 'template' dict in scenario '{scenario_name}' should be a string"

# Test to ensure values in "template" is a string
def test_presta_template_values_string(morlevi_categories_data):
    """Checks that the values in the 'template' dict in 'presta_categories' are strings."""
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
         for value in scenario_data["presta_categories"]["template"].values():
            assert isinstance(value, str) , f"Values in the 'template' dict in scenario '{scenario_name}' should be a string"

# Test to check all conditions are "new"
def test_condition_value_new(morlevi_categories_data):
    """Checks that the 'condition' value in each scenario is always 'new'."""
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert scenario_data["condition"] == "new", f"Condition in scenario '{scenario_name}' should be 'new'"

# Test for checking the scenarios keys are string
def test_scenario_name_is_string(morlevi_categories_data):
    """Checks if the scenario names are strings"""
    for scenario_name in morlevi_categories_data["scenarios"]:
        assert isinstance(scenario_name, str), f"Scenario name '{scenario_name}' should be a string."
```