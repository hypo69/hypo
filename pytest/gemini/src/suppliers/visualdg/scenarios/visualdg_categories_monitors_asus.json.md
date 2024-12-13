```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def json_data():
    """Loads the JSON data from the provided string."""
    json_string = """
{
  "scenarios": {
    "ASUS 18": {
      "brand": "ASUS",
      "url": "https://www.visualdg.co.il/169413-%D7%9E%D7%A1%D7%9B%D7%99-%D7%9E%D7%97%D7%A9%D7%91-ASUS/253029",
      "checkbox": false,
      "active": true,
      "condition":"new","presta_categories": "127,241,535"
    },
    "ASUS 19.5": {
      "brand": "ASUS",
      "url": "https://www.visualdg.co.il/169413-%D7%9E%D7%A1%D7%9B%D7%99-%D7%9E%D7%97%D7%A9%D7%91-ASUS/253029",
      "checkbox": false,
      "active": true,
      "condition":"new","presta_categories": "127,241,535"
    },
    "ASUS 22": {
      "brand": "ASUS",
      "url": "https://www.visualdg.co.il/169413-%D7%9E%D7%A1%D7%9B%D7%99-%D7%9E%D7%97%D7%A9%D7%91-ASUS/253020",
      "checkbox": false,
      "active": true,
      "condition":"new","presta_categories": "127,128,535"
    },
    "ASUS 24-25": {
      "brand": "ASUS",
      "url": "https://www.visualdg.co.il/169413-%D7%9E%D7%A1%D7%9B%D7%99-%D7%9E%D7%97%D7%A9%D7%91-ASUS/253024",
      "checkbox": false,
      "active": true,
      "condition":"new","presta_categories": "127,535"
    
    },
    "ASUS 27-29": {
      "brand": "ASUS",
      "url": "https://www.visualdg.co.il/169413-%D7%9E%D7%A1%D7%9B%D7%99-%D7%9E%D7%97%D7%A9%D7%91-ASUS/253022",
      "checkbox": false,
      "active": true,
      "condition":"new","presta_categories": "127,535"
    },
    "ASUS 32": {
      "brand": "ASUS",
      "url": "https://www.visualdg.co.il/169413-%D7%9E%D7%A1%D7%9B%D7%99-%D7%9E%D7%97%D7%A9%D7%91-ASUS/253023",
      "checkbox": false,
      "active": true,
      "condition":"new","presta_categories": "127,131,535"
    },
    "ASUS 34": {
      "brand": "ASUS",
      "url": " --------------------------  ASUS 34 -----------------------------------",
      "checkbox": false,
      "active": true,
      "condition":"new","presta_categories": "127,132,535"
    },
    "ASUS 49": {
      "brand": "ASUS",
      "url": "https://www.visualdg.co.il/169413-%D7%9E%D7%A1%D7%9B%D7%99-%D7%9E%D7%97%D7%A9%D7%91-ASUS/253038",
      "checkbox": false,
      "active": true,
      "condition":"new","presta_categories": "127,133,535"
    }
  }
}
    """
    return json.loads(json_string)

def test_json_data_loaded(json_data):
    """Test if the JSON data is loaded correctly."""
    assert json_data is not None
    assert isinstance(json_data, dict)
    assert "scenarios" in json_data


def test_scenarios_exist(json_data):
    """Test if the 'scenarios' key exists and is a dictionary."""
    assert "scenarios" in json_data
    assert isinstance(json_data["scenarios"], dict)

def test_scenario_asus_18_exists(json_data):
    """Test if a specific scenario 'ASUS 18' exists and has the correct data."""
    scenarios = json_data["scenarios"]
    assert "ASUS 18" in scenarios
    asus_18 = scenarios["ASUS 18"]
    assert asus_18["brand"] == "ASUS"
    assert asus_18["url"] == "https://www.visualdg.co.il/169413-%D7%9E%D7%A1%D7%9B%D7%99-%D7%9E%D7%97%D7%A9%D7%91-ASUS/253029"
    assert asus_18["checkbox"] == False
    assert asus_18["active"] == True
    assert asus_18["condition"] == "new"
    assert asus_18["presta_categories"] == "127,241,535"

def test_scenario_asus_34_url_edge_case(json_data):
    """Test if the scenario 'ASUS 34' handles URLs with unusual formatting"""
    scenarios = json_data["scenarios"]
    assert "ASUS 34" in scenarios
    asus_34 = scenarios["ASUS 34"]
    assert asus_34["url"] == " --------------------------  ASUS 34 -----------------------------------"

def test_all_scenarios_have_required_keys(json_data):
    """Test that each scenario has all the required keys"""
    scenarios = json_data["scenarios"]
    required_keys = ["brand", "url", "checkbox", "active", "condition", "presta_categories"]
    for scenario_name, scenario_data in scenarios.items():
        for key in required_keys:
            assert key in scenario_data, f"Scenario '{scenario_name}' is missing key: '{key}'"

def test_scenarios_values_data_types(json_data):
    """Test that the values of each scenario have the correct data type"""
    scenarios = json_data["scenarios"]
    for scenario_name, scenario_data in scenarios.items():
        assert isinstance(scenario_data["brand"], str), f"Scenario '{scenario_name}' brand is not a string"
        assert isinstance(scenario_data["url"], str), f"Scenario '{scenario_name}' url is not a string"
        assert isinstance(scenario_data["checkbox"], bool), f"Scenario '{scenario_name}' checkbox is not a boolean"
        assert isinstance(scenario_data["active"], bool), f"Scenario '{scenario_name}' active is not a boolean"
        assert isinstance(scenario_data["condition"], str), f"Scenario '{scenario_name}' condition is not a string"
        assert isinstance(scenario_data["presta_categories"], str), f"Scenario '{scenario_name}' presta_categories is not a string"
```