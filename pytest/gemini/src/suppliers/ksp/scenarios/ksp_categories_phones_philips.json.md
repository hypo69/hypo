```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def ksp_categories_phones_philips_data():
    """Loads the JSON data for testing."""
    json_data = """
    {
      "scenarios": {
        "E102A": {
          "brand": "PHILIPS",
          "url": "https://ksp.co.il/web/cat/272..573..506..30843",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": {}
        },
        "E209A": {
          "brand": "PHILIPS",
          "url": "https://ksp.co.il/web/cat/272..573..506..30843",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": {}
        }
      }
    }
    """
    return json.loads(json_data)


def test_ksp_categories_phones_philips_data_structure(ksp_categories_phones_philips_data):
    """
    Test if the loaded JSON data has the correct structure,
    specifically if it contains a 'scenarios' key.
    """
    assert "scenarios" in ksp_categories_phones_philips_data, "The JSON should contain a 'scenarios' key."


def test_ksp_categories_phones_philips_scenarios_not_empty(ksp_categories_phones_philips_data):
    """
    Test if the 'scenarios' dictionary within the JSON data is not empty.
    """
    assert ksp_categories_phones_philips_data["scenarios"], "The 'scenarios' dictionary should not be empty."


def test_ksp_categories_phones_philips_scenario_keys(ksp_categories_phones_philips_data):
    """
    Test that each scenario within the 'scenarios' dictionary has the expected keys:
    'brand', 'url', 'checkbox', 'active', 'condition', and 'presta_categories'.
    """
    for scenario_key, scenario_data in ksp_categories_phones_philips_data["scenarios"].items():
        assert "brand" in scenario_data, f"Scenario '{scenario_key}' should have a 'brand' key."
        assert "url" in scenario_data, f"Scenario '{scenario_key}' should have a 'url' key."
        assert "checkbox" in scenario_data, f"Scenario '{scenario_key}' should have a 'checkbox' key."
        assert "active" in scenario_data, f"Scenario '{scenario_key}' should have an 'active' key."
        assert "condition" in scenario_data, f"Scenario '{scenario_key}' should have a 'condition' key."
        assert "presta_categories" in scenario_data, f"Scenario '{scenario_key}' should have a 'presta_categories' key."


def test_ksp_categories_phones_philips_scenario_brand_values(ksp_categories_phones_philips_data):
    """
    Test that the 'brand' key in each scenario has the expected value "PHILIPS".
    """
    for scenario_key, scenario_data in ksp_categories_phones_philips_data["scenarios"].items():
      assert scenario_data["brand"] == "PHILIPS", f"Scenario '{scenario_key}' should have 'PHILIPS' as the brand."


def test_ksp_categories_phones_philips_scenario_url_valid(ksp_categories_phones_philips_data):
    """
    Test that the URL in each scenario starts with "https://ksp.co.il".
    """
    for scenario_key, scenario_data in ksp_categories_phones_philips_data["scenarios"].items():
        assert scenario_data["url"].startswith("https://ksp.co.il"), f"Scenario '{scenario_key}' URL should start with 'https://ksp.co.il'."


def test_ksp_categories_phones_philips_scenario_checkbox_type(ksp_categories_phones_philips_data):
    """
    Test that the 'checkbox' key in each scenario has a boolean type.
    """
    for scenario_key, scenario_data in ksp_categories_phones_philips_data["scenarios"].items():
      assert isinstance(scenario_data["checkbox"], bool), f"Scenario '{scenario_key}' 'checkbox' should be a boolean."


def test_ksp_categories_phones_philips_scenario_active_type(ksp_categories_phones_philips_data):
     """
     Test that the 'active' key in each scenario has a boolean type.
     """
     for scenario_key, scenario_data in ksp_categories_phones_philips_data["scenarios"].items():
         assert isinstance(scenario_data["active"], bool), f"Scenario '{scenario_key}' 'active' should be a boolean."

def test_ksp_categories_phones_philips_scenario_condition_value(ksp_categories_phones_philips_data):
    """
    Test that the 'condition' key in each scenario has the value 'new'.
    """
    for scenario_key, scenario_data in ksp_categories_phones_philips_data["scenarios"].items():
      assert scenario_data["condition"] == "new", f"Scenario '{scenario_key}' should have 'new' as the condition."

def test_ksp_categories_phones_philips_scenario_presta_categories_type(ksp_categories_phones_philips_data):
    """
    Test that 'presta_categories' key is a dictionary in each scenario.
    """
    for scenario_key, scenario_data in ksp_categories_phones_philips_data["scenarios"].items():
        assert isinstance(scenario_data["presta_categories"], dict), f"Scenario '{scenario_key}' 'presta_categories' should be a dictionary."


def test_ksp_categories_phones_philips_empty_presta_categories(ksp_categories_phones_philips_data):
    """
    Test that 'presta_categories' dictionary is empty in each scenario.
    """
    for scenario_key, scenario_data in ksp_categories_phones_philips_data["scenarios"].items():
        assert not scenario_data["presta_categories"], f"Scenario '{scenario_key}' 'presta_categories' should be empty."
```