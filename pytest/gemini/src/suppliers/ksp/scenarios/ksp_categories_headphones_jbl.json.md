```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def ksp_headphones_data():
    """Provides the test data from the JSON file."""
    file_path = "hypotez/src/suppliers/ksp/scenarios/ksp_categories_headphones_jbl.json"
    with open(file_path, 'r') as file:
        return json.load(file)

# Test to check if the JSON data is loaded correctly
def test_ksp_headphones_data_loaded(ksp_headphones_data):
    """Checks if the fixture is loaded correctly."""
    assert isinstance(ksp_headphones_data, dict), "The loaded data should be a dictionary."
    assert "scenarios" in ksp_headphones_data, "The 'scenarios' key should be present."
    assert isinstance(ksp_headphones_data["scenarios"], dict), "The 'scenarios' value should be a dictionary."
    assert len(ksp_headphones_data["scenarios"]) > 0, "The 'scenarios' should not be empty."

# Test to verify the structure of each scenario
def test_ksp_headphones_scenario_structure(ksp_headphones_data):
    """Checks the structure of each scenario."""
    for scenario_name, scenario_data in ksp_headphones_data["scenarios"].items():
        assert isinstance(scenario_name, str), "Scenario name should be a string."
        assert isinstance(scenario_data, dict), f"Scenario '{scenario_name}' should be a dictionary."
        assert "brand" in scenario_data, f"Scenario '{scenario_name}' should contain 'brand'."
        assert "url" in scenario_data, f"Scenario '{scenario_name}' should contain 'url'."
        assert "checkbox" in scenario_data, f"Scenario '{scenario_name}' should contain 'checkbox'."
        assert "active" in scenario_data, f"Scenario '{scenario_name}' should contain 'active'."
        assert "condition" in scenario_data, f"Scenario '{scenario_name}' should contain 'condition'."
        assert "presta_categories" in scenario_data, f"Scenario '{scenario_name}' should contain 'presta_categories'."
        assert isinstance(scenario_data["presta_categories"], dict), f"Scenario '{scenario_name}' presta_categories should be a dictionary."
        assert "template" in scenario_data["presta_categories"], f"Scenario '{scenario_name}' presta_categories should contain 'template'."
        assert isinstance(scenario_data["presta_categories"]["template"], dict), f"Scenario '{scenario_name}' template should be a dictionary."
        assert len(scenario_data["presta_categories"]["template"]) == 1, f"Scenario '{scenario_name}' template should have only one key-value pair."
        
        
# Test to check for correct types of values in each scenario
def test_ksp_headphones_scenario_value_types(ksp_headphones_data):
    """Checks the value types in each scenario."""
    for scenario_name, scenario_data in ksp_headphones_data["scenarios"].items():
        assert isinstance(scenario_data["brand"], str), f"Scenario '{scenario_name}' brand should be a string."
        assert isinstance(scenario_data["url"], str), f"Scenario '{scenario_name}' url should be a string."
        assert isinstance(scenario_data["checkbox"], bool), f"Scenario '{scenario_name}' checkbox should be a boolean."
        assert isinstance(scenario_data["active"], bool), f"Scenario '{scenario_name}' active should be a boolean."
        assert isinstance(scenario_data["condition"], str), f"Scenario '{scenario_name}' condition should be a string."
        for key, value in scenario_data["presta_categories"]["template"].items():
           assert isinstance(key, str), f"Scenario '{scenario_name}' template key should be a string."
           assert isinstance(value, str), f"Scenario '{scenario_name}' template value should be a string."
           

# Test to check if URLs are valid
def test_ksp_headphones_scenario_valid_url(ksp_headphones_data):
     """Checks if the URLs in each scenario are strings and not empty."""
     for scenario_name, scenario_data in ksp_headphones_data["scenarios"].items():
          assert isinstance(scenario_data["url"], str), f"Scenario '{scenario_name}' URL should be a string."
          assert len(scenario_data["url"]) > 0, f"Scenario '{scenario_name}' URL should not be empty."
          assert scenario_data["url"].startswith("https://"), f"Scenario '{scenario_name}' URL should start with https://"
          
# Test to ensure 'condition' is always 'new'
def test_ksp_headphones_scenario_condition_is_new(ksp_headphones_data):
     """Checks if condition of each scenario is equal to new."""
     for scenario_name, scenario_data in ksp_headphones_data["scenarios"].items():
          assert scenario_data["condition"] == "new", f"Scenario '{scenario_name}' condition should be 'new'."
        
# Test that brand is always JBL
def test_ksp_headphones_scenario_brand_is_jbl(ksp_headphones_data):
     """Checks if the brand of each scenario is equal to jbl."""
     for scenario_name, scenario_data in ksp_headphones_data["scenarios"].items():
          assert scenario_data["brand"] == "JBL", f"Scenario '{scenario_name}' brand should be 'JBL'."

#Test if 'active' value is always True
def test_ksp_headphones_scenario_active_is_true(ksp_headphones_data):
     """Checks if the active key of each scenario is equal to true."""
     for scenario_name, scenario_data in ksp_headphones_data["scenarios"].items():
          assert scenario_data["active"] == True, f"Scenario '{scenario_name}' active should be True."

#Test if 'checkbox' value is always False
def test_ksp_headphones_scenario_checkbox_is_false(ksp_headphones_data):
     """Checks if the checkbox key of each scenario is equal to false."""
     for scenario_name, scenario_data in ksp_headphones_data["scenarios"].items():
          assert scenario_data["checkbox"] == False, f"Scenario '{scenario_name}' checkbox should be False."
```