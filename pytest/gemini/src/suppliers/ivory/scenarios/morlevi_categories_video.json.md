```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def morlevi_data():
    """Loads the morlevi_categories_video.json data."""
    file_path = "hypotez/src/suppliers/ivory/scenarios/morlevi_categories_video.json"
    with open(file_path, 'r') as f:
        return json.load(f)


def test_morlevi_data_structure(morlevi_data):
    """
    Test that the loaded data has the expected structure.
    Checks for the existence of the 'scenarios' key and that its value is a dictionary.
    """
    assert "scenarios" in morlevi_data
    assert isinstance(morlevi_data["scenarios"], dict)


def test_morlevi_scenario_keys(morlevi_data):
     """
     Test that each scenario in the JSON data has the required keys.
     Iterates through each scenario and checks that it contains the keys 'brand', 'url', 'checkbox', 'active',
     'condition', and 'presta_categories'.
     """
     for scenario_name, scenario_data in morlevi_data["scenarios"].items():
        assert "brand" in scenario_data, f"Missing 'brand' key in scenario: {scenario_name}"
        assert "url" in scenario_data, f"Missing 'url' key in scenario: {scenario_name}"
        assert "checkbox" in scenario_data, f"Missing 'checkbox' key in scenario: {scenario_name}"
        assert "active" in scenario_data, f"Missing 'active' key in scenario: {scenario_name}"
        assert "condition" in scenario_data, f"Missing 'condition' key in scenario: {scenario_name}"
        assert "presta_categories" in scenario_data, f"Missing 'presta_categories' key in scenario: {scenario_name}"

def test_morlevi_scenario_values_types(morlevi_data):
    """
    Test that the values in each scenario have the expected types.
    Verifies that 'brand' is a string, 'url' is a string, 'checkbox' is a boolean, 'active' is a boolean,
    'condition' is a string and 'presta_categories' is a dictionary.
    """
    for scenario_name, scenario_data in morlevi_data["scenarios"].items():
        assert isinstance(scenario_data["brand"], str), f"Invalid type for 'brand' in scenario: {scenario_name}"
        assert isinstance(scenario_data["url"], str), f"Invalid type for 'url' in scenario: {scenario_name}"
        assert isinstance(scenario_data["checkbox"], bool), f"Invalid type for 'checkbox' in scenario: {scenario_name}"
        assert isinstance(scenario_data["active"], bool), f"Invalid type for 'active' in scenario: {scenario_name}"
        assert isinstance(scenario_data["condition"], str), f"Invalid type for 'condition' in scenario: {scenario_name}"
        assert isinstance(scenario_data["presta_categories"], dict), f"Invalid type for 'presta_categories' in scenario: {scenario_name}"


def test_morlevi_presta_categories_template(morlevi_data):
    """
    Test that the 'presta_categories' structure is valid.
    Checks that each 'presta_categories' has a 'template' key and that it's a dictionary.
    Then it checks that each template has a single key value pair
    """
    for scenario_name, scenario_data in morlevi_data["scenarios"].items():
        presta_categories = scenario_data["presta_categories"]
        assert "template" in presta_categories, f"Missing 'template' key in presta_categories of scenario: {scenario_name}"
        assert isinstance(presta_categories["template"], dict), f"Invalid type for 'template' in presta_categories of scenario: {scenario_name}"
        assert len(presta_categories["template"]) == 1, f"Template should have only one key-value pair in scenario: {scenario_name}"

def test_morlevi_urls_are_strings(morlevi_data):
    """
    Test that the 'url' values are valid strings.
     Iterates through each scenario and checks if the value of the 'url' key is a string
    """
    for scenario_name, scenario_data in morlevi_data["scenarios"].items():
         assert isinstance(scenario_data["url"], str), f"Invalid type for url in scenario {scenario_name}"

def test_morlevi_all_active_is_bool(morlevi_data):
    """
    Test that the 'active' values are booleans.
    Iterates through each scenario and checks if the value of the 'active' key is boolean
    """
    for scenario_name, scenario_data in morlevi_data["scenarios"].items():
        assert isinstance(scenario_data["active"], bool), f"Invalid type for active in scenario {scenario_name}"
def test_morlevi_all_checkbox_is_bool(morlevi_data):
    """
    Test that the 'checkbox' values are booleans.
    Iterates through each scenario and checks if the value of the 'checkbox' key is boolean
    """
    for scenario_name, scenario_data in morlevi_data["scenarios"].items():
        assert isinstance(scenario_data["checkbox"], bool), f"Invalid type for checkbox in scenario {scenario_name}"


def test_morlevi_condition_is_string(morlevi_data):
    """
    Test that the 'condition' values are strings.
    Iterates through each scenario and checks if the value of the 'condition' key is string
    """
    for scenario_name, scenario_data in morlevi_data["scenarios"].items():
         assert isinstance(scenario_data["condition"], str), f"Invalid type for condition in scenario {scenario_name}"
```