```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def morlevi_data():
    """Loads the morlevi JSON data from the file."""
    file_location = "hypotez/src/suppliers/ivory/scenarios/morlevi_categories_monitors_samsung.json"
    with open(file_location, 'r') as f:
        return json.load(f)


def test_morlevi_data_structure(morlevi_data):
    """
    Checks if the loaded JSON has the correct top-level structure (i.e., a 'scenarios' key).
    """
    assert "scenarios" in morlevi_data, "The JSON should have a 'scenarios' key."
    assert isinstance(morlevi_data["scenarios"], dict), "The 'scenarios' value should be a dictionary."


def test_scenario_keys_exist(morlevi_data):
    """
    Checks that each scenario within 'scenarios' has the expected keys.
    """
    expected_keys = {"brand", "url", "checkbox", "active", "condition", "presta_categories"}
    for scenario_name, scenario_data in morlevi_data["scenarios"].items():
        assert set(scenario_data.keys()) == expected_keys, f"Scenario '{scenario_name}' is missing or has unexpected keys."


def test_scenario_data_types(morlevi_data):
    """
    Verifies the data type of each value in each scenario.
    """
    for scenario_name, scenario_data in morlevi_data["scenarios"].items():
        assert isinstance(scenario_data["brand"], str), f"Brand in '{scenario_name}' should be a string."
        assert isinstance(scenario_data["url"], str), f"URL in '{scenario_name}' should be a string."
        assert isinstance(scenario_data["checkbox"], bool), f"Checkbox in '{scenario_name}' should be a boolean."
        assert isinstance(scenario_data["active"], bool), f"Active in '{scenario_name}' should be a boolean."
        assert isinstance(scenario_data["condition"], str), f"Condition in '{scenario_name}' should be a string."
        assert isinstance(scenario_data["presta_categories"], dict), f"Presta Categories in '{scenario_name}' should be a dict."

def test_presta_categories_structure(morlevi_data):
    """
    Checks the structure inside 'presta_categories' for each scenario.
    """
    for scenario_name, scenario_data in morlevi_data["scenarios"].items():
        presta_categories = scenario_data["presta_categories"]
        assert "template" in presta_categories, f"'template' key is missing in presta_categories for '{scenario_name}'"
        assert isinstance(presta_categories["template"], dict), f"'template' value should be a dict for '{scenario_name}'"
        assert len(presta_categories["template"]) == 1, f"There should be only one key-value pair in template for '{scenario_name}'"
        for k, v in presta_categories["template"].items():
          assert isinstance(k, str), f"Key in template should be a string for '{scenario_name}'"
          assert isinstance(v, str), f"Value in template should be a string for '{scenario_name}'"

def test_url_format(morlevi_data):
    """
    Checks that URLs are strings and start with 'https://'.
    """
    for scenario_name, scenario_data in morlevi_data["scenarios"].items():
        url = scenario_data["url"]
        assert url.startswith("https://"), f"URL for '{scenario_name}' should start with 'https://'."


def test_scenario_values_non_empty(morlevi_data):
    """
    Ensures that values for brand, url, and condition are not empty strings.
    """
    for scenario_name, scenario_data in morlevi_data["scenarios"].items():
        assert scenario_data["brand"], f"Brand value should not be empty for '{scenario_name}'."
        assert scenario_data["url"], f"URL value should not be empty for '{scenario_name}'."
        assert scenario_data["condition"], f"Condition value should not be empty for '{scenario_name}'."

def test_checkbox_active_values(morlevi_data):
    """
    Checks if 'checkbox' and 'active' are boolean
    """
    for scenario_name, scenario_data in morlevi_data["scenarios"].items():
        assert isinstance(scenario_data["checkbox"], bool), f"Checkbox value should be a boolean for '{scenario_name}'."
        assert isinstance(scenario_data["active"], bool), f"Active value should be a boolean for '{scenario_name}'."
```