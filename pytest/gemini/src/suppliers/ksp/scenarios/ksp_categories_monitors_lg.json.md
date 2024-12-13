```python
import pytest
import json

# Fixture to load the json data
@pytest.fixture
def ksp_categories_monitors_lg_data():
    """Loads the json data for testing."""
    json_data = """
    {
      "scenarios": {
        "LG monitors 21 - 22 inch": {
          "brand": "LG",
          "url": "https://ksp.co.il/web/cat/230..134..31308..194..195",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": {
            "template": { "lg": "PC MONITORS 21 - 22" }
          }
        },
        "LG monitors 22 -24 inch": {
          "brand": "LG",
          "url": "https://ksp.co.il/web/cat/230..134..1649..198",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": {
            "template": { "lg": "PC MONITORS 22 - 24" }
          }
        },
        "LG monitors 26 28 inch": {
          "brand": "LG",
          "url": "https://ksp.co.il/web/cat/230..137..4831..199..4784..2037",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": {
            "template": { "lg": "PC MONITORS 26 - 28" }
          }
        },
        "LG monitors about 29 inch": {
          "brand": "LG",
          "url": "https://ksp.co.il/web/cat/230..137..4831..199..4784..2037",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": {
            "template": { "lg": "PC MONITORS 26 - 28" }
          }
        },
        "LG monitors 31 32 inch": {
          "brand": "LG",
          "url": "https://ksp.co.il/web/cat/230..137..1948..200",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": {
            "template": { "lg": "PC MONITORS 31 - 33" }
          }
        },
        "LG monitors 34 inch": {
          "brand": "LG",
          "url": "https://ksp.co.il/web/cat/230..137..2129",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": {
            "template": { "lg": "PC MONITORS 34 - 38" }
          }
        },
        "LG monitors 48 inch": {
          "brand": "LG",
          "url": "https://ksp.co.il/web/cat/230..137..4831..199..4784..2037",
          "checkbox": false,
          "active": true,
          "condition":"new",
          "presta_categories": {
            "template": { "lg": "PC MONITORS 50" }
          }
        }
      }
    }
    """
    return json.loads(json_data)

def test_ksp_categories_monitors_lg_data_loaded(ksp_categories_monitors_lg_data):
    """
    Test that the json data is loaded correctly and is not empty.
    """
    assert ksp_categories_monitors_lg_data
    assert "scenarios" in ksp_categories_monitors_lg_data
    assert ksp_categories_monitors_lg_data["scenarios"]

def test_scenario_keys_exist(ksp_categories_monitors_lg_data):
    """
    Test that each scenario has the expected keys.
    """
    for scenario_name, scenario_data in ksp_categories_monitors_lg_data["scenarios"].items():
        assert "brand" in scenario_data
        assert "url" in scenario_data
        assert "checkbox" in scenario_data
        assert "active" in scenario_data
        assert "condition" in scenario_data
        assert "presta_categories" in scenario_data
        assert "template" in scenario_data["presta_categories"]

def test_scenario_values_correct_type(ksp_categories_monitors_lg_data):
     """
     Test that each value of the keys has the correct type.
     """
     for scenario_name, scenario_data in ksp_categories_monitors_lg_data["scenarios"].items():
        assert isinstance(scenario_data["brand"], str)
        assert isinstance(scenario_data["url"], str)
        assert isinstance(scenario_data["checkbox"], bool)
        assert isinstance(scenario_data["active"], bool)
        assert isinstance(scenario_data["condition"], str)
        assert isinstance(scenario_data["presta_categories"], dict)
        assert isinstance(scenario_data["presta_categories"]["template"], dict)

def test_scenario_brand_is_lg(ksp_categories_monitors_lg_data):
    """
    Test that all scenarios have the brand "LG".
    """
    for scenario_name, scenario_data in ksp_categories_monitors_lg_data["scenarios"].items():
        assert scenario_data["brand"] == "LG"
def test_scenario_checkbox_is_false(ksp_categories_monitors_lg_data):
    """
    Test that all scenarios have checkbox set to false
    """
    for scenario_name, scenario_data in ksp_categories_monitors_lg_data["scenarios"].items():
        assert scenario_data["checkbox"] == False

def test_scenario_active_is_true(ksp_categories_monitors_lg_data):
    """
    Test that all scenarios have active set to true
    """
    for scenario_name, scenario_data in ksp_categories_monitors_lg_data["scenarios"].items():
         assert scenario_data["active"] == True
def test_scenario_condition_is_new(ksp_categories_monitors_lg_data):
    """
    Test that all scenarios have the condition as new
    """
    for scenario_name, scenario_data in ksp_categories_monitors_lg_data["scenarios"].items():
        assert scenario_data["condition"] == "new"

def test_scenario_presta_categories_template_lg(ksp_categories_monitors_lg_data):
    """
    Test that presta_categories template has an 'lg' key and the value is a string.
    """
    for scenario_name, scenario_data in ksp_categories_monitors_lg_data["scenarios"].items():
        assert "lg" in scenario_data["presta_categories"]["template"]
        assert isinstance(scenario_data["presta_categories"]["template"]["lg"], str)

def test_scenario_url_is_valid(ksp_categories_monitors_lg_data):
    """
    Test that the url is a string starting with "https://"
    """
    for scenario_name, scenario_data in ksp_categories_monitors_lg_data["scenarios"].items():
        assert scenario_data["url"].startswith("https://")

```