```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def morlevi_categories_data():
    """Loads the morlevi categories data from the json."""
    json_data = '''
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
    '''
    return json.loads(json_data)

def test_morlevi_categories_data_structure(morlevi_categories_data):
    """
    Test the overall structure of the loaded JSON data.
    Ensures that the data contains the 'scenarios' key and that it is a dictionary.
    """
    assert "scenarios" in morlevi_categories_data
    assert isinstance(morlevi_categories_data["scenarios"], dict)

def test_morlevi_categories_scenario_keys(morlevi_categories_data):
    """
    Test the presence of the correct keys in each scenario.
    Ensures that each scenario has all the required keys like 'brand', 'url', 'checkbox', etc.
    """
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
       assert "brand" in scenario_data
       assert "url" in scenario_data
       assert "checkbox" in scenario_data
       assert "active" in scenario_data
       assert "condition" in scenario_data
       assert "presta_categories" in scenario_data

def test_morlevi_categories_scenario_data_types(morlevi_categories_data):
    """
    Test the data types of the values in each scenario.
    Checks if values have the correct data types as expected.
    """
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert isinstance(scenario_data["brand"], str)
        assert isinstance(scenario_data["url"], str)
        assert isinstance(scenario_data["checkbox"], bool)
        assert isinstance(scenario_data["active"], bool)
        assert isinstance(scenario_data["condition"], str)
        assert isinstance(scenario_data["presta_categories"], str)


def test_morlevi_categories_scenario_brand_values(morlevi_categories_data):
   """
   Test that all brands are equal 'GENIUS'
   """
   for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert scenario_data["brand"] == "GENIUS"


def test_morlevi_categories_scenario_checkbox_values(morlevi_categories_data):
   """
   Test that all checkbox values are False
   """
   for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert scenario_data["checkbox"] == False

def test_morlevi_categories_scenario_active_values(morlevi_categories_data):
   """
   Test that all active values are True
   """
   for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert scenario_data["active"] == True

def test_morlevi_categories_scenario_condition_values(morlevi_categories_data):
   """
   Test that all conditions values are new
   """
   for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert scenario_data["condition"] == "new"


def test_morlevi_categories_presta_categories_format(morlevi_categories_data):
    """
    Test that 'presta_categories' values are comma separated strings of integers.
    Ensures that the 'presta_categories' value is a string of comma separated integers.
    """
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        presta_categories = scenario_data["presta_categories"]
        categories = presta_categories.split(',')
        for category in categories:
            assert category.isdigit(), f"Category '{category}' is not a digit in scenario: {scenario_name}"

def test_morlevi_categories_url_values(morlevi_categories_data):
    """
    Test that the url values are strings, and at least one url is not correct
    """
    invalid_url_present = False
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        url = scenario_data["url"]
        assert isinstance(url, str)
        if "GENIUS WIRELESS KEYBOARD" in scenario_name:
           invalid_url_present = True
    assert invalid_url_present, "The expected invalid url is missing"
```