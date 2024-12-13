```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def visualdg_data():
    """Loads the visualdg data from the provided JSON string."""
    json_data = """
    {
      "scenarios": {
        "LENOVO YOGA 13.4 - 13.3 I3": {
          "brand": "LENOVO",
          "template": "YOGA",
          "url": "-----------------YOGA 13.4 - 13.3 I3-------------r ",
          "checkbox": false,
          "active": true,
          "condition":"new","presta_categories": "3,53,306,9,4,370,839"
        },
        "LENOVO YOGA 13.4 - 13.3 I5": {
          "brand": "LENOVO",
          "template": "YOGA",
          "url": "https://www.visualdg.co.il/172330--%D7%A0%D7%99%D7%99%D7%93%D7%99-ThinkPad-Yoga/253273/253294",
          "checkbox": false,
          "active": true,
           "condition":"new","presta_categories": "3,53,306,9,5,371,839"
        },
        "LENOVO YOGA 13.4 - 13.3 I7": {
          "brand": "LENOVO",
          "template": "YOGA",
          "url": "https://www.visualdg.co.il/172330--%D7%A0%D7%99%D7%99%D7%93%D7%99-ThinkPad-Yoga/253274/253294",
          "checkbox": false,
          "active": true,
           "condition":"new","presta_categories": "3,53,306,9,6,372,839"
        },
        "LENOVO YOGA 13.4 - 13.3 I9": {
          "brand": "LENOVO",
          "template": "YOGA",
          "url": "----------------LENOVO YOGA 13.4 - 13.3 I9------------- ",
          "checkbox": false,
          "active": true,
           "condition":"new","presta_categories": "3,53,306,9,7,373,839"
        },
        "LENOVO YOGA 13.4 - 13.3 AMD": {
          "brand": "LENOVO",
          "template": "YOGA",
          "url": "--------------LENOVO YOGA 13.4 - 13.3 AMD--------------- ",
          "checkbox": false,
          "active": true,
           "condition":"new","presta_categories": "3,53,306,9,234,347,839"
        },
        "LENOVO YOGA 14 I3": {
          "brand": "LENOVO",
          "template": "YOGA",
          "url": "------------------------LENOVO YOGA 14 I3----------------------",
          "checkbox": false,
          "active": true,
          "condition":"new","presta_categories": "3,53,104,10,4,377,839"
        },
        "LENOVO YOGA 14 I5": {
          "brand": "LENOVO",
          "template": "YOGA",
          "url": "------------------LENOVO YOGA 14 I5---------------",
          "checkbox": false,
          "active": true,
           "condition":"new","presta_categories": "3,53,104,10,5,378,839"
        },
        "LENOVO YOGA 14 I7": {
          "brand": "LENOVO",
          "template": "YOGA",
          "url": "https://www.visualdg.co.il/172330--%D7%A0%D7%99%D7%99%D7%93%D7%99-ThinkPad-Yoga/253274/253295",
          "checkbox": false,
          "active": true,
           "condition":"new","presta_categories": "3,53,104,10,6,379,839"
        },
        "LENOVO YOGA 14 I9": {
          "brand": "LENOVO",
          "template": "YOGA",
          "url": "----------------LENOVO YOGA 14 I9------------- ",
          "checkbox": false,
          "active": true,
           "condition":"new","presta_categories": "3,53,104,10,7,380,839"
        },
        "LENOVO YOGA 14 AMD": {
          "brand": "LENOVO",
          "template": "YOGA",
          "url": "----------------LENOVO YOGA 14 AMD------------- ",
          "checkbox": false,
          "active": true,
           "condition":"new","presta_categories": "3,53,104,10,234,381,839"
        },
    
        "LENOVO YOGA 15 I3": {
          "brand": "LENOVO",
          "template": "YOGA",
          "url": "----------------LENOVO YOGA 15 I3------------- ",
          "checkbox": false,
          "active": true,
           "condition":"new","presta_categories": "3,53,105,11,4,384,839"
        },
        "LENOVO YOGA 15 I5": {
          "brand": "LENOVO",
          "template": "YOGA",
          "url": "--------------LENOVO YOGA 15 I5--------------------",
          "checkbox": false,
          "active": true,
           "condition":"new","presta_categories": "3,53,105,11,5,385,839"
        },
        "LENOVO YOGA 15 I7": {
          "brand": "LENOVO",
          "template": "YOGA",
          "url": "--------------LENOVO YOGA 15 I7--------------------",
          "checkbox": false,
          "active": true,
           "condition":"new","presta_categories": "3,53,105,11,6,386,839"
        },
        "LENOVO YOGA 15 I9": {
          "brand": "LENOVO",
          "template": "YOGA",
          "url": "----------------LENOVO YOGA 15 I9------------- ",
          "checkbox": false,
          "active": true,
           "condition":"new","presta_categories": "3,53,105,11,7,387,839"
        },
        "LENOVO YOGA 15 AMD": {
          "brand": "LENOVO",
          "template": "YOGA",
          "url": "----------------LENOVO YOGA 15 AMD------------- ",
          "checkbox": false,
          "active": true,
           "condition":"new","presta_categories": "3,53,105,11,234,388,839"
        }
      }
    }
    """
    return json.loads(json_data)


def test_visualdg_data_load(visualdg_data):
    """
    Test that the fixture loads the data correctly.
    """
    assert isinstance(visualdg_data, dict)
    assert "scenarios" in visualdg_data
    assert isinstance(visualdg_data["scenarios"], dict)
    assert len(visualdg_data["scenarios"]) == 16

def test_scenario_keys_exist(visualdg_data):
    """
    Test that each scenario has the correct keys.
    """
    expected_keys = {"brand", "template", "url", "checkbox", "active", "condition","presta_categories"}
    for scenario_name, scenario_data in visualdg_data["scenarios"].items():
        assert set(scenario_data.keys()) == expected_keys, f"Scenario '{scenario_name}' does not have expected keys."


def test_scenario_values_types(visualdg_data):
    """
        Test that each scenario has the correct value types.
    """
    for scenario_name, scenario_data in visualdg_data["scenarios"].items():
        assert isinstance(scenario_data["brand"], str), f"Scenario '{scenario_name}' 'brand' is not a string."
        assert isinstance(scenario_data["template"], str), f"Scenario '{scenario_name}' 'template' is not a string."
        assert isinstance(scenario_data["url"], str), f"Scenario '{scenario_name}' 'url' is not a string."
        assert isinstance(scenario_data["checkbox"], bool), f"Scenario '{scenario_name}' 'checkbox' is not a boolean."
        assert isinstance(scenario_data["active"], bool), f"Scenario '{scenario_name}' 'active' is not a boolean."
        assert isinstance(scenario_data["condition"], str), f"Scenario '{scenario_name}' 'condition' is not a string."
        assert isinstance(scenario_data["presta_categories"], str), f"Scenario '{scenario_name}' 'presta_categories' is not a string."

def test_scenario_brand_values(visualdg_data):
    """
    Test that all brands are LENOVO.
    """
    for scenario_name, scenario_data in visualdg_data["scenarios"].items():
         assert scenario_data["brand"] == "LENOVO", f"Scenario '{scenario_name}' has unexpected brand value"


def test_scenario_template_values(visualdg_data):
    """
    Test that all templates are YOGA
    """
    for scenario_name, scenario_data in visualdg_data["scenarios"].items():
         assert scenario_data["template"] == "YOGA", f"Scenario '{scenario_name}' has unexpected template value"

def test_scenario_checkbox_values(visualdg_data):
     """
     Test that all checkbox values are false
     """
     for scenario_name, scenario_data in visualdg_data["scenarios"].items():
        assert scenario_data["checkbox"] == False, f"Scenario '{scenario_name}' has unexpected checkbox value"

def test_scenario_active_values(visualdg_data):
    """
    Test that all active values are true
    """
    for scenario_name, scenario_data in visualdg_data["scenarios"].items():
        assert scenario_data["active"] == True, f"Scenario '{scenario_name}' has unexpected active value"

def test_scenario_condition_values(visualdg_data):
     """
     Test that all condition values are new
     """
     for scenario_name, scenario_data in visualdg_data["scenarios"].items():
        assert scenario_data["condition"] == "new", f"Scenario '{scenario_name}' has unexpected condition value"

def test_presta_categories_format(visualdg_data):
    """
    Test that presta_categories is a string of comma-separated integers.
    """
    for scenario_name, scenario_data in visualdg_data["scenarios"].items():
        categories = scenario_data["presta_categories"].split(",")
        for cat in categories:
             assert cat.isdigit(), f"Scenario '{scenario_name}' presta_categories contains non-integer value: {cat}"
```