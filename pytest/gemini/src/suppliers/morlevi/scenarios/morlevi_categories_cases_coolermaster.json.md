```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def morlevi_categories_data():
    """Loads the morlevi categories JSON data from the provided string."""
    json_data = """
    {
      "scenarios": {
        "COOLERMASTER MID TOWER": {
          "brand": "COOLER MASTER",
          "template": "",
          "url": "https://www.morlevi.co.il/Cat/285?p_315=74&p_124=540&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": {
            "template": { "cooler master": "MID TOWER" }
          }
        },
        "COOLERMASTER full tower": {
          "brand": "COOLER MASTER",
          "template": "",
          "url": "https://www.morlevi.co.il/Cat/285?p_315=74&p_124=541&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": {
            "template": { "cooler master": "FULL TOWER" }
          }
        },
        "COOLERMASTER mini tower": {
          "brand": "COOLER MASTER",
          "template": "",
          "url": "https://www.morlevi.co.il/Cat/285?p_315=74&p_124=542&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": {
            "template": { "cooler master": "MINI TOWER" }
          }
        },
        "COOLERMASTER gaming MID TOWER": {
          "brand": "COOLER MASTER",
          "template": "",
          "url": "https://www.morlevi.co.il/Cat/285?p_315=74&p_124=545&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": {
            "template": { "cooler master": "GAMING MID TOWER" }
          }
        },
        "COOLERMASTER gaming full tower": {
          "brand": "COOLER MASTER",
          "template": "",
          "url": "----------------------------COOLER MASTER gaming full TOWER--------------------------------",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": {
            "template": { "cooler master": "GAMING FULL TOWER" }
          }
        },
        "COOLERMASTER mini itx": {
          "brand": "COOLER MASTER",
          "template": "",
          "url": "https://www.morlevi.co.il/Cat/285?p_124=3527&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": {
            "template": { "cooler master": "MINI ITX" }
          }
        }
      }
    }
    """
    return json.loads(json_data)

# Test cases for the 'scenarios' data structure

def test_morlevi_categories_data_structure(morlevi_categories_data):
  """
    Checks the top level structure to verify existence of 'scenarios'
  """
  assert "scenarios" in morlevi_categories_data, "The top level key 'scenarios' does not exist"
  assert isinstance(morlevi_categories_data["scenarios"], dict), "The 'scenarios' should be a dictionary"


def test_scenario_keys_exist(morlevi_categories_data):
    """
    Checks if all scenarios have all necessary keys.
    """
    for scenario_name, scenario_data in morlevi_categories_data['scenarios'].items():
      assert 'brand' in scenario_data, f"Scenario '{scenario_name}' missing 'brand' key"
      assert 'template' in scenario_data, f"Scenario '{scenario_name}' missing 'template' key"
      assert 'url' in scenario_data, f"Scenario '{scenario_name}' missing 'url' key"
      assert 'checkbox' in scenario_data, f"Scenario '{scenario_name}' missing 'checkbox' key"
      assert 'active' in scenario_data, f"Scenario '{scenario_name}' missing 'active' key"
      assert 'condition' in scenario_data, f"Scenario '{scenario_name}' missing 'condition' key"
      assert 'presta_categories' in scenario_data, f"Scenario '{scenario_name}' missing 'presta_categories' key"

def test_scenario_data_types(morlevi_categories_data):
  """
    Checks if the values of the scenario keys have the expected data type
  """
  for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
    assert isinstance(scenario_data["brand"], str), f"Scenario '{scenario_name}' 'brand' must be a string"
    assert isinstance(scenario_data["template"], str), f"Scenario '{scenario_name}' 'template' must be a string"
    assert isinstance(scenario_data["url"], str), f"Scenario '{scenario_name}' 'url' must be a string"
    assert isinstance(scenario_data["checkbox"], bool), f"Scenario '{scenario_name}' 'checkbox' must be a boolean"
    assert isinstance(scenario_data["active"], bool), f"Scenario '{scenario_name}' 'active' must be a boolean"
    assert isinstance(scenario_data["condition"], str), f"Scenario '{scenario_name}' 'condition' must be a string"
    assert isinstance(scenario_data["presta_categories"], dict), f"Scenario '{scenario_name}' 'presta_categories' must be a dictionary"
    assert isinstance(scenario_data["presta_categories"]["template"], dict), f"Scenario '{scenario_name}' 'presta_categories.template' must be a dictionary"

def test_scenario_brand_values(morlevi_categories_data):
    """
    Checks if all 'brand' values are equal to "COOLER MASTER"
    """
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert scenario_data["brand"] == "COOLER MASTER", f"Scenario '{scenario_name}' brand should be 'COOLER MASTER' "

def test_scenario_checkbox_values(morlevi_categories_data):
    """
    Checks if all 'checkbox' values are equal to False
    """
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
      assert scenario_data['checkbox'] is False, f"Scenario '{scenario_name}' checkbox value should be False"

def test_scenario_active_values(morlevi_categories_data):
  """
    Checks if all 'active' values are equal to True
  """
  for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
    assert scenario_data["active"] is True, f"Scenario '{scenario_name}' active should be True"

def test_scenario_condition_values(morlevi_categories_data):
    """
    Checks if all 'condition' values are equal to "new"
    """
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
      assert scenario_data["condition"] == "new", f"Scenario '{scenario_name}' condition should be 'new'"

def test_scenario_presta_categories_template_values(morlevi_categories_data):
  """
  Checks the correct structure and values of the 'presta_categories.template'
  """
  for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
      presta_template = scenario_data["presta_categories"]["template"]
      assert len(presta_template) == 1, f"Scenario '{scenario_name}' 'presta_categories.template' should have one key"
      assert "cooler master" in presta_template, f"Scenario '{scenario_name}' 'presta_categories.template' must have the key 'cooler master'"
      assert isinstance(presta_template["cooler master"], str), f"Scenario '{scenario_name}' 'presta_categories.template.cooler master' value must be a string"


def test_scenario_url_not_empty(morlevi_categories_data):
  """
    Checks if the url is not empty for all scenarios
  """
  for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
    assert len(scenario_data["url"]) > 0, f"Scenario '{scenario_name}' url should not be empty"


def test_scenario_url_is_string(morlevi_categories_data):
    """
    Checks if url value is a string for all scenarios
    """
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert isinstance(scenario_data["url"], str), f"Scenario '{scenario_name}' url should be a string"

def test_scenario_template_is_string(morlevi_categories_data):
    """
    Checks if the template value is a string for all scenarios
    """
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert isinstance(scenario_data["template"], str), f"Scenario '{scenario_name}' template should be a string"


def test_scenario_template_empty(morlevi_categories_data):
    """
    Checks if all 'template' values are empty string
    """
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        assert scenario_data["template"] == "", f"Scenario '{scenario_name}' template should be an empty string"

def test_scenario_values_are_not_none(morlevi_categories_data):
    """
    Checks if values are not None for all scenarios
    """
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
        for value in scenario_data.values():
           assert value is not None, f"Scenario '{scenario_name}' should not have None value"
        for value in scenario_data["presta_categories"].values():
            assert value is not None, f"Scenario '{scenario_name}' presta_categories should not have None value"
```