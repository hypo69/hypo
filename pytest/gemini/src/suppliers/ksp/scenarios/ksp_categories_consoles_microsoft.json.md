```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def ksp_categories_consoles_microsoft_data():
    """Loads the JSON data for testing."""
    json_data = """
    {
      "scenarios": {
        "Xbox Series X": {
          "brand": "MICROSOFT",
          "url": "https://ksp.co.il/web/cat/219..255..15733..9335",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": {
            "template": { "microsoft": "Xbox Series X" }
          },
          "price_rule": 1
        },
        "Xbox Series S": {
          "brand": "MICROSOFT",
          "url": "https://ksp.co.il/web/cat/219..255..15734..9335",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": {
            "template": { "microsoft": "Xbox Series S" }
          },
          "price_rule": 1
        }
      }
    }
    """
    return json.loads(json_data)


def test_ksp_categories_consoles_microsoft_data_structure(ksp_categories_consoles_microsoft_data):
    """
    Test that the data is loaded as expected and the correct structure is present.
    """
    assert isinstance(ksp_categories_consoles_microsoft_data, dict)
    assert "scenarios" in ksp_categories_consoles_microsoft_data
    assert isinstance(ksp_categories_consoles_microsoft_data["scenarios"], dict)


def test_ksp_categories_consoles_microsoft_has_xbox_series_x(ksp_categories_consoles_microsoft_data):
    """
    Test that the 'Xbox Series X' scenario is present with the expected properties.
    """
    scenarios = ksp_categories_consoles_microsoft_data["scenarios"]
    assert "Xbox Series X" in scenarios
    xbox_series_x = scenarios["Xbox Series X"]
    assert xbox_series_x["brand"] == "MICROSOFT"
    assert xbox_series_x["url"] == "https://ksp.co.il/web/cat/219..255..15733..9335"
    assert xbox_series_x["checkbox"] == False
    assert xbox_series_x["active"] == True
    assert xbox_series_x["condition"] == "new"
    assert xbox_series_x["presta_categories"]["template"]["microsoft"] == "Xbox Series X"
    assert xbox_series_x["price_rule"] == 1


def test_ksp_categories_consoles_microsoft_has_xbox_series_s(ksp_categories_consoles_microsoft_data):
    """
    Test that the 'Xbox Series S' scenario is present with the expected properties.
    """
    scenarios = ksp_categories_consoles_microsoft_data["scenarios"]
    assert "Xbox Series S" in scenarios
    xbox_series_s = scenarios["Xbox Series S"]
    assert xbox_series_s["brand"] == "MICROSOFT"
    assert xbox_series_s["url"] == "https://ksp.co.il/web/cat/219..255..15734..9335"
    assert xbox_series_s["checkbox"] == False
    assert xbox_series_s["active"] == True
    assert xbox_series_s["condition"] == "new"
    assert xbox_series_s["presta_categories"]["template"]["microsoft"] == "Xbox Series S"
    assert xbox_series_s["price_rule"] == 1


def test_ksp_categories_consoles_microsoft_scenario_count(ksp_categories_consoles_microsoft_data):
  """
  Test that the correct number of scenarios is loaded.
  """
  scenarios = ksp_categories_consoles_microsoft_data["scenarios"]
  assert len(scenarios) == 2


def test_ksp_categories_consoles_microsoft_scenario_value_types(ksp_categories_consoles_microsoft_data):
    """
    Test that the value types within the scenario data are correct.
    """
    scenarios = ksp_categories_consoles_microsoft_data["scenarios"]
    for scenario_name, scenario_data in scenarios.items():
      assert isinstance(scenario_data["brand"], str)
      assert isinstance(scenario_data["url"], str)
      assert isinstance(scenario_data["checkbox"], bool)
      assert isinstance(scenario_data["active"], bool)
      assert isinstance(scenario_data["condition"], str)
      assert isinstance(scenario_data["presta_categories"], dict)
      assert isinstance(scenario_data["price_rule"], int)
      assert isinstance(scenario_data["presta_categories"]["template"],dict)
      assert isinstance(list(scenario_data["presta_categories"]["template"].values())[0], str)

def test_ksp_categories_consoles_microsoft_empty_scenarios():
    """
    Test that the data handles empty scenarios gracefully
    """
    empty_data = {"scenarios": {}}
    
    assert isinstance(empty_data, dict)
    assert "scenarios" in empty_data
    assert isinstance(empty_data["scenarios"], dict)
    assert len(empty_data["scenarios"]) == 0

def test_ksp_categories_consoles_microsoft_missing_key():
    """Test handling a case with missing key
    """
    
    missing_key_data = {"scenario" : {"test":{}}}
    assert "scenarios" not in missing_key_data
```