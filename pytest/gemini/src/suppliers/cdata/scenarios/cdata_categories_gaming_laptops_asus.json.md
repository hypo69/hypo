```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def cdata_categories_data():
    """Loads the JSON data from the provided string."""
    json_data = """
{
  "scenarios": {
    "ASUS GAMING 14 I5": {
      "brand": "ASUS",
      "url": "-----------------------------------ASUS GAMING 14 I5----------------------------",
      "checkbox": false,
      "active": true,
      "condition":"new",
      "presta_categories": "3,49,50,48,98,10,5,434"
    },
    "ASUS GAMING 14 I7": {
      "brand": "ASUS",
      "url": "-----------------------------------ASUS GAMING 14 I7----------------------------",
      "checkbox": false,
      "active": true,
      "condition":"new",
      "presta_categories": "3,49,50,48,98,10,6,435"
    },
    "ASUS GAMING 14 I9": {
      "brand": "ASUS",
      "url": "------------------------------------ASUS GAMING 14 I9--------------------------",
      "checkbox": false,
      "active": true,
      "condition":"new",
      "presta_categories": "3,49,50,48,98,10,7,436"
    },
    "ASUS GAMING 14 AMD": {
      "brand": "ASUS",
      "url": "https://reseller.c-data.co.il/%D7%A0%D7%99%D7%99%D7%93%D7%99-gaming#/specFilters=227m!#-!4920!-#!225!#-!4662&manFilters=10",
      "checkbox": false,
      "active": true,
       "condition":"new",
      "presta_categories": "3,49,50,48,98,10,234,437"
    },
    "ASUS GAMING 15 I5": {
      "brand": "ASUS",
      "url": "------------------------------------ASUS GAMING 15 I5 --------------------------4",
      "checkbox": false,
      "active": true,
       "condition":"new",
      "presta_categories": "3,49,50,48,99,11,5,441"
    },
    "ASUS GAMING 15 I7": {
      "brand": "ASUS",
      "url": "https://reseller.c-data.co.il/%D7%A0%D7%99%D7%99%D7%93%D7%99-gaming#/specFilters=227!#-!4635!-#!225m!#-!4663&manFilters=10",
      "checkbox": false,
      "active": true,
       "condition":"new",
      "presta_categories": "3,49,50,48,99,11,6,442"
    },
    "ASUS GAMING 15 I9": {
      "brand": "ASUS",
      "url": "https://reseller.c-data.co.il/%D7%A0%D7%99%D7%99%D7%93%D7%99-gaming#/specFilters=227m!#-!5836!-#!225!#-!4663&manFilters=10",
      "checkbox": false,
      "active": true,
       "condition":"new",
      "presta_categories": "3,49,50,48,99,11,7,443"
    },
    "ASUS GAMING 15 AMD": {
      "brand": "ASUS",
      "url": "https://reseller.c-data.co.il/%D7%A0%D7%99%D7%99%D7%93%D7%99-gaming#/specFilters=227m!#-!4920!-#!225!#-!4663&manFilters=10",
      "checkbox": false,
      "active": true,
       "condition":"new",
      "presta_categories": "3,49,50,48,99,11,234,444"
    },
    "ASUS GAMING 17 I5": {
      "brand": "ASUS",
      "url": "----------------------------------ASUS GAMING 17 I5----------------------------",
      "checkbox": false,
      "active": true,
      "condition":"new",
      "presta_categories": "3,49,50,48,99,12,5,448"
    },
    "ASUS GAMING 17 I7": {
      "brand": "ASUS",
      "url": "https://reseller.c-data.co.il/%D7%A0%D7%99%D7%99%D7%93%D7%99-gaming#/specFilters=227m!#-!4635!-#!225!#-!4664&manFilters=10",
      "checkbox": false,
      "active": true,
      "condition":"new",
      "presta_categories": "3,49,50,48,100,12,6,449"
    },
    "ASUS GAMING 17 I9": {
      "brand": "ASUS",
      "url": "----------------------------------ASUS GAMING 17 I9----------------------------",
      "checkbox": false,
      "active": true,
       "condition":"new",
      "presta_categories": "3,49,50,48,100,12,7,450"
    },
    "ASUS GAMING 17 AMD": {
      "brand": "ASUS",
      "url": "-------------------------------------ASUS GAMING 17 AMD-------------------------",
      "checkbox": false,
      "active": true,
       "condition":"new",
      "presta_categories": "3,49,50,48,100,12,234,451"
    }
  }
}
"""
    return json.loads(json_data)


def test_cdata_categories_data_load(cdata_categories_data):
    """
    Test that the fixture loads the data correctly.
    """
    assert isinstance(cdata_categories_data, dict)
    assert "scenarios" in cdata_categories_data
    assert isinstance(cdata_categories_data["scenarios"], dict)
    assert len(cdata_categories_data["scenarios"]) == 12


def test_scenario_has_required_fields(cdata_categories_data):
    """
    Test that each scenario has the required fields.
    """
    for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
        assert "brand" in scenario_data
        assert "url" in scenario_data
        assert "checkbox" in scenario_data
        assert "active" in scenario_data
        assert "condition" in scenario_data
        assert "presta_categories" in scenario_data


def test_scenario_brand_is_asus(cdata_categories_data):
    """
    Test that the 'brand' field is always 'ASUS'.
    """
    for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
        assert scenario_data["brand"] == "ASUS"


def test_scenario_checkbox_is_false(cdata_categories_data):
    """
    Test that the 'checkbox' field is always False.
    """
    for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
        assert scenario_data["checkbox"] is False

def test_scenario_active_is_true(cdata_categories_data):
    """
    Test that the 'active' field is always True.
    """
    for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
        assert scenario_data["active"] is True


def test_scenario_condition_is_new(cdata_categories_data):
    """
    Test that the 'condition' field is always 'new'.
    """
    for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
        assert scenario_data["condition"] == "new"

def test_scenario_presta_categories_is_string(cdata_categories_data):
     """
     Test that the 'presta_categories' field is always a string.
     """
     for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
         assert isinstance(scenario_data["presta_categories"], str)


def test_scenario_presta_categories_not_empty(cdata_categories_data):
    """
    Test that the 'presta_categories' field is not empty.
    """
    for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
         assert len(scenario_data["presta_categories"]) > 0


def test_scenario_url_is_string(cdata_categories_data):
     """
     Test that the 'url' field is always a string.
     """
     for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
         assert isinstance(scenario_data["url"], str)

def test_scenario_url_not_empty(cdata_categories_data):
    """
    Test that the 'url' field is not empty.
    """
    for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
         assert len(scenario_data["url"]) > 0

def test_scenario_names_are_strings(cdata_categories_data):
    """
    Test that scenario names are strings and not empty
    """
    for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
        assert isinstance(scenario_name, str)
        assert len(scenario_name) > 0
```