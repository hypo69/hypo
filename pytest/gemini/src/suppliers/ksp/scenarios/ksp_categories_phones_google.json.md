```python
import pytest
import json

# Fixture for loading the json data
@pytest.fixture
def ksp_categories_data():
    """Loads the KSP categories data from the provided JSON."""
    json_data = """
    {
    "scenarios": {
        "Pixel 6 PRO": {
            "brand": "GOOGLE",
            "url": "https://ksp.co.il/web/cat/573..3887..31508",
            "checkbox": false,
            "active": true,
            "condition":"new",
            "presta_categories": {
              "template": { "google": "GOOGLE PIXEL 6 PRO" }
             }
        },
        "Pixel 6": {
            "brand": "GOOGLE",
            "url": "https://ksp.co.il/web/cat/573..3887..30356",
            "checkbox": false,
            "active": true,
           "condition":"new",
             "presta_categories": {
              "template": { "google": "GOOGLE PIXEL 6" }
            }
        },
         "Google Pixel 5a 5G": {
            "brand": "GOOGLE",
            "url": "https://ksp.co.il/web/cat/573..3887..28492",
            "checkbox": false,
            "active": true,
           "condition":"new",
             "presta_categories": {
              "template": { "google": "GOOGLE PIXEL 5A 5G" }
             }
         },
        "Google Pixel 6a": {
            "brand": "GOOGLE",
            "url": "https://ksp.co.il/web/cat/573..3887..28492",
            "checkbox": false,
            "active": true,
             "condition":"new",
            "presta_categories": {
              "template": { "google": "GOOGLE PIXEL 6A" }
             }
        }
      }
    }
    """
    return json.loads(json_data)

def test_ksp_categories_data_structure(ksp_categories_data):
    """Tests that the loaded data has the expected top-level structure."""
    assert "scenarios" in ksp_categories_data, "Top level 'scenarios' key is missing"
    assert isinstance(ksp_categories_data["scenarios"], dict), "'scenarios' should be a dictionary"

def test_ksp_categories_scenario_keys(ksp_categories_data):
    """Tests that the scenarios dictionary contains the expected keys."""
    scenarios = ksp_categories_data["scenarios"]
    expected_keys = ["Pixel 6 PRO", "Pixel 6", "Google Pixel 5a 5G", "Google Pixel 6a"]
    assert all(key in scenarios for key in expected_keys), "Not all expected scenario keys are present"

def test_ksp_categories_scenario_values(ksp_categories_data):
    """Tests the structure and values of the scenarios."""
    scenarios = ksp_categories_data["scenarios"]

    for scenario_name, scenario_data in scenarios.items():
        assert "brand" in scenario_data, f"'{scenario_name}': 'brand' key is missing"
        assert "url" in scenario_data, f"'{scenario_name}': 'url' key is missing"
        assert "checkbox" in scenario_data, f"'{scenario_name}': 'checkbox' key is missing"
        assert "active" in scenario_data, f"'{scenario_name}': 'active' key is missing"
        assert "condition" in scenario_data, f"'{scenario_name}': 'condition' key is missing"
        assert "presta_categories" in scenario_data, f"'{scenario_name}': 'presta_categories' key is missing"
        assert isinstance(scenario_data["presta_categories"], dict) ,f"'{scenario_name}': 'presta_categories' should be a dictionary"
        assert "template" in scenario_data["presta_categories"] ,f"'{scenario_name}': 'template' key is missing inside presta_categories"
        assert isinstance(scenario_data["presta_categories"]["template"], dict) ,f"'{scenario_name}': 'template' should be a dictionary"
        assert "google" in scenario_data["presta_categories"]["template"] ,f"'{scenario_name}': 'google' key is missing inside template"

        assert isinstance(scenario_data["brand"], str),f"'{scenario_name}': brand should be a string"
        assert isinstance(scenario_data["url"], str),f"'{scenario_name}': url should be a string"
        assert isinstance(scenario_data["checkbox"], bool),f"'{scenario_name}': checkbox should be a boolean"
        assert isinstance(scenario_data["active"], bool),f"'{scenario_name}': active should be a boolean"
        assert isinstance(scenario_data["condition"], str),f"'{scenario_name}': condition should be a string"

def test_ksp_categories_brand_values(ksp_categories_data):
  """Tests the values of brand for scenarios"""
  scenarios = ksp_categories_data["scenarios"]
  for scenario_name, scenario_data in scenarios.items():
    assert scenario_data["brand"] == "GOOGLE", f"'{scenario_name}': brand should be GOOGLE"

def test_ksp_categories_checkbox_values(ksp_categories_data):
  """Tests the values of checkbox for scenarios"""
  scenarios = ksp_categories_data["scenarios"]
  for scenario_name, scenario_data in scenarios.items():
    assert scenario_data["checkbox"] == False, f"'{scenario_name}': checkbox should be False"

def test_ksp_categories_active_values(ksp_categories_data):
    """Tests the values of active for scenarios"""
    scenarios = ksp_categories_data["scenarios"]
    for scenario_name, scenario_data in scenarios.items():
      assert scenario_data["active"] == True, f"'{scenario_name}': active should be True"

def test_ksp_categories_condition_values(ksp_categories_data):
  """Tests the values of condition for scenarios"""
  scenarios = ksp_categories_data["scenarios"]
  for scenario_name, scenario_data in scenarios.items():
    assert scenario_data["condition"] == "new", f"'{scenario_name}': condition should be new"

def test_ksp_categories_presta_categories_values(ksp_categories_data):
  """Tests the values inside presta_categories for scenarios"""
  scenarios = ksp_categories_data["scenarios"]
  expected_google_values = {
    "Pixel 6 PRO": "GOOGLE PIXEL 6 PRO",
    "Pixel 6": "GOOGLE PIXEL 6",
    "Google Pixel 5a 5G": "GOOGLE PIXEL 5A 5G",
    "Google Pixel 6a": "GOOGLE PIXEL 6A"
  }
  for scenario_name, scenario_data in scenarios.items():
      assert scenario_data["presta_categories"]["template"]["google"] == expected_google_values[scenario_name], \
          f"'{scenario_name}': google value inside presta_categories is incorrect"
```