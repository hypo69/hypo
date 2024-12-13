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
        "GIGABYTE MINIPC I3 8-9th GEN": {
          "brand": "GIGABYTE",
          "url": "https://www.morlevi.co.il/Cat/127?p_315=2&p_189=1895&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": "159,160"
        },
        "GIGABYTE MINIPC I3 10th GEN": {
          "brand": "GIGABYTE",
          "url": "https://www.morlevi.co.il/Cat/127?p_315=2&p_189=3447&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": "159,160"
        },
        "GIGABYTE MINIPC I5 8-9th": {
          "brand": "GIGABYTE",
          "url": "--------------------------GIGABYTE MINIPC I5 8-9th-------------------------",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": "159,161"
        },
        "GIGABYTE MINIPC I5 10th": {
          "brand": "GIGABYTE",
          "url": "https://www.morlevi.co.il/Cat/127?p_315=2&p_189=3500&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": "159,161"
        },
        "GIGABYTE  MINIPC I7": {
          "brand": "GIGABYTE",
          "url": "https://www.morlevi.co.il/Cat/127?p_315=2&p_189=3501&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": "159,162"
        },
        "GIGABYTE  MINIPC I9": {
          "brand": "GIGABYTE",
          "url": "-------------GIGABYTE  MINIPC I9---------------- ",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": "159,530"
        },
        "GIGABYTE MINIPC AMD": {
          "brand": "GIGABYTE",
          "url": "-------------GIGABYTE MINIPC AMD---------------- ",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": "159,531"
        },
        "GIGABYTE MINIPC Celeron": {
          "brand": "GIGABYTE",
          "url": "https://www.morlevi.co.il/Cat/127?p_315=2&p_189=3371&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": "159,532"
        },
        "GIGABYTE MINIPC Celeron 2": {
          "brand": "GIGABYTE",
          "url": "https://www.morlevi.co.il/Cat/127?p_315=2&p_189=3133&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": "159,532"
        },
        "GIGABYTE MINIPC Pentium": {
          "brand": "GIGABYTE",
          "url": "https://www.morlevi.co.il/Cat/127?p_315=2&p_189=3133&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": "159,532"
        }
      }
    }
    """
    return json.loads(json_data)

def test_morlevi_categories_data_structure(morlevi_categories_data):
    """
    Test the basic structure of the loaded JSON data.
    It checks if the top level key 'scenarios' exists and is a dictionary.
    """
    assert "scenarios" in morlevi_categories_data
    assert isinstance(morlevi_categories_data["scenarios"], dict)


def test_scenario_keys(morlevi_categories_data):
    """
    Tests if each scenario within the 'scenarios' dictionary
    contains the expected keys ('brand', 'url', 'checkbox', 'active', 'condition', 'presta_categories').
    """
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert "brand" in scenario_data
        assert "url" in scenario_data
        assert "checkbox" in scenario_data
        assert "active" in scenario_data
        assert "condition" in scenario_data
        assert "presta_categories" in scenario_data

def test_scenario_values_types(morlevi_categories_data):
    """
    Tests the data types of the values within each scenario.
     Checks if 'brand' and 'url' are strings, 'checkbox' and 'active' are booleans,
    'condition' is string and 'presta_categories' is a string.
    """
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert isinstance(scenario_data["brand"], str)
        assert isinstance(scenario_data["url"], str)
        assert isinstance(scenario_data["checkbox"], bool)
        assert isinstance(scenario_data["active"], bool)
        assert isinstance(scenario_data["condition"], str)
        assert isinstance(scenario_data["presta_categories"], str)


def test_url_value_types(morlevi_categories_data):
    """
    Tests that the 'url' value of each scenario is always a string.
     It verifies that each url is a string and not None or empty string
    """
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert isinstance(scenario_data["url"], str)
        assert scenario_data["url"] != ""

def test_presta_categories_not_empty(morlevi_categories_data):
    """
    Tests that the 'presta_categories' value of each scenario is not empty.
    It verifies that each 'presta_categories' is a string and not None or empty string
    """
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert isinstance(scenario_data["presta_categories"], str)
        assert scenario_data["presta_categories"] != ""

def test_active_is_boolean(morlevi_categories_data):
    """
        Tests that the 'active' value of each scenario is a boolean
        It verifies that each 'active' is a boolean
    """
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert isinstance(scenario_data["active"],bool)

def test_condition_is_new(morlevi_categories_data):
    """
        Tests that the 'condition' value of each scenario is a new
         It verifies that each 'condition' is a string and equal to new
    """
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert isinstance(scenario_data["condition"], str)
        assert scenario_data["condition"] =="new"


def test_checkbox_is_false(morlevi_categories_data):
    """
        Tests that the 'checkbox' value of each scenario is a false
        It verifies that each 'checkbox' is a boolean and equal to false
    """
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert isinstance(scenario_data["checkbox"],bool)
        assert scenario_data["checkbox"] == False
```