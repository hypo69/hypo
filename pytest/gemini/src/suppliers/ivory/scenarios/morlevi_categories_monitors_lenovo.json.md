```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def morlevi_data():
    """Loads the JSON data for testing."""
    file_path = 'hypotez/src/suppliers/ivory/scenarios/morlevi_categories_monitors_lenovo.json'
    with open(file_path, 'r') as f:
        return json.load(f)

def test_morlevi_data_structure(morlevi_data):
    """
    Test that the loaded JSON data has the expected structure.
    Checks if the top-level key 'scenarios' exists and is a dictionary.
    """
    assert "scenarios" in morlevi_data
    assert isinstance(morlevi_data["scenarios"], dict)

def test_morlevi_scenario_keys(morlevi_data):
    """
    Test that each scenario within the 'scenarios' dictionary has the correct keys.
    Verifies presence of 'brand', 'url', 'checkbox', 'active', 'condition', 'presta_categories'
    """
    for scenario_name, scenario_data in morlevi_data["scenarios"].items():
        assert "brand" in scenario_data
        assert "url" in scenario_data
        assert "checkbox" in scenario_data
        assert "active" in scenario_data
        assert "condition" in scenario_data
        assert "presta_categories" in scenario_data

def test_morlevi_scenario_brand_type(morlevi_data):
    """
    Test that the 'brand' value in each scenario is a string.
    """
    for scenario_name, scenario_data in morlevi_data["scenarios"].items():
         assert isinstance(scenario_data["brand"], str)

def test_morlevi_scenario_url_type(morlevi_data):
    """
    Test that the 'url' value in each scenario is a string.
    """
    for scenario_name, scenario_data in morlevi_data["scenarios"].items():
        assert isinstance(scenario_data["url"], str)

def test_morlevi_scenario_checkbox_type(morlevi_data):
    """
    Test that the 'checkbox' value in each scenario is a boolean.
    """
    for scenario_name, scenario_data in morlevi_data["scenarios"].items():
        assert isinstance(scenario_data["checkbox"], bool)

def test_morlevi_scenario_active_type(morlevi_data):
     """
     Test that the 'active' value in each scenario is a boolean.
     """
     for scenario_name, scenario_data in morlevi_data["scenarios"].items():
        assert isinstance(scenario_data["active"], bool)

def test_morlevi_scenario_condition_type(morlevi_data):
    """
    Test that the 'condition' value in each scenario is a string.
    """
    for scenario_name, scenario_data in morlevi_data["scenarios"].items():
         assert isinstance(scenario_data["condition"], str)

def test_morlevi_scenario_presta_categories_structure(morlevi_data):
    """
    Test that 'presta_categories' has a 'template' key and it's a dict
    """
    for scenario_name, scenario_data in morlevi_data["scenarios"].items():
        assert "template" in scenario_data["presta_categories"]
        assert isinstance(scenario_data["presta_categories"]["template"], dict)
        
def test_morlevi_scenario_presta_categories_template_content(morlevi_data):
    """
    Test that 'template' dictionary inside 'presta_categories' is not empty
    and contains string values
    """
    for scenario_name, scenario_data in morlevi_data["scenarios"].items():
       template = scenario_data["presta_categories"]["template"]
       assert template
       for key, value in template.items():
           assert isinstance(key, str)
           assert isinstance(value, str)
```