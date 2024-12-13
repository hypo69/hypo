```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def scenarios_data():
    """Loads the JSON data for testing."""
    json_data = """
    {
      "scenarios": {
        "LENOVO THINKPAD L 13.4 - 13.3 I3": {
          "brand": "LENOVO",
          "template": "THINKPAD L",
          "url": "-----------------LENOVO 13.4 - 13.3 I3-------------r ",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": "3,53,306,9,4,370,838"
        },
        "LENOVO THINKPAD L 13.4 - 13.3 I5": {
          "brand": "LENOVO",
          "template": "THINKPAD L",
          "url": "https://www.visualdg.co.il/172321--%D7%A0%D7%99%D7%99%D7%93%D7%99-ThinkPad-L-/253273/253294",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": "3,53,306,9,5,371,838"
        },
        "LENOVO THINKPAD L 13.4 - 13.3 I7": {
          "brand": "LENOVO",
          "template": "THINKPAD L",
          "url": "https://www.visualdg.co.il/172321--%D7%A0%D7%99%D7%99%D7%93%D7%99-ThinkPad-L-/253274/253294",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": "3,53,306,9,6,372,838"
        },
        "LENOVO THINKPAD L 13.4 - 13.3 I9": {
          "brand": "LENOVO",
          "template": "THINKPAD L",
          "url": "----------------LENOVO THINKPAD L 13.4 - 13.3 I9------------- ",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": "3,53,306,9,7,373,838"
        },
        "LENOVO THINKPAD L 13.4 - 13.3 AMD": {
          "brand": "LENOVO",
          "template": "THINKPAD L",
          "url": "--------------LENOVO THINKPAD L 13.4 - 13.3 AMD--------------- ",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": "3,53,306,9,234,347,838"
        },
        "LENOVO THINKPAD L 14 I3": {
          "brand": "LENOVO",
          "template": "THINKPAD L",
          "url": "------------------------LENOVO THINKPAD L 14 I3----------------------",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": "3,53,104,10,4,377,838"
        },
        "LENOVO THINKPAD L 14 I5": {
          "brand": "LENOVO",
          "template": "THINKPAD L",
          "url": "https://www.visualdg.co.il/172321--%D7%A0%D7%99%D7%99%D7%93%D7%99-ThinkPad-L-/253273/253295",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": "3,53,104,10,5,378,838"
        },
        "LENOVO THINKPAD L 14 I7": {
          "brand": "LENOVO",
          "template": "THINKPAD L",
          "url": "https://www.visualdg.co.il/172321--%D7%A0%D7%99%D7%99%D7%93%D7%99-ThinkPad-L-/253274/253295",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": "3,53,104,10,6,379,838"
        },
        "LENOVO THINKPAD L 14 I9": {
          "brand": "LENOVO",
          "template": "THINKPAD L",
          "url": "----------------LENOVO THINKPAD L 14 I9------------- ",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": "3,53,104,10,7,380,838"
        },
        "LENOVO THINKPAD L 14 AMD": {
          "brand": "LENOVO",
          "template": "THINKPAD L",
          "url": "----------------LENOVO THINKPAD L 14 AMD------------- ",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": "3,53,104,10,234,381,838"
        },
        "LENOVO THINKPAD L 15 I3": {
          "brand": "LENOVO",
          "template": "THINKPAD L",
          "url": "----------------LENOVO THINKPAD L 15 I3------------- ",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": "3,53,105,11,4,384,838"
        },
        "LENOVO THINKPAD L 15 I5": {
          "brand": "LENOVO",
          "template": "THINKPAD L",
          "url": "https://www.visualdg.co.il/172321--%D7%A0%D7%99%D7%99%D7%93%D7%99-ThinkPad-L-/253273/253296",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": "3,53,105,11,5,385,838"
        },
        "LENOVO THINKPAD L 15 I7": {
          "brand": "LENOVO",
          "template": "THINKPAD L",
          "url": "-----------------THINKPAD L 15 I7----------------",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": "3,53,105,11,6,386,838"
        },
         "LENOVO THINKPAD L 15 I9": {
          "brand": "LENOVO",
          "template": "THINKPAD L",
          "url": "----------------LENOVO THINKPAD L 15 I9------------- ",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": "3,53,105,11,7,387,838"
        },
        "LENOVO THINKPAD L 15 AMD": {
          "brand": "LENOVO",
          "template": "THINKPAD L",
          "url": "----------------LENOVO THINKPAD L 15 AMD------------- ",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": "3,53,105,11,234,388,838"
        }
      }
    }
    """
    return json.loads(json_data)

def test_scenarios_data_loaded(scenarios_data):
    """Verify that the fixture loads the data correctly."""
    assert scenarios_data is not None
    assert isinstance(scenarios_data, dict)
    assert "scenarios" in scenarios_data


def test_scenario_keys_present(scenarios_data):
    """Verify that all scenarios have the correct keys."""
    for scenario_name, scenario_data in scenarios_data["scenarios"].items():
      assert "brand" in scenario_data
      assert "template" in scenario_data
      assert "url" in scenario_data
      assert "checkbox" in scenario_data
      assert "active" in scenario_data
      assert "condition" in scenario_data
      assert "presta_categories" in scenario_data



def test_scenario_brand_values(scenarios_data):
    """Verify that all brands are LENOVO."""
    for scenario_data in scenarios_data["scenarios"].values():
        assert scenario_data["brand"] == "LENOVO"

def test_scenario_template_values(scenarios_data):
    """Verify that all templates are THINKPAD L."""
    for scenario_data in scenarios_data["scenarios"].values():
        assert scenario_data["template"] == "THINKPAD L"

def test_scenario_checkbox_values(scenarios_data):
    """Verify that all checkbox values are False."""
    for scenario_data in scenarios_data["scenarios"].values():
        assert scenario_data["checkbox"] is False

def test_scenario_active_values(scenarios_data):
    """Verify that all active values are True."""
    for scenario_data in scenarios_data["scenarios"].values():
         assert scenario_data["active"] is True

def test_scenario_condition_values(scenarios_data):
    """Verify that all conditions are new."""
    for scenario_data in scenarios_data["scenarios"].values():
        assert scenario_data["condition"] == "new"


def test_presta_categories_format(scenarios_data):
    """Verify that presta_categories are strings of comma-separated integers."""
    for scenario_data in scenarios_data["scenarios"].values():
        categories = scenario_data["presta_categories"]
        assert isinstance(categories, str)
        for cat_id in categories.split(','):
            assert cat_id.isdigit(), f"Category ID '{cat_id}' is not a digit in {categories}"

def test_url_values_not_empty(scenarios_data):
    """Verify that all URLs are not empty strings."""
    for scenario_data in scenarios_data["scenarios"].values():
        assert scenario_data["url"].strip() != ""


def test_specific_scenario_data(scenarios_data):
    """Verify the data of a specific scenario."""
    specific_scenario = scenarios_data["scenarios"].get("LENOVO THINKPAD L 14 I5")
    assert specific_scenario is not None
    assert specific_scenario["brand"] == "LENOVO"
    assert specific_scenario["template"] == "THINKPAD L"
    assert specific_scenario["url"] == "https://www.visualdg.co.il/172321--%D7%A0%D7%99%D7%99%D7%93%D7%99-ThinkPad-L-/253273/253295"
    assert specific_scenario["checkbox"] is False
    assert specific_scenario["active"] is True
    assert specific_scenario["condition"] == "new"
    assert specific_scenario["presta_categories"] == "3,53,104,10,5,378,838"

def test_empty_scenarios(scenarios_data):
    """Test that the 'scenarios' is not empty."""
    assert scenarios_data["scenarios"]
```