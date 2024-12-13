```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def morlevi_categories_data():
    """Loads the JSON data for testing."""
    json_data = """
    {
      "scenarios": {
        "DELL 22": {
          "brand": "DELL",
          "url": "--------------------------------- DELL 22 -----------------------------------------------------------------",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": "127,128,528"
        },
        "DELL 24-25": {
          "brand": "DELL",
          "url": "https://www.morlevi.co.il/Cat/8?p_315=7&p_350=1807&p_75=483&p_75=292&p_75=293&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": "127,129,528"
    
        },
        "DELL 27-29": {
          "brand": "DELL",
          "url": "https://www.morlevi.co.il/Cat/8?p_315=7&p_350=1808&p_75=297&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": "127,130,528"
        },
        "DELL 32": {
          "brand": "DELL",
          "url": "https://www.morlevi.co.il/Cat/8?p_315=7&p_350=1809&p_75=298&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": "127,131,528"
        },
        "DELL 34": {
          "brand": "DELL",
          "url": " --------------------------  DELL 34 -----------------------------------",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": "127,132,528"
        },
        "DELL 49": {
          "brand": "DELL",
          "url": "-----------------------------  DELL 49 ---------------------------------",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": "127,133,528"
        }
      }
    }
    """
    return json.loads(json_data)


def test_morlevi_categories_data_structure(morlevi_categories_data):
    """
    Test that the base structure of the data is correct.
    Checks if 'scenarios' key exists and is a dictionary.
    """
    assert "scenarios" in morlevi_categories_data
    assert isinstance(morlevi_categories_data["scenarios"], dict)


def test_morlevi_scenario_keys(morlevi_categories_data):
    """
    Test if each scenario has the correct keys.
    Checks for 'brand', 'url', 'checkbox', 'active', 'condition', 'presta_categories' keys
    in the 'scenarios' dictionary.
    """
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert "brand" in scenario_data
        assert "url" in scenario_data
        assert "checkbox" in scenario_data
        assert "active" in scenario_data
        assert "condition" in scenario_data
        assert "presta_categories" in scenario_data

def test_morlevi_scenario_data_types(morlevi_categories_data):
    """
    Test the data types of the values in each scenario.
    Checks that 'brand' and 'url' are strings, 'checkbox' and 'active' are booleans,
    and 'presta_categories' is a string.
    """
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert isinstance(scenario_data["brand"], str)
        assert isinstance(scenario_data["url"], str)
        assert isinstance(scenario_data["checkbox"], bool)
        assert isinstance(scenario_data["active"], bool)
        assert isinstance(scenario_data["condition"], str)
        assert isinstance(scenario_data["presta_categories"], str)

def test_morlevi_scenario_active_values(morlevi_categories_data):
     """
    Test the  'active' values in each scenario.
    Checks that all active flags are True
    """
     for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert scenario_data["active"] == True

def test_morlevi_scenario_checkbox_values(morlevi_categories_data):
     """
    Test the  'checkbox' values in each scenario.
    Checks that all checkbox flags are False
    """
     for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert scenario_data["checkbox"] == False

def test_morlevi_scenario_condition_values(morlevi_categories_data):
    """
    Test the 'condition' values in each scenario.
    Checks that all conditions are 'new'
    """
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert scenario_data["condition"] == "new"

def test_morlevi_scenario_presta_categories_format(morlevi_categories_data):
    """
    Test the format of 'presta_categories'.
    Checks if it is a comma-separated string of numbers.
    """
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        categories = scenario_data["presta_categories"].split(',')
        for cat in categories:
          assert cat.strip().isdigit()



def test_morlevi_scenario_urls_not_empty(morlevi_categories_data):
    """
    Test that the url is not an empty string.
    """
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
         assert len(scenario_data["url"])>0

def test_morlevi_scenario_brand_values(morlevi_categories_data):
    """
    Test the 'brand' values in each scenario.
     Checks that all brand values are DELL
    """
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert scenario_data["brand"] == "DELL"
```