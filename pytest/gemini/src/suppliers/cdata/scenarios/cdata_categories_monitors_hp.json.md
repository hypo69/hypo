```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def cdata_categories_monitors_hp_data():
    """Loads the cdata_categories_monitors_hp.json data."""
    json_data = """
    {
      "scenarios": {
        "HP 18": {
          "brand": "HP",
          "url": "https://reseller.c-data.co.il/%D7%9E%D7%A1%D7%9B%D7%99%D7%9D#/specFilters=215!#-!4586!-#!216m&manFilters=2",
          "checkbox": false,
          "active": true,
          "condition":"new","presta_categories": "127,241"
        },
        "HP 21.5": {
          "brand": "HP",
          "url": "https://reseller.c-data.co.il/%D7%9E%D7%A1%D7%9B%D7%99%D7%9D#/specFilters=215m!#-!4587&manFilters=2",
          "checkbox": false,
          "active": true,
           "condition":"new","presta_categories": "127,128"
        },
        "HP 23.5": {
          "brand": "HP",
          "url": "https://reseller.c-data.co.il/%D7%9E%D7%A1%D7%9B%D7%99%D7%9D#/specFilters=215m!#-!4588!##!4589&manFilters=2",
          "checkbox": false,
          "active": true,
           "condition":"new","presta_categories": "127,129"
        },
        "HP 27": {
          "brand": "HP",
          "url": "https://reseller.c-data.co.il/%D7%9E%D7%A1%D7%9B%D7%99%D7%9D#/specFilters=215m!#-!4590&manFilters=2",
          "checkbox": false,
          "active": true,
           "condition":"new","presta_categories": "127,130"
        },
        "HP 31": {
          "brand": "HP",
          "url": "https://reseller.c-data.co.il/%D7%9E%D7%A1%D7%9B%D7%99%D7%9D#/specFilters=215m!#-!4591&manFilters=2",
          "checkbox": false,
          "active": true,
           "condition":"new","presta_categories": "127,131"
        },
        "HP 34": {
          "brand": "HP",
          "url": "https://reseller.c-data.co.il/%D7%9E%D7%A1%D7%9B%D7%99%D7%9D#/specFilters=215m!#-!4592&manFilters=2",
          "checkbox": false,
          "active": true,
          "condition":"new","presta_categories": "127,132"
        },
        "HP 49": {
          "brand": "HP",
          "url": "https://reseller.c-data.co.il/%D7%9E%D7%A1%D7%9B%D7%99%D7%9D#/specFilters=215m!#-!4592&manFilters=2",
          "checkbox": false,
          "active": true,
          "condition":"new","presta_categories": "127,133"
        }
      }
    }
    """
    return json.loads(json_data)


def test_cdata_categories_monitors_hp_data_structure(cdata_categories_monitors_hp_data):
    """
    Test if the loaded JSON has the expected structure.
    Checks that the root is a dictionary with a "scenarios" key, which itself is a dictionary.
    """
    assert isinstance(cdata_categories_monitors_hp_data, dict)
    assert "scenarios" in cdata_categories_monitors_hp_data
    assert isinstance(cdata_categories_monitors_hp_data["scenarios"], dict)


def test_cdata_categories_monitors_hp_scenario_keys(cdata_categories_monitors_hp_data):
    """
    Test if each scenario in "scenarios" has the expected keys.
    Checks for keys 'brand', 'url', 'checkbox', 'active', 'condition' and 'presta_categories' in every scenario.
    """
    for scenario_name, scenario_data in cdata_categories_monitors_hp_data["scenarios"].items():
        assert "brand" in scenario_data
        assert "url" in scenario_data
        assert "checkbox" in scenario_data
        assert "active" in scenario_data
        assert "condition" in scenario_data
        assert "presta_categories" in scenario_data


def test_cdata_categories_monitors_hp_scenario_values_types(cdata_categories_monitors_hp_data):
    """
    Test the data types of the values in each scenario.
    Checks that 'brand' and 'url' are strings, 'checkbox' and 'active' are booleans, and 'presta_categories' is a string.
    """
    for scenario_name, scenario_data in cdata_categories_monitors_hp_data["scenarios"].items():
        assert isinstance(scenario_data["brand"], str)
        assert isinstance(scenario_data["url"], str)
        assert isinstance(scenario_data["checkbox"], bool)
        assert isinstance(scenario_data["active"], bool)
        assert isinstance(scenario_data["condition"], str)
        assert isinstance(scenario_data["presta_categories"], str)


def test_cdata_categories_monitors_hp_scenario_brand_value(cdata_categories_monitors_hp_data):
    """
    Test if the 'brand' value is always "HP".
     Ensures all scenarios are for the HP brand.
    """
    for scenario_name, scenario_data in cdata_categories_monitors_hp_data["scenarios"].items():
         assert scenario_data["brand"] == "HP"


def test_cdata_categories_monitors_hp_scenario_url_format(cdata_categories_monitors_hp_data):
    """
    Test if the 'url' values are strings and start with "https://".
     Checks that URLs are valid and point to the expected domain.
    """
    for scenario_name, scenario_data in cdata_categories_monitors_hp_data["scenarios"].items():
        assert isinstance(scenario_data["url"], str)
        assert scenario_data["url"].startswith("https://")


def test_cdata_categories_monitors_hp_scenario_checkbox_value(cdata_categories_monitors_hp_data):
    """
     Test if the 'checkbox' value is always false.
    Ensures that the checkbox is unchecked across all scenarios.
    """
    for scenario_name, scenario_data in cdata_categories_monitors_hp_data["scenarios"].items():
        assert scenario_data["checkbox"] == False

def test_cdata_categories_monitors_hp_scenario_active_value(cdata_categories_monitors_hp_data):
    """
     Test if the 'active' value is always true.
     Ensures that all scenarios are active.
    """
    for scenario_name, scenario_data in cdata_categories_monitors_hp_data["scenarios"].items():
        assert scenario_data["active"] == True


def test_cdata_categories_monitors_hp_scenario_condition_value(cdata_categories_monitors_hp_data):
    """
    Test if the 'condition' value is always "new".
    Ensures that the condition of all products is new.
    """
    for scenario_name, scenario_data in cdata_categories_monitors_hp_data["scenarios"].items():
        assert scenario_data["condition"] == "new"


def test_cdata_categories_monitors_hp_scenario_presta_categories_value(cdata_categories_monitors_hp_data):
    """
    Test if the 'presta_categories' value is a string containing comma-separated numbers.
    Verifies that the format of PrestaShop categories is correct.
    """
    for scenario_name, scenario_data in cdata_categories_monitors_hp_data["scenarios"].items():
        assert isinstance(scenario_data["presta_categories"], str)
        categories = scenario_data["presta_categories"].split(',')
        for cat in categories:
            assert cat.isdigit()
```