```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def cdata_categories_data():
    """Loads the JSON data for testing."""
    json_data = """
    {
      "scenarios": {
        "DELL GAMING 14 I5": {
          "brand": "DELL",
          "url": "------------------------------DELL GAMING 14 I5--------------------------------",
          "checkbox": false,
          "active": true,
          "condition":"new",
           "presta_categories": "3,49,50,23,93,10,5"
        },
        "DELL GAMING 14 I7": {
          "brand": "DELL",
          "url": "-------------------------DELL GAMING 14 I7--------------------------------------",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": "3,49,50,23,93,10,6"
        },
        "DELL GAMING 14 I9": {
          "brand": "DELL",
          "url": "--------------------------DELL GAMING 14 I9------------------------------------",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": "3,49,50,23,93,10,7"
        },
        "DELL GAMING 14 AMD": {
          "brand": "DELL",
          "url": "----------------------------DELL GAMING 14 AMD----------------------------------",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": "3,49,50,23,93,10,234"
        },
        "DELL GAMING 15 I5": {
          "brand": "DELL",
          "url": "--------------------------------DELL GAMING 15 I5------------------------------",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": "3,49,50,23,96,11,5"
        },
        "DELL GAMING 15 I7": {
          "brand": "DELL",
          "url": "https://reseller.c-data.co.il/%D7%A0%D7%99%D7%99%D7%93%D7%99-gaming#/specFilters=227!#-!4635!-#!225m!#-!4663&manFilters=4",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": "3,49,50,23,96,11,6"
        },
        "DELL GAMING 15 I9": {
          "brand": "DELL",
          "url": "--------------------------DELL GAMING 15 I9------------------------------------",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": "3,49,50,23,96,11,7"
        },
        "DELL GAMING 15 AMD": {
          "brand": "DELL",
          "url": "-----------------------------DELL GAMING 15 AMD---------------------------------",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": "3,49,50,23,96,11,234"
        },
        "DELL GAMING 17 I5": {
          "brand": "DELL",
          "url": "---------------------------------DELL GAMING 17 I5-----------------------------",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": "3,49,50,23,97,12,5"
        },
        "DELL GAMING 17 I7": {
          "brand": "DELL",
          "url": "-------------------------------DELL GAMING 17 I7--------------------------------",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": "3,49,50,23,97,12,6"
        },
        "DELL GAMING 17 I9": {
          "brand": "DELL",
          "url": "---------------------------DELL GAMING 17 I9----------------------------------",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": "3,49,50,23,97,12,7"
        },
        "DELL GAMING 17 AMD": {
          "brand": "DELL",
          "url": "------------------------------------DELL GAMING 17 AMD--------------------------",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": "3,49,50,23,97,12,234"
        }
      }
    }
    """
    return json.loads(json_data)

def test_cdata_categories_data_structure(cdata_categories_data):
    """
    Checks if the loaded data has the expected structure.
    """
    assert "scenarios" in cdata_categories_data
    assert isinstance(cdata_categories_data["scenarios"], dict)
    assert len(cdata_categories_data["scenarios"]) == 12


def test_cdata_categories_data_content(cdata_categories_data):
    """
    Checks if a specific scenario has the expected values.
    """
    scenario = cdata_categories_data["scenarios"].get("DELL GAMING 15 I7")
    assert scenario is not None
    assert scenario["brand"] == "DELL"
    assert scenario["url"] == "https://reseller.c-data.co.il/%D7%A0%D7%99%D7%99%D7%93%D7%99-gaming#/specFilters=227!#-!4635!-#!225m!#-!4663&manFilters=4"
    assert scenario["checkbox"] is False
    assert scenario["active"] is True
    assert scenario["condition"] == "new"
    assert scenario["presta_categories"] == "3,49,50,23,96,11,6"

def test_cdata_categories_all_scenarios_present(cdata_categories_data):
  """
  Checks if all expected scenarios are present in the data.
  """
  expected_scenarios = [
    "DELL GAMING 14 I5",
    "DELL GAMING 14 I7",
    "DELL GAMING 14 I9",
    "DELL GAMING 14 AMD",
    "DELL GAMING 15 I5",
    "DELL GAMING 15 I7",
    "DELL GAMING 15 I9",
    "DELL GAMING 15 AMD",
    "DELL GAMING 17 I5",
    "DELL GAMING 17 I7",
    "DELL GAMING 17 I9",
    "DELL GAMING 17 AMD",
    ]
  
  for scenario_name in expected_scenarios:
    assert scenario_name in cdata_categories_data["scenarios"]

def test_cdata_categories_all_fields_present(cdata_categories_data):
    """
    Checks if all required fields are present in all scenarios.
    """
    required_fields = ["brand", "url", "checkbox", "active", "condition", "presta_categories"]
    for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
        for field in required_fields:
            assert field in scenario_data, f"Field '{field}' missing in scenario '{scenario_name}'"

def test_cdata_categories_valid_data_types(cdata_categories_data):
    """
    Checks if data types for specific fields are correct.
    """
    for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
        assert isinstance(scenario_data["brand"], str), f"'brand' should be string in scenario '{scenario_name}'"
        assert isinstance(scenario_data["url"], str), f"'url' should be string in scenario '{scenario_name}'"
        assert isinstance(scenario_data["checkbox"], bool), f"'checkbox' should be boolean in scenario '{scenario_name}'"
        assert isinstance(scenario_data["active"], bool), f"'active' should be boolean in scenario '{scenario_name}'"
        assert isinstance(scenario_data["condition"], str), f"'condition' should be string in scenario '{scenario_name}'"
        assert isinstance(scenario_data["presta_categories"], str), f"'presta_categories' should be string in scenario '{scenario_name}'"


def test_cdata_categories_checkbox_value(cdata_categories_data):
    """
    Checks if the 'checkbox' field is consistently false for all scenarios.
    """
    for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
        assert scenario_data["checkbox"] is False, f"'checkbox' should be False in scenario '{scenario_name}'"

def test_cdata_categories_active_value(cdata_categories_data):
    """
    Checks if the 'active' field is consistently True for all scenarios.
    """
    for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
        assert scenario_data["active"] is True, f"'active' should be True in scenario '{scenario_name}'"

def test_cdata_categories_condition_value(cdata_categories_data):
    """
    Checks if the 'condition' field is consistently 'new' for all scenarios.
    """
    for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
        assert scenario_data["condition"] == "new", f"'condition' should be 'new' in scenario '{scenario_name}'"

def test_cdata_categories_presta_categories_is_string(cdata_categories_data):
    """
    Checks if the 'presta_categories' field is a string for all scenarios.
    """
    for scenario_name, scenario_data in cdata_categories_data["scenarios"].items():
        assert isinstance(scenario_data["presta_categories"], str), f"'presta_categories' should be a string in scenario '{scenario_name}'"
```