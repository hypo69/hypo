```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def morlevi_categories_data():
    """Provides the loaded JSON data for tests."""
    json_data = """
    {
      "scenarios": {
        "GENIUS WIRELESS KEYBOARD": {
          "brand": "GENIUS",
          "url": "-----------------------------------------------GENIUS WIRELESS KEYBOARD----------------------------------------------",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": "203,204,316"
        },
        "GENIUS USB KEYBOARD": {
          "brand": "GENIUS",
          "url": "https://www.morlevi.co.il/Cat/155?p_315=43&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": "203,204,315"
        },
        "GENIUS USB MOUSE": {
          "brand": "GENIUS",
          "url": "https://www.morlevi.co.il/Cat/108?p_315=43&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": "203,206,317"
        },
        "GENIUS WIRELESS MOUSE": {
          "brand": "GENIUS",
          "url": "https://www.morlevi.co.il/Cat/109?p_315=43&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": "203,206,318"
        },
        "GENIUS USB KEYBOARD-MOUSE SET": {
          "brand": "GENIUS",
          "url": "https://www.morlevi.co.il/Cat/113?p_315=43&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": "203,207,208"
        },
        "GENIUS WIRELESS  KEYBOARD-MOUSE SET": {
          "brand": "GENIUS",
          "url": "https://www.morlevi.co.il/Cat/114?p_315=43&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": "203,207,334"
        }
      }
    }
    """
    return json.loads(json_data)

# Test to check if the data is loaded correctly
def test_morlevi_categories_data_loaded(morlevi_categories_data):
    """Test if the data is loaded correctly."""
    assert isinstance(morlevi_categories_data, dict)
    assert "scenarios" in morlevi_categories_data
    assert isinstance(morlevi_categories_data["scenarios"], dict)
    assert len(morlevi_categories_data["scenarios"]) == 6


# Test case for a specific scenario
def test_genius_wireless_keyboard_scenario(morlevi_categories_data):
    """Test the 'GENIUS WIRELESS KEYBOARD' scenario."""
    scenario = morlevi_categories_data["scenarios"]["GENIUS WIRELESS KEYBOARD"]
    assert scenario["brand"] == "GENIUS"
    assert scenario["url"] == "-----------------------------------------------GENIUS WIRELESS KEYBOARD----------------------------------------------"
    assert scenario["checkbox"] == False
    assert scenario["active"] == True
    assert scenario["condition"] == "new"
    assert scenario["presta_categories"] == "203,204,316"


# Test case for another specific scenario
def test_genius_usb_keyboard_scenario(morlevi_categories_data):
    """Test the 'GENIUS USB KEYBOARD' scenario."""
    scenario = morlevi_categories_data["scenarios"]["GENIUS USB KEYBOARD"]
    assert scenario["brand"] == "GENIUS"
    assert scenario["url"] == "https://www.morlevi.co.il/Cat/155?p_315=43&sort=datafloat2%2Cprice&keyword="
    assert scenario["checkbox"] == False
    assert scenario["active"] == True
    assert scenario["condition"] == "new"
    assert scenario["presta_categories"] == "203,204,315"


# Test case for edge case or missing values, if applicable
def test_scenario_with_missing_url(morlevi_categories_data):
    """Test if scenario with missing url handle it correctly."""
    scenario = morlevi_categories_data["scenarios"].get("GENIUS WIRELESS KEYBOARD")
    assert scenario.get("url") is not None, "URL should be present"

# Test case if scenario is missing
def test_scenario_missing(morlevi_categories_data):
    """Test if a missing scenario will return none."""
    scenario = morlevi_categories_data["scenarios"].get("NON EXISTING SCENARIO")
    assert scenario is None, "Scenario should not exists"

# Test case to verify the data type of the values.
def test_data_types(morlevi_categories_data):
    """Test the data types of the different values."""
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert isinstance(scenario_data["brand"], str), f"Brand should be a string in {scenario_name}"
        assert isinstance(scenario_data["url"], str), f"URL should be a string in {scenario_name}"
        assert isinstance(scenario_data["checkbox"], bool), f"checkbox should be a boolean in {scenario_name}"
        assert isinstance(scenario_data["active"], bool), f"active should be a boolean in {scenario_name}"
        assert isinstance(scenario_data["condition"], str), f"condition should be a string in {scenario_name}"
        assert isinstance(scenario_data["presta_categories"], str), f"presta_categories should be a string in {scenario_name}"
```