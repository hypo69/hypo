```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def morlevi_categories_data():
    """Loads the JSON data from the file."""
    file_path = "hypotez/src/suppliers/morlevi/scenarios/morlevi_categories_storage_gigabyte.json"
    with open(file_path, 'r') as f:
        return json.load(f)

def test_scenarios_structure(morlevi_categories_data):
    """
    Tests if the loaded JSON has the correct 'scenarios' structure, which should be a dictionary.
    """
    assert "scenarios" in morlevi_categories_data, "The JSON should have a 'scenarios' key."
    assert isinstance(morlevi_categories_data["scenarios"], dict), "'scenarios' should be a dictionary."

def test_scenario_keys(morlevi_categories_data):
    """
    Tests if each scenario within 'scenarios' has the expected keys: brand, name, url, checkbox, active, condition, and presta_categories.
    """
    expected_keys = ["brand", "name", "url", "checkbox", "active", "condition", "presta_categories"]
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert isinstance(scenario_data, dict), f"Scenario '{scenario_name}' data should be a dictionary."
        for key in expected_keys:
            assert key in scenario_data, f"Scenario '{scenario_name}' should contain the key '{key}'."

def test_scenario_values_types(morlevi_categories_data):
     """
     Tests if each scenario's values have the expected types.
     """
     for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
         assert isinstance(scenario_data["brand"], str), f"Scenario '{scenario_name}' brand should be a string."
         assert isinstance(scenario_data["name"], str), f"Scenario '{scenario_name}' name should be a string."
         assert isinstance(scenario_data["url"], str), f"Scenario '{scenario_name}' url should be a string."
         assert isinstance(scenario_data["checkbox"], bool), f"Scenario '{scenario_name}' checkbox should be a boolean."
         assert isinstance(scenario_data["active"], bool), f"Scenario '{scenario_name}' active should be a boolean."
         assert isinstance(scenario_data["condition"], str), f"Scenario '{scenario_name}' condition should be a string."
         assert isinstance(scenario_data["presta_categories"], str), f"Scenario '{scenario_name}' presta_categories should be a string."

def test_scenario_url_validity(morlevi_categories_data):
    """
    Tests if URLs are valid strings (does not check if the URL is actually a valid internet address).
    Also checks for a specific pattern for the urls that should be the correct link.
    """
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        url = scenario_data["url"]
        assert isinstance(url, str), f"Scenario '{scenario_name}' URL should be a string."
        if  not url.startswith("---"):
            assert url.startswith("https://www.morlevi.co.il/Cat/"), f"Scenario '{scenario_name}' URL '{url}' does not start with 'https://www.morlevi.co.il/Cat/'"

def test_scenario_presta_categories_validity(morlevi_categories_data):
    """
    Tests if presta_categories is a string of comma-separated integers.
    """
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        presta_categories = scenario_data["presta_categories"]
        assert isinstance(presta_categories, str), f"Scenario '{scenario_name}' presta_categories should be a string."
        categories = presta_categories.split(",")
        for cat in categories:
            assert cat.isdigit(), f"Scenario '{scenario_name}' presta_categories contains non-digit value: '{cat}'."

def test_scenario_active_values(morlevi_categories_data):
     """
     Tests if all 'active' values are set to True.
     """
     for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
         assert scenario_data["active"] == True, f"Scenario '{scenario_name}' active should be True."

def test_scenario_checkbox_values(morlevi_categories_data):
     """
     Tests if all 'checkbox' values are set to False.
     """
     for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
         assert scenario_data["checkbox"] == False, f"Scenario '{scenario_name}' checkbox should be False."
```