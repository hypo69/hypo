```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def morlevi_categories_data():
    """Loads the morlevi_categories_monitors_gigabyte.json data."""
    
    json_data =  '''{
        "scenarios": {
            "GIGABYTE 22": {
            "brand": "GIGABYTE",
            "url": "----------------------------------GIGABYTE 22---------------------------------------",
            "checkbox": false,
            "active": true,
            "condition":"new","presta_categories": "127,128,980"
            },
            "GIGABYTE 24-25": {
            "brand": "GIGABYTE",
            "url": "https://www.morlevi.co.il/Cat/8?p_315=2&p_350=1807&sort=datafloat2%2Cprice&keyword=",
            "checkbox": false,
            "active": true,
            "condition":"new","presta_categories": "127,129,980"
            
            },
            "GIGABYTE 27-29": {
            "brand": "GIGABYTE",
            "url": "https://www.morlevi.co.il/Cat/8?p_315=2&p_350=1808&sort=datafloat2%2Cprice&keyword=",
            "checkbox": false,
            "active": true,
            "condition":"new","presta_categories": "127,130,980"
            },
            "GIGABYTE 32": {
            "brand": "GIGABYTE",
            "url": "https://www.morlevi.co.il/Cat/8?p_315=2&p_350=1809&sort=datafloat2%2Cprice&keyword=",
            "checkbox": false,
            "active": true,
            "condition":"new","presta_categories": "127,131,980"
            },
            "GIGABYTE 34": {
            "brand": "GIGABYTE",
            "url": "https://www.morlevi.co.il/Cat/8?p_315=2&p_350=1810&sort=datafloat2%2Cprice&keyword=",
            "checkbox": false,
            "active": true,
            "condition":"new","presta_categories": "127,132,980"
            },
            "GIGABYTE 49": {
            "brand": "GIGABYTE",
            "url": "-----------------------------  GIGABYTE 49 ---------------------------------",
            "checkbox": false,
            "active": true,
            "condition":"new","presta_categories": "127,133,980"
            }
        }
    }
    '''
    return json.loads(json_data)

def test_scenarios_structure(morlevi_categories_data):
    """
    Test that the 'scenarios' key exists and is a dictionary.
    """
    assert "scenarios" in morlevi_categories_data
    assert isinstance(morlevi_categories_data["scenarios"], dict)

def test_scenario_keys(morlevi_categories_data):
    """
    Test that each scenario within 'scenarios' has the required keys
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
    Test that values in each scenario are of the correct type
    """
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert isinstance(scenario_data["brand"], str)
        assert isinstance(scenario_data["url"], str)
        assert isinstance(scenario_data["checkbox"], bool)
        assert isinstance(scenario_data["active"], bool)
        assert isinstance(scenario_data["condition"], str)
        assert isinstance(scenario_data["presta_categories"], str)


def test_scenario_checkbox_values(morlevi_categories_data):
    """
    Test that checkbox values are only booleans and false
    """
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert scenario_data["checkbox"] == False, "Checkbox should be False"

def test_scenario_active_values(morlevi_categories_data):
    """
    Test that active values are only booleans and true
    """
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert scenario_data["active"] == True, "active should be True"

def test_scenario_presta_categories_format(morlevi_categories_data):
    """
    Test that presta_categories is a string with comma-separated numeric values.
    """
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        categories = scenario_data["presta_categories"].split(",")
        for cat in categories:
            assert cat.isdigit(), f"presta_categories should be comma-separated numbers. Invalid category: {cat} in scenario: {scenario_name}"


def test_scenario_url_not_empty(morlevi_categories_data):
        """
        Test that the url is not empty string.
        """
        for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
            assert len(scenario_data["url"].strip()) > 0 , "URL should not be empty"


def test_scenario_condition_is_new(morlevi_categories_data):
    """
    Test that the condition is always "new".
    """
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert scenario_data["condition"] == "new" , "condition should be new"
```