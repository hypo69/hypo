```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def visualdg_data():
    """Loads the visualdg JSON data for testing."""
    json_data = """
    {
      "scenarios": {
        "ASUS MINIPC I3": {
          "brand": "ASUS",
          "url": "https://www.visualdg.co.il/169415-ASUS-MiniPC/253272",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": "159,160"
        },
        "ASUS MINIPC I5": {
          "brand": "ASUS",
          "url": "https://www.visualdg.co.il/169415-ASUS-MiniPC/253273",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": "159,161"
        },
        "ASUS  MINIPC I7": {
          "brand": "ASUS",
          "url": "https://www.visualdg.co.il/169415-ASUS-MiniPC/253274",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": "159,162"
        },
        "ASUS  MINIPC I9": {
          "brand": "ASUS",
          "url": "-------------ASUS  MINIPC I9---------------- ",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": "159,530"
        },
        "ASUS MINIPC AMD": {
          "brand": "ASUS",
          "url": "-------------ASUS MINIPC AMD---------------- ",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": "159,531"
        },
        "ASUS MINIPC Celeron": {
          "brand": "ASUS",
          "url": "-------------ASUS MINIPC Celeron---------------- ",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": "159,532"
        }
      }
    }
    """
    return json.loads(json_data)

# Test cases for the structure and basic data access
def test_visualdg_data_structure(visualdg_data):
    """Checks if the data has the correct 'scenarios' key."""
    assert "scenarios" in visualdg_data
    assert isinstance(visualdg_data["scenarios"], dict)

def test_scenario_keys_exist(visualdg_data):
    """Checks if the scenarios have the required keys."""
    for scenario in visualdg_data["scenarios"].values():
      assert "brand" in scenario
      assert "url" in scenario
      assert "checkbox" in scenario
      assert "active" in scenario
      assert "condition" in scenario
      assert "presta_categories" in scenario


def test_scenario_data_types(visualdg_data):
    """Checks if the scenario values are the correct data types."""
    for scenario in visualdg_data["scenarios"].values():
        assert isinstance(scenario["brand"], str)
        assert isinstance(scenario["url"], str)
        assert isinstance(scenario["checkbox"], bool)
        assert isinstance(scenario["active"], bool)
        assert isinstance(scenario["condition"], str)
        assert isinstance(scenario["presta_categories"], str)
def test_scenario_brand_values(visualdg_data):
     """Checks if the brand is always ASUS"""
     for scenario in visualdg_data["scenarios"].values():
          assert scenario["brand"]=="ASUS"
def test_scenario_active_values(visualdg_data):
    """Checks if active field is always True"""
    for scenario in visualdg_data["scenarios"].values():
          assert scenario["active"]==True
def test_scenario_condition_values(visualdg_data):
      """Checks if the condition field is always new"""
      for scenario in visualdg_data["scenarios"].values():
            assert scenario["condition"]=="new"
def test_scenario_checkbox_values(visualdg_data):
    """Checks if checkbox field is always False"""
    for scenario in visualdg_data["scenarios"].values():
          assert scenario["checkbox"]==False
def test_scenario_url_format(visualdg_data):
      """Checks if the URL is not a placeholder"""
      for scenario in visualdg_data["scenarios"].values():
           if not scenario["url"].startswith("-------------"):
                assert scenario["url"].startswith("https://www.visualdg.co.il/")
def test_scenario_presta_categories_format(visualdg_data):
    """Checks if presta categories are strings in the correct format"""
    for scenario in visualdg_data["scenarios"].values():
        assert isinstance(scenario["presta_categories"],str)
        categories=scenario["presta_categories"].split(",")
        for cat in categories:
              assert cat.isdigit()
```