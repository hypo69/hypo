```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def ksp_categories_data():
    """Provides the JSON data for testing."""
    
    json_data = """
{
  "scenarios": {
    "MacBook Air 13 Late 2020": {
      "brand": "APPLE",
      "url": "https://ksp.co.il/web/cat/271..245..19037",
      "checkbox": false,
      "active": true,
      "condition":"new","presta_categories": {
        "3405": "GOOGLE PIXEL PRO",
        "3198": "CONSUMER ELECTRONICS",
        "3202": "computer,smartphone,gaming console,smart device",
        "6471": "Smartphones",
        "3403": "GOOGLE"
      }
    },
    "MacBook Pro 13 Late 2020": {
      "brand": "APPLE",
      "url": "https://ksp.co.il/web/cat/271..245..19085",
      "checkbox": false,
      "active": true,
      "condition":"new","presta_categories": {
        "3405": "GOOGLE PIXEL PRO",
        "3198": "CONSUMER ELECTRONICS",
        "3202": "computer,smartphone,gaming console,smart device",
        "6471": "Smartphones",
        "3403": "GOOGLE"
      }
    },
    "MacBook Pro 14 Late 2021": {
      "brand": "APPLE",
      "url": "https://ksp.co.il/web/cat/271..245..29598",
      "checkbox": false,
      "active": true,
      "condition":"new","presta_categories": {
        "3405": "GOOGLE PIXEL PRO",
        "3198": "CONSUMER ELECTRONICS",
        "3202": "computer,smartphone,gaming console,smart device",
        "6471": "Smartphones",
        "3403": "GOOGLE"
      }
    },
    "MacBook Pro 16 Late 2021": {
      "brand": "APPLE",
      "url": "https://ksp.co.il/web/cat/271..245..29608",
      "checkbox": false,
      "active": true,
      "condition":"new","presta_categories": {
        "3405": "GOOGLE PIXEL PRO",
        "3198": "CONSUMER ELECTRONICS",
        "3202": "computer,smartphone,gaming console,smart device",
        "6471": "Smartphones",
        "3403": "GOOGLE"
      }
    }
  }
}
"""
    return json.loads(json_data)

def test_ksp_categories_data_structure(ksp_categories_data):
    """
    Test that the loaded data has the correct top-level structure (i.e., 'scenarios' key).
    """
    assert "scenarios" in ksp_categories_data, "Top-level key 'scenarios' is missing."
    assert isinstance(ksp_categories_data["scenarios"], dict), "'scenarios' should be a dictionary."

def test_ksp_categories_scenario_keys(ksp_categories_data):
    """
    Test that each scenario has the correct keys and are of the right type
    """
    for scenario_name, scenario_data in ksp_categories_data["scenarios"].items():
        assert isinstance(scenario_name, str), "Scenario name should be a string"
        assert isinstance(scenario_data, dict), "Scenario data should be a dictionary"
        assert "brand" in scenario_data, f"Scenario '{scenario_name}' missing 'brand' key"
        assert isinstance(scenario_data["brand"], str), f"'brand' should be a string in scenario '{scenario_name}'"
        assert "url" in scenario_data, f"Scenario '{scenario_name}' missing 'url' key"
        assert isinstance(scenario_data["url"], str), f"'url' should be a string in scenario '{scenario_name}'"
        assert "checkbox" in scenario_data, f"Scenario '{scenario_name}' missing 'checkbox' key"
        assert isinstance(scenario_data["checkbox"], bool), f"'checkbox' should be a bool in scenario '{scenario_name}'"
        assert "active" in scenario_data, f"Scenario '{scenario_name}' missing 'active' key"
        assert isinstance(scenario_data["active"], bool), f"'active' should be a bool in scenario '{scenario_name}'"
        assert "condition" in scenario_data, f"Scenario '{scenario_name}' missing 'condition' key"
        assert isinstance(scenario_data["condition"], str), f"'condition' should be a string in scenario '{scenario_name}'"
        assert "presta_categories" in scenario_data, f"Scenario '{scenario_name}' missing 'presta_categories' key"
        assert isinstance(scenario_data["presta_categories"], dict), f"'presta_categories' should be a dict in scenario '{scenario_name}'"
    
def test_ksp_categories_presta_categories_content(ksp_categories_data):
    """
    Test the content of the presta categories for each scenario.
    """
    for scenario_name, scenario_data in ksp_categories_data["scenarios"].items():
       presta_categories = scenario_data["presta_categories"]
       for key, value in presta_categories.items():
           assert isinstance(key, str), f"Key in 'presta_categories' should be a string in scenario '{scenario_name}'"
           assert isinstance(value, str), f"Value in 'presta_categories' should be a string in scenario '{scenario_name}'"
           
def test_ksp_categories_empty_scenarios(ksp_categories_data):
    """
    Test that the json data has at least one entry in scenarios.
    """
    assert ksp_categories_data["scenarios"], "There should be at least one entry in 'scenarios'."
    

def test_ksp_categories_valid_url(ksp_categories_data):
    """
    Test that all urls start with "https://ksp.co.il/web/cat/"
    """
    for scenario_name, scenario_data in ksp_categories_data["scenarios"].items():
        url = scenario_data["url"]
        assert url.startswith("https://ksp.co.il/web/cat/"), f"URL '{url}' in scenario '{scenario_name}' does not start with 'https://ksp.co.il/web/cat/'"

def test_ksp_categories_active_boolean(ksp_categories_data):
    """
    Test that all 'active' values are boolean
    """
    for scenario_name, scenario_data in ksp_categories_data["scenarios"].items():
        assert isinstance(scenario_data["active"], bool), f"'active' should be a boolean value in scenario '{scenario_name}'"

def test_ksp_categories_checkbox_boolean(ksp_categories_data):
    """
    Test that all 'checkbox' values are boolean
    """
    for scenario_name, scenario_data in ksp_categories_data["scenarios"].items():
        assert isinstance(scenario_data["checkbox"], bool), f"'checkbox' should be a boolean value in scenario '{scenario_name}'"


def test_ksp_categories_condition_new(ksp_categories_data):
        """
        Test that all 'condition' values are equal to new
        """
        for scenario_name, scenario_data in ksp_categories_data["scenarios"].items():
            assert scenario_data["condition"] == "new" , f"Condition must be equal to new in scenario '{scenario_name}'"
```