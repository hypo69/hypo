```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def laptop_data():
    """Loads the JSON data from the file."""
    file_path = 'hypotez/src/suppliers/visualdg/scenarios/visualdg_categories_laptops_lenovo_thinkpad_t.json'
    with open(file_path, 'r') as file:
        return json.load(file)

def test_laptop_data_structure(laptop_data):
    """Checks if the loaded data has the correct structure."""
    assert "scenarios" in laptop_data
    assert isinstance(laptop_data["scenarios"], dict)

def test_laptop_data_scenarios_not_empty(laptop_data):
    """Checks that the scenarios dictionary is not empty."""
    assert laptop_data["scenarios"]

def test_laptop_scenario_keys(laptop_data):
    """Checks if the first scenario contains the correct keys."""
    first_scenario_key = next(iter(laptop_data["scenarios"]))
    first_scenario = laptop_data["scenarios"][first_scenario_key]
    expected_keys = {"brand", "template", "url", "checkbox", "active", "condition","presta_categories"}
    assert set(first_scenario.keys()) == expected_keys

def test_laptop_scenario_brand_value(laptop_data):
    """Checks the brand value in the first scenario."""
    first_scenario_key = next(iter(laptop_data["scenarios"]))
    first_scenario = laptop_data["scenarios"][first_scenario_key]
    assert first_scenario["brand"] == "LENOVO"

def test_laptop_scenario_template_value(laptop_data):
        """Checks the template value in the first scenario."""
        first_scenario_key = next(iter(laptop_data["scenarios"]))
        first_scenario = laptop_data["scenarios"][first_scenario_key]
        assert first_scenario["template"] == "THINKPAD T"

def test_laptop_scenario_checkbox_type(laptop_data):
    """Checks that the checkbox value is a boolean in all scenarios."""
    for scenario in laptop_data["scenarios"].values():
        assert isinstance(scenario["checkbox"], bool)

def test_laptop_scenario_active_type(laptop_data):
    """Checks that the active value is a boolean in all scenarios."""
    for scenario in laptop_data["scenarios"].values():
        assert isinstance(scenario["active"], bool)

def test_laptop_scenario_condition_value(laptop_data):
    """Checks the condition value in all scenarios."""
    for scenario in laptop_data["scenarios"].values():
        assert scenario["condition"] == "new"
    
def test_laptop_scenario_presta_categories_type(laptop_data):
    """Checks if presta_categories is a string in all scenarios."""
    for scenario in laptop_data["scenarios"].values():
         assert isinstance(scenario["presta_categories"], str)
    
def test_laptop_scenario_url_not_empty(laptop_data):
    """Checks that the url value is not an empty string in all scenarios."""
    for scenario in laptop_data["scenarios"].values():
        assert scenario["url"] is not None
        assert isinstance(scenario["url"],str)
        
def test_multiple_scenarios_present(laptop_data):
    """Checks that there are more than one scenario present."""
    assert len(laptop_data["scenarios"]) > 1

def test_all_scenarios_have_data(laptop_data):
    """Checks that all scenarios have complete data."""
    for scenario_name, scenario_data in laptop_data["scenarios"].items():
       assert scenario_data is not None
       assert isinstance(scenario_data, dict)
       assert all(key in scenario_data for key in ["brand", "template", "url", "checkbox", "active","condition", "presta_categories"])

def test_scenario_names_are_strings(laptop_data):
    """Checks that all scenario names are strings."""
    for scenario_name in laptop_data["scenarios"].keys():
        assert isinstance(scenario_name,str)
```