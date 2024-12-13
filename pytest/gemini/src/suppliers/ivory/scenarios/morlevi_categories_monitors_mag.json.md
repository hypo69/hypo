```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def morlevi_categories_monitors_mag_data():
    """Loads the JSON data for testing."""
    json_data = """
    {
      "scenarios": {
        "MAG 22": {
          "brand": "MAG",
          "url": "https://www.morlevi.co.il/Cat/8?p_315=24&p_350=1805&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": "127,128,529"
        },
        "MAG 24-25": {
          "brand": "MAG",
          "url": "https://www.morlevi.co.il/Cat/8?p_315=24&p_350=1807&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": "127,129,529"
        },
        "MAG 27-29": {
          "brand": "MAG",
          "url": "https://www.morlevi.co.il/Cat/8?p_315=24&p_350=1808&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": "127,130,529"
        },
        "MAG 32": {
          "brand": "MAG",
          "url": "https://www.morlevi.co.il/Cat/8?p_315=24&p_350=1809&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": "127,131,529"
        },
        "MAG 34": {
          "brand": "MAG",
          "url": " --------------------------  MAG 34 -----------------------------------",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": "127,132,529"
        },
        "MAG 49": {
          "brand": "MAG",
          "url": "-----------------------------  MAG 49 ---------------------------------",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": "127,133,529"
        }
      }
    }
    """
    return json.loads(json_data)


def test_morlevi_categories_monitors_mag_data_load(morlevi_categories_monitors_mag_data):
    """
    Test if the JSON data is loaded correctly.
    Checks if the loaded data is a dictionary and has the 'scenarios' key
    """
    assert isinstance(morlevi_categories_monitors_mag_data, dict)
    assert "scenarios" in morlevi_categories_monitors_mag_data


def test_morlevi_categories_monitors_mag_scenario_count(morlevi_categories_monitors_mag_data):
    """
    Test if the correct number of scenarios are loaded.
    Checks if the 'scenarios' key contains the expected number of scenarios
    """
    assert len(morlevi_categories_monitors_mag_data["scenarios"]) == 6


def test_morlevi_categories_monitors_mag_scenario_structure(morlevi_categories_monitors_mag_data):
    """
    Test if each scenario has the correct structure.
    Checks if each scenario has the expected keys like 'brand', 'url', 'checkbox', 'active', 'condition', and 'presta_categories'
    """
    for scenario in morlevi_categories_monitors_mag_data["scenarios"].values():
        assert "brand" in scenario
        assert "url" in scenario
        assert "checkbox" in scenario
        assert "active" in scenario
        assert "condition" in scenario
        assert "presta_categories" in scenario


def test_morlevi_categories_monitors_mag_scenario_values(morlevi_categories_monitors_mag_data):
    """
    Test the values of a specific scenario for correctness.
    Checks the specific values of the "MAG 22" scenario to see if the values are correct
    """
    mag_22_scenario = morlevi_categories_monitors_mag_data["scenarios"]["MAG 22"]
    assert mag_22_scenario["brand"] == "MAG"
    assert mag_22_scenario["url"] == "https://www.morlevi.co.il/Cat/8?p_315=24&p_350=1805&sort=datafloat2%2Cprice&keyword="
    assert mag_22_scenario["checkbox"] == False
    assert mag_22_scenario["active"] == True
    assert mag_22_scenario["condition"] == "new"
    assert mag_22_scenario["presta_categories"] == "127,128,529"


def test_morlevi_categories_monitors_mag_invalid_url_scenario(morlevi_categories_monitors_mag_data):
    """
    Test scenarios with invalid URLs.
     Checks if scenarios "MAG 34" and "MAG 49" have invalid URLs and if the other values are correct
    """
    mag_34_scenario = morlevi_categories_monitors_mag_data["scenarios"]["MAG 34"]
    assert mag_34_scenario["brand"] == "MAG"
    assert mag_34_scenario["url"] == " --------------------------  MAG 34 -----------------------------------"
    assert mag_34_scenario["checkbox"] == False
    assert mag_34_scenario["active"] == True
    assert mag_34_scenario["condition"] == "new"
    assert mag_34_scenario["presta_categories"] == "127,132,529"

    mag_49_scenario = morlevi_categories_monitors_mag_data["scenarios"]["MAG 49"]
    assert mag_49_scenario["brand"] == "MAG"
    assert mag_49_scenario["url"] == "-----------------------------  MAG 49 ---------------------------------"
    assert mag_49_scenario["checkbox"] == False
    assert mag_49_scenario["active"] == True
    assert mag_49_scenario["condition"] == "new"
    assert mag_49_scenario["presta_categories"] == "127,133,529"
```