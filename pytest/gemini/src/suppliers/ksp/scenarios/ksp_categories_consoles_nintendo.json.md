```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def ksp_nintendo_data():
    """Loads the JSON data for testing."""
    json_data = """
    {
      "scenarios": {
        "Nintendo Switch OLED": {
          "brand": "NINTENDO",
          "url": "https://ksp.co.il/web/cat/255..1304..28511",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": {
            "template": { "nintendo": "Nintendo Switch OLED" }
          }
        },
        "Nintendo Switch": {
          "brand": "NINTENDO",
          "url": "https://ksp.co.il/web/cat/255..1304..4173",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": {
            "template": { "nintendo": "Nintendo Switch OLED" }
          }
        },
        "Nintendo Switch Lite": {
          "brand": "NINTENDO",
          "url": "https://ksp.co.il/web/cat/255..1304..9674",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": {
            "template": { "nintendo": "Nintendo Switch Lite" }
          }
        },
        "Nintendo Classic": {
          "brand": "NINTENDO",
          "url": "https://ksp.co.il/web/cat/255..1304..5192",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": {
            "template": { "nintendo": "Nintendo Classic" }
          }
        }
      }
    }
    """
    return json.loads(json_data)


def test_ksp_nintendo_data_structure(ksp_nintendo_data):
    """Tests if the base structure of loaded json is correct"""
    assert "scenarios" in ksp_nintendo_data
    assert isinstance(ksp_nintendo_data["scenarios"], dict)

def test_ksp_nintendo_scenario_keys(ksp_nintendo_data):
  """Test keys for each scenario in json"""
  for scenario_name, scenario_data in ksp_nintendo_data["scenarios"].items():
    assert "brand" in scenario_data
    assert "url" in scenario_data
    assert "checkbox" in scenario_data
    assert "active" in scenario_data
    assert "condition" in scenario_data
    assert "presta_categories" in scenario_data
    assert "template" in scenario_data["presta_categories"]
    assert "nintendo" in scenario_data["presta_categories"]["template"]


def test_ksp_nintendo_scenario_values(ksp_nintendo_data):
    """Test the values for each key in the json scenarios"""
    for scenario_name, scenario_data in ksp_nintendo_data["scenarios"].items():
        assert scenario_data["brand"] == "NINTENDO"
        assert isinstance(scenario_data["url"], str)
        assert isinstance(scenario_data["checkbox"], bool)
        assert isinstance(scenario_data["active"], bool)
        assert scenario_data["condition"] == "new"
        assert isinstance(scenario_data["presta_categories"], dict)
        assert isinstance(scenario_data["presta_categories"]["template"], dict)
        assert isinstance(scenario_data["presta_categories"]["template"]["nintendo"],str)

def test_ksp_nintendo_specific_scenario_data(ksp_nintendo_data):
  """Test data in one specific scenario"""
  oled_data = ksp_nintendo_data["scenarios"]["Nintendo Switch OLED"]
  assert oled_data["brand"] == "NINTENDO"
  assert oled_data["url"] == "https://ksp.co.il/web/cat/255..1304..28511"
  assert oled_data["checkbox"] == False
  assert oled_data["active"] == True
  assert oled_data["condition"] == "new"
  assert oled_data["presta_categories"]["template"]["nintendo"] == "Nintendo Switch OLED"

def test_ksp_nintendo_empty_json():
    """Test with an empty json"""
    empty_json = {}
    with pytest.raises(KeyError):
        assert "scenarios" in empty_json

def test_ksp_nintendo_missing_key():
  """Test json with missing required key in scenario"""
  json_data = """
    {
      "scenarios": {
        "Nintendo Switch OLED": {
          "brand": "NINTENDO",
          "url": "https://ksp.co.il/web/cat/255..1304..28511",
          "checkbox": false,
          "active": true,
          "condition":"new"
        }
      }
    }
    """
  data = json.loads(json_data)
  with pytest.raises(KeyError):
        assert "presta_categories" in data["scenarios"]["Nintendo Switch OLED"]
```