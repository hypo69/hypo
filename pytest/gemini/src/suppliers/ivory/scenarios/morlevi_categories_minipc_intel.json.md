```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def morlevi_categories_data():
    """Provides the JSON data for tests."""
    json_data = """
    {
      "scenarios": {
        "INTEL MINIPC I3 8-9th GEN": {
          "brand": "INTEL",
          "url": "https://www.morlevi.co.il/Cat/127?p_315=3&p_189=3339&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
          "condition":"new","presta_categories": "159,160"
        },
        "INTEL MINIPC I3 10th GEN": {
          "brand": "INTEL",
          "url": "https://www.morlevi.co.il/Cat/127?p_315=3&p_189=3498&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
          "condition":"new","presta_categories": "159,160"
        },
    
        "INTEL MINIPC I5 8-9th": {
          "brand": "INTEL",
          "url": "https://www.morlevi.co.il/Cat/127?p_315=3&p_189=3391&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
          "condition":"new","presta_categories": "159,161"
        },
        "INTEL MINIPC I5 10th": {
          "brand": "INTEL",
          "url": "https://www.morlevi.co.il/Cat/127?p_315=3&p_189=3500&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
          "condition":"new","presta_categories": "159,161"
        },
        "INTEL  MINIPC I7": {
          "brand": "INTEL",
          "url": "https://www.morlevi.co.il/Cat/127?p_315=3&p_189=3501&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
          "condition":"new","presta_categories": "159,162"
        },
        "INTEL  MINIPC I9": {
          "brand": "INTEL",
          "url": "-------------INTEL  MINIPC I9---------------- ",
          "checkbox": false,
          "active": true,
          "condition":"new","presta_categories": "159,530"
        },
        "INTEL MINIPC AMD": {
          "brand": "INTEL",
          "url": "-------------INTEL MINIPC AMD---------------- ",
          "checkbox": false,
          "active": true,
          "condition":"new","presta_categories": "159,531"
        },
        "INTEL MINIPC Celeron": {
          "brand": "INTEL",
          "url": "-------------INTEL MINIPC Celeron---------------- ",
          "checkbox": false,
          "active": true,
          "condition":"new","presta_categories": "159,532"
        }
      }
    }
    """
    return json.loads(json_data)


def test_morlevi_categories_data_structure(morlevi_categories_data):
    """
    Test that the structure of the loaded JSON data is correct.
    Checks if the 'scenarios' key exists and is a dictionary.
    """
    assert "scenarios" in morlevi_categories_data
    assert isinstance(morlevi_categories_data["scenarios"], dict)


def test_morlevi_categories_scenario_keys(morlevi_categories_data):
    """
    Test that each scenario in the 'scenarios' dictionary has the expected keys.
    Checks for the existence of 'brand', 'url', 'checkbox', 'active', 'condition', and 'presta_categories' keys in each scenario.
    """
    for scenario_name, scenario_data in morlevi_categories_data["scenarios"].items():
      assert "brand" in scenario_data
      assert "url" in scenario_data
      assert "checkbox" in scenario_data
      assert "active" in scenario_data
      assert "condition" in scenario_data
      assert "presta_categories" in scenario_data


def test_morlevi_categories_scenario_values_types(morlevi_categories_data):
    """
    Test that the data types of values for each scenario are correct.
    Checks the data types for 'brand'(str),'url'(str), 'checkbox'(bool), 'active'(bool), 'condition'(str) and 'presta_categories'(str)
    """
    for _, scenario_data in morlevi_categories_data["scenarios"].items():
      assert isinstance(scenario_data["brand"], str)
      assert isinstance(scenario_data["url"], str)
      assert isinstance(scenario_data["checkbox"], bool)
      assert isinstance(scenario_data["active"], bool)
      assert isinstance(scenario_data["condition"], str)
      assert isinstance(scenario_data["presta_categories"], str)

def test_morlevi_categories_active_values(morlevi_categories_data):
    """
    Test that the 'active' value is always True.
    Checks that all scenarios have the key `active` set to `True`.
    """
    for _, scenario_data in morlevi_categories_data["scenarios"].items():
        assert scenario_data["active"] is True


def test_morlevi_categories_checkbox_values(morlevi_categories_data):
    """
     Test that the 'checkbox' value is always False.
    Checks that all scenarios have the key `checkbox` set to `False`.
    """
    for _, scenario_data in morlevi_categories_data["scenarios"].items():
      assert scenario_data["checkbox"] is False

def test_morlevi_categories_condition_values(morlevi_categories_data):
  """
    Test that the 'condition' value is always 'new'.
    Checks that all scenarios have the key `condition` set to 'new'.
    """
  for _, scenario_data in morlevi_categories_data["scenarios"].items():
    assert scenario_data["condition"] == 'new'


def test_morlevi_categories_presta_categories_valid_values(morlevi_categories_data):
    """
    Test that 'presta_categories' values are strings containing comma-separated integers.
    Checks that 'presta_categories' contain only integers separated by commas
    """
    for _, scenario_data in morlevi_categories_data["scenarios"].items():
      presta_categories = scenario_data["presta_categories"]
      categories_list = presta_categories.split(',')
      for category in categories_list:
        assert category.isdigit(), f"Invalid presta_categories value: {presta_categories}"

def test_morlevi_categories_url_not_empty(morlevi_categories_data):
    """
    Test that the 'url' values are not empty strings.
    Checks that all scenarios have a non-empty string for the 'url' key.
    """
    for _, scenario_data in morlevi_categories_data["scenarios"].items():
        assert scenario_data["url"] != "", "URL cannot be empty"
```