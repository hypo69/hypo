```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def morlevi_categories_data():
    """Loads the morlevi_categories_sound.json data."""
    file_path = "hypotez/src/suppliers/morlevi/scenarios/morlevi_categories_sound.json"
    with open(file_path, 'r') as f:
        return json.load(f)

# Test case for checking the structure of the loaded data
def test_morlevi_categories_data_structure(morlevi_categories_data):
    """Checks if the loaded data has the correct 'scenarios' key and is a dict."""
    assert "scenarios" in morlevi_categories_data
    assert isinstance(morlevi_categories_data["scenarios"], dict)

# Test case for checking the presence of expected scenarios
def test_morlevi_categories_expected_scenarios(morlevi_categories_data):
    """Checks for specific scenarios and their expected attributes."""
    scenarios = morlevi_categories_data["scenarios"]
    
    assert "Logitech speakers" in scenarios
    assert scenarios["Logitech speakers"]["brand"] == "LOGITECH"
    assert scenarios["Logitech speakers"]["url"].startswith("https://www.morlevi.co.il/Cat/161")
    assert scenarios["Logitech speakers"]["checkbox"] == False
    assert scenarios["Logitech speakers"]["active"] == True
    assert scenarios["Logitech speakers"]["condition"] == "new"
    assert scenarios["Logitech speakers"]["presta_categories"] == "520,521"
    
    assert "Headphones Corsair" in scenarios
    assert scenarios["Headphones Corsair"]["brand"] == "Corsair"
    assert scenarios["Headphones Corsair"]["presta_categories"] == "520,522"

    assert "Cams GENERIC AONI" in scenarios
    assert scenarios["Cams GENERIC AONI"]["brand"] == "GENERIC"
    assert scenarios["Cams GENERIC AONI"]["presta_categories"] == "520,523"


# Test case to check all scenarios have required keys
def test_morlevi_categories_all_scenarios_have_keys(morlevi_categories_data):
    """Checks if all scenarios have the necessary keys."""
    required_keys = ["brand", "url", "checkbox", "active", "condition", "presta_categories"]
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        for key in required_keys:
             assert key in scenario_data, f"Scenario '{scenario_name}' is missing key: {key}"

# Test case for ensuring brand values are strings
def test_morlevi_categories_brand_values_are_strings(morlevi_categories_data):
     """Checks that all brand values are strings"""
     for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
          assert isinstance(scenario_data["brand"], str), f"Brand value for scenario '{scenario_name}' is not a string"

# Test case to check if URLs are valid strings and start with the correct domain
def test_morlevi_categories_url_format(morlevi_categories_data):
    """Checks if URLs are strings and start with the correct domain."""
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert isinstance(scenario_data["url"], str), f"URL for scenario '{scenario_name}' is not a string"
        assert scenario_data["url"].startswith("https://www.morlevi.co.il/Cat/"), f"URL for scenario '{scenario_name}' does not start with expected domain"

# Test case to check if 'checkbox' and 'active' values are booleans
def test_morlevi_categories_checkbox_active_are_booleans(morlevi_categories_data):
    """Checks if checkbox and active values are boolean."""
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert isinstance(scenario_data["checkbox"], bool), f"Checkbox for scenario '{scenario_name}' is not a boolean"
        assert isinstance(scenario_data["active"], bool), f"Active for scenario '{scenario_name}' is not a boolean"

# Test case to check if 'condition' values are strings
def test_morlevi_categories_condition_are_strings(morlevi_categories_data):
    """Checks if condition values are strings."""
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert isinstance(scenario_data["condition"], str), f"Condition for scenario '{scenario_name}' is not a string"

# Test case to check if 'presta_categories' values are strings containing digits and commas only
def test_morlevi_categories_presta_categories_format(morlevi_categories_data):
    """Checks if presta_categories are strings with digits and commas only."""
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert isinstance(scenario_data["presta_categories"], str), f"presta_categories for scenario '{scenario_name}' is not a string"
        assert all(char.isdigit() or char == ',' for char in scenario_data["presta_categories"]), f"presta_categories for '{scenario_name}' contains invalid characters"
```