```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def morlevi_categories_data():
    """Loads the morlevi categories data from the JSON file."""
    file_path = "hypotez/src/suppliers/morlevi/scenarios/morlevi_categories_psu_antec.json"
    with open(file_path, 'r') as f:
        return json.load(f)

# Test to verify that the loaded data is a dictionary
def test_morlevi_categories_data_is_dict(morlevi_categories_data):
    """Checks if the loaded data is a dictionary."""
    assert isinstance(morlevi_categories_data, dict)

# Test to verify that the "scenarios" key exists
def test_morlevi_categories_data_has_scenarios_key(morlevi_categories_data):
    """Checks if the 'scenarios' key exists in the loaded data."""
    assert "scenarios" in morlevi_categories_data

# Test to verify that "scenarios" value is a dict
def test_morlevi_categories_scenarios_is_dict(morlevi_categories_data):
     """Checks if the 'scenarios' value is a dictionary."""
     assert isinstance(morlevi_categories_data["scenarios"], dict)

# Test to check for specific scenarios
def test_morlevi_categories_check_specific_scenarios(morlevi_categories_data):
     """Checks the content of some specific scenarios."""
     scenarios = morlevi_categories_data["scenarios"]
     assert "ANTEC 450W" in scenarios
     assert scenarios["ANTEC 450W"]["brand"] == "ANTEC"
     assert scenarios["ANTEC 450W"]["name"] == "450W"
     assert scenarios["ANTEC 450W"]["url"] == "https://www.morlevi.co.il/Cat/66?p_145=634&sort=datafloat2%2Cprice&keyword="
     assert scenarios["ANTEC 450W"]["checkbox"] == False
     assert scenarios["ANTEC 450W"]["active"] == True
     assert scenarios["ANTEC 450W"]["condition"] == "new"
     assert scenarios["ANTEC 450W"]["presta_categories"] == "158,511,188,577"

     assert "ANTEC 750W" in scenarios
     assert scenarios["ANTEC 750W"]["brand"] == "ANTEC"
     assert scenarios["ANTEC 750W"]["name"] == "750W"
     assert scenarios["ANTEC 750W"]["url"] == "https://www.morlevi.co.il/Cat/66?p_145=670&sort=datafloat2%2Cprice&keyword="
     assert scenarios["ANTEC 750W"]["checkbox"] == False
     assert scenarios["ANTEC 750W"]["active"] == True
     assert scenarios["ANTEC 750W"]["condition"] == "new"
     assert scenarios["ANTEC 750W"]["presta_categories"] == "151,158,511,194,577"

# Test to check if all scenarios has all the necessary keys
def test_morlevi_categories_all_scenarios_have_all_keys(morlevi_categories_data):
    """Checks if all scenarios have the required keys."""
    required_keys = ["brand", "name", "url", "checkbox", "active", "condition", "presta_categories"]
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
         for key in required_keys:
             assert key in scenario_data, f"Scenario '{scenario_name}' is missing key: '{key}'"

# Test to check if the 'url' value is a valid string
def test_morlevi_categories_url_is_string(morlevi_categories_data):
     """Checks if the URL is a string in all scenarios."""
     for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert isinstance(scenario_data["url"], str), f"URL in scenario '{scenario_name}' is not a string"

# Test to check if the 'checkbox' value is a boolean
def test_morlevi_categories_checkbox_is_bool(morlevi_categories_data):
     """Checks if the 'checkbox' is boolean in all scenarios."""
     for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert isinstance(scenario_data["checkbox"], bool), f"Checkbox in scenario '{scenario_name}' is not a boolean"

# Test to check if the 'active' value is a boolean
def test_morlevi_categories_active_is_bool(morlevi_categories_data):
     """Checks if the 'active' is boolean in all scenarios."""
     for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert isinstance(scenario_data["active"], bool), f"Active in scenario '{scenario_name}' is not a boolean"

# Test to check if the 'condition' value is a string
def test_morlevi_categories_condition_is_string(morlevi_categories_data):
    """Checks if the condition is a string in all scenarios."""
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert isinstance(scenario_data["condition"], str), f"Condition in scenario '{scenario_name}' is not a string"

# Test to check if the 'presta_categories' value is a string
def test_morlevi_categories_presta_categories_is_string(morlevi_categories_data):
    """Checks if the presta_categories is a string in all scenarios."""
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert isinstance(scenario_data["presta_categories"], str), f"'presta_categories' in scenario '{scenario_name}' is not a string"
```