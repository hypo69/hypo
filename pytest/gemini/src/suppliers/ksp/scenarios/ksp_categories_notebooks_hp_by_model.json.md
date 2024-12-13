```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def ksp_categories_data():
    """Loads the ksp categories data from the JSON file."""
    file_path = 'hypotez/src/suppliers/ksp/scenarios/ksp_categories_notebooks_hp_by_model.json'
    with open(file_path, 'r') as file:
        return json.load(file)

# Test cases for the 'scenarios' structure

def test_scenarios_structure_is_dict(ksp_categories_data):
    """Check if the 'scenarios' key is a dictionary."""
    assert isinstance(ksp_categories_data['scenarios'], dict)

def test_scenarios_are_not_empty(ksp_categories_data):
    """Check if the 'scenarios' dictionary is not empty."""
    assert ksp_categories_data['scenarios']

def test_scenario_keys_are_strings(ksp_categories_data):
    """Check if all keys in the scenarios dictionary are strings"""
    for key in ksp_categories_data['scenarios']:
        assert isinstance(key, str), f"Key {key} is not a string"

def test_scenario_values_are_dicts(ksp_categories_data):
    """Check if all values in the scenarios dictionary are dictionaries"""
    for value in ksp_categories_data['scenarios'].values():
        assert isinstance(value, dict), f"Value {value} is not a dict"

# Test cases for individual scenario entries

def test_scenario_has_required_keys(ksp_categories_data):
    """Check if each scenario has the required keys: brand, url, checkbox, active, condition, presta_categories"""
    required_keys = ['brand', 'url', 'checkbox', 'active', 'condition', 'presta_categories']
    for scenario in ksp_categories_data['scenarios'].values():
        for key in required_keys:
            assert key in scenario, f"Missing key {key} in scenario: {scenario}"

def test_scenario_brand_is_string(ksp_categories_data):
    """Check if the 'brand' value is a string"""
    for scenario in ksp_categories_data['scenarios'].values():
        assert isinstance(scenario['brand'], str), f"'brand' value {scenario['brand']} is not a string"

def test_scenario_url_is_string(ksp_categories_data):
   """Check if the 'url' value is a string"""
   for scenario in ksp_categories_data['scenarios'].values():
       assert isinstance(scenario['url'], str), f"'url' value {scenario['url']} is not a string"


def test_scenario_checkbox_is_boolean(ksp_categories_data):
    """Check if the 'checkbox' value is a boolean."""
    for scenario in ksp_categories_data['scenarios'].values():
        assert isinstance(scenario['checkbox'], bool), f"'checkbox' value {scenario['checkbox']} is not a boolean"

def test_scenario_active_is_boolean(ksp_categories_data):
    """Check if the 'active' value is a boolean."""
    for scenario in ksp_categories_data['scenarios'].values():
       assert isinstance(scenario['active'], bool), f"'active' value {scenario['active']} is not a boolean"

def test_scenario_condition_is_string(ksp_categories_data):
    """Check if the 'condition' value is a string."""
    for scenario in ksp_categories_data['scenarios'].values():
        assert isinstance(scenario['condition'], str), f"'condition' value {scenario['condition']} is not a string"

def test_scenario_presta_categories_is_dict(ksp_categories_data):
    """Check if the 'presta_categories' value is a dictionary."""
    for scenario in ksp_categories_data['scenarios'].values():
        assert isinstance(scenario['presta_categories'], dict), f"'presta_categories' value {scenario['presta_categories']} is not a dict"

# Test cases for 'presta_categories' structure

def test_presta_categories_has_template_key(ksp_categories_data):
    """Check if 'presta_categories' has the key 'template'"""
    for scenario in ksp_categories_data['scenarios'].values():
       assert 'template' in scenario['presta_categories'], f"'template' key missing in 'presta_categories': {scenario['presta_categories']}"

def test_presta_categories_template_is_dict(ksp_categories_data):
    """Check if the value of 'template' is a dictionary"""
    for scenario in ksp_categories_data['scenarios'].values():
        assert isinstance(scenario['presta_categories']['template'], dict), f"'template' value {scenario['presta_categories']['template']} is not a dictionary"

def test_presta_categories_template_has_hp_key(ksp_categories_data):
   """Check if 'template' has 'hp' key"""
   for scenario in ksp_categories_data['scenarios'].values():
        assert 'hp' in scenario['presta_categories']['template'], f"'hp' key missing in 'template': {scenario['presta_categories']['template']}"


def test_presta_categories_hp_is_list(ksp_categories_data):
    """Check if 'hp' key's value is a list"""
    for scenario in ksp_categories_data['scenarios'].values():
        assert isinstance(scenario['presta_categories']['template']['hp'], list), f"'hp' value {scenario['presta_categories']['template']['hp']} is not a list"

def test_presta_categories_hp_list_contains_strings(ksp_categories_data):
    """Check if 'hp' list contains only strings"""
    for scenario in ksp_categories_data['scenarios'].values():
        for item in scenario['presta_categories']['template']['hp']:
           assert isinstance(item, str), f"Item {item} in 'hp' list is not a string"


```