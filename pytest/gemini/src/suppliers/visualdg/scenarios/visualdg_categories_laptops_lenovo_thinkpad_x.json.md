```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def scenario_data():
    """Provides the scenario data from the JSON file."""
    file_path = 'hypotez/src/suppliers/visualdg/scenarios/visualdg_categories_laptops_lenovo_thinkpad_x.json'
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data['scenarios']

# Test cases for the scenario data structure
def test_scenario_data_structure(scenario_data):
    """
    Test that the data loaded is a dictionary.
    Test that each scenario in the data is a dictionary.
    Test that all scenarios have the correct keys.
    """
    assert isinstance(scenario_data, dict), "The scenarios data should be a dictionary."
    
    required_keys = {"brand", "template", "url", "checkbox", "active", "condition", "presta_categories"}
    for scenario_name, scenario in scenario_data.items():
        assert isinstance(scenario, dict), f"Scenario '{scenario_name}' should be a dictionary."
        assert set(scenario.keys()) == required_keys, f"Scenario '{scenario_name}' does not have the required keys."

def test_scenario_brand_value(scenario_data):
     """Test that the 'brand' value is always 'LENOVO'."""
     for scenario_name, scenario in scenario_data.items():
         assert scenario["brand"] == "LENOVO", f"Scenario '{scenario_name}' brand is not 'LENOVO'"

def test_scenario_template_value(scenario_data):
     """Test that the 'template' value is always 'THINKPAD X'."""
     for scenario_name, scenario in scenario_data.items():
         assert scenario["template"] == "THINKPAD X", f"Scenario '{scenario_name}' template is not 'THINKPAD X'"

def test_scenario_url_not_empty(scenario_data):
    """Test that the 'url' value is not empty."""
    for scenario_name, scenario in scenario_data.items():
        assert scenario["url"] != "", f"Scenario '{scenario_name}' URL is empty."

def test_scenario_url_type(scenario_data):
     """Test that the 'url' value is a string."""
     for scenario_name, scenario in scenario_data.items():
        assert isinstance(scenario["url"],str) , f"Scenario '{scenario_name}' URL is not a string."

def test_scenario_checkbox_value(scenario_data):
    """Test that the 'checkbox' value is always false."""
    for scenario_name, scenario in scenario_data.items():
        assert scenario["checkbox"] == False, f"Scenario '{scenario_name}' checkbox is not False."

def test_scenario_active_value(scenario_data):
    """Test that the 'active' value is always True."""
    for scenario_name, scenario in scenario_data.items():
        assert scenario["active"] == True, f"Scenario '{scenario_name}' active is not True."

def test_scenario_condition_value(scenario_data):
    """Test that the 'condition' value is always 'new'."""
    for scenario_name, scenario in scenario_data.items():
         assert scenario["condition"] == "new", f"Scenario '{scenario_name}' condition is not 'new'."

def test_scenario_presta_categories_not_empty(scenario_data):
    """Test that the 'presta_categories' value is not empty."""
    for scenario_name, scenario in scenario_data.items():
         assert scenario["presta_categories"] != "", f"Scenario '{scenario_name}' presta_categories is empty."
         
def test_scenario_presta_categories_type(scenario_data):
    """Test that the 'presta_categories' value is a string."""
    for scenario_name, scenario in scenario_data.items():
         assert isinstance(scenario["presta_categories"], str), f"Scenario '{scenario_name}' presta_categories is not a string."
```