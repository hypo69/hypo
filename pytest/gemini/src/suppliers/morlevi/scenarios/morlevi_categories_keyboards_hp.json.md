```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def morlevi_categories_data():
    """Provides the morlevi categories data from the JSON file."""
    json_data = """
    {
      "scenarios": {
        "HP WIRELESS KEYBOARD": {
          "brand": "HP",
          "url": "-----------------------------------------------HP WIRELESS KEYBOARD----------------------------------------------",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": "203,204,316"
        },
        "HP USB KEYBOARD": {
          "brand": "HP",
          "url": "-------------------------------------------------------------------------------",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": "203,204,315"
        },
        "HP USB MOUSE": {
          "brand": "HP",
          "url": "------------------------------------------------------HP USB MOUSE------------------------------------------------",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": "203,206,317"
        },
        "HP WIRELESS MOUSE": {
          "brand": "HP",
          "url": "---------------------------------------------------------------------------",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": "203,206,318"
        },
        "HP USB KEYBOARD-MOUSE SET": {
          "brand": "HP",
          "url": "--------------------------------------------------------------------------",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": "203,207,208"
        },
        "HP WIRELESS  KEYBOARD-MOUSE SET": {
          "brand": "HP",
          "url": "https://www.morlevi.co.il/Cat/114?p_315=10&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": "203,207,334"
        }
      }
    }
    """
    return json.loads(json_data)

# Test cases for the structure and content of the loaded JSON data
def test_morlevi_categories_data_structure(morlevi_categories_data):
    """
    Tests if the loaded JSON data has the correct structure (i.e., a 'scenarios' key).
    """
    assert "scenarios" in morlevi_categories_data, "The JSON data should have a 'scenarios' key."
    assert isinstance(morlevi_categories_data["scenarios"], dict), "The 'scenarios' value should be a dictionary."

def test_morlevi_categories_data_count(morlevi_categories_data):
    """
    Tests if the loaded JSON data contains the correct number of scenarios.
    """
    assert len(morlevi_categories_data["scenarios"]) == 6, "The JSON data should contain exactly 6 scenarios."


def test_morlevi_categories_data_content(morlevi_categories_data):
    """
    Tests the content of a specific scenario within the loaded JSON data.
    Checks for the correct brand, url, checkbox value, active state, condition and presta_categories of a scenario.
    """
    scenario = morlevi_categories_data["scenarios"]["HP WIRELESS KEYBOARD"]
    assert scenario["brand"] == "HP", "The brand for 'HP WIRELESS KEYBOARD' should be 'HP'."
    assert scenario["url"] == "-----------------------------------------------HP WIRELESS KEYBOARD----------------------------------------------", "The URL for 'HP WIRELESS KEYBOARD' is incorrect."
    assert scenario["checkbox"] == False, "The checkbox value for 'HP WIRELESS KEYBOARD' should be False."
    assert scenario["active"] == True, "The active value for 'HP WIRELESS KEYBOARD' should be True."
    assert scenario["condition"] == "new", "The condition for 'HP WIRELESS KEYBOARD' should be 'new'."
    assert scenario["presta_categories"] == "203,204,316", "The presta_categories for 'HP WIRELESS KEYBOARD' should be '203,204,316'."


def test_morlevi_categories_data_edge_case_url(morlevi_categories_data):
    """
    Tests a scenario with a non-standard URL, verifying correct loading.
    """
    scenario = morlevi_categories_data["scenarios"]["HP WIRELESS  KEYBOARD-MOUSE SET"]
    assert scenario["url"] == "https://www.morlevi.co.il/Cat/114?p_315=10&sort=datafloat2%2Cprice&keyword=", "The URL for 'HP WIRELESS  KEYBOARD-MOUSE SET' is incorrect."


def test_morlevi_categories_data_all_keys_present(morlevi_categories_data):
    """
    Tests if all the required keys ('brand', 'url', 'checkbox', 'active', 'condition', 'presta_categories') are present in all scenarios.
    """
    for scenario_name, scenario in morlevi_categories_data["scenarios"].items():
        assert "brand" in scenario, f"The 'brand' key is missing in scenario '{scenario_name}'."
        assert "url" in scenario, f"The 'url' key is missing in scenario '{scenario_name}'."
        assert "checkbox" in scenario, f"The 'checkbox' key is missing in scenario '{scenario_name}'."
        assert "active" in scenario, f"The 'active' key is missing in scenario '{scenario_name}'."
        assert "condition" in scenario, f"The 'condition' key is missing in scenario '{scenario_name}'."
        assert "presta_categories" in scenario, f"The 'presta_categories' key is missing in scenario '{scenario_name}'."

def test_morlevi_categories_data_presta_categories_type(morlevi_categories_data):
    """
     Tests if 'presta_categories' value is string in all scenarios.
    """
    for scenario_name, scenario in morlevi_categories_data["scenarios"].items():
        assert isinstance(scenario["presta_categories"], str), f"The 'presta_categories' value for '{scenario_name}' should be a string."

def test_morlevi_categories_data_checkbox_type(morlevi_categories_data):
    """
     Tests if 'checkbox' value is boolean in all scenarios.
    """
    for scenario_name, scenario in morlevi_categories_data["scenarios"].items():
        assert isinstance(scenario["checkbox"], bool), f"The 'checkbox' value for '{scenario_name}' should be a boolean."

def test_morlevi_categories_data_active_type(morlevi_categories_data):
    """
     Tests if 'active' value is boolean in all scenarios.
    """
    for scenario_name, scenario in morlevi_categories_data["scenarios"].items():
        assert isinstance(scenario["active"], bool), f"The 'active' value for '{scenario_name}' should be a boolean."

def test_morlevi_categories_data_condition_type(morlevi_categories_data):
    """
     Tests if 'condition' value is string in all scenarios.
    """
    for scenario_name, scenario in morlevi_categories_data["scenarios"].items():
         assert isinstance(scenario["condition"], str), f"The 'condition' value for '{scenario_name}' should be a string."
```