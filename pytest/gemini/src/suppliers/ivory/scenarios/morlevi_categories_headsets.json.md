```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def morlevi_categories_headsets_data():
    """Loads the JSON data for testing."""
    json_data = """
    {
      "scenarios": {
        "HEADSET_LOGITECH": {
          "brand": "LOGITECH",
          "template": "HEADSET_LOGITECH",
          "url": "https://www.morlevi.co.il/Cat/162?p_315=29&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
          "condition":"new",
           "presta_categories": { "template": { "logitech": "HEADPHONES" } }
        },
        "HEADSET_MICROSOFT": {
          "brand": "MICROSOFT",
          "template": "HEADSET_MICROSOFT",
          "url": "https://www.morlevi.co.il/Cat/162?p_315=42&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": {
            "template": { "microsoft": "HEADPHONES" }
          }
        },
        "HEADSET_ZALMAN": {
          "brand": "ZALMAN",
          "template": "HEADSET_ZALMAN",
          "url": "https://www.morlevi.co.il/Cat/162?p_315=34&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
          "condition":"new",
           "presta_categories": {
            "template": { "zalman": "HEADPHONES" }
          }
        },
        "HEADSET_CORSAIR": {
          "brand": "CORSAIR",
          "template": "HEADSET_CORSAIR",
          "url": "https://www.morlevi.co.il/Cat/162?p_315=20&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": {
            "template": { "corsair": "HEADPHONES" }
          }
        },
        "HEADSET_COOLER MASTER": {
          "brand": "COOLER MASTER",
          "template": "HEADSET_COOLER MASTER",
          "url": "https://www.morlevi.co.il/Cat/162?p_315=74&sort=datafloat2%2Cprice&keyword=",
          "checkbox": false,
          "active": true,
           "condition":"new",
          "presta_categories": {
            "template": { "cooler master": "HEADPHONES" }
          }
        }
      }
    }
    """
    return json.loads(json_data)

def test_scenarios_exist(morlevi_categories_headsets_data):
    """Checks if the 'scenarios' key exists in the JSON data."""
    assert "scenarios" in morlevi_categories_headsets_data, "The 'scenarios' key is missing from the JSON data."

def test_headset_logitech_data(morlevi_categories_headsets_data):
    """Checks the data for the 'HEADSET_LOGITECH' scenario."""
    logitech_data = morlevi_categories_headsets_data["scenarios"].get("HEADSET_LOGITECH")
    assert logitech_data is not None, "HEADSET_LOGITECH scenario is missing."
    assert logitech_data["brand"] == "LOGITECH"
    assert logitech_data["template"] == "HEADSET_LOGITECH"
    assert logitech_data["url"] == "https://www.morlevi.co.il/Cat/162?p_315=29&sort=datafloat2%2Cprice&keyword="
    assert logitech_data["checkbox"] == False
    assert logitech_data["active"] == True
    assert logitech_data["condition"] == "new"
    assert logitech_data["presta_categories"]["template"]["logitech"] == "HEADPHONES"

def test_headset_microsoft_data(morlevi_categories_headsets_data):
    """Checks the data for the 'HEADSET_MICROSOFT' scenario."""
    microsoft_data = morlevi_categories_headsets_data["scenarios"].get("HEADSET_MICROSOFT")
    assert microsoft_data is not None, "HEADSET_MICROSOFT scenario is missing."
    assert microsoft_data["brand"] == "MICROSOFT"
    assert microsoft_data["template"] == "HEADSET_MICROSOFT"
    assert microsoft_data["url"] == "https://www.morlevi.co.il/Cat/162?p_315=42&sort=datafloat2%2Cprice&keyword="
    assert microsoft_data["checkbox"] == False
    assert microsoft_data["active"] == True
    assert microsoft_data["condition"] == "new"
    assert microsoft_data["presta_categories"]["template"]["microsoft"] == "HEADPHONES"

def test_headset_zalman_data(morlevi_categories_headsets_data):
      """Checks the data for the 'HEADSET_ZALMAN' scenario."""
      zalman_data = morlevi_categories_headsets_data["scenarios"].get("HEADSET_ZALMAN")
      assert zalman_data is not None, "HEADSET_ZALMAN scenario is missing."
      assert zalman_data["brand"] == "ZALMAN"
      assert zalman_data["template"] == "HEADSET_ZALMAN"
      assert zalman_data["url"] == "https://www.morlevi.co.il/Cat/162?p_315=34&sort=datafloat2%2Cprice&keyword="
      assert zalman_data["checkbox"] == False
      assert zalman_data["active"] == True
      assert zalman_data["condition"] == "new"
      assert zalman_data["presta_categories"]["template"]["zalman"] == "HEADPHONES"


def test_headset_corsair_data(morlevi_categories_headsets_data):
    """Checks the data for the 'HEADSET_CORSAIR' scenario."""
    corsair_data = morlevi_categories_headsets_data["scenarios"].get("HEADSET_CORSAIR")
    assert corsair_data is not None, "HEADSET_CORSAIR scenario is missing."
    assert corsair_data["brand"] == "CORSAIR"
    assert corsair_data["template"] == "HEADSET_CORSAIR"
    assert corsair_data["url"] == "https://www.morlevi.co.il/Cat/162?p_315=20&sort=datafloat2%2Cprice&keyword="
    assert corsair_data["checkbox"] == False
    assert corsair_data["active"] == True
    assert corsair_data["condition"] == "new"
    assert corsair_data["presta_categories"]["template"]["corsair"] == "HEADPHONES"


def test_headset_cooler_master_data(morlevi_categories_headsets_data):
    """Checks the data for the 'HEADSET_COOLER MASTER' scenario."""
    cooler_master_data = morlevi_categories_headsets_data["scenarios"].get("HEADSET_COOLER MASTER")
    assert cooler_master_data is not None, "HEADSET_COOLER MASTER scenario is missing."
    assert cooler_master_data["brand"] == "COOLER MASTER"
    assert cooler_master_data["template"] == "HEADSET_COOLER MASTER"
    assert cooler_master_data["url"] == "https://www.morlevi.co.il/Cat/162?p_315=74&sort=datafloat2%2Cprice&keyword="
    assert cooler_master_data["checkbox"] == False
    assert cooler_master_data["active"] == True
    assert cooler_master_data["condition"] == "new"
    assert cooler_master_data["presta_categories"]["template"]["cooler master"] == "HEADPHONES"

def test_scenario_has_all_required_keys(morlevi_categories_headsets_data):
    """Checks if each scenario has all the required keys."""
    required_keys = ["brand", "template", "url", "checkbox", "active", "condition", "presta_categories"]
    for scenario_name, scenario_data in morlevi_categories_headsets_data["scenarios"].items():
        for key in required_keys:
            assert key in scenario_data, f"Scenario '{scenario_name}' is missing the key '{key}'."
def test_presta_categories_template_exists(morlevi_categories_headsets_data):
    """Checks if 'template' key exists in 'presta_categories' for each scenario."""
    for scenario_name, scenario_data in morlevi_categories_headsets_data["scenarios"].items():
      assert "template" in scenario_data["presta_categories"], f"Scenario '{scenario_name}' is missing 'template' key in 'presta_categories'."


def test_presta_categories_template_not_empty(morlevi_categories_headsets_data):
    """Checks if the 'template' dictionary within 'presta_categories' is not empty for each scenario."""
    for scenario_name, scenario_data in morlevi_categories_headsets_data["scenarios"].items():
         assert scenario_data["presta_categories"]["template"], f"The 'template' dictionary in 'presta_categories' for scenario '{scenario_name}' is empty."

def test_active_is_boolean(morlevi_categories_headsets_data):
    """Checks if the 'active' value is boolean"""
    for scenario_name, scenario_data in morlevi_categories_headsets_data["scenarios"].items():
        assert isinstance(scenario_data["active"], bool), f"The 'active' value in '{scenario_name}' is not a boolean."

def test_checkbox_is_boolean(morlevi_categories_headsets_data):
    """Checks if the 'checkbox' value is boolean"""
    for scenario_name, scenario_data in morlevi_categories_headsets_data["scenarios"].items():
        assert isinstance(scenario_data["checkbox"], bool), f"The 'checkbox' value in '{scenario_name}' is not a boolean."

def test_condition_is_string(morlevi_categories_headsets_data):
  """Checks if the 'condition' value is string"""
  for scenario_name, scenario_data in morlevi_categories_headsets_data["scenarios"].items():
      assert isinstance(scenario_data["condition"], str), f"The 'condition' value in '{scenario_name}' is not a string."
```