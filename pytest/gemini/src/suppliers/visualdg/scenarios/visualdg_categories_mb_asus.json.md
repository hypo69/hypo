```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def visualdg_data():
    """Provides test data loaded from the JSON file."""
    file_path = 'hypotez/src/suppliers/visualdg/scenarios/visualdg_categories_mb_asus.json'
    with open(file_path, 'r') as file:
        return json.load(file)

def test_scenario_keys_exist(visualdg_data):
    """Checks if the 'scenarios' key exists in the loaded JSON."""
    assert 'scenarios' in visualdg_data, "The 'scenarios' key should exist in the JSON data."

def test_scenarios_not_empty(visualdg_data):
      """Checks if the 'scenarios' dictionary is not empty."""
      assert visualdg_data['scenarios'], "The 'scenarios' dictionary should not be empty."

def test_motherboard_brand_asus(visualdg_data):
    """Checks if all scenarios have the correct brand 'ASUS'."""
    for scenario_name, scenario_data in visualdg_data['scenarios'].items():
        assert scenario_data['brand'] == "ASUS", f"Scenario '{scenario_name}' should have brand 'ASUS'."

def test_motherboard_url_exists(visualdg_data):
    """Checks if all scenarios have a URL."""
    for scenario_name, scenario_data in visualdg_data['scenarios'].items():
        assert 'url' in scenario_data, f"Scenario '{scenario_name}' should have a URL."

def test_motherboard_checkbox_is_false(visualdg_data):
    """Checks if all scenarios have 'checkbox' set to false."""
    for scenario_name, scenario_data in visualdg_data['scenarios'].items():
        assert scenario_data['checkbox'] == False, f"Scenario '{scenario_name}' should have 'checkbox' set to false."


def test_motherboard_active_is_true(visualdg_data):
    """Checks if all scenarios have 'active' set to true."""
    for scenario_name, scenario_data in visualdg_data['scenarios'].items():
        assert scenario_data['active'] == True, f"Scenario '{scenario_name}' should have 'active' set to true."

def test_motherboard_condition_is_new(visualdg_data):
    """Checks if all scenarios have 'condition' set to 'new'."""
    for scenario_name, scenario_data in visualdg_data['scenarios'].items():
        assert scenario_data['condition'] == 'new', f"Scenario '{scenario_name}' should have 'condition' set to 'new'."

def test_presta_categories_exist(visualdg_data):
    """Checks if all scenarios have 'presta_categories' key."""
    for scenario_name, scenario_data in visualdg_data['scenarios'].items():
        assert 'presta_categories' in scenario_data, f"Scenario '{scenario_name}' should have 'presta_categories' key."

def test_presta_categories_not_empty(visualdg_data):
    """Checks if all 'presta_categories' values are not empty strings."""
    for scenario_name, scenario_data in visualdg_data['scenarios'].items():
      assert scenario_data['presta_categories'] , f"Scenario '{scenario_name}' 'presta_categories' value should not be empty."
    
def test_presta_categories_is_string(visualdg_data):
     """Checks if all 'presta_categories' values are strings."""
     for scenario_name, scenario_data in visualdg_data['scenarios'].items():
         assert isinstance(scenario_data['presta_categories'], str), f"Scenario '{scenario_name}' 'presta_categories' value should be a string."
```